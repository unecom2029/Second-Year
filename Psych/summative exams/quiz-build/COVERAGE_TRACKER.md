# OMK 2A Psych Exam 2 — Quiz Build Tracker

Source: `OMK_2A_Psych_Exam2_By_Objective.html` (105 learning objectives)
Running question file: `exam2_bank.json` — all batches merged into one array as they are finished
(per-batch source files kept alongside it: `exam2_batch2.json`, ...; `exam2_bank.backup.json` = pre-merge Batch 1 only)
Batch size: 20 items (see note at bottom)
**Every answer key now carries a `[Learning objectives: LO ...]` tag at the end of the `explanation` field — answer key only, never the stem.**
Batches 1 and 2 were retrofitted with tags on 2026-08-28.

## Batch plan

| # | Batch | Topic block | LOs targeted | Status |
|---|-------|-------------|--------------|--------|
| 1 | Mood, Mood Stabilizers & Antidepressant Pharm | Mood & Mood Stabilizers + Cross-Cutting Pharm | 017 018 024 037 043 044 046 056 064 074 085 088 090 102 (+029 097 partial) | ✅ DONE (20 items) |
| 2 | Psychosis & Antipsychotics | Psychosis & Antipsychotics | 004 021 022 045 047 049 051 053 055 063 068 070 083 086 087 095 | ✅ DONE (20 items, merged) |
| 3 | Anxiety, OCD & Trauma + Psychotherapy/Theory | Anxiety/OCD/Trauma + Psychotherapy | 002 009 011 012 035 036 041p 050 058 060 061 073 076 081 091 098 099 | ✅ DONE (20 items, merged) |
| 4 | Substance Use, Tox & Neurocognitive/AMS | Substance & Tox + Neurocognitive | 001 003 005 006 010 013 015 026 030 032 091 093 099 | ✅ DONE (20 items, merged) |
| 5 | Personality, Eating, Somatoform/Dissoc/Sexual | PD + ED + Somatoform | 008 014 020 023 030 031 033 034 038 039 041 067 069 077 078 089 105 | ✅ DONE (20 items, merged) |
| 6 | Legal/Ethics/Risk + Child & Adolescent + MSE | Legal + Child + Assessment | 010 016 029 032 044 052 054 057 059 066 072 075 079 080 084 090 092 094 096 100 101 103 | ✅ DONE (20 items, merged) |
| 7 | Top-up: limbic circuits, ADHD adjuncts, pregnancy, psychosexual | Cross-block gap closure | 025 042 074 082 084 092 104 | ✅ DONE (12 items, merged) |

## FINAL STATUS — 7 batches complete, 132 items

**102 of 105 objectives** carry at least one dedicated item (LO tags sit at the end of each `explanation`).

### Batch 7 — top-up (items 121–132), 12 items
Closed the four writable gaps left after Batch 6:
- **025** limbic circuit neuroanatomy — Q1 motor loop/dyskinesias, Q2 associative loop/intrusive thoughts,
  Q3 limbic loop/labile mood (a three-item parallel set built on one option architecture), Q4 nucleus
  accumbens dopamine vs amygdala norepinephrine
- **042** ADHD adjuncts — Q5 alpha-2 agonist added for residual hyperactivity when the stimulant already
  fixed attention, Q6 atomoxetine "never worked" at 0.45 mg/kg (underdosing, not drug failure),
  Q7 atomoxetine/viloxazine suicidality warning
- **082** psychotropics in pregnancy — Q8 lithium held in T1 and resumed later (Ebstein timing),
  Q9 preconception valproate transition + high-dose folate, Q10 benzodiazepine risk window at 2–8 weeks,
  Q11 carbamazepine induction defeating oral contraceptives → IUD
- **104** Freud's psychosexual stages — Q12 anal-retentive fixation

### The 3 objectives with no item — and why
The study guide marks these **✕ Not in your notes**. Writing items would mean inventing content the
lectures do not contain:
- **040** differential diagnosis of the various dementias
- **062** differential of memory impairment + forms of dementia
- **065** left / central / right frontal CVA and psychiatric symptoms

These are a genuine content hole in the source material, not a gap in the bank. If the professor confirms
they are testable, obtain the missing lecture and they become a short supplemental batch.

### Bank-wide metrics at 132 items
- Answer letters: A25 · B25 · C25 · D25 · E24 · F8 — no letter correct 3 times consecutively anywhere.
- Bloom: Analyze 44 · Apply 33 · Evaluate 25 · Understand 20 · Remember 10 (69 of 132 at Analyze/Evaluate).
- 31% of items carry 6 options.
- Every answer key LO-tagged; every `wrongExplanations` key verified against its true choice index.

