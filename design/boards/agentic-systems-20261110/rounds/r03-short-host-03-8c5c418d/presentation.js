'use strict';
const NS='http://www.w3.org/2000/svg';
const $=id=>document.getElementById(id);
const el=(tag,attrs={},text='')=>{const n=document.createElementNS(NS,tag);for(const[k,v]of Object.entries(attrs))n.setAttribute(k,v);if(text)n.textContent=text;return n};
const H=(tag,attrs={},text='')=>{const n=document.createElement(tag);for(const[k,v]of Object.entries(attrs))n.setAttribute(k,v);n.textContent=text;return n};
const refinedChapters=new Set(['systems','director','learning','communication','human']);
const refined=()=>refinedChapters.has(chapter);
const roles=[{id:'design',name:'Design',x:-105,y:-108},{id:'engineering',name:'Engineering',x:112,y:-109},{id:'quality',name:'Quality',x:161,y:72},{id:'operations',name:'Operations',x:-23,y:169},{id:'research',name:'Research',x:-168,y:61}];
const chapters={
systems:{"label": "Agentic systems", "title": "One domain.\nMany surveys.", "description": "Fieldwork supports plans, capture tools and reports over time. In this example a Director agent coordinates bounded work; people contribute goals, judgment and evidence.", "scope": "One illustrative arrangement", "qualification": "Branches stand for agents, teams or maintained responsibilities. This is an illustrative field-survey request.", "steps": [["How does one request become usable work?", "The ongoing Fieldwork domain supports many plans, tools and reports. Follow one field-survey package through the checks that make it useful.", "overview"], ["Prepare the next\nsurvey package.", "The caller needs a plan, capture tools and access evidence for both sites. The Director records those conditions.", "intake"], ["Choose the plan\nand its checks.", "Design receives the goal and defines a two-site plan: capture a location and an observation at each site.", "design"], ["The plan makes\nthe next work clear.", "The returned plan calls for capture tools and independent access evidence. Those become two bounded assignments.", "design-return"], ["Prepare tools.\nCheck conditions.", "Engineering prepares location-and-observation capture. Quality checks access evidence for both sites. Each owns its bounded assignment.", "parallel"], ["Tools are ready.\nOne check remains.", "Tools are ready; access is unverified. The Director compares both returns with the original conditions, then commissions the missing check.", "verify"], ["The missing\nevidence returns.", "Quality returns access evidence for both sites. The Director compares it with the open condition before accepting the package.", "final-return"], ["A checked package,\nready to use.", "The caller receives the two-site plan, prepared tools and checked access evidence. The request closes with a usable deliverable.", "conclude"], ["Other domains\nextend the result.", "Infrastructure retains the checked evidence and returns an archive reference. Each domain keeps responsibility for its own work.", "network"], ["One survey.\nUseful shared work.", "Publishing uses the checked package and archive reference to draft a briefing. The wider outcome is retained evidence and reusable work.", "network-many"]], "cueSummaries": ["One ongoing domain; many plans, tools and reports.", "Goal: plan, tools and checked access for both sites.", "Design defines two sites and what the package needs.", "The plan calls for tools and independent access evidence.", "Engineering prepares capture; Quality checks access evidence.", "Tools are ready. Access is unverified, so Quality checks it.", "Access evidence returns; the package can meet all three checks.", "The caller receives the plan, tools and checked evidence.", "Infrastructure retains the evidence and returns an archive reference.", "Publishing uses checked evidence to draft a reusable briefing."]},
director:{"label": "The Director Pattern", "title": "One request.\nOne accountable owner.", "description": "Work can happen across Fieldwork. A Director agent keeps the caller’s original conditions in view and remains responsible for the checked return.", "scope": "Current method · one illustrated arrangement", "qualification": "Branches represent agents, teams or ongoing responsibilities. People contribute goals, judgment and evidence.", "steps": [["The Director stays accountable.", "The Director retains the caller’s whole request while other responsibilities own bounded contributions. Follow one two-site field-survey package.", "overview"], ["Make ‘ready’\nexplicit.", "The caller needs a usable two-site plan, prepared capture tools and evidence that both sites are accessible. The Director records those conditions and acknowledges the request.", "intake"], ["Give Design\na bounded goal.", "Design is asked for a usable two-site plan. It records the assignment and works out the locations, capture needs and access checks.", "design"], ["Use the plan to\ndivide the work.", "Design returns a location-and-observation plan for both sites. The Director reviews it, assigns tools and access checks separately, and tells the caller what is underway.", "parallel-status"], ["Tools are ready.\nThe package is not.", "Engineering returns prepared capture tools. Quality’s access review is still pending. The Director records the progress and tells the caller what remains open.", "partial-return"], ["A return can\nreveal a gap.", "Quality reports access unverified. The Director compares that finding with the original conditions, commissions the missing check and explains why the request remains open.", "verify-status"], ["Check evidence\nagainst the request.", "Quality returns evidence that both planned sites are accessible. The Director checks it alongside the plan and tools before recording that all three conditions are met.", "final-return"], ["Return the\nchecked package.", "The caller receives the two-site plan, prepared capture tools and checked access evidence. The Director closes the request with the result and its basis recorded.", "conclude"]], "cueSummaries": ["The Director keeps the whole outcome in view.", "A usable plan, ready tools and checked access to both sites.", "Design owns its bounded plan; the Director retains the request.", "A reviewed plan leads to tools, access checks and a caller update.", "Tools are ready; the access review remains open.", "A gap report causes a focused check, not a ready decision.", "Returned access evidence is checked before readiness is accepted.", "The caller receives the checked package and the request concludes."]},
learning:{"label": "Learning and growth", "title": "Work leaves\nevidence.", "description": "Earlier Fieldwork records retain planning briefs, corrections and late access follow-ups. A review can turn selected experience into a scoped change; an owner decides what is maintained.", "scope": "Owner-initiated learning · optional growth", "qualification": "Research performs the bounded review in this example. Recording a trace does not change instructions.", "steps": [["Work leaves evidence.", "Earlier survey-package records preserve work, corrections and late access follow-ups. Those traces give an owner something concrete to review.", "learn-observe"], ["The owner chooses\na bounded review.", "The Director asks Research to review selected planning briefs and corrections: why were per-site access-evidence needs discovered late? This is bounded work, initiated by an owner.", "learn-review"], ["Propose a better\nplanning brief.", "The selected briefs omitted per-site evidence needs. Research proposes naming those needs in the initial brief for future multi-site survey planning. An owner decision is still pending.", "learn-propose"], ["An owner decides\nwhat changes.", "The authorized owner accepts this scoped improvement. The maintained planning instructions are then updated to include per-site evidence requirements in the initial brief.", "learn-decide"], ["A matching task\nuses the lesson.", "A later multi-site survey request loads the guidance before delegation. Design receives per-site evidence requirements in its brief and includes them in the new plan. Access still needs checking.", "learn-reuse"], ["Growth needs its\nown justification.", "Repeated internal summaries present another need. After review, the owner chooses Synthesis, and its duties and route are maintained before the responsibility becomes available.", "learn-grow"], ["A later request\ntests the new role.", "On a separate encounter, a checked package reaches Synthesis for an evidence-linked internal summary. Its result returns for evaluation and becomes new work evidence.", "learn-use"]], "cueSummaries": ["Retained work is evidence for a chosen review.", "Research reviews selected briefs and late corrections.", "Proposed change: initial briefs name per-site evidence needs.", "Owner acceptance precedes attributable instruction maintenance.", "A later matching brief includes the maintained lesson.", "A separately justified, reviewed and implemented responsibility.", "A separate summary request tests the maintained role."]},
communication:{"label": "Across systems", "title": "Two domains.\nTheir own work.", "description": "Fieldwork needs its checked survey evidence retained. Addressed messages connect independent domains while each keeps responsibility for its own work.", "scope": "Proposed shared exchange", "qualification": "", "steps": [["Two domains.\nTheir own work.", "Fieldwork needs its checked survey evidence retained. Infrastructure owns the archive work; Fieldwork keeps the original commitment and checks the returned result.", "exchange-overview"], ["Leave an addressed\narchive request.", "Fieldwork sends the checked two-site package, archive task and return address to Infrastructure. It asks for a usable reference and a retained-item list.", "exchange-send"], ["Pick up the work\naddressed to you.", "Infrastructure selects its archive request and records the bounded task locally. Messages for Research and the person remain waiting.", "exchange-pickup"], ["Acknowledge.\nArchive locally.", "Infrastructure accepts the task and sends an acknowledgment through the exchange. Its own Engineering responsibility retains the evidence. The archive result is still pending.", "exchange-work"], ["Return a reference\nand a retained list.", "Infrastructure records its completed archive work, then sends Fieldwork the reference and retained-item list for the same two-site package.", "exchange-return"], ["Check the result\nagainst the request.", "Fieldwork checks the package identity, requested inventory and usable reference before accepting the archive result. Each domain retains its own record.", "exchange-evaluate"]], "cueSummaries": ["Independent domains keep their own responsibilities.", "Two-site package → archive reference and retained-item list.", "Only Infrastructure picks up its addressed archive request.", "Acceptance is acknowledged; the archive result remains pending.", "A new result message carries the reference and retained items.", "Same package, requested items and usable reference must match."]},
human:{label:'People in the loop',title:'This next step\nneeds a person.',description:'The checked survey package is ready. Preparing a Site 2 schedule draft still needs an explicit decision from the visit owner.',scope:'Proposed shared exchange · human decision',qualification:'',steps:[
 ['This next step\nneeds a person.','The visit owner decides whether preparation of a Site 2 schedule draft should proceed. The checked survey package supplies context; it does not supply that permission.','human-overview'],
 ['Ask for a\nspecific decision.','The Director asks the visit owner: approve preparing the Site 2 schedule draft? The addressed question includes the checked package and a reply route to Fieldwork.','human-send'],
 ['The schedule waits\nfor an answer.','The dependent preparation stays on hold while the question is unanswered. Separately authorized Operations work can continue; waiting does not create approval.','human-wait'],
 ['The person\nmakes the choice.','The visit owner picks up the question, reviews its context and explicitly approves preparing the Site 2 schedule draft. That recorded choice has not reached Fieldwork yet.','human-decide'],
 ['Resume only what\nthe reply permits.','The answer returns through the same exchange. The Director records it and checks the person, question and draft-only scope before assigning Engineering.','human-return'],
 ['Return the outcome\nof that decision.','Engineering prepares the schedule draft. The Director checks it against the approved scope and reports the result to the person through the same exchange. No visit has been booked.','human-conclude']
],cueSummaries:['The visit owner decides whether draft preparation proceeds.','Question: approve preparing the Site 2 schedule draft?','No answer yet. The schedule preparation stays on hold.','A person makes and records one explicit, scoped choice.','Receive the reply, check its scope, then assign the draft.','A checked draft returns to the person; no visit is booked.']}

};
let ownerLinks=[],shortFocusKey='';
let chapter='systems',index=0,playing=false,motionRunning=true,storyStarted=false,playMode='cue',elapsed=0,lifeTime=0,last=performance.now(),scene='',construction='',cellNodes={},signals=[],camera={},timeline=null,duration=8200;
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
motionRunning=!reduced;
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ease=x=>x*x*(3-2*x);
const recordOffsets={director:[23,47],design:[28,-65],engineering:[4,82],quality:[-186,58],operations:[18,22],research:[-82,22]};
function layoutMode(){const w=window.innerWidth||1600;return w<=600?'phone':w<=1000?'compact':'wide';}
function shortViewport(){return(window.innerHeight||900)<=640;}
function pairPose(id,code=chapters[chapter].steps[index][2]){
 if(chapter==='human'&&layoutMode()==='phone')return{x:155,y:185,s:['human-return','human-conclude'].includes(code)?.42:.32};
 if(chapter==='communication'&&layoutMode()==='phone'){const active=id==='right'&&['exchange-work','exchange-return'].includes(code)||id==='left'&&code==='exchange-evaluate';return{x:id==='left'?155:445,y:185,s:active?.42:id==='left'?.32:.30};}
 return layoutMode()==='phone'?{x:300,y:id==='left'?260:1260,s:.55}:{x:id==='left'?730:1380,y:450,s:id==='left'?.65:.61};
}
function communicationBox(){return layoutMode()==='phone'?{x:30,y:435,w:540,h:200}:{x:965,y:260,w:220,h:368};}
function communicationSlot(i){const box=communicationBox(),phone=layoutMode()==='phone';return{x:box.x+(phone?(i%2?285:15):13),y:box.y+(phone?18+Math.floor(i/2)*88:20+i*86),w:phone?240:194,h:72};}
function communicationRecordSlot(cell,role,t){
 if(layoutMode()!=='phone')return[cell==='left'?600:1220,role==='director'?665:750];
 const code=timeline.code,x=cell==='left'?30:330;
 let active='director';if(cell==='right'&&(code==='exchange-work'&&t>=4000||code==='exchange-return'&&t<5550))active='engineering';
 if(cell==='left'&&code==='exchange-evaluate'&&t>=5750&&t<15500)active='quality';
 return[x,role===active?290:700];
}
function humanRecordSlot(role,t){
 const code=timeline.code,phone=layoutMode()==='phone';if(!phone)return[600,role==='director'?665:role==='engineering'?750:role==='operations'&&layoutMode()==='wide'?800:835];
 const active=code==='human-return'&&t>=12250||code==='human-conclude'&&t<7250?'engineering':'director';
 return[30,role===active?290:role==='operations'?800:700];
}
function personPoint(){const p=new DOMPoint(0,0).matrixTransform($('person').getCTM()).matrixTransform($('diagram').getCTM().inverse());return[p.x,p.y];}
function neighborViews(){return layoutMode()==='phone'?[['infrastructure',475,600,.30],['publishing',475,1000,.28],['research-cell',115,1000,.28],['care',115,600,.28]]:[['infrastructure',1365,200,.35],['publishing',1360,720,.31],['research-cell',700,730,.28],['care',630,165,.25]];}
function phoneRecordBase(){return shortViewport()?((window.innerHeight||900)<=500?440:480):600;}
function phoneRecordSlot(role,t=elapsed){
 if(['systems','director'].includes(chapter)){
  const base=phoneRecordBase();if(role==='director')return[30,base];
  const visible=timeline.records.filter(e=>e.role!=='director'&&e.cell==='main'&&e.at<=t),written=latest(visible.filter(e=>e.at>0),t),working=timeline.work.filter(e=>e.cell==='main'&&e.start<=t&&e.end>=t&&visible.some(r=>r.role===e.role));
  const catching=latest(timeline.arrivals.filter(e=>e.cell==='main'&&e.role!=='director'&&e.at<=t&&t<e.at+300),t),writing=latest(visible.filter(e=>e.at>0&&t<e.at+620),t);
  const active=(shortViewport()?writing?.role||catching?.role:null)||written?.role||working.find(e=>e.direction==='return')?.role||working[0]?.role||visible[visible.length-1]?.role||'design';
  if(role===active)return[330,base];const parked=['design','engineering','quality','research','operations'].filter(r=>r!==active).indexOf(role);return[30+(Math.max(0,parked)%2)*300,780+Math.floor(Math.max(0,parked)/2)*90];
 }
 let order=['director','design','engineering','quality','research','operations'];
 if(chapter==='learning'){const code=chapters[chapter].steps[index][2];if(code==='learn-reuse'&&role==='design'&&t<8250)return[30,780];order=code==='learn-use'?['director','synthesis','research','design','engineering','quality','operations']:code==='learn-reuse'?['director','design','research','engineering','quality','operations','synthesis']:['learn-decide','learn-grow'].includes(code)?['director',null,'research','design','engineering','quality','operations','synthesis']:['director','research','design','engineering','quality','operations','synthesis'];}
 const i=Math.max(0,order.indexOf(role));return[30+(i%2)*300,phoneRecordBase()+Math.floor(i/2)*90];
}
function prepareSceneViewport(){
 const mode=layoutMode(),phone=mode==='phone',svg=$('diagram'),code=chapters[chapter].steps[index][2];document.body.dataset.layout=mode;prepareShortView();
 if(mode==='wide'){svg.setAttribute('viewBox','0 0 1600 900');svg.style.height='';}
 else if(mode==='compact'){svg.setAttribute('viewBox',scene==='cell'?'450 0 1150 900':'400 150 1200 800');svg.style.height=scene==='cell'?'600px':'520px';}
 else{let h=chapter==='communication'?850:chapter==='human'?900:scene!=='cell'?1700:code.startsWith('network')?1250:600;if(scene==='cell'&&!code.startsWith('network'))for(const e of timeline.records)if(e.cell==='main')h=Math.max(h,phoneRecordSlot(e.role)[1]+80);if(chapter==='learning'&&['learn-reuse','learn-grow','learn-use'].includes(code))h=Math.max(h,900);svg.setAttribute('viewBox',`0 0 600 ${h}`);svg.style.height=(h*(window.innerWidth||390)/600)+'px';}
 if(scene==='cell'){
  $('caller').querySelector('circle').setAttribute('cx',phone?45:480);$('caller').querySelector('circle').setAttribute('cy',phone?300:455);const label=$('caller').querySelector('text');label.setAttribute('x',phone?45:480);label.setAttribute('y',phone?332:487);label.style.fontSize=phone?'18px':'';
  $('wide-main-label').setAttribute('x',phone?300:1000);$('wide-main-label').setAttribute('y',phone?430:665);
  if(chapter==='learning'){$('instructions-actor').setAttribute('transform',phone?'translate(30 590)':'translate(1170 700)');$('learning-decision').setAttribute('transform',phone?(shortViewport()?((window.innerHeight||900)<=500?'translate(30 620)':'translate(30 385)'):'translate(30 435)'):'translate(610 700)');}else{$('instructions-actor').setAttribute('transform',phone?'translate(-285 76)':'');$('learning-decision').setAttribute('transform',phone?'translate(120 850)':'translate(1100 736)');}
 }else{
  for(const id of ['left',...(scene==='exchange'?['right']:[])]){const q=pairPose(id);setCamera(id,q.x,q.y,q.s);}
  $('exchange').setAttribute('transform',phone?'translate(201 625)':'translate(965 292)');$('exchange-state').setAttribute('x',phone?300:1064);$('exchange-state').setAttribute('y',phone?1610:730);
  $('left-domain').setAttribute('x',phone?300:730);$('left-domain').setAttribute('y',phone?525:715);$('right-domain').setAttribute('x',phone?300:1380);$('right-domain').setAttribute('y',phone?1525:715);
  if(chapter==='communication')layoutCommunication();
  if(scene==='human')layoutHuman();
 }
}
function seed(n){const x=Math.sin(n*127.1+311.7)*43758.5453123;return x-Math.floor(x)}
function buildDust(){for(let i=0;i<120;i++)$('dust').append(el('circle',{cx:seed(i+1)*1600,cy:seed(i+180)*900,r:seed(i+350)*2.5+.3,fill:i%6?'#276780':'#91c8db',opacity:seed(i+600)*.13+.025}));}
function record(label){const g=el('g',{class:'record'});g.append(el('rect',{x:0,y:0,width:28,height:30,rx:3}));for(let i=0;i<3;i++)g.append(el('path',{d:`M6 ${8+i*6} H${i===2?17:22}`,fill:'none',class:'record-line',pathLength:1}));g.append(el('text',{x:35,y:12,class:'record-name'},label),el('text',{x:35,y:27,class:'record-status'},''));return g}
function createCell(name,id,{labels=true,simple=false,color='#27ddc8',variant=id}={}){
 variant={main:0,left:0,right:1,infrastructure:1,publishing:2,'research-cell':3,care:4}[id]??variant;
 const requestedRoles=chapter==='learning'&&id==='main'?[...roles,{id:'synthesis',name:'Synthesis'}]:roles;
 const c=LivingCell.create({id,name,roles:requestedRoles,labels,simple,color,variant});c.g.classList.add('cell');
 if(id==='main')c.domainTitle=[...c.g.querySelectorAll('text')].find(n=>n.textContent===name);
 c.records={director:record('Request')};c.g.append(c.records.director);
 for(const r of requestedRoles){c.records[r.id]=record('Work record');c.g.append(c.records[r.id]);}
 c.name=name;cellNodes[id]=c;return c.g;
}
function fixedWire(id,from,to,color='#42606f',curve=0){const p=el('path',{id,d:`M${from[0]},${from[1]} Q${(from[0]+to[0])/2},${(from[1]+to[1])/2+curve} ${to[0]},${to[1]}`,fill:'none',stroke:color,'stroke-width':1.2,opacity:.3});$('world').prepend(p);return p}
function globalPoint(cellId,roleId='director'){
 const c=cellNodes[cellId],p=c.point(roleId),svg=$('diagram');
 const q=new DOMPoint(p.x,p.y).matrixTransform(c.g.getCTM()).matrixTransform(svg.getCTM().inverse());return[q.x,q.y];
}
function pointOn(path,f){const p=path.getPointAtLength(path.getTotalLength()*clamp(f));const q=new DOMPoint(p.x,p.y).matrixTransform(path.getCTM()).matrixTransform($('diagram').getCTM().inverse());return[q.x,q.y];}
function setCamera(id,x,y,s,opacity=1){const old=camera[id];if(old&&old.to.x===x&&old.to.y===y&&old.to.s===s&&old.to.opacity===opacity)return;const value=old?.value||{x,y,s,opacity};camera[id]={from:{...value},to:{x,y,s,opacity},value:{...value},at:lifeTime};}
// Fit the whole-cell overview to the actual clipped stage. Working scenes
// deliberately move closer to the Director; the domain title leaves that frame.
function mainView(code){
 const network=code.startsWith('network'),opening=code==='overview'||code==='learn-observe',mode=layoutMode();
 if(mode==='phone'){if(chapter==='learning'&&code!=='learn-observe')return{x:300,y:260,s:.62};return{x:300,y:network?250:300,s:network?.5:.74};}
 if(mode==='compact')return{x:network?1000:1060,y:network?450:437,s:network?.59:opening||code.startsWith('learn-')?1.31:1.48};
 if(network)return{x:1000,y:450,s:.59};
 if(!opening&&!code.startsWith('learn-'))return{x:1080,y:450,s:2};
 const wanted={x:1060,y:437,s:opening||code.startsWith('learn-')?1.31:1.48};
 const stage=$('stage'),svg=$('diagram');
 if(!stage.getBoundingClientRect||!svg.getScreenCTM)return wanted;
 const box=stage.getBoundingClientRect(),matrix=svg.getScreenCTM();if(!matrix)return wanted;
 const inverse=matrix.inverse(),top=new DOMPoint(box.left,box.top+18).matrixTransform(inverse).y,bottom=new DOMPoint(box.left,box.bottom-18).matrixTransform(inverse).y;
 const above=opening?325:300,below=300,s=Math.min(wanted.s,(bottom-top)/(above+below));
 return{x:wanted.x,y:clamp(wanted.y,top+above*s,bottom-below*s),s};
}
function applyMainView(code){const view=mainView(code);setCamera('main',view.x,view.y,view.s);}
function renderCamera(){for(const[id,v]of Object.entries(camera)){const f=reduced?1:ease(clamp((lifeTime-v.at)/1700));for(const k of ['x','y','s','opacity'])v.value[k]=v.from[k]+(v.to[k]-v.from[k])*f;const q=v.value;cellNodes[id]?.g.setAttribute('transform',`translate(${q.x} ${q.y}) scale(${q.s})`);cellNodes[id]?.g.setAttribute('opacity',q.opacity);const title=cellNodes[id]?.domainTitle;if(id!=='main'&&title){title.style.fontSize=(20/q.s)+'px';title.setAttribute('y',300+30/q.s)}if(layoutMode()==='phone'&&id==='main'){for(const role of Object.values(cellNodes[id].rs))if(role.label)role.label.style.fontSize=(18/q.s)+'px';const director=[...cellNodes[id].g.querySelectorAll('text')].find(n=>n.textContent==='Director');if(director)director.style.fontSize=(18/q.s)+'px';if(title)title.style.fontSize=(20/q.s)+'px';}else if(id==='main'){for(const role of Object.values(cellNodes[id].rs))if(role.label)role.label.style.fontSize='14px';const director=[...cellNodes[id].g.querySelectorAll('text')].find(n=>n.textContent==='Director');if(director)director.style.fontSize='14px';if(title)title.style.fontSize='14px';}}}
function makeLearningTools(){
 const g=el('g',{id:'learning-tools'});
 const review=el('g',{id:'review-actor',class:'learning-actor'});
 review.append(el('circle',{cx:730,cy:365,r:21,fill:'url(#star)',class:'review-halo'}),el('circle',{cx:730,cy:365,r:6,fill:'#e9bd79',class:'review-core'}),el('text',{x:730,y:318,'text-anchor':'middle',class:'tool-label'},'Bounded review'));
 const branches=el('g',{id:'review-branches'});
 for(const [i,x,y]of [[0,680,382],[1,699,422],[2,763,421],[3,780,366]]){branches.append(el('path',{d:`M730,365 Q${(730+x)/2},${y-8} ${x},${y}`,fill:'none',stroke:'#e9bd79','stroke-width':1.1,'data-branch':i}),el('circle',{cx:x,cy:y,r:3,fill:'#e9bd79'}));}
 review.append(branches);const rr=record('Review record');rr.id='review-record';rr.setAttribute('transform','translate(676 447) scale(1.6)');review.append(rr);g.append(review);
 const instructions=el('g',{id:'instructions-actor'});instructions.append(el('rect',{x:705,y:574,width:43,height:40,rx:4,fill:'#10242b',stroke:'#e9bd79','stroke-width':1.4}),el('path',{d:'M715 586 H739 M715 594 H739 M715 602 H733',fill:'none',stroke:'#e9bd79','stroke-width':1.2}),el('text',{x:726,y:650,'text-anchor':'middle',class:'tool-label',id:'instructions-label'},'Maintained instructions'));g.append(instructions);
 const decision=el('g',{id:'learning-decision',transform:'translate(1100 736)'});decision.append(el('rect',{width:360,height:70,rx:7,class:'decision-panel'}),el('text',{x:18,y:25,class:'decision-title'},'Owner decision'),el('text',{x:18,y:51,class:'tool-status',id:'decision-label'},'Proposal under review'));g.append(decision);
 if(chapter==='learning'){
  instructions.replaceChildren();const label=el('text',{x:0,y:-18,class:'tool-label',id:'instructions-label'},'Guidance to maintain'),paper=record('Planning instructions');paper.id='instruction-record';instructions.append(label,paper);
  decision.querySelector('rect').setAttribute('width',420);decision.querySelector('rect').setAttribute('height',112);decision.append(el('text',{x:18,y:77,class:'lesson-content',id:'lesson-content'},'Initial brief: per-site evidence needs'),el('text',{x:18,y:99,class:'lesson-scope',id:'lesson-scope'},'Scope: multi-site survey planning'));
 }
 $('world').append(g);
 fixedWire('review-wire',[1060,437],[730,365],'#9c865d',-35);
 fixedWire('proposal-wire',[730,365],[1100,770],'#9c865d',40).setAttribute('d','M730,365 C1030,330 970,600 1100,770');
 fixedWire('guidance-wire',[1100,770],[726,594],'#9c865d',35);
 fixedWire('guidance-director-wire',[726,594],[1060,437],'#9c865d',45);
}
function makeScene(kind){const signature=kind+':'+(chapter==='learning'?'learning':'standard');if(scene===kind&&construction===signature)return;scene=kind;construction=signature;cellNodes={};camera={};$('world').replaceChildren();$('signals').replaceChildren();
 if(kind==='cell'){
  $('world').append(createCell('Fieldwork','main',{variant:0}),el('text',{id:'wide-main-label',x:1000,y:665,'text-anchor':'middle',class:'exchange-domain',opacity:0},'Fieldwork'));
  const caller=el('g',{id:'caller',class:'caller'});caller.append(el('circle',{cx:480,cy:455,r:5,fill:'#a5c5d4'}),el('text',{x:480,y:487,'text-anchor':'middle',class:'external-label'},'Caller'));$('world').append(caller);fixedWire('caller-wire',[480,455],[1060,437]);
  for(const[n,id,x,y,s,c]of [['Infrastructure','infrastructure',1365,200,.35,'#7d9fe2'],['Publishing','publishing',1360,720,.31,'#f58eab'],['Research','research-cell',700,730,.28,'#e9bd79'],['Customer care','care',630,165,.25,'#68b6b8']]){const g=createCell(n,id,{labels:false,simple:true,color:c,variant:id});const title=el('text',{y:335,'text-anchor':'middle',class:'neighbor-label',style:`fill:${c};font-size:43px`},n);g.append(title);cellNodes[id].domainTitle=title;$('world').append(g);const v=neighborViews().find(v=>v[0]===id);setCamera(id,v[1],v[2],v[3],0)}
  for(const[id,from,to]of [['network-infrastructure','main','infrastructure'],['network-publishing','main','publishing'],['network-research','main','research-cell'],['network-care','care','infrastructure'],['network-archive-brief','infrastructure','publishing']]){const p=fixedWire(id,[0,0],[0,0]);p.dataset.from=from;p.dataset.to=to;p.classList.add('network-wire');}
  makeLearningTools();
 }else{
  $('world').append(createCell('Fieldwork','left',{labels:['communication','human'].includes(chapter),simple:false,variant:0}));{const q=pairPose('left');setCamera('left',q.x,q.y,q.s);}
  if(kind==='exchange'){$('world').append(createCell('Infrastructure','right',{labels:chapter==='communication',simple:false,color:'#f58eab',variant:1}));{const q=pairPose('right');setCamera('right',q.x,q.y,q.s);}}
  else{const p=el('g',{id:'person',transform:'translate(1380 450)'});p.append(el('circle',{cx:0,cy:-46,r:29,fill:'none',stroke:'#e9bd79','stroke-width':2,class:'person-head'}),el('path',{d:'M-59 70 C-59 -8 59 -8 59 70 M-78 91 H78',fill:'none',stroke:'#e9bd79','stroke-width':2}),el('circle',{cx:0,cy:0,r:67,fill:'#e9bd79',opacity:0,class:'person-catch'}));$('world').append(p);
   for(const[id,name]of [['decision','Person · decision'],['outcome','Person · outcome']]){const paper=record(name);paper.id='person-record-'+id;paper.querySelector('.record-name')._learningName=name;$('world').append(paper);}
   $('world').append(el('text',{id:'person-scope',x:1380,y:225,'text-anchor':'middle',class:'person-scope'},'Draft preparation only'));
  }
  $('world').append(el('text',{id:'left-domain',x:730,y:715,'text-anchor':'middle',class:'exchange-domain'},'Fieldwork'),el('text',{id:'right-domain',x:1380,y:715,'text-anchor':'middle',class:'exchange-domain',style:`fill:${kind==='exchange'?'#f58eab':'#e9bd79'}`},kind==='exchange'?'Infrastructure':'Visit owner · person'));
  fixedWire('exchange-left',[730,450],[968,450]);fixedWire('exchange-right',[1160,450],[1380,450]);
  const ex=el('g',{id:'exchange',transform:'translate(965 292)'});ex.append(el('rect',{width:198,height:290,rx:12,fill:'#07131c',stroke:'#294651','stroke-width':1.3}),el('text',{x:99,y:-25,'text-anchor':'middle',class:'exchange-label'},'Shared exchange'));
  for(let i=0;i<4;i++){const row=el('g',{id:'mail-'+i,transform:`translate(13 ${20+i*66})`});row.append(el('rect',{width:172,height:51,rx:5,class:'exchange-card'}),el('circle',{cx:14,cy:18,r:3.5,fill:['#7d9fe2','#f58eab','#e9bd79','#27ddc8'][i]}),el('text',{x:26,y:22,class:'exchange-text'},['Research','Infrastructure','Person','Fieldwork'][i]),el('text',{x:26,y:41,class:'mail-status'},'Addressed message'));if(['communication','human'].includes(chapter)){row.querySelector('circle').setAttribute('class','mail-catch');row.append(el('text',{x:24,y:42,class:'mail-payload'},'No message'));}ex.append(row)}$('world').append(ex,el('text',{id:'exchange-state',x:1064,y:730,'text-anchor':'middle',class:'exchange-caption'},'Each system keeps its own work.'));
 }
}
function newTimeline(){signals=[];ownerLinks=[];$('ownership').replaceChildren();$('signals').replaceChildren();timeline={records:[],work:[],arrivals:[],mail:[],caption:[],tools:[],toolRecords:[],toolArrivals:[],decisions:[],reveal:[]};duration=8200;if(chapter==='director')timeline.callerStatus=[];if(chapter==='learning')timeline.instructionRecords=[];if(chapter==='human')timeline.personRecords=[];if(refined())for(const[cell,c]of Object.entries(cellNodes))for(const[role,record]of Object.entries(c.records)){const g=el('g',{class:'ownership-link'}),base=el('path',{class:'ownership-base',fill:'none'}),ink=el('path',{class:'ownership-ink',fill:'none',pathLength:1}),dot=el('circle',{r:3.5,class:'writing-dot'});g.append(base,ink,dot);$('ownership').append(g);ownerLinks.push({cell,role,record,g,base,ink,dot});}}
function addInstructionOwnership(){if(chapter!=='learning')return;const g=el('g',{class:'ownership-link'}),base=el('path',{class:'ownership-base',fill:'none'}),ink=el('path',{class:'ownership-ink',fill:'none',pathLength:1}),dot=el('circle',{r:3.5,class:'writing-dot'});g.append(base,ink,dot);$('ownership').append(g);ownerLinks.push({cell:'main',role:'director',record:$('instruction-record'),g,base,ink,dot,instructions:true});}

