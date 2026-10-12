"""Build the Cardio summative exam files from the question modules.

    python3 build.py A            # audit Part A only
    python3 build.py A write      # audit and write Cardio_Summative_Exam_Part_A.html
    python3 build.py all write    # every part that has modules

Each question module defines Q = [dict(...), ...] with:
  img / cap   image key from images.py and a neutral caption (or img=None for a text item)
  stem        HTML; '{FIG}' marks where the figure goes (before the lead-in)
  choices     option texts WITHOUT letters (sorted alphabetically at build time unless all start with a digit)
  key         index of the correct option in `choices` as written
  exp         explanation HTML, ending with '<b>Educational objective:</b> ...'
  wrong       {index: why that option is wrong} for every wrong option (indexes as written)
  eli5        plain-language version, at most 3 sentences
  sec         review-page section number the item tests (for the coverage table in the handoff)
"""
import json, re, sys, importlib, os
from images import data_uri, IMGS

HERE = os.path.dirname(os.path.abspath(__file__))
EXAM = os.path.dirname(HERE)
SRC = os.path.join(EXAM, 'index.html')        # untouched copy of quizbuilder/Unmodified Index/index.html
LET = 'ABCDEFGH'

PARTS = {
    'A': ('Cardio Summative Exam — Part A: The Normal Heart', 'Cardio_Summative_Exam_Part_A.html',
          ['q_A1_cycle', 'q_A2_sounds', 'q_A3_murmurs', 'q_A4_maneuvers', 'q_A5_exercise', 'q_A6_control']),
    'B': ('Cardio Summative Exam — Part B: The ECG and Arrhythmias', 'Cardio_Summative_Exam_Part_B.html',
          ['q_B1_basics', 'q_B2_patterns', 'q_B3_arrhythmias', 'q_B4_afib', 'q_B5_antiarrhythmics']),
    'C': ('Cardio Summative Exam — Part C: Atherosclerosis and Ischemic Heart Disease', 'Cardio_Summative_Exam_Part_C.html',
          ['q_C1_athero', 'q_C2_ihd', 'q_C3_biomarkers', 'q_C4_mipath', 'q_C5_complications', 'q_C6_pharm']),
    'D': ('Cardio Summative Exam — Part D: Heart Failure, Cardiomyopathies and Tumors', 'Cardio_Summative_Exam_Part_D.html',
          ['q_D1_hf', 'q_D2_hfpharm', 'q_D3_cm', 'q_D4_tumors']),
    'E': ('Cardio Summative Exam — Part E: Endocarditis, Myocarditis and Pericarditis', 'Cardio_Summative_Exam_Part_E.html',
          ['q_E1_ie', 'q_E2_ie_dxrx', 'q_E3_myoperi']),
    'F': ('Cardio Summative Exam — Part F: Valve Disease and Valve Replacement', 'Cardio_Summative_Exam_Part_F.html',
          ['q_F1_valves', 'q_F2_avr']),
    'G': ('Cardio Summative Exam — Part G: Congenital Heart Disease', 'Cardio_Summative_Exam_Part_G.html',
          ['q_G1_chd', 'q_G2_coarct_newborn']),
    'H': ('Cardio Summative Exam — Part H: Vessels (plus Section 37)', 'Cardio_Summative_Exam_Part_H.html',
          ['q_H1_htn', 'q_H2_htnpharm', 'q_H3_lipids', 'q_H4_lipidpharm', 'q_H5_aorta', 'q_H6_vasculitis', 'q_H7_pad', 'q_H8_mesenteric', 'q_H9_women']),
}

def fig(key, cap):
    credit = IMGS[key]['credit']
    assert 'uworld' not in IMGS[key]['p'].lower(), 'UWorld image: ' + key
    return ('<figure class="qfig" style="margin:16px 0;text-align:center">'
            f'<img src="{data_uri(key)}" alt="Figure 1" style="display:block;margin:0 auto;max-width:100%;max-height:460px;height:auto;'
            'border-radius:8px;border:1px solid rgba(0,0,0,.14);background:#fff;cursor:zoom-in" onclick="window.open(this.src)">'
            f'<figcaption class="qfig-cap" style="font-size:12.5px;margin-top:6px;opacity:.8">Figure 1 · {cap} · <i>{credit}</i></figcaption></figure>')

