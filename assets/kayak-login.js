/* Wave geometry and paddler adapted from the supplied Gentle Waves scene. */
(function(){
  var active=false;
  window.triggerKayakLoginEasterEgg=function(options){
    options=options||{};
    if(active)return;
    var overlay=document.getElementById('authOverlay');
    if(!overlay||!document.body.classList.contains('auth-locked')){
      if(options.onComplete)options.onComplete();
      return;
    }
    active=true;
    var reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var layer=document.createElement('div');
    layer.className='kayak-login-layer';
    layer.setAttribute('aria-hidden','true');
    layer.style.cssText='position:fixed;inset:0;z-index:14000;overflow:hidden;pointer-events:none;background:#edf5f7;isolation:isolate;transform:translateY(100%)';
    var canvas=document.createElement('canvas');
    canvas.style.cssText='position:absolute;inset:0;width:100%;height:100%';
    layer.appendChild(canvas);
    var logo=document.createElement('img');
    logo.alt='';
    // Multiplication removes the light GIF matte while preserving its animated frames.
    logo.style.cssText='position:absolute;left:50%;top:12%;transform:translateX(-50%);width:min(900px,92%);height:40%;object-fit:contain;filter:brightness(1.08);mix-blend-mode:multiply;opacity:0';
    layer.appendChild(logo);
    document.body.appendChild(layer);
    var ctx=canvas.getContext('2d');
    var slide=overlay.animate(reduced?[{opacity:1},{opacity:0}]:[{transform:'translateY(0)'},{transform:'translateY(-100vh)'}],{duration:1100,easing:'cubic-bezier(.65,0,.35,1)',fill:'forwards'});
    var rise=layer.animate(reduced?[{transform:'none',opacity:0},{transform:'none',opacity:1}]:[{transform:'translateY(100%)'},{transform:'translateY(0)'}],{duration:1100,easing:'cubic-bezier(.65,0,.35,1)',fill:'forwards'});
    var colors=['#e2f0f6','#c6e1ec','#a2cedf','#7bb9d2','#56a4c3','#3690b5','#227ba0','#196987','#14566f','#10465a','#0c3747','#082b37','#06222c'];
    var started=performance.now(),raf,finished=false,logoStarted=false;
    var glideStartsAt=1.1,glideDuration=6.2;
    var settleAt=glideStartsAt+glideDuration,logoAt=settleAt+1;
    function draw(now){
      if(finished)return;
      var t=(now-started)/1000,w=layer.clientWidth,h=layer.clientHeight;
      var dpr=Math.min(window.devicePixelRatio||1,2);
      if(canvas.width!==Math.round(w*dpr)||canvas.height!==Math.round(h*dpr)){
        canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);
      }
      ctx.setTransform(dpr,0,0,dpr,0,0);
      ctx.fillStyle='#edf5f7';ctx.fillRect(0,0,w,h);
      var motion=reduced?0:t;
      var arrival=Math.min(1,Math.max(0,(t-glideStartsAt)/glideDuration));
      var glide=arrival<.2
        ? 3.125*arrival*arrival
        : arrival>.8
          ? 1-3.125*(1-arrival)*(1-arrival)
          : 1.25*arrival-.125;
      var targetX=w*.54;
      function wave(x,i){
        var f=i/12,wl=Math.max(180,w*(620-f*300)/1920),amp=11*(.4+f*1.3);
        var phase=(i%2?-2:1)*2*Math.PI*motion/22;
        var ripple=amp*Math.sin(x/wl*2*Math.PI+phase)+amp*.22*Math.sin(x/(wl*.47)*2*Math.PI-phase*1.3);
        if(i>=7&&i<=9){
          var calmDistance=(x-targetX)/(w*.17);
          ripple*=1-glide*.78*Math.exp(-calmDistance*calmDistance);
        }
        return h*.12+f*h*.85+ripple;
      }
      var scale=Math.max(1.25,Math.min(2.6,w/420));
      var x=-170+(targetX+170)*glide;
      var y=wave(x,8)-9;
      for(var i=0;i<13;i++){
        ctx.beginPath();ctx.moveTo(0,wave(0,i));
        for(var px=6;px<w+6;px+=6)ctx.lineTo(px,wave(px,i));
        ctx.lineTo(w,h);ctx.lineTo(0,h);ctx.closePath();ctx.fillStyle=colors[i];ctx.fill();
        if(i===8){
          ctx.save();ctx.translate(x,y);
          ctx.rotate(Math.atan((wave(x+6,i)-wave(x-6,i))/12)*(.7-.58*glide));ctx.scale(scale,scale);
          ctx.fillStyle='#ec3013';ctx.beginPath();ctx.moveTo(-58,0);ctx.bezierCurveTo(-40,-11,40,-11,58,0);ctx.bezierCurveTo(40,9,-40,9,-58,0);ctx.fill();
          var a=.4+.26*Math.sin(motion*2*Math.PI*.45),dx=Math.cos(a)*46,dy=Math.sin(a)*46*.55;
          ctx.strokeStyle='#201e1d';ctx.fillStyle='#201e1d';ctx.lineWidth=3.5;ctx.lineCap='round';
          ctx.beginPath();ctx.moveTo(-dx,-5.4-dy);ctx.lineTo(dx,-5.4+dy);ctx.stroke();
          [[-dx,-5.4-dy],[dx,-5.4+dy],[0,-30]].forEach(function(p,j){ctx.beginPath();ctx.arc(p[0],p[1],j===2?7:6,0,Math.PI*2);ctx.fill();});
          ctx.fillRect(-7,-24,14,16);ctx.restore();
        }
      }
      // The logo begins after the kayak has rested in the calm water for one second.
      if(t>=logoAt&&!logoStarted){
        logoStarted=true;logo.src='assets/kayak-study-hub.gif';
        logo.animate([{opacity:0},{opacity:1}],{duration:350,fill:'forwards'});
      }
      raf=requestAnimationFrame(draw);
    }
    raf=requestAnimationFrame(draw);
    window.setTimeout(function(){
      slide.cancel();
      if(options.onComplete)options.onComplete();
      layer.animate([{opacity:1},{opacity:0}],{duration:650,fill:'forwards'});
      window.setTimeout(function(){
        finished=true;cancelAnimationFrame(raf);layer.remove();slide.cancel();rise.cancel();active=false;
      },660);
    },11900);
  };
})();
