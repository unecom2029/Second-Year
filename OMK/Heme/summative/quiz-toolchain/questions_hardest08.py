# Hardest Exam — batch H8 (questions 141–154): the tutor's high-yield list, and the three CBL cases.
#
# A previous student's "Tutor High-Yield Review Points" list was checked against the first 140
# questions: 15 of 22 points were already tested, 5 were only partly covered and 2 appeared nowhere.
# This batch closes those gaps, sourced from the review file wherever it covers the point and from
# the three CBL cases Jeevs supplied (Jessica Turner — DVT/PE and the Wells score; Lisa Masterson —
# myeloma; Amir Islam — therapy-related APL). Oncolytic virus therapy (Q149) is in neither the
# review nor the cases; it is written from the tutor's own definition plus standard pharmacology.

Q = []


def q(stem, opts, correct, explanation, eli5, image=None, imcap=None, exim=None, excap=None):
    assert correct in opts, correct
    assert opts[correct] == "", "keyed option must carry an empty wrong-explanation"
    assert "Educational objective:" in explanation
    bodies = sorted(opts, key=str.lower)
    ci = bodies.index(correct)
    d = {
        "stem": stem,
        "choices": [f"{chr(65 + i)}. {b}" for i, b in enumerate(bodies)],
        "correct": ci,
        "explanation": explanation,
        "wrongExplanations": {str(i): opts[b] for i, b in enumerate(bodies) if i != ci},
        "eli5": eli5,
    }
    if image:
        d["image"] = image
        d["imageCaption"] = imcap
    if exim:
        d["explanationImage"] = exim
        d["explanationImageCaption"] = excap
    Q.append(d)


# ── 141. High pretest probability of DVT — skip the D-dimer (Jessica Turner case) ─────────────
q(
    "A 35-year-old woman comes to the emergency department due to 24 hours of swelling and aching "
    "of the right calf, ankle and foot. For the past 3 weeks she has worn a walking boot on the right "
    "foot for plantar fasciitis, and 2 days ago she made a 9-hour bus trip. The swelling persists "
    "when she removes the boot and elevates the leg. She has no chest pain or breathlessness. Her "
    "sister died of a 'blood clot' at age 33. Temperature is 37.1 C (98.8 F), pulse is 84/min and "
    "oxygen saturation is 99% on room air. The right leg shows pitting edema from the foot to the "
    "mid-thigh, and the right calf measures 42 cm in circumference compared with 38 cm on the left, "
    "measured 10 cm below the tibial tuberosity. There is tenderness along the course of the deep "
    "veins. There is no erythema, fluctuance or popliteal fullness.\n\n"
    "Which of the following is the most appropriate next step in diagnosis?",
    {
        "Compression ultrasonography of the right leg": "",
        "Contrast venography of the right leg":
            "Venography is the historical reference standard, but it is invasive, uses contrast and "
            "has been replaced by compression ultrasonography as the first-line test.",
        "CT pulmonary angiography":
            "There are no symptoms or signs of pulmonary embolism — no dyspnea, chest pain, "
            "tachycardia or hypoxemia. The question here is the leg.",
        "Quantitative D-dimer, with imaging only if elevated":
            "D-dimer is useful only when pretest probability is low to moderate, because its value "
            "is its NEGATIVE result. At high pretest probability a negative D-dimer would not "
            "exclude thrombosis, so it cannot change the decision to image.",
        "Thrombophilia testing before any imaging":
            "Thrombophilia testing does not diagnose a clot, and it is unreliable during an acute "
            "event and on anticoagulation. Whether to test at all is a later, shared decision.",
    },
    "Compression ultrasonography of the right leg",
    "The diagnostic sequence for suspected deep vein thrombosis has three steps, and this patient "
    "legitimately skips the middle one.\n\n"
    "1st — PRETEST PROBABILITY. The Modified Wells score for DVT is the most widely used and best "
    "validated decision rule in the outpatient setting. Here: calf swelling more than 3 cm larger "
    "than the other side, pitting edema confined to the symptomatic leg, localized tenderness along "
    "the deep venous system, and recent immobilization of the lower extremity — a score of at least 3, "
    "the HIGH-probability group (about 75% in the case discussion). No alternative diagnosis is as "
    "likely: no erythema or fever to suggest cellulitis, no popliteal fullness to suggest a ruptured "
    "Baker cyst, and swelling that does NOT improve with elevation, unlike venous insufficiency.\n\n"
    "2nd — D-DIMER, but only at low or moderate probability. It is highly sensitive and poorly "
    "specific, so its value is a negative result that rules thrombosis out. At high probability it "
    "cannot do that, so it is not ordered.\n\n"
    "3rd — IMAGING. Compression ultrasonography is first line: a noncompressible vein, directly "
    "visualized thrombus with venous dilation, and abnormal Doppler flow. Sensitivity is about 94% "
    "and specificity about 98% for proximal DVT. It may be equivocal for pelvic veins and misses "
    "May-Thurner syndrome, where CT or MR venography is needed.\n\n"
    "Her risk factors fill Virchow's triad: STASIS from the boot and the long bus journey, and a "
    "possible HYPERCOAGULABLE state suggested by a first-degree relative with fatal thrombosis — "
    "which carries a 2–4 times higher odds of venous thrombosis.\n\n"
    "Educational objective: The diagnosis of DVT begins with pretest probability (Modified Wells "
    "score). D-dimer is used only when probability is low or moderate, to rule thrombosis out; at "
    "high probability, proceed directly to compression ultrasonography.",
    "Everything about her story already makes a clot very likely. The blood test (D-dimer) is only "
    "good at telling you a clot is NOT there, and it cannot do that for someone this likely to have "
    "one — so you skip it and go straight to the ultrasound, which can actually see the clot.",
)

