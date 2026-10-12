"""Image registry for the Cardio summative exam.

Each key maps to a dict:
  p       source path
  crop    (l, t, r, b) as fractions, applied AFTER masks and labels
  credit  neutral source credit shown in the caption (never names the answer)
  masks   list of (l, t, r, b[, colour]) fractions; colour 'auto' samples the pixel just outside the box
  labels  list of (x, y, text[, size_frac]) centred at fractions of the ORIGINAL image; drawn in a white disc
  up      minimum width in px (small sources are upscaled so they don't show as thumbnails)

No UWorld images (Jeeval's rule for the summative).
"""
import base64, io, os
from PIL import Image, ImageDraw, ImageFont

HOME = os.path.expanduser('~')
AM = HOME + '/Board Study/figures/amboss/'
RB = HOME + '/Board Study/figures/Robbins/'
SA = HOME + '/Documents/GitHub/Second-Year/OMK/Cardio/summative/assets/'
W14 = HOME + '/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/assets/'
W15 = HOME + '/Documents/GitHub/Second-Year/OMK/Cardio/Week 15/notes/assets/'
FONT = '/System/Library/Fonts/Helvetica.ttc'
L = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ecglib') + '/'   # ecglibrary.com tracings (transparent GIFs)
E1 = HOME + '/Documents/GitHub/Second-Year/OMK/Cardio/Week 13/Notes/assets/ekg/'
E2 = HOME + '/Documents/GitHub/Second-Year/OMK/Cardio/Week 14/notes/assets/ekg-2/'
CP = HOME + '/Board Study/figures/Cardio/Cardiovascular pathophys/'
_GRID = None
def _ongrid(p):
    # ecglibrary GIFs are transparent: draw them onto the site's own 30-px grid tile
    global _GRID
    if _GRID is None: _GRID = Image.open(L + 'grid.gif').convert('RGBA')
    im = Image.open(p).convert('RGBA'); bg = Image.new('RGBA', im.size)
    for x in range(0, im.width, _GRID.width):
        for y in range(0, im.height, _GRID.height): bg.paste(_GRID, (x, y))
    bg.alpha_composite(im); return bg.convert('RGB')

def phono_click(x):   # mask an arrow + label above a phonocardiogram spike, centred at x
    return (x - 0.065, 0.385, x + 0.065, 0.515, 'auto')

