window.triggerRocketLogin=function(options){
  options=options||{};
  var card=document.getElementById('authLoginCard'),overlay=document.getElementById('authOverlay');
  if(!card||!overlay||document.querySelector('.rocket-login-layer'))return;
  var reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rect=card.getBoundingClientRect(),width=rect.width,height=rect.height;
  var layer=document.createElement('div');
  layer.className='rocket-login-layer';layer.setAttribute('aria-hidden','true');
  layer.style.cssText='position:fixed;inset:0;z-index:14000;pointer-events:none;overflow:hidden';
  var space=document.createElement('img');
  space.src='assets/rocket-space.gif';space.alt='';
  space.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0';
  layer.appendChild(space);
  var bird=document.createElement('div');
  bird.style.cssText='position:absolute;left:'+rect.left+'px;top:'+rect.top+'px;width:'+width+'px;height:'+height+'px;transform-origin:50% 50%';
  layer.appendChild(bird);
  var targets=[[[200,8],[156,76],[200,76]],[[200,8],[200,76],[244,76]],[[156,76],[244,76],[244,202]],[[156,76],[244,202],[156,202]],[[156,148],[156,217],[112,231]],[[244,148],[288,231],[244,217]],[[170,202],[230,202],[230,219]],[[170,202],[230,219],[170,219]]];
  var factor=Math.min(1.45,width*.96/400,height*.7/250),ox=(width-400*factor)/2,oy=(height-250*factor)/2;
  var pieces=[];
  targets.forEach(function(target,index){
    var cell=Math.floor(index/2),x=(cell%2)*width/2,y=Math.floor(cell/2)*height/2;
    var source=index%2?[[x,y],[x+width/2,y+height/2],[x,y+height/2]]:[[x,y],[x+width/2,y],[x+width/2,y+height/2]];
    var piece=document.createElement('div');
    piece.style.cssText='position:absolute;inset:0;transform-origin:0 0;will-change:transform;overflow:hidden;background:#30495b;clip-path:polygon('+source.map(function(p){return p[0]+'px '+p[1]+'px';}).join(',')+')';
    var clone=cloneGravityElement(card);
    clone.style.cssText+=';position:absolute;inset:0;margin:0;width:'+width+'px;height:'+height+'px;max-width:none;max-height:none;box-sizing:border-box;pointer-events:none;animation:none;transform:none';
    piece.appendChild(clone);bird.appendChild(piece);
    pieces.push({element:piece,source:source,target:target});
  });
  var flame=document.createElement('div');
  flame.style.cssText='position:absolute;left:'+(ox+172*factor)+'px;top:'+(oy+215*factor)+'px;width:'+(56*factor)+'px;height:'+(100*factor)+'px;transform-origin:50% 0;opacity:0;background:linear-gradient(#fff6b0 0%,#ffc22e 28%,#ff5c22 65%,transparent);clip-path:polygon(0 0,100% 0,78% 48%,58% 100%,35% 73%,15% 45%);filter:drop-shadow(0 0 12px #ff8b20)';
  bird.insertBefore(flame,bird.firstChild);
  var cat=document.createElement('img');cat.src='assets/rocket-cat.png';cat.alt='';
  cat.style.cssText='position:absolute;left:65%;top:24%;width:min(30vw,250px);height:44%;object-fit:contain;opacity:0;filter:drop-shadow(0 0 6px #b5ddff88)';
  layer.appendChild(cat);
  var finale=document.createElement('img');finale.alt='';
  finale.style.cssText='position:absolute;left:2%;bottom:2%;width:min(52vw,480px,48vh);height:auto;opacity:0;mix-blend-mode:screen;mask-image:radial-gradient(ellipse closest-side,#000 62%,transparent 100%);-webkit-mask-image:radial-gradient(ellipse closest-side,#000 62%,transparent 100%)';
  layer.appendChild(finale);
  var finaleRequested=false,finaleStarted=null;
  finale.onload=function(){finaleStarted=performance.now();};
  finale.onerror=function(){finaleStarted=performance.now()-4800;};
  document.body.appendChild(layer);overlay.classList.add('origami-active');
  var originalTransform=overlay.style.transform;
  // Map the original printed card triangles directly onto the folded paper faces.
  function matrix(s,d){
    var ux=s[1][0]-s[0][0],uy=s[1][1]-s[0][1],vx=s[2][0]-s[0][0],vy=s[2][1]-s[0][1],det=ux*vy-vx*uy;
    var ax=d[1][0]-d[0][0],ay=d[1][1]-d[0][1],bx=d[2][0]-d[0][0],by=d[2][1]-d[0][1];
    var a=(ax*vy-bx*uy)/det,b=(ay*vy-by*uy)/det,c=(bx*ux-ax*vx)/det,e=(by*ux-ay*vx)/det;
    return 'matrix('+[a,b,c,e,d[0][0]-a*s[0][0]-c*s[0][1],d[0][1]-b*s[0][0]-e*s[0][1]].join(',')+')';
  }
  function ease(t){t=Math.max(0,Math.min(1,t));return t*t*(3-2*t);}
  var start=performance.now(),waitingForSpace=0;
  function frame(now){
    // Hold the ascent until the full-screen star field has decoded.
    if(now-start>=3000&&!space.complete&&waitingForSpace<5000){
      waitingForSpace+=16;start+=16;requestAnimationFrame(frame);return;
    }
    var elapsed=now-start,flight=ease((elapsed-2400)/2400);
    var orbit=ease((elapsed-4400)/850);
    var floatTime=Math.max(0,elapsed-5250)/1000;
    pieces.forEach(function(piece,index){
      var fold=ease((elapsed-120-index*65)/1650);
      var destination=piece.target.map(function(p,j){
        var py=p[1];
        return [ox+p[0]*factor,oy+py*factor];
      });
      var current=piece.source.map(function(p,j){return [p[0]+(destination[j][0]-p[0])*fold,p[1]+(destination[j][1]-p[1])*fold];});
      piece.element.style.transform=matrix(piece.source,current);
      piece.element.style.filter='brightness('+(1+fold*(index%2?.25:-.08))+')';
    });
    var orbitX=window.innerWidth*.35-(rect.left+width/2);
    var orbitY=window.innerHeight*.32-(rect.top+height/2);
    bird.style.transform='translate('+(orbit*orbitX+Math.sin(floatTime)*8)+'px,'+(flight*orbitY+Math.sin(floatTime*1.4)*9)+'px) rotate('+(orbit*8+Math.sin(floatTime)*4)+'deg) scale('+(1-orbit*.16)+')';
    flame.style.opacity=elapsed>2300?String(1-orbit):'0';
    flame.style.transform='scaleY('+(1+Math.sin(elapsed/45)*.15)+')';
    space.style.opacity=String(ease((elapsed-3000)/2250));
    space.style.transform='translateY('+(-(1-flight)*window.innerHeight*.3)+'px) scale(1.6)';
    overlay.style.transform='translateY('+(flight*window.innerHeight)+'px)';
    var catArrival=ease((elapsed-5350)/1800);
    cat.style.opacity=String(catArrival);
    cat.style.transform='translate('+((1-catArrival)*window.innerWidth*.5)+'px,'+(Math.sin(floatTime)*15)+'px) rotate('+(-18+Math.sin(floatTime*.8)*12)+'deg)';
    if(reduced){bird.style.opacity='0';cat.style.transform='none';space.style.transform='none';overlay.style.transform=originalTransform;flame.style.opacity='0';}
    if(elapsed>=5350&&!finaleRequested){
      finaleRequested=true;
      finale.src='assets/rocket-study-hub.gif';
    }
    var finaleTime=finaleStarted===null?0:now-finaleStarted;
    var reveal=ease(finaleTime/650);
    finale.style.opacity=String(reveal);
    layer.style.opacity=String(1-ease((finaleTime-4800)/600));
    if((finaleStarted===null||finaleTime<5400)&&elapsed<20000){requestAnimationFrame(frame);return;}
    overlay.style.transform=originalTransform;
    if(options.onComplete)options.onComplete();
    overlay.classList.remove('origami-active');layer.remove();
  }
  requestAnimationFrame(frame);
};