# ── 142. The age-adjusted D-dimer (Jessica Turner case) ───────────────────────────────────────
q(
    "A 68-year-old man comes to the office due to 2 days of mild aching in the left calf that began "
    "after a weekend of heavy gardening. He has no swelling, chest pain or breathlessness, no recent "
    "surgery or travel, no cancer and no previous thrombosis. Vital signs are normal. The left calf "
    "is mildly tender over the medial gastrocnemius; calf circumferences are equal, and there is no "
    "edema or venous distension. His Modified Wells score for deep vein thrombosis is 0.\n\n"
    "Laboratory studies show:\n"
    "D-dimer 590 ng/mL FEU (N=<500 ng/mL FEU)\n"
    "Creatinine 0.9 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "Which of the following is the most appropriate next step?",
    {
        "No imaging; the D-dimer is below his age-adjusted cutoff": "",
        "Compression ultrasonography of the left leg":
            "This would be the next step if the D-dimer were positive — but interpreted correctly for "
            "his age, it is not. Imaging here would be unnecessary.",
        "Empirical apixaban while awaiting ultrasonography":
            "Empirical anticoagulation is for patients with a high probability of thrombosis and a "
            "delay to imaging. This patient has neither.",
        "Repeat the D-dimer in 1 week":
            "Serial D-dimer testing does not resolve anything here. The first result, read against "
            "the right threshold, already answers the question.",
        "Whole-leg ultrasonography with CT pulmonary angiography":
            "There are no features of pulmonary embolism at all, and a low-probability patient with "
            "a negative D-dimer needs no imaging of either kind.",
    },
    "No imaging; the D-dimer is below his age-adjusted cutoff",
    "D-dimer is a degradation product of CROSS-LINKED fibrin. Generating it takes three enzymes — "
    "thrombin to form fibrin, activated factor XIII to cross-link it, and plasmin to break it down — "
    "so a raised level means clot has formed and been lysed somewhere. That makes it highly SENSITIVE "
    "and poorly SPECIFIC, which dictates how it is used: its value is a NEGATIVE result, in a patient "
    "whose pretest probability is low or moderate.\n\n"
    "D-dimer also rises physiologically with AGE, so the conventional 500 ng/mL cut-off loses "
    "specificity in older patients and generates unnecessary imaging. The AGE-ADJUSTED threshold for "
    "patients over 50 is:\n\n"
    "age × 10 ng/mL (fibrinogen equivalent units)\n\n"
    "For this 68-year-old the threshold is 680 ng/mL. His value of 590 is BELOW it — a negative "
    "result. With a Wells score of 0 (low probability), deep vein thrombosis is excluded without "
    "imaging. Age adjustment improved specificity by about 9.5% without an increase in missed events, "
    "and the ADJUST-PE study showed a 0.3% rate of subsequent embolism when it was combined with a low "
    "clinical probability.\n\n"
    "Two caveats from the case: the strategy is less reliable in patients with cancer, and it must be "
    "paired with a formal low pretest probability — D-dimer should not be ordered when thrombosis is "
    "not clinically suspected at all. Other conditions that raise D-dimer include pregnancy, "
    "infection, inflammation, recent surgery or trauma, malignancy and disseminated intravascular "
    "coagulation.\n\n"
    "Educational objective: In a patient older than 50 with low pretest probability, interpret "
    "D-dimer against an age-adjusted threshold of age × 10 ng/mL FEU. A value below that threshold "
    "excludes venous thromboembolism without imaging.",
    "The clot test naturally drifts upward as people get older, so the usual cut-off flags too many "
    "healthy older people. The fix is to use his age times ten as the cut-off. For him that is 680, "
    "and he is at 590 — so it is actually a normal result and he does not need a scan.",
)

# ── 143. Suspected PE with high pretest probability — straight to CTPA (Jessica Turner case) ───
q(
    "A 35-year-old woman is being evaluated in the emergency department for 24 hours of right leg "
    "swelling after 3 weeks in a walking boot and a 9-hour bus trip. Since this morning she has "
    "become short of breath with minimal exertion and has sharp right posterior chest pain on "
    "inspiration, with palpitations. Temperature is 37.1 C (98.8 F), blood pressure is 116/76 mm Hg, "
    "pulse is 110/min, respirations are 22/min and oxygen saturation is 93% on room air. The lungs "
    "are clear and there is no pleural rub. The right leg is swollen from foot to mid-thigh. A "
    "pregnancy test is negative. An ECG is shown.\n\n"
    "Which of the following is the most appropriate next step in diagnosis?",
    {
        "CT pulmonary angiography": "",
        "Apply the PE rule-out criteria":
            "The PE rule-out criteria (PERC) are used only when clinical pretest probability is "
            "already low, below about 15%. Her heart rate above 100/min and unilateral leg swelling "
            "each fail a criterion — and her probability is high, so PERC does not apply at all.",
        "Planar ventilation-perfusion scanning":
            "An alternative when CT angiography is contraindicated, but it is less sensitive for "
            "acute embolism (56%–98%) and cannot identify alternative diagnoses such as pneumonia or "
            "effusion.",
        "Quantitative D-dimer":
            "At high pretest probability a negative D-dimer would not exclude embolism, so it cannot "
            "change the decision to image. The case discussion states explicitly that D-dimer is not "
            "indicated here.",
        "Transthoracic echocardiography":
            "Echocardiography assesses right ventricular function for risk stratification once the "
            "diagnosis is made, or at the bedside in a patient too unstable to scan. It is not the "
            "diagnostic test in a hemodynamically stable patient.",
    },
    "CT pulmonary angiography",
    "Pulmonary embolism secondary to a right leg DVT, with HIGH pretest probability. The same "
    "three-step sequence applies as for DVT — probability, then D-dimer only if probability is low "
    "or moderate, then imaging.\n\n"
    "PROBABILITY. The two validated rules are the Wells criteria for PE (7 items, including the "
    "clinician's judgement that PE is the most likely diagnosis) and the Revised Geneva score "
    "(8 objective items, no subjective element). In the case she scores 7.5–9 on Wells and 12 on "
    "Revised Geneva — high risk on both. The item in the Wells score asking whether an alternative "
    "diagnosis is as likely as PE is the one most predictive of a negative work-up.\n\n"
    "IMAGING. CT pulmonary angiography is the study of choice: sensitivity for an intraluminal "
    "filling defect of about 94%, a low rate of inconclusive results, and the ability to show "
    "alternative diagnoses such as pneumonia or effusion.\n\n"
    "The ECG supports the diagnosis without making it. It shows sinus tachycardia, a prominent S "
    "wave in lead I with a Q wave and T-wave inversion in lead III — the S1Q3T3 pattern (McGinn-White "
    "sign) — and T-wave inversion across the anterior leads. S1Q3T3 reflects acute right ventricular "
    "strain (acute cor pulmonale) and appears in only 15%–25% of patients with PE. Sinus tachycardia "
    "is the commonest finding, and a completely normal ECG occurs in 9%–30%.\n\n"
    "The arterial blood gas in the case shows a PaO2 of 68 mm Hg with a widened alveolar-arterial "
    "gradient of 30–34 mm Hg — the expected gradient at age 35 is about 10–11 — from "
    "ventilation-perfusion mismatch. Neither hypoxemia nor hypocapnia discriminates reliably, "
    "though, which is why the blood gas is not a diagnostic step.\n\n"
    "Educational objective: When suspected pulmonary embolism has high pretest probability by the "
    "Wells or Revised Geneva score, proceed directly to CT pulmonary angiography. D-dimer and the PE "
    "rule-out criteria apply only when probability is low.",
    "Her leg clot has most likely broken off and travelled to her lungs, and her score says that is "
    "very likely. When a clot is that likely, you do not waste time on tests designed to rule it "
    "out — you go straight to the CT scan that can actually show it.",
    image="fig_hx_pe_ecg",
    imcap="12-lead ECG on arrival",
)