function systemRecordName(cell,role){if(chapter==='human')return role==='director'?'Fieldwork · schedule':role==='engineering'?'Engineering · draft':role==='operations'?'Operations · unrelated':'Work';if(chapter==='communication')return role==='director'?(cell==='left'?'Fieldwork · request':'Infrastructure · archive'):role==='engineering'?'Engineering · retention':'Quality · archive check';if(chapter==='learning')return{director:'Director · memory',design:'Design · plans',research:'Research · review',synthesis:'Synthesis · summary'}[role]||((roles.find(r=>r.id===role)?.name||role)+' · work');if(role==='director')return cell==='infrastructure'?'Infrastructure · archive':cell==='publishing'?'Publishing · draft':'Director · request';return{design:'Design · plan',engineering:'Engineering · tools',quality:'Quality · access'}[role]||((roles.find(r=>r.id===role)?.name||'Work')+' record');}
function directorRecordLabel(cell,role,kind,label){const code=timeline.code;
 if(cell!=='main')return label;
 if(role==='design'&&kind==='complete')return'Two-site plan ready';
 if(role==='engineering'&&kind==='complete')return'Capture tools ready';
 if(role==='quality'&&kind==='complete')return code==='verify-status'?'Access unverified':'Both sites accessible';
 if(role==='director'&&kind==='received'&&code==='intake')return'Goal + checks recorded';
 if(role==='director'&&kind==='routed')return{design:'Plan assigned','parallel-status':'Tools + access assigned','verify-status':'Focused access check'}[code]||label;
 if(role==='director'&&kind==='evaluated')return{'parallel-status':'Plan usable','partial-return':'Tools accepted; access pending','verify-status':'Access still unverified','final-return':'All three checks met'}[code]||label;
 return label;
}
function systemRecordLabel(cell,role,kind,label,at){if(['communication','human'].includes(chapter))return label;if(chapter==='learning'){
 if(role==='director'&&kind==='routed')return{'learn-review':'Bounded review assigned','learn-reuse':'Per-site needs in brief','learn-use':'Summary task assigned'}[timeline.code]||label;
 if(kind==='complete'&&at>0)return role==='research'?'Proposal: per-site needs':role==='design'?'Per-site needs listed':role==='synthesis'?'Evidence-linked summary ready':label;
 return label;
 }if(chapter==='director')return directorRecordLabel(cell,role,kind,label);const code=timeline.code;
 if(cell==='main'){
  if(role==='design'&&kind==='complete')return'Two-site plan ready';
  if(role==='engineering'&&kind==='complete')return'Capture tools ready';
  if(role==='quality'&&kind==='complete')return code==='verify'?'Access unverified':'Both sites accessible';
  if(role==='director'&&kind==='routed')return code==='design'?'Design brief prepared':code==='parallel'?'Tools + checks prepared':code==='verify'?'Focused check prepared':label;
  if(role==='director'&&kind==='evaluated')return{'design-return':'Plan sets next work',verify:'Access still unverified','final-return':'All three checks met',network:'Archive reference linked','network-many':'Briefing draft linked'}[code]||label;
  if(role==='director'&&kind==='complete'&&code==='conclude')return'Package complete';
  if(role==='director'&&kind==='received'&&code==='intake')return'Survey goal recorded';
 }
 return label;
}
// Explanatory focus follows sustained story phases; individual writes and packets
// retain their own exact clocks without briefly replacing the readable sentence.
const systemFocus={
 intake:[
  [0,'The caller asks for a two-site field-survey package.'],
  [2200,'The Director records the goal and the three conditions.']
 ],
 design:[
  [0,'The Director prepares and sends the survey goal to Design.'],
  [3050,'Design records the goal, then works out a two-site plan.']
 ],
 'design-return':[
  [0,'Design gathers the results from its connected branches.'],
  [3400,'Design records and returns the two-site plan.'],
  [6000,'The Director records what the plan requires next.']
 ],
 parallel:[
  [0,'Two bounded assignments go to Engineering and Quality.'],
  [3750,'Engineering prepares capture tools; Quality checks access evidence.']
 ],
 verify:[
  [0,'Engineering and Quality gather their branch results.'],
  [3400,'Each records and returns its findings to the Director.'],
  [9000,'The Director compares the returns, then asks Quality to resolve access.'],
  [13300,'Quality gathers the missing access evidence.']
 ],
 'final-return':[
  [0,'Quality gathers the access evidence from its branches.'],
  [3400,'Quality records and returns access evidence for both sites.'],
  [6000,'The Director checks the evidence against the open condition.']
 ],
 conclude:[
  [0,'The Director records the checked package and returns it to the caller.'],
  [3600,'The caller now has a usable two-site survey package.']
 ],
 network:[
  [0,'Fieldwork asks Infrastructure to retain the checked evidence.'],
  [3600,'Infrastructure archives the evidence and records its reference.'],
  [8200,'The archive reference returns to Fieldwork for reuse.']
 ],
 'network-many':[
  [0,'Fieldwork prepares and sends a briefing request to Publishing.'],
  [3500,'Publishing receives the request and Infrastructure’s archive reference.'],
  [6400,'Publishing combines the checked package and reference into a draft.'],
  [9500,'Publishing records and returns the briefing draft.'],
  [12000,'Fieldwork links the returned briefing draft.']
 ]
};
const directorFocus={
 intake:[[0,'The caller asks for a ready two-site survey package.'],[2200,'The Director preserves the conditions and prepares an acknowledgment.'],[4500,'The acknowledgment returns to the caller.']],
 design:[[0,'Design receives a bounded goal: make the two-site plan usable.'],[3750,'Design works out the sites, capture needs and access checks.']],
 'parallel-status':[[0,'Design gathers the results from its connected branches.'],[3400,'Design records and returns the two-site plan.'],[6000,'The Director reviews what the plan requires next.'],[8800,'Tools and access checks become two bounded assignments.'],[12250,'Separate work begins; the Director reports what is underway.']],
 'partial-return':[[0,'Engineering gathers its result while Quality continues its review.'],[3400,'Engineering records and returns the prepared capture tools.'],[5950,'The Director checks the tools; the access review remains open.'],[8600,'The Director reports partial progress without closing the request.']],
 'verify-status':[[0,'Quality gathers its findings about access to both sites.'],[3400,'Quality records and returns an access gap report.'],[5950,'The original conditions expose the missing access evidence.'],[8800,'The Director assigns a focused check of access to both sites.'],[12250,'Quality checks the gap; the Director tells the caller what remains open.']],
 'final-return':[[0,'Quality gathers the missing access evidence from its branches.'],[3400,'Quality records and returns access evidence for both sites.'],[6000,'The Director checks the evidence against the original conditions.']],
 conclude:[[0,'The Director records and returns the checked package.'],[3600,'The caller has the package and the basis for its readiness.']]
};
const learningFocus={
 'learn-review':[[0,'The Director selects cases and assigns a bounded review.'],[3900,'Research compares the planning briefs with the later corrections.']],
 'learn-propose':[[0,'Research gathers its findings from the connected review work.'],[3400,'Research records and returns a scoped planning-brief proposal.'],[6000,'The owner receives the proposal; a decision is still pending.']],
 'learn-decide':[[0,'The owner reviews the evidence and the proposed scope.'],[2200,'The owner accepts this change for multi-site planning.'],[4600,'The Director writes the accepted lesson into maintained guidance.']],
 'learn-reuse':[[0,'A later multi-site survey request matches the maintained lesson.'],[2900,'The Director loads the guidance before preparing the brief.'],[6800,'Design receives a brief that names per-site evidence needs.'],[9250,'Design uses those requirements while preparing the new plan.'],[16450,'Design records and returns a plan with the per-site needs listed.'],[19000,'The Director checks the plan; access itself still needs verification.']],
 'learn-grow':[[0,'A recurring need supports a separate internal-summary proposal.'],[3000,'The owner accepts a bounded Synthesis responsibility.'],[5200,'The responsibility and its route are maintained before availability.']],
 'learn-use':[[0,'A separate later request asks for an evidence-linked summary.'],[4300,'Synthesis receives the checked package and a bounded task.'],[6750,'Synthesis assembles a summary with links to the checked inputs.'],[10000,'Completion gathers from the working branches toward Synthesis.'],[13400,'Synthesis records and returns the evidence-linked summary.'],[15950,'The Director receives and checks the summary against its sources.']]
};
const communicationFocus={
 'exchange-send':[[0,'Fieldwork prepares the archive request and checked evidence.'],[3500,'The addressed request waits for Infrastructure in the exchange.']],
 'exchange-pickup':[[0,'Infrastructure selects only the message addressed to it.'],[2500,'Infrastructure records the archive task in its own domain.']],
 'exchange-work':[[0,'Infrastructure accepts the task and sends an acknowledgment.'],[5200,'Local archive work continues while the acknowledgment returns.']],
 'exchange-return':[[0,'The archive work gathers inward, then records its result.'],[6800,'Infrastructure prepares the reference and retained-item list.'],[8700,'A new result message returns to the Fieldwork inbox.']],
 'exchange-evaluate':[[0,'Fieldwork picks up its addressed archive result.'],[3650,'The Director sends Quality a bounded archive comparison.'],[6900,'Quality compares package identity, retained items and the reference.'],[10000,'Quality gathers its findings inward, then records the check.'],[14200,'Quality returns the check; the Director evaluates the result.'],[17500,'The archive commitment is met; both domains keep their own records.']]
};
const humanFocus={
 'human-overview':[[0,'The visit owner decides whether schedule preparation proceeds.']],
 'human-send':[[0,'The Director records and sends a draft-preparation question.'],[4200,'The question waits for the addressed visit owner in the exchange.']],
 'human-wait':[[0,'No reply yet: schedule preparation remains on hold.']],
 'human-decide':[[0,'The person picks up and reviews the Site 2 draft question.'],[6600,'The person approves preparing the Site 2 schedule draft.']],
 'human-return':[[0,'The explicit answer returns through the same exchange.'],[6500,'The Director checks the person, question and draft-only scope.'],[9600,'Engineering receives and begins only the authorized schedule draft.']],
 'human-conclude':[[0,'Engineering finishes the draft and gathers its work inward.'],[5650,'The draft returns to the Director for a scope check.'],[11600,'The checked draft is reported through the same exchange.'],[17700,'The person receives the draft; no visit is booked.']]
};
function systemFocusAt(code,t){const phases=(chapter==='human'?humanFocus:chapter==='communication'?communicationFocus:chapter==='learning'?learningFocus:chapter==='director'?directorFocus:systemFocus)[code]||[];let text='';for(const[at,caption]of phases){if(at>t)break;text=caption;}return text;}
function renderCueSummary(t){
 if(!refined())return;const summary=$('phase-cue').querySelector('.cue-summary');if(!summary)return;
 const fallback=chapters[chapter].cueSummaries?.[index]||'',text=layoutMode()==='phone'||shortViewport()?(systemFocusAt(timeline.code,t)||fallback):fallback;
 if(summary.textContent!==text)summary.textContent=text;
}
function directorReadinessAt(t){const code=timeline.code;
 if(code==='parallel-status')return[t>=7600?'✓':t>=6620?'received':'open','open',t>=12700?'reviewing':'open'];
 if(code==='partial-return')return['✓',t>=7500?'✓':t>=6570?'received':'open','reviewing'];
 if(code==='verify-status')return['✓','✓',t>=12250?'checking':t>=7500?'?':t>=6570?'gap report':'reviewing'];
 if(code==='final-return')return['✓','✓',t>=7600?'✓':t>=6620?'received':'checking'];
 if(code==='conclude')return['✓','✓','✓'];return['open','open','open'];
}
function directorCallerReport(code){return{
 intake:'Request recorded.',
 'parallel-status':'Plan ready; checks underway.',
 'partial-return':'Tools ready; access pending.',
 'verify-status':'Access unverified; check underway.',
 conclude:'Checked survey package received.'
}[code]||'';}
function renderCallerStatus(t){if(chapter!=='director')return;const status=latest(timeline.callerStatus||[],t)?.text||'Awaiting acknowledgment.';$('caller-update-text').textContent=status;const cue=$('cue-caller');if(cue)cue.textContent='Caller: '+status;}
function readinessAt(t){if(chapter==='director')return directorReadinessAt(t);const code=timeline.code;let values=['open','open','open'];if(['parallel','verify','final-return','conclude','network','network-many'].includes(code))values[0]='✓';
 if(code==='design-return'){if(t>=6620)values[0]='received';if(t>=7600)values[0]='✓';}
 if(code==='verify'){if(t>=6570)values[1]='received';if(t>=7970)values[2]='gap report';if(t>=9000){values[1]='✓';values[2]='?';}if(t>=13200)values[2]='checking';}
 if(code==='final-return'){values[1]='✓';values[2]=t>=7600?'✓':t>=6620?'received':'checking';}
 if(['conclude','network','network-many'].includes(code))values=['✓','✓','✓'];return values;
}
function recAt(cell,role='director',at=0,updated=false,kind=updated?'complete':'received',label=null){label=label||(kind==='complete'?'Result recorded':kind==='received'?'Received':'Updated');if(refined())label=systemRecordLabel(cell,role,kind,label,at);timeline.records.push({cell,role,at,updated,kind,label});}
function work(cell,role,start,end,direction=null){const code=timeline.code||'';if(refined())direction=direction||(['design-return','final-return'].includes(code)||(code==='verify'&&start<6000)?'return':code.startsWith('network')?'cycle':'outbound');timeline.work.push({cell,role,start,end,direction});}
function message(pathProvider,{reverse=false,color='#27ddc8',at=300,travel=1550,toCell=null,toRole='director',receipt='Received',toTool=null}={}){
 const g=el('g');const halo=el('circle',{r:13,fill:color,opacity:.28,filter:'url(#glow)'}),tail=el('circle',{r:2.5,fill:color,opacity:.45}),dot=el('circle',{r:4.5,fill:color});g.append(halo,tail,dot);$('signals').append(g);signals.push({pathProvider,reverse,color,at,travel,g,halo,tail,dot});
 if(toCell){timeline.arrivals.push({cell:toCell,role:toRole,at:at+travel});recAt(toCell,toRole,at+travel+300,false,'received',receipt)}
 if(toTool)timeline.toolArrivals.push({tool:toTool,at:at+travel});
}
function internal(cell,role,reverse=false,at=1200,travel=1450,color='#27ddc8',receipt=null,writeSource=true){
 if(writeSource)recAt(cell,reverse?role:'director',at-800,true,reverse?'complete':'routed',reverse?'Result recorded':'Assignment ready');
 const detail=chapter==='learning'?(receipt||(reverse?'Result received':'Assignment received')):refined()&&cell==='main'?(reverse?{design:'Two-site plan received',engineering:'Capture tools received',quality:timeline.code==='final-return'?'Access evidence received':'Access gap received'}[role]:{design:'Survey goal received',engineering:'Capture preparation assigned',quality:['verify','verify-status'].includes(timeline.code)?'Focused access check':'Access review assigned'}[role]):null;message(()=>cellNodes[cell].route(role),{reverse,at,travel,color,toCell:cell,toRole:reverse?'director':role,receipt:detail||receipt||(reverse?'Result received':'Assignment received')});Object.assign(signals[signals.length-1],{kind:'internal',role,cell,reverseInternal:reverse});
}
function external(id,reverse=false,at=1200,travel=1450,color='#27ddc8',toCell=null,toRole='director',receipt='Received',toTool=null){
 const ends={'caller-wire':[null,'main'],'network-infrastructure':['main','infrastructure'],'network-publishing':['main','publishing'],'network-research':['main','research-cell'],'network-care':['care','infrastructure'],'network-archive-brief':['infrastructure','publishing'],'exchange-left':['left',null],'exchange-right':[null,scene==='exchange'?'right':null],'review-wire':['main',null],'proposal-wire':[null,null],'guidance-wire':[null,null],'guidance-director-wire':[null,'main']}[id]||[null,null];
 toCell=toCell||ends[reverse?0:1];if(refined()&&id==='caller-wire'&&reverse)toTool='caller';message(()=>$(id),{reverse,at,travel,color,toCell,toRole,receipt,toTool});const item=signals[signals.length-1];item.kind='external';item.wireId=id;if(chapter==='director'&&id==='caller-wire'&&reverse)timeline.callerStatus.push({at:at+travel,text:directorCallerReport(timeline.code)});if(refined()){item.caption=id==='network-infrastructure'?(reverse?'Archive reference':'Checked evidence'):id==='network-publishing'?(reverse?'Briefing draft':'Briefing request'):id==='network-archive-brief'?'Archive reference':null;if(item.caption){item.labelNode=el('text',{'text-anchor':'middle',class:'network-payload',fill:color},item.caption);item.g.append(item.labelNode);}}
}
function baseline(cell,entries){for(const entry of entries){const [role,updated,label]=typeof entry==='string'?[entry,false,entry==='director'?'Request held':'Assignment held']:entry;recAt(cell,role,0,updated,updated?'complete':'received',label||(updated?'Result recorded':'Assignment received'))}}
function mail(index,at,returned=false,status=null,messageId=null){const item={index,at,returned,status:status||(returned?'Result ready':'Request waiting')};if(messageId)item.messageId=messageId;timeline.mail.push(item)}
function caption(text,at=0){timeline.caption.push({text,at})}
function tool(id,at=0){timeline.tools.push({id,at})}
function toolRecord(at,label,complete=false){timeline.toolRecords.push({at,label,complete})}
function decision(text,at=0){timeline.decisions.push({text,at})}
function personRecord(role,at,label,updated=false,kind=updated?'updated':'received'){timeline.personRecords.push({role,at,label,updated,kind});}
function finishTimeline(){timeline.records.sort((a,b)=>a.at-b.at);timeline.mail.sort((a,b)=>a.at-b.at);timeline.caption.sort((a,b)=>a.at-b.at);duration=Math.max(6200,timeline.durationFloor||0,...(timeline.personRecords||[]).filter(e=>e.at>0).map(e=>e.at+1100),...signals.map(e=>e.at+e.travel+850),...timeline.records.filter(e=>e.at>0).map(e=>e.at+1100),...timeline.work.map(e=>e.end+450),...timeline.toolRecords.filter(e=>e.at>0).map(e=>e.at+1100),...timeline.tools.map(e=>(e.end??e.at)+650),...timeline.decisions.map(e=>e.at+1100),...timeline.caption.map(e=>e.at+1100),...timeline.mail.map(e=>e.at+1100),...timeline.reveal.map(e=>e.at+1300));}
function configureDirectorWork(code){
 if(code==='intake'){
  external('caller-wire',false,300,1600,'#27ddc8','main','director','Goal + checks recorded');recAt('main','director',3500,true,'updated','Acknowledgment ready');external('caller-wire',true,4500,1600,'#e9bd79');return true;
 }
 if(code==='parallel-status'){
  work('main','design',0,3000,'return');internal('main','design',true,4200,1500,'#dbeaf7');recAt('main','director',7600,true,'evaluated','Plan usable');recAt('main','director',8800,true,'routed','Tools + access assigned');
  internal('main','engineering',false,9800,1450,'#27ddc8',null,false);internal('main','quality',false,10250,1450,'#27ddc8',null,false);work('main','engineering',12250,14900,'outbound');work('main','quality',12700,15400,'outbound');
  recAt('main','director',13200,true,'updated','Plan ready; checks underway');external('caller-wire',true,14100,1600,'#e9bd79');return true;
 }
 if(code==='partial-return'){
  work('main','engineering',0,3000,'return');internal('main','engineering',true,4200,1450,'#dbeaf7');work('main','quality',0,11500,'outbound');recAt('main','director',7500,true,'evaluated','Tools accepted; access pending');recAt('main','director',8600,true,'updated','Tools ready; access pending');external('caller-wire',true,9500,1600,'#e9bd79');return true;
 }
 if(code==='verify-status'){
  work('main','quality',0,3000,'return');internal('main','quality',true,4200,1450,'#dbeaf7');recAt('main','director',7500,true,'evaluated','Access still unverified');internal('main','quality',false,9800,1450,'#27ddc8','Focused access check');work('main','quality',12250,15400,'outbound');recAt('main','director',12650,true,'updated','Access check in progress');external('caller-wire',true,13600,1600,'#e9bd79');return true;
 }
 if(code==='conclude'){
  recAt('main','director',750,true,'complete','Checked package ready');external('caller-wire',true,1800,1800,'#27ddc8');recAt('main','director',4700,true,'complete','Request concluded');return true;
 }
 return false;
}
function configureCell(code){makeScene('cell');newTimeline();addInstructionOwnership();timeline.code=code;const network=code.startsWith('network'),learning=code.startsWith('learn-');
 applyMainView(code);
 for(const[id,x,y,s]of neighborViews())setCamera(id,x,y,s,network?1:0);
 $('caller').setAttribute('opacity',!network&&!learning&&code!=='overview'?1:0);$('caller-wire').setAttribute('opacity',!network&&!learning&&code!=='overview'?.28:0);
 for(const id of ['review-actor','instructions-actor','learning-decision','review-wire','proposal-wire','guidance-wire','guidance-director-wire'])$(id).setAttribute('opacity',0);
 for(const p of $('world').querySelectorAll('.network-wire'))p.setAttribute('opacity',network?.28:0);
 for(const label of cellNodes.main.g.querySelectorAll('text'))label.style.opacity=network?'0':'1';$('wide-main-label').setAttribute('opacity',network?1:0);if(cellNodes.main.domainTitle)cellNodes.main.domainTitle.style.opacity=code==='overview'||code==='learn-observe'?'1':'0';
 for(const r of roles){const n=cellNodes.main.rs[r.id];n.group.setAttribute('opacity',1);if(n.label)n.label.textContent=r.name;}
 if(cellNodes.main.rs.synthesis)cellNodes.main.rs.synthesis.group.setAttribute('opacity',0);
 cellNodes.main.mem.removeAttribute('transform');
 if(code==='overview')return;
 if(chapter==='director'&&configureDirectorWork(code))return;
 if(network&&refined()){
  if(code==='network'){
   recAt('main','director',900,true,'routed','Archive requested');external('network-infrastructure',false,1800,1500,'#7d9fe2','infrastructure','director','Checked evidence received');work('infrastructure','engineering',4200,7000,'cycle');recAt('infrastructure','director',7400,true,'complete','Archive reference ready');external('network-infrastructure',true,8200,1500,'#27ddc8','main','director','Archive reference received');recAt('main','director',11000,true,'evaluated','Archive reference linked');
  }else{
   recAt('main','director',900,true,'routed','Briefing requested');external('network-publishing',false,1800,1400,'#f58eab','publishing','director','Briefing request received');recAt('infrastructure','director',3000,true,'updated','Archive reference shared');external('network-archive-brief',false,4000,1400,'#7d9fe2','publishing','director','Archive reference linked');work('publishing','design',6400,9100,'cycle');recAt('publishing','director',9500,true,'complete','Briefing draft ready');external('network-publishing',true,10300,1400,'#f58eab','main','director','Briefing draft received');recAt('main','director',13000,true,'evaluated','Briefing draft linked');
  }return;
 }
 if(network){
  baseline('main',[['director',true,'Outcome retained']]);recAt('main','director',900,true,'routed','Shared work ready');external('network-infrastructure',false,1800,1500,'#7d9fe2','infrastructure');work('infrastructure','engineering',4200,6200);recAt('infrastructure','director',6500,true,'complete','Result recorded');external('network-infrastructure',true,7300,1500,'#27ddc8','main','director','Return received');recAt('main','director',10050,true,'evaluated','Return evaluated');
  if(code==='network-many'){
   work('publishing','design',0,700);recAt('publishing','director',1100,true,'complete','Result recorded');external('network-publishing',true,1950,1550,'#f58eab','main','director','Publishing returned');
   recAt('main','director',4750,true,'evaluated','Publishing evaluated');recAt('main','director',5750,true,'routed','Research request ready');external('network-research',false,6600,1550,'#e9bd79','research-cell');work('research-cell','research',9000,11050);recAt('research-cell','director',11450,true,'complete','Result recorded');external('network-research',true,12350,1550,'#e9bd79','main','director','Research returned');recAt('main','director',15150,true,'evaluated','Returns evaluated');
  }return;
 }
 if(code==='intake'){external('caller-wire',false,300,1600,'#27ddc8','main','director','Intent recorded');return}
 if(learning){configureLearning(code);return}
 baseline('main',[['director',false,'Intent recorded']]);
 if(code==='design'){internal('main','design',false,1300);work('main','design',3750,7100);return}
 if(code==='design-return'&&refined()){baseline('main',[['design',false,'Assignment held']]);work('main','design',0,3000,'return');internal('main','design',true,4200,1500,'#dbeaf7');recAt('main','director',7600,true,'evaluated','Outcome evaluated');return}
 if(code==='design-return'){baseline('main',[['design',false,'Assignment held']]);work('main','design',0,1400);internal('main','design',true,2600,1500,'#dbeaf7');recAt('main','director',5300,true,'evaluated','Outcome evaluated');return}
 if(code==='parallel'||code==='parallel-status'){
  baseline('main',[['design',code==='parallel',code==='parallel'?'Result recorded':'Assignment held']]);let start=1400;
  if(code==='parallel-status'){work('main','design',0,1000);internal('main','design',true,2100,1450,'#dbeaf7');recAt('main','director',4750,true,'evaluated','Outcome evaluated');start=6400}else baseline('main',[['director',true,'Outcome evaluated']]);
  recAt('main','director',start-850,true,'routed','Assignments ready');
  internal('main','engineering',false,start,1450,'#27ddc8',null,false);internal('main','quality',false,start+450,1450,'#27ddc8',null,false);work('main','engineering',start+2350,start+5100);work('main','quality',start+2800,start+5500);
  if(code==='parallel-status'){recAt('main','director',8500,true,'updated','Status recorded');external('caller-wire',true,9350,1500,'#e9bd79');}return;
 }
 if(code==='partial-return'){baseline('main',[['design',true],'engineering','quality']);work('main','engineering',0,1100);work('main','quality',0,9200);internal('main','engineering',true,2300,1450,'#dbeaf7');recAt('main','director',5000,true,'evaluated','Progress evaluated');recAt('main','director',6000,true,'updated','Status recorded');external('caller-wire',true,6850,1500,'#e9bd79');return}
 if(code==='verify'&&refined()){
  work('main','engineering',0,3000,'return');internal('main','engineering',true,4200,1450,'#dbeaf7');work('main','quality',1400,4400,'return');internal('main','quality',true,5600,1450,'#dbeaf7');recAt('main','director',9000,true,'evaluated','Results evaluated');internal('main','quality',false,10800,1450,'#27ddc8','Focused access check');work('main','quality',13300,16000,'outbound');return;
 }
 if(code==='verify'||code==='verify-status'){
  baseline('main',[['design',true],'engineering','quality']);
  if(code==='verify'){work('main','engineering',0,900);internal('main','engineering',true,2100,1450,'#dbeaf7')}else baseline('main',[['engineering',true],['director',true,'Progress retained']]);
  work('main','quality',0,1400);internal('main','quality',true,2800,1450,'#dbeaf7');recAt('main','director',5500,true,'evaluated','Results evaluated');internal('main','quality',false,7500,1450,'#27ddc8','Follow-up received');work('main','quality',9800,12200);if(code==='verify-status'){recAt('main','director',8500,true,'updated','Status recorded');external('caller-wire',true,9350,1500,'#e9bd79');}return;
 }
 if(code==='final-return'&&refined()){work('main','quality',0,3000,'return');internal('main','quality',true,4200,1500,'#dbeaf7');recAt('main','director',7600,true,'evaluated','All three checks met');return}
 if(code==='final-return'){baseline('main',[['design',true],['engineering',true],'quality',['director',true,'Follow-up held']]);work('main','quality',0,1450);internal('main','quality',true,2700,1500,'#dbeaf7');recAt('main','director',5400,true,'evaluated','Final check evaluated');return}
 if(code==='conclude'){baseline('main',[['design',true],['engineering',true],['quality',true],['director',true,'Checks retained']]);recAt('main','director',750,true,'complete','Outcome concluded');external('caller-wire',true,1800,1800,'#27ddc8');return}
}
function configureLearning(code){
 const amber='#e9bd79';
 if(code==='learn-observe'){baseline('main',[['director',true,'Late follow-ups retained'],['design',true,'Earlier briefs retained']]);return}
 if(code==='learn-review'){internal('main','research',false,1400,1450,amber,'Cases + question received');work('main','research',3900,7000,'outbound');return}
 if(code==='learn-propose'){work('main','research',0,3000,'return');internal('main','research',true,4200,1500,amber,'Scoped proposal received');tool('learning-decision',6000);decision('Proposal received · decision pending',6000);recAt('main','director',7000,true,'updated','Owner decision pending');return}
 tool('learning-decision');
 if(code==='learn-decide'){
  decision('Accept: multi-site planning only',2200);recAt('main','director',2600,true,'updated','Scoped guidance accepted');tool('instructions-actor',3300);timeline.instructionRecords.push({at:4600,updated:true,kind:'maintained',label:'Per-site needs in brief'});recAt('main','director',6500,true,'updated','Accepted guidance maintained');decision('Accepted guidance maintained',6600);return;
 }
 tool('instructions-actor');
 if(code==='learn-reuse'){
  $('caller').setAttribute('opacity',1);$('caller-wire').setAttribute('opacity',.28);external('caller-wire',false,300,1450,'#27ddc8','main','director','Later matching request');tool('guidance-director-wire',2200);external('guidance-director-wire',false,2900,1450,amber,'main','director','Matching guidance loaded');internal('main','design',false,6800,1450,'#27ddc8','Plan + per-site needs received');work('main','design',9250,16050,'cycle');internal('main','design',true,17250,1450,'#dbeaf7','Per-site plan received');recAt('main','director',20550,true,'evaluated','Requirements checked; access unchecked');return;
 }
 if(code==='learn-grow'){
  recAt('main','director',800,true,'updated','Internal-summary role proposed');decision('Proposed: evidence-linked summaries',800);decision('Accept: internal-summary responsibility',3000);recAt('main','director',3500,true,'updated','Summary responsibility accepted');recAt('main','director',5200,true,'updated','Synthesis role + route maintained');decision('Implemented: Synthesis available',6500);timeline.reveal.push({role:'synthesis',at:6500});return;
 }
 if(code==='learn-use'){
  $('caller').setAttribute('opacity',1);$('caller-wire').setAttribute('opacity',.28);external('caller-wire',false,300,1450,'#27ddc8','main','director','Later checked-package request');internal('main','synthesis',false,4300,1450,'#27ddc8','Checked package received');work('main','synthesis',6750,9750,'outbound');work('main','synthesis',10000,13000,'return');internal('main','synthesis',true,14200,1450,'#dbeaf7','Summary + source links received');recAt('main','director',17500,true,'evaluated','Summary and evidence links checked');return;
 }
}

