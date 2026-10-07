from PIL import Image
import os
M='deck/ppt/media/'
OUT='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 15/notes/assets/cardiac-cycle/'
os.makedirs(OUT,exist_ok=True)
F=[('image1.png','cc-wiggers.jpg',1400),
 ('image2.png','cc-phase1-atrial.jpg',1100),('image3.png','cc-phase2-ivc.jpg',1100),('image4.png','cc-phase3-rapid-ejection.jpg',1100),
 ('image6.png','cc-phase4-reduced-ejection.jpg',1100),('image8.png','cc-phase5-ivr.jpg',1100),('image9.png','cc-phase6-rapid-filling.jpg',1100),
 ('image10.png','cc-phase7-reduced-filling.jpg',1100),
 ('image11.png','cc-ms-schematic.jpg',730),('image12.png','cc-ms-tracing.jpg',730),
 ('image14.png','cc-as-schematic.jpg',730),('image15.png','cc-as-tracing.jpg',730),
 ('image17.png','cc-mr-schematic.jpg',730),('image18.png','cc-mr-tracing.jpg',730),
 ('image20.png','cc-ar-schematic.jpg',730),('image21.png','cc-ar-tracing.jpg',730)]
for src,dst,mx in F:
    im=Image.open(M+src)
    if im.mode in ('RGBA','LA','P'):
        im=im.convert('RGBA'); bg=Image.new('RGB',im.size,(255,255,255)); bg.paste(im,mask=im.split()[3]); im=bg
    else: im=im.convert('RGB')
    im.thumbnail((mx,mx*2))
    im.save(OUT+dst,'JPEG',quality=86,optimize=True,progressive=True)
    print(dst,im.size,os.path.getsize(OUT+dst)//1024,'KB')
