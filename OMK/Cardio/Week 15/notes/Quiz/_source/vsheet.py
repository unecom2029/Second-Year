import sys
from PIL import Image, ImageDraw
from images import load
out=sys.argv[1]; keys=sys.argv[2:]; W=620; cols=2
ims=[load(k,1400) for k in keys]
for im in ims: im.thumbnail((W-6,2000))
rows=[ims[i:i+cols] for i in range(0,len(ims),cols)]
H=sum(max(i.height for i in r)+22 for r in rows)
s=Image.new('RGB',(W*cols,H),'white'); d=ImageDraw.Draw(s); y=0; n=0
for r in rows:
    for j,im in enumerate(r):
        s.paste(im,(j*W+3,y+20)); d.text((j*W+4,y+4),keys[n],fill='red'); n+=1
    y+=max(i.height for i in r)+22
s.save(out,quality=88)
