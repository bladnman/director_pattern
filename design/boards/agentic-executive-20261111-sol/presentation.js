(() => {
  'use strict';
  const C={teal:'#54dfc2',rose:'#f2a5c5',amber:'#ebbd77',violet:'#b9a5ed',blue:'#86bce4',ink:'#d8eaf5',dim:'#365064'};
  const chapters=[
    {id:'systems',name:'Agentic systems',cues:[
      ['A system around a domain.','Agents work together around a problem, with shared context that lasts beyond one conversation.','Organise around the work the domain needs.','A connected organic boundary contains several branches around a coordinating agent. Shared context stays inside the domain.'],
      ['A request enters one place.','The system takes responsibility for the request and coordinates the work inside.','','A request travels from outside the domain to a single central agent.'],
      ['Many parts. One outcome.','Different agents work in parallel. Their results return when each part is ready.','','Two branches receive work together and return results at different times.'],
      ['The result comes back.','The requester gets one coherent response. The domain keeps its context for the next request.','The value accumulates in the system.','A response leaves the coordinating agent. The system and its retained context remain ready for more work.']
    ]},
    {id:'director',name:'The Director Pattern',cues:[
      ['One accountable coordinator.','The Director owns the conversation, delegates bounded work, and judges the whole result.','','The central agent is identified as the Director. All external request and response traffic reaches this agent.'],
      ['Work stays traceable.','The request, its conditions, and the work in progress are retained as the team acts.','','A small local record is written by the Director, then bounded work travels into two internal branches.'],
      ['The domain shares its context.','History, guidance, guardrails and tools inform the work across the system.','Every agent works with the domain’s knowledge.','Small retained record icons near several agents update briefly. The common domain context is highlighted.'],
      ['The Director closes the loop.','Returns are checked against the request before the Director responds outside.','','Different returns converge at the Director. A check completes, then a single outward response leaves the domain.']
    ]},
    {id:'learning',name:'Learning and adaptation',cues:[
      ['Experience becomes evidence.','Corrections, failures and repeated work reveal what this domain needs to do better.','','A quality branch returns amber evidence of a correction. The evidence remains near the Director.'],
      ['Keep the useful lesson.','Review turns evidence into maintained guidance for this domain.','','Evidence reaches review, then a retained lesson becomes visible beside the quality responsibility.'],
      ['Use it on the next request.','The next matching task uses that lesson and passes the check that needed rework before.','Learning changes the next attempt.','A new request reaches the quality branch. It reads the retained lesson, passes its check and returns without the earlier rework.'],
      ['Inspect how the system works.','An Architect examines recurring demand, rework and underused parts of the domain.','Proposed adaptive operating concept.','A distinct violet Architect subgraph inside the domain receives evidence through the Director and inspects the surrounding branches.'],
      ['Grow where the work needs it.','Recurring work can earn a dedicated responsibility that other parts of the system can use.','','The Architect proposes a change through the Director. A new branch grows inside the same domain and receives work.'],
      ['Simplify when needs change.','Retire an underused responsibility. Keep a system that fits the work, rather than one that only grows.','Proposed adaptive operating concept.','An underused branch fades and is removed. The useful new responsibility stays, leaving a smaller, clearer structure.']
    ]},
    {id:'communication',name:'Across systems',cues:[
      ['Leave work in a shared exchange.','Systems coordinate through a common message layer while keeping their own context and ownership.','','Two domain systems sit on either side of an empty pending-message collection, without permanent external links or reserved inboxes.'],
      ['Messages appear when written.','New items join the pending collection and carry who they are for.','','A Director writes new messages. Colored rows appear in the shared collection and group by recipient.'],
      ['Collect when ready.','A recipient asks for its messages. Matching items leave the pending collection and enter its Director.','','The rose system asks for its messages. Matching rose rows are pulled into its Director; other pending work remains.'],
      ['A reply takes the same route.','The result is written back. The requesting system collects it, checks it, and continues.','Each domain stays responsible for its part.','The rose Director writes a teal reply to the collection. The teal Director later pulls the reply and resumes its internal work.']
    ]},
    {id:'human',name:'People in the loop',cues:[
      ['People use the same exchange.','A person can provide a request or contribute information without entering the system’s internals.','','A person writes an input into the shared message collection, and the system Director collects it.'],
      ['Ask when judgment is needed.','A question goes out. The work that needs an answer waits while other work can continue.','','One branch pauses for judgment. Another stays active. The Director writes a question into the shared collection.'],
      ['People answer and decide.','A person collects the question and places a decision back in the same exchange.','','The person pulls the question and writes a decision back. The waiting branch remains paused until that reply is collected.'],
      ['The answer unlocks the work.','The Director collects the reply, resumes the relevant work, and returns the outcome.','Human authority stays explicit.','The Director pulls the decision, resumes the paused branch and delivers a result back through the exchange to the person.']
    ]},
    {id:'scale',name:'Across the organisation',cues:[
      ['One domain is the starting point.','Start with a focused system that is useful on its own.','The same domain stays in view.','The familiar domain fills the view. It remains the fixed anchor as the camera later moves outward.'],
      ['Different domains need different systems.','Their shape, size and capabilities follow the work they own.','','The camera continuously pulls back to reveal neighboring systems with different shapes, sizes and internal compositions.'],
      ['An organisation can hold many.','Each system keeps its own context while contributing to a much larger whole.','','The same camera pulls farther back to reveal many varied domains across the organisation. The original domain remains visible at the center.'],
      ['Focused locally. Coordinated together.','Systems share work and expertise through a common exchange, without becoming one giant team.','Adopt one domain at a time.','Directors exchange sparse messages through a shared pending collection. Local work and context stay inside their separate domains.']
    ]}
  ];
  const $=id=>document.getElementById(id), clamp=x=>Math.max(0,Math.min(1,x));
  const ease=x=>{x=clamp(x);return x*x*(3-2*x);};
  const phase=(t,a,b)=>clamp((t-a)/(b-a));
  const flight=(t,a,b)=>phase(t,a,a+(b-a)/1.7);
  const fmt=n=>Number(n.toFixed(2));
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const scene=$('scene');let ci=0,qi=0,elapsed=0,last=0,paused=false,frame=0;
  const duration=5000;
  const text=(x,y,s,cls='label',color='',anchor='middle')=>`<text x="${x}" y="${y}" class="${cls}" text-anchor="${anchor}"${color?` style="fill:${color}"`:''}>${s}</text>`;
  const line=(pts,color=C.dim,width=1.3,opacity=1)=>`<path data-curve="true" d="${routeGeometry(pts).d}" fill="none" stroke="${color}" stroke-width="${width}" opacity="${opacity}" stroke-linecap="round"/>`;
  function dot(x,y,r=5,color=C.ink,glow=0){return `${glow?`<circle cx="${x}" cy="${y}" r="${r*2.7}" fill="${color}" opacity="${glow*.35}" filter="url(#glow)"/>`:''}<circle cx="${x}" cy="${y}" r="${r}" fill="${color}"/>`;}
  function check(x,y,color=C.teal,alpha=1){return `<g opacity="${alpha}"><circle cx="${x}" cy="${y}" r="13" fill="#0b2c2b" stroke="${color}"/><path d="M${x-6},${y} l4,4 8,-9" fill="none" stroke="${color}" stroke-width="2" stroke-linecap="round"/></g>`;}
  function file(x,y,color=C.teal,flash=0){return `<g transform="translate(${x},${y})"><path d="M0,0 h11 l5,5 v17 h-16 z M11,0 v5 h5 M4,10 h8 M4,14 h8" fill="${flash?'#174b42':'#0b2331'}" stroke="${color}" stroke-width="1.2"/>${flash?`<rect x="-4" y="-4" width="24" height="30" rx="5" fill="${color}" opacity="${flash*.17}"/>`:''}</g>`;}
  function signal(pts,p,color=C.teal,trail=true){p=clamp(p*1.7);if(p<=0||p>=1)return '';const [x,y]=pointOnRoute(routeGeometry(pts),p);return `${trail?line(pts,color,1.4,.27):''}<g data-moving-signal="true">${dot(fmt(x),fmt(y),5,color,1)}</g>`;}
  const root=[470,300];
  const branches=[
    {at:[325,187],trunk:[[421,281],[398,203]],leaves:[[227,164],[301,108]],leafCurves:[[[290,183],[265,162]],[[321,160],[306,140]]],color:C.blue},
    {at:[636,261],trunk:[[530,280],[568,268]],leaves:[[751,218]],leafCurves:[[[684,259],[713,228]]],color:C.rose},
    {at:[646,397],trunk:[[528,314],[568,383]],leaves:[[746,345],[703,438],[610,507]],leafCurves:[[[686,391],[711,354]],[[667,409],[684,431]],[[641,441],[621,473]]],color:C.teal},
    {at:[347,439],trunk:[[424,335],[397,409]],leaves:[[279,468],[380,531]],leafCurves:[[[323,452],[303,463]],[[350,478],[370,500]]],color:C.amber},
    {at:[267,345],trunk:[[395,305],[349,343]],leaves:[[210,415]],leafCurves:[[[242,356],[225,389]]],color:C.blue}
  ];
  const addedAt=[511,474],addedLeaves=[[461,522],[579,507]],architectAt=[485,146],architectNodes=[[443,167],[526,121],[546,167]];
  const edgeCurves=new Map(),routeCache=new Map();
  const pointKey=p=>p.map(n=>fmt(n)).join(','),edgeKey=(a,b)=>`${pointKey(a)}>${pointKey(b)}`;
  function registerCurve(a,c1,c2,b){edgeCurves.set(edgeKey(a,b),[c1,c2]);edgeCurves.set(edgeKey(b,a),[c2,c1]);}
  branches.forEach(b=>{registerCurve(root,...b.trunk,b.at);b.leaves.forEach((p,i)=>registerCurve(b.at,...b.leafCurves[i],p));});
  registerCurve(root,[489,352],[505,414],addedAt);
  registerCurve(addedAt,[494,493],[477,511],addedLeaves[0]);
  registerCurve(addedAt,[535,478],[557,498],addedLeaves[1]);
  registerCurve(root,[496,252],[501,197],architectAt);
  registerCurve(architectAt,[467,150],[455,164],architectNodes[0]);
  registerCurve(architectAt,[499,131],[513,121],architectNodes[1]);
  registerCurve(architectNodes[1],[540,132],[546,148],architectNodes[2]);
  function routeGeometry(pts){
    const key=pts.map(pointKey).join('>');if(routeCache.has(key))return routeCache.get(key);
    let d=`M${pts[0].join(',')}`,samples=[pts[0]],lengths=[0],total=0;
    for(let i=1;i<pts.length;i++){
      const a=pts[i-1],b=pts[i],dx=b[0]-a[0],dy=b[1]-a[1];
      const controls=edgeCurves.get(edgeKey(a,b))||[[a[0]+dx*.36-dy*.08,a[1]+dy*.22+dx*.08],[a[0]+dx*.69-dy*.08,a[1]+dy*.83+dx*.08]], [c1,c2]=controls;
      d+=` C${c1.join(',')} ${c2.join(',')} ${b.join(',')}`;
      for(let j=1;j<=80;j++){const t=j/80,u=1-t,p=[u*u*u*a[0]+3*u*u*t*c1[0]+3*u*t*t*c2[0]+t*t*t*b[0],u*u*u*a[1]+3*u*u*t*c1[1]+3*u*t*t*c2[1]+t*t*t*b[1]],last=samples.at(-1);total+=Math.hypot(p[0]-last[0],p[1]-last[1]);samples.push(p);lengths.push(total);}
    }
    const g={d,samples,lengths,total};routeCache.set(key,g);return g;
  }
  function pointOnRoute(g,p){const target=g.total*clamp(p);let i=g.lengths.findIndex(n=>n>=target);if(i<=0)return g.samples[0];const f=(target-g.lengths[i-1])/(g.lengths[i]-g.lengths[i-1]),a=g.samples[i-1],b=g.samples[i];return[a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f];}
  function boundary(color=C.teal,scale=1){return `<path data-boundary="true" d="M470,63 C585,43 741,90 773,210 C816,309 781,463 671,525 C565,601 388,593 291,535 C176,481 135,369 165,262 C175,145 326,58 470,63Z" fill="url(#cell-fill)" stroke="${color}" stroke-width="1.25" opacity="${scale}"/>`;}
  function system(opts={}){
    const active=opts.active||[],fade=opts.fade??1,removed=opts.removed??0,added=opts.added??0;
    let s=`<g opacity="${fade}">${boundary(opts.color||C.teal)}`;
    branches.forEach((b,i)=>{const op=i===0?1-removed:1,col=active.includes(i)?b.color:'#7796a7';s+=`<g data-branch="${i}" data-leaf-count="${b.leaves.length}" opacity="${op}">${line([root,b.at],col,active.includes(i)?2:1.2,active.includes(i)?1:.7)}`;b.leaves.forEach(p=>{s+=line([b.at,p],col,.85,.7)+dot(...p,2.7,col,active.includes(i)?.55:0);});s+=dot(...b.at,5,col,active.includes(i)?1:0)+'</g>';});
    if(added){s+=`<g data-added-branch="true" opacity="${added}">${line([root,addedAt],C.teal,1.6)}`;addedLeaves.forEach(p=>s+=line([addedAt,p],C.teal,.95)+dot(...p,3,C.teal));s+=dot(...addedAt,6,C.teal,1)+text(535,577,'New responsibility','small',C.teal)+'</g>';}
    s+=dot(...root,8,opts.rootColor||C.ink,opts.rootActive?1:.3);
    if(opts.director)s+=text(470,275,'Director','label',C.ink);
    if(opts.context)s+=`<g opacity="${opts.context}"><path d="M316,549 Q467,594 628,540" fill="none" stroke="${C.teal}" stroke-width="2" opacity=".65"/>${text(470,559,opts.contextLabel||'Shared domain context','quiet-label',C.teal)}</g>`;
    if(opts.records){s+=file(492,313,C.teal,opts.flash||0)+file(670,402,C.teal,opts.flash||0)+file(368,444,C.amber,opts.flash||0);}
    if(opts.architect){const a=opts.architect;s+=`<g data-architect="true" opacity="${a}"><path d="M424,100 C459,78 525,80 554,113 C577,148 561,193 524,207 C479,223 427,203 414,166 C405,139 407,115 424,100Z" fill="#342747" fill-opacity=".35" stroke="${C.violet}" stroke-width="1.1"/>${line([root,architectAt],C.violet,1.2,.65)}${line([architectAt,architectNodes[0]],C.violet,1)}${line([architectAt,architectNodes[1],architectNodes[2]],C.violet,1)}${dot(...architectAt,6,C.violet,1)}${architectNodes.map(p=>dot(...p,3,C.violet)).join('')}${text(488,75,'Architect','label',C.violet)}</g>`;}
    if(opts.name!==false)s+=text(470,620,'One domain','big-label',opts.color||C.teal);
    return s+'</g>';
  }
  function caller(label='Request',color=C.ink){return `${dot(60,300,6,color,.2)}${text(60,336,label,'label',color)}`;}
  function branchTrip(i,t,a,b,color,back=false){const p=phase(t,a,b),pts=back?[branches[i].leaves[0],branches[i].at,root]:[root,branches[i].at,branches[i].leaves[0]];return signal(pts,p,color||branches[i].color);}
  function baseScene(t){
    if(ci===0){
      let s=system({context:1,rootActive:qi>0,active:qi>=2?[2,3]:[]});
      if(qi===0)return s;
      s+=caller(qi===3?'Response':'Request',qi===3?C.teal:C.ink);
      if(qi===1)s+=signal([[60,300],root],phase(t,.04,.65),C.teal)+ (t>.65?`<circle cx="470" cy="300" r="${15+Math.sin(t*6)*2}" fill="none" stroke="${C.teal}" opacity=".65"/>`:'');
      if(qi===2){s+=branchTrip(2,t,.02,.35)+branchTrip(3,t,.02,.38);s+=branchTrip(2,t,.36,.60,null,true)+branchTrip(3,t,.62,.88,null,true);if(t>.60)s+=check(680,360,C.teal);if(t>.88)s+=check(409,432,C.amber);}
      if(qi===3){s+=check(505,286,C.teal,t>.15?1:0)+signal([root,[60,300]],phase(t,.25,.85),C.teal);if(t>.85)s+=check(60,300);}
      return s;
    }
    if(ci===1){
      let s=system({director:true,rootActive:true,context:qi>=2?1:.2,records:qi>=1,flash:qi===2?Math.sin(t*Math.PI)*.9:0,active:qi===1?[2,3]:qi===2?[1,2,3]:[]});
      if(qi===0){s+=caller('Outside');s+=signal([[60,300],root],phase(t,.03,.46));s+=signal([root,[60,300]],phase(t,.58,.96),C.teal);}
      if(qi===1){s+=file(492,313,C.teal,t<.3?1:0)+branchTrip(2,t,.22,.65)+branchTrip(3,t,.3,.8);}
      if(qi===2){s+=text(470,595,'History · Guidance · Guardrails · Tools','small');s+=branchTrip(1,t,.15,.5)+branchTrip(2,t,.32,.7)+branchTrip(3,t,.5,.9);}
      if(qi===3){s+=caller('Response',C.teal)+branchTrip(2,t,.01,.35,null,true)+branchTrip(3,t,.12,.5,null,true);if(t>.5)s+=check(507,288);s+=signal([root,[60,300]],phase(t,.6,.95));if(t>.95)s+=check(60,300);}
      return s;
    }
    if(ci===2){
      const arch=qi>=3?1:0,add=qi===4?ease(phase(t,.25,.7)):qi===5?1:0,removed=qi===5?ease(phase(t,.25,.8)):0;
      let s=system({director:qi>=3,context:1,rootActive:true,active:qi<3?[2]:[],architect:arch,added:add,removed});
      if(qi===0){s+=branchTrip(2,t,.05,.46,C.amber,true);s+=file(492,315,C.amber,t>.46?1:0);s+=text(688,476,'Correction','small',C.amber);if(t>.46)s+=dot(512,359,3,C.amber)+dot(528,359,3,C.amber)+dot(544,359,3,C.amber);}
      if(qi===1){s+=file(492,315,C.amber,t<.45?1:0);s+=signal([root,branches[2].at],phase(t,.2,.68),C.teal);if(t>.3)s+=file(670,402,C.teal,t<.8?1:0);if(t>.8)s+=text(699,483,'Lesson retained','small',C.teal);}
      if(qi===2){s+=caller('New request')+file(670,402,C.teal,t>.28&&t<.65?1:0);s+=signal([[60,300],root],phase(t,0,.23))+branchTrip(2,t,.24,.55)+branchTrip(2,t,.65,.93,C.teal,true);if(t>.57)s+=check(...branches[2].leaves[0]);if(t>.93)s+=check(505,284);}
      if(qi===3){s+=file(492,315,C.amber,0)+file(670,402,C.teal,0);s+=signal([branches[2].at,root,architectAt],phase(t,.05,.6),C.amber)+signal([branches[4].at,root,architectAt],phase(t,.25,.83),C.blue);s+=text(702,572,'Flow · Rework · Use','small',C.violet);}
      if(qi===4){s+=signal([architectAt,root],phase(t,.01,.24),C.violet);if(t>.7){s+=signal([root,addedAt,addedLeaves[1]],phase(t,.72,.96),C.teal);s+=check(607,507,C.teal,t>.96?1:0);}}
      if(qi===5){s+=signal([architectAt,root,branches[0].at],phase(t,0,.3),C.violet);if(t>.8)s+=text(326,178,'Retired','small','#607487');s+=check(607,507);}
      return s;
    }
    return ci===3?exchangeScene(t):ci===4?humanScene(t):scaleScene(t);
  }
  function miniCell(x,y,scale,color,active=false){return `<g transform="translate(${x},${y}) scale(${scale}) translate(-470,-300)">${system({color,name:false,rootActive:active,active:active?[2,3]:[]})}</g>`;}
  function messageRow(x,y,color,width=104,alpha=1){return `<g opacity="${alpha}"><rect x="${x}" y="${y}" width="${width}" height="28" rx="5" fill="${color}" fill-opacity=".11" stroke="${color}" stroke-opacity=".65"/><circle cx="${x+13}" cy="${y+14}" r="3" fill="${color}"/><path d="M${x+26},${y+10} h${width-39} M${x+26},${y+17} h${width-55}" stroke="${color}" stroke-width="1.1" opacity=".75"/></g>`;}
  function collection(rows){let s=`<rect x="390" y="168" width="162" height="274" rx="11" fill="#091b2a" stroke="#345064" stroke-width="1.2"/>${text(471,144,'Shared exchange','label')}${text(471,470,'Pending messages','small')}`;if(!rows.length)s+=text(471,305,'No pending items','small');rows.forEach(r=>s+=messageRow(r.x??419,r.y,r.color,r.width??104,r.alpha??1));return s;}
  function floatingRow(x,y,color,alpha=1){return messageRow(x-34,y-12,color,68,alpha);}
  function travelRow(a,b,p,color){if(p<=0||p>=1)return '';const [x,y]=pointOnRoute(routeGeometry([a,b]),ease(p));return floatingRow(fmt(x),fmt(y),color);}
  function exchangeScene(t){
    let s=miniCell(166,312,.43,C.teal,qi===3&&t>.6)+miniCell(781,312,.43,C.rose,qi===2&&t>.65);
    s+=text(166,491,'A domain','big-label',C.teal)+text(781,491,'Another domain','big-label',C.rose);
    let rows=[];
    if(qi===0)return s+collection(rows);
    if(qi===1){
      const ins=[{a:.05,b:.28,c:C.rose,y:213},{a:.25,b:.48,c:C.blue,y:285},{a:.45,b:.69,c:C.rose,y:249}];
      ins.forEach(r=>{const p=flight(t,r.a,r.b);if(p>=1)rows.push({y:r.y,color:r.c});else s+=travelRow([166,312],[471,r.y+14],p,r.c);});
      rows.sort((a,b)=>a.y-b.y);
    }
    if(qi===2){
      rows=[{y:285,color:C.blue}];
      const p=flight(t,.3,.76);if(p<1){rows.push({y:213,color:C.rose,alpha:1-p},{y:249,color:C.rose,alpha:1-p});s+=travelRow([471,227],[781,312],p,C.rose)+travelRow([471,263],[781,337],p,C.rose);}
      s+=signal([[781,312],[552,312]],phase(t,.03,.28),C.rose,false);if(t>.78)s+=check(820,286,C.rose);
      s+=text(780,127,'Anything for me?','label',C.rose);
    }
    if(qi===3){
      rows=[{y:285,color:C.blue}];const write=flight(t,.03,.34),pull=flight(t,.55,.86);
      if(write<1)s+=travelRow([781,312],[471,227],write,C.teal);else if(pull===0)rows.push({y:213,color:C.teal});
      if(pull>0&&pull<1)s+=travelRow([471,227],[166,312],pull,C.teal);
      s+=signal([[166,312],[390,312]],phase(t,.35,.53),C.teal,false);
      if(t>.86)s+=check(130,286)+miniBranchTrip(2,t,.87,1);
    }
    return s+collection(rows);
  }
  function person(x,y,color=C.amber,active=false){return `<g transform="translate(${x},${y})"><circle cx="0" cy="-29" r="18" fill="#122939" stroke="${color}" stroke-width="1.5"/><path d="M-34,37 v-15 q0,-31 34,-31 q34,0 34,31 v15" fill="#122939" stroke="${color}" stroke-width="1.5"/>${active?`<circle cx="0" cy="-29" r="27" fill="none" stroke="${color}" opacity=".3"/>`:''}</g>`;}
  const miniPoint=p=>[166+(p[0]-470)*.43,312+(p[1]-300)*.43];
  function miniBranchTrip(i,t,a,b,back=false){return `<g transform="translate(166,312) scale(.43) translate(-470,-300)">${branchTrip(i,t,a,b,C.teal,back)}</g>`;}
  function humanScene(t){
    let s=miniCell(166,312,.43,C.teal,qi>0)+person(781,312,C.amber,qi===2),rows=[];
    s+=text(166,491,'A domain','big-label',C.teal)+text(781,491,'A person','big-label',C.amber);
    if(qi===0){const w=flight(t,.02,.35),p=flight(t,.54,.88);s+=travelRow([781,312],[471,227],w,C.teal);if(w>=1&&p===0)rows.push({y:213,color:C.teal});s+=travelRow([471,227],[166,312],p,C.teal);if(t>.88)s+=check(130,286);}
    if(qi===1){
      const p=flight(t,.25,.6);s+=travelRow([166,312],[471,227],p,C.amber);if(p>=1)rows.push({y:213,color:C.amber});
      s+=`<g transform="translate(166,312) scale(.43) translate(-470,-300)"><circle cx="646" cy="397" r="12" fill="#102232" stroke="${C.amber}" stroke-width="2"/><path d="M642,392 v10 M650,392 v10" stroke="${C.amber}" stroke-width="2"/></g>`;
      s+=text(183,535,'Waiting for judgment','small',C.amber);
      s+=miniBranchTrip(3,t,.08,.46)+miniBranchTrip(3,t,.5,.9,true);
    }
    if(qi===2){
      const p=flight(t,.05,.38),w=flight(t,.58,.91);if(p===0)rows.push({y:213,color:C.amber});s+=travelRow([471,227],[781,312],p,C.amber);s+=travelRow([781,312],[471,227],w,C.teal);if(w>=1)rows.push({y:213,color:C.teal});
      s+=text(183,535,'Waiting for the reply','small',C.amber);if(t>.38)s+=check(827,280,C.amber);
    }
    if(qi===3){
      const p=flight(t,.02,.25),w=flight(t,.54,.73),receive=flight(t,.79,.99);if(p===0)rows.push({y:213,color:C.teal});s+=travelRow([471,227],[166,312],p,C.teal);
      s+=miniBranchTrip(2,t,.25,.39)+miniBranchTrip(2,t,.4,.53,true);
      s+=travelRow([166,312],[471,227],w,C.amber);if(w>=1&&receive===0)rows.push({y:213,color:C.amber});s+=travelRow([471,227],[781,312],receive,C.amber);
      if(t>.53)s+=check(...miniPoint(branches[2].at));if(t>.99)s+=check(827,280,C.amber);
    }
    return s+collection(rows);
  }
  const domainShapes=[
    'M-275,-80 C-240,-230 60,-245 245,-120 C350,0 210,200 30,225 C-155,250 -330,115 -275,-80Z',
    'M-140,-260 C20,-300 175,-185 180,-20 C225,130 155,270 -15,285 C-175,273 -218,95 -185,-65 C-210,-170 -245,-230 -140,-260Z',
    'M-330,-65 C-275,-180 -40,-200 110,-160 C290,-185 390,-70 330,80 C260,205 40,170 -130,170 C-290,165 -390,60 -330,-65Z',
    'M-205,-85 C-160,-210 15,-220 160,-135 C270,-45 215,155 70,190 C-90,230 -250,110 -205,-85Z',
    'M-225,-170 C-70,-245 110,-200 230,-80 C310,35 180,190 15,235 C-130,215 -265,95 -250,-60 C-255,-110 -249,-145 -225,-170Z'
  ];
  const arbors=[
    [[-160,-90],[130,-100],[165,100],[-100,145]],
    [[-100,-175],[110,-35],[60,175]],
    [[-225,-25],[-80,-105],[170,-80],[235,65],[45,110]],
    [[-110,-70],[105,-50],[50,120]],
    [[-135,-110],[35,-135],[155,-25],[110,120],[-45,155],[-160,40]]
  ];
  const innerScales=[[.78,.78],[.56,.8],[.9,.64],[.64,.67],[.69,.74]];
  const scaleDomains=[
    {id:0,x:470,y:300,sx:1,sy:1,color:C.teal,anchor:true},
    ...[
      [-400,140,.8,.9,2,0],[1320,150,1.5,.95,0,1],[300,-500,.45,.5,1,2],[680,1060,.8,.85,4,3],
      [-1120,-620,.65,.85,1,4],[1450,-770,1.05,.8,2,1],[-1160,850,.7,.46,0,0],[1600,1120,.62,.85,3,2],
      [-1900,100,.85,.65,4,3],[2660,250,1.85,1.5,0,4],[0,1700,.65,.72,1,0],[540,-1470,1.6,1,2,1],
      [-1780,-1300,1.2,.7,2,2],[2440,-750,.6,.85,1,3],[-2280,1160,.7,.9,3,4],[2370,1250,1.05,.8,4,0],
      [-710,-1730,.42,.58,1,1],[1680,-1680,.5,.4,0,2],[-1050,1800,.6,.5,4,3],[1500,1950,.9,1.05,1,4],
      [-2750,-720,.8,1,0,0],[3500,-350,1.15,.7,2,1],[-2730,520,.38,.65,1,2],[3280,1010,.55,.65,3,3],
      [-2330,-1920,.65,.5,4,4],[2850,-1590,.6,.65,1,0],[-2200,2050,1.65,.9,2,1],[2700,2130,.65,.5,0,2],
      [120,-2260,.75,.6,3,3],[760,2520,1.25,.65,2,4],[-3400,1630,.65,.75,4,0]
    ].map((d,i)=>({id:i+1,x:d[0],y:d[1],sx:d[2],sy:d[3],shape:d[4],arbor:d[5],color:[C.blue,C.rose,C.violet,C.teal,C.amber][i%5],origin:[i%3===0?-22:i%3===1?15:0,i%2?14:-8]}))
  ];
  function calmCurve(a,b,bend=18){const dx=b[0]-a[0],dy=b[1]-a[1],len=Math.hypot(dx,dy)||1,nx=-dy/len*bend,ny=dx/len*bend;return `M${a.join(',')} C${[a[0]+dx*.34+nx,a[1]+dy*.34+ny]} ${[a[0]+dx*.73+nx*.5,a[1]+dy*.73+ny*.5]} ${b.join(',')}`;}
  function smallDomain(d){
    const origin=d.origin,inner=innerScales[d.shape];let s=`<g data-scale-domain="${d.id}" data-domain-shape="${d.shape}" data-domain-arbor="${d.arbor}" transform="translate(${d.x},${d.y}) scale(${d.sx},${d.sy})"><path data-scale-outline="true" d="${domainShapes[d.shape]}" fill="${d.color}" fill-opacity=".035" stroke="${d.color}" stroke-width="1" opacity=".68"/><g transform="scale(${inner[0]},${inner[1]})">`;
    arbors[d.arbor].forEach((at,i)=>{
      s+=`<path data-local-curve="true" d="${calmCurve(origin,at,(i%2?1:-1)*(12+d.id%12))}" fill="none" stroke="#8ba5b7" stroke-width="1" opacity=".52"/>${dot(...at,4,'#99b3c5')}`;
      const a=Math.atan2(at[1]-origin[1],at[0]-origin[0]),n=1+(i+d.id)%2;
      for(let j=0;j<n;j++){const angle=a+(j-(n-1)/2)*.7,len=34+((i*19+d.id*13+j*23)%50),end=[at[0]+Math.cos(angle)*len,at[1]+Math.sin(angle)*len];s+=`<path data-local-curve="true" d="${calmCurve(at,end,(j?1:-1)*7)}" fill="none" stroke="#8ba5b7" stroke-width=".8" opacity=".45"/>${dot(...end,2.5,'#839eaf')}`;}
    });
    const contextY=[174,220,125,140,170][d.shape];s+=`<g data-domain-director="true">${dot(...origin,8,C.ink,.2)}</g></g><path d="M-45,${contextY} Q0,${contextY+15} 45,${contextY}" fill="none" stroke="${d.color}" stroke-width="2" opacity=".5"/>`;
    return s+'</g>';
  }
  function domainDirector(i){const d=scaleDomains[i],inner=innerScales[d.shape];return d.anchor?root:[d.x+d.origin[0]*inner[0]*d.sx,d.y+d.origin[1]*inner[1]*d.sy];}
  const exchangePoints=[[-600,-280],[980,680],[1060,1650]],exchangeAssignments=[[0,1],[1,0],[2,1],[4,2],[5,0],[6,1],[8,2],[9,0],[10,1],[13,0],[16,2],[20,2]];
  exchangeAssignments.forEach(([i,j])=>{const a=domainDirector(i),b=exchangePoints[j],dx=b[0]-a[0],dy=b[1]-a[1];registerCurve(a,[a[0]+dx*.36-dy*.06,a[1]+dy*.28+dx*.06],[a[0]+dx*.73-dy*.04,a[1]+dy*.77+dx*.04],b);});
  registerCurve(exchangePoints[0],[700,-120],[860,-50],exchangePoints[1]);
  registerCurve(exchangePoints[1],[1050,920],[1000,1350],exchangePoints[2]);
  function scalePacket(pts,p,color){p=clamp(p*1.7);if(p<=0||p>=1)return '';const [x,y]=pointOnRoute(routeGeometry(pts),p);return `<g data-scale-packet="true">${dot(fmt(x),fmt(y),19,color,.9)}</g>`;}
  function scaleScene(t){
    const zooms=[1,.34,.13,.125],from=qi?zooms[qi-1]:1,to=zooms[qi],zoom=from+(to-from)*ease(t),labelAlpha=clamp((zoom-.48)/.42);
    let world=scaleDomains.slice(1).map(smallDomain).join('');
    world+=`<g data-scale-domain="0" data-scale-anchor="true">${system({name:false,context:labelAlpha})}<g opacity="${labelAlpha}">${text(470,620,'One domain','big-label',C.teal)}</g></g>`;
    if(qi===3){
      const visible=ease(phase(t,.02,.13));
      world+=`<g data-scale-exchange="true" opacity="${visible}">`;
      exchangeAssignments.forEach(([i,j])=>world+=`<path data-exchange-route="${i}" data-exchange-access="${j}" d="${routeGeometry([domainDirector(i),exchangePoints[j]]).d}" fill="none" stroke="#7eacb8" stroke-width="7.5" opacity=".62"/>`);
      [[0,1],[1,2]].forEach(([i,j])=>world+=`<path data-exchange-backbone="true" d="${routeGeometry([exchangePoints[i],exchangePoints[j]]).d}" fill="none" stroke="#7eacb8" stroke-width="9" opacity=".65"/>`);
      world+=scalePacket([domainDirector(5),exchangePoints[0]],phase(t,.14,.34),C.rose)+scalePacket([exchangePoints[0],exchangePoints[1]],phase(t,.33,.53),C.rose)+scalePacket([exchangePoints[1],domainDirector(2)],phase(t,.52,.72),C.rose);
      world+=scalePacket([domainDirector(16),exchangePoints[2]],phase(t,.2,.4),C.teal)+scalePacket([exchangePoints[2],exchangePoints[1]],phase(t,.44,.64),C.teal)+scalePacket([exchangePoints[1],domainDirector(0)],phase(t,.68,.88),C.teal)+scalePacket([domainDirector(1),exchangePoints[0]],phase(t,.75,.95),C.blue);
      exchangePoints.forEach(([x,y],i)=>{world+=`<rect data-exchange-collection="${i}" x="${x-148}" y="${y-99}" width="296" height="198" rx="22" fill="#0b2230" stroke="#82a3ae" stroke-width="6"/>`;});
      const roseA=flight(t,.14,.34),roseAB=flight(t,.33,.53),roseOut=flight(t,.52,.72),tealC=flight(t,.2,.4),tealCB=flight(t,.44,.64),tealOut=flight(t,.68,.88),blueA=flight(t,.75,.95);
      if(roseA===1&&roseAB===0)world+=messageRow(exchangePoints[0][0]-113,exchangePoints[0][1]-70,C.rose,226);
      if(roseAB===1&&roseOut===0)world+=messageRow(exchangePoints[1][0]-113,exchangePoints[1][1]-70,C.rose,226);
      if(tealC===1&&tealCB===0)world+=messageRow(exchangePoints[2][0]-113,exchangePoints[2][1]-30,C.teal,226);
      if(tealCB===1&&tealOut===0)world+=messageRow(exchangePoints[1][0]-113,exchangePoints[1][1]-30,C.teal,226);
      if(blueA===1)world+=messageRow(exchangePoints[0][0]-113,exchangePoints[0][1]+10,C.blue,226);
      world+='</g>';
    }
    let s=`<defs><clipPath id="scale-view"><rect x="0" y="0" width="940" height="650"/></clipPath></defs><g clip-path="url(#scale-view)"><g class="scale-camera" data-scale-camera="true" data-zoom="${zoom}" transform="translate(470,300) scale(${zoom}) translate(-470,-300)">${world}</g></g>`;
    if(zoom<.48)s+=`<g opacity="${clamp((.48-zoom)/.12)}">${text(470,355,'The original domain','small',C.teal)}</g>`;
    if(qi===3)s+=`<g opacity="${ease(phase(t,.02,.13))}">${text(586,382,'Shared exchange','label','#b3cbd4')}</g>`;
    return s;
  }
  function render(t){scene.innerHTML=baseScene(t);$('diagram').dataset.chapter=chapters[ci].id;$('diagram').dataset.cue=String(qi+1);$('diagram').dataset.progress=String(fmt(t));$('scene-state').textContent=reduced.matches?'Ready':paused?'Paused':t>=1?'Ready':'Playing cue';$('pause').textContent=paused?'Resume':'Pause';$('pause').disabled=reduced.matches||t>=1;window.presenterState={chapter:chapters[ci].id,cue:qi+1,progress:t,paused,reduced:reduced.matches};}
  function updateText(){const ch=chapters[ci],cue=ch.cues[qi];$('chapter-name').textContent=ch.name;$('headline').textContent=cue[0];$('explanation').textContent=cue[1];$('takeaway').textContent=cue[2];$('scene-title').textContent=cue[0];$('scene-description').textContent=cue[3];$('chapter').value=ch.id;$('cue-count').textContent=`${qi+1} / ${ch.cues.length}`;$('cue-buttons').innerHTML=ch.cues.map((c,i)=>`<button type="button" data-cue="${i}" aria-label="Cue ${i+1}: ${c[0]}" aria-current="${i===qi}" class="${i<qi?'completed':''}"></button>`).join('');$('previous').disabled=ci===0&&qi===0;$('next').disabled=ci===chapters.length-1&&qi===ch.cues.length-1;document.title=`${ch.name} · Inside agentic systems · GPT-6.1 Sol`;}
  function tick(now){if(!last)last=now;if(!paused)elapsed+=now-last;last=now;const t=reduced.matches?1:clamp(elapsed/duration);render(t);if(t<1)frame=requestAnimationFrame(tick);}
  function restart(){cancelAnimationFrame(frame);elapsed=0;last=0;paused=false;render(reduced.matches?1:0);if(!reduced.matches)frame=requestAnimationFrame(tick);}
  function go(c,q,hash=true){ci=Math.max(0,Math.min(chapters.length-1,Math.trunc(c)));qi=Math.max(0,Math.min(chapters[ci].cues.length-1,Math.trunc(q)));if(hash)history.replaceState(null,'',`#${chapters[ci].id}~${qi+1}`);updateText();restart();}
  function readHash(){const m=location.hash.slice(1).split('~'),found=chapters.findIndex(c=>c.id===m[0]);go(found<0?0:found,Number.isFinite(Number(m[1]))?Math.max(0,Number(m[1])-1):0,false);}
  function next(){if(qi<chapters[ci].cues.length-1)go(ci,qi+1);else if(ci<chapters.length-1)go(ci+1,0);}
  function previous(){if(qi>0)go(ci,qi-1);else if(ci>0)go(ci-1,chapters[ci-1].cues.length-1);}
  function pause(){if(reduced.matches||elapsed>=duration)return;paused=!paused;last=performance.now();render(clamp(elapsed/duration));}
  $('next').addEventListener('click',next);$('previous').addEventListener('click',previous);$('replay').addEventListener('click',restart);$('pause').addEventListener('click',pause);$('chapter').addEventListener('change',e=>go(chapters.findIndex(c=>c.id===e.target.value),0));$('cue-buttons').addEventListener('click',e=>{const b=e.target.closest('[data-cue]');if(b)go(ci,Number(b.dataset.cue));});
  document.addEventListener('keydown',e=>{if(e.altKey||e.ctrlKey||e.metaKey||e.repeat||e.target.closest('input,select,textarea,[contenteditable=true]'))return;if(e.key==='ArrowRight'){e.preventDefault();next();}else if(e.key==='ArrowLeft'){e.preventDefault();previous();}else if(e.key.toLowerCase()==='r'){e.preventDefault();restart();}else if(e.key==='Home'){e.preventDefault();go(ci,0);}else if(e.code==='Space'&&!e.target.closest('button,a')){e.preventDefault();pause();}});
  window.addEventListener('hashchange',readHash);reduced.addEventListener('change',restart);document.addEventListener('visibilitychange',()=>{last=performance.now();});readHash();
})();
