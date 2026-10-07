import re
P='/Users/jeeval/Documents/GitHub/Second-Year/OMK/Cardio/Week 15/notes/Exercise_Rehabilitation_Study_Notes.html'
s=open(P,encoding='utf-8').read()
assert 'From the recording' not in s, 'already applied'
def co(title,body): return '    <div class="callout callout-hook">\n      <div class="callout-title">🎙️ From the recording: '+title+'</div>\n      '+body+'\n    </div>\n'
ADD={
's1-lifestyle':co('what she stressed',
 '<ul class="notes-list"><li>Bulk of coronary disease is <strong>modifiable</strong>: bad diet, inactivity and smoking, plus overweight; hypertension and diabetes are the clinical risk factors.</li>'
 '<li><strong>Too much of a good thing</strong>: inflammatory markers are actually <em>high</em> right after a marathon, and <strong>ultra-endurance runners (50–100 miles) commonly get atrial fibrillation</strong>. The protective effects belong to <strong>regular, moderate</strong> exercise.</li>'
 '<li>The lipid effect she sees most in clinic: sedentary patients who start exercising get a clear <strong>rise in HDL</strong>.</li>'
 '<li>Psychological benefit: in a trial of depressed patients on one antidepressant, <strong>adding regular exercise worked about as well as adding a second antidepressant</strong>.</li></ul>'),
's2-physiology':co('conditioned vs deconditioned',
 '<div class="compare-grid"><div class="compare-card" style="background:var(--red-bg);border-color:var(--accent)"><h4>Deconditioned</h4><p><strong>High resting HR</strong>; HR <strong>skyrockets</strong> as soon as the treadmill starts; stays elevated a long time after stopping.</p></div>'
 '<div class="compare-card" style="background:var(--green-bg);border-color:#2e7d32"><h4>Conditioned (e.g. marathoner)</h4><p><strong>Slow resting HR</strong>; HR stays low for much of the protocol; <strong>drops back to baseline quickly</strong> after stopping.</p></div></div>'
 '<p>The Bruce protocol raises speed and incline every 3 minutes so patients are still walking, not running. Blood flow at rest: 15–20% to muscle; with exercise it flips, so only 15–20% stays with the viscera. That is why you don\'t work out right after a big meal. SBP can reach about <strong>190</strong>; DBP stays the same.</p>'
 '<p><strong>VO₂max vs VO₂peak in practice</strong>: measured by cardiopulmonary exercise testing, mostly in <strong>HFrEF to judge transplant candidacy</strong> (a falling VO₂peak means the patient is getting closer to transplant). It is increasingly ordered in "longevity" medicine.</p>'),
's3-fitness':co('the conversation',
 '<p>Counselling about exercise is hard because patients often hear it as a comment on their <strong>weight</strong>; some refuse to be weighed, and weight "is kind of like a vital sign." She asked the class to find ways to discuss it <strong>without the patient feeling fat-shamed</strong>. Guideline answer to "how much?": <strong>≥ 150 min/week moderate or ≥ 75 min/week vigorous</strong>.</p>'),
's4-cr':co('how CR actually runs today',
 '<ul class="notes-list"><li><strong>Phase I is now mostly meaningless.</strong> It dates from the bed-rest era of MI care; today a STEMI gets emergency PCI and goes home in a day or two, so patients go <strong>straight to phase II</strong>.</li>'
 '<li><strong>Phase II</strong>: a staffed facility (a cardiologist available, exercise physiologists, CR nurses, nutritionists). Medicare pays for <strong><span class="num">36</span> sessions</strong>, to be used within <strong>about a year</strong>, usually <strong>2–3 one-hour sessions a week</strong>. Its defining feature is <strong>continuous ECG monitoring</strong> for HR response and exercise-induced arrhythmias.</li>'
 '<li><strong>Phase III (and IV)</strong>: <strong>unmonitored</strong> and <strong>not covered</strong>, "like an expensive gym membership" (about $90/month at Maine Medical Center); some patients stay for 20 years.</li>'
 '<li>Coverage quirks: <strong>PAD with claudication</strong> qualifies (first-line therapy is a walking programme plus medicines). Medicare covers chronic HF <strong>only with EF ≤ <span class="num">35</span>%</strong> (HFrEF), not HFpEF, which she called a disservice.</li>'
 '<li>Hospitals generate <strong>automatic referrals</strong> (MI, CABG, PCI, valve surgery); case managers find the nearest programme. After sternotomy patients usually need <strong>at least 4 weeks</strong> before they are cleared for activity.</li>'
 '<li>Why so little trial data? <strong>CR loses money</strong> for most institutions (unlike TAVR); large centres keep it because it <strong>cuts readmissions</strong>.</li></ul>'),
's5-evidence':co('her take',
 '<p>Even the <strong>frailest HFrEF patients</strong> benefit: getting them to walk 10 steps and do some arm exercises three times a week measurably improves quality of life. Older studies of CR were hard to run; one programme even <strong>paid patients per visit</strong> to keep them coming so outcomes could be followed.</p>'),
's6-rx':co('practical prescription',
 '<ul class="notes-list"><li>"Doctor, what should my heart rate be?" Her sweet spot: about <strong><span class="num">65–70</span>% of maximal HR</strong>. VO₂-based targets need a lab test, so HR targets are more useful day to day.</li>'
 '<li>Always <strong>warm up</strong>, since middle-aged patients injure easily, and cool down.</li>'
 '<li><strong>HIIT</strong> was the fashion in the 2000s–2010s and is now questioned (cortisol). <strong>Resistance training</strong> is never wrong and is the strongest defence against <strong>frailty</strong> ("frailty will kill people"). Add <strong>flexibility</strong>, and <strong>balance and mobility</strong> in patients in their 70s–80s.</li>'
 '<li>Consistent moderate aerobic work plus some resistance plus flexibility makes a patient "a 1%er."</li></ul>'),
's7-underuse':co('what you can do',
 '<p>The determinant with the most impact is <strong class="hot">the strength of the primary physician\'s endorsement</strong>. Make "has a cardiac rehab referral been done?" part of your <strong>post-MI / post-surgery template</strong>, and sell both the exercise and the education. Middle-aged patients with full-time jobs struggle to attend 3 hours a week. Post-MI patients are often <strong>afraid of every chest sensation</strong> (almost PTSD-like), and CR staff help them regain confidence. Exception: a very fit, motivated patient who will exercise anyway can reasonably go it alone. Her cautionary case was a triathlete whose chest discomfort at mile 8 turned out to be a critical LAD "widow-maker" lesion.</p>'),
's8-diet':co('diets in practice',
 '<ul class="notes-list"><li><strong>Ornish</strong>: fully plant-based, <strong>no fats or oils</strong>; small case series showed <strong>plaque regression</strong>, but it is almost impossible to sustain. <strong>Esselstyn</strong> (Cleveland Clinic; the basis of <em>Forks Over Knives</em>) is similar. Her patient with likely familial hypercholesterolemia, who was statin-intolerant, got total cholesterol under 200 for the first time after 6 weeks on it.</li>'
 '<li>Mediterranean specifics: plenty of carbohydrate, as long as it is <strong>complex</strong>; fat mainly from <strong>olive oil or nuts</strong>; protein mainly <strong>seafood</strong>; red meat and sweets at the tip.</li>'
 '<li><strong>PREDIMED was re-analysed and republished in 2018</strong> after randomisation problems; the benefit held. She repeated the slide\'s "30 g per week" of nuts (the trial used 30 g/day).</li>'
 '<li>Sodium: <strong>&lt; 2,400 mg</strong> is reasonable for hypertension; &lt; 1,500 is "a totally bland diet."</li>'
 '<li><strong>Eggs are fine.</strong> Only a small share of dietary cholesterol shows up in the blood panel (she quoted ~3%). The real culprits are junk food: <strong>saturated fat and refined carbohydrates</strong>.</li>'
 '<li><strong class="hot">Mediterranean is the only diet with an RCT</strong> supporting it in cardiovascular disease.</li></ul>')}
for sid,blk in ADD.items():
    m=re.search(r'<div class="section" id="'+sid+r'">',s); assert m,sid
    end=s.find('<div class="section"',m.end())
    k=s.find('    <div class="exam-q">',m.end()); assert 0<k<end,sid
    s=s[:k]+blk+s[k:]
old='<span class="value">43 slides (no recording)</span>'; assert old in s
s=s.replace(old,'<span class="value">43 slides + recording</span>')
old='43 slides, including ACC Education slides; no recording)'; assert old in s
s=s.replace(old,'43 slides, including ACC Education slides; plus the lecture recording, whose emphasis is in the "From the recording" boxes)')
open(P,'w',encoding='utf-8').write(s); print('done', s.count('From the recording'))