### Concepts used — Batch 7 (to avoid repeats)
Motor loop → chorea · associative loop → intrusive thoughts ("choreiform movements of the mind") ·
limbic loop → labile mood · accumbens dopamine (augmentation) vs amygdala norepinephrine (restraint) ·
guanfacine added for residual hyperactivity when attention is already controlled · atomoxetine underdosed
at 0.45 mg/kg · atomoxetine/viloxazine suicidality warning · lithium held in first trimester, resumed later ·
preconception valproate switch + folate above prenatal dosing · benzodiazepine organogenesis window
2–8 weeks and category D/X · carbamazepine induction → OCP failure → IUD · anal-retentive fixation

**Structural device spent in Batch 7** — a three-item parallel set (Q1–Q3) that reuses one 6-option
architecture across three different clinical surfaces, with the correct loop moved to a different slot each
time so the set teaches the discrimination rather than the position.

## LO coverage log

### Batch 1 — covered
- **017** mood disorder differentiation (Q1, Q2, Q3, Q6)
- **018** antidepressant mood switching vs MDD vs serotonin toxicity (Q1, Q12)
- **024** MDD vs persistent depressive disorder (Q3)
- **037** hypomania differential (Q2)
- **046** MDD specifiers (Q4, Q5)
- **043** CYP450 inducers/inhibitors/substrates (Q10, Q11)
- **044** antidepressant sexual side effects — *partial* (bupropion referenced in explanations; a dedicated item is queued for a later batch)
- **056** serotonin syndrome / NMS / hypertensive crisis / discontinuation (Q12, Q13, Q14)
- **064** lithium drug–drug interactions (Q7)
- **074** lithium PK/PD (Q7, Q8, Q9)
- **085 / 088** lithium side effects + toxicity (Q7, Q8, Q9)
- **090** acute depression with suicidality — *partial* (lithium antisuicidal thread; ECT item queued for batch 6)
- **102** antidepressant combinations & contraindications (Q17)
- **097** antidepressant class pharmacology (Q15, Q16, Q18, Q19, Q20)

### Batch 2 — covered (items 21–40 of `exam2_bank.json`)
- **004** withdrawal pharmacology — DTs managed with a long-acting benzo, clonidine rejected (Q2)
- **021** complications of psych meds — NMS vs serotonin syndrome by reflexes/onset (Q13)
- **022** physiology/pharm/complications in psychosis mgmt (Q4, Q5, Q10, Q11, Q12, Q13)
- **045** antipsychotic selection by side-effect profile + comorbidity (Q6, Q8, Q9, Q16)
- **047 / 068** four dopamine pathways (Q3 therapeutic effect, Q18 negative symptoms)
- **049 / 051 / 053** acute management of each EPS type (Q4 dystonia, Q5 akathisia, Q11 TD, Q12 pseudoparkinsonism)
- **055** typical potency ↔ side-effect see-saw (Q17 chlorpromazine → α1 orthostasis)
- **063** differential of psychosis, primary vs secondary (Q2, Q19; Q1/Q20 duration ladder + delusional disorder)
- **070** smoking / CYP1A2 — *reverse direction from Batch 1*: hospitalization removes induction → clozapine level rises → seizure (Q10)
- **083** receptor dynamics / binding profiles (Q3, Q7, Q17, Q18)
- **086 / 087** antipsychotic side-effect profiles + effect→agent ID (Q6 QT, Q7 prolactin, Q8 metabolic, Q10)
- **095** treating antipsychotic side effects, contraindications, second-line (Q9, Q11, Q13, Q17)

### Not yet covered from batch-2 blocks (carry forward)
- CATIE / CUtLASS trial specifics and the first-line consensus ladder (SGA → SGA/FGA → clozapine → clozapine augmentation) — no dedicated item; **fold into batch 6**
- Metabolic monitoring schedule for SGAs (weight at 4 & 8 wk then quarterly; glucose/lipids at baseline, 4 wk, quarterly) — **batch 6**
- Cobenfy (M1/M4 agonist), valbenazine for TD, Hafyera 6-month LAI — named in notes, not yet tested

### Not yet covered from batch-1 blocks (carry forward)
- **019** unique considerations per antidepressant class — partly hit; revisit
- **066 / 072** efficacy of treatment options, optimal MDD strategy (ECT / ketamine / esketamine / TMS ladder) → **batch 6**
- **084 / 096** bipolar treatment protocols by phase, lamotrigine + valproate glucuronidation → **batch 6**
- **029** parasuicidal outpatient management, malpractice documentation → **batch 6**
- **044** dedicated SSRI sexual-dysfunction management item → **batch 6**