# ── 144. Reading a sickle electrophoresis — trait versus disease ─────────────────────────────
q(
    "A 19-year-old college soccer player undergoes a preparticipation evaluation. He has never had "
    "pain crises, jaundice, hospitalizations or transfusions and is in excellent health. His "
    "parents are healthy and know of no blood disorder in the family. Examination is normal, with no "
    "splenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 14.9 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 45% (N=41%–53%)\n"
    "Mean corpuscular volume 87 µm3 (N=80–100 µm3)\n"
    "Reticulocyte count 1.0% (N=0.5%–1.5%)\n"
    "Hemoglobin A 57% (N=95%–98%)\n"
    "Hemoglobin S 40% (N=0%)\n"
    "Hemoglobin A2 2.8% (N=1.5%–3.5%)\n"
    "Hemoglobin F 0.2% (N=<2%)\n\n"
    "Which of the following best describes this patient's genotype?",
    {
        "Heterozygous: one sickle and one normal beta-globin gene": "",
        "Compound heterozygous for hemoglobin S and hemoglobin C":
            "HbSC disease would show a hemoglobin C band in roughly equal proportion to hemoglobin S, "
            "and NO hemoglobin A at all, because neither beta-globin gene is normal.",
        "Compound heterozygous for hemoglobin S and beta-plus thalassemia":
            "HbS/beta-plus thalassemia does produce some hemoglobin A, but HbS EXCEEDS HbA, the "
            "hemoglobin A2 is raised and the cells are microcytic. Here HbA is the larger fraction and "
            "the indices are normal.",
        "Compound heterozygous for hemoglobin S and beta-zero thalassemia":
            "Beta-zero thalassemia makes no beta chains, so like homozygous sickle cell disease there "
            "would be NO hemoglobin A — plus microcytosis and a raised hemoglobin A2.",
        "Homozygous for the sickle allele":
            "Homozygous sickle cell disease produces no normal beta chains, so hemoglobin A is absent "
            "and hemoglobin S makes up roughly 85%–95%, with some hemoglobin F.",
    },
    "Heterozygous: one sickle and one normal beta-globin gene",
    "Sickle cell TRAIT (HbAS). The electrophoresis answers the question by one rule: the presence "
    "and size of the HEMOGLOBIN A fraction tells you how many normal beta-globin genes there are.\n\n"
    "• HbA present and LARGER than HbS (about 55%–60% A, 35%–45% S), normal indices → TRAIT. One "
    "normal gene. HbA exceeds HbS because normal beta chains associate with alpha chains slightly "
    "more efficiently.\n"
    "• HbA ABSENT, HbS about 85%–95%, some HbF → homozygous sickle cell DISEASE (HbSS). The review's "
    "worked example: HbS 85%, HbF 12%, HbA 0%.\n"
    "• HbA absent with a hemoglobin C band → HbSC.\n"
    "• HbA present but SMALLER than HbS, with raised A2 and microcytosis → HbS/beta-plus "
    "thalassemia.\n"
    "• HbA absent, raised A2, microcytosis → HbS/beta-zero thalassemia.\n\n"
    "His normal hemoglobin, indices and reticulocyte count fit trait, which is asymptomatic under "
    "ordinary conditions. And his parents' ignorance of any blood disorder is exactly what the "
    "review predicts: because sickle cell trait is silent, carrier parents frequently do not know. "
    "The practical importance of the diagnosis is genetic — two trait carriers have a 1-in-4 chance "
    "with each pregnancy of a child with sickle cell disease.\n\n"
    "Educational objective: On hemoglobin electrophoresis, sickle cell trait shows hemoglobin A "
    "present and larger than hemoglobin S (roughly 60:40) with normal red cell indices. Absent "
    "hemoglobin A indicates that neither beta-globin gene is normal — homozygous disease or a "
    "compound heterozygote.",
    "The test measures how much normal hemoglobin he makes. He still makes more normal hemoglobin "
    "than the sickle kind, which means he got one normal gene and one sickle gene — a carrier, not "
    "someone with the disease. Someone with the disease makes no normal hemoglobin at all.",
)

# ── 145. Why hydroxyurea works in sickle cell disease ─────────────────────────────────────────
q(
    "An 11-year-old boy with sickle cell disease is brought to the office for follow-up. He has had "
    "four hospitalizations for vaso-occlusive pain in the past year and one episode of acute chest "
    "syndrome. He takes folic acid and daily penicillin was stopped at age 5.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.1 g/dL (N=11.5–15.5 g/dL)\n"
    "Hematocrit 24% (N=35%–45%)\n"
    "Reticulocyte count 11% (N=0.5%–1.5%)\n"
    "Hemoglobin S 86% (N=0%)\n"
    "Hemoglobin F 11% (N=<2%)\n"
    "Hemoglobin A 0% (N=95%–98%)\n\n"
    "Hydroxyurea is started. Which of the following best explains its principal benefit in this "
    "patient?",
    {
        "Induction of gamma chains that dilute the HbS polymer": "",
        "Chelation of iron accumulated from previous transfusions":
            "That is the role of deferasirox or deferoxamine in chronically transfused patients. "
            "Hydroxyurea has no chelating activity.",
        "Correction of the beta-globin mutation in hematopoietic stem cells":
            "Correcting or bypassing the defect in stem cells is what gene therapy does — including "
            "CRISPR-based editing of BCL11A, the switch that silences fetal hemoglobin after birth. "
            "Hydroxyurea is a drug, not a gene edit.",
        "Increased synthesis of hemoglobin A2 to replace hemoglobin S":
            "Hemoglobin A2 (alpha2 delta2) is a minor fraction that hydroxyurea does not "
            "meaningfully raise. The fraction it increases is hemoglobin F.",
        "Irreversible inhibition of platelet cyclooxygenase-1":
            "That is aspirin. Vaso-occlusion in sickle cell disease is driven by polymerized "
            "hemoglobin S deforming red cells, not by platelet aggregation.",
    },
    "Induction of gamma chains that dilute the HbS polymer",
    "Hydroxyurea is the disease-modifying mainstay of sickle cell disease, and it works by turning "
    "FETAL HEMOGLOBIN back on.\n\n"
    "The mechanism in one line from the review: hydroxyurea raises HbF, and HbS polymerizes poorly "
    "with HbF — 'you are diluting the polymer.' Fetal hemoglobin (alpha2 gamma2) uses gamma chains "
    "rather than beta chains, so it carries no sickle mutation, and gamma chains cannot participate "
    "in the HbS polymer. Every molecule of HbF in a red cell dilutes the HbS within it, slowing "
    "polymerization so that more cells traverse the microcirculation before they sickle.\n\n"
    "This is the same biology that explains two other things. It is why sickle cell disease does not "
    "present at birth — the newborn's red cells are still mostly HbF, and symptoms emerge only as "
    "gamma-chain production switches off over the first months. And it is why this patient's own "
    "residual HbF of 11% is protective; raising it further is exactly the aim.\n\n"
    "Indications: frequent painful episodes, severe symptomatic anemia, acute chest syndrome or "
    "other severe vaso-occlusive complications — this patient meets several. The starting dose is "
    "15 mg/kg once daily. It is a chemotherapy agent with two boxed warnings: MYELOSUPPRESSION, "
    "requiring blood count monitoring, and secondary malignancy.\n\n"
    "Educational objective: Hydroxyurea reduces vaso-occlusive crises and acute chest syndrome in "
    "sickle cell disease by increasing fetal hemoglobin, which does not copolymerize with "
    "hemoglobin S. Its principal toxicity is myelosuppression.",
    "The medicine switches back on the baby form of hemoglobin, which everyone makes before birth. "
    "Baby hemoglobin does not have the sickle fault and gets in the way of the sickle hemoglobin "
    "sticking together — so fewer cells bend into sickles and block blood vessels.",
)

