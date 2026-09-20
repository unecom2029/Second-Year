# Key Findings — vignette highlights for Hardest Exam questions 141–154 (batch H8).
# Authoring rules and categories: see highlights_hardest_001_030.py and QUIZ_BUILD_METHOD.md.

F, M, T, P, W = "finding", "mechanism", "term", "pattern", "workup"
EYEBROW = {F: "FINDING", M: "MECHANISM", T: "KEY TERM", P: "PATTERN", W: "WHAT'S ASKED"}


def h(text, cat, title, body):
    return {"text": text, "cat": cat, "eyebrow": EYEBROW[cat], "title": title, "body": body}


HIGHLIGHTS = {

141: [
 h("she has worn a walking boot on the right foot for plantar fasciitis, and 2 days ago she made a "
   "9-hour bus trip", M, "Stasis — one corner of Virchow's triad",
   "Virchow's triad (1856): endothelial injury, stasis and hypercoagulability. Immobilization of "
   "the leg and prolonged sitting both slow venous return in the calf, where most DVTs begin."),
 h("The swelling persists when she removes the boot and elevates the leg", P,
   "Elevation separates the edemas",
   "Venous insufficiency improves with elevation and recumbency. DVT and lymphedema do not. The "
   "stem also removes the boot as a mechanical explanation."),
 h("Her sister died of a 'blood clot' at age 33", F, "A first-degree relative with VTE",
   "A first-degree family history carries 2–4 times higher odds of venous thrombosis and raises "
   "the question of inherited thrombophilia — to be revisited after the acute episode, not tested "
   "for now."),
 h("the right calf measures 42 cm in circumference compared with 38 cm on the left, measured 10 cm "
   "below the tibial tuberosity", W, "A Wells item, measured properly",
   "Calf swelling more than 3 cm compared with the other leg scores a point, and it must be measured "
   "at a fixed landmark — 10 cm below the tibial tuberosity — to be reproducible. Asymmetric calf "
   "swelling of 2 cm or more has a positive likelihood ratio of about 2.1."),
 h("There is no erythema, fluctuance or popliteal fullness", P, "The alternatives are closed off",
   "No redness or fever against cellulitis; no popliteal fullness against a ruptured Baker cyst "
   "(pseudothrombophlebitis). The Wells item 'alternative diagnosis at least as likely' subtracts "
   "2 points — so ruling alternatives out keeps the score high."),
 h("Which of the following is the most appropriate next step in diagnosis?", W,
   "Probability → D-dimer → imaging",
   "The three-step sequence. At HIGH pretest probability the middle step is skipped: a negative "
   "D-dimer could not exclude a clot this likely, so it would not change anything. Go straight to "
   "compression ultrasonography."),
],

142: [
 h("after a weekend of heavy gardening", P, "An alternative explanation",
   "Muscle strain after unaccustomed exertion is a plausible alternative diagnosis, which is part "
   "of why his Wells score is low."),
 h("His Modified Wells score for deep vein thrombosis is 0", W, "Low pretest probability",
   "This is the precondition for using a D-dimer at all. D-dimer is best used when probability is "
   "low to moderate, and should not be ordered when thrombosis is not clinically suspected."),
 h("D-dimer 590 ng/mL FEU", F, "Positive by the standard cut-off only",
   "Above the manufacturer's dichotomous cut-off of 500 ng/mL — but that cut-off was not designed "
   "for a 68-year-old."),
 h("A 68-year-old man", M, "Age raises D-dimer physiologically",
   "D-dimer rises with age, which lowers its specificity after 50. The AGE-ADJUSTED threshold is "
   "age × 10 ng/mL FEU — 680 for him. His 590 is below it, a negative result, and DVT is excluded "
   "without imaging. Age adjustment improved specificity by about 9.5%."),
],

143: [
 h("sharp right posterior chest pain on inspiration", F, "Pleuritic chest pain",
   "With unilateral leg swelling, pleuritic pain points to pulmonary embolism from a DVT — though "
   "myocardial infarction, pericarditis, aortic dissection, pneumonia and pneumothorax stay on the "
   "differential."),
 h("pulse is 110/min", P, "One PERC criterion fails",
   "The PE rule-out criteria require a heart rate below 100/min. Tachycardia — together with "
   "unilateral leg swelling — means PERC cannot be used to exclude embolism, and PERC applies only "
   "when clinical probability is already low anyway."),
 h("blood pressure is 116/76 mm Hg", W, "Hemodynamically stable",
   "Refractory hypotension would suggest a massive PE with obstructive shock and change the "
   "approach entirely. Stability means she can go to the CT scanner."),
 h("oxygen saturation is 93% on room air", F, "Hypoxemia with a widened gradient",
   "In the case, PaO2 was 68 mm Hg with an alveolar-arterial gradient of 30–34 mm Hg, against an "
   "expected 10–11 at her age — ventilation-perfusion mismatch. Neither hypoxemia nor hypocapnia "
   "discriminates reliably, which is why a blood gas is not a diagnostic step."),
 h("A pregnancy test is negative", W, "Cleared for contrast CT",
   "Pregnancy would change the imaging choice. With it excluded, CT pulmonary angiography is the "
   "study of choice — about 94% sensitive, rarely inconclusive, and able to show an alternative "
   "diagnosis."),
 h("An ECG is shown", T, "S1Q3T3 — McGinn-White sign",
   "A deep S wave in lead I, Q wave and T-wave inversion in lead III, plus anterior T-wave "
   "inversion: acute right ventricular strain. Present in only 15%–25% of PE; sinus tachycardia is "
   "commoner, and the ECG is normal in 9%–30%."),
],

144: [
 h("He has never had pain crises, jaundice, hospitalizations or transfusions", P,
   "Clinically silent",
   "No vaso-occlusion, no hemolysis, no transfusion history. Whatever the electrophoresis shows, "
   "this is not someone with sickle cell disease."),
 h("His parents are healthy and know of no blood disorder in the family", P,
   "Carriers usually do not know",
   "Because sickle cell trait is asymptomatic, carrier parents frequently have no idea. A negative "
   "family history does not argue against a carrier state."),
 h("Hemoglobin A 57%", W, "HbA present, and the larger fraction",
   "The rule: the presence and size of the HbA fraction tells you how many normal beta-globin "
   "genes there are. HbA present and larger than HbS means one normal gene — trait."),
 h("Hemoglobin S 40%", F, "Below 50%, as expected in trait",
   "In trait HbS runs roughly 35%–45%, because normal beta chains pair with alpha chains slightly "
   "more efficiently. HbS EXCEEDING HbA would point to HbS/beta-plus thalassemia instead."),
 h("Mean corpuscular volume 87 µm3", W, "Normal indices exclude the thalassemia compounds",
   "HbS/beta-thalassemia is microcytic with a raised HbA2. Normal indices and a normal A2 remove it."),
],

145: [
 h("four hospitalizations for vaso-occlusive pain in the past year and one episode of acute chest "
   "syndrome", W, "The indications for hydroxyurea",
   "Frequent painful episodes, severe symptomatic anemia, acute chest syndrome or other severe "
   "vaso-occlusive complications. He meets two."),
 h("Hemoglobin A 0%", F, "No normal beta-globin gene",
   "HbS 86% with no HbA means homozygous disease (HbSS), not trait."),
 h("Hemoglobin F 11%", M, "The protective fraction",
   "Fetal hemoglobin (alpha2 gamma2) uses gamma chains, which carry no sickle mutation and cannot "
   "join the HbS polymer. His residual 11% already dilutes the HbS in each cell — hydroxyurea's job "
   "is to raise it further. 'You are diluting the polymer.'"),
 h("Hydroxyurea is started", T, "A chemotherapy drug with two boxed warnings",
   "Myelosuppression — so blood counts are monitored — and secondary malignancy. Start 15 mg/kg once "
   "daily."),
],

146: [
 h("She is RhD negative", F, "The mother lacks the antigen",
   "D is foreign to a D-negative woman, so exposure to D-positive fetal cells can provoke anti-D."),
 h("she did not receive anti-D immune globulin during or after that pregnancy", M,
   "The missed prevention",
   "Anti-D immune globulin clears D-positive fetal cells from the mother's circulation before she "
   "can mount her own response. Without it she was sensitized at her first delivery — and that first "
   "child was unaffected."),
 h("At 14 hours of age the infant is visibly jaundiced", P, "Jaundice in the first 24 hours",
   "Never physiologic. Physiologic jaundice appears after 24 hours and does not cause anemia."),
 h("the liver and spleen are palpable", M, "The site of destruction",
   "IgG-coated red cells are removed by macrophages in the spleen and liver — predominantly "
   "EXTRAVASCULAR hemolysis — and both organs also take on extramedullary hematopoiesis."),
 h("the direct antiglobulin test is positive", W, "Antibody is on the infant's cells",
   "Proves immune destruction and excludes non-immune neonatal hemolysis such as G6PD deficiency or "
   "hereditary spherocytosis, where the test is negative."),
],

147: [
 h("She undergoes leukapheresis, and 5 weeks later she receives a single infusion", M,
   "Collect, engineer, expand, re-infuse",
   "The five-week gap is manufacturing: her own T cells are collected, a chimeric antigen receptor "
   "gene is inserted outside the body, and the cells are grown to large numbers before return. A "
   "bispecific antibody, by contrast, is an off-the-shelf drug with no collection step."),
 h("directed against B-cell maturation antigen (BCMA)", T, "The myeloma target",
   "BCMA is expressed at high levels on myeloma cells. CD19 is the target for B-cell lymphomas and "
   "B-lymphoblastic leukemia."),
 h("she develops fever and hypotension that respond to tocilizumab", F,
   "Cytokine release syndrome",
   "The commonest reaction to CAR T cells and T-cell engagers, driven by interleukin-6 — hence the "
   "anti-IL-6 receptor antibody tocilizumab."),
 h("Which of the following best describes how this therapy recognizes and kills the myeloma cells?",
   W, "Recognition without MHC",
   "The receptor's binding domain comes from an antibody, so it binds the antigen directly on the "
   "cell surface — no MHC presentation needed. That is what lets engineered T cells kill tumour "
   "cells that hide from ordinary T-cell recognition."),
],

148: [
 h("tumour cells that strongly express programmed death-ligand 1 (PD-L1)", M,
   "The tumour's 'stop' signal",
   "PD-L1 engages PD-1 on T cells and switches them off — the major immune resistance mechanism in "
   "tumours."),
 h("CD8 T lymphocytes that express high levels of programmed cell death protein 1 (PD-1) but show "
   "little cytotoxic activity", F, "Present but exhausted",
   "The T cells have reached the tumour and been silenced there. Checkpoint blockade works on "
   "exactly these cells — it does not bring new ones."),
 h("his thyroid-stimulating hormone is elevated", P, "Benefit and harm share a mechanism",
   "PD-1 also restrains autoreactive T cells. Releasing it causes immune-related adverse events — "
   "thyroiditis here, colitis in question 88."),
 h("Which of the following best describes the mechanism of this drug?", W, "Which side of the checkpoint",
   "PD-1 (on the T cell): pembrolizumab, nivolumab, cemiplimab. PD-L1 (on the tumour): "
   "atezolizumab, avelumab, durvalumab. CTLA-4 (priming): ipilimumab."),
],

149: [
 h("genetically modified to replicate selectively in tumour cells", M, "Direct oncolysis",
   "The virus replicates in, and bursts, tumour cells with defective antiviral defences — which "
   "explains regression of the INJECTED lesions."),
 h("to express granulocyte-macrophage colony-stimulating factor (GM-CSF)", M,
   "Recruiting the antigen-presenting cells",
   "GM-CSF is not cytotoxic. It recruits and matures dendritic cells, which carry released tumour "
   "antigens to the draining nodes to prime T cells."),
 h("Several lesions on the thigh that were never injected also regress", P,
   "The effect travels without the virus",
   "Regression at sites the virus never reached cannot be oncolysis. It is systemic immunity."),
 h("a dense infiltrate of CD8 T lymphocytes", W, "The evidence for the mechanism",
   "Tumour-specific cytotoxic T cells primed by the injected lesions are now attacking melanoma "
   "elsewhere — an 'in-situ vaccine'. Note: oncolytic virus therapy is not in the review file; this "
   "follows the tutor's high-yield definition."),
],

150: [
 h("Conditioning consisted of busulfan and cyclophosphamide", W, "Two alkylators, two organs",
   "Match organ to drug: busulfan → lung (and skin). Cyclophosphamide → bladder (hemorrhagic "
   "cystitis from acrolein) and, at high dose, heart."),
 h("progressive dry cough and breathlessness on climbing stairs", F, "Insidious interstitial disease",
   "Months after exposure, a dry cough with exertional dyspnea is the pattern of drug-induced "
   "pulmonary fibrosis rather than an acute infection."),
 h("His skin has become diffusely darker since the transplant", T, "Busulfan hyperpigmentation",
   "A characteristic second effect of busulfan, and a helpful clue that points to the same drug as "
   "the lung disease."),
 h("Spirometry shows a restrictive pattern with a reduced diffusing capacity for carbon monoxide", F,
   "Restriction with a falling DLCO",
   "The physiological signature of interstitial fibrosis. The diffusing capacity is the earliest "
   "measurable change and is what pulmonary function surveillance looks for."),
 h("Bronchoalveolar lavage shows no organisms", P, "Infection excluded first",
   "In any transplant recipient, infection is the main alternative and must be ruled out before a "
   "drug toxicity is accepted. He also has no rash, diarrhea or jaundice against graft-versus-host "
   "disease."),
],

151: [
 h("managed with observation and a single course of therapy 3 years ago, with stable small nodes "
   "since", P, "Years of indolence",
   "Chronic lymphocytic leukemia is a grow-slow disease. What matters in this stem is the abrupt "
   "change of tempo."),
 h("3 weeks of a rapidly enlarging lump in the left axilla, fevers, drenching night sweats and 5 kg "
   "of weight loss", F, "One node outgrowing the rest, with B symptoms",
   "A single rapidly enlarging mass while the other nodes stay unchanged is the clinical signature "
   "of transformation. Biopsy the fastest-growing site."),
 h("Lactate dehydrogenase 910 U/L", F, "High cell turnover",
   "A sharply rising lactate dehydrogenase reflects a newly aggressive, rapidly proliferating "
   "population."),
 h("diffuse sheets of large B cells with vesicular nuclei and prominent nucleoli, replacing the "
   "small lymphocytes", W, "Richter transformation",
   "Diffuse large B-cell lymphoma arising from CLL/SLL, driven by newly acquired TP53 or MYC "
   "mutations. It occurs in 2%–9% and is usually fatal."),
],

152: [
 h("chemotherapy with bleomycin, etoposide and cisplatin", W, "Find the topoisomerase II inhibitor",
   "Of the three, only etoposide is leukemogenic. Bleomycin injures the lung; cisplatin the kidney, "
   "ear and nerves."),
 h("Four years ago", M, "Latency points to the drug class",
   "Topoisomerase II inhibitors cause therapy-related myeloid neoplasms after a short latency — "
   "typically 1–3 years, within a range of 1–10. Alkylating agents take 5–7 years."),
 h("Fibrinogen 90 mg/dL", F, "APL's coagulopathy",
   "Disseminated intravascular coagulation — low fibrinogen, very high D-dimer, mucocutaneous "
   "bleeding — the leading cause of early death in acute promyelocytic leukemia."),
 h("cytogenetics show t(15;17)", M, "A balanced translocation",
   "Topoisomerase II trapped mid-cut leaves double-strand breaks; mis-repair between two chromosomes "
   "produces balanced translocations like PML-RARA. Alkylator-related disease instead shows losses "
   "of chromosomes 5 or 7."),
],

153: [
 h("day 9 of induction with all-trans retinoic acid and arsenic trioxide", F, "Inside the window",
   "Differentiation syndrome occurs 2–21 days after starting therapy, in a quarter to a half of "
   "patients."),
 h("4 kg of weight gain with ankle edema", F, "Capillary leak",
   "Weight gain and edema, with effusions and pulmonary infiltrates, reflect maturing leukemic cells "
   "releasing cytokines and migrating into tissues."),
 h("bilateral pulmonary infiltrates with small bilateral pleural effusions", F, "Lungs and serosa",
   "Pulmonary infiltrates, hypoxemia and serositis — pleural or pericardial effusions — are core "
   "features."),
 h("His leukocyte count was 3,400/mm3 at diagnosis", P, "Hyperleukocytosis from maturation",
   "The rise from 3,400 to 31,000 is the companion phenomenon: leukemic cells maturing rapidly. A "
   "high count AT DIAGNOSIS is the main risk factor for the syndrome."),
 h("Blood cultures are drawn and broad-spectrum antibiotics started", W,
   "Cover infection, but treat the syndrome",
   "Sepsis looks identical and must be covered — but antibiotics do not replace dexamethasone. "
   "Retinoic acid and arsenic are held only temporarily in severe cases."),
],

154: [
 h("increased thirst and passing more urine", M, "Hypercalcemia on the kidney",
   "High calcium impairs urinary concentration — a nephrogenic diabetes insipidus effect — "
   "producing polyuria and polydipsia, and it causes constipation."),
 h("Anion gap 3 mEq/L", T, "A low anion gap",
   "A subtle, historic clue to IgG myeloma: IgG paraprotein is cationic, so it is an unmeasured "
   "cation that narrows the gap."),
 h("Alkaline phosphatase 74 U/L", W, "Normal — and that is the question",
   "Alkaline phosphatase sits on active osteoblasts and marks bone FORMATION. Myeloma lesions are "
   "purely 'clastic', so it stays normal despite extensive destruction."),
 h("The peripheral smear shows red cells stacked in long chains", T, "Rouleaux",
   "Paraprotein alters the red cell surface charge so cells stack like coins — the same process "
   "that drives the sedimentation rate above 100 mm/h."),
 h("A technetium bone scan obtained earlier by another clinician was reported as normal", P,
   "The wrong test for myeloma",
   "Bone scans image osteoblastic activity, which myeloma suppresses through DKK1 while activating "
   "osteoclasts via RANK ligand. Use skeletal survey, low-dose whole-body CT or MRI."),
],

}