IMGS = {
 # ---------- Part A: the normal heart ----------
 'wiggers': dict(p=SA+'cc-wiggers.jpg', credit='Qazi lecture',
    masks=[(0.10,0.0,0.66,0.24,'white'), (0.145,0.25,0.23,0.30,'white'), (0.395,0.329,0.472,0.38,'white'),
           (0.145,0.405,0.23,0.46,'white'), (0.383,0.40,0.468,0.452,'white')],
    labels=[(0.205,0.53,'1',0.03), (0.215,0.33,'2',0.03), (0.375,0.29,'3',0.03), (0.40,0.53,'4',0.03)],
    crop=(0.0,0.19,1.0,0.97)),
 'jvp': dict(p=AM+'Jugular venous pressure waveform.jpg', credit='AMBOSS', crop=(0,0,1,0.78)),
 'pvcycle': dict(p=AM+'Cardiac cycle on the pressure-volume loop.jpg', credit='AMBOSS',
    masks=[(0.468,0.535,0.555,0.59,'auto'), (0.664,0.713,0.778,0.765,'auto'), (0.221,0.721,0.331,0.776,'auto'),
           (0.44,0.86,0.62,0.896,'auto'), (0.748,0.549,0.91,0.574,'auto'), (0.79,0.726,0.965,0.754,'auto')],
    crop=(0.0,0.40,0.80,1.0)),
 'pvAS': dict(p=AM+'Pressure-volume loop in aortic stenosis.jpg', credit='AMBOSS', masks=[(0.66,0.33,0.875,0.44,'white')]),
 'pvMR': dict(p=AM+'Pressure-volume loop in mitral regurgitation.jpg', credit='AMBOSS', masks=[(0.62,0.24,0.97,0.38,'white')]),
 'pvAR': dict(p=AM+'Changes to pressure-volume loop in aortic regurgitation.jpg', credit='AMBOSS'),
 'pvSysDia': dict(p=AM+'Pressure-volume loops of the left ventricle in systolic and diastolic dysfunction.jpg', credit='AMBOSS',
    masks=[(0.235,0.10,0.325,0.15,'white'), (0.155,0.27,0.287,0.36,'white'), (0.735,0.27,0.875,0.36,'white')],
    labels=[(0.23,0.315,'1'), (0.28,0.125,'2'), (0.80,0.315,'3')]),
 'sarcEM': dict(p=W14+'physiology/p-sarcomere-em.jpg', credit='Morganelli lecture'),
 'troponin': dict(p=SA+'p-troponin.jpg', credit='Morganelli lecture'),
 'splitPhys': dict(p=AM+'Physiological split of S2.jpg', credit='AMBOSS'),
 'splitWide': dict(p=AM+'Wide split of S2.jpg', credit='AMBOSS'),
 'splitFixed': dict(p=AM+'Fixed split of S2.jpg', credit='AMBOSS'),
 'splitPara': dict(p=AM+'Paradoxical (reversed) split of S2.jpg', credit='AMBOSS'),
 'phonoMS': dict(p=AM+'Heart murmur in mitral stenosis.jpg', credit='AMBOSS', masks=[(0.296,0.415,0.33,0.529,'auto'), (0.688,0.415,0.724,0.529,'auto')]),
 'phonoMVP': dict(p=AM+'Heart murmur in mitral valve prolapse.jpg', credit='AMBOSS', masks=[(0.16,0.38,0.265,0.528,'auto'), (0.555,0.38,0.66,0.528,'auto')]),
 'phonoAS': dict(p=AM+'Heart murmur in aortic and pulmonary stenosis.jpg', credit='AMBOSS', masks=[(0.164,0.41,0.258,0.528,'auto'), (0.561,0.41,0.652,0.528,'auto'), (0.148,0.405,0.166,0.452,'auto'), (0.543,0.405,0.563,0.452,'auto')]),
 'phonoAS_lab': dict(p=AM+'Heart murmur in aortic and pulmonary stenosis.jpg', credit='AMBOSS'),
 'phonoAR': dict(p=AM+'Heart murmur in aortic and pulmonary insufficiency.jpg', credit='AMBOSS'),
 'phonoHolo': dict(p=AM+'Heart murmur in ventricular septal defect, mitral regurgitation, and tricuspid regurgitation.jpg', credit='AMBOSS'),
 'phonoHCM': dict(p=AM+'Heart murmur in hypertrophic obstructive cardiomyopathy, aortic stenosis, and pulmonary stenosis.jpg', credit='AMBOSS'),
 'trMS': dict(p=SA+'cc-ms-tracing.jpg', credit='Qazi lecture', masks=[(0.42,0.11,0.73,0.275,'auto')]),
 'trAS': dict(p=SA+'cc-as-tracing.jpg', credit='Qazi lecture', masks=[(0.46,0.17,0.83,0.29,'auto')]),
 'trMR': dict(p=SA+'cc-mr-tracing.jpg', credit='Qazi lecture', masks=[(0.30,0.19,0.86,0.275,'auto'), (0.385,0.525,0.522,0.648,'auto'), (0.52,0.585,0.537,0.633,'auto')]),
 'trAR': dict(p=SA+'cc-ar-tracing.jpg', credit='Qazi lecture',
    masks=[(0.30,0.18,0.93,0.265,'auto'), (0.52,0.27,0.70,0.39,'auto'), (0.70,0.60,0.828,0.668,'auto'), (0.735,0.668,0.81,0.74,'auto'), (0.435,0.585,0.525,0.665,'auto')],
    labels=[(0.48,0.625,'LAP',0.030)]),
 'trMRamb': dict(p=AM+'Time-pressure curves in mitral regurgitation.jpg', credit='AMBOSS', masks=[(0.36,0.0,0.70,0.065,'white')]),
 'schemMS': dict(p=SA+'cc-ms-schematic.jpg', credit='Qazi lecture', masks=[(0.55,0.82,0.99,0.93,'auto')]),
 'schemAS': dict(p=SA+'cc-as-schematic.jpg', credit='Qazi lecture', masks=[(0.58,0.88,0.99,0.995,'auto')]),
 'schemAR': dict(p=SA+'cc-ar-schematic.jpg', credit='Qazi lecture', masks=[(0.52,0.9,0.99,0.995,'auto')]),
 'auscSites': dict(p=AM+'Auscultatory sites of the heart valves.jpg', credit='AMBOSS',
    masks=[(x-0.022, y-0.032, x+0.022, y+0.032, 'auto') for x, y in
           [(0.451,0.209),(0.446,0.462),(0.553,0.454),(0.553,0.534),(0.553,0.609),(0.641,0.646),(0.717,0.583)]],
    labels=[(0.451,0.209,'1'),(0.446,0.462,'2'),(0.553,0.454,'3'),(0.553,0.534,'4'),(0.553,0.609,'5'),(0.641,0.646,'6'),(0.717,0.583,'7')]),
 'aschoff': dict(p=AM+'Aschoff body and Anitschkow cells.jpg', credit='AMBOSS'),
 'msGross': dict(p=AM+'Mitral stenosis.jpg', credit='AMBOSS'),
 'rheumMV': dict(p=SA+'c-rheumatic-mv.jpg', credit='Robbins & Cotran Atlas'),
 'exBP': dict(p=SA+'er-exercise-response.jpg', credit='Qazi lecture', crop=(0.0,0.5,0.52,1.0), up=720),
 'guytonEx': dict(p=SA+'p-guyton-exercise.jpg', credit='Morganelli lecture'),
 'metMort': dict(p=SA+'er-met-mortality.jpg', credit='Qazi lecture (Kodama, JAMA 2009)'),
 'predimed': dict(p=SA+'er-predimed.jpg', credit='Qazi lecture (Estruch, NEJM 2013)'),
 'dashNa': dict(p=SA+'er-dash-sodium.jpg', credit='Qazi lecture (Sacks, NEJM 2001)'),
 'neEpiIso': dict(p=SA+'b-ne-epi-iso.jpg', credit='Scully lecture', masks=[(0.08,0.0,0.99,0.075,'white')],
    labels=[(0.29,0.035,'Drug 1',0.035), (0.53,0.035,'Drug 2',0.035), (0.84,0.035,'Drug 3',0.035)]),
 'ansRate': dict(p=SA+'p-ans-rate.jpg', credit='Morganelli lecture',
    masks=[(0.418,0.14,0.494,0.21,'white'), (0.603,0.14,0.775,0.21,'white'), (0.69,0.745,0.98,0.835,'white')],
    labels=[(0.475,0.172,'1',0.06), (0.70,0.172,'2',0.06), (0.75,0.79,'3',0.06)]),
 'pacemakerAP': dict(p=SA+'p-pacemaker-ap.jpg', credit='Morganelli lecture'),
 'fastAP': dict(p=SA+'p-fast-ap.jpg', credit='Morganelli lecture'),
 'refractory': dict(p=SA+'p-refractory.jpg', credit='Morganelli lecture'),
 'vfcShift': dict(p=SA+'p-vfc-shifts.jpg', credit='Morganelli lecture'),
 'cvFunc': dict(p=AM+'Normal cardiac and vascular function curves.jpg', credit='AMBOSS'),
 'continuity': dict(p=SA+'p-continuity.jpg', credit='Morganelli lecture'),
 'baroLoop': dict(p=SA+'p-baroreflex.jpg', credit='Morganelli lecture'),
 'coDist': dict(p=SA+'p-co-distribution.jpg', credit='Morganelli lecture'),

 # ---------- Part B: ECG, arrhythmias, atrial fibrillation, antiarrhythmics ----------
 'B_lad': dict(p=E1+'k-lad-ecg.jpg', credit='Qazi lecture', crop=(0,0,1,0.96)),
 'B_lll': dict(p=L+'img_lll.png', credit='ecglibrary.com', crop=(0,0.04,1,1)),
 'B_norm': dict(p=L+'img_norm.png', credit='ecglibrary.com'),
 'B_sinusArr': dict(p=E1+'k-sinus-arrhythmia.jpg', credit='Qazi lecture', crop=(0,0.11,1,0.95)),
 'B_mat': dict(p=E1+'k-mat.jpg', credit='Qazi lecture (courtesy J. E. Roediger)'),
 'B_stach': dict(p=L+'img_stach.gif', credit='ecglibrary.com', crop=(0,0.07,1,1)),
 'B_artifact': dict(p=E2+'r-artifact.jpg', credit='Electrophysiology lecture'),
 'B_flutter41': dict(p=E1+'k-flutter.jpg', credit='Qazi lecture'),
 'B_rvh': dict(p=E1+'k-rvh.jpg', credit='Qazi lecture', crop=(0,0.12,1,0.95)),
 'B_lvhCase': dict(p=E1+'k-case-lvh.jpg', credit='Qazi lecture'),
 'B_lvhlah': dict(p=L+'img_lvhlah.gif', credit='ecglibrary.com'),
 'B_rah': dict(p=L+'img_rah.gif', credit='ecglibrary.com'),
 'B_mSten': dict(p=L+'img_m_sten3.gif', credit='ecglibrary.com'),
 'B_lbbbCase': dict(p=E1+'k-case-lbbb.jpg', credit='Qazi lecture', crop=(0,0,1,0.9)),
 'B_rbbbCase': dict(p=E1+'k-case-rbbb.jpg', credit='Qazi lecture'),
 'B_trifas': dict(p=L+'img_trifas2.gif', credit='ecglibrary.com', crop=(0,0.2,1,0.95)),
 'B_wpw8': dict(p=E1+'k-case-8.jpg', credit='Qazi lecture', crop=(0,0.19,1,1)),
 'B_wpwL': dict(p=L+'img_wpw.gif', credit='ecglibrary.com', crop=(0,0.30,1,1)),
 'B_lqt': dict(p=L+'img_l_qt.gif', credit='ecglibrary.com', crop=(0,0,1,0.93)),
 'B_tdpStrip': dict(p=L+'img_tdp.gif', credit='ecglibrary.com', up=900),
 'B_highk': dict(p=L+'img_highk.gif', credit='ecglibrary.com', crop=(0,0,1,0.95)),
 'B_hyperkSev': dict(p=CP+'Arrhythmias - 1.25 - Severe Hyperkalemia Preterminal ECG.png', credit='Cardiovascular Pathophysiology for Pre-Clinical Students', up=420),
 'B_hypok': dict(p=L+'img_hypok.gif', credit='ecglibrary.com'),
 'B_dig': dict(p=L+'img_dig.gif', credit='ecglibrary.com', crop=(0,0,1,0.92)),
 'B_infmi': dict(p=L+'img_infmi.gif', credit='ecglibrary.com', crop=(0,0,1,0.94)),
 'B_ami': dict(p=L+'img_ami.gif', credit='ecglibrary.com', crop=(0,0,1,0.9)),
 'B_postlat': dict(p=L+'img_postlat.gif', credit='ecglibrary.com', crop=(0,0,1,0.94)),
 'B_oldmi': dict(p=L+'img_oldmi.gif', credit='ecglibrary.com'),
 'B_nstemi': dict(p=E1+'k-nstemi.jpg', credit='Qazi lecture'),
 'B_chbStemi': dict(p=E1+'k-case-chb-stemi.jpg', credit='Qazi lecture'),
 'B_hyperacute': dict(p=E1+'k-hyperacute.jpg', credit='Qazi lecture'),
 'B_peri': dict(p=E2+'r-case-pericarditis.jpg', credit='Electrophysiology lecture'),
 'B_1avb': dict(p=E1+'k-1avb.jpg', credit='Qazi lecture', crop=(0,0.075,1,0.97)),
 'B_wenck': dict(p=CP+'Arrhythmias - 1.11 - Mobitz I Second-Degree AV Block.png', credit='Cardiovascular Pathophysiology for Pre-Clinical Students'),
 'B_mobitz2': dict(p=CP+'Arrhythmias - 1.12 - Mobitz II Second-Degree AV Block.png', credit='Cardiovascular Pathophysiology for Pre-Clinical Students'),
 'B_chb': dict(p=L+'img_chb4.gif', credit='ecglibrary.com'),
 'B_2to1': dict(p=E1+'k-case-2to1.jpg', credit='Qazi lecture'),
 'B_afchb': dict(p=L+'img_af_chb3.gif', credit='ecglibrary.com'),
 'B_avnrt': dict(p=E2+'r-a-avnrt-ecg.jpg', credit='AMBOSS'),
 'B_svt': dict(p=E2+'r-case-svt.jpg', credit='Electrophysiology lecture', crop=(0,0,1,0.93)),
 'B_adenoFl': dict(p=E2+'r-adenosine-flutter.jpg', credit='Electrophysiology lecture',
    masks=[(0.0,0.125,1.0,0.153,'white'), (0.0,0.413,0.52,0.447,'white'), (0.0,0.763,1.0,0.797,'white')]),
 'B_flutter21': dict(p=L+'img_af2_1.gif', credit='ecglibrary.com'),
 'B_flutterCase': dict(p=E2+'r-case-flutter.jpg', credit='Electrophysiology lecture', crop=(0,0.1,1,0.92)),
 'B_vtavd': dict(p=L+'img_vtavd2.gif', credit='ecglibrary.com', crop=(0,0.27,1,1)),
 'B_vtCapture': dict(p=E2+'r-case-vt-capture.png', credit='Electrophysiology lecture', crop=(0,0,1,0.92)),
 'B_negConc': dict(p=E2+'r-neg-concordance.png', credit='Electrophysiology lecture'),
 'B_vtMono': dict(p=CP+'Arrhythmias - 1.07 - Monomorphic and Polymorphic Ventricular Tachycardia.png', credit='Cardiovascular Pathophysiology for Pre-Clinical Students', crop=(0.0,0.065,1.0,0.33)),
 'B_vf': dict(p=CP+'Arrhythmias - 1.09 - Ventricular Fibrillation ECG.png', credit='Cardiovascular Pathophysiology for Pre-Clinical Students', up=1000),
 'B_wpwAF': dict(p=L+'img_wpwaf2s.gif', credit='ecglibrary.com'),
 'B_wpwAFcase': dict(p=E2+'r-case-wpw-af.jpg', credit='Electrophysiology lecture', crop=(0,0.33,1,0.95)),
 'B_tdpCase': dict(p=E1+'k-torsades.jpg', credit='Qazi lecture (courtesy J. E. Roediger)'),
 'B_lqtCase': dict(p=E2+'r-case-lqt.jpg', credit='Electrophysiology lecture'),
 'B_brugada': dict(p=SA+'r-a-brugada.jpg', credit='AMBOSS'),
 'B_bigem': dict(p=L+'img_bigem.gif', credit='ecglibrary.com', crop=(0,0,1,0.93)),
 'B_flutter1to1': dict(p=E2+'r-case-flutter-1to1.png', credit='Electrophysiology lecture', crop=(0,0,1,0.92)),
 'B_afFast': dict(p=L+'img_af_fast2.gif', credit='ecglibrary.com'),
 'B_afCase': dict(p=E2+'r-case-af.jpg', credit='Electrophysiology lecture'),
 'B_afLbbb': dict(p=L+'img_af_lbbb.gif', credit='ecglibrary.com'),
 'B_amioLung': dict(p=SA+'aa-a-amio-lung.jpg', credit='AMBOSS'),
 'B_cornea': dict(p=SA+'aa-a-corneal-deposits.jpg', credit='AMBOSS'),
 'B_butterfly': dict(p=SA+'aa-butterfly-rash.jpg', credit='Scully lecture', crop=(0,0.2,1,1), up=480),
 'B_class1': dict(p=SA+'aa-class1-abc.jpg', credit='Scully lecture (after Golan)',
    masks=[(0.03,0.12,0.19,0.42,'auto'), (0.33,0.04,0.48,0.21,'auto'), (0.35,0.21,0.5,0.41,'auto'), (0.58,0.04,0.73,0.21,'auto'),
           (0.62,0.21,0.77,0.39,'auto'), (0.84,0.03,0.99,0.2,'auto'), (0.2,0.75,0.95,0.87,'auto')],
    labels=[(0.27,0.81,'Drug 1',0.07), (0.54,0.81,'Drug 2',0.07), (0.81,0.81,'Drug 3',0.07)]),

 # ---------- Part C: atherosclerosis and ischemic heart disease ----------
 'C_hyaline': dict(p=SA+'v-hyaline.jpg', credit='Gardner lecture', crop=(0,0,1,0.87), up=720),
 'C_hyalineAm': dict(p=AM+'Hyaline arteriolosclerosis.jpg', credit='AMBOSS'),
 'C_hyperplastic': dict(p=SA+'v-hyperplastic.jpg', credit='Gardner lecture', up=760),
 'C_monck': dict(p=SA+'v-monckeberg.jpg', credit='Gardner lecture'),
 'C_clefts': dict(p=SA+'v-cholesterol-clefts.jpg', credit='Robbins & Cotran Atlas'),
 'C_foam': dict(p=AM+'Foam cells.jpg', credit='AMBOSS'),
 'C_flow': dict(p=SA+'v-flow-culture.jpg', credit='Gardner lecture', up=820,
    masks=[(0.0,0.86,0.10,1.0,'auto'), (0.53,0.86,0.63,1.0,'auto')],
    labels=[(0.05,0.93,'1',0.07), (0.575,0.93,'2',0.07)]),
 'C_plaqueAnat': dict(p=SA+'v-plaque-anatomy.jpg', credit='Gardner lecture', up=760,
    masks=[(0.466,0.0,1.0,1.0,'white')],
    labels=[(0.08,0.31,'1',0.09), (0.20,0.50,'2',0.09), (0.16,0.92,'3',0.09)], crop=(0,0,0.462,1)),
 'C_livedo': dict(p=AM+'Livedo reticularis.jpg', credit='AMBOSS'),
 'C_cholEmb': dict(p=AM+'Renal cholesterol emboli.jpg', credit='AMBOSS'),
 'C_flowReserve': dict(p=SA+'as1-coronary-flow-reserve.jpg', credit='Watkins case module (Gould)'),
 'C_steal': dict(p=AM+'Coronary steal syndrome.jpg', credit='AMBOSS'),
 'C_nstemiEcg': dict(p=SA+'as1-nstemi-ecg.jpg', credit='Watkins case module', crop=(0.035,0.10,0.985,0.95)),
 'C_infStemi': dict(p=E1+'k-inferior-stemi.jpg', credit='Qazi lecture', crop=(0,0,1,0.93)),
 'C_antStemi': dict(p=E1+'k-anterior-stemi.jpg', credit='Qazi lecture', crop=(0,0,1,0.94)),
 'C_prinzPain': dict(p=SA+'ihd-a-prinzmetal-pain.jpg', credit='AMBOSS', crop=(0,0.07,1,1)),
 'C_ach': dict(p=SA+'ihd-acetylcholine.jpg', credit='Scully lecture (NEJM)', up=900,
    masks=[(0.0,0.0,0.045,0.07,'auto'), (0.5,0.0,0.545,0.07,'auto')],
    labels=[(0.03,0.05,'1',0.07), (0.53,0.05,'2',0.07)]),
 'C_bio': dict(p=CP+'Ischemic Heart Disease - 7.03 - Cardiac Biomarkers After Myocardial Infarction.png', credit='CV Pathophysiology for Pre-Clinical Students',
    masks=[(0.105,0.405,0.24,0.47,'white')]
          + [(0.645+0.094*t/11-0.007, 0.257+0.086*t/11-0.03, 0.645+0.094*t/11+0.007, 0.257+0.086*t/11+0.03, 'white') for t in range(12)]
          + [(0.442+0.111*t/13-0.021, 0.362+0.230*t/13-0.012, 0.442+0.111*t/13+0.021, 0.362+0.230*t/13+0.012, 'white') for t in range(14)],
    labels=[(0.17,0.44,'1',0.05), (0.50,0.47,'2',0.05), (0.69,0.30,'3',0.05)], crop=(0,0.05,1,1)),
 'C_wavy': dict(p=SA+'c-mi-histo-a.jpg', credit='Gardner lecture', crop=(0,0,1,0.86), up=720),
 'C_neut': dict(p=SA+'c-mi-histo-b.jpg', credit='Gardner lecture', crop=(0,0,1,0.86), up=720),
 'C_macro': dict(p=SA+'c-mi-histo-c.jpg', credit='Gardner lecture', crop=(0,0,1,0.86), up=720),
 'C_gran': dict(p=SA+'c-mi-histo-d.jpg', credit='Gardner lecture', crop=(0,0,1,0.86), up=720),
 'C_scar': dict(p=SA+'c-mi-histo-e.jpg', credit='Gardner lecture', crop=(0,0,1,0.86), up=720),
 'C_neutRb': dict(p=RB+'The Heart - 209f3f3f846ec58b.jpg', credit='Robbins & Cotran Atlas'),
 'C_coag': dict(p=AM+'Myocardial infarction (extensive coagulative necrosis).jpg', credit='AMBOSS'),
 'C_scarAm': dict(p=AM+'Myocardial scar (post infarction).jpg', credit='AMBOSS'),
 'C_cbn': dict(p=SA+'c-contraction-band.jpg', credit='Robbins & Cotran Atlas'),
 'C_mottled': dict(p=SA+'c-mi-3-5d.jpg', credit='Gardner lecture', crop=(0,0,0.86,1)),
 'C_transmural': dict(p=SA+'c-transmural.jpg', credit='Robbins & Cotran Atlas'),
 'C_oldReperf': dict(p=SA+'c-mi-old-reperf.jpg', credit='Gardner lecture', up=760),
 'C_hemoperi': dict(p=SA+'c-hemopericardium.jpg', credit='Robbins & Cotran Atlas'),
 'C_papRupt': dict(p=AM+'Papillary muscle rupture.jpg', credit='AMBOSS'),
 'C_freeWall': dict(p=AM+'Posterolateral myocardial infarction with secondary wall rupture.jpg', credit='AMBOSS'),
 'C_fibrinous': dict(p=AM+'Fibrinous pericarditis.jpg', credit='AMBOSS'),
 'C_vsrEcho': dict(p=SA+'as1-vsr-echo.jpg', credit='Watkins case module', masks=[(0.0,0.0,1.0,0.135,'black')]),

 # ---------- Part D: heart failure, cardiomyopathies, tumors ----------
 'D_boxcar': dict(p=SA+'c-lvh.jpg', credit='Gardner lecture', crop=(0.505,0.52,1.0,0.935), up=760),
 'D_nutmeg': dict(p=SA+'c-nutmeg.jpg', credit='Gardner lecture'),
 'D_psaxLVH': dict(p=SA+'as2-psax-lvh.jpg', credit='Segal/Scully heart-failure case'),
 'D_hfrefLoop': dict(p=SA+'p-hfref-loop.png', credit='Morganelli lecture',
    masks=[(0.585,0.43,0.75,0.52,'auto'), (0.67,0.13,0.82,0.22,'white')], labels=[(0.665,0.475,'Patient',0.045)]),
 'D_hfpefLoop': dict(p=SA+'p-hfpef-loop.png', credit='Morganelli lecture',
    masks=[(0.40,0.61,0.57,0.69,'auto')], labels=[(0.465,0.42,'Patient',0.045)]),
 'D_neuro': dict(p=SA+'hf-neurohumoral.jpg', credit='Scully lecture (Golan)', up=620,
    masks=[(0.345,0.52,0.475,0.58,'auto')], labels=[(0.41,0.548,'X',0.04)]),
 'D_cxrEdema': dict(p=AM+'Cardiogenic pulmonary edema.jpg', credit='AMBOSS'),
 'D_hfCells': dict(p=AM+'Heart failure cells in decompensated heart failure.jpg', credit='AMBOSS'),
 'D_dcm': dict(p=AM+'Dilated cardiomyopathy.jpg', credit='AMBOSS'),
 'D_hcmGross': dict(p=SA+'c-hcm-gross.jpg', credit='Robbins & Cotran Atlas', masks=[(0.0,0.91,0.11,1.0,'black')]),
 'D_disarray': dict(p=SA+'c-hcm-disarray.jpg', credit='Gardner lecture', masks=[(0.0,0.92,0.09,1.0,'auto')]),
 'D_amyloid': dict(p=SA+'c-amyloid.jpg', credit='Robbins & Cotran Atlas'),
 'D_iron': dict(p=SA+'c-iron.jpg', credit='Robbins & Cotran Atlas'),
 'D_arvc': dict(p=SA+'r-a-arvc.jpg', credit='AMBOSS'),
 'D_myxGross': dict(p=SA+'c-myxoma-gross.jpg', credit='Gardner lecture', masks=[(0.0,0.92,0.10,1.0,'black')]),
 'D_myxHisto': dict(p=SA+'c-myxoma-histo.jpg', credit='Gardner lecture', masks=[(0.0,0.92,0.10,1.0,'auto')], up=600),
 'D_tsCT': dict(p=AM+'Tuberous sclerosis.jpg', credit='AMBOSS'),

 # ---------- Part E: endocarditis, myocarditis, pericarditis ----------
 'E_nbte': dict(p=SA+'e-nbte.jpg', credit='CV Pathophysiology (ID lecture)'),
 'E_mitralVeg': dict(p=SA+'e-mitral-veg.jpg', credit='ID lecture'),
 'E_aorticPerf': dict(p=SA+'e-aortic-perforation.jpg', credit='ID lecture'),
 'E_libman': dict(p=SA+'c-libman.jpg', credit='Robbins & Cotran Atlas'),
 'E_candida': dict(p=SA+'e-candida-veg.jpg', credit='ID lecture'),
 'E_prosth': dict(p=SA+'e-prosthetic-veg.jpg', credit='ID lecture', crop=(0.0,0.0,0.49,0.84), up=640),
 'E_conj': dict(p=SA+'e-petechiae-conj.jpg', credit='ID lecture', up=520),
 'E_splinter': dict(p=SA+'e-splinter.jpg', credit='ID lecture'),
 'E_janeway': dict(p=AM+'Janeway lesions.jpg', credit='AMBOSS'),
 'E_roth': dict(p=SA+'e-roth.jpg', credit='ID lecture'),
 'E_tte': dict(p=SA+'e-tte.jpg', credit='ID lecture'),
 'E_toe': dict(p=SA+'e-toe.jpg', credit='ID lecture'),
 'E_pet': dict(p=SA+'e-pet.jpg', credit='ID lecture'),
 'E_biofilm': dict(p=SA+'e-biofilm-sem.jpg', credit='ID lecture'),
 'E_lyme': dict(p=SA+'e-lyme-block.jpg', credit='AMBOSS'),
 'E_lymph': dict(p=SA+'e-lymphocytic.jpg', credit='AMBOSS'),
 'E_chagas': dict(p=SA+'c-chagas-histo.jpg', credit='Gardner lecture', up=760),
 'E_tb': dict(p=SA+'e-tb-pericarditis.jpg', credit='Robbins & Cotran Atlas'),
 'E_waterBottle': dict(p=SA+'e-water-bottle.jpg', credit='AMBOSS'),
 'E_fibrinous': dict(p=SA+'c-fibrinous.jpg', credit='Gardner lecture'),
 'E_alternans': dict(p=AM+'Electrical alternans.jpg', credit='AMBOSS'),
 'E_periEcg': dict(p=AM+'Viral pericarditis.jpg', credit='AMBOSS', crop=(0,0,1,0.95)),
 'E_pericCalc': dict(p=AM+'Pericardial thickening and calcification.jpg', credit='AMBOSS'),

 # ---------- Part F: valve disease and valve replacement ----------
 'F_valvePlane': dict(p=SA+'s-valve-plane.jpg', credit='McGrath lecture',
    masks=[(0.10,0.05,0.30,0.14,'white'), (0.77,0.04,0.96,0.14,'white'), (0.10,0.80,0.25,0.86,'white'), (0.77,0.81,0.97,0.87,'white')],
    labels=[(0.20,0.095,'1',0.05), (0.865,0.09,'2',0.05), (0.175,0.83,'3',0.05), (0.87,0.84,'4',0.05)]),
 'F_ossif': dict(p=CP+'Valvular Disease - 4.01 - Calcific Aortic Valve Ossification Histology.png', credit='CV Pathophysiology for Pre-Clinical Students',
    masks=[(0.0,0.0,0.12,0.17,'white')]),
 'F_bileaflet': dict(p=SA+'s-a-bileaflet.jpg', credit='AMBOSS', up=600),
 'F_bioprosth': dict(p=SA+'s-a-bioprosthetic.jpg', credit='AMBOSS'),
 'F_bioFail': dict(p=SA+'s-r-bioprosthesis-fail.jpg', credit='Robbins & Cotran Atlas'),
 'F_tilting': dict(p=SA+'s-r-tilting.jpg', credit='Robbins & Cotran Atlas'),
 'F_valveCxr': dict(p=SA+'s-r-valve-cxr.jpg', credit='Robbins & Cotran Atlas'),
 'F_schisto': dict(p=AM+'Schistocytes.jpg', credit='AMBOSS'),
 'F_angio': dict(p=AM+'Angiodysplasia.jpg', credit='AMBOSS'),

 # ---------- Part G: congenital heart disease ----------
 'G_asdvsd': dict(p=SA+'c-asd-vsd-gross.jpg', credit='Robbins & Cotran Atlas'),
 'G_pda': dict(p=SA+'c-pda-gross.jpg', credit='Robbins & Cotran Atlas'),
 'G_pfo': dict(p=SA+'c-pfo.jpg', credit='Robbins & Cotran Atlas'),
 'G_boot': dict(p=SA+'c-boot.jpg', credit='AMBOSS'),
 'G_circum': dict(p=SA+'pc-circumoral.jpg', credit='Pediatric Cardiology lecture'),
 'G_tga': dict(p=AM+'Transposition of the great vessels (TGV).jpg', credit='AMBOSS'),
 'G_truncus': dict(p=AM+'Persistent truncus arteriosus.jpg', credit='AMBOSS',
    masks=[(0.455,0.0,1.0,0.075,'auto'), (0.865,0.55,0.995,0.76,'auto')]),
 'G_coarcAngio': dict(p=SA+'pc-coarct-angio.jpg', credit='Pediatric Cardiology lecture', up=620),
 'G_coarcGross': dict(p=SA+'c-coarct.jpg', credit='Robbins & Cotran Atlas'),
 'G_clubbing': dict(p=AM+'Digital clubbing.jpg', credit='AMBOSS'),
 'G_asdEcg': dict(p=AM+'ECG in pulmonary hypertension secondary to an atrial septal defect.jpg', credit='AMBOSS', crop=(0,0.08,1,0.97)),
 'G_vsdGross': dict(p=AM+'Subaortic ventricular septal defect.jpg', credit='AMBOSS'),

 # ---------- Part H: vessels — hypertension, lipids, aorta, vasculitis, PAD, mesenteric ----------
 'H_retino': dict(p=AM+'Grade IV hypertensive retinopathy.jpg', credit='AMBOSS'),
 'H_adrenal': dict(p=AM+'Left adrenal mass.jpg', credit='AMBOSS'),
 'H_striae': dict(p=AM+'Stretch marks (striae).jpg', credit='AMBOSS'),
 'H_tophi': dict(p=AM+'Gouty tophi.jpg', credit='AMBOSS'),
 'H_lipemic': dict(p=SA+'lp-a-lipemic.jpg', credit='AMBOSS'),
 'H_arcus': dict(p=SA+'lp-a-arcus.jpg', credit='AMBOSS'),
 'H_xanthelasma': dict(p=SA+'lp-a-xanthelasma.jpg', credit='AMBOSS'),
 'H_aaaGross': dict(p=SA+'v-aaa-gross.jpg', credit='Robbins & Cotran Atlas'),
 'H_aaaCt': dict(p=SA+'vs-aaa-ct.jpg', credit='Ciraulo lecture'),
 'H_splenic': dict(p=SA+'vs-splenic-aneurysm.jpg', credit='Ciraulo lecture', up=700),
 'H_popliteal': dict(p=SA+'vs-popliteal-aneurysm.jpg', credit='Ciraulo lecture', up=700),
 'H_colitis': dict(p=SA+'vs-ischemic-colitis.jpg', credit='Ciraulo lecture'),
 'H_ctaDissection': dict(p=SA+'vs-cta-dissection.jpg', credit='Ciraulo lecture'),
 'H_doubleBarrel': dict(p=SA+'v-double-barrel.jpg', credit='Gardner lecture'),
 'H_debakey': dict(p=SA+'v-debakey.jpg', credit='Gardner lecture (Radiopaedia)',
    masks=[(0.0,0.0,1.0,0.05,'white'), (0.0,0.935,1.0,1.0,'white')],
    labels=[(0.16,0.028,'1',0.035), (0.5,0.028,'2',0.035), (0.83,0.028,'3',0.035)]),
 'H_ehlers': dict(p=AM+'Facial features of Ehlers-Danlos syndrome.jpg', credit='AMBOSS'),
 'H_gcaHisto': dict(p=SA+'v-gca-histo.jpg', credit='Gardner lecture'),
 'H_gcaTemporal': dict(p=SA+'v-gca-temporal.jpg', credit='Gardner lecture', masks=[(0.0,0.93,0.07,1.0,'auto')]),
 'H_takayasu': dict(p=SA+'v-takayasu.jpg', credit='Robbins & Cotran Atlas'),
 'H_pan': dict(p=SA+'v-pan-fibrinoid.jpg', credit='Gardner lecture'),
 'H_buerger': dict(p=SA+'vs-buerger.jpg', credit='Ciraulo lecture', up=760),
 'H_cAnca': dict(p=SA+'v-c-anca.jpg', credit='AMBOSS', masks=[(0.55,0.85,1.0,0.99,'black')]),
 'H_pAnca': dict(p=SA+'v-p-anca.jpg', credit='AMBOSS', masks=[(0.45,0.84,1.0,0.99,'black')]),
 'H_purpura': dict(p=SA+'v-palpable-purpura.jpg', credit='Robbins & Cotran Atlas'),
 'H_leuko': dict(p=SA+'v-leukocytoclastic.jpg', credit='Gardner lecture', up=700),
 'H_rubor': dict(p=SA+'as2-dependent-rubor.jpg', credit='Segal PAD case (NEJM)', masks=[(0.0,0.0,0.06,0.07,'auto')]),
 'H_blueToe': dict(p=SA+'vs-blue-toe.jpg', credit='Ciraulo lecture', up=700, masks=[(0.68,0.82,0.98,0.95,'auto')]),
 'H_leriche': dict(p=SA+'as2-leriche-ct.jpg', credit='Segal PAD case'),
 'H_abi': dict(p=SA+'vs-abi.jpg', credit='Ciraulo lecture', up=760, masks=[(0.14,0.83,0.46,0.995,'auto'), (0.54,0.83,0.86,0.995,'auto')]),
 'H_fasciotomy': dict(p=SA+'vs-fasciotomy.jpg', credit='Ciraulo lecture'),
 'H_sma': dict(p=SA+'vs-sma-embolus.jpg', credit='Ciraulo lecture', crop=(0,0,1,0.86)),
 'H_deadBowel': dict(p=SA+'vs-dead-bowel.jpg', credit='Ciraulo lecture'),
}

