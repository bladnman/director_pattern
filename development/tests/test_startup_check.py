"""First-reply local evidence boundaries; actual actor traces remain separate."""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest

STARTER=Path(__file__).resolve().parents[2]/'pattern/starter'
spec=importlib.util.spec_from_file_location('badge_installer',STARTER/'install.py')
installer=importlib.util.module_from_spec(spec);spec.loader.exec_module(installer)


class StartupCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.project=Path(self.temp.name).resolve()/'project'
        installer.operation('install',self.project)
        self.root=self.project/'.director'

    def receipt(self):return json.loads((self.root/'install.json').read_bytes())
    def save_receipt(self,value): (self.root/'install.json').write_text(json.dumps(value)+'\n')
    def tree(self):return {str(p.relative_to(self.project)):p.read_bytes() for p in self.project.rglob('*') if p.is_file()}
    def run_check(self,*args,ok=True):
        r=subprocess.run([sys.executable,'-B',str(self.root/'startup_check.py'),*args],cwd=self.project,text=True,capture_output=True)
        self.assertEqual(r.returncode==0,ok,r.stdout+r.stderr)
        self.assertLessEqual(len(r.stdout.encode()),4097)
        self.assertNotIn('Traceback',r.stderr)
        return json.loads(r.stdout)

    def test_fresh_check_is_readonly_and_does_not_claim_consumption_role_or_ledger(self):
        before=self.tree();r=self.run_check()
        self.assertEqual(r['status'],'evidence_matched')
        self.assertEqual(len(r['checked_paths']),5)
        self.assertEqual(r['backend']['record_mode'],'tracked')
        self.assertTrue(r['actor_must_confirm'])
        self.assertIn('ledger/history integrity',r['not_proved'])
        self.assertEqual(before,self.tree())

    def test_missing_provenance_and_corrupt_selected_route_block_without_writes(self):
        original=self.receipt();bad=json.loads(json.dumps(original));bad.pop('source');self.save_receipt(bad)
        before=self.tree();r=self.run_check(ok=False);self.assertIn('source URL',r['gap']);self.assertEqual(before,self.tree())
        self.save_receipt(original);(self.root/'DIRECTOR.md').write_text('changed local route')
        r=self.run_check(ok=False);self.assertIn('baseline mismatch',r['gap'])

    def test_mature_map_list_and_external_config_header_need_all_selected_guards(self):
        receipt=self.receipt();receipt['managed_files']=[{'path':p,'installed_sha256':h} for p,h in receipt.pop('managed').items()]
        self.save_receipt(receipt)
        (self.project/'.producer').mkdir();config=json.loads((self.root/'config.json').read_bytes());config['request_store']['format']='request-bundles'
        (self.project/'.producer/config.json').write_text(json.dumps(config))
        self.assertEqual(self.run_check('--config','.producer/config.json')['status'],'evidence_matched')
        (self.project/'shared.md').write_text('actual shared authority')
        r=self.run_check('--config','.producer/config.json','--guard','shared.md',ok=False)
        self.assertIn('baseline',r['gap'])

    def test_tracked_schema_format_and_identity_are_real_checks(self):
        original=json.loads((self.root/'config.json').read_bytes())
        cases=[{**original,'schema_version':999},{**original,'request_store':{**original['request_store'],'schema_version':999}},
               {**original,'request_store':{**original['request_store'],'format':'unknown'}},
               {**original,'request_store':{**original['request_store'],'project_id':'PROJ-not-an-id'}}]
        for cfg in cases:
            (self.root/'config.json').write_text(json.dumps(cfg));self.run_check(ok=False)
        (self.root/'config.json').write_text(json.dumps(original))
        r=self.run_check('--expect-project-id','PROJ-'+'0'*32,ok=False);self.assertIn('identity',r['gap'])

    def test_lean_custom_contract_has_no_json_requirement_but_is_evidence_only(self):
        marker=self.root/'STATE.md';marker.write_text('Authoritative project route: lean manual notes; no tracked JSON backend.\n')
        receipt=self.receipt();receipt['managed']['.director/STATE.md']=hashlib.sha256(marker.read_bytes()).hexdigest();self.save_receipt(receipt)
        (self.root/'config.json').unlink();before=self.tree()
        r=self.run_check('--backend-contract','.director/STATE.md')
        self.assertEqual(r['status'],'evidence_matched')
        self.assertIn('authoritative canonical backend',r['actor_must_confirm'][2])
        self.assertEqual(before,self.tree())
        # Matching arbitrary bytes never authorizes a badge/role on its own.
        r=self.run_check('--backend-contract','AGENTS.md')
        self.assertEqual(r['status'],'evidence_matched');self.assertIn('actor evaluation',r['scope'])

    def test_unconfigured_template_provenance_and_malformed_json_fail_boundedly(self):
        original=self.receipt();bad={**original,'not_setup_acceptance':True};self.save_receipt(bad)
        self.assertIn('template',self.run_check(ok=False)['gap'])
        for url in [None,42,{},[]]:
            bad={**original,'source':{**original['source'],'url':url}};self.save_receipt(bad);self.run_check(ok=False)
        (self.root/'install.json').write_text('{"bad":NaN}');self.assertIn('nonfinite',self.run_check(ok=False)['gap'])
        (self.root/'install.json').write_text('{"bad":'+('['*1500)+'0'+(']'*1500)+'}')
        self.run_check(ok=False)

    def test_paths_symlinks_oversized_receipt_and_missing_guard_are_not_followed(self):
        self.run_check('--receipt','../outside.json',ok=False)
        (self.root/'DIRECTOR.md').unlink();(self.root/'DIRECTOR.md').symlink_to(self.root/'WORKER.md')
        self.assertIn('symlink',self.run_check(ok=False)['gap'])
        (self.root/'install.json').write_bytes(b' '*512001)
        self.assertIn('bound',self.run_check(ok=False)['gap'])


if __name__=='__main__':unittest.main()
