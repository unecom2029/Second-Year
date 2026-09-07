(function(){
  var active=false;
  window.triggerSpiderLoginSwing=function(options){
    var card=document.getElementById('authLoginCard');
    if(active||!card)return;
    active=true;
    var rect=card.getBoundingClientRect(),w=window.innerWidth,h=window.innerHeight;
    var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var size=Math.min(112,Math.max(66,w*.095),h*.18);
    var layer=document.createElement('div');
    layer.className='spider-login-swing';
    layer.setAttribute('aria-hidden','true');
    layer.style.cssText='position:fixed;inset:0;z-index:13100;overflow:hidden;pointer-events:none';
    var ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');
    svg.setAttribute('width','100%');svg.setAttribute('height','100%');
    svg.style.cssText='position:absolute;inset:0;overflow:visible';
    var tether=document.createElementNS(ns,'line'),grip=document.createElementNS(ns,'line');
    [tether,grip].forEach(function(line){line.setAttribute('stroke','#f1f7ff');line.setAttribute('stroke-width','2');line.setAttribute('stroke-linecap','round');svg.appendChild(line);});
    layer.appendChild(svg);
    var hero=document.createElement('img');
    hero.src='assets/google-spiderman-sprite.png';hero.alt='';
    hero.style.cssText='position:absolute;left:0;top:0;width:'+size+'px;max-width:none;height:auto;transform-origin:46% 2%;filter:drop-shadow(0 8px 10px #0003)';
    layer.appendChild(hero);document.body.appendChild(layer);
    var originalTransform=card.style.transform,originalOpacity=card.style.opacity;
    var originalTransition=card.style.transition,originalOrigin=card.style.transformOrigin;
    card.style.transition='none';
    card.style.transformOrigin='100% 0';
    var start=performance.now(),duration=reduced?1000:4400;
    function smooth(v){v=Math.max(0,Math.min(1,v));return v*v*(3-2*v);}
    function line(el,x1,y1,x2,y2){el.setAttribute('x1',x1);el.setAttribute('y1',y1);el.setAttribute('x2',x2);el.setAttribute('y2',y2);}
    function tick(now){
      var p=Math.min(1,(now-start)/duration);
      // Clear the card before the swing begins, then bring the mask toward the viewer.
      var pull=smooth(p/.3),approach=smooth((p-.32)/.34),closeup=smooth((p-.68)/.27);
      var dx=pull*(w+rect.width),dy=-pull*h*.7;
      var zoom=1+closeup*(Math.min(h/(size*.65),w/(size*.65))-1);
      var swingX=-size+(w*.5+size)*approach;
      var swingY=h*.16+Math.sin(Math.PI*approach)*h*.15;
      var x=swingX*(1-closeup)+(w*.5-size*.27*zoom)*closeup;
      var y=swingY*(1-closeup)+(h*.4-size*.74*zoom)*closeup;
      var angle=(-28+28*approach)*(1-closeup);
      hero.style.opacity=p>=.32?'1':'0';
      hero.style.transform='translate('+(x-size*.46)+'px,'+y+'px) rotate('+angle+'deg) scale('+zoom+')';
      var handY=y+size*(352/135)*.02;
      line(tether,w*.58,-25,x,handY);
      tether.style.opacity=p>=.32?String(1-closeup):'0';
      line(grip,w*.85,-25,rect.right+dx,rect.top+dy);
      grip.style.opacity=p<.3?'1':'0';
      card.style.transform='translate('+dx+'px,'+dy+'px) rotate('+(-55*pull)+'deg)';
      if(reduced){svg.style.opacity='0';hero.style.opacity='0';card.style.transform=originalTransform;card.style.opacity=String(1-p);}
      if(p<1){requestAnimationFrame(tick);return;}
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
