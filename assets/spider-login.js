(function(){
  var active=false;
  window.triggerSpiderLoginSwing=function(options){
    options=options||{};
    var card=document.getElementById('authLoginCard');
    if(active||!card)return;
    active=true;
    var rect=card.getBoundingClientRect(),w=window.innerWidth,h=window.innerHeight;
    var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var layer=document.createElement('div');
    layer.className='spider-login-swing';
    layer.setAttribute('aria-hidden','true');
    layer.style.cssText='position:fixed;inset:0;z-index:13100;overflow:hidden;pointer-events:none';
    var city=document.createElement('img');
    city.src='assets/spider-city.png';city.alt='';
    city.style.cssText='position:absolute;left:0;bottom:0;width:100%;height:100%;max-width:none;object-fit:fill;transform:translateY(100%);clip-path:polygon(0 40%,3.5% 40%,3.5% 30%,5% 30%,5% 25%,6% 25%,6% 23%,8.5% 23%,8.5% 25%,10% 25%,10% 30%,11% 30%,11% 39%,14% 39%,14% 34%,18% 34%,18% 40%,20% 40%,20% 36%,23% 36%,23% 32%,24.5% 32%,24.5% 18.5%,33.5% 18.5%,33.5% 38%,37% 38%,37% 36%,40.7% 36%,40.7% 21%,45.5% 21%,45.5% 33%,48% 33%,48% 28%,53.5% 28%,53.5% 37%,56% 37%,56% 34%,57.3% 34%,57.3% 24%,58.5% 21%,59.2% 13%,59.5% 21%,61% 24%,61% 25%,65.5% 25%,65.5% 27%,67.2% 27%,67.2% 22%,69% 17%,69.7% 2%,70% 17%,72.5% 22%,72.5% 27%,74% 27%,74% 38%,79% 38%,79% 39%,83.4% 39%,83.4% 23%,85% 23%,85% 21%,87% 21%,87% 18%,88.5% 18%,88.7% 13%,89% 18%,90% 18%,90% 23%,90.4% 23%,90.4% 40%,94.3% 40%,94.3% 34%,95.8% 32%,100% 32%,100% 100%,0 100%)';
    layer.appendChild(city);
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
      // Raise the skyline after the card exits, then play Spider-Man in front.
      var rise=smooth((elapsed-1200)/1100);
      city.style.transform='translateY('+((1-rise)*100)+'%)';
      if(!reduced&&elapsed>=2350&&!requested){
        requested=true;hero.src='assets/spider-login-animated.webp?play='+Date.now();
      }
      var mediaElapsed=mediaStart===null?0:now-mediaStart;
      hero.style.opacity=mediaStart===null?'0':String(Math.min(1,Math.max(0,(1480-mediaElapsed)/120)));
      line(grip,w*.85,-25,rect.right+dx,rect.top+dy);
      grip.style.opacity=elapsed<1200?'1':'0';
      card.style.transform='translate('+dx+'px,'+dy+'px) rotate('+(-55*pull)+'deg)';
      if(reduced){city.style.display='none';svg.style.opacity='0';hero.style.opacity='0';card.style.transform=originalTransform;card.style.opacity=String(1-p);}
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