const archiveMessages={request:{name:'Archive request'},ack:{name:'Acceptance'},result:{name:'Archive result'},research:{name:'Other research'},person:{name:'Other decision'}};
function archiveTransport(id,reverse,at,travel,color,toCell=null,receipt='Received',messageId='request'){
 external(id,reverse,at,travel,color,toCell,'director',receipt);const signal=signals[signals.length-1];signal.messageId=messageId;
 signal.labelNode=el('text',{'text-anchor':'middle',class:'network-payload transport-payload',fill:color},archiveMessages[messageId].name);signal.g.append(signal.labelNode);
 if(!toCell)timeline.toolArrivals.push({tool:'mail-'+timeline.exchangeIndex,at:at+travel});
}
const humanMessages={question:{name:'Draft question'},reply:{name:'Approve draft'},outcome:{name:'Schedule draft'},research:{name:'Other research'},infrastructure:{name:'Other archive'}};
function humanTransport(id,reverse,at,travel,destination,messageId,receipt='Received'){
 const color=destination==='source'?'#27ddc8':'#e9bd79';external(id,reverse,at,travel,color,destination==='source'?'left':null,'director',receipt,destination==='person'?'person':null);
 const signal=signals[signals.length-1];signal.messageId=messageId;signal.labelNode=el('text',{'text-anchor':'middle',class:'network-payload transport-payload',fill:color},humanMessages[messageId].name);signal.g.append(signal.labelNode);
 if(destination==='queue')timeline.toolArrivals.push({tool:'mail-'+timeline.exchangeIndex,at:at+travel});
}
function addPersonOwnership(){
 for(const role of ['decision','outcome']){const g=el('g',{class:'ownership-link'}),base=el('path',{class:'ownership-base',fill:'none'}),ink=el('path',{class:'ownership-ink',fill:'none',pathLength:1}),dot=el('circle',{r:3.5,class:'writing-dot'});g.append(base,ink,dot);$('ownership').append(g);ownerLinks.push({personRole:role,record:$('person-record-'+role),g,base,ink,dot});}
}
function configureHuman(code){
 const q=pairPose('left',code);setCamera('left',q.x,q.y,q.s);timeline.exchangeIndex=code==='human-return'?3:2;addPersonOwnership();
 if(code==='human-overview'){baseline('left',[['director',false,'Preparation decision needed'],['operations',false,'Separate maintenance authorized']]);mail(0,0,false,'Waiting','research');mail(1,0,false,'Waiting','infrastructure');return;}
 if(code==='human-send'){
  recAt('left','director',450,true,'routed','Question: prepare Site 2 draft');humanTransport('exchange-left',false,1450,1600,'queue','question');mail(2,3350,false,'Waiting','question');recAt('left','director',4350,true,'updated','Question sent; decision pending');timeline.durationFloor=7000;return;
 }
 if(code==='human-wait'){work('left','operations',1400,7200,'outbound');timeline.durationFloor=7200;return;}
 if(code==='human-decide'){
  mail(2,800,false,'Picked up','question');humanTransport('exchange-right',false,800,1600,'person','question');personRecord('decision',2700,'Question received; decision pending');personRecord('decision',6800,'Approve: Site 2 schedule draft',true,'decision');timeline.durationFloor=10200;return;
 }
 if(code==='human-return'){
  humanTransport('exchange-right',true,600,1600,'queue','reply');mail(3,2500,true,'Waiting','reply');mail(3,3800,true,'Picked up','reply');humanTransport('exchange-left',true,3800,1600,'source','reply','Reply received: approve draft');recAt('left','director',8450,true,'evaluated','Site 2 draft preparation authorized');recAt('left','director',9600,true,'routed','Prepare Site 2 schedule draft');internal('left','engineering',false,10650,1600,'#27ddc8','Draft task received',false);work('left','engineering',13400,16200,'outbound');timeline.durationFloor=17000;return;
 }
 if(code==='human-conclude'){
  work('left','engineering',0,1200,'outbound');work('left','engineering',1300,4300,'return');recAt('left','engineering',4600,true,'complete','Site 2 schedule draft ready');internal('left','engineering',true,5650,1600,'#dbeaf7','Schedule draft received',false);recAt('left','director',10500,true,'evaluated','Authorized draft evaluated');recAt('left','director',11600,true,'routed','Outcome report prepared');humanTransport('exchange-left',false,12650,1600,'queue','outcome');mail(2,14550,true,'Waiting','outcome');recAt('left','director',14600,true,'updated','Outcome report sent');mail(2,16100,true,'Picked up','outcome');humanTransport('exchange-right',false,16100,1600,'person','outcome');personRecord('outcome',18000,'Site 2 schedule draft received');timeline.durationFloor=20500;return;
 }
}
function layoutHuman(){
 layoutCommunication();const phone=layoutMode()==='phone';$('person').setAttribute('transform',phone?'translate(445 185)':'translate(1380 450)');$('right-domain').textContent='Visit owner · person';$('person-scope').setAttribute('x',phone?445:1380);$('person-scope').setAttribute('y',phone?45:225);$('mail-2').querySelector('.exchange-text').textContent='Visit owner';
}
function humanStateAt(t){
 const code=timeline.code;
 if(code==='human-return')return t>=13400?'Source: draft authorized · Engineering working':t>=9070?'Source: draft-only scope checked':t>=6320?'Source: reply received · scope check pending':'Source: decision still pending';
 if(code==='human-conclude')return t>=15220?'Source: outcome report sent':t>=11120?'Source: authorized draft evaluated':'Source: authorized draft in progress';
 if(code==='human-decide')return t>=7420?'Source: decision pending · Person: approve draft only':t>=3320?'Person: reviewing · Source: decision pending':'Source: decision pending · Schedule held';
 return'Approval needed · Schedule preparation not started';
}
function renderHuman(t){
 const phone=layoutMode()==='phone',q=camera.left.value,c=cellNodes.left;const domain=[...c.g.querySelectorAll('text')].find(n=>n.textContent==='Fieldwork');if(domain)domain.style.opacity='0';
 for(const[role,r]of Object.entries(c.rs)){if(!r.label)continue;const e=latest(timeline.records.filter(v=>v.role===role),t),shown=role==='engineering'&&e||role==='operations'&&timeline.code==='human-wait';r.label.style.opacity=shown?'1':'0';r.label.style.fontSize=(18/q.s)+'px';const p=c.point(role);r.label.setAttribute('x',p.x);r.label.setAttribute('y',p.y-20/q.s);r.label.setAttribute('text-anchor','middle');}
 const label=[...c.g.querySelectorAll('text')].find(n=>n.textContent==='Director');if(label){label.style.fontSize=(16/q.s)+'px';label.setAttribute('x',-20/q.s);label.setAttribute('y',-12/q.s);label.setAttribute('text-anchor','end');}
 for(let i=0;i<4;i++){const row=$('mail-'+i),m=latest(timeline.mail.filter(e=>e.index===i),t),info=m?humanMessages[m.messageId]:null;row.querySelector('.mail-payload').textContent=info?.name||'No message';const a=latest(timeline.toolArrivals.filter(e=>e.tool==='mail-'+i),t),age=a?t-a.at:1e6;row.querySelector('.mail-catch').setAttribute('r',3.5+(reduced?0:Math.exp(-age/650)*3.5));}
 for(const role of ['decision','outcome']){const g=$('person-record-'+role),events=timeline.personRecords.filter(e=>e.role===role),raw=latest(events,t),e=raw?{...raw,existing:events.some(v=>v.at<raw.at)}:null,park=role==='decision'&&timeline.code==='human-conclude'&&t>=17700;g.setAttribute('transform',phone?`translate(330 ${park?700:290})`:`translate(1250 ${role==='decision'?665:760})`);renderRecord(g,e,t);}
 const a=latest(timeline.toolArrivals.filter(e=>e.tool==='person'),t),age=a?t-a.at:1e6,pulse=Math.exp(-age/900);$('person').querySelector('.person-head').setAttribute('r',29+(reduced?0:pulse*8));$('person').querySelector('.person-catch').setAttribute('opacity',reduced?0:pulse*.18);
 $('readiness').hidden=true;$('cue-checks').textContent=humanStateAt(t);$('exchange-state').textContent=humanStateAt(t);
}
function configureCommunication(code){
 for(const id of ['left','right']){const q=pairPose(id,code);setCamera(id,q.x,q.y,q.s);}
 timeline.exchangeIndex=['exchange-work','exchange-return','exchange-evaluate'].includes(code)?3:1;
 if(code==='exchange-overview'){baseline('left',[['director',false,'Archive commitment open']]);mail(0,0,false,'Waiting','research');mail(2,0,false,'Waiting','person');return}
 if(code==='exchange-send'){
  recAt('left','director',600,true,'routed','Prepared: retain checked evidence');archiveTransport('exchange-left',false,1600,1600,'#27ddc8');mail(1,3500,false,'Waiting','request');recAt('left','director',3600,true,'updated','Sent; acknowledgment pending');return;
 }
 if(code==='exchange-pickup'){
  mail(1,900,false,'Picked up','request');archiveTransport('exchange-right',false,900,1600,'#f58eab','right','Archive task received');return;
 }
 if(code==='exchange-work'){
  recAt('right','director',600,true,'updated','Accepted; archive pending');archiveTransport('exchange-right',true,1600,1450,'#f58eab',null,'Received','ack');recAt('right','director',1900,true,'routed','Accepted; retention assigned');internal('right','engineering',false,2800,1200,'#f58eab','Checked package received',false);
  mail(3,3350,false,'Waiting','ack');mail(3,4300,false,'Picked up','ack');archiveTransport('exchange-left',true,4300,1450,'#e9bd79','left','Accepted; archive pending','ack');work('right','engineering',5200,8000,'outbound');return;
 }
 if(code==='exchange-return'){
  work('right','engineering',0,3000,'return');recAt('right','engineering',3400,true,'complete','Checked evidence retained');internal('right','engineering',true,4300,1250,'#dbeaf7','Retained-item list received',false);recAt('right','director',6800,true,'evaluated','Local archive result checked');recAt('right','director',7800,true,'complete','Archive reference ready');archiveTransport('exchange-right',true,8700,1550,'#f58eab',null,'Received','result');mail(3,10550,true,'Waiting','result');return;
 }
 if(code==='exchange-evaluate'){
  mail(3,900,true,'Picked up','result');archiveTransport('exchange-left',true,900,1550,'#27ddc8','left','Archive result received','result');recAt('left','director',3650,true,'routed','Compare package, items and reference');internal('left','quality',false,4550,1200,'#27ddc8','Reference + item list received',false);work('left','quality',6900,9500,'outbound');work('left','quality',10000,13000,'return');recAt('left','quality',13400,true,'complete','Package, items and reference match');internal('left','quality',true,14300,1200,'#dbeaf7','Archive check returned',false);recAt('left','director',16800,true,'evaluated','Archive commitment met');timeline.durationFloor=19600;return;
 }
}
function layoutCommunication(){
 const box=communicationBox(),phone=layoutMode()==='phone';$('exchange').setAttribute('transform',`translate(${box.x} ${box.y})`);$('exchange').querySelector('rect').setAttribute('width',box.w);$('exchange').querySelector('rect').setAttribute('height',box.h);const title=$('exchange').querySelector('.exchange-label');title.setAttribute('x',box.w/2);title.setAttribute('y',-25);
 for(let i=0;i<4;i++){const slot=communicationSlot(i),row=$('mail-'+i);row.setAttribute('transform',`translate(${slot.x-box.x} ${slot.y-box.y})`);row.querySelector('rect').setAttribute('width',slot.w);row.querySelector('rect').setAttribute('height',slot.h);row.querySelector('.exchange-text').setAttribute('x',24);row.querySelector('.exchange-text').setAttribute('y',20);row.querySelector('.mail-status').setAttribute('x',24);row.querySelector('.mail-status').setAttribute('y',62);}
 for(const[id,x]of [['left-domain',phone?155:730],['right-domain',phone?445:1380]]){$(id).setAttribute('x',x);$(id).setAttribute('y',phone?20:200);}
 $('exchange-state').setAttribute('x',phone?300:1075);$('exchange-state').setAttribute('y',phone?670:690);
}
function configureExchange(code,human){makeScene(human?'human':'exchange');newTimeline();timeline.code=code;if(chapter==='communication'){configureCommunication(code);return}if(chapter==='human'){configureHuman(code);return}caption('Each system keeps its own work.');
 timeline.exchangeIndex=human?(code==='human-return'?3:2):['exchange-work','exchange-return','exchange-evaluate'].includes(code)?3:1;
 if(human){
  if(code==='human-overview'){caption('A person uses the same addressed exchange.');return}
  baseline('left',[['director',false,'Decision needed']]);
  if(code==='human-send'){recAt('left','director',450,true,'routed','Question prepared');external('exchange-left',false,1450,1600,'#e9bd79');mail(2,3350,false,'Decision requested');caption('Context, proposed action and a clear decision.',3350)}
  if(code==='human-wait'){baseline('left',[['engineering',false,'Other work authorized']]);mail(2,0,false,'Awaiting a reply');caption('Decision pending. The dependent action waits.');work('left','engineering',800,7000)}
  if(code==='human-decide'){mail(2,0,false,'Decision requested');external('exchange-right',false,750,1650,'#e9bd79',null,'director','Received','person');mail(2,750,false,'Picked up');caption('The person reviews the concrete proposal.',2850);caption('Explicit reply: “Approve this action.”',5200);tool('person-decision',5200);timeline.toolArrivals.push({tool:'person-decision',at:5200})}
  if(code==='human-return'){tool('person-decision');external('exchange-right',true,1000,1550,'#e9bd79');mail(3,2850,true,'Explicit approval');caption('The person’s actual answer returns.',2850);mail(3,3900,true,'Picked up');external('exchange-left',true,3900,1550,'#27ddc8','left','director','Decision recorded');recAt('left','director',6700,true,'evaluated','Authority checked');internal('left','quality',false,8500,1200,'#27ddc8','Authorized work');work('left','quality',10850,13100);caption('The reply authorizes this action. Work resumes.',10850)}
  if(code==='human-conclude'){baseline('left',[['director',true,'Decision recorded'],['quality',false,'Authorized work held']]);work('left','quality',0,1150);internal('left','quality',true,2400,1200,'#dbeaf7');recAt('left','director',4800,true,'evaluated','Outcome evaluated');recAt('left','director',5800,true,'complete','Report recorded');external('exchange-left',false,6650,1400);mail(2,8350,true,'Outcome reported');mail(2,9350,true,'Picked up');external('exchange-right',false,9350,1450,'#27ddc8',null,'director','Received','person');caption('The person receives the outcome of the action.',11150)}
 }else{
  if(code==='exchange-overview')return;baseline('left',[['director',false,'Commitment held']]);
  if(code==='exchange-send'){recAt('left','director',450,true,'routed','Shared work ready');external('exchange-left',false,1450,1600);mail(1,3350,false,'Request waiting');caption('To Infrastructure, with context and a return route.',3350)}
  if(code==='exchange-pickup'){mail(1,0,false,'Request waiting');external('exchange-right',false,700,1600,'#f58eab','right','director','Request recorded');mail(1,700,false,'Picked up');internal('right','engineering',false,4400,1200,'#f58eab');work('right','engineering',6550,8500);caption('Only Infrastructure picks up its addressed request.',2650)}
  if(code==='exchange-work'){baseline('right',[['director',false,'Request held'],['engineering',false,'Assignment held']]);work('right','engineering',0,7700);recAt('right','director',450,true,'updated','Acceptance recorded');external('exchange-right',true,1450,1450,'#f58eab');mail(3,3200,false,'Accepted by recipient');mail(3,4200,false,'Picked up');external('exchange-left',true,4200,1450,'#e9bd79','left','director','Acceptance recorded');caption('Acknowledged. Infrastructure owns its bounded work.',6050)}
  if(code==='exchange-return'){baseline('right',[['director',false,'Work in progress'],['engineering',false,'Assignment held']]);work('right','engineering',0,1150);internal('right','engineering',true,2450,1250,'#dbeaf7');recAt('right','director',4900,true,'evaluated','Result evaluated');recAt('right','director',5900,true,'complete','Return recorded');external('exchange-right',true,7000,1550,'#f58eab');mail(3,8850,true,'Result and evidence');caption('The result is addressed back to Fieldwork.',8850)}
  if(code==='exchange-evaluate'){baseline('right',[['director',true,'Return retained']]);mail(3,0,true,'Result and evidence');mail(3,800,true,'Picked up');external('exchange-left',true,800,1550,'#27ddc8','left','director','Return recorded');internal('left','quality',false,4400,1200);work('left','quality',6450,8400);internal('left','quality',true,10200,1200,'#dbeaf7');recAt('left','director',12600,true,'evaluated','Commitment evaluated');caption('Fieldwork evaluates the result against its commitment.',12600)}
 }
}
function updateWires(){const phone=layoutMode()==='phone';if(scene==='cell'){
 const d=globalPoint('main'),caller=phone?[45,300]:[480,455];$('caller-wire').setAttribute('d',`M${caller} C${caller[0]+(phone?80:145)},${caller[1]-45} ${d[0]-(phone?70:105)},${d[1]-38} ${d}`);
 for(const p of $('world').querySelectorAll('.network-wire')){const a=globalPoint(p.dataset.from),b=globalPoint(p.dataset.to);p.setAttribute('d',`M${a} Q${(a[0]+b[0])/2+20},${(a[1]+b[1])/2-55} ${b}`)}
 if(phone){$('review-wire').setAttribute('d',`M${d} C150,220 40,360 40,500 L40,660 H150`);$('proposal-wire').setAttribute('d','M150,660 C40,660 40,710 40,740 L40,884 H120');$('guidance-wire').setAttribute('d','M120,884 H40 V820 H585 V670 H441');$('guidance-director-wire').setAttribute('d',`M441,670 H570 V150 C570,90 ${d[0]},140 ${d}`);}
 else{$('review-wire').setAttribute('d',`M${d} Q830,325 730,365`);$('proposal-wire').setAttribute('d','M730,365 C1030,330 970,600 1100,770');$('guidance-wire').setAttribute('d','M1100,770 Q913,717 726,594');$('guidance-director-wire').setAttribute('d',`M726,594 C840,620 ${d[0]-90},${d[1]-95} ${d}`);}
 if(chapter==='learning'){const a=paperPoint($('instruction-record'),14,0);$('guidance-director-wire').setAttribute('d',phone?`M${a} H570 V50 C570,-20 ${d[0]},0 ${d}`:`M${a} H1500 V80 C1500,20 ${d[0]},100 ${d}`);}
 }else{if(chapter==='human'){const a=globalPoint('left'),b=personPoint(),slot=communicationSlot(timeline.exchangeIndex),y=slot.y+slot.h/2;
 if(phone){const left=timeline.exchangeIndex%2===0;$('exchange-left').setAttribute('d',left?`M${a} C${a[0]-60},${a[1]+20} 20,${a[1]+25} 20,${a[1]+60} V${y} H${slot.x}`:`M${a} C${a[0]-60},${a[1]+20} 20,${a[1]+25} 20,${a[1]+60} V418 H300 V${y} H${slot.x}`);$('exchange-right').setAttribute('d',left?`M${slot.x+slot.w},${y} H300 V418 H585 V${b[1]} C585,${b[1]-40} ${b[0]+40},${b[1]} ${b}`:`M${slot.x+slot.w},${y} H585 V${b[1]} C585,${b[1]-40} ${b[0]+40},${b[1]} ${b}`);}
 else{$('exchange-left').setAttribute('d',`M${a} C${a[0]+120},${a[1]-45} 900,${y} ${slot.x},${y}`);$('exchange-right').setAttribute('d',`M${slot.x+slot.w},${y} C1250,${y} ${b[0]-120},${b[1]-45} ${b}`);}return;}
 if(chapter==='communication'){const a=globalPoint('left'),b=globalPoint('right'),slot=communicationSlot(timeline.exchangeIndex),y=slot.y+slot.h/2;if(phone){$('exchange-left').setAttribute('d',`M${a} C20,${a[1]} 20,418 20,418 H300 V${y} H${slot.x}`);$('exchange-right').setAttribute('d',`M${slot.x+slot.w},${y} H585 V${b[1]} C585,${b[1]-40} ${b[0]+40},${b[1]} ${b}`);}else{$('exchange-left').setAttribute('d',`M${a} C${a[0]+120},${a[1]-45} 900,${y} ${slot.x},${y}`);$('exchange-right').setAttribute('d',`M${slot.x+slot.w},${y} C1250,${y} ${b[0]-120},${b[1]-45} ${b}`);}return}const a=globalPoint('left'),b=scene==='exchange'?globalPoint('right'):phone?[300,1260]:[1380,450],row=timeline.exchangeIndex??1,y=(phone?625:292)+20+row*66+26;
 if(phone){$('exchange-left').setAttribute('d',`M${a} C60,350 60,410 60,450 L60,${y} H214`);$('exchange-right').setAttribute('d',`M386,${y} H540 V1110 C540,1220 410,1260 ${b}`);}
 else{$('exchange-left').setAttribute('d',`M${a} C${a[0]+120},${a[1]-45} 900,${y} 978,${y}`);$('exchange-right').setAttribute('d',`M1150,${y} C1230,${y} ${b[0]-120},${b[1]-45} ${b}`);}
 }}
