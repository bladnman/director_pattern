'use strict';
const NS='http://www.w3.org/2000/svg';
const $=id=>document.getElementById(id);
const el=(tag,attrs={},text='')=>{const n=document.createElementNS(NS,tag);for(const[k,v]of Object.entries(attrs))n.setAttribute(k,v);if(text)n.textContent=text;return n};
const H=(tag,attrs={},text='')=>{const n=document.createElement(tag);for(const[k,v]of Object.entries(attrs))n.setAttribute(k,v);n.textContent=text;return n};
const roles=[{id:'design',name:'Design',x:-105,y:-108},{id:'engineering',name:'Engineering',x:112,y:-109},{id:'quality',name:'Quality',x:161,y:72},{id:'operations',name:'Operations',x:-23,y:169},{id:'research',name:'Research',x:-168,y:61}];
const chapters={
systems:{label:'Agentic systems',title:'An area of work.\nA system of its own.',description:'One cell holds the people, responsibilities and memory that support an ongoing area of work.',scope:'A general model',steps:[
 ['A domain, held together','A cell can include several teams and many outputs. Its branches represent responsibilities, not a fixed organization.','overview'],
 ['A request enters','The Director is the point of contact. The request comes in, and its intent is recorded.','intake'],
 ['Work goes to a responsibility','Design records its assignment. Its branch comes alive as work moves through the local graph.','design'],
 ['A return changes the next move','Design updates its work record and returns an outcome. The Director updates the request before routing again.','design-return'],
 ['One request can become several','Engineering and Quality receive different, bounded assignments. The flow can branch and run in parallel.','parallel'],
 ['Returns are brought together','Each responsibility updates its own record. The Director evaluates the combined result and asks Quality for a final check.','verify'],
 ['The final check returns','Quality updates its record and sends the checked result back. The Director records that final return before closing the request.','final-return'],
 ['The request is concluded','The Director reconciles the result with the request and returns an outcome to the caller.','conclude'],
 ['A cell is one part of a wider world','Other areas of work have systems of their own. Requests cross a boundary; results come back.','network'],
 ['Cooperation becomes a network','More systems exchange work. Each keeps its own responsibilities while contributing to shared outcomes.','network-many']
]},
director:{label:'The Director Pattern',title:'One conversation.\nWork in many places.',description:'The Director keeps the whole outcome in view while bounded work moves through the system.',scope:'Current method · illustrated',steps:[
 ['Start with the whole request','The cell holds capabilities and durable memory. The Director remains accountable for the usable outcome.','overview'],
 ['Understand and record','A request arrives. The Director preserves intent, identifies the obligations and records what success means.','intake'],
 ['Delegate bounded work','Design gets a clear assignment and records it locally. A message carries the work; a durable record preserves continuity.','design'],
 ['Evaluate, then branch','The first result returns. The Director updates the request and dispatches distinct work to Engineering and Quality.','parallel-status'],
 ['Keep the caller informed','Engineering returns first. The Director records the result and gives the caller a progress update while Quality continues.','partial-return'],
 ['Review the whole result','Quality returns its findings. The Director evaluates the evidence and routes a focused follow-up when needed.','verify-status'],
 ['The follow-up returns','Quality updates its record and returns the focused check. The Director evaluates that return and updates the request.','final-return'],
 ['Conclude against the request','The records reflect the final result. The caller receives the outcome after the work has been evaluated.','conclude']
]},
learning:{label:'Learning and growth',title:'Experience becomes\nbetter instructions.',description:'Work leaves evidence. A deliberate review turns selected lessons into guidance the system can use again.',scope:'Current learning loop · optional growth',qualification:'Role growth is a proposed illustration.',steps:[
 ['Work leaves a trace','Completed work, corrections and exceptions provide evidence. Recording an observation does not yet change the system.','learn-observe'],
 ['The owner initiates a review','At an appropriate checkpoint, the Director assigns a bounded learning review. The review examines selected evidence.','learn-review'],
 ['Propose a better way','The reviewer proposes a scoped improvement. Better instructions, changed routing or a new specialty are different kinds of proposal.','learn-propose'],
 ['An owner decides','The owner evaluates the proposal. Accepted guidance is maintained in the instructions that future work will actually load.','learn-decide'],
 ['A recurring need can justify growth','A new specialty is proposed and reviewed. It becomes available only after its responsibility and routing have been implemented.','learn-grow'],
 ['A later request uses the change','A new request reaches the Director and is routed to the maintained specialty. Actual use tests whether the change helps.','learn-use']
]},
communication:{label:'Across systems',title:'Independent systems.\nA common exchange.',description:'An addressed message can cross a domain boundary without moving ownership of either system.',scope:'Proposed transport',qualification:'A shared exchange is a proposed mechanism.',steps:[
 ['A place to leave work','Systems keep their own internal graphs. A shared exchange carries addressed requests, acknowledgments and returns.','exchange-overview'],
 ['Write to the destination','Fieldwork places a request addressed to Infrastructure in the exchange, with context and a return route.','exchange-send'],
 ['Pick up the work addressed to you','Infrastructure selects its message. Other messages remain for their intended recipients.','exchange-pickup'],
 ['Acknowledge, then work locally','Infrastructure accepts the bounded work and activates its own graph. Fieldwork keeps its commitment to the caller.','exchange-work'],
 ['Return through the same exchange','Infrastructure updates its record and writes a result addressed back to Fieldwork.','exchange-return'],
 ['Evaluate the returned outcome','Fieldwork picks up the result, updates its own record and evaluates whether the commitment is met.','exchange-evaluate']
]},
human:{label:'People in the loop',title:'A person is part\nof the conversation.',description:'The same exchange can carry a decision to a person and bring their answer back to the system.',scope:'Proposed exchange · human authority',qualification:'The exchange illustrates a proposed transport.',steps:[
 ['Work reaches a human boundary','The system can prepare a concrete decision for a person. Human judgment remains part of the workflow.','human-overview'],
 ['Put a reviewable question in the exchange','The Director sends the context, proposed action and decision needed. The message is addressed to the person.','human-send'],
 ['Waiting is visible','The dependent action waits. Other authorized work may continue while the decision remains unanswered.','human-wait'],
 ['The person reviews and decides','The person picks up the request and returns an explicit choice: approve, revise or decline.','human-decide'],
 ['Bring the decision back','The system receives and records the answer, then resumes only the work that answer authorizes.','human-return'],
 ['Close the loop','The Director reports what happened. A recorded human decision is a return in the conversation, not a transfer of all authority.','human-conclude']
]}
};
let chapter='systems',index=0,playing=false,elapsed=0,last=performance.now(),scene='',cellNodes={},signals=[],tick=0,frame=0;
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
const duration=6200;
const membrane='M0,-267 C91,-266 235,-170 264,-48 C296,75 232,230 111,257 C-20,286 -185,260 -242,151 C-290,59 -272,-75 -223,-148 C-153,-231 -72,-269 0,-267 Z';
function seed(n){let x=Math.sin(n*127.1+311.7)*43758.5453123;return x-Math.floor(x)}
function buildDust(){for(let i=0;i<130;i++){const x=seed(i+1)*1600,y=seed(i+180)*900,r=seed(i+350)*2.5+.3;const c=el('circle',{cx:x,cy:y,r,fill:i%6?'#276780':'#91c8db',opacity:seed(i+600)*.17+.025});$('dust').append(c)}for(let i=0;i<8;i++)$('dust').append(el('circle',{cx:seed(i+520)*1600,cy:seed(i+830)*900,r:seed(i+300)*12+5,fill:'#135779',opacity:'.06',filter:'url(#soft)'}));}
function createCell(name,id,{labels=true,simple=false,color='#27ddc8'}={}){
 const g=el('g',{id,class:'cell'}),mem=el('path',{d:membrane,class:'membrane',style:`stroke:${color}`});g.append(mem,el('path',{d:membrane,transform:'scale(.966)',class:'inner-membrane',style:`stroke:${color}`}));
 if(labels)g.append(el('text',{x:0,y:-300,'text-anchor':'middle',class:'domain-label',style:`fill:${color}`},name));
 const rs={};
 for(let ri=0;ri<roles.length;ri++){
  const r=roles[ri],rg=el('g',{'data-role':r.id,class:'role'}),path=el('path',{d:`M0,0 Q${r.x*.7},${r.y*.25} ${r.x},${r.y}`,class:'trunk'});rg.append(path);
  for(let j=0;j<(simple?3:6);j++){
   const a=Math.atan2(r.y,r.x)+(j-2.5)*.235,len=54+seed(ri*20+j+20)*50;
   let x=r.x+Math.cos(a)*len,y=r.y+Math.sin(a)*len;const radius=Math.hypot(x,y);if(radius>241){x*=241/radius;y*=241/radius;}
   rg.append(el('path',{d:`M${r.x},${r.y} Q${r.x+Math.cos(a+.4)*len*.5},${r.y+Math.sin(a+.4)*len*.5} ${x},${y}`,class:'twig'}));
   rg.append(el('circle',{cx:x,cy:y,r:simple?2:2.7,fill:'#c7e4f1',opacity:'.72'}));
   if(!simple&&j%2===0){let tx=x+Math.cos(a+.7)*18,ty=y+Math.sin(a+.7)*18;const radius2=Math.hypot(tx,ty);if(radius2>248){tx*=248/radius2;ty*=248/radius2;}rg.append(el('path',{d:`M${x},${y} L${tx},${ty}`,class:'twig'}),el('circle',{cx:tx,cy:ty,r:1.5,fill:'#bfdee8',opacity:'.65'}));}
  }
  rg.append(el('circle',{cx:r.x,cy:r.y,r:17,fill:'url(#star)',opacity:'.3',class:'halo'}),el('circle',{cx:r.x,cy:r.y,r:6,class:'core'}));
  if(labels)rg.append(el('text',{x:r.x+(r.x<-50?-12:r.x>50?12:0),y:r.y+(r.id==='operations'?23:-14),'text-anchor':r.x<-50?'end':r.x>50?'start':'middle',class:'node-label'},r.name));
  const rec=record(r.x+12,r.y+17,r.id==='research'?'Guidance':'Work record');rg.append(rec);rs[r.id]={group:rg,record:rec};g.append(rg);
 }
 g.append(el('circle',{r:28,fill:'url(#star)',opacity:'.9'}),el('circle',{r:10,fill:'#f0f7fb',opacity:'.95'}));if(labels)g.append(el('text',{x:0,y:31,'text-anchor':'middle',class:'director-label'},'Director'));
 const rec=record(15,45,'Request');g.append(rec);cellNodes[id]={g,rs,record:rec,mem};return g;
}
function record(x,y,label){const g=el('g',{transform:`translate(${x} ${y})`,class:'record'});g.append(el('rect',{x:0,y:0,width:35,height:27,rx:3}),el('path',{d:'M8 7 H26 M8 12 H26 M8 17 H20',fill:'none'}),el('text',{x:42,y:15},label));return g}
function line(id,from,to,color='#315363',curve=0){const p=el('path',{id,d:`M${from[0]},${from[1]} Q${(from[0]+to[0])/2},${(from[1]+to[1])/2+curve} ${to[0]},${to[1]}`,fill:'none',stroke:color,'stroke-width':1,opacity:.45});$('world').append(p);return p}
function makeScene(kind){if(scene===kind)return;scene=kind;cellNodes={};$('world').replaceChildren();$('signals').replaceChildren();
 if(kind==='cell'){
  $('world').append(createCell('Fieldwork','main'));
  const caller=el('g',{id:'caller',class:'caller'});caller.append(el('circle',{cx:573,cy:450,r:5,fill:'#9cb8c7'}),el('text',{x:573,y:477,'text-anchor':'middle',class:'tiny-label'},'Caller'));$('world').append(caller);
  line('caller-line',[585,450],[1000,450]);
  for(const[n,x,y,s,c]of [['Infrastructure',1300,235,.32,'#7d9fe2'],['Publishing',1330,670,.28,'#f58eab'],['Research',750,735,.25,'#e9bd79'],['Customer care',665,185,.22,'#68b6b8']]){const id='other-'+n.replace(' ','-');const g=createCell(n,id,{labels:false,simple:true,color:c});g.setAttribute('transform',`translate(${x} ${y}) scale(${s})`);g.setAttribute('class','other-cell');g.setAttribute('opacity','0');g.append(el('text',{y:330,'text-anchor':'middle',class:'domain-label',style:`fill:${c};font-size:30px`},n));$('world').append(g);}
  const learn=el('g',{id:'learning-tools',opacity:0});learn.append(el('path',{d:'M800 270 Q700 370 790 520',class:'learning-arc'}),el('text',{x:710,y:378,class:'state-label'},'Evidence'),el('text',{x:710,y:399,class:'state-label'},'Review'),el('text',{x:710,y:420,class:'state-label'},'Instructions'));$('world').append(learn);
  const panel=el('g',{id:'learning-decision',opacity:0,transform:'translate(1030 690)'});panel.append(el('rect',{x:0,y:0,width:190,height:49,rx:6,class:'decision-panel'}),el('text',{x:15,y:20,class:'decision-title'},'Owner decision'),el('text',{x:15,y:37,class:'tiny-label',id:'decision-label'},'Proposal under review'));$('world').append(panel);
 }else{
  $('world').append(createCell('Fieldwork','left',{labels:false,simple:true}));cellNodes.left.g.setAttribute('transform','translate(650 445) scale(.43)');
  if(kind==='exchange'){$('world').append(createCell('Infrastructure','right',{labels:false,simple:true,color:'#f58eab'}));cellNodes.right.g.setAttribute('transform','translate(1360 445) scale(.43)');}
  else{const p=el('g',{id:'person',transform:'translate(1360 425)'});p.append(el('circle',{cx:0,cy:-34,r:21,fill:'none',stroke:'#e9bd79','stroke-width':1.5}),el('path',{d:'M-43 50 C-43 -5 43 -5 43 50 M-60 69 H60',fill:'none',stroke:'#e9bd79','stroke-width':1.5}));$('world').append(p);}
  $('world').append(el('text',{x:650,y:615,'text-anchor':'middle',class:'domain-label'},'Fieldwork'),el('text',{x:1360,y:615,'text-anchor':'middle',class:'domain-label',style:`fill:${kind==='exchange'?'#f58eab':'#e9bd79'}`},kind==='exchange'?'Infrastructure':'Person'));
  line('to-exchange',[770,445],[935,445]);line('from-exchange',[1080,445],[1240,445]);
  const ex=el('g',{id:'exchange',transform:'translate(920 328)'});ex.append(el('rect',{width:172,height:238,rx:12,fill:'#07131c',stroke:'#294651','stroke-width':1}),el('text',{x:86,y:-20,'text-anchor':'middle',class:'exchange-label'},'Shared exchange'),el('text',{x:86,y:263,'text-anchor':'middle',class:'scene-tag'},'Proposed transport'));
  for(let i=0;i<4;i++){const row=el('g',{id:'mail-'+i,transform:`translate(17 ${23+i*51})`});row.append(el('rect',{width:138,height:38,rx:5,class:'exchange-card'}),el('circle',{cx:15,cy:19,r:3,fill:['#7d9fe2','#f58eab','#e9bd79','#27ddc8'][i]}),el('text',{x:28,y:23,class:'exchange-text'},['Research','Infrastructure','Person','Fieldwork'][i]));ex.append(row)}$('world').append(ex);
  const state=el('text',{id:'exchange-state',x:1008,y:667,'text-anchor':'middle',class:'state-label'},'Addressed work. An explicit return.');$('world').append(state);
 }
}
function coords(role,cx=1000,cy=450,s=1){if(role==='director')return[cx,cy];const r=roles.find(x=>x.id===role);return[cx+r.x*s,cy+r.y*s]}
let target={x:1000,y:450,s:1};
function route(from,to,color='#27ddc8',delay=0,curve=0){const path=el('path',{d:`M${from[0]},${from[1]} Q${(from[0]+to[0])/2},${(from[1]+to[1])/2+curve} ${to[0]},${to[1]}`,fill:'none',stroke:color,'stroke-width':1,opacity:'.18'});$('signals').append(path);const halo=el('circle',{r:10,fill:color,opacity:'.25',filter:'url(#glow)'}),dot=el('circle',{r:3.2,fill:color});$('signals').append(halo,dot);signals.push({path,halo,dot,delay,len:path.getTotalLength()});}
function active(id,role,on=true){const n=cellNodes[id]?.rs[role];if(n)n.group.classList.toggle('active',on)}
function rec(id,role,update=false){const n=role?cellNodes[id]?.rs[role]?.record:cellNodes[id]?.record;if(n)n.setAttribute('class','record visible'+(update?' updated':''));}
function cellState(code){makeScene('cell');const network=code.startsWith('network'),learning=code.startsWith('learn-'),zoom=!['overview','network','network-many','learn-observe'].includes(code);target=network?{x:950,y:450,s:.6}:zoom?{x:1030,y:435,s:1.23}:{x:1030,y:450,s:1.08};
 const c=cellNodes.main;c.g.setAttribute('transform',`translate(${target.x} ${target.y}) scale(${target.s})`);$('caller').setAttribute('opacity',network||learning?0:1);$('caller-line').setAttribute('opacity',network||learning?0:.5);$('learning-tools').setAttribute('opacity',learning?1:0);$('learning-decision').setAttribute('opacity',['learn-propose','learn-decide','learn-grow','learn-use'].includes(code)?1:0);
 for(const[id,n]of Object.entries(cellNodes)){for(const r of Object.values(n.rs)){r.group.classList.remove('active');r.record.setAttribute('class','record')}n.record.setAttribute('class','record');if(id!=='main')n.g.setAttribute('opacity',network?1:0)}
 const r=role=>coords(role,target.x,target.y,target.s),d=r('director'),caller=[573,450];
 for(const role of roles){c.rs[role.id].group.setAttribute('opacity',learning&&['research','operations'].includes(role.id)?0:1);const txt=c.rs[role.id].group.querySelector('.node-label');if(txt)txt.textContent=role.name}
 c.mem.setAttribute('transform',['learn-grow','learn-use'].includes(code)?'scale(1.08)':'scale(1)');
 if(code==='overview')return;
 if(network){for(const[id,n]of Object.entries(cellNodes))if(id!=='main')for(const role of ['engineering','design'])active(id,role);active('main','quality');route([950,450],[1300,235],'#7d9fe2',0,-50);route([1300,235],[950,450],'#27ddc8',.45,30);if(code==='network-many'){route([1330,670],[950,450],'#f58eab',.2,70);route([950,450],[750,735],'#e9bd79',.6,20);route([665,185],[1300,235],'#7d9fe2',.8,-40);route([750,735],[1330,670],'#f58eab',1,-20);route([950,450],[665,185],'#27ddc8',1.3,-70)}return}
 rec('main',null,['design-return','verify','verify-status','partial-return','conclude','learn-decide','learn-grow','learn-use'].includes(code));
 if(code==='intake'){route(caller,d);return}
 if(code==='design'){active('main','design');rec('main','design');route(d,r('design'));return}
 if(code==='design-return'){active('main','design');rec('main','design',true);route(r('design'),d,'#dbeaf7');return}
 if(['parallel','parallel-status','partial-return','verify','verify-status'].includes(code)){
  rec('main','design',true);for(const role of ['engineering','quality']){active('main',role);rec('main',role,['partial-return','verify','verify-status'].includes(code));}
  if(code==='partial-return'){route(r('engineering'),d,'#dbeaf7');route(d,caller,'#e9bd79',.45,-80);route(d,r('quality'),'#27ddc8',.6)}
  else if(code.startsWith('verify')){route(r('engineering'),d,'#dbeaf7',0);route(r('quality'),d,'#dbeaf7',.25);route(d,r('quality'),'#27ddc8',2.1,35);if(code==='verify-status')route(d,caller,'#e9bd79',.65,-80)}
  else{route(r('design'),d,'#dbeaf7',0);route(d,r('engineering'),'#27ddc8',1.9);route(d,r('quality'),'#27ddc8',1.9);if(code==='parallel-status')route(d,caller,'#e9bd79',2.5,-80)}return;
 }
 if(code==='final-return'){rec('main','engineering',true);rec('main','quality',true);rec('main',null,true);active('main','quality');route(r('quality'),d,'#dbeaf7',0,-22);return}
 if(code==='conclude'){for(const role of ['design','engineering','quality'])rec('main',role,true);route(d,caller,'#27ddc8',0,-70);$('caller').querySelector('circle').setAttribute('fill','#27ddc8');return}
 if(learning){
  const review=[795,435],instructions=[795,520];$('caller').setAttribute('opacity',0);
  const lr=cellNodes.main.rs.research,txt=lr.group.querySelector('.node-label');
  if(code==='learn-observe'){for(const role of ['design','engineering','quality']){rec('main',role,true);route(r(role),d,'#dbeaf7',roles.findIndex(x=>x.id===role)*.15)}rec('main',null,true)}
  if(code==='learn-review'){route(d,review,'#e9bd79');route(r('engineering'),review,'#dbeaf7',.4);active('main','engineering');rec('main','engineering',true)}
  if(code==='learn-propose'){route(review,instructions,'#e9bd79');$('decision-label').textContent='Proposal under review'}
  if(code==='learn-decide'){route(instructions,d,'#e9bd79');rec('main',null,true);$('decision-label').textContent='Guidance accepted + maintained'}
  if(['learn-grow','learn-use'].includes(code)){lr.group.setAttribute('opacity',1);txt.textContent='Synthesis';active('main','research');rec('main','research',code==='learn-use');$('decision-label').textContent=code==='learn-grow'?'New role implemented':'Maintained role used';route(code==='learn-grow'?instructions:d,r('research'),'#e9bd79');if(code==='learn-use'){route(caller,d,'#27ddc8');route(r('research'),d,'#dbeaf7',.65);$('caller').setAttribute('opacity',1)}}
 }
}
function exchangeState(code,human){makeScene(human?'human':'exchange');const left=[650,445],right=human?[1360,425]:[1360,445],ex=[1008,445];for(const c of Object.values(cellNodes)){for(const r of Object.values(c.rs)){r.group.classList.remove('active');r.record.setAttribute('class','record')}c.record.setAttribute('class','record')}
 for(let i=0;i<4;i++)$('mail-'+i).querySelector('rect').setAttribute('class','exchange-card');const select=(i,ret=false)=>$('mail-'+i).querySelector('rect').setAttribute('class','exchange-card '+(ret?'return':'selected'));
 $('exchange-state').textContent='Addressed work. An explicit return.';
 if(human){
  if(code==='human-overview')return;
  rec('left');
  if(code==='human-send'){select(2);route(left,ex,'#e9bd79');$('exchange-state').textContent='Decision requested · Person'}
  if(code==='human-wait'){select(2);active('left','engineering');$('exchange-state').textContent='Decision pending · dependent action waits';route(coords('engineering',650,445,.43),left,'#27ddc8',.5);}
  if(code==='human-decide'){select(2);route(ex,right,'#e9bd79');$('exchange-state').textContent='Approve, revise or decline'}
  if(code==='human-return'){select(3,true);route(right,ex,'#e9bd79');route(ex,left,'#27ddc8',.65);rec('left',null,true);$('exchange-state').textContent='Explicit decision received · record updated'}
  if(code==='human-conclude'){rec('left',null,true);active('left','quality');route(left,ex,'#27ddc8');route(ex,right,'#27ddc8',.6);$('exchange-state').textContent='Authorized work resumed · outcome reported'}
 }else{
  if(code==='exchange-overview')return;
  rec('left');
  if(code==='exchange-send'){select(1);route(left,ex);$('exchange-state').textContent='To Infrastructure · request + return route'}
  if(code==='exchange-pickup'){select(1);route(ex,right,'#f58eab');$('exchange-state').textContent='Infrastructure selects its addressed request'}
  if(code==='exchange-work'){rec('right');active('right','engineering');active('right','quality');route(right,ex,'#f58eab');route(ex,left,'#e9bd79',.6,-35);$('exchange-state').textContent='Acknowledged · work stays with Infrastructure'}
  if(code==='exchange-return'){rec('right',null,true);select(3,true);route(right,ex,'#f58eab');$('exchange-state').textContent='To Fieldwork · result + evidence'}
  if(code==='exchange-evaluate'){rec('right',null,true);rec('left',null,true);select(3,true);route(ex,left);active('left','quality');$('exchange-state').textContent='Return evaluated · source commitment retained'}
 }
}
function show({reset=true}={}){const ch=chapters[chapter],step=ch.steps[index];if(reset)elapsed=0;$('chapter-label').textContent=ch.label;$('title').innerHTML=ch.title.replace('\n','<br>');$('description').textContent=ch.description;$('scope').textContent=ch.scope;$('qualification').textContent=ch.qualification||'';$('step-title').textContent=step[0];$('step-copy').textContent=step[1];$('step-count').textContent=`${String(index+1).padStart(2,'0')} / ${String(ch.steps.length).padStart(2,'0')}`;$('diagram-desc').textContent=step[0]+'. '+step[1];$('chapter').value=chapter;
 $('steps').replaceChildren(...ch.steps.map((s,i)=>{const b=H('button',{'aria-label':`Step ${i+1}: ${s[0]}`,'aria-current':String(i===index),title:s[0],class:i<index?'completed':''});b.onclick=()=>{playing=false;index=i;show()};return b}));
 signals=[];$('signals').replaceChildren();if(chapter==='communication'||chapter==='human')exchangeState(step[2],chapter==='human');else cellState(step[2]);
 $('previous').disabled=index===0;$('next').disabled=index===ch.steps.length-1;updatePlay();drawSignals();
 const hash=`#${chapter}${index?'~'+(index+1):''}`;if(location.hash!==hash)history.replaceState(null,'',hash);document.title=ch.label+' — Inside agentic systems';
}
function updatePlay(){$('play').innerHTML=playing?'Ⅱ <span>Pause</span>':'▶ <span>Play</span>';$('play').setAttribute('aria-label',playing?'Pause animation':'Play animation');}
function drawSignals(){for(const s of signals){let t=elapsed/1000-s.delay;const visible=t>=0&&t<1.6;const f=Math.max(0,Math.min(1,t/1.6));const p=s.path.getPointAtLength(s.len*(f*f*(3-2*f)));for(const n of[s.halo,s.dot]){n.setAttribute('cx',p.x);n.setAttribute('cy',p.y);n.setAttribute('opacity',visible?(n===s.halo?.3:1):0)}if(reduced){s.dot.setAttribute('cx',s.path.getPointAtLength(s.len*.56).x);s.dot.setAttribute('cy',s.path.getPointAtLength(s.len*.56).y);s.dot.setAttribute('opacity',1);s.halo.setAttribute('opacity',0)}}}
function move(n){playing=false;index=Math.max(0,Math.min(chapters[chapter].steps.length-1,index+n));show()}
function selectChapter(k){if(!chapters[k])k='systems';chapter=k;index=0;scene='';playing=false;show()}
function parseHash(){const[k,s]=location.hash.slice(1).split('~');if(chapters[k]){chapter=k;index=Math.max(0,Math.min(chapters[k].steps.length-1,(parseInt(s)||1)-1))}else{chapter='systems';index=0}scene='';show()}
$('previous').onclick=()=>move(-1);$('next').onclick=()=>move(1);$('play').onclick=()=>{if(index===chapters[chapter].steps.length-1&&!playing){index=0;show()}playing=!playing;last=performance.now();updatePlay()};$('replay').onclick=()=>{index=0;playing=!reduced;show()};$('chapter').onchange=e=>selectChapter(e.target.value);
$('fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen()}catch{}};
document.addEventListener('keydown',e=>{if(['SELECT','INPUT','TEXTAREA','BUTTON'].includes(e.target.tagName)&&e.key===' ')return;if(['SELECT','INPUT','TEXTAREA'].includes(e.target.tagName))return;if(e.key==='ArrowRight'){e.preventDefault();move(1)}else if(e.key==='ArrowLeft'){e.preventDefault();move(-1)}else if(e.code==='Space'){e.preventDefault();$('play').click()}else if(e.key.toLowerCase()==='r')$('replay').click();else if(e.key==='Home'){e.preventDefault();index=0;playing=false;show()}});
window.addEventListener('hashchange',parseHash);
function animate(now){const dt=Math.min(100,now-last);last=now;if(playing){elapsed+=dt;if(elapsed>=duration){if(index<chapters[chapter].steps.length-1){index++;show()}else{playing=false;updatePlay()}}drawSignals()}frame=requestAnimationFrame(animate)}
buildDust();parseHash();requestAnimationFrame(animate);
window.presentation={get state(){return{chapter,index,playing,elapsed,scene,steps:chapters[chapter].steps.length}},go:(k,i=0)=>{selectChapter(k);index=Math.max(0,Math.min(chapters[k].steps.length-1,i));show()},chapters};
