window.foldLoginCardIntoCrane=function(card,overlay,options){
  var rect=card.getBoundingClientRect(),width=rect.width,height=rect.height;
  var layer=document.createElement('div');
  layer.className='auth-origami-layer';layer.setAttribute('aria-hidden','true');
  var bird=document.createElement('div');
  bird.style.cssText='position:absolute;left:'+rect.left+'px;top:'+rect.top+'px;width:'+width+'px;height:'+height+'px;transform-origin:50% 50%';
  layer.appendChild(bird);
  var targets=[[[18,106],[187,165],[127,175]],[[178,163],[278,24],[247,163]],[[127,175],[185,149],[213,201]],[[185,149],[285,166],[213,201]],[[245,175],[296,77],[280,152]],[[296,77],[317,77],[280,152]],[[296,77],[317,77],[370,112]],[[213,201],[69,18],[149,184]]];
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
  document.body.appendChild(layer);overlay.classList.add('origami-active');
  // Map the original printed card triangles directly onto the folded paper faces.
  function matrix(s,d){
    var ux=s[1][0]-s[0][0],uy=s[1][1]-s[0][1],vx=s[2][0]-s[0][0],vy=s[2][1]-s[0][1],det=ux*vy-vx*uy;
    var ax=d[1][0]-d[0][0],ay=d[1][1]-d[0][1],bx=d[2][0]-d[0][0],by=d[2][1]-d[0][1];
    var a=(ax*vy-bx*uy)/det,b=(ay*vy-by*uy)/det,c=(bx*ux-ax*vx)/det,e=(by*ux-ay*vx)/det;
    return 'matrix('+[a,b,c,e,d[0][0]-a*s[0][0]-c*s[0][1],d[0][1]-b*s[0][0]-e*s[0][1]].join(',')+')';
  }
  function ease(t){t=Math.max(0,Math.min(1,t));return t*t*(3-2*t);}
  var start=performance.now();
  function frame(now){
    var elapsed=now-start,flight=ease((elapsed-2850)/1350);
    pieces.forEach(function(piece,index){
      var fold=ease((elapsed-120-index*65)/1650);
      var flap=Math.sin(Math.max(0,elapsed-2300)/180)*.28*ease((elapsed-2300)/350);
      var destination=piece.target.map(function(p,j){
        var py=p[1];
        if((index===1||index===7)&&j===1)py+=flap*(155-py);
        return [ox+p[0]*factor,oy+py*factor];
      });
      var current=piece.source.map(function(p,j){return [p[0]+(destination[j][0]-p[0])*fold,p[1]+(destination[j][1]-p[1])*fold];});
      piece.element.style.transform=matrix(piece.source,current);
      piece.element.style.filter='brightness('+(1+fold*(index%2?.25:-.08))+')';
    });
    bird.style.transform='translate('+flight*window.innerWidth+'px,'+(-flight*window.innerHeight*.75)+'px) rotate('+(-flight*18)+'deg) scale('+(1-flight*.5)+')';
    if(elapsed<4200){requestAnimationFrame(frame);return;}
    if(options.onComplete)options.onComplete();
    overlay.classList.remove('origami-active');layer.remove();
  }
  requestAnimationFrame(frame);
};