function latest(events,t){let out=null;for(const e of events)if(e.at<=t&&(!out||e.at>=out.at))out=e;return out}
const shortRecordStatus={
 'Commitment held':'Open','Shared work ready':'Prepared','Request recorded':'Recorded','Request held':'Open','Assignment ready':'Assigned','Assignment received':'Received','Acceptance recorded':'Accepted','Result recorded':'Finished','Work in progress':'In progress','Result received':'Returned','Result evaluated':'Evaluated','Return recorded':'Returned','Return retained':'Retained','Commitment evaluated':'Evaluated','Decision needed':'Pending','Question prepared':'Prepared','Decision recorded':'Answered','Authority checked':'Authorized','Authorized work':'Authorized','Other work authorized':'Other work','Authorized work held':'Authorized','Outcome evaluated':'Evaluated','Report recorded':'Reported'
};
const shortMailStatus={'Accepted by recipient':'Accepted','Result and evidence':'Result ready','Decision requested':'Decision needed','Picked up for review':'Picked up'};
function initialSlotStatus(i){return i===0||(chapter==='human'?i===1:i===2)?'Waiting':'Empty';}
function learningRecordLines(node,text,y,width=210){
 const key=text+'|'+y+'|'+width;
 if(node._learningWrapKey===key)return node._learningLines||1;
 const measure=value=>{node.textContent=value;const n=typeof node.getComputedTextLength==='function'?node.getComputedTextLength():value.length*10.2;return Number.isFinite(n)&&n>0?n:value.length*10.2;};
 const words=text.split(/\s+/).filter(Boolean),lines=[];let line='';
 for(const word of words){
  if(measure(word)>width){if(line){lines.push(line);line='';}let part='';for(const letter of word){if(part&&measure(part+letter)>width){lines.push(part);part=letter;}else part+=letter;}line=part;continue;}
  const candidate=line?line+' '+word:word;if(line&&measure(candidate)>width){lines.push(line);line=word;}else line=candidate;
 }
 if(line||!lines.length)lines.push(line);node.replaceChildren(...lines.map((value,i)=>el('tspan',{x:35,y:y+i*18},value)));node.setAttribute('aria-label',text);node._learningRawText=text;node._learningWrapKey=key;node._learningLines=lines.length;return lines.length;
}
function renderRecord(g,e,t){
 const visible=Boolean(e),age=e?t-e.at:0;g.setAttribute('class','record'+(visible?' visible':'')+(e?.updated?' updated':''));g.style.opacity=String(visible?(e.at===0||refined()&&e.existing?1:clamp(age/250)):0);
 const pulse=visible&&e.at>0?Math.max(0,1-age/850):0;g.querySelector('rect').style.strokeWidth=String(1+pulse*1.8);g.querySelector('rect').style.fill=pulse>.15?'#174b42':'#07171f';const paired=scene!=='cell',large=paired||layoutMode()==='phone';g.querySelector('.record-name').setAttribute('y',large?15:12);g.querySelector('.record-status').setAttribute('y',large?35:27);g.querySelector('rect').setAttribute('height',large?40:30);const status=e?(paired?(shortRecordStatus[e.label]||e.label):e.label):'',statusNode=g.querySelector('.record-status'),nameNode=g.querySelector('.record-name');
 if(['learning','communication','human'].includes(chapter)&&layoutMode()==='phone'){const count=learningRecordLines(nameNode,nameNode._learningName??nameNode._learningRawText??nameNode.textContent,15);learningRecordLines(statusNode,status,35+(count-1)*18);}
 else{statusNode.textContent=status;statusNode.removeAttribute('aria-label');nameNode.removeAttribute('aria-label');if(nameNode._learningRawText!==undefined)nameNode.textContent=nameNode._learningName??nameNode._learningRawText;statusNode._learningWrapKey=null;nameNode._learningWrapKey=null;}
 for(const[i,line]of [...g.querySelectorAll('.record-line')].entries()){const amount=e&&e.at>0?clamp((age-(refined()?120:0)-i*100)/260):1;line.style.strokeDasharray='1';line.style.strokeDashoffset=String(1-amount);line.style.stroke=pulse>.1?'#a3ffee':'#74a4b0'}
}
function paperPoint(g,x,y){const p=new DOMPoint(x,y).matrixTransform(g.getCTM()).matrixTransform($('diagram').getCTM().inverse());return[p.x,p.y];}
function renderOwnership(t){
 for(const link of ownerLinks){const events=link.personRole?timeline.personRecords.filter(e=>e.role===link.personRole):link.instructions?timeline.instructionRecords:timeline.records.filter(e=>e.cell===link.cell&&e.role===link.role),e=latest(events,t),c=cellNodes[link.cell];link.g.setAttribute('opacity',e?(link.personRole?1:camera[link.cell]?.value.opacity??1):0);if(!e)continue;
  const a=link.personRole?personPoint():globalPoint(link.cell,link.role),large=scene!=='cell'||layoutMode()==='phone',h=large?40:30,center=paperPoint(link.record,14,h/2),phone=layoutMode()==='phone'&&!timeline.code?.startsWith('network');let end;
  if(phone||chapter==='human')end=paperPoint(link.record,14,0);else if(link.role==='quality')end=paperPoint(link.record,14,h);else if(Math.abs(a[1]-center[1])>Math.abs(a[0]-center[0])*1.2)end=paperPoint(link.record,14,a[1]<center[1]?0:h);else end=paperPoint(link.record,a[0]<center[0]?0:28,h/2);
  const q=camera[link.cell]?.value.s||1;let d;
  if(chapter==='human'){const edge=phone?(link.personRole?585:20):(link.personRole?1580:500);d=link.role==='engineering'?`M${a} C${a[0]+80},${a[1]} ${a[0]+80},70 ${a[0]+80},70 H${edge} V${end[1]} H${end[0]}`:`M${a} C${edge},${a[1]} ${edge},${end[1]-45} ${edge},${end[1]} H${end[0]}`;}
  else if(chapter==='communication'){const edge=phone?(link.cell==='left'?20:585):(link.cell==='left'?500:1580),below=phone?Math.max(a[1]+40,end[1]+55):820;d=`M${a} C${edge},${a[1]} ${edge},${below} ${edge},${below} H${end[0]} V${end[1]}`;}
  else if(link.instructions){d=phone?`M${a} C${a[0]},${a[1]-180} 570,20 570,40 V550 H${end[0]} V${end[1]}`:`M${a} C${a[0]},180 1510,80 1510,200 L1510,650 C1510,700 ${end[0]+75},720 ${end}`;}
  else if(phone){const right=['engineering','quality','operations'].includes(link.role),corridor=right?570:20,up=link.role==='engineering'||link.role==='director',cy=a[1]+(up?-120:20);d=`M${a} C${corridor},${cy} ${corridor},420 ${corridor},520 L${corridor},${end[1]-30} H${end[0]} V${end[1]}`;}
  else if(link.role==='director')d=`M${a} C${a[0]-90*q},${a[1]-15*q} ${end[0]-88*q},${end[1]+13*q} ${end}`;
  else if(link.role==='quality')d=`M${a} C${a[0]+75*q},${a[1]+22*q} ${end[0]+40*q},${end[1]+70*q} ${end}`;
  else d=`M${a} C${a[0]},${a[1]+(end[1]-a[1])*.3} ${end[0]},${end[1]-(end[1]-a[1])*.3} ${end}`;
  link.base.setAttribute('d',d);link.ink.setAttribute('d',d);const age=t-e.at,writing=e.at>0&&age>=0&&age<620,f=clamp(age/240);link.base.style.opacity=timeline.code?.startsWith('network')?'.12':'.48';link.ink.style.opacity=writing?String(1-clamp((age-360)/260)):0;link.ink.style.strokeDasharray='1';link.ink.style.strokeDashoffset=String(1-f);link.dot.setAttribute('opacity',writing&&age<260?1:0);if(writing){const p=pointOn(link.ink,f);link.dot.setAttribute('cx',p[0]);link.dot.setAttribute('cy',p[1]);}
 }
 if(refined()&&index>0)$('phase-action').textContent=systemFocusAt(timeline.code,t);
 renderCueSummary(t);
}
function layoutLearningArtifacts(t){if(chapter!=='learning')return;const phone=layoutMode()==='phone',code=timeline.code;
 if(phone){const base=phoneRecordBase();let x=330,y=base;if(code==='learn-reuse'){const f=ease(clamp((t-6800)/1000));x=330;y=base+(820-base)*f;}else if(['learn-grow','learn-use'].includes(code)){x=330;y=820;}$('instructions-actor').setAttribute('transform',`translate(${x} ${y})`);}
}