def _auto(im, box):
    # lightest of the four corners just inside the box: the background, not a line or a letter
    w, h = im.size
    l, t, r, b = int(box[0]*w), int(box[1]*h), int(box[2]*w)-1, int(box[3]*h)-1
    pts = [(l+1, t+1), (r-1, t+1), (l+1, b-1), (r-1, b-1)]
    return max((im.getpixel(p) for p in pts), key=sum)

def load(key, maxw=1100):
    e = IMGS[key]
    im = _ongrid(e['p']) if e['p'].lower().endswith('.gif') else Image.open(e['p']).convert('RGB')
    w, h = im.size; d = ImageDraw.Draw(im)
    for m in e.get('masks', []):
        col = m[4] if len(m) > 4 else 'white'
        if col == 'auto': col = _auto(im, m)
        d.rectangle((int(m[0]*w), int(m[1]*h), int(m[2]*w), int(m[3]*h)), fill=col)
    for lab in e.get('labels', []):
        x, y, txt = lab[:3]; size = lab[3] if len(lab) > 3 else 0.045
        f = ImageFont.truetype(FONT, max(12, int(size*h)))
        bb = d.textbbox((0, 0), txt, font=f); tw, th = bb[2]-bb[0], bb[3]-bb[1]
        cx, cy = x*w, y*h; r = max(tw, th)/2 + 0.35*th
        if len(txt) <= 2:
            d.ellipse((cx-r, cy-r, cx+r, cy+r), fill='white', outline=(30, 30, 30), width=max(2, int(r/7)))
        d.text((cx-tw/2-bb[0], cy-th/2-bb[1]), txt, font=f, fill=(20, 20, 20))
    if e.get('crop'):
        l, t, r, b = e['crop']; im = im.crop((int(l*w), int(t*h), int(r*w), int(b*h)))
    up = e.get('up')
    if up and im.width < up:
        im = im.resize((up, int(im.height*up/im.width)), Image.LANCZOS)
    if im.width > maxw:
        im = im.resize((maxw, int(im.height*maxw/im.width)), Image.LANCZOS)
    return im

def data_uri(key):
    im = load(key); buf = io.BytesIO(); im.save(buf, 'JPEG', quality=85, optimize=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
