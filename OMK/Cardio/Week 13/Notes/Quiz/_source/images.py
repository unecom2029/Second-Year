import base64, io, json
from PIL import Image
N='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 13/Notes/assets/'
R='/Users/jeeval/Board Study/figures/Robbins/The Heart - '
A='/Users/jeeval/Board Study/figures/amboss/'
U='/Users/jeeval/Board Study/figures/Uworld images/'
import os
L=os.path.join(os.path.dirname(os.path.abspath(__file__)),'ecglib')+'/'
_GRID=None
def _ongrid(p):
    global _GRID
    if _GRID is None: _GRID=Image.open(L+'grid.gif').convert('RGBA')
    im=Image.open(p).convert('RGBA'); bg=Image.new('RGBA',im.size)
    for x in range(0,im.width,_GRID.width):
        for y in range(0,im.height,_GRID.height): bg.paste(_GRID,(x,y))
    bg.alpha_composite(im); return bg.convert('RGB')
# key: (path, crop box as fractions (l,t,r,b) or None, source credit)
IMGS={
 # cardiac pathology
 'hcm':(N+'cardiac/c-hcm.jpg',None,'Gardner lecture · slide 77'),
 'cband':(R+'aaa4518562a17dc6.png',None,'Robbins & Cotran Atlas of Pathology'),
 'mi2d':(R+'209f3f3f846ec58b.png',None,'Robbins & Cotran Atlas of Pathology'),
 'hemoperi':(N+'cardiac/c-hemopericardium.jpg',None,'Robbins & Cotran Atlas of Pathology'),
 'boot':(N+'cardiac/c-boot.jpg',None,'AMBOSS'),
 'aschoff':(N+'cardiac/c-aschoff.jpg',None,'AMBOSS'),
 'ms':(R+'34bed6ae91691964.png',None,'Robbins & Cotran Atlas of Pathology'),
 'amyloid':(R+'f799a2a4632b32ec.png',None,'Robbins & Cotran Atlas of Pathology'),
 'chagas':(R+'8a589fbf2ecbeae2.png',None,'Robbins & Cotran Atlas of Pathology'),
 'myxoma':(R+'d3dcbee0471ee054.png',None,'Robbins & Cotran Atlas of Pathology'),
 'fibrinous':(A+'Fibrinous pericarditis in uremia.png',None,'AMBOSS'),
 'nutmeg':(N+'cardiac/c-nutmeg.jpg',None,'Gardner lecture · slide 55'),
 'dcm':(R+'ba942720015dfc04.png',None,'Robbins & Cotran Atlas of Pathology'),
 'lvh':(R+'2241e511f42c82f9.png',None,'Robbins & Cotran Atlas of Pathology'),
 'lqt':(N+'cardiac/c-long-qt.jpg',None,'AMBOSS'),
 'wpw':(A+'Wolff-Parkinson-White syndrome.png',None,'AMBOSS'),
 'pfo':(R+'3efcf0aa8ff8c0a0.png',None,'Robbins & Cotran Atlas of Pathology'),
 'inferior':(A+'Acute inferior STEMI.png',None,'AMBOSS'),
 # endocarditis / myocarditis / pericarditis
 'janeway':(N+'endocarditis/e-janeway.jpg',None,'Infectious Disease lecture deck'),
 'roth':(N+'endocarditis/e-roth.jpg',(0,0,1,0.955),'Case Studies in Infectious Disease (Garland Science)'),
 'conj':(N+'endocarditis/e-petechiae-conj.jpg',None,'Infectious Disease lecture deck'),
 'aorticperf':(N+'endocarditis/e-aortic-perforation.jpg',(0,0,1,0.865),'Infectious Disease lecture deck'),
 'candida':(N+'endocarditis/e-candida-veg.jpg',(0.17,0.09,1,1),'Infectious Disease lecture deck'),
 'nbte':(N+'endocarditis/e-nbte.jpg',None,'Cardiovascular Pathophysiology for Pre-Clinical Students'),
 'pet':(N+'endocarditis/e-pet.jpg',(0,0,1,0.935),'Infectious Disease lecture deck'),
 'echoveg':(R+'fc2da25c4f67fec4.png',None,'Robbins & Cotran Atlas of Pathology'),
 'tte':(N+'endocarditis/e-tte.jpg',None,'Infectious Disease lecture deck'),
 'aorticveg':(N+'endocarditis/e-aortic-veg.jpg',None,'Infectious Disease lecture deck'),
 'lyme':(N+'endocarditis/e-lyme-block.jpg',None,'AMBOSS'),
 'lympho':(R+'3cec8d9219f80f02.png',None,'Robbins & Cotran Atlas of Pathology'),
 'periecg':(N+'endocarditis/e-pericarditis-ecg.jpg',None,'AMBOSS'),
 'waterbottle':(N+'endocarditis/e-water-bottle.jpg',None,'AMBOSS'),
 'tbperi':(N+'endocarditis/e-tb-pericarditis.jpg',None,'Robbins & Cotran Atlas of Pathology'),
 'myoecg':(N+'endocarditis/e-myo-ecg.jpg',None,'AMBOSS'),
 'palate':(N+'endocarditis/e-petechiae-palate.jpg',None,'Infectious Disease lecture deck'),
 'mitralveg':(N+'endocarditis/e-mitral-veg.jpg',None,'Infectious Disease lecture deck'),
 'eisen':(R+'1e2ef88518bc5b63.png',None,'Robbins & Cotran Atlas of Pathology'),
 'pda':(R+'1d26cc18d59fd089.png',None,'Robbins & Cotran Atlas of Pathology'),
 'cihd':(R+'fa09aa8fdfde09b1.png',None,'Robbins & Cotran Atlas of Pathology'),
 'iron':(R+'e58d6a0bcceb8eae.png',None,'Robbins & Cotran Atlas of Pathology'),
 'libman':(N+'cardiac/c-libman.jpg',None,'Robbins & Cotran Atlas of Pathology'),
 'brugada':(A+'Brugada pattern.png',None,'AMBOSS'),
 'osler':(N+'cardiac/c-osler.jpg',None,'Gardner lecture · slide 74'),
 'toe':(N+'endocarditis/e-toe.jpg',None,'Infectious Disease lecture deck'),
 'giantcell':(R+'f6913308a30ab43f.png',None,'Robbins & Cotran Atlas of Pathology'),
 'asperg':(N+'endocarditis/e-aspergillus-veg.jpg',None,'AMBOSS'),
 'clubbing':(N+'endocarditis/e-clubbing.jpg',None,'Infectious Disease lecture deck'),
 # pharm
 'Uangio':(U+'COMLEX 1 (Step1 + OMT1) - Allergy & Immunology/08_hereditary_angioedema.jpg',None,'UWorld'),
 'Uvap':(U+'COMLEX 1 (Step1 + OMT1) - Cardiovascular System/112_ventricular_action_potential_phases_lettered.jpg',None,'UWorld'),
 'Uepi':(U+'COMLEX 1 (Step1 + OMT1) - Cardiovascular System/118_epinephrine_group_epinephrine_drug_a_group.jpg',None,'UWorld'),
 'Uiso':(U+'COMLEX 1 (Step1 + OMT1) - Cardiovascular System/122_question_288_isoproterenol.jpg',None,'UWorld'),
 'Upace':(U+'COMLEX 1 (Step1 + OMT1) - Cardiovascular System/146_cardiac_pacemaker_action_potential.jpg',(0,0.075,1,0.69),'UWorld'),
 'Uautoreg':(U+'COMLEX 1 (Step1 + OMT1) - Cardiovascular System/084_autoregulation_of_blood_flow_in_chronic_hypertension.png',None,'UWorld'),
 'Agout':(A+'Gouty tophi.png',None,'AMBOSS'),
 'Aedema':(A+'Pitting edema of lower leg.png',None,'AMBOSS'),
 'Apeakt':(A+'Peaked T waves in hyperkalemia.png',None,'AMBOSS'),
 'Aretino':(A+'Grade IV hypertensive retinopathy.png',None,'AMBOSS'),
 'Aadrenal':(A+'Adrenal adenoma.png',None,'AMBOSS'),
 'Apupil':(A+'Miosis and mydriasis.png',None,'AMBOSS'),
 'Anetest':(A+'Examples of direct sympathomimetic drugs.png',None,'AMBOSS'),
 'Ahypok':(A+'Flat T waves in hypokalemia.png',None,'AMBOSS'),
 'Arenal':(A+'Renal artery stenosis.png',None,'AMBOSS'),
 'Apheo':(A+'Pheochromocytoma.png',None,'AMBOSS'),
 # ECG basics
 'kafib':(N+'ekg/k-afib.jpg',None,'AMBOSS'),
 'kflutter':(N+'ekg/k-flutter.jpg',None,'AMBOSS'),
 'kste':(N+'ekg/k-ste-types.jpg',None,'AMBOSS'),
 'kqwave':(N+'ekg/k-q-wave.jpg',None,'AMBOSS'),
 'Laflbbb':(L+'img_af_lbbb.gif',None,'ecglibrary.com'),
 'klvh':(N+'ekg/k-case-lvh.jpg',None,'Qazi lecture · class ECG'),
 'ksinarr':(N+'ekg/k-sinus-arrhythmia.jpg',None,'AMBOSS'),
 'krvh':(N+'ekg/k-rvh.jpg',None,'AMBOSS'),
 'k2to1':(N+'ekg/k-case-2to1.jpg',None,'Qazi lecture · class ECG'),
 'klbbb':(N+'ekg/k-case-lbbb.jpg',None,'Qazi lecture · class ECG'),
 'krbbb':(N+'ekg/k-case-rbbb.jpg',None,'Qazi lecture · class ECG'),
 'kchbstemi':(N+'ekg/k-case-chb-stemi.jpg',None,'Qazi lecture · class ECG'),
 'kmat':(N+'ekg/k-mat.jpg',(0,0.035,1,1),'AMBOSS'),
 'knstemi':(N+'ekg/k-nstemi.jpg',None,'AMBOSS'),
 'klad':(N+'ekg/k-lad-ecg.jpg',None,'AMBOSS'),
 'khyper':(N+'ekg/k-hyperacute.jpg',None,'Cardiovascular Pathophysiology for Pre-Clinical Students'),
 'kmob2':(N+'ekg/k-mobitz2.jpg',(0,0,1,0.86),'AMBOSS'),
 'Lchb':(L+'img_chb4.gif',None,'ecglibrary.com'),
 'Lfl21':(L+'img_af2_1.gif',None,'ecglibrary.com'),
 'Lafrvr':(L+'img_af_fast2.gif',None,'ecglibrary.com'),
 'Ltrifas':(L+'img_trifas2.gif',(0,0.27,1,0.95),'ecglibrary.com'),
 'Llvh':(L+'img_lvhlah.gif',None,'ecglibrary.com'),
 'Lrah':(L+'img_rah.gif',None,'ecglibrary.com'),
 'Llqt':(L+'img_l_qt.gif',None,'ecglibrary.com'),
 'Ltdp':(L+'img_tdp.gif',None,'ecglibrary.com'),
 'Lhighk':(L+'img_highk.gif',None,'ecglibrary.com'),
 'Lami':(L+'img_ami.gif',None,'ecglibrary.com'),
 'Lpost':(L+'img_postlat.gif',None,'ecglibrary.com'),
 'Loldmi':(L+'img_oldmi.gif',None,'ecglibrary.com'),
 'Lhypok':(L+'img_hypok.gif',None,'ecglibrary.com'),
 'Lstach':(L+'img_stach.gif',None,'ecglibrary.com'),
 'Lwpw':(L+'img_wpw.gif',(0,0.28,1,1),'ecglibrary.com'),
}
def load(key, maxw=1100):
    p,crop,_=IMGS[key]
    im=_ongrid(p) if p.endswith('.gif') else Image.open(p).convert('RGB')
    if crop:
        w,h=im.size; l,t,r,b=crop
        im=im.crop((int(l*w),int(t*h),int(r*w),int(b*h)))
    if key=='osler':
        im=im.resize((im.width*2,im.height*2),Image.LANCZOS)
    if im.width>maxw:
        im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    return im
def data_uri(key):
    im=load(key); buf=io.BytesIO(); im.save(buf,'JPEG',quality=82,optimize=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(buf.getvalue()).decode()
if __name__=='__main__':
    import sys
    keys=sys.argv[2:]; T=420; cols=3; rows=(len(keys)+2)//3
    from PIL import ImageDraw
    s=Image.new('RGB',(cols*T,rows*(T+20)),'white'); d=ImageDraw.Draw(s)
    for i,k in enumerate(keys):
        im=load(k); im.thumbnail((T-6,T-6)); x=(i%3)*T; y=(i//3)*(T+20)
        s.paste(im,(x+3,y+20)); d.text((x+4,y+4),k,fill='red')
    s.save(sys.argv[1],quality=80)