function renderLearningState(t){
 const instruction=latest(timeline.instructionRecords,t),settled=instruction&&(instruction.at===0||t>=instruction.at+620);renderRecord($('instruction-record'),instruction?{...instruction,existing:timeline.instructionRecords.some(e=>e.at<instruction.at)}:null,t);$('instructions-label').textContent=settled?(layoutMode()==='phone'?'Maintained guidance':'Maintained planning instructions'):'Guidance to maintain';
 const available=latest(timeline.reveal.filter(e=>e.role==='synthesis'),t);cellNodes.main.rs.synthesis.group.setAttribute('opacity',available?(available.at===0||reduced?1:clamp((t-available.at)/1000)):0);
 const code=timeline.code,growth=['learn-grow','learn-use'].includes(code),proposed=growth&&(code==='learn-use'||t>=800);$('lesson-content').textContent=proposed?'Duty: evidence-linked internal summaries':'Initial brief: per-site evidence needs';$('lesson-scope').textContent=proposed?(code==='learn-use'||t>=5820?'Maintained route: summaries → Synthesis':'Proposed route: summaries → Synthesis'):'Scope: multi-site survey planning';
 for(const role of ['research','design']){const g=cellNodes.main.records[role];if(g.classList.contains('visible')&&growth)g.style.opacity='.5';}
 if(layoutMode()==='phone'&&code==='learn-reuse')$('guidance-director-wire').setAttribute('opacity',clamp((t-2200)/550)*(1-clamp((t-6800)/1000)));
 const cue=$('cue-checks');if(cue)cue.textContent=code==='learn-decide'?(settled?'Guidance maintained':t>=2200?'Accepted · maintenance pending':'Owner decision pending'):code==='learn-grow'?(available?'Synthesis implemented and available':t>=3000?'Accepted · implementation pending':'Optional growth · owner choice required'):code==='learn-use'?'Later encounter · internal summary task':code==='learn-reuse'?(t>=9250?'Design uses the fuller brief · access still needs checking':t>=5270?'Matching guidance loaded; changed brief follows':'Later matching task · guidance will be loaded'):code==='learn-propose'?'Owner decision pending · guidance unchanged':code==='learn-review'?'Bounded review of selected cases':'';
}

