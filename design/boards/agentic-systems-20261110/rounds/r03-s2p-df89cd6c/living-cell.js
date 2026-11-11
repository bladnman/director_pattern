/* A living cell's anatomy. The presenter supplies every clock and work event. */
(function (host) {
  'use strict';

  const NS = 'http://www.w3.org/2000/svg';
  const ice = '#dbeaf7';
  const clamp = (n, lo, hi) => Math.max(lo, Math.min(hi, n));
  const mix = (a, b, t) => a + (b - a) * t;
  const node = (tag, attrs, text) => {
    const n = document.createElementNS(NS, tag);
    for (const [key, value] of Object.entries(attrs || {})) n.setAttribute(key, value);
    if (text) n.textContent = text;
    return n;
  };
  const hash = (s) => [...String(s)].reduce((a, c) => ((a * 31) + c.charCodeAt(0)) >>> 0, 7);
  const noise = (n) => { const v = Math.sin(n * 12.9898 + 78.233) * 43758.5453; return v - Math.floor(v); };
  const catchAt = (age) => Number.isFinite(age) && age >= 0
    ? Math.exp(-age/760) * (.35 + .65*Math.sin(Math.PI*clamp(age/620,0,1))) : 0;
  const beatAt = (progress,at,width=.14) => {
    const age=(progress-at)/width;
    return age>=0&&age<1 ? (.22+.78*Math.sin(Math.PI*age))*Math.pow(1-age,.65) : 0;
  };

  // Each arbor has its own silhouette, branch depth and open spaces. Coordinates
  // are cell-local; parents refer to earlier nodes, with -1 meaning the role hub.
  const anatomy = {
    design: { hub: [-80, -72], radius: 6.2, label: [-13, -16, 'end'], bend: -17, nodes: [
      [-136,-127,-1],[-158,-173,0],[-148,-218,1],[-181,-204,1],[-204,-180,1],
      [-180,-142,0],[-225,-140,5],[-206,-111,5],[-155,-98,-1],[-205,-84,8],
      [-237,-64,9],[-220,-43,9],[-190,-57,8],[-116,-154,0],[-111,-208,13]
    ]},
    engineering: { hub: [115, -142], radius: 7.5, label: [12, 17, 'start'], bend: 26, nodes: [
      [134,-181,-1],[152,-225,0],[183,-194,0],[198,-167,2],[225,-138,3],
      [190,-122,-1],[240,-96,5],[226,-70,5],[159,-112,-1],[206,-82,8],
      [94,-195,-1],[80,-236,10],[116,-239,10],[50,-216,10],[143,-156,-1],
      [181,-155,14],[159,-201,14],[204,-190,16]
    ]},
    quality: { hub: [171, 53], radius: 4.7, label: [10, -15, 'start'], bend: -23, nodes: [
      [211,39,-1],[247,22,0],[232,72,-1],[254,81,2],[208,114,-1],
      [233,147,4],[179,153,4],[191,190,6],[128,108,-1],[145,161,8]
    ]},
    operations: { hub: [-16, 171], radius: 5.6, label: [-13, 5, 'end'], bend: 23, nodes: [
      [-31,182,-1],[-58,218,0],[-91,230,1],[-49,252,1],[-4,210,0],
      [27,245,4],[46,219,4],[64,170,-1],[93,214,7],[117,202,8],
      [-84,165,-1],[-138,194,10],[-128,220,11],[-111,157,10]
    ]},
    research: { hub: [-135, 43], radius: 4.2, label: [-10, -15, 'end'], bend: 17, nodes: [
      [-208,19,-1],[-247,-7,0],[-231,49,0],[-215,90,2],[-243,113,3],
      [-198,142,3],[-174,195,5],[-153,174,5],[-141,120,-1],[-109,143,8],
      [-229,76,2],[-211,-20,0],[-234,-47,11]
    ]}
  };

  function smoothLoop(points) {
    let d = `M${points[0].x.toFixed(3)},${points[0].y.toFixed(3)}`;
    for (let i = 0; i < points.length; i++) {
      const p0 = points[(i - 1 + points.length) % points.length];
      const p1 = points[i], p2 = points[(i + 1) % points.length], p3 = points[(i + 2) % points.length];
      d += ` C${(p1.x+(p2.x-p0.x)/6).toFixed(3)},${(p1.y+(p2.y-p0.y)/6).toFixed(3)}`;
      d += ` ${(p2.x-(p3.x-p1.x)/6).toFixed(3)},${(p2.y-(p3.y-p1.y)/6).toFixed(3)}`;
      d += ` ${p2.x.toFixed(3)},${p2.y.toFixed(3)}`;
    }
    return d + ' Z';
  }

  function cubic(a, b, bend) {
    const dx = b.x-a.x, dy = b.y-a.y, length = Math.max(1, Math.hypot(dx, dy));
    return [a, {x:a.x+dx*.28-dy/length*bend, y:a.y+dy*.28+dx/length*bend},
      {x:a.x+dx*.72-dy/length*bend*.65, y:a.y+dy*.72+dx/length*bend*.65}, b];
  }
  const cubicPath = (p) => `M${p[0].x},${p[0].y} C${p[1].x},${p[1].y} ${p[2].x},${p[2].y} ${p[3].x},${p[3].y}`;
  function cubicPoint(p, t) {
    const u = 1-t;
    return {x:u*u*u*p[0].x+3*u*u*t*p[1].x+3*u*t*t*p[2].x+t*t*t*p[3].x,
      y:u*u*u*p[0].y+3*u*u*t*p[1].y+3*u*t*t*p[2].y+t*t*t*p[3].y};
  }

  function wirePoint(path,curve,amount) {
    const p=clamp(amount,0,1);
    if(typeof path.getTotalLength==='function') {
      const point=path.getPointAtLength(path.getTotalLength()*p);
      return {x:point.x,y:point.y};
    }
    return cubicPoint(curve,p);
  }

  function create({id='cell', name='', roles, labels=true, simple=false, color='#27ddc8', variant=0} = {}) {
    const identity = hash(id + ':' + variant);
    const variantValue = typeof variant === 'number' ? variant : hash(variant) % 11;
    const main = !variantValue;
    const phase = (identity % 628) / 100;
    const rotation = main ? 0 : (noise(identity+4)-.5)*.55;
    const proportions = [[1,1],[.91,1.08],[1.10,.87],[.94,1.12],[1.07,.96]][variantValue % 5];
    const width = main ? 1 : proportions[0];
    const height = main ? 1 : proportions[1];
    const channels=/^#([0-9a-f]{6})$/i.exec(color)?.[1];
    const brightColor=channels?'#'+[0,2,4].map(i=>Math.round(parseInt(channels.slice(i,i+2),16)*.59+255*.41).toString(16).padStart(2,'0')).join(''):'#b6fff1';
    const g = node('g', {id, class:'cell living-cell', 'data-anatomy':variantValue});
    const unique = ('living-'+id).replace(/[^a-zA-Z0-9_-]/g,'-');
    const defs = node('defs');
    const fill = node('radialGradient', {id:unique+'-fill', cx:'.43', cy:'.42', r:'.65'});
    fill.append(node('stop', {offset:'0', 'stop-color':'#102c3a', 'stop-opacity':'.13'}),
      node('stop', {offset:'.72', 'stop-color':'#0b252d', 'stop-opacity':'.20'}),
      node('stop', {offset:'1', 'stop-color':color, 'stop-opacity':'.12'}));
    defs.append(fill); g.append(defs);
    const aura = node('path', {fill:'none', stroke:color, 'stroke-width':'12', opacity:'.055', filter:'url(#glow)'});
    const mem = node('path', {class:'living-membrane', fill:`url(#${unique}-fill)`, stroke:color, 'stroke-width':'1.55', opacity:'.91'});
    const inner = node('path', {fill:'none', stroke:color, 'stroke-width':'.8', 'stroke-dasharray':'2 12', opacity:'.29'});
    g.append(aura, mem, inner);
    const structure = node('g', {class:'living-structure'}); g.append(structure);
    const rs = {};
    let nucleus = {x:0,y:0};

    function radiusAt(angle) {
      return 265*(1+.034*Math.sin(angle*3+1.1+variantValue*.31)+.022*Math.cos(angle*5-.7));
    }

    function breathingAt(angle,t) {
      return 4.4*Math.sin(t*.77+phase)+3.1*Math.sin(angle*3-t*.53+phase)+1.6*Math.cos(angle*5+t*.31);
    }

    function basePoint(x,y) {
      const r = Math.hypot(x,y), angle = Math.atan2(y,x);
      const limit = radiusAt(angle+rotation)-17;
      // Ease distant tips toward their local wall. A shared circular clipping
      // radius would turn unequal branch lengths into another repeated fringe.
      if (r > limit-14) {
        const fitted=limit-14+14*(1-Math.exp(-(r-limit+14)/14));
        x*=fitted/r; y*=fitted/r;
      }
      return {x:(x*Math.cos(rotation)-y*Math.sin(rotation))*width,
        y:(x*Math.sin(rotation)+y*Math.cos(rotation))*height};
    }

    for (const [ri, role] of (roles || Object.keys(anatomy).map(key => ({id:key,name:key}))).entries()) {
      const profile = anatomy[role.id];
      if (!profile) continue;
      const roleSeed=hash(role.id)+variantValue*137;
      const hubReach=main?1:.83+noise(roleSeed)*.31;
      const hub = basePoint(profile.hub[0]*hubReach,profile.hub[1]*hubReach);
      const spread=main?1:.75+noise(roleSeed+8)*.47;
      const twist=main?0:(noise(roleSeed+12)-.5)*.53;
      const rg = node('g', {'data-role':role.id, class:'role living-role'});
      const path = node('path', {class:'living-trunk', fill:'none', stroke:ice, 'stroke-width':'1.1', opacity:'.48'});
      const shadow = node('path', {fill:'none', stroke:color, 'stroke-width':'6', opacity:'0', filter:'url(#soft)'});
      rg.append(shadow, path);
      const arbor = [], depth = [], roots=[];
      const workRoots={design:[0],engineering:[0,10],quality:[4,8],operations:[0,10],research:[0]}[role.id];
      for (let j=0;j<profile.nodes.length;j++) {
        const [x,y,parent] = profile.nodes[j];
        depth[j] = parent < 0 ? 1 : depth[parent]+1;
        if(parent<0)roots.push(j);
        // Neighbors retain different silhouettes; reducing detail never turns
        // every responsibility into the same three-pronged symbol.
        if (simple && depth[j] > 2+(variantValue+ri)%3 && noise(roleSeed+j*17) < .72) continue;
        if (parent >= 0 && !arbor[parent]) continue;
        const dx=(x-profile.hub[0])*spread,dy=(y-profile.hub[1])*spread;
        const endpoint = basePoint(profile.hub[0]*hubReach+dx*Math.cos(twist)-dy*Math.sin(twist),
          profile.hub[1]*hubReach+dx*Math.sin(twist)+dy*Math.cos(twist));
        const edge = node('path', {class:'living-filament', fill:'none', stroke:ice, 'stroke-width':'.75', opacity:'.34'});
        const pin = node('circle', {r:depth[j]===1?2.5:1.7, fill:ice, opacity:'.64'});
        const flow=node('g',{class:'living-branch-flow',opacity:'0','pointer-events':'none'});
        const flowHalo=node('circle',{r:7,fill:color,opacity:'.28',filter:'url(#soft)'});
        const flowTail=node('circle',{r:1.2,fill:brightColor,opacity:'.48'});
        const flowDot=node('circle',{r:2.4,fill:'#e3fff8'});
        flow.append(flowHalo,flowTail,flowDot);
        rg.append(edge,flow,pin);
        const root=parent<0?j:arbor[parent].root;
        const onset=parent<0?.065+roots.indexOf(j)*.11:arbor[parent].onset+.13+noise(roleSeed+j)*.085;
        arbor[j] = {edge,pin,base:endpoint,parent,root,used:workRoots.includes(root),depth:depth[j],
          bend:(noise(identity+ri*50+j)-.5)*19,point:endpoint,onset,children:[],
          flow,flowHalo,flowTail,flowDot,curve:null};
      }
      for(const branch of arbor.filter(Boolean))if(branch.parent>=0)arbor[branch.parent].children.push(branch);
      // Completion follows the actual tree. A parent waits for every used
      // child; only then can its own edge carry a result toward the role hub.
      for(const [j,branch] of arbor.entries()) {
        if(!branch||!branch.used)continue;
        const parent=branch.parent<0?hub:arbor[branch.parent].base;
        branch.travel=.10+Math.min(100,Math.hypot(branch.base.x-parent.x,branch.base.y-parent.y))*.0008;
        branch.outStart=branch.parent<0?.025+roots.indexOf(j)*.045:arbor[branch.parent].outEnd+.025;
        branch.outEnd=branch.outStart+branch.travel;
      }
      for(const [j,branch] of [...arbor.entries()].reverse()) {
        if(!branch||!branch.used)continue;
        const children=branch.children.filter(child=>child.used);
        const ready=children.length?Math.max(...children.map(child=>child.returnEnd)):.02+noise(roleSeed+j)*.065;
        branch.returnReady=ready;
        branch.returnStart=ready+.045;
        branch.returnEnd=branch.returnStart+branch.travel;
      }
      const used=arbor.filter(branch=>branch?.used);
      const outwardScale=.82/Math.max(...used.map(branch=>branch.outEnd));
      const returnScale=.82/Math.max(...used.filter(branch=>branch.parent<0).map(branch=>branch.returnEnd));
      for(const branch of used) {
        branch.outStart*=outwardScale;branch.outEnd*=outwardScale;
        branch.returnReady*=returnScale;branch.returnStart*=returnScale;branch.returnEnd*=returnScale;
      }
      const halo = node('circle', {r:profile.radius*3.8, fill:'url(#star)', opacity:'.37'});
      const core = node('circle', {r:profile.radius, fill:ice, opacity:'.92'});
      rg.append(halo,core);
      let label;
      if (labels) {
        label=node('text', {'text-anchor':profile.label[2], fill:ice, class:'node-label living-label',
          style:'font-size:14px;font-weight:570;letter-spacing:.5px;paint-order:stroke;stroke:#061017;stroke-width:3px;stroke-linejoin:round'},role.name);
        rg.append(label);
      }
      rs[role.id] = {group:rg,path,label,arbor,hub,point:hub,profile,halo,core,shadow,curve:null,phase:phase+ri*1.67};
      structure.append(rg);
    }

    const centerHalo = node('circle', {r:33, fill:'url(#star)', opacity:'.85'});
    const centerCore = node('circle', {r:10.5, fill:'#effaff', opacity:'.98'});
    g.append(centerHalo,centerCore);
    const directorLabel = labels ? node('text', {'text-anchor':'middle', fill:ice,
      style:'font-size:14px;letter-spacing:.7px;font-weight:600;paint-order:stroke;stroke:#061017;stroke-width:3px'},'Director') : null;
    if (directorLabel) g.append(directorLabel);
    const domainLabel = labels ? node('text', {'text-anchor':'middle', fill:color, y:-301,
      style:'font-size:14px;letter-spacing:2.4px;font-weight:520'},name) : null;
    if (domainLabel) g.append(domainLabel);

    function deform(base,t,rolePhase,depth,impact) {
      const x=base.x/width,y=base.y/height;
      const radial=Math.hypot(x,y)/265,angle=Math.atan2(y,x);
      const swell=breathingAt(angle,t)/265;
      const flex=Math.sin(t*.51+angle*2+phase)*1.5*radial;
      const distal=Math.sin(t*.68+rolePhase+radial*2.4)*depth*.38;
      return {
        x:base.x*(1+swell)-Math.sin(angle)*(flex+distal)+base.x/265*impact*2.2,
        y:base.y*(1+swell)+Math.cos(angle)*(flex+distal)+base.y/265*impact*2.2
      };
    }

    function update(timeMs=0,{active={},arrivals={},reducedMotion=false}={}) {
      const t = reducedMotion ? 0 : Math.max(0,timeMs)/1000;
      const membranePoints = [];
      const impacts = Object.entries(arrivals).map(([roleId,age]) => {
        const role=rs[roleId];
        return role && Number.isFinite(age) && age>=0 ? {angle:Math.atan2(role.hub.y,role.hub.x),
          amount:reducedMotion?0:Math.exp(-age/1000)*Math.sin(age/210)*3.8} : null;
      }).filter(Boolean);
      for(let i=0;i<36;i++) {
        const a=i/36*Math.PI*2;
        const anatomyRadius=radiusAt(a);
        const breath=reducedMotion?0:breathingAt(a,t);
        const response=impacts.reduce((sum,v)=>sum+v.amount*Math.exp(-Math.pow(Math.atan2(Math.sin(a-v.angle),Math.cos(a-v.angle))/.5,2)),0);
        const r=anatomyRadius+breath+response;
        membranePoints.push({x:Math.cos(a)*r*width, y:Math.sin(a)*r*height});
      }
      const d=smoothLoop(membranePoints);
      mem.setAttribute('d',d); aura.setAttribute('d',d);
      inner.setAttribute('d',smoothLoop(membranePoints.map(p=>({x:p.x*.962,y:p.y*.962}))));
      nucleus = reducedMotion ? {x:0,y:0} : {x:Math.sin(t*.62+phase)*.65,y:Math.cos(t*.57+phase)*.75};
      centerCore.setAttribute('cx',nucleus.x); centerCore.setAttribute('cy',nucleus.y);
      centerHalo.setAttribute('cx',nucleus.x); centerHalo.setAttribute('cy',nucleus.y);
      const directorCatch=reducedMotion?0:catchAt(arrivals.director);
      centerCore.setAttribute('r',10.5+(reducedMotion?0:directorCatch*5.1));
      centerCore.style.fill=directorCatch>.04?'#e8fff9':'#effaff';
      centerHalo.setAttribute('r',reducedMotion?33:33+Math.sin(t*.77+phase)*1.1+directorCatch*21);
      centerHalo.style.opacity=String(clamp(.85+directorCatch*.24,0,1));
      if(directorLabel){directorLabel.setAttribute('x',nucleus.x);directorLabel.setAttribute('y',nucleus.y+31);}

      for(const [roleId,role] of Object.entries(rs)) {
        const age=arrivals[roleId];
        const arrival=Number.isFinite(age)&&age>=0 ? Math.exp(-age/900) : 0;
        const receiptCatch=reducedMotion?0:catchAt(age);
        const impact=reducedMotion||!arrival?0:arrival*Math.sin(age/170);
        const activity=active[roleId];
        const directed=activity&&typeof activity==='object'&&['outbound','return','cycle'].includes(activity.direction);
        const progress=directed?activity.progress:activity;
        const working=Number.isFinite(progress);
        const p=working?clamp(progress,0,1):0;
        let direction=directed?activity.direction:'legacy',flowProgress=p;
        if(direction==='cycle') {
          direction=p<.56?'outbound':'return';
          flowProgress=p<.56?clamp(p/.44,0,1):clamp((p-.56)/.44,0,1);
        }
        const rootReturns=role.arbor.filter(branch=>branch?.used&&branch.parent<0).map(branch=>branch.returnEnd);
        const finishCatch=working&&direction==='return'&&!reducedMotion
          ? Math.max(...rootReturns.map(at=>beatAt(flowProgress,at)),beatAt(flowProgress,.86)) : 0;
        const workGlow=working?(direction==='return'?.10+finishCatch*.65:Math.sin(p*Math.PI)*.42+.12):0;
        role.point=reducedMotion?role.hub:deform(role.hub,t,role.phase,0,impact);
        role.curve=cubic(nucleus,role.point,role.profile.bend);
        const trunkD=cubicPath(role.curve);
        role.path.setAttribute('d',trunkD);role.shadow.setAttribute('d',trunkD);
        role.path.style.stroke=working||arrival>.04?brightColor:ice;
        role.path.style.opacity=String(clamp(.38+arrival*.51+workGlow*.62,0,1));
        role.path.style.strokeWidth=String(1.02+arrival*.6+workGlow*.9);
        role.shadow.style.opacity=String(arrival*.21+workGlow*.15);
        for(const [j,branch] of role.arbor.entries()) {
          if(!branch)continue;
          branch.point=reducedMotion?branch.base:deform(branch.base,t,role.phase,branch.depth,impact);
          const parent=branch.parent<0?role.point:role.arbor[branch.parent].point;
          branch.curve=cubic(parent,branch.point,branch.bend);
          branch.edge.setAttribute('d',cubicPath(branch.curve));
          // Work recruits connected subtrees. Other arms remain reference
          // anatomy, and each fork answers after its own parent rather than
          // coloring a whole role at once. Receipt itself belongs to the hub.
          let response=working&&branch.used?Math.exp(-Math.pow((p-branch.onset)/.11,2)):0;
          let recruited=working&&branch.used&&p>=branch.onset ? .17 : 0;
          let nodeCatch=0;
          branch.flow.setAttribute('opacity','0');
          if(directed&&working&&branch.used) {
            const returning=direction==='return';
            const start=returning?branch.returnStart:branch.outStart;
            const end=returning?branch.returnEnd:branch.outEnd;
            const f=(flowProgress-start)/(end-start);
            response=f>=0&&f<=1?Math.sin(Math.PI*f)*.75+.2:0;
            recruited=returning?.13:flowProgress>=end?.17:0;
            const receives=returning?branch.children.filter(child=>child.used).map(child=>child.returnEnd):[branch.outEnd];
            const finishes=returning?[(branch.returnReady+branch.returnStart)/2]:[];
            nodeCatch=reducedMotion?0:Math.max(0,...receives.concat(finishes).map(at=>beatAt(flowProgress,at)));
            if(f>=0&&f<=1&&!reducedMotion) {
              const along=returning?1-f:f;
              const q=wirePoint(branch.edge,branch.curve,along);
              const tail=wirePoint(branch.edge,branch.curve,returning?1-clamp(f-.12,0,1):clamp(f-.12,0,1));
              for(const n of [branch.flowHalo,branch.flowDot]){n.setAttribute('cx',q.x);n.setAttribute('cy',q.y);}
              branch.flowTail.setAttribute('cx',tail.x);branch.flowTail.setAttribute('cy',tail.y);
              branch.flow.setAttribute('opacity','1');
            }
          }
          const energy=clamp(response*.82+recruited+nodeCatch*.23,0,1);
          branch.edge.style.stroke=energy>.12?brightColor:ice;
          branch.edge.style.opacity=String(.23+energy*.76);
          branch.edge.style.strokeWidth=String(.70+energy*1.02);
          branch.pin.setAttribute('cx',branch.point.x);branch.pin.setAttribute('cy',branch.point.y);
          branch.pin.setAttribute('r',(branch.depth===1?2.5:1.7)+(reducedMotion?0:energy*2.0+nodeCatch*2.4));
          branch.pin.style.fill=energy>.17?'#cbfff6':ice;
          branch.pin.style.opacity=String(.48+energy*.51);
        }
        for(const n of [role.core,role.halo]){n.setAttribute('cx',role.point.x);n.setAttribute('cy',role.point.y);}
        role.core.setAttribute('r',role.profile.radius+(reducedMotion?0:receiptCatch*4.1+workGlow*.8+finishCatch*4.1));
        role.core.style.fill=arrival>.1||finishCatch>.1?'#e7fffb':ice;
        role.halo.style.opacity=String(clamp(.30+receiptCatch*.70+workGlow*.37+finishCatch*.70,0,1));
        role.halo.setAttribute('r',role.profile.radius*(3.8+(reducedMotion?0:receiptCatch*2.0+workGlow*.8+finishCatch*2.0)));
        if(role.label){role.label.setAttribute('x',role.point.x+role.profile.label[0]);role.label.setAttribute('y',role.point.y+role.profile.label[1]);}
      }
      return api;
    }

    const api={g,rs,mem,update,
      point(roleId='director'){return roleId==='director'?{...nucleus}:rs[roleId]?{...rs[roleId].point}:null;},
      route(roleId){return rs[roleId]?.path||null;},
      sample(roleId,progress,reverse=false){
        const role=rs[roleId];if(!role)return null;
        const amount=clamp(reverse?1-progress:progress,0,1);
        // Non-rendering consumers use the identical cubic, never a second wire.
        return wirePoint(role.path,role.curve,amount);
      }};
    update(0);
    return api;
  }

  host.LivingCell={create};
})(typeof window==='undefined'?globalThis:window);