### Batch 3 — covered (items 41–60 of `exam2_bank.json`)
- **036** anxiety-chapter differential (Q1 panic disorder, Q3, Q4 GAD-7, Q5, Q14, Q15, Q16 chapter membership)
- **050** acute panic management + ruling out the four killers (Q2 → ECG for a 50-min episode at HR 194; Q13)
- **081** psychotherapy/pharmacotherapy by anxiety disorder (Q3 daily vs episodic exposure rule, Q5, Q6, Q14)
- **073** SSRI pharmacokinetics/pharmacodynamics (Q13 side effects at 1–2 wk vs benefit at 4–6 wk)
- **035** child anxiety differential (Q7 separation anxiety, with selective mutism + ASD as rule-outs)
- **061** id / ego / superego (Q8)
- **060 / 098** trauma & stressor-related criteria + adjustment timeline (Q9 ASD at 3 wk ↔ Q10 PTSD at 7 mo cloned pair; Q11 adjustment subtype)
- **076** PTSD pharmacotherapy algorithm (Q12 prazosin for nightmares)
- **041** *partial* — OCD vs OCPD ego-dystonic/ego-syntonic split (Q15); full PD differential still owed to batch 5
- **091** LOT benzodiazepines in hepatic impairment (Q17)
- **058** defense mechanisms (Q18 displacement, Q19 suppression vs repression)
- **002 / 009 / 011 / 012** psychotherapy modality selection (Q20 supportive therapy on C-L service)

### Batch 4 — covered (items 61–80 of `exam2_bank.json`)
- **010** intoxication/withdrawal toxidromes (Q1 opioid withdrawal, Q3, Q4, Q7 cocaine, Q8 amphetamine withdrawal, Q9 PCP, Q10 uppers-on/downers-off rule)
- **013** antidote adverse effects (Q2 naloxone short t½ → redose; Q4 no antidote for barbiturates)
- **026** MOA/adverse effects of drugs of abuse (Q1, Q4, Q7, Q8, Q9, Q12, Q14, Q19, Q20 conditioned tolerance)
- **001 / 005 / 006 / 015** SUD pharmacotherapy (Q5 disulfiram reverse-ID, Q6 acamprosate under opioid constraint, Q12 Suboxone 4:1, Q13 buprenorphine over methadone at QTc 498)
- **091** acute intoxication/withdrawal management (Q2, Q3, Q11 clonidine when agonists are declined)
- **003** recreational drug use intervention (Q14 MDMA → hyponatremia)
- **032** altered mental status differential (Q10, Q15 valproate hyperammonemia at a therapeutic level, Q17 rule-out ladder order)
- **093** dementia-related agitation (Q16 boxed warning → trazodone)
- **030** regression / dissociative differential (Q18 dissociative fugue)
- **099** secondary causes of a panic-like presentation (Q19 caffeine withdrawal)

### ⚠️ Cannot be written from this source — flagged, not forgotten
The study guide labels these **✕ Not in your notes**, so no item was written for them. Writing questions
would mean inventing content outside your lectures:
- **040** differential diagnosis of the various dementias
- **062** differential of memory impairment + forms of dementia
- **065** effect of left / central / right frontal CVA on psychiatric symptoms
If your professor confirms these are testable, get the missing lecture and they become a mini-batch.

### Not yet covered from batch-3/4 blocks (carry forward)
- **059** MSE thought-process/thought-content descriptors — the notes themselves lack flight of ideas,
  tangentiality, looseness of association, thought blocking, ideas of reference → **batch 6**, MSE vs MMSE vs MoCA angle only
- **094** CIWA protocol specifics and alcohol withdrawal with medical comorbidity → **batch 6**
- **013** N-acetylcysteine, atropine/pralidoxime, physostigmine adverse effects — absent from notes
- Barbiturate withdrawal (delirium + CV collapse) tested only indirectly

## Concepts used — Batch 3 (to avoid repeats)
Uncued/nocturnal panic attacks + 1 month behavior change → panic disorder · 50-minute "panic attack" at HR 194 →
ECG for SVT · generalized social anxiety with daily exposure → SSRI, propranolol as the episodic-only trap ·
GAD-7 ≥10 · sertraline at 200 mg max + AUD in remission → buspirone augmentation · buspirone "like water" at day 4 ·
school refusal + fear harm befalls mother → separation anxiety · lecture-hall superego · fire survivor at 3 weeks →
acute stress disorder ↔ same vignette at 7 months → PTSD · husband left, quit job, threatening calls, keyed car →
adjustment disorder with mixed disturbance of emotions and conduct · combat nightmares on sertraline → prazosin ·
panic disorder SSRI counseling (side effects at 1–2 wk, benefit at 4–6 wk) · OCD on fluoxetine 20 mg → increase to
max, not switch · Marcus the estate attorney → OCPD (ego-syntonic) · excoriation disorder is in the OCD chapter ·
cirrhosis + preop anxiety → lorazepam (LOT) · angry at the surgeon not the driver → displacement · suppression vs
repression · day 4 post-MI on C-L service → supportive psychotherapy