# ── 146. Hemolytic disease of the fetus and newborn ───────────────────────────────────────────
q(
    "A 29-year-old woman, gravida 2 para 1, delivers a boy at 37 weeks' gestation. She is RhD "
    "negative. Her first child, born 3 years ago in another country, was RhD positive, and she did "
    "not receive anti-D immune globulin during or after that pregnancy. At 14 hours of age the "
    "infant is visibly jaundiced and pale, and the liver and spleen are palpable.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 10.2 g/dL (N=14.0–22.0 g/dL)\n"
    "Hematocrit 31% (N=42%–65%)\n"
    "Reticulocyte count 12% (N=3%–7%)\n"
    "Bilirubin, total 11.6 mg/dL (N=<6.0 mg/dL)\n"
    "Bilirubin, direct 0.5 mg/dL (N=0.0–0.4 mg/dL)\n\n"
    "The infant is RhD positive and the direct antiglobulin test is positive. Which of the "
    "following best describes how this infant's red cells are being destroyed?",
    {
        "Macrophage removal of IgG-coated cells in spleen and liver": "",
        "Complement-mediated lysis of red cells within the circulation":
            "That is the mechanism of an ABO-incompatible transfusion, driven by IgM that fixes "
            "complement efficiently. Anti-D is an IgG alloantibody and produces extravascular "
            "destruction.",
        "Maternal IgM anti-D antibodies crossing the placenta":
            "IgM is a pentamer and cannot cross the placenta. Only IgG is transported across, which "
            "is why the first sensitizing exposure produces no disease and a later IgG response "
            "does.",
        "Oxidative injury in a neonate with G6PD deficiency":
            "G6PD deficiency can cause neonatal jaundice, but the direct antiglobulin test would be "
            "NEGATIVE, because no antibody is involved.",
        "Physiologic breakdown of fetal hemoglobin after birth":
            "Physiologic jaundice appears after 24 hours, does not cause anemia or a high "
            "reticulocyte count, and never produces a positive direct antiglobulin test.",
    },
    "Macrophage removal of IgG-coated cells in spleen and liver",
    "Hemolytic disease of the fetus and newborn (HDFN) from anti-D alloimmunization.\n\n"
    "The sequence, as the review sets it out for RhD:\n\n"
    "1. A D-negative woman is exposed to D-positive red cells — here at the delivery of her first "
    "D-positive child. D is foreign to her, so she forms anti-D. That first pregnancy is unaffected, "
    "because the response comes too late and begins as IgM.\n"
    "2. The next exposure is the problem. Her anti-D is now IgG, and IgG crosses the placenta.\n"
    "3. If the next fetus is D positive, maternal IgG anti-D coats its red cells, and the fetal "
    "spleen and liver remove them — PREDOMINANTLY EXTRAVASCULAR hemolysis, the characteristic "
    "pattern of an IgG alloantibody.\n\n"
    "The findings follow from that mechanism. Anemia with a brisk reticulocytosis shows destruction "
    "with a responding marrow. Hepatosplenomegaly reflects both the macrophage workload and "
    "extramedullary hematopoiesis. The bilirubin is UNCONJUGATED — heme from destroyed cells, which "
    "the placenta cleared before birth and the immature neonatal liver now cannot — and it appears "
    "within the first 24 hours, which is never physiologic. The positive direct antiglobulin test "
    "proves antibody is on the infant's red cells. In severe cases the fetus develops hydrops in "
    "utero.\n\n"
    "Prevention is the point of the story: anti-D immune globulin given to a D-negative mother "
    "during pregnancy and after delivery of a D-positive infant clears fetal cells before she can "
    "mount her own response. It is also why blood banks save RhD-negative units for girls and "
    "women of childbearing potential.\n\n"
    "Educational objective: In hemolytic disease of the fetus and newborn, maternal IgG "
    "alloantibody crosses the placenta and coats fetal red cells, which are destroyed predominantly "
    "extravascularly by the spleen and liver. Sensitization occurs at a prior exposure, and anti-D "
    "immune globulin prevents it.",
    "Mum's body learned to attack the baby's blood type during her first birth. This time her "
    "antibodies crossed over to the baby and stuck to his red cells like labels, and his spleen and "
    "liver have been pulling the labelled cells out — which is why he is pale, yellow and has a big "
    "liver and spleen.",
)

# ── 147. What CAR T-cell therapy actually is (Lisa Masterson case) ────────────────────────────
q(
    "A 58-year-old woman with IgG kappa multiple myeloma has relapsed after three lines of therapy, "
    "including a proteasome inhibitor, an immunomodulatory drug and an anti-CD38 monoclonal "
    "antibody. She undergoes leukapheresis, and 5 weeks later she receives a single infusion of "
    "ciltacabtagene autoleucel, a product directed against B-cell maturation antigen (BCMA), which "
    "is expressed at high levels on myeloma cells. Two days later she develops fever and "
    "hypotension that respond to tocilizumab. Three months later her monoclonal protein is "
    "undetectable.\n\n"
    "Which of the following best describes how this therapy recognizes and kills the myeloma cells?",
    {
        "Her own T cells express an engineered receptor that binds BCMA directly": "",
        "A bispecific antibody bridges CD3 on resting T cells to BCMA on myeloma cells":
            "Bispecific antibodies also target BCMA and also use T cells — which is why this is the "
            "closest distractor. But a bispecific is an off-the-shelf DRUG with two binding arms that "
            "pulls unmodified T cells up to the tumour. It involves no leukapheresis and no "
            "engineering of the patient's cells.",
        "An antibody blocks PD-1 so that exhausted T cells resume killing":
            "That is checkpoint blockade — pembrolizumab or nivolumab. It releases a brake on "
            "existing T cells rather than giving them a new receptor.",
        "An antibody delivers a cytotoxic payload into cells that express BCMA":
            "That describes an antibody-drug conjugate, in which the killing is done by a toxin "
            "carried into the cell, not by T cells.",
        "Donor T cells recognize the recipient's HLA molecules as foreign":
            "That is the graft-versus-tumour effect of an ALLOGENEIC stem cell transplant — and the "
            "same recognition causes graft-versus-host disease. This product uses the patient's own "
            "(autologous) cells.",
    },
    "Her own T cells express an engineered receptor that binds BCMA directly",
    "Chimeric antigen receptor (CAR) T-cell therapy. The review describes the process in four steps: "
    "COLLECT the patient's own T cells by leukapheresis, ENGINEER a chimeric antigen receptor into "
    "them outside the body, EXPAND them, and RE-INFUSE them.\n\n"
    "The receptor is 'chimeric' because it joins parts that never occur together naturally: an "
    "antibody-derived binding domain on the outside, fused to T-cell signalling domains on the "
    "inside. The Lisa Masterson case calls it a custom homing beacon programmed to lock onto BCMA. "
    "Because the binding domain comes from an antibody, it recognizes the antigen directly on the "
    "cell surface, WITHOUT needing it to be presented on MHC — which is what lets engineered T cells "
    "kill tumour cells that have learned to hide from ordinary T-cell recognition.\n\n"
    "Targets to know from the review: CD19-directed products (tisagenlecleucel, axicabtagene "
    "ciloleucel, brexucabtagene autoleucel, lisocabtagene maraleucel) for B-cell lymphomas and "
    "B-lymphoblastic leukemia, and BCMA-directed products (idecabtagene vicleucel, ciltacabtagene "
    "autoleucel) for myeloma. The United States label carries a boxed warning for secondary "
    "malignancies, added in 2024.\n\n"
    "Her fever and hypotension at 48 hours were CYTOKINE RELEASE SYNDROME — the commonest reaction "
    "to both CAR T cells and T-cell engagers, driven by interleukin-6 and therefore treated with "
    "tocilizumab, as in question 89.\n\n"
    "Educational objective: CAR T-cell therapy re-infuses the patient's own T cells after they have "
    "been engineered to express a chimeric antigen receptor that binds a tumour surface antigen "
    "(CD19 or BCMA) directly, independent of MHC. Bispecific antibodies reach the same target "
    "with unmodified T cells.",
    "Doctors took her own immune cells out, gave them a new 'grabber' that fits a molecule on the "
    "cancer cells, grew millions of them, and put them back. Now her own immune cells can find and "
    "kill the cancer cells that were hiding from them before.",
    exim="fig_hx_cart_diagram",
    excap="CAR T-cell therapy — collect, engineer, expand, re-infuse",
)