function renderCommunication(t){
 for(const[id,c]of Object.entries(cellNodes)){const q=camera[id].value,shown=id==='right'?'engineering':'quality';for(const[role,r]of Object.entries(c.rs)){if(!r.label)continue;const e=latest(timeline.records.filter(v=>v.cell===id&&v.role===role),t);r.label.style.opacity=role===shown&&e?'1':'0';r.label.style.fontSize=(18/q.s)+'px';const p=c.point(role);r.label.setAttribute('x',p.x+(role==='quality'?15/q.s:0));r.label.setAttribute('y',p.y-20/q.s);r.label.setAttribute('text-anchor','middle');}
  const label=[...c.g.querySelectorAll('text')].find(n=>n.textContent==='Director');if(label){label.style.fontSize=(16/q.s)+'px';label.setAttribute('x',-20/q.s);label.setAttribute('y',-12/q.s);label.setAttribute('text-anchor','end');}
 }
 for(let i=0;i<4;i++){const row=$('mail-'+i),m=latest(timeline.mail.filter(e=>e.index===i),t),info=m?archiveMessages[m.messageId]:null;row.querySelector('.mail-payload').textContent=info?.name||'No message';const a=latest(timeline.toolArrivals.filter(e=>e.tool==='mail-'+i),t),age=a?t-a.at:1e6;row.querySelector('.mail-catch').setAttribute('r',3.5+(reduced?0:Math.exp(-age/650)*3.5));}
 const checked=timeline.code==='exchange-evaluate'&&t>=16800,checking=timeline.code==='exchange-evaluate'&&t>=6900;for(let i=0;i<3;i++){$('check-label-'+i).textContent=['Same package','Retained items','Usable reference'][i];$('check-'+i).textContent=checked?'✓':checking?'checking':'open';$('check-'+i).dataset.state=checked?'met':'open';}
 $('readiness').hidden=false;const state=timeline.code==='exchange-work'&&t>=6050?'ACK received · archive pending':timeline.code==='exchange-return'?'Fieldwork still awaits the archive result':checked?'Archive commitment met':timeline.code==='exchange-evaluate'?(t>=2450?'Archive result received; checks remain':t>=900?'Archive result returning to Fieldwork':'Archive result waiting for Fieldwork'):'Request and result stay separately owned';$('cue-checks').textContent=state+(shortViewport()?'\n'+['Same package','Retained items','Usable reference'].map(name=>name+': '+(checked?'✓':checking?'checking':'open')).join(' · '):'');$('exchange-state').textContent=checked?'Archive commitment met':'Two-site survey package';
}