## Concepts used — Batch 4 (to avoid repeats)
Jail intake at 14 h → opioid withdrawal (wet & wide) · naloxone re-sedation at 40 min → redose · alcohol = deadliest
withdrawal · phenobarbital OD, naloxone and flumazenil both fail → alkalinize urine · mouthwash → disulfiram flush ·
AUD post-detox on chronic oxycodone → acamprosate (naltrexone blocked) · bugs under the skin + septal perforation +
gingival erosion → cocaine · 3 days off a meth binge, hypersomnia/hyperphagia/existential crisis → amphetamine
withdrawal · punched a window, no pain from tendon-deep laceration, vertical + horizontal nystagmus → PCP ·
psychosis = uppers-on / downers-off · declines agonist therapy → clonidine · Suboxone 4:1 route-based deterrent ·
QTc 498 on two tracings → buprenorphine over methadone · festival, water refills, seizure → hyponatremia ·
asterixis on therapeutic valproate → serum ammonia · nightly pacing in dementia, CAD, no psychosis → trazodone ·
rule-out ladder order (faking → substance → medical → primary) · 300 miles away under a new name → dissociative
fugue · NPO 18 h, five coffees daily → caffeine withdrawal · syringe cue drops heart rate → conditioned tolerance

**Structural devices spent in Batch 3** — a 2-item pharmacologic chain (Q5→Q6 buspirone), a duration-swap cloned
pair (Q9↔Q10 identical vignette, 3 weeks vs 7 months), a double-hop counseling item with the drug never named (Q13),
and a compact third-person narrative (Q15).
**Structural devices spent in Batch 4** — three consecutive reverse-ID toxidrome items with deliberately parallel
6-option substance sets (Q1, Q7, Q9), a mechanism-explanation item with no patient (Q12), and a sequence/ordering
item that tests the rule-out ladder's order rather than its content (Q17).

## Concepts used — Batch 1 (to avoid repeats)
Bipolar I via hospitalization · Bipolar II clone · double depression · atypical features · seasonal specifier ·
schizoaffective 2-week window · lithium+NSAID toxicity · coarse tremor · lithium and AV block ·
smoking/CYP1A2/olanzapine · bupropion 2D6 + imipramine · serotonin syndrome · cyproheptadine ·
MAOI tyramine/phentolamine · TCA overdose · fluoxetine half-life · fluoxetine for bulimia ·
trazodone priapism · mirtazapine in elderly · fluvoxamine OCD-only

## Concepts used — Batch 2 (to avoid repeats)
5-month duration ladder → schizophreniform · delirium tremens treated with chlordiazepoxide (clonidine as the
seizure-inadequate near-miss) · mesolimbic blockade = therapeutic effect · oculogyric crisis + torticollis → IM
benztropine (oral routes as the trap) · akathisia → propranolol (aripiprazole switch as false sophistication) ·
QTc 486 + hypokalemia → avoid ziprasidone · galactorrhea/amenorrhea → risperidone · new T2DM on olanzapine →
switch to aripiprazole · treatment-resistant + suicidality → clozapine (unnamed) → ANC monitoring ·
smoking cessation on a non-smoking ward → clozapine level rise → seizure · 9-year orofacial dyskinesia →
reduce/switch, not benztropine · 9-day cogwheel rigidity → pseudoparkinsonism (7-option EPS set) ·
NMS → stop the antipsychotic first · refused oral meds → B-52 IM · unmedicated relapse 70%/1yr ·
adherence-driven relapse → LAI paliperidone, not clozapine · chlorpromazine orthostasis → α1 ·
negative symptoms on haloperidol → mesocortical blockade · visual hallucinations → secondary psychosis ·
encapsulated non-bizarre fence delusion → delusional disorder, persecutory type

**Structural devices spent in Batch 2** — a 3-item evolving chain off one stem (Q3→Q4→Q5), a 7-option
movement-disorder rule-out set (Q12), a sentence-completion item (Q19), and a compact third-person
narrative (Q20). Batch 1 spent the cloned-stem variable swap, the 2-item chain, and the reused
five-antidote option list.

## Batch size note
20 > 25. At 25 the planning protocol (buried clue + separate decoy + parallel distractors + 5 written
explanations per item) starts thinning out around item 18–20, and the answer-balance/Bloom checks get
sloppier. 20 keeps every item at full build quality. Say the word and I'll run 25.