# ── 148. Pembrolizumab — which side of the checkpoint ─────────────────────────────────────────
q(
    "A 62-year-old man with metastatic melanoma begins treatment with pembrolizumab. Biopsy of a "
    "liver metastasis shows tumour cells that strongly express programmed death-ligand 1 (PD-L1), "
    "surrounded by CD8 T lymphocytes that express high levels of programmed cell death protein 1 "
    "(PD-1) but show little cytotoxic activity. After 4 months his metastases have shrunk by 60%. "
    "Several weeks later he develops fatigue, and his thyroid-stimulating hormone is elevated.\n\n"
    "Which of the following best describes the mechanism of this drug?",
    {
        "It binds PD-1 on T cells so tumour PD-L1 cannot switch them off": "",
        "It binds CTLA-4 and prevents inhibition of T-cell priming":
            "That is ipilimumab. CTLA-4 acts mainly during T-cell priming in lymphoid tissue, and "
            "blocking it is a different checkpoint with a higher rate of immune toxicity.",
        "It binds PD-L1 on tumour cells and blocks its interaction with PD-1":
            "The closest distractor, because it would interrupt the same interaction. But blocking "
            "the TUMOUR-side ligand is what atezolizumab, avelumab and durvalumab do. Pembrolizumab "
            "binds the receptor on the T CELL.",
        "It fixes complement on melanoma cells and lyses them directly":
            "Checkpoint inhibitors are not cytotoxic antibodies against the tumour. They act on "
            "T cells, and it is the T cells that kill.",
        "It is a T cell engineered to recognize a melanoma surface antigen":
            "That describes CAR T-cell therapy. Pembrolizumab is a monoclonal antibody given as an "
            "infusion, and it modifies nothing genetically.",
    },
    "It binds PD-1 on T cells so tumour PD-L1 cannot switch them off",
    "Pembrolizumab is a monoclonal antibody against PD-1, the inhibitory receptor on T cells.\n\n"
    "PD-1 exists to limit autoimmunity by dampening T cells in peripheral tissues. Tumours exploit "
    "it: by expressing its ligand, PD-L1, a tumour switches off the T cells that have reached it — "
    "the review calls this the major immune resistance mechanism in tumours. The biopsy shows "
    "exactly that standoff: PD-L1-positive tumour cells beside PD-1-high CD8 T cells that are "
    "present but not killing ('exhausted').\n\n"
    "Pembrolizumab binds PD-1 so that PD-L1 cannot engage it, the brake comes off, and the T cells "
    "already in the tumour resume killing. Nothing is aimed at the tumour directly.\n\n"
    "The drug classes, by which side of the checkpoint they block:\n"
    "• PD-1 (on the T cell): pembrolizumab, nivolumab, cemiplimab, dostarlimab, toripalimab\n"
    "• PD-L1 (on the tumour): atezolizumab, avelumab, durvalumab\n"
    "• CTLA-4 (T-cell priming): ipilimumab, tremelimumab\n\n"
    "The elevated thyroid-stimulating hormone is the other side of the same mechanism. PD-1 normally "
    "restrains autoreactive T cells as well, so releasing it causes IMMUNE-RELATED ADVERSE EVENTS — "
    "thyroiditis, colitis (question 88), pneumonitis, hepatitis, hypophysitis. The mechanism of "
    "benefit and the mechanism of harm are the same.\n\n"
    "Educational objective: Pembrolizumab and nivolumab are anti-PD-1 monoclonal antibodies that "
    "prevent tumour PD-L1 from inactivating T cells, restoring antitumour cytotoxicity. Anti-PD-L1 "
    "drugs block the tumour-side ligand, and anti-CTLA-4 drugs act at T-cell priming.",
    "The cancer was holding up a 'stop' sign that made his immune cells stand down. The drug covers "
    "the immune cells' eyes so they cannot see the stop sign, and they go back to attacking the "
    "cancer. The catch is they also stop respecting the body's own 'stop' signs, which is why his "
    "thyroid got attacked too.",
)

# ── 149. Oncolytic virus therapy ──────────────────────────────────────────────────────────────
q(
    "A 58-year-old woman has unresectable melanoma with more than a dozen cutaneous and subcutaneous "
    "metastases on her left leg. She is treated with serial injections into the skin lesions of "
    "talimogene laherparepvec, a herpes simplex virus type 1 that has been genetically modified to "
    "replicate selectively in tumour cells and to express granulocyte-macrophage "
    "colony-stimulating factor (GM-CSF). Over 6 months the injected lesions regress completely. "
    "Several lesions on the thigh that were never injected also regress, and biopsy of one shows a "
    "dense infiltrate of CD8 T lymphocytes.\n\n"
    "Which of the following best explains the regression of the lesions that were not injected?",
    {
        "Tumour lysis released antigens that primed systemic T cells": "",
        "Antibodies against herpes simplex virus cross-react with melanoma antigens":
            "Antiviral antibodies are directed at viral proteins, not melanoma antigens, and the "
            "biopsy shows a T-cell response rather than an antibody one.",
        "GM-CSF secreted by infected cells is directly cytotoxic to melanoma cells":
            "GM-CSF is not cytotoxic. It is a growth and recruitment signal for dendritic cells — "
            "which is exactly how it contributes to the immune response, not a direct kill.",
        "The virus spread through the blood and lysed the distant tumour cells":
            "The modified virus replicates locally in injected tissue. The CD8 T-cell infiltrate in "
            "a non-injected lesion points to an immune mechanism rather than viral spread.",
        "Viral DNA integrated into tumour cells and silenced their oncogenes":
            "Herpes simplex virus does not integrate into the host genome, and oncolytic viruses do "
            "not work by correcting the tumour's mutations.",
    },
    "Tumour lysis released antigens that primed systemic T cells",
    "Oncolytic virus therapy works in two stages, and the tutor's definition names both: viruses are "
    "engineered or selected to infect and LYSE tumour cells, and they can also STIMULATE AN "
    "ANTITUMOUR IMMUNE RESPONSE.\n\n"
    "1. Direct oncolysis. The modified virus replicates preferentially in tumour cells, which often "
    "have defective antiviral defences, and bursts them. This explains regression of the INJECTED "
    "lesions.\n\n"
    "2. In-situ vaccination. Lysis releases tumour antigens in an intensely inflammatory setting, "
    "and the GM-CSF the virus carries recruits and matures dendritic cells, which carry those "
    "antigens to the draining nodes and prime tumour-specific CD8 T cells. Those T cells circulate "
    "and attack melanoma wherever it is — including lesions the virus never reached. That systemic "
    "effect explains the NON-injected regression, and the CD8 infiltrate in the biopsy is the "
    "evidence for it.\n\n"
    "Talimogene laherparepvec (T-VEC) is herpes simplex virus type 1 with two genes deleted — one "
    "that allows replication in normal neurons, restricting growth to tumour cells, and one that "
    "normally hides infected cells from T cells, improving antigen presentation — and the gene for "
    "GM-CSF inserted. It is approved for injectable, unresectable melanoma.\n\n"
    "Note on sources: oncolytic virus therapy is not in the summative review file. This question "
    "follows the tutor's high-yield definition, supplemented with standard pharmacology, and is "
    "tagged to the immunotherapy mechanism objective.\n\n"
    "Educational objective: Oncolytic viruses selectively infect and lyse tumour cells, and the "
    "released antigens — with immune stimulation such as GM-CSF — prime a systemic T-cell response "
    "that can clear tumour deposits the virus never reached.",
    "Doctors injected a harmless, re-programmed cold-sore virus into the cancer bumps. It only grows "
    "in cancer cells and pops them. The popped cells spill out their contents, which teaches the "
    "immune system what the cancer looks like — so immune cells then go and attack the bumps that "
    "were never injected.",
)