function render(){if(!timeline)return;const t=reduced?duration:elapsed;
 for(const[id,c]of Object.entries(cellNodes)){
  const active={},arrivals={};for(const w of timeline.work)if(w.cell===id&&t>=w.start&&t<=w.end)active[w.role]=refined()?{progress:clamp((t-w.start)/(w.end-w.start)),direction:w.direction||'outbound'}:clamp((t-w.start)/(w.end-w.start));for(const a of timeline.arrivals)if(a.cell===id&&t>=a.at)arrivals[a.role]=Math.min(arrivals[a.role]??Infinity,t-a.at);
  c.update(lifeTime,{active,arrivals,reducedMotion:reduced});
  for(const[role,g]of Object.entries(c.records)){
   const paired=scene!=='cell',context=chapter==='learning'&&id==='main';
   const owner=c.rs[role]?.label?.textContent||roles.find(r=>r.id===role)?.name||'Work';
   const name=refined()?systemRecordName(id,role):role==='director'?'Request':paired?owner:owner+' record',nameNode=g.querySelector('.record-name');
   if(['learning','communication','human'].includes(chapter)&&layoutMode()==='phone'){if(nameNode._learningName!==name){nameNode.textContent=name;nameNode._learningName=name;nameNode._learningWrapKey=null;}}else nameNode.textContent=name;
   const events=timeline.records.filter(e=>e.cell===id&&e.role===role),raw=latest(events,t),e=raw?{...raw,existing:events.some(other=>other.at<raw.at)}:null;renderRecord(g,e,t);
   const p=c.point(role);let offset=recordOffsets[role]||[20,30],scale=context?1.35:1;
   if(context&&role==='engineering')offset=[-15,82];if(context&&role==='research')offset=[20,50];
   let x=p.x+offset[0],y=p.y+offset[1];
   if(context&&layoutMode()!=='phone'&&['research','design','synthesis'].includes(role)){const q=camera[id].value,slot=role==='research'?[650,610]:role==='design'?[650,540]:[1100,330];x=(slot[0]-q.x)/q.s;y=(slot[1]-q.y)/q.s;scale=1.4/q.s;}
   if(chapter==='human'){const q=camera[id].value,slot=humanRecordSlot(role,t);x=(slot[0]-q.x)/q.s;y=(slot[1]-q.y)/q.s;scale=1/q.s;}
   else if(chapter==='communication'){const q=camera[id].value,slot=communicationRecordSlot(id,role,t);x=(slot[0]-q.x)/q.s;y=(slot[1]-q.y)/q.s;scale=1/q.s;}
   else if(paired){const q=camera[id].value,slot=role==='director'?[-95,205]:role==='quality'?[55,205]:[-90,-220];x=slot[0]/q.s;y=slot[1]/q.s;scale=1/q.s;}else if(layoutMode()==='phone'&&id==='main'&&!chapters[chapter].steps[index][2].startsWith('network')){const q=camera[id].value,slot=phoneRecordSlot(role,t);x=(slot[0]-q.x)/q.s;y=(slot[1]-q.y)/q.s;scale=1/q.s;}
   g.setAttribute('transform',`translate(${x} ${y})${scale!==1?' scale('+scale+')':''}`);g.classList.toggle('mini-record',scene==='cell'&&id!=='main');
  }
 }
 renderCamera();layoutLearningArtifacts(t);if(chapter==='human')renderHuman(t);updateWires();renderOwnership(t);renderCallerStatus(t);
 if(scene==='cell'){
  const code=chapters[chapter].steps[index][2],wide=code.startsWith('network'),park=code==='learn-grow'?ease(clamp(t/1300)):code==='learn-use'?1:0;$('review-actor').setAttribute('transform',layoutMode()==='phone'?'translate(-580 295)':`translate(0 ${-90*park})`);
  if(refined()){for(let i=0;i<3;i++)$('check-label-'+i).textContent=['Usable plan','Capture tools','Access evidence'][i];const checks=readinessAt(t),visible=index>0&&!wide&&chapter!=='learning';$('readiness').hidden=!visible;for(let i=0;i<3;i++){const value=$('check-'+i);value.textContent=checks[i];value.dataset.state=checks[i]==='✓'?'met':checks[i]==='?'?'gap':'open';}$('cue-checks').textContent=visible?['Plan','Tools','Access'].map((n,i)=>n+' '+checks[i]).join('   '):'';const arrival=latest(timeline.toolArrivals.filter(e=>e.tool==='caller'),t),age=arrival?t-arrival.at:1e6;$('caller').querySelector('circle').setAttribute('r',5+(reduced?0:Math.exp(-age/650)*5));}
  if(wide){const scale=camera.main.value.s,phone=layoutMode()==='phone',detail=phone?clamp((scale-.60)/.14):clamp((scale-.85)/.5);for(const label of cellNodes.main.g.querySelectorAll('text'))label.style.opacity=detail;if(cellNodes.main.domainTitle)cellNodes.main.domainTitle.style.opacity=0;$('wide-main-label').setAttribute('opacity',layoutMode()==='phone'?clamp((.60-scale)/.10):clamp((.75-scale)/.16));}
  for(const id of ['review-actor','instructions-actor','learning-decision','review-wire','proposal-wire','guidance-wire','guidance-director-wire']){const e=latest(timeline.tools.filter(e=>e.id===id),t);$(id).setAttribute('opacity',e?(e.at===0?1:clamp((t-e.at)/550)):0)}
  const age=t-(latest(timeline.toolArrivals.filter(e=>e.tool==='review'),t)?.at??-1e6),catchPulse=age>=0?Math.exp(-age/900)*Math.sin(Math.min(1,age/650)*Math.PI):0;$('review-actor').querySelector('.review-core').setAttribute('r',6+(reduced?0:catchPulse*6));$('review-actor').querySelector('.review-halo').setAttribute('r',21+(reduced?0:catchPulse*25));
  const tw=latest(timeline.tools.filter(e=>e.id==='review-work'&&t<e.end),t),p=tw?clamp((t-tw.at)/(tw.end-tw.at)):0;for(const path of $('review-branches').querySelectorAll('path')){const b=Number(path.dataset.branch),energy=tw?Math.exp(-Math.pow((p-(.17+b*.16))/.18,2)):0;path.style.opacity=String(.25+energy*.75);path.style.strokeWidth=String(1+energy*1.7)}
  const tr=latest(timeline.toolRecords,t);renderRecord($('review-record'),tr?{...tr,updated:tr.complete}:null,t);
  const dec=latest(timeline.decisions,t);$('decision-label').textContent=dec?.text||'';
  const instructionArrival=latest(timeline.toolArrivals.filter(e=>e.tool==='instructions'),t);if(chapter!=='learning')$('instructions-label').textContent='Maintained instructions';$('instructions-actor').classList.toggle('received',Boolean(instructionArrival));
  if(chapter==='learning')renderLearningState(t);
 }else{
  for(let i=0;i<4;i++){const row=$('mail-'+i),m=latest(timeline.mail.filter(e=>e.index===i),t),status=m?(shortMailStatus[m.status]||m.status):initialSlotStatus(i),consumed=status==='Picked up',available=m&&!consumed;row.querySelector('rect').setAttribute('class','exchange-card'+(consumed?' consumed':available?' '+(m.returned?'return':'selected'):''));row.querySelector('.mail-status').textContent=status;}

  $('exchange-state').textContent=latest(timeline.caption,t)?.text||'';if(chapter==='communication')renderCommunication(t);

 }
 if(refined()&&scene==='cell')for(const p of $('world').querySelectorAll('.network-wire')){p.style.strokeWidth='1.5';p.style.stroke='#668b9a';p.style.opacity=timeline.code.startsWith('network')?'.48':'0';}
 for(const s of signals){const f=(t-s.at)/s.travel,visible=f>=0&&f<=1,path=s.pathProvider();s.g.setAttribute('opacity',visible?1:0);if(!path)continue;if(refined()&&s.wireId?.startsWith('network')&&visible){path.style.stroke=s.color;path.style.strokeWidth='2.6';path.style.opacity='.95';s.dot.setAttribute('r',6.5);s.halo.setAttribute('r',18);}if(s.labelNode){const label=pointOn(path,.5);s.labelNode.setAttribute('x',label[0]);s.labelNode.setAttribute('y',label[1]-22);}const along=x=>s.reverse?1-x:x;const p=pointOn(path,along(ease(clamp(f)))),q=pointOn(path,along(ease(clamp(f-.075))));for(const n of[s.halo,s.dot]){n.setAttribute('cx',p[0]);n.setAttribute('cy',p[1])}s.tail.setAttribute('cx',q[0]);s.tail.setAttribute('cy',q[1]);}
 followShortScene(t);
}
// Derive every entry from the preceding settled story, including direct links,
// back, dots and replay. A record changes only through a visible event in this cue.
function configureWithContinuity(ch,target){
 camera={};let carried=new Map(),reviewRecord=null,slots=new Map(),callerState=null,instructionState=null,decisionState=null,availability=new Map(),personState=new Map();
 for(let i=0;i<=target;i++){
  const code=ch.steps[i][2];
  if(chapter==='communication'||chapter==='human')configureExchange(code,chapter==='human');else configureCell(code);
  const freshBaseline=timeline.records.filter(e=>e.at===0&&!carried.has(e.cell+':'+e.role));
  timeline.records=[...carried.values()].filter(e=>cellNodes[e.cell]?.records[e.role]).map(e=>({...e,at:0})).concat(freshBaseline,timeline.records.filter(e=>e.at>0));
  const freshSlots=timeline.mail.filter(e=>e.at===0&&!slots.has(e.index));timeline.mail=[...slots.values()].map(e=>({...e,at:0})).concat(freshSlots,timeline.mail.filter(e=>e.at>0));
  if(reviewRecord)timeline.toolRecords=[{...reviewRecord,at:0},...timeline.toolRecords.filter(e=>e.at>0)];
  if(chapter==='director'&&callerState)timeline.callerStatus=[{...callerState,at:0},...timeline.callerStatus];
  if(chapter==='learning'){
   if(instructionState)timeline.instructionRecords=[{...instructionState,at:0},...timeline.instructionRecords.filter(e=>e.at>0)];
   if(decisionState)timeline.decisions=[{...decisionState,at:0},...timeline.decisions.filter(e=>e.at>0)];
   timeline.reveal=[...availability.values()].map(e=>({...e,at:0})).concat(timeline.reveal.filter(e=>e.at>0));
  }
  if(chapter==='human')timeline.personRecords=[...personState.values()].map(e=>({...e,at:0})).concat(timeline.personRecords.filter(e=>e.at>0));
  finishTimeline();if(chapter==='director')callerState=latest(timeline.callerStatus,duration)||callerState;
  if(chapter==='learning'){instructionState=latest(timeline.instructionRecords,duration)||instructionState;decisionState=latest(timeline.decisions,duration)||decisionState;for(const e of timeline.reveal)availability.set(e.role,e);} 
  if(chapter==='human')for(const e of timeline.personRecords){const old=personState.get(e.role);if(!old||e.at>=old.at)personState.set(e.role,e);}
  carried=new Map();for(const e of timeline.records){const key=e.cell+':'+e.role,old=carried.get(key);if(!old||e.at>=old.at)carried.set(key,e)}
  if(i<target)for(const c of Object.values(camera)){c.from={...c.to};c.value={...c.to};c.at=lifeTime;}reviewRecord=latest(timeline.toolRecords,duration)||reviewRecord;slots=new Map();for(const e of timeline.mail){const old=slots.get(e.index);if(!old||e.at>=old.at)slots.set(e.index,e)}
 }
}
function show(){if(shortViewport())shortFocusKey='';const ch=chapters[chapter],step=ch.steps[index];elapsed=0;$('caller-update').hidden=chapter!=='director'||index===0;$('chapter-label').textContent=ch.label;if(refined()&&(index>0||['communication','human'].includes(chapter)))$('chapter-label').append(H('span',{id:'phase-position',class:'phase-position','aria-live':'polite'},''));const guided=refined()&&(index>0||['communication','human'].includes(chapter));document.body.dataset.refined=String(guided);$('title').innerHTML=(guided?step[0]:ch.title).replace('\n','<br>');$('description').textContent=guided?step[1]:ch.description;$('phase-action').textContent='';$('readiness').hidden=!guided||step[2].startsWith('network')||['learning','human'].includes(chapter);$('phase-cue').replaceChildren();if(guided){$('phase-cue').append(H('span',{class:'cue-title'},`${index+1} / ${ch.steps.length} · ${step[0].replace('\n',' ')}`),H('span',{id:'cue-state',class:'cue-state'},''),H('span',{class:'cue-summary'},ch.cueSummaries?.[index]||''),H('span',{id:'cue-checks',class:'cue-checks'},''));}else $('phase-cue').append(H('span',{id:'cue-checks',class:'cue-checks'},''));if(['communication','human'].includes(chapter))$('phase-cue').append(H('span',{class:'cue-scope'},'Proposed shared exchange'));if(chapter==='director'&&guided)$('phase-cue').append(H('span',{id:'cue-caller',class:'cue-caller'},''));$('scope').textContent=ch.scope;$('qualification').textContent=refined()&&index>0?'':ch.qualification||'';$('step-title').textContent=step[0];$('step-copy').textContent=step[1];$('step-title').hidden=refined()&&index>0;$('step-copy').hidden=refined()&&index>0;$('step-count').textContent=`${String(index+1).padStart(2,'0')} / ${String(ch.steps.length).padStart(2,'0')}`;$('diagram-desc').textContent=step[0]+'. '+step[1];$('chapter').value=chapter;$('stage').dataset.chapter=chapter;$('diagram-key').style.display=step[2].startsWith('network')||['communication','human'].includes(chapter)?'none':'flex';
 $('steps').replaceChildren(...ch.steps.map((s,i)=>{const b=H('button',{'aria-label':`Step ${i+1}: ${s[0]}`,'aria-current':String(i===index),title:s[0],class:i<index?'completed':''});b.onclick=()=>cue(i);return b}));
 configureWithContinuity(ch,index);prepareSceneViewport();$('previous').disabled=index===0;$('next').disabled=index===ch.steps.length-1;updatePlay();render();const hash=`#${chapter}${index?'~'+(index+1):''}`;if(location.hash!==hash)history.replaceState(null,'',hash);document.title=ch.label+' — Inside agentic systems';
}
function updatePlay(){const action=playing&&motionRunning&&playMode==='continuous'?'Pause':playing&&!motionRunning?'Continue':'Play all';$('play').innerHTML=(action==='Pause'?'Ⅱ':'▶')+' <span>'+action+'</span>';$('play').setAttribute('aria-label',action==='Pause'?'Pause all motion and story':action);$('motion').innerHTML=(motionRunning?'Ⅱ':'▷')+' <span>'+(motionRunning?'Pause motion':'Resume motion')+'</span>';$('motion').setAttribute('aria-label',motionRunning?'Pause all motion':'Resume motion');$('motion').title=motionRunning?'Pause the whole living system':'Resume the living system';$('motion').setAttribute('aria-pressed',String(!motionRunning));const cueState=$('cue-state');if(cueState)cueState.textContent=playing?(motionRunning?'Animating':'Paused'):elapsed>=duration?'Ready':'Cue';const phasePosition=$('phase-position');if(phasePosition)phasePosition.textContent=`${index+1} / ${chapters[chapter].steps.length} · `+(playing?(motionRunning?'Animating':'Paused'):elapsed>=duration?'Ready':'Cue');$('cue-status').textContent=playing?(motionRunning?'Animating':'Paused'):elapsed>=duration?'Ready':'Arrow keys present';}
function prepareShortView(){
 let button=$('short-scene');if(!shortViewport()){if(button)button.remove();shortFocusKey='';return;}
 if(!button){button=H('button',{id:'short-scene','aria-label':'View current scene',title:'View the living scene without advancing'},'View scene ↓');button.onclick=()=>{if(index===0){const r=$('diagram').getBoundingClientRect();window.scrollTo({top:window.scrollY+r.top-8,behavior:'auto'});}else followShortScene(reduced?duration:elapsed,true);};$('fullscreen').parentElement.prepend(button);}
}
function shortSceneTarget(t){
 let target={at:-1,type:'cell',cell:cellNodes.main?'main':'left',role:'director'};const add=v=>{if(v.at<=t&&v.at>=target.at)target=v;};
 for(const w of timeline.work)if(w.start<=t&&t<=w.end)add({at:w.start,type:'cell',cell:w.cell,role:w.role});
 for(const e of timeline.records)if(e.at>0)add({at:e.at,type:'cell',cell:e.cell,role:e.role});
 for(const e of timeline.instructionRecords||[])if(e.at>0)add({at:e.at,type:'instructions',cell:'main',role:'director'});
 for(const e of timeline.personRecords||[])if(e.at>0)add({at:e.at,type:'person',role:e.role});
 for(const a of timeline.arrivals)if(t<a.at+300)add({at:a.at-500,type:'cell',cell:a.cell,role:a.role,approaching:t<a.at});
 for(const a of timeline.toolArrivals)if(t<a.at+300){if(a.tool.startsWith('mail-'))add({at:a.at-500,type:'mail',id:a.tool});else if(a.tool==='person'){const e=(timeline.personRecords||[]).find(e=>e.at===a.at+300);add({at:a.at-500,type:'person',role:e?.role||'decision',approaching:t<a.at});}}
 const writing=[...timeline.records.map(e=>({...e,type:'cell'})),...(timeline.instructionRecords||[]).map(e=>({...e,type:'instructions',cell:'main',role:'director'})),...(timeline.personRecords||[]).map(e=>({...e,type:'person'}))].filter(e=>e.at>0&&e.at<=t&&t<e.at+620);const write=latest(writing,t);return write||target;
}
function followShortScene(t,force=false){
 if(!shortViewport()||!force&&(!storyStarted||index===0))return;const svg=$('diagram'),matrix=svg.getScreenCTM?.();if(!matrix||typeof DOMPoint==='undefined')return;
 const target=shortSceneTarget(t);let paper=null,owner=null,label=null,visible=false;
 if(target.type==='mail')paper=$(target.id);
 else if(target.type==='person'){owner=personPoint();paper=$('person-record-'+target.role);visible=Boolean(latest((timeline.personRecords||[]).filter(e=>e.role===target.role),t));}
 else{const c=cellNodes[target.cell];if(!c)return;owner=globalPoint(target.cell,target.role);label=target.role==='director'?null:c.rs[target.role]?.label;paper=target.type==='instructions'?$('instruction-record'):c.records[target.role];visible=Boolean(latest(target.type==='instructions'?timeline.instructionRecords:timeline.records.filter(e=>e.cell===target.cell&&e.role===target.role),t));}
 const key=chapter+':'+index+':'+target.type+':'+(target.cell||target.id||'')+':'+(target.role||'')+':'+Boolean(target.approaching)+':'+visible;if(!force&&key===shortFocusKey)return;
 const bounds=[];if(owner){const p=new DOMPoint(owner[0],owner[1]).matrixTransform(matrix);bounds.push({top:p.y-20,bottom:p.y+20});}if(label&&label.style.opacity!=='0')bounds.push(label.getBoundingClientRect());if(paper&&(target.type==='mail'||visible&&!target.approaching))bounds.push(paper.getBoundingClientRect());if(!bounds.length)return;
 const cue=$('phase-cue'),cueHeight=document.body.dataset.refined==='true'?cue.getBoundingClientRect().height:0,footer=document.querySelector('footer').getBoundingClientRect(),top=cueHeight+12,bottom=footer.top-12;if(bottom<=top)return;
 const min=Math.min(...bounds.map(b=>b.top)),max=Math.max(...bounds.map(b=>b.bottom)),center=(min+max)/2;shortFocusKey=key;window.scrollTo({top:Math.max(0,window.scrollY+center-(top+bottom)/2),behavior:'auto'});
}
function focusCue(){
 if(!refined()||layoutMode()!=='phone'&&!shortViewport())return;
 if(index===0){window.scrollTo({top:0,behavior:'auto'});return}
 if(shortViewport()){followShortScene(reduced?duration:elapsed,true);return;}
 const rect=$('diagram').getBoundingClientRect(),code=chapters[chapter].steps[index][2],cueHeight=$('phase-cue').getBoundingClientRect().height;
 // The world view may crop quiet upper membrane, while its active central hub
 // and lower exchange destinations remain below the persistent phase cue.
 const offset=code.startsWith('network')?mainView(code).y*rect.width/600-cueHeight-16:-cueHeight;
 window.scrollTo({top:window.scrollY+rect.top+offset,behavior:'auto'});
}
function cue(i){index=Math.max(0,Math.min(chapters[chapter].steps.length-1,i));playing=!reduced;playMode='cue';storyStarted=true;motionRunning=!reduced;show();if(reduced){elapsed=duration;render();updatePlay()}requestAnimationFrame(focusCue)}
function move(n){cue(index+n)}
function selectChapter(k){chapter=chapters[k]?k:'systems';index=0;scene='';playing=false;storyStarted=false;show();if(shortViewport())window.scrollTo({top:0,behavior:'auto'})}
function parseHash(){playing=false;storyStarted=false;playMode='cue';const[k,s]=location.hash.slice(1).split('~');if(chapters[k]){chapter=k;index=Math.max(0,Math.min(chapters[k].steps.length-1,(parseInt(s)||1)-1))}else{chapter='systems';index=0}scene='';show()}
$('previous').onclick=()=>move(-1);$('next').onclick=()=>move(1);$('play').onclick=()=>{if(playing&&motionRunning&&playMode==='continuous'){motionRunning=false}else{if(elapsed>=duration)elapsed=0;playMode='continuous';playing=true;storyStarted=true;motionRunning=true}last=performance.now();updatePlay()};$('motion').onclick=()=>{motionRunning=!motionRunning;last=performance.now();updatePlay()};$('replay').onclick=()=>cue(index);$('chapter').onchange=e=>selectChapter(e.target.value);
$('fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen()}catch{}};
document.addEventListener('keydown',e=>{if(['SELECT','INPUT','TEXTAREA','BUTTON'].includes(e.target.tagName)&&e.key===' ')return;if(['SELECT','INPUT','TEXTAREA'].includes(e.target.tagName))return;if(e.key==='ArrowRight'){e.preventDefault();move(1)}else if(e.key==='ArrowLeft'){e.preventDefault();move(-1)}else if(e.code==='Space'){e.preventDefault();$('play').click()}else if(e.key.toLowerCase()==='r')$('replay').click();else if(e.key==='Home'){e.preventDefault();cue(0)}});window.addEventListener('hashchange',parseHash);window.addEventListener('resize',()=>{if(!timeline)return;prepareSceneViewport();if(scene==='cell'&&cellNodes.main){applyMainView(chapters[chapter].steps[index][2]);for(const[id,x,y,s]of neighborViews())setCamera(id,x,y,s,camera[id]?.to.opacity??0);}for(const c of Object.values(camera)){c.from={...c.to};c.value={...c.to};c.at=lifeTime;}render()});
function animate(now){const dt=Math.min(100,now-last);last=now;if(motionRunning){lifeTime+=dt;if(playing){elapsed+=dt;if(elapsed>=duration){if(playMode==='continuous'&&index<chapters[chapter].steps.length-1){index++;show()}else{elapsed=duration;playing=false;updatePlay()}}}render()}requestAnimationFrame(animate)}
buildDust();parseHash();requestAnimationFrame(animate);
window.presentation={get state(){return{chapter,index,playing:playing&&motionRunning,motionRunning,storyStarted,playMode,elapsed,lifeTime,duration,scene,steps:chapters[chapter].steps.length}},go:(k,i=0)=>{selectChapter(k);index=Math.max(0,Math.min(chapters[k].steps.length-1,i));show()},chapters,diagnostics:()=>({timeline,duration,records:[...document.querySelectorAll('.record.visible')].map(g=>({label:g.querySelector('text')?.textContent,opacity:g.style.opacity})),wires:signals.map(s=>({at:s.at,arrival:s.at+s.travel,visiblePath:s.pathProvider()?.id||s.pathProvider()?.tagName}))})};
