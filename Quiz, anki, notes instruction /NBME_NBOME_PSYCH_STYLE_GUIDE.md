# NBME / NBOME Psychiatry Question-Writing Style Guide
### For use in Neuro/Psych study pipeline — vignette construction, distractor architecture, and self-QC gates

---

## 0. HOW TO USE THIS FILE

This guide has two independent style profiles (NBME, NBOME) plus a shared construction checklist and a **mandatory quality gate**. When asked to generate board-style questions:

1. Determine which profile applies (NBME-style USMLE-flavor vs. NBOME/COMLEX-flavor). If unspecified, ask or default to whichever the source lecture/professor most resembles (Willard = more NBOME-adjacent; most Block content = NBME-adjacent).
2. Build the vignette using the skeleton for that profile.
3. Build the answer choices using the distractor rules for that profile.
4. Run the item against the **Quality Gate (Section 4)** before returning it.
5. **If the item fails any gate criterion, do not return it.** Revise internally and re-check. Never present a failing item "for feedback" — fix it first, silently, the way NBME item-writers iterate before an item ever reaches review.

---

## 1. NBME-STYLE VIGNETTE CONSTRUCTION

### 1.1 The Skeleton (follow in this order)

1. **Opening line:** age + sex + presenting complaint + who brought them in / how they arrived.
   - "A 45-year-old man is brought to the physician by his spouse."
2. **Chronicity marker:** an exact, never-vague duration. The duration is frequently load-bearing (differentiates adjustment disorder from MDD, hypomania from mania, brief psychotic disorder from schizophreniform from schizophrenia).
3. **Symptom cluster in behavioral language, not diagnostic language.** Never write "she has depressed mood" — write what she *does* (quits the softball team, dawdles at bedtime, hides behind her mother then warms up).
4. **A "throwaway normal" data block:** vitals, physical exam, sometimes labs. ~85-90% of this block should be unremarkable and exists only to look clinically authoritative. Embed exactly 1-2 load-bearing facts inside it (a BMI, a single abnormal vital, one lab value).
5. **Explicit negative findings** stated directly ("no personal or family history of alcohol abuse," "urine toxicology screening is negative") — these are not filler. They are pre-emptive exclusions of the tempting wrong answer.
6. **MSE placed last, right before the question stem.** This is often the tiebreaker between two remaining plausible diagnoses.
7. **Optional closing patient quote** — a short, verbatim-sounding line that carries disproportionate diagnostic weight ("I don't know, but if I don't go back to work tomorrow, I'll lose my job.").
8. **Question stem**, one of a small set of fixed phrasings:
   - "Which of the following is the most likely diagnosis?"
   - "Which of the following is the most appropriate next step in management?"
   - "Which of the following is the most appropriate next step in diagnosis?"
   - "Which of the following is most appropriate at this point?" (communication/ethics items)
   - "Which of the following is the most appropriate pharmacotherapy?"

### 1.2 The Booby-Trap Rule