# ── 150. Busulfan lung ────────────────────────────────────────────────────────────────────────
q(
    "A 45-year-old man comes to the office 7 months after an allogeneic hematopoietic stem cell "
    "transplant for acute myeloid leukemia. Conditioning consisted of busulfan and cyclophosphamide, "
    "and he previously received induction with cytarabine and daunorubicin. He reports 2 months of "
    "progressive dry cough and breathlessness on climbing stairs. He has no fever, rash, diarrhea or "
    "jaundice. His skin has become diffusely darker since the transplant. Fine inspiratory crackles "
    "are heard at both lung bases. Spirometry shows a restrictive pattern with a reduced diffusing "
    "capacity for carbon monoxide, and high-resolution CT shows bibasilar reticular opacities. "
    "Bronchoalveolar lavage shows no organisms.\n\n"
    "Which of the following drugs is most likely responsible for his pulmonary disease?",
    {
        "Busulfan": "",
        "Cyclophosphamide":
            "Cyclophosphamide's signature toxicity is hemorrhagic cystitis from its urinary "
            "metabolite acrolein, prevented with mesna; at high doses it can also injure the heart.",
        "Cytarabine":
            "High-dose cytarabine is known for cerebellar toxicity and conjunctivitis, and is "
            "strongly myelosuppressive. Pulmonary fibrosis is not its characteristic lesion.",
        "Daunorubicin":
            "Anthracyclines are cardiotoxic — a cumulative, dose-dependent cardiomyopathy — and "
            "their organ of concern is the heart, not the lung.",
        "Fludarabine":
            "Fludarabine causes profound, prolonged lymphopenia and opportunistic infection. It is "
            "not the agent associated with fibrosis.",
    },
    "Busulfan",
    "Busulfan pulmonary fibrosis. The review's organ-by-organ toxicity table lists two drugs for the "
    "lung — BLEOMYCIN and BUSULFAN, both causing pulmonary fibrosis — and bleomycin was not given "
    "here.\n\n"
    "The clinical pattern is interstitial fibrosis: an insidious dry cough and exertional dyspnea, "
    "bibasilar fine crackles, restrictive physiology with a falling diffusing capacity, and basal "
    "reticulation on CT. It typically appears months after exposure, and the lavage matters because "
    "infection is the main alternative in any transplant recipient and must be excluded first. The "
    "darkening of his skin is a second, characteristic busulfan effect.\n\n"
    "Busulfan is an ALKYLATING agent used principally for myeloablative conditioning before stem "
    "cell transplant, and historically for chronic myeloid leukemia before tyrosine kinase "
    "inhibitors.\n\n"
    "The method matters more than the fact. Each drug in a regimen has one organ it is known for, "
    "so match the organ to the drug: lung → bleomycin and busulfan; bladder → cyclophosphamide and "
    "ifosfamide; heart → anthracyclines and trastuzumab; nerves → vincristine; cerebellum → "
    "high-dose cytarabine.\n\n"
    "Educational objective: Busulfan, an alkylating agent used in transplant conditioning, causes "
    "interstitial pulmonary fibrosis — the same organ toxicity as bleomycin — and skin "
    "hyperpigmentation. Identify a chemotherapy toxicity by matching the injured organ to the "
    "agent known for it.",
    "Each chemotherapy drug tends to damage one particular organ. Only two are famous for scarring "
    "the lungs, and he was given one of them before his transplant. The scarring builds up slowly, "
    "which is why his cough started months later.",
)

# ── 151. Richter transformation ───────────────────────────────────────────────────────────────
q(
    "A 71-year-old man has had chronic lymphocytic leukemia for 6 years, managed with observation "
    "and a single course of therapy 3 years ago, with stable small nodes since. He comes to the "
    "office due to 3 weeks of a rapidly enlarging lump in the left axilla, fevers, drenching night "
    "sweats and 5 kg of weight loss. Examination shows a firm 7 cm left axillary mass; the other "
    "nodes are unchanged.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 11.8 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 35% (N=41%–53%)\n"
    "Leukocyte count 24,000/mm3 (N=4,500–11,000/mm3)\n"
    "Lactate dehydrogenase 910 U/L (N=45–200 U/L)\n\n"
    "Biopsy of the axillary mass shows diffuse sheets of large B cells with vesicular nuclei and "
    "prominent nucleoli, replacing the small lymphocytes seen in a node biopsied at diagnosis. The "
    "Ki-67 proliferation index is 80%. Which of the following is the most likely diagnosis?",
    {
        "Transformation to diffuse large B-cell lymphoma": "",
        "Autoimmune hemolytic anemia complicating the leukemia":
            "An autoimmune complication of CLL causes anemia with hemolysis — reticulocytosis, "
            "spherocytes, a positive direct antiglobulin test. It does not produce a rapidly growing "
            "mass of large cells.",
        "Progression of the leukemia without histologic change":
            "Progressive CLL enlarges nodes gradually and keeps its small-cell morphology and low "
            "proliferation rate. Sheets of large cells with a proliferation index of 80% are a "
            "different disease.",
        "Reactive lymphadenitis from an opportunistic infection":
            "Infection is common in CLL and can cause fever and adenopathy, but it does not replace "
            "a node with monotonous sheets of large neoplastic B cells.",
        "Transformation to mantle cell lymphoma":
            "Mantle cell lymphoma is a distinct CD5-positive, CD23-negative neoplasm driven by "
            "t(11;14) and cyclin D1. CLL does not transform into it.",
    },
    "Transformation to diffuse large B-cell lymphoma",
    "RICHTER TRANSFORMATION — progression of chronic lymphocytic leukemia / small lymphocytic "
    "lymphoma to diffuse large B-cell lymphoma.\n\n"
    "The clinical signature from the review is a RAPIDLY ENLARGING MASS in a node or the spleen in a "
    "patient whose disease had previously been indolent — here a single node outgrowing all the "
    "others within weeks, with B symptoms (fever, night sweats, weight loss) and a sharply raised "
    "lactate dehydrogenase. Any abrupt change of tempo in CLL should prompt a biopsy of the "
    "fastest-growing site, and ideally of the most metabolically active site on PET.\n\n"
    "The biopsy defines it: SHEETS OF LARGE CELLS replacing the previous small lymphocytic "
    "population, with a proliferation rate an order of magnitude higher than CLL's.\n\n"
    "The genetic fact is the one to hold: it is driven by newly acquired mutations in TP53 or MYC. "
    "TP53 loss, including the 17p deletion, also predicts a poor response to chemoimmunotherapy in "
    "CLL itself, which is why that group is treated with a BTK or BCL-2 inhibitor instead. Richter "
    "transformation occurs in 2%–9% of patients and is usually fatal — the aggressive end of the "
    "grow-fast, die-fast rule.\n\n"
    "Educational objective: Richter transformation is progression of CLL/SLL to diffuse large B-cell "
    "lymphoma, presenting as a rapidly enlarging mass with B symptoms and a rising lactate "
    "dehydrogenase, confirmed by biopsy showing sheets of large cells. It is driven by acquired TP53 "
    "or MYC mutations and carries a poor prognosis.",
    "His slow, quiet blood cancer has turned into a fast, aggressive one. That is why one lump grew "
    "huge in a few weeks while the others stayed the same, and why the biopsy now shows big, rapidly "
    "dividing cells instead of the small ones he had before.",
)