def check(q, where):
    n = len(q['choices'])
    assert 4 <= n <= 8, (where, 'option count', n)
    assert 0 <= q['key'] < n, (where, 'key')
    assert set(q['wrong']) == set(range(n)) - {q['key']}, (where, 'wrong keys', sorted(q['wrong']))
    assert '{FIG}' in q['stem'], (where, 'no {FIG} marker')
    assert 'Educational objective' in q['exp'], (where, 'no educational objective')
    assert len(set(c.lower() for c in q['choices'])) == n, (where, 'duplicate option')
    if q.get('img'): assert q['img'] in IMGS, (where, 'unknown image', q['img'])

def to_json(Q):
    out = []
    for i, q in enumerate(Q, 1):
        check(q, i)
        stem = q['stem'].replace('{FIG}', fig(q['img'], q['cap']) if q.get('img') else '<br><br>')
        order = list(range(len(q['choices'])))
        if not all(c[:1].isdigit() for c in q['choices']):
            order = sorted(order, key=lambda j: q['choices'][j].lower())
        ch = [f'{LET[n]}. {q["choices"][j]}' for n, j in enumerate(order)]
        out.append(dict(stem=stem, choices=ch, correct=order.index(q['key']), explanation=q['exp'],
                        wrongExplanations={str(order.index(j)): v for j, v in q['wrong'].items()}, eli5=q['eli5']))
    return out

def audit(name, Q):
    n = longest = shortest = 0; chance = 0.0
    for q in Q:
        if all(len(c.split()) <= 4 for c in q['choices']): continue   # single-term lists are naturally uneven
        L = [len(c) for c in q['choices']]; k = q['key']; n += 1; chance += 1/len(L)
        longest += L[k] == max(L) and L.count(max(L)) == 1
        shortest += L[k] == min(L) and L.count(min(L)) == 1
    imgs = sum(1 for q in Q if q.get('img'))
    counts = {}
    for q in Q: counts[len(q['choices'])] = counts.get(len(q['choices']), 0) + 1
    print(f'{name}: {len(Q)} items, {imgs} with images; option counts {dict(sorted(counts.items()))}; '
          f'phrase-style {n}: key uniquely longest {longest}, uniquely shortest {shortest} (chance ≈ {chance:.1f} each)')

def write(Q, title, fn):
    qs = to_json(Q)
    html = open(SRC, encoding='utf-8').read()
    enc = lambda v: json.dumps(v, ensure_ascii=False).replace('</script', '<\\/script').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    html = re.sub(r'(<div class="view) active(" id="viewSetup">)', r'\1\2', html, count=1)
    html = re.sub(r'<title>[^<]*</title>', lambda m: f'<title>{title}</title>', html, count=1)
    html = re.sub(r'^var PRELOADED_QUIZ_NAME=[^\r\n]*;', lambda m: 'var PRELOADED_QUIZ_NAME=' + enc(title) + ';', html, count=1, flags=re.M)
    html = re.sub(r'^var PRELOADED_QUESTIONS_JSON=[^\r\n]*;', lambda m: 'var PRELOADED_QUESTIONS_JSON=' + enc(json.dumps(qs, ensure_ascii=False)) + ';', html, count=1, flags=re.M)
    html = re.sub(r'^var PRELOADED_UI_MODE=[^\r\n]*;', lambda m: 'var PRELOADED_UI_MODE=' + enc('nbme') + ';', html, count=1, flags=re.M)
    out = os.path.join(EXAM, fn)
    open(out, 'w', encoding='utf-8').write(html)
    print('wrote', out, round(len(html)/1e6, 2), 'MB,', len(qs), 'questions')

if __name__ == '__main__':
    sys.path.insert(0, HERE)
    parts = [p for p in sys.argv[1:] if p != 'write']
    if parts == ['all']: parts = list(PARTS)
    for p in parts:
        title, fn, mods = PARTS[p]; Q = []
        for m in mods:
            try: mq = importlib.import_module(m).Q
            except ModuleNotFoundError: print('  (not written yet:', m + ')'); continue
            audit('  ' + m, mq); Q += mq
        audit(f'Part {p} total', Q)
        if 'write' in sys.argv: write(Q, title, fn)
