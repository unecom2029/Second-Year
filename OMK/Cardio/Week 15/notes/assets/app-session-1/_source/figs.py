from PIL import Image
import os
A='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 15/notes/assets/'
F={'app-session-1':[
 ('pres','image3.png','as1-ischemia-descriptors.jpg',1100),('pres','image2.png','as1-chest-pain-table.jpg',1300),
 ('pres','image4.jpeg','as1-fh-signs.jpg',1100),('pres','image11.png','as1-sihd-testing.jpg',1400),
 ('pres','image12.jpeg','as1-omt-survival.jpg',900),('pres','image13.png','as1-nstemi-ecg.jpg',1400),
 ('pres','image14.jpeg','as1-acs-pyramid.jpg',1300),('pres','image16.png','as1-type1-type2-mi.jpg',1200),
 ('pres','image17.png','as1-coronary-flow-reserve.jpg',800),('pres','image20.png','as1-nste-acs-invasive.jpg',1000),
 ('pres','image24.png','as1-mechanical-complications.jpg',900),('pres','image27.jpeg','as1-vsr-echo.jpg',900),
 ('pres','image15.jpg','as1-mi-classification.jpg',900),
 ('htn','image8.jpeg','as1-bp-methods.jpg',900),('htn','image10.png','as1-sodium-mechanism.jpg',1200),
 ('htn','image13.png','as1-bp-phenotypes.jpg',800),('htn','image18.jpeg','as1-aldosterone-principal-cell.jpg',1200),
 ('htn','image19.jpeg','as1-aldosterone-tissues.jpg',1000),('htn','image21.png','as1-low-renin-algorithm.jpg',1100),
 ('htn','image22.jpeg','as1-pa-prevalence.jpg',960),('htn','image27.png','as1-pa-management.jpg',1400),
 ('htn','image28.jpeg','as1-aldosterone-escape.jpg',1200),('htn','image29.png','as1-renin-independent-aldo.jpg',1400),
 ('htn','image6.jpeg','as1-bp-positioning.jpg',1000)],
'app-session-2':[
 ('hf','image1.jpeg','as2-hfpef-ecg.jpg',1024),('hf','image3.png','as2-psax-lvh.jpg',833),('hf','image4.png','as2-concentric-eccentric.jpg',900),
 ('hf','image5.png','as2-h2fpef.jpg',1300),('hf','image7.jpeg','as2-hfref-vs-hfpef.jpg',905),('hf','image8.jpeg','as2-nyha.jpg',1280),
 ('hf','image9.jpeg','as2-diuretic-sites.jpg',1400),('hf','image10.png','as2-sglt2i-mechanism.jpg',1300),('hf','image12.png','as2-mra-mechanisms.jpg',1100),
 ('hf','image14.png','as2-alcohol-cm.jpg',1000),('hf','image15.png','as2-cocaine-bb.jpg',1200),('hf','image16.jpeg','as2-cxr-edema.jpg',800),
 ('hf','image17.jpeg','as2-cxr-signs.jpg',640),('hf','image19.png','as2-forrester.jpg',1300),('hf','image20.png','as2-neurohormonal.jpg',1300),
 ('hf','image21.png','as2-loop-diuretic.jpg',1200),('hf','image22.png','as2-pillars-remodeling.jpg',900),('hf','image23.png','as2-pillars-hr.jpg',900),
 ('hf','image25.png','as2-shock-types.jpg',758),('hf','image26.png','as2-starling-curves.jpg',1100),('hf','image27.png','as2-adhf-cycle.jpg',1300),
 ('hf','image29.jpg','as2-hfpef-algorithm.jpg',1300),('hf','image30.jpg','as2-hfref-rapid-gdmt.jpg',1400),
 ('pad','image2.png','as2-leg-arteries.jpg',518),('pad','image3.png','as2-claudication-ddx.jpg',1299),('pad','image5.jpeg','as2-pad-prevalence.jpg',1100),
 ('pad','image6.png','as2-pad-odds-ratios.jpg',1400),('pad','image10.png','as2-pad-subsets.jpg',744),('pad','image11.png','as2-dependent-rubor.jpg',636),
 ('pad','image12.png','as2-buerger-test.jpg',542),('pad','image13.jpeg','as2-pad-symptom-sites.jpg',256),('pad','image14.png','as2-leriche-ct.jpg',429),
 ('pad','image15.png','as2-abi-method.jpg',1300),('pad','image16.png','as2-abi-cutoffs.jpg',1400),('pad','image17.png','as2-pvr-doppler.jpg',835),
 ('pad','image18.png','as2-pad-diagnostic-algorithm.jpg',868),('pad','image21.png','as2-pad-antithrombotic.jpg',1400),('pad','image20.jpeg','as2-pad-medical-therapy.jpg',750),
 ('pad','image23.jpeg','as2-exercise-mechanisms.jpg',1280),('pad','image24.png','as2-set-table.jpg',1400),('pad','image25.jpeg','as2-smoking-outcomes.jpg',1400),
 ('pad','image26.jpeg','as2-smoking-plan.jpg',942),('pad','image29.png','as2-polyvascular.jpg',1400)]}
for d,L in F.items():
    os.makedirs(A+d,exist_ok=True)
    for k,src,dst,mx in L:
        im=Image.open(f'{k}/ppt/media/{src}')
        if im.mode in ('RGBA','LA','P'):
            im=im.convert('RGBA'); bg=Image.new('RGB',im.size,'white'); bg.paste(im,mask=im.split()[3]); im=bg
        else: im=im.convert('RGB')
        im.thumbnail((mx,mx*3)); im.save(A+d+'/'+dst,'JPEG',quality=86,optimize=True,progressive=True)
    print(d,len(L))