# ── 152. Therapy-related APL after etoposide (Amir Islam case) ────────────────────────────────
q(
    "A 29-year-old man comes to the office due to 4 weeks of worsening fatigue, breathlessness and "
    "easy bruising. Four years ago he was diagnosed with metastatic testicular germ cell cancer; he "
    "underwent left orchiectomy and chemotherapy with bleomycin, etoposide and cisplatin, and "
    "achieved complete remission. He received no radiation. He has petechiae on both shins and "
    "bleeding from the gums.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.0 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 24% (N=41%–53%)\n"
    "Leukocyte count 2,200/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 21,000/mm3 (N=150,000–400,000/mm3)\n"
    "Fibrinogen 90 mg/dL (N=200–400 mg/dL)\n"
    "D-dimer 7,800 ng/mL (N=<250 ng/mL)\n\n"
    "The smear shows hypergranular promyelocytes, several containing multiple Auer rods, and "
    "cytogenetics show t(15;17). Which of the following most likely caused this malignancy?",
    {
        "Etoposide": "",
        "Bleomycin":
            "Bleomycin's organ toxicity is the lung — pulmonary fibrosis — and it is notably "
            "non-myelosuppressive. It is not leukemogenic.",
        "Cisplatin":
            "Cisplatin is known for nephrotoxicity, ototoxicity and peripheral neuropathy, not for "
            "causing a balanced-translocation leukemia.",
        "Cyclophosphamide":
            "Alkylating agents do cause therapy-related myeloid neoplasms — but with a longer "
            "latency of 5–7 years, often a preceding myelodysplastic phase, and deletions of "
            "chromosomes 5 or 7 rather than a balanced translocation. And he never received one.",
        "Radiotherapy":
            "Radiation can be leukemogenic, but the history states he received none.",
    },
    "Etoposide",
    "Therapy-related acute promyelocytic leukemia after a TOPOISOMERASE II INHIBITOR.\n\n"
    "The Amir Islam case asks precisely this: what increased his risk of AML? The answer is his "
    "testicular cancer treatment, and specifically the topoisomerase II inhibitor etoposide. The "
    "latency between cytotoxic exposure and a therapy-related myeloid neoplasm ranges from one to "
    "ten years, and for topoisomerase II inhibitors it is typically 1–3 years.\n\n"
    "The two families of leukemogenic chemotherapy are worth contrasting, because the pattern "
    "identifies the culprit:\n"
    "• TOPOISOMERASE II INHIBITORS (etoposide, anthracyclines) — shorter latency, no preceding "
    "myelodysplasia, BALANCED translocations such as those involving KMT2A at 11q23, or t(15;17).\n"
    "• ALKYLATING AGENTS and radiation — longer latency of 5–7 years, often a myelodysplastic "
    "prodrome, and unbalanced losses of chromosomes 5 or 7 with a poor prognosis.\n\n"
    "Topoisomerase II cuts both DNA strands and re-ligates them; trapping the enzyme mid-cut leaves "
    "double-strand breaks, and mis-repair between two broken chromosomes produces exactly the kind "
    "of balanced translocation seen here.\n\n"
    "The leukemia itself is acute promyelocytic leukemia: hypergranular promyelocytes with multiple "
    "Auer rods, t(15;17) fusing PML to RARA, and disseminated intravascular coagulation — low "
    "fibrinogen, very high D-dimer and mucocutaneous bleeding. As in question 63, all-trans retinoic "
    "acid is started on suspicion because early hemorrhagic death is the principal threat, and APL "
    "is curable in more than 70% of patients with ATRA plus arsenic trioxide or an anthracycline.\n\n"
    "Educational objective: Topoisomerase II inhibitors such as etoposide cause therapy-related "
    "myeloid neoplasms with a short latency (typically 1–3 years), no myelodysplastic prodrome, and "
    "balanced translocations. Alkylating agents cause them after a longer latency, often with "
    "chromosome 5 or 7 losses.",
    "One of the drugs that cured his first cancer works by cutting DNA. Occasionally the cuts are "
    "glued back together wrongly, joining two chromosomes, and that mistake can start a new blood "
    "cancer a couple of years later — which is what happened here.",
)