Every stem should contain **one detail engineered to seduce the reader toward a specific, named wrong answer.** Decide the trap before writing the rest of the item. Common trap types:
- **Dramatic symptom as decoy:** the most visually/emotionally striking detail in the stem is usually NOT the answer-determining detail (heavy drinking after job loss ≠ the diagnosis; the diagnosis is adjustment disorder, and the drinking is scenery).
- **Medical-disease-in-psychiatric-clothing:** psychotic or mood symptoms are the presenting complaint, but a physical exam finding (moon facies + ecchymoses + truncal obesity = Cushing's) reveals a medical cause. This is one of NBME's signature moves — use it often for GMC-mimicking-psych items.
- **The "second workup" trap:** an acute change from a recent baseline (elderly patient, sudden delirium) tempts you toward a chronic diagnosis (dementia) when the real answer is an acute reversible cause (UTI, delirium workup).

### 1.3 Answer Choice Architecture

- **Parallel-category distractors.** Wrong answers come from the *same diagnostic family* as the correct answer, differing by exactly one criterion (duration, precipitant, presence/absence of one specific feature). Never mix families with no shared logic (e.g., don't pad a mood-disorder differential with an unrelated psychotic disorder unless the psychosis-vs-mood distinction is literally the point of the item).
- **Match stem type to answer type:**
  - "Most likely diagnosis" → tests pattern recognition against DSM-5 criteria.
  - "Next step in management" → tests sequencing logic; correct answer is usually the more conservative/reversible/safety-first action, not the most aggressive one.
  - "Next step in diagnosis" → tests which test/workup, not which treatment.
  - Communication/ethics items → correct answer nearly always: (a) acknowledges/validates before acting, (b) asks directly about safety/suicidality before doing anything else, (c) addresses the patient directly rather than triangulating through family, unless the patient is a minor or incompetent.
- **No length bias.** The correct answer should never be conspicuously the longest or most technical-sounding option, nor the shortest by contrast design. Randomize which position is longest/shortest independent of correctness — this must be checked programmatically (see Section 4).
- **5-7 options**, occasionally more for "select the substance/exposure" style items (Q19 in the sample set used 7).

### 1.4 Rhetorical Fingerprints to Replicate

- Precise, almost legalistic vitals ("blood pressure is 164/88 mm Hg") even when the number isn't diagnostically important — this is atmosphere, not always signal.
- Explicit negative history stated in full sentences, not just omitted.
- Age-appropriate developmental milestones dropped in as reassurance/red-herring for pediatric items.
- Closing quote or MSE line functions as the "punchline" — write it last, make it earn its place.

---

## 2. NBOME-STYLE VIGNETTE CONSTRUCTION

Everything in Section 1 applies as a baseline. NBOME/COMLEX-flavor items add the following layers on top.

### 2.1 What's Different From NBME

1. **Structural/osteopathic exam findings can replace or supplement lab values as the buried clue.**
   - *Confirming direction:* spinal segmental hypertonicity used as if it were a lab value — e.g., T2-T4 and T9 hypertonicity pointing toward sympathetic/adrenal viscerosomatic reflex activity in an endocrine-flavored psychiatric-mimic item.
   - *Ruling-out direction (more sophisticated):* a full structural exam described as unremarkable (negative standing/seated flexion test, no piriformis tenderness, normal lumbar ROM) is used specifically to eliminate a musculoskeletal/OMM-treatable explanation, pushing the diagnosis toward a psychiatric one (e.g., illness anxiety disorder over conversion disorder). Use this direction when you want to test whether the reader can recognize a *negative* structural exam as diagnostically meaningful, not just a positive one.
2. **Neuroanatomic/neuroscience answer choices instead of clinical actions.** A classic clinical-recognition stem (e.g., pediatric ADHD) can have answer choices that are brain regions/structures instead of treatments (DLPFC hypoactivity, periaqueductal gray hyperactivity, tentorium cerebelli shear, cranial rhythmic impulse, diaphragma sellae strain). This tests two layers at once: DSM pattern recognition, then translation to neuroanatomic correlate — with 1-2 distractors deliberately worded to sound cranial-osteopathic-plausible to someone who conflates OMM vocabulary with actual pathophysiology.
3. **Forensic/legal psychiatry framing appears more often** ("brought to the office for evaluation of criminal responsibility"). These items tend to stack multiple bizarre-but-plausible symptoms (ideas of reference, magical thinking, hallucination-adjacent experiences) so the reader must count DSM criteria carefully rather than pattern-match a single obvious symptom.
4. **Iatrogenic-complication-in-progress items.** Instead of a static toxidrome, the stem shows a complication unfolding in real time as a result of treatment already started (e.g., dextrose given to a malnourished/alcohol-use-disorder patient precipitating worsening confusion and extraocular dyssynergia = unmasked Wernicke encephalopathy). The "next step" answer addresses the iatrogenic mechanism directly (add thiamine), not just the presenting complaint.
5. **Tighter, more literal DSM-duration arithmetic.** Duration should function almost like a math constraint rather than supporting color — e.g., a 3-month behavioral change stem transparently tied to a loss 4 months prior nudges toward adjustment disorder over a superficially-matching but duration-incompatible diagnosis (conduct disorder). When you write NBOME-style duration traps, the durations must be internally consistent and specific enough that the reader can rule diagnoses in/out on the numbers alone.
6. **Functional-outcome / negative-symptom literacy items.** Test whether the reader understands symptom control ≠ functional recovery, especially in schizophrenia — a stable, adherent, symptom-controlled patient with poor social/occupational functioning should point toward a functioning-focused intervention (psychosocial rehabilitation), not a symptom-focused one (med change, CBT, DBT).

### 2.2 NBOME Question Stem Phrasing

NBOME stems more often fold the question directly into the final sentence rather than posing a separate "Which of the following..." line:
- "...The most likely diagnosis is"
- "...The most appropriate medication to deescalate this patient is"
- "...Which of the following cerebral abnormalities is most likely present in this patient?"
- "...The most appropriate management to institute while continuing his workup is"

Match this inline phrasing style rather than defaulting to NBME's separated question format.

### 2.3 NBOME Distractor Rules

Build each item with (at minimum):
- **One adjacent-DSM-category distractor** (duration-swap or criteria-swap from the correct diagnosis's neighbor).
- **One "obvious surface-read" distractor** (the diagnosis a reader would pick if they only used the chief complaint and ignored the buried clue).
- **One structural/cranial/neuroanatomic-sounding distractor**, when the item is OMM- or neuroscience-flavored, worded to be plausible only on vocabulary resemblance, not actual pathophysiology.

---

## 3. SHARED CONSTRUCTION TEMPLATE (fill-in-the-blank skeleton)

```
[Age]-year-old [sex] [presents/is brought] to [setting] with a [precise duration]
history of [2-4 symptoms in behavioral, not diagnostic, language].

[1-2 sentences of contextual/historical detail — often a loss, deployment,
medication trial, or recent life event that seems incidental but is load-bearing.]

[Throwaway-normal data block: vitals / physical exam, ~85-90% unremarkable,
with 1-2 load-bearing facts embedded. For NBOME items, may include a structural/
OMM exam finding used to confirm OR explicitly rule out a somatic cause.]

[Explicit negative history, stated in full sentences.]

[MSE, placed last, functioning as tiebreaker.]

[Optional: one short, quote-style patient/family line carrying outsized
diagnostic weight.]

[Question stem — NBME: separate "Which of the following..." line.
NBOME: often folded into the final sentence.]

(A) [correct or distractor]
(B) [correct or distractor]
(C) [correct or distractor]
(D) [correct or distractor]
(E) [correct or distractor]
[(F)/(G) as needed]
```

---

## 4. QUALITY GATE — MANDATORY BEFORE RETURNING ANY GENERATED ITEM

**Do not output a generated question to the user if it fails any of the following checks.** Revise silently and re-run the checklist. Only return items that pass all applicable criteria. If a batch is requested and some items fail after 2-3 revision attempts, drop those items rather than shipping a weak item — quality over quantity.

### 4.1 Structural checks
- [ ] Opening line has age, sex, presenting complaint, and context of presentation (brought by whom / how / where).
- [ ] Exact duration/chronicity is stated, not vague ("for a while," "recently" are forbidden).
- [ ] Symptom description is behavioral/observational, not diagnostic-label language (no "the patient has anhedonia" — describe what that looks like instead).
- [ ] At least one explicit negative history/exam finding is present.
- [ ] MSE (if psychiatric item) is placed at or near the end of the vignette, not buried mid-paragraph.

### 4.2 Trap/signal checks
- [ ] There is exactly one clearly identifiable "buried clue" that determines the correct answer.
- [ ] There is at least one "dramatic decoy" detail that would tempt a reader toward a specific wrong answer if they didn't catch the buried clue.
- [ ] The buried clue and the decoy are NOT the same detail.
- [ ] Every negative finding stated in the stem is doing exclusionary work (ruling out a specific listed distractor) — no negative findings included "just for atmosphere" without a distractor they rule out.

### 4.3 Answer choice checks
- [ ] All distractors are plausible to a reader who missed the buried clue — no throwaway/absurd options.
- [ ] At least one distractor comes from the same diagnostic/pharmacologic family as the correct answer (parallel-category rule).
- [ ] **Length-bias check:** the correct answer is not the uniquely longest or uniquely shortest option. If it naturally is, rewrite distractors to normalize length, or rewrite the correct answer to be mid-length.
- [ ] **Position check (for batches):** correct answer letter is varied across the set — not clustered on the same letter repeatedly. Track and rebalance across a generated batch.
- [ ] Options are mutually exclusive (no two options could both be defended as correct given the stem).
- [ ] Exactly one answer is unambiguously correct given standard DSM-5/clinical criteria as of your knowledge base — if a diagnosis is genuinely borderline between two options, revise the stem to remove the ambiguity rather than leaving it.

### 4.4 Stem-type / answer-type match check
- [ ] If the stem asks "most likely diagnosis," the correct answer is a diagnosis, not an action.
- [ ] If the stem asks "next step in management," the correct answer reflects the most conservative/safe/sequentially appropriate action — not necessarily the most definitive treatment.
- [ ] If the stem asks "next step in diagnosis," the correct answer is a test/workup, not a treatment.
- [ ] Communication/ethics items follow the hierarchy: validate/acknowledge → assess safety directly → address patient before third parties (unless patient is a minor/incompetent).

### 4.5 NBOME-specific checks (skip if writing pure NBME-style)
- [ ] If a structural/OMM finding is used, it is being used correctly — either as confirmatory evidence for a viscerosomatic-adjacent process OR explicitly as a rule-out for a somatic/musculoskeletal cause. It should never be decorative.
- [ ] If neuroanatomic distractors are used, at least one is a genuine, correct neuroscience correlate for a *different* diagnosis than the correct answer (real teaching value), and at most one or two are cranial/OMM-vocabulary-plausible-but-wrong.
- [ ] Duration arithmetic is internally consistent and precise enough to function as a real constraint, not just color.
- [ ] Question stem phrasing is folded into the final sentence where appropriate, matching NBOME's inline style.

### 4.6 Fidelity checks (house standards — carried over from existing pipeline)
- [ ] Answer-length bias correction applied (matches existing quiz-bank programmatic validation standard: correct answer is never uniquely shortest or longest).
- [ ] If this item is meant for a specific professor's style guide (e.g., Willard), cross-check against that guide's vignette skeleton and distractor architecture before finalizing.
- [ ] If pharmacology content, diction matches Professor Ly's style, not Ferland's.
- [ ] No real, identifiable patient information; all names/details fictional.

### 4.7 Final gate statement

> **If any box above is unchecked, the item is not ready. Fix it before it leaves this file/response. Never present an item that hasn't passed Section 4 in full, and never tell the user "here's a draft, let me know what you think" as a substitute for actually finishing the quality pass yourself first.**

---

## 5. QUICK-REFERENCE: WHEN TO USE WHICH PROFILE

| Signal in source material | Use profile |
|---|---|
| Straight DSM-5 differential, lab-value-as-clue, USMLE-style phrasing | NBME |
| OMM/structural exam findings relevant, cranial concepts, forensic psychiatry, Willard-style content | NBOME |
| Mixed/unclear | Default to NBME skeleton, but ask if osteopathic content should be layered in |

---

*End of guide. Update this file as new item patterns are identified from additional NBME/NBOME sample sets.*
