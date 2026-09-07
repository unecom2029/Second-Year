(function(){
  var active=false;
  window.triggerSpiderLoginSwing=function(options){
    var card=document.getElementById('authLoginCard');
    if(active||!card)return;
    active=true;
    var rect=card.getBoundingClientRect(),w=window.innerWidth,h=window.innerHeight;
    var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var layer=document.createElement('div');
    layer.className='spider-login-swing';
    layer.setAttribute('aria-hidden','true');
    layer.style.cssText='position:fixed;inset:0;z-index:13100;overflow:hidden;pointer-events:none';
    var ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');
    svg.setAttribute('width','100%');svg.setAttribute('height','100%');
    svg.style.cssText='position:absolute;inset:0;overflow:visible';
    var grip=document.createElementNS(ns,'line');
    grip.setAttribute('stroke','#f1f7ff');grip.setAttribute('stroke-width','2');svg.appendChild(grip);
    layer.appendChild(svg);
    var hero=document.createElement('img');
    hero.alt='';
    hero.style.cssText='position:absolute;inset:0;width:100vw;height:100vh;max-width:none;object-fit:cover;object-position:center;opacity:0';
    layer.appendChild(hero);document.body.appendChild(layer);
    var originalTransform=card.style.transform,originalOpacity=card.style.opacity;
    var originalTransition=card.style.transition,originalOrigin=card.style.transformOrigin;
    card.style.transition='none';
    card.style.transformOrigin='100% 0';
    var start=performance.now(),mediaStart=null,requested=false,failed=false;
    hero.onload=function(){mediaStart=performance.now();};
    hero.onerror=function(){failed=true;};
    function smooth(v){v=Math.max(0,Math.min(1,v));return v*v*(3-2*v);}
    function line(el,x1,y1,x2,y2){el.setAttribute('x1',x1);el.setAttribute('y1',y1);el.setAttribute('x2',x2);el.setAttribute('y2',y2);}
    function tick(now){
      var elapsed=now-start;
      var p=Math.min(1,elapsed/1000),pull=smooth(elapsed/1200);
      var dx=pull*(w+rect.width),dy=-pull*h*.7;
      // Start the supplied clip only after the card has cleared the screen.
      if(!reduced&&elapsed>=1200&&!requested){
        requested=true;hero.src='assets/spider-login-animated.webp?play='+Date.now();
      }
      var mediaElapsed=mediaStart===null?0:now-mediaStart;
      hero.style.opacity=mediaStart===null?'0':String(Math.min(1,Math.max(0,(1480-mediaElapsed)/120)));
      line(grip,w*.85,-25,rect.right+dx,rect.top+dy);
      grip.style.opacity=elapsed<1200?'1':'0';
      card.style.transform='translate('+dx+'px,'+dy+'px) rotate('+(-55*pull)+'deg)';
      if(reduced){svg.style.opacity='0';hero.style.opacity='0';card.style.transform=originalTransform;card.style.opacity=String(1-p);}
      var complete=reduced?p===1:failed||mediaStart!==null&&mediaElapsed>=1480||elapsed>=6000;
      if(!complete){requestAnimationFrame(tick);return;}
      if(typeof options.onComplete==='function')options.onComplete();
      layer.remove();
      card.style.transform=originalTransform;card.style.opacity=originalOpacity;
      card.style.transition=originalTransition;
      card.style.transformOrigin=originalOrigin;
      if(!options.onComplete)card.animate([{opacity:0},{opacity:1}],{duration:250});
      active=false;
    }
    requestAnimationFrame(tick);
  };
})();