# ── 153. Differentiation syndrome on ATRA (Amir Islam case) ───────────────────────────────────
q(
    "A 29-year-old man with acute promyelocytic leukemia is on day 9 of induction with all-trans "
    "retinoic acid and arsenic trioxide. His bleeding has stopped and the fibrinogen has normalized. "
    "Over the past 24 hours he has developed fever to 38.9 C (102.0 F), progressive breathlessness "
    "and 4 kg of weight gain with ankle edema. Blood pressure is 94/58 mm Hg, respirations are "
    "28/min and oxygen saturation is 88% on room air. Chest radiography shows bilateral pulmonary "
    "infiltrates with small bilateral pleural effusions.\n\n"
    "Laboratory studies show:\n"
    "Leukocyte count 31,000/mm3 (N=4,500–11,000/mm3)\n"
    "Creatinine 1.9 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "His leukocyte count was 3,400/mm3 at diagnosis. Blood cultures are drawn and broad-spectrum "
    "antibiotics started. Which of the following is the most appropriate additional treatment?",
    {
        "Dexamethasone": "",
        "Intravenous furosemide":
            "Diuresis may help the fluid, but it misses the cause. This is an inflammatory syndrome "
            "driven by the maturing leukemic cells, and treating only the fluid lets it progress.",
        "Permanent withdrawal of retinoic acid":
            "These drugs are curing his leukemia. In severe differentiation syndrome they may be "
            "held TEMPORARILY, but abandoning them permanently would forfeit a cure rate above 70%.",
        "Cryoprecipitate transfusion":
            "His coagulopathy has resolved, which is the expected benefit of retinoic acid. The new "
            "problem is not bleeding.",
        "Tocilizumab":
            "Tocilizumab is the specific treatment for cytokine release syndrome after CAR T cells or "
            "T-cell engagers. The treatment for differentiation syndrome is a corticosteroid.",
    },
    "Dexamethasone",
    "DIFFERENTIATION SYNDROME — the principal complication of retinoic acid (and arsenic) therapy in "
    "acute promyelocytic leukemia, described in the Amir Islam case as a cytokine storm.\n\n"
    "All-trans retinoic acid forces the malignant promyelocytes to mature into neutrophil-like "
    "cells. Maturing cells change their adhesion molecules and release cytokines, migrate into the "
    "tissues — especially the lungs — and cause capillary leak. The case gives the numbers: it "
    "occurs in a quarter to a half of patients, 2–21 days after starting treatment, and the risk is "
    "higher with a high white count at diagnosis.\n\n"
    "The features are exactly this patient's: fever, peripheral edema and weight gain, pulmonary "
    "infiltrates, hypoxemia and respiratory distress, hypotension, renal and hepatic dysfunction, and "
    "serositis with pleural or pericardial effusions. The steeply rising leukocyte count is the "
    "companion phenomenon — hyperleukocytosis from rapid maturation of the leukemic cells, seen in "
    "up to half of patients on retinoic acid alone.\n\n"
    "Treatment is DEXAMETHASONE, started at the first suspicion, with the differentiating agents held "
    "only temporarily if the syndrome is severe. Infection must be covered, as here, because it "
    "presents identically — but it does not replace the steroid.\n\n"
    "One more retinoic acid toxicity from the case: raised intracranial pressure (pseudotumor "
    "cerebri), most common in children and adolescents.\n\n"
    "Educational objective: Differentiation syndrome complicates all-trans retinoic acid and arsenic "
    "therapy for APL within days to weeks, with fever, pulmonary infiltrates, effusions, weight gain, "
    "hypotension and renal dysfunction. Treat promptly with dexamethasone and continue the "
    "differentiating therapy when possible.",
    "His medicine works by making the cancer cells grow up into normal-looking white cells. When "
    "lots of them grow up at once, they release alarm chemicals and pile into his lungs, making him "
    "feverish, swollen and short of breath. A steroid calms that storm down while the medicine keeps "
    "curing the leukemia.",
)

# ── 154. Why the bone scan is negative in myeloma (Lisa Masterson case) ───────────────────────
q(
    "A 50-year-old woman comes to the urgent care center due to 6 weeks of worsening thoracolumbar "
    "back pain that wakes her at night. She recently had herpes zoster that was slow to heal, and she "
    "reports fatigue, constipation, increased thirst and passing more urine.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.6 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 29% (N=36%–46%)\n"
    "Calcium 11.6 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Creatinine 1.8 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Total protein 9.8 g/dL (N=6.0–7.8 g/dL)\n"
    "Albumin 3.4 g/dL (N=3.5–5.5 g/dL)\n"
    "Anion gap 3 mEq/L (N=8–12 mEq/L)\n"
    "Alkaline phosphatase 74 U/L (N=44–121 U/L)\n"
    "Erythrocyte sedimentation rate 118 mm/h (N=0–20 mm/h)\n\n"
    "The peripheral smear shows red cells stacked in long chains. A lateral skull radiograph is "
    "shown. A technetium bone scan obtained earlier by another clinician was reported as normal. "
    "Which of the following best explains the normal alkaline phosphatase and bone scan?",
    {
        "Osteoclast activation with suppression of osteoblast activity": "",
        "Hypercalcemia prevents skeletal uptake of the radiotracer":
            "Calcium levels do not block technetium uptake. The scan is negative because of what is "
            "happening, or not happening, in the bone itself.",
        "The lesions are metastatic deposits from an occult carcinoma":
            "Most metastatic carcinomas provoke reactive bone formation and are hot on bone scan — "
            "prostate cancer most dramatically. Purely lytic, scan-negative disease with this "
            "biochemistry points to myeloma.",
        "The lesions are too small to be detected by scintigraphy":
            "The skull lesions are plainly visible on a simple radiograph, which is a far less "
            "sensitive test. Size is not the issue.",
        "Renal impairment increases clearance of alkaline phosphatase":
            "Alkaline phosphatase is not renally cleared in any way that would mask bone disease. "
            "It is normal because bone formation is not increased.",
    },
    "Osteoclast activation with suppression of osteoblast activity",
    "Multiple myeloma with purely LYTIC bone disease — the skull shows innumerable punched-out "
    "lesions of varying size, the 'raindrop' pattern.\n\n"
    "Myeloma UNCOUPLES bone remodelling. Malignant plasma cells secrete osteoclast-activating "
    "factors, tipping the RANK ligand / osteoprotegerin balance toward resorption, and they "
    "simultaneously SUPPRESS osteoblasts through DKK1. Bone is removed with no repair response at "
    "all. Two tests depend on that repair response:\n\n"
    "• ALKALINE PHOSPHATASE is an enzyme on the surface of active osteoblasts and the primary marker "
    "of bone formation — so it stays normal. The case notes that because myeloma lesions are purely "
    "'clastic', alkaline phosphatase is suppressed.\n"
    "• A TECHNETIUM BONE SCAN images osteoblastic activity, not bone loss — so it can be normal "
    "despite extensive destruction. Myeloma bone disease is assessed instead with a skeletal survey, "
    "low-dose whole-body CT or MRI.\n\n"
    "The rest of the stem is the Lisa Masterson case's own set of clues. The CRAB features — "
    "hyperCalcemia (with polyuria and polydipsia from a nephrogenic diabetes insipidus effect, and "
    "constipation), Renal impairment, Anemia and Bone lesions. A protein gap (total protein 9.8 with "
    "albumin 3.4) from the paraprotein. Rouleaux — red cells stacked like coins because the "
    "paraprotein alters their surface charge — which also drives the sedimentation rate above 100. "
    "A LOW ANION GAP, a subtle historical clue to an IgG myeloma, because IgG paraprotein is "
    "cationic. And slow-healing zoster from immune paresis: hypogammaglobulinemia of the normal "
    "immunoglobulins.\n\n"
    "Educational objective: Myeloma bone lesions are purely lytic because malignant plasma cells "
    "activate osteoclasts and suppress osteoblasts. Alkaline phosphatase and technetium bone scans "
    "reflect osteoblastic activity and are therefore often normal, so skeletal survey, low-dose CT "
    "or MRI is used instead.",
    "Bone is constantly being eaten away and rebuilt. Her cancer cells turn the 'eaters' up and "
    "switch the 'builders' off. The blood test and the bone scan both look for builders at work — "
    "and there are none — so both look normal even though her bones are full of holes.",
    image="fig_hx_myeloma_skull",
    imcap="Lateral skull radiograph",
)
