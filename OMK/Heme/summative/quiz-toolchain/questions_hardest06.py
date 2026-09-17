# Hardest Exam — batch H6 (questions 101–120): high-yield depth.
# Each item is built on a card from the review file's own Master High-Yield Checklist that the first
# 100 questions did not test: cards 06, 07, 12, 13, 14, 15, 16, 17, 22, 24, 27, 28, 32, 41, 47, 48,
# 51, 53, 56 and 61.

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


# ── 101. Never give folate alone for a macrocytosis (card 06) ───────────────────
q(
    "A 71-year-old man is admitted to the hospital due to falls. He has a 6-month history of "
    "unsteadiness and numbness of both feet. He follows a strict vegan diet. Examination shows a "
    "wide-based gait, absent ankle reflexes, reduced vibration sense to both knees, and a positive "
    "Romberg sign.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.6 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 29% (N=41%–53%)\n"
    "Mean corpuscular volume 113 µm3 (N=80–100 µm3)\n"
    "Reticulocyte count 0.5% (N=0.5%–1.5%)\n"
    "Lactate dehydrogenase 980 U/L (N=45–200 U/L)\n\n"
    "The intern starts oral folic acid 1 mg daily while awaiting further results. Four weeks later "
    "the hemoglobin is 12.8 g/dL and the mean corpuscular volume is 94 µm3, but the patient now "
    "cannot feel his feet and has fallen twice more. Which of the following best explains this "
    "course?",
    {
        "Folate corrects the anemia without treating the neurologic lesion": "",
        "Folate supplementation has precipitated an iron deficiency":
            "A brisk response to any hematinic can unmask limited iron stores, but that would blunt "
            "the hemoglobin rise rather than produce a progressive myelopathy.",
        "Folate has caused a drug-induced peripheral neuropathy":
            "Folic acid is essentially nontoxic even at high doses and is rapidly excreted in the "
            "urine. The neurologic disease is the untreated deficiency, not the treatment.",
        "The neurologic findings are unrelated to the hematologic disorder":
            "Dorsal column signs with a macrocytic anemia in a strict vegan are one disease, not two. "
            "Assuming otherwise is exactly how the diagnosis gets missed.",
        "The patient has developed a superimposed myelodysplastic syndrome":
            "Myelodysplasia can cause a macrocytic anemia in an older patient, but it does not "
            "correct with folic acid, and it does not cause subacute combined degeneration.",
    },
    "Folate corrects the anemia without treating the neurologic lesion",
    "Vitamin B12 deficiency treated with folate alone — the single most dangerous shortcut in the "
    "anemia block.\n\n"
    "B12 has TWO jobs; folate has only the first:\n"
    "• DNA synthesis — shared with folate, so folate alone repairs the megaloblastic anemia\n"
    "• Maintenance of myelin — B12 ONLY, so the dorsal and lateral column degeneration continues "
    "unopposed and eventually becomes irreversible\n\n"
    "That asymmetry is why the blood count improving is the trap: everyone relaxes, the patient looks "
    "better, and the subacute combined degeneration progresses. Always check a B12 level BEFORE "
    "treating a macrocytic anemia with folate.\n\n"
    "How the two are separated when both cause macrocytosis with hypersegmented neutrophils: "
    "METHYLMALONIC ACID is elevated in B12 deficiency and normal in folate deficiency, while "
    "homocysteine rises in both and therefore discriminates nothing. If you can order one test, order "
    "the methylmalonic acid. And the clinical version: B12 has the Brain; folate does not.\n\n"
    "His raised lactate dehydrogenase with a low reticulocyte count is the signature of ineffective "
    "erythropoiesis — precursors made in large numbers and destroyed inside the marrow. A strict "
    "vegan diet is a genuine risk factor because plants contain very little cobalamin; other routes "
    "are pernicious anemia, gastrectomy or bypass, ileal disease, fish tapeworm, metformin and proton "
    "pump inhibitors.\n\n"
    "Educational objective: Folate corrects the megaloblastic anemia of vitamin B12 deficiency while "
    "the neurologic degeneration continues, so a B12 level must be checked before treating any "
    "macrocytic anemia with folate. Methylmalonic acid is elevated in B12 deficiency and normal in "
    "folate deficiency.",
    "The vitamin he was given fixes the blood problem but not the nerve problem, so his blood counts "
    "looked great while his spinal cord kept getting worse. The missing vitamin is the only one that "
    "protects nerves.",
    exim="fig_slide_b12_tree",
    excap="The B12 decision tree — and why the neurologic arm is the one folate cannot treat.",
)

# ── 102. Thalassemia trait versus iron deficiency (card 07) ─────────────────────
q(
    "A 3-year-old boy is brought to the office for a routine health maintenance visit. He is "
    "asymptomatic, active and growing along the 50th percentile. His parents are of Greek descent. "
    "He drinks a varied diet and takes no supplements.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 10.6 g/dL (N=11.0–14.0 g/dL)\n"
    "Hematocrit 32% (N=33%–42%)\n"
    "Mean corpuscular volume 62 µm3 (N=70–86 µm3)\n"
    "Erythrocyte count 5.6 million/mm3 (N=3.9–5.3 million/mm3)\n"
    "Red cell distribution width 13.1% (N=11.5%–14.5%)\n"
    "Ferritin 68 ng/mL (N=10–120 ng/mL)\n"
    "Transferrin saturation 31% (N=20%–50%)\n\n"
    "The peripheral smear is shown. Which of the following is the most appropriate next step in "
    "management?",
    {
        "Bone marrow aspiration with Prussian blue staining":
            "A marrow iron stain is the historical gold standard for iron stores, but his ferritin "
            "and transferrin saturation already establish that iron is not the problem, and this is "
            "an invasive test in a well child.",
        "Hemoglobin electrophoresis": "",
        "Intravenous iron sucrose":
            "Parenteral iron is for malabsorption, intolerance or ongoing loss in a genuinely "
            "iron-deficient patient. Giving it here creates overload with no benefit.",
        "Oral ferrous sulfate for 3 months":
            "This is the reflex answer to any microcytic anemia, and it is the trap. His iron studies "
            "are normal, so iron will achieve nothing except risking overload.",
        "Reassurance with no further testing":
            "The indices are not normal and the diagnosis has consequences for genetic counseling and "
            "for avoiding a lifetime of unnecessary iron.",
        "Testing stool for occult blood":
            "Occult gastrointestinal blood loss is the cause to chase in an ADULT male or "
            "postmenopausal woman with iron deficiency. He is neither, and he is not iron deficient.",
    },
    "Hemoglobin electrophoresis",
    "Thalassemia trait. Three microcytic anemias look alike on the complete blood count and are "
    "treated in three completely different ways:\n"
    "• IRON DEFICIENCY — ferritin LOW, total iron-binding capacity HIGH, red cell distribution width "
    "raised, red cell count LOW → give iron\n"
    "• ANEMIA OF CHRONIC DISEASE — ferritin HIGH, TIBC LOW → treat the underlying disease\n"
    "• THALASSEMIA TRAIT — ALL iron studies NORMAL, MCV disproportionately low for a mild anemia, red "
    "cell count HIGH, RDW normal → give nothing, and specifically not iron\n\n"
    "The discriminating pair on the blood count alone is the MCV against the red cell COUNT: in "
    "thalassemia the marrow makes MANY small cells, whereas in iron deficiency it makes FEW small "
    "cells. An MCV of 62 with a red cell count of 5.6 million and a normal RDW is thalassemia until "
    "proven otherwise.\n\n"
    "Confirm with hemoglobin electrophoresis or high-performance liquid chromatography: beta "
    "thalassemia trait shows a raised hemoglobin A2 (and often raised hemoglobin F), while alpha "
    "thalassemia trait shows normal electrophoresis and is a diagnosis of exclusion or genetic "
    "testing. That distinction matters for counseling — two parents with trait can produce a child "
    "with thalassemia major or, in alpha thalassemia, hydrops fetalis.\n\n"
    "Give iron to a thalassemic patient and you produce exactly the complication that transfused "
    "thalassemia patients spend their lives chelating out.\n\n"
    "Educational objective: Microcytosis with normal iron studies, a disproportionately low MCV, a "
    "HIGH red cell count and a normal RDW indicates thalassemia trait, which is confirmed by "
    "hemoglobin electrophoresis and must not be treated with iron.",
    "His red cells are small, but he has plenty of them and plenty of iron — so this is not iron "
    "deficiency. Giving iron would do nothing except slowly poison him with too much of it.",
    image="fig_target_cells",
    imcap="Peripheral blood smear: several erythrocytes show a central dot of dense staining "
          "surrounded by a pale ring and a darker rim, giving a bull's-eye appearance; the cells are "
          "small and uniform in size.",
    exim="fig_thal_minor_uw",
    excap="Beta thalassemia trait — microcytic cells with target forms, and normal iron studies.",
)

# ── 103. The restrictive transfusion threshold (card 12) ────────────────────────
q(
    "A 64-year-old woman is in the intensive care unit on day 4 of treatment for community-acquired "
    "pneumonia. She is hemodynamically stable on no vasopressors, is euvolemic, and has had no "
    "bleeding. She has stable coronary artery disease and reports no chest pain. Pulse is 84/min and "
    "blood pressure is 122/70 mm Hg.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.6 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 23% (N=36%–46%)\n"
    "Platelet count 210,000/mm3 (N=150,000–400,000/mm3)\n"
    "Creatinine 0.9 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "The resident proposes transfusing 2 units of red blood cells to bring the hemoglobin above 10 "
    "g/dL, reasoning that a higher hemoglobin will speed her recovery. Which of the following is the "
    "most appropriate response?",
    {
        "Transfuse 1 unit now and reassess before giving any further units":
            "One unit at a time and then reassess is the correct TECHNIQUE whenever transfusion is "
            "indicated — but at 7.6 g/dL in a stable, asymptomatic, euvolemic patient the indication "
            "itself has not been met.",
        "Transfuse 2 units to a target hemoglobin above 10 g/dL":
            "This is the liberal strategy tested in the TRICC trial, and the liberal arm did WORSE. "
            "It is also two units given reflexively rather than one and a reassessment.",
        "Transfuse 2 units because her coronary disease requires a higher threshold":
            "Stable coronary disease does not by itself justify a liberal threshold; she has no "
            "ischemic symptoms. Acute coronary syndrome is the setting where a higher trigger is "
            "debated.",
        "Withhold transfusion and continue to monitor": "",
        "Withhold transfusion and start an erythropoiesis-stimulating agent":
            "Erythropoiesis-stimulating agents are approved for anemia of chronic kidney disease and "
            "chemotherapy-induced anemia, take weeks to work, and are never a substitute for "
            "transfusion in acute illness. Her creatinine is normal.",
    },
    "Withhold transfusion and continue to monitor",
    "The TRICC trial is the evidence, and it is worth being able to state:\n"
    "• QUESTION — in critically ill patients, is a restrictive or a liberal red cell transfusion "
    "strategy better?\n"
    "• DESIGN — randomized trial, 838 intensive care patients, all EUVOLEMIC (that is, not actively "
    "bleeding)\n"
    "• ARMS — restrictive, transfuse below 7 g/dL, versus liberal, transfuse below 10 g/dL\n"
    "• RESULT — no difference in 30-day mortality, and the LIBERAL arm, which received more blood, "
    "did worse\n\n"
    "Why the euvolemic entry criterion matters: an actively bleeding patient loses whole blood — "
    "plasma, coagulation factors and platelets along with red cells — and needs volume and the full "
    "range of products regardless of a hemoglobin that can look deceptively normal early on. The 7 "
    "g/dL threshold does not apply to active hemorrhage.\n\n"
    "What red cells are for: increasing oxygen-carrying capacity, replacing red cell mass after "
    "significant hemorrhage, and chronic transfusion programs in sickle cell disease and thalassemia. "
    "What they are explicitly NOT for: promoting wound healing or shortening time to ambulation. Both "
    "were once believed and neither is supported.\n\n"
    "And the framing that governs every transfusion decision: blood cannot be manufactured, and every "
    "unit carries a reaction and residual infectious risk — so the question is never 'is the number "
    "low?' but 'will this unit help this patient more than it might harm them?'\n\n"
    "Educational objective: In stable, euvolemic patients a restrictive transfusion threshold of 7 "
    "g/dL is at least as safe as a liberal threshold of 10 g/dL, and when transfusion is indicated it "
    "is given one unit at a time with reassessment. Red cells are not given to promote healing or "
    "mobility.",
    "Giving extra blood to a stable patient does not make them recover faster — the big trial showed "
    "the group that got more blood actually did worse. Below about seven is when it genuinely helps.",
)

# ── 104. Platelet transfusion thresholds (card 13) ──────────────────────────────
q(
    "A 43-year-old man with acute myeloid leukemia is on day 15 after induction chemotherapy. He has "
    "no bleeding, no petechiae and no fever, and his examination is unremarkable. A diagnostic lumbar "
    "puncture is planned for tomorrow because of a new headache. His hemoglobin is 8.4 g/dL, "
    "leukocyte count is 400/mm3 and platelet count is 14,000/mm3 (N=150,000–400,000/mm3). "
    "Coagulation studies are normal. Which of the following is the most appropriate transfusion plan?",
    {
        "Transfuse platelets now and again before the procedure": "",
        "Transfuse platelets now to a target count above 50,000/mm3":
            "A threshold near 50,000 applies to a patient who is actively bleeding or undergoing "
            "major surgery, not to a diagnostic lumbar puncture in a non-bleeding patient.",
        "Transfuse platelets only if bleeding develops":
            "Withholding platelets entirely is correct for CONSUMPTIVE thrombocytopenia — immune "
            "thrombocytopenia or dengue — where transfused platelets are destroyed just as fast. His "
            "marrow is hypoproliferative after chemotherapy.",
        "Transfuse red blood cells and platelets to normalize both counts":
            "Normalizing numbers is not a transfusion indication. His hemoglobin of 8.4 g/dL does not "
            "meet the restrictive threshold, and platelets are given to a threshold, not to normal.",
        "Withhold platelets because the count is above 10,000/mm3":
            "The 10,000 threshold is for a NON-BLEEDING patient with hypoproliferative "
            "thrombocytopenia and nothing planned. A procedure raises the threshold — a spinal "
            "hematoma would be catastrophic.",
    },
    "Transfuse platelets now and again before the procedure",
    "Three numbers, in ascending order of how much risk you are willing to take:\n"
    "• 10,000/µL — a stable, NON-BLEEDING patient with hypoproliferative thrombocytopenia (receiving "
    "chemotherapy or undergoing stem cell transplant). Nothing is about to be done to them\n"
    "• 20,000/µL — before a LUMBAR PUNCTURE, because you are putting a needle into the spinal canal "
    "where a hematoma would be catastrophic\n"
    "• 25,000/µL — a PRETERM NEONATE, whose germinal matrix vessels are fragile\n\n"
    "Because a procedure is planned, the higher threshold governs — so he is transfused now and "
    "topped up immediately before the puncture, since transfused platelets survive only a few days.\n\n"
    "The fourth entry on the same list teaches the principle rather than a number: in DENGUE the "
    "thrombocytopenia is CONSUMPTIVE, so do not transfuse on the count alone — transfused platelets "
    "are consumed too. The same logic applies to immune thrombocytopenia, where the marrow is making "
    "platelets normally and an autoantibody is destroying them: treatment is directed at the immune "
    "process (corticosteroids, intravenous immunoglobulin, thrombopoietin receptor agonists), with "
    "platelet transfusion reserved for serious active bleeding. Treat the mechanism, not the number.\n\n"
    "Educational objective: Platelets are transfused below 10,000/µL in a non-bleeding patient with "
    "hypoproliferative thrombocytopenia, below 20,000/µL before a lumbar puncture and below 25,000/µL "
    "in a preterm neonate; consumptive thrombocytopenias such as immune thrombocytopenia and dengue "
    "are not transfused on the count alone.",
    "How low you let platelets go depends on what you are about to do. Doing nothing, ten thousand is "
    "safe enough; putting a needle near the spinal cord, you want double that.",
    exim="fig_tx_reactions",
    excap="The four blood products and their indications, side by side.",
)

# ── 105. The 30% rule and the commonest plasma error (card 14) ──────────────────
q(
    "A 58-year-old woman with cirrhosis is scheduled for a diagnostic paracentesis for new ascites. "
    "She has had no bleeding, and there is no bruising or mucosal bleeding on examination.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 10.8 g/dL (N=12.0–16.0 g/dL)\n"
    "Platelet count 84,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 17 sec (N=11–15 sec)\n"
    "International normalized ratio 1.4 (N=0.9–1.1)\n"
    "Fibrinogen 210 mg/dL (N=200–400 mg/dL)\n\n"
    "The surgical intern requests 2 units of fresh frozen plasma to 'normalize the INR' before the "
    "procedure. Which of the following is the best reason to decline?",
    {
        "Cirrhotic patients are hypercoagulable and plasma would cause thrombosis":
            "Liver disease produces a REBALANCED system — both procoagulants and the natural "
            "anticoagulants fall — so patients can clot or bleed. That is an argument against "
            "trusting the INR, not a claim that plasma causes thrombosis.",
        "Cryoprecipitate should be given instead of plasma":
            "Cryoprecipitate is the concentrated fibrinogen product, for hypofibrinogenemia in "
            "disseminated intravascular coagulation or obstetric hemorrhage. Her fibrinogen is "
            "normal.",
        "Her factor activity is already above the level needed for hemostasis": "",
        "Plasma cannot correct a coagulopathy caused by liver disease":
            "Plasma does contain the factors the liver is failing to make; the issue is that this "
            "patient does not need them, not that the product would not work.",
        "Vitamin K should be given instead to correct the prothrombin time":
            "Vitamin K helps when deficiency is the cause — factors II, VII, IX and X low with a "
            "NORMAL factor V. In hepatic synthetic failure factor V falls too, and vitamin K does "
            "not fix it. Either way, no correction is needed here.",
    },
    "Her factor activity is already above the level needed for hemostasis",
    "The single number governing plasma transfusion is 30%: you need only about 30% coagulation "
    "factor activity to form a clot. Above that line hemostasis is adequate.\n\n"
    "The metaphor makes it stick. Your circulating plasma is an OCEAN; a unit of transfused plasma is "
    "a TEACUP. If the ocean already holds 50%–60% activity, a teacup changes essentially nothing — "
    "and nothing needed changing. Only when the ocean is down at 10%–15% does that same teacup move "
    "the needle. Translated into numbers you will see: an INR of 1.1 is far above the threshold, and "
    "a prothrombin time around 2 to 2.2 times normal is roughly where 30% activity sits.\n\n"
    "The commonest plasma error in the hospital is someone seeing an INR of 1.1 or 1.4 and ordering "
    "plasma to normalize it. The transfusion achieves nothing measurable while exposing the patient "
    "to a transfusion reaction, a residual infectious risk and a volume load. You are not treating "
    "the patient; you are treating the number.\n\n"
    "Liver disease sharpens the point further: the liver makes both the procoagulant factors AND "
    "protein C, protein S and antithrombin, so losing both sides leaves a rebalanced but fragile "
    "hemostasis. The INR measures only the procoagulant half, so it reports a coagulopathy the "
    "patient may not clinically have — quite unlike warfarin, where the INR is a validated, "
    "dose-calibrated measure.\n\n"
    "The legitimate indications for plasma: a documented factor deficiency AND active bleeding; a "
    "markedly prolonged clotting time before a procedure; and warfarin reversal, where prothrombin "
    "complex concentrate plus vitamin K is preferred. Not for a single factor deficiency — give the "
    "specific concentrate.\n\n"
    "Educational objective: Approximately 30% coagulation factor activity is sufficient for "
    "hemostasis, so plasma given for a mildly raised INR provides no benefit while exposing the "
    "patient to transfusion risk; in liver disease the INR particularly overstates bleeding risk "
    "because the natural anticoagulants fall in parallel.",
    "You only need about a third of your clotting proteins working to form a clot, and she is well "
    "above that. A bag of plasma is a teacup poured into an ocean.",
)

# ── 106. Irradiation and transfusion-associated graft-versus-host disease (card 16) ─
q(
    "A 6-month-old boy with severe combined immunodeficiency is scheduled for a hematopoietic stem "
    "cell transplant and requires a red blood cell transfusion for a hemoglobin of 6.4 g/dL. His "
    "mother, who is ABO compatible, asks to donate the unit herself so that her son receives 'family "
    "blood'. Which of the following best describes the risk of this request?",
    {
        "Donor lymphocytes may engraft and attack the recipient's tissues": "",
        "Maternal antibodies may cross into the infant and cause hemolysis":
            "Maternal antibody crossing the placenta causes hemolytic disease of the fetus and "
            "newborn before birth. A transfused unit is leukoreduced red cells, and ABO compatibility "
            "has been established.",
        "Related donors transmit cytomegalovirus more often than volunteers":
            "Cytomegalovirus risk is managed with leukoreduced or cytomegalovirus-negative products "
            "and is not increased by relatedness.",
        "The infant will become alloimmunized against paternal antigens":
            "Alloimmunization to minor red cell antigens is a real consequence of repeated "
            "transfusion — it is why chronically transfused patients receive extended antigen-matched "
            "units — but it is not the danger specific to a related donor.",
        "The unit will contain fewer functional platelets than a volunteer unit":
            "Platelet content is a property of the product, not of the donor relationship, and red "
            "cell units are not given for platelets.",
    },
    "Donor lymphocytes may engraft and attack the recipient's tissues",
    "Transfusion-associated graft-versus-host disease — and here the GRAFT is the blood product "
    "itself.\n\n"
    "Every blood product contains residual donor lymphocytes. A competent immune system recognizes "
    "and destroys them. Two groups cannot:\n"
    "• Patients with a severely dysfunctional immune system — this infant with severe combined "
    "immunodeficiency, and congenital T-cell deficiencies generally\n"
    "• Patients whose donor PARTIALLY matches their HLA type — which is exactly why directed donation "
    "from relatives is discouraged. If a mother is HLA A2/A3 and the child inherited A3 from her and "
    "A3 from the father, the child's immune system sees her cells as sufficiently self and tolerates "
    "them, while her donor lymphocytes recognize the child's paternal antigen as foreign and attack. "
    "One-way recognition — and relatedness makes it MORE dangerous, not less\n\n"
    "The disease: donor lymphocytes engraft, proliferate and attack recipient tissues including the "
    "BONE MARROW, so every cell line collapses into pancytopenia, with rash, diarrhea and liver "
    "dysfunction, 1–6 weeks after transfusion. Treatment is largely futile and it is usually fatal.\n\n"
    "Prevention is IRRADIATION of the product, and it is the only defence. Irradiation damages the "
    "DNA of residual white cells so they cannot proliferate; red cells have no nucleus and still "
    "function. Note that leukoreduction — which prevents febrile non-hemolytic reactions and HLA "
    "alloimmunization — is NOT sufficient for this purpose.\n\n"
    "The same rule applies to DiGeorge syndrome and other severe T-cell deficiencies, along with the "
    "companion rule that live vaccines are contraindicated in them.\n\n"
    "Educational objective: Residual donor lymphocytes in blood products can engraft in severely "
    "immunocompromised recipients or in recipients partially HLA-matched to a related donor, causing "
    "fatal transfusion-associated graft-versus-host disease; irradiation of the product is the only "
    "prevention, and leukoreduction does not substitute.",
    "Blood contains a few of the donor's immune cells. A baby with no working immune system cannot "
    "kill them, so they take up residence and attack him — and a relative's blood is more dangerous "
    "here, not safer.",
    exim="fig_tx_timeline",
    excap="Transfusion reactions by time of onset — graft-versus-host disease is the late one, at 1–6 "
          "weeks.",
)

# ── 107. TACO versus TRALI (card 15) ───────────────────────────────────────────
q(
    "An 82-year-old woman with chronic kidney disease and heart failure with preserved ejection "
    "fraction is admitted with symptomatic anemia and receives 2 units of red blood cells over 90 "
    "minutes. Thirty minutes after the second unit she becomes acutely breathless and cannot lie "
    "flat. Temperature is 36.8 C (98.2 F), blood pressure is 186/96 mm Hg (baseline 138/78 mm Hg), "
    "pulse is 104/min, and oxygen saturation is 86% on room air. Jugular venous pressure is elevated "
    "to the angle of the jaw, and there are crackles to both mid-zones with an S3. Chest radiography "
    "shows bilateral perihilar opacities with prominent upper lobe vessels and small pleural "
    "effusions. Brain natriuretic peptide is markedly elevated. Which of the following is the most "
    "appropriate treatment?",
    {
        "Epinephrine and airway support":
            "Anaphylaxis presents within minutes of a tiny volume with hypotension, urticaria and "
            "throat tightness, classically in an IgA-deficient recipient with anti-IgA antibodies. "
            "She is hypertensive with no urticaria.",
        "Intravenous furosemide": "",
        "Intravenous hydrocortisone and antihistamine":
            "This treats an allergic or urticarial reaction — hives and itching with stable vital "
            "signs, from a soluble allergen in donor plasma.",
        "Intravenous normal saline bolus":
            "Fluid is the treatment for the hypotension of transfusion-related acute lung injury or "
            "sepsis. Giving more volume to a patient in circulatory overload will worsen her.",
        "Supportive ventilation without diuresis":
            "This is the management of transfusion-related acute lung injury, in which diuresis does "
            "NOT help. Her hypertension, raised jugular venous pressure and high natriuretic peptide "
            "point the other way.",
    },
    "Intravenous furosemide",
    "Transfusion-associated circulatory overload (TACO) — too much volume, too fast, in a patient "
    "with limited cardiac and renal reserve.\n\n"
    "TACO and TRALI are the two most confused entries on the reaction list because both present as a "
    "hypoxic patient with a white-out on chest imaging. Everything else separates them:\n"
    "• TACO — HYPERtension, RAISED jugular venous pressure, an S3, a raised brain natriuretic "
    "peptide, and it RESPONDS TO DIURESIS. Prevention is slower rates, smaller volumes and "
    "pre-emptive diuretics in at-risk patients\n"
    "• TRALI — HYPOtension, NORMAL jugular venous pressure, normal natriuretic peptide, and diuresis "
    "does NOT help. The mechanism is donor anti-HLA antibodies (classically from a multiparous "
    "female donor) activating recipient leukocytes in the pulmonary capillaries. Management is "
    "supportive\n\n"
    "The memory hook: TACO = Too much volume. TRALI = the donor's antibodies attacked the Lung.\n\n"
    "Whatever the reaction turns out to be, the first five steps are the same: STOP the transfusion; "
    "keep the intravenous line open with normal saline through fresh tubing; perform the CLERICAL "
    "CHECK of unit against patient identity, which is where the fatal ABO error is caught; see and "
    "treat (oxygen for hypoxia, antihistamine for hives, escalating to steroids or epinephrine); and "
    "send the unit, the tubing and fresh samples to the blood bank. You stop the exposure before you "
    "diagnose it, because the two most lethal reactions — acute hemolysis and anaphylaxis — are "
    "dose-dependent.\n\n"
    "Educational objective: Transfusion-associated circulatory overload causes hypoxemia with "
    "HYPERtension, raised jugular venous pressure and a high natriuretic peptide, and responds to "
    "diuresis; transfusion-related acute lung injury causes hypoxemia with hypotension and a normal "
    "jugular venous pressure and does not.",
    "Two units of blood went in faster than her weak heart and kidneys could handle, so fluid backed "
    "up into her lungs. A diuretic pulls that extra fluid off.",
    exim="fig_tx_timeline",
    excap="Transfusion reactions by time of onset — circulatory overload occurs during or within "
          "hours of the transfusion.",
)

# ── 108. White clot versus red clot (card 17) ──────────────────────────────────
q(
    "A 68-year-old man with newly diagnosed atrial fibrillation comes to the office to discuss stroke "
    "prevention. He has hypertension and diabetes mellitus. He has no history of bleeding, his renal "
    "function is normal, and echocardiography shows no valvular abnormality. He says he would prefer "
    "to take low-dose aspirin, which he already takes for cardiovascular prevention, rather than "
    "start a new medication. Which of the following best explains why an anticoagulant is "
    "recommended instead?",
    {
        "Aspirin inhibits platelet aggregation but does not interrupt fibrin formation": "",
        "Aspirin is inactivated by a genetic polymorphism in most patients":
            "It is CLOPIDOGREL that is a prodrug requiring CYP2C19, so that poor metabolizers get "
            "little benefit. Aspirin acts directly and irreversibly on cyclooxygenase-1.",
        "Aspirin causes more intracranial bleeding than a direct oral anticoagulant":
            "Direct oral anticoagulants actually have lower intracranial bleeding rates than "
            "warfarin, and the argument for them here is efficacy against this kind of clot, not a "
            "bleeding comparison with aspirin.",
        "Aspirin loses effect because platelets are replaced within 24 hours":
            "Aspirin inhibits cyclooxygenase irreversibly and a platelet cannot make new enzyme, so a "
            "single dose lasts that platelet's 7–10 day life — which is why it is stopped a week "
            "before surgery.",
        "Aspirin requires monitoring that a direct oral anticoagulant does not":
            "Neither aspirin nor a direct oral anticoagulant requires routine monitoring; warfarin "
            "does.",
    },
    "Aspirin inhibits platelet aggregation but does not interrupt fibrin formation",
    "White clot versus red clot — one distinction that answers a surprising number of 'which drug' "
    "questions.\n\n"
    "• ARTERIAL clots are PLATELET-rich ('white clots'), formed under high shear at a ruptured "
    "atherosclerotic plaque. Treat with ANTIPLATELET drugs: myocardial infarction, ischemic stroke "
    "from plaque, peripheral arterial disease, coronary stents\n"
    "• VENOUS and stasis clots are FIBRIN- and red-cell-rich ('red clots'), formed where blood is "
    "moving slowly. Treat with ANTICOAGULANTS: deep vein thrombosis, pulmonary embolism, and the clot "
    "that forms in a fibrillating left atrial appendage\n\n"
    "Fast blood makes white clots; slow blood makes red ones. The clot in atrial fibrillation forms "
    "in a quivering, poorly emptying appendage — a stasis clot. Aspirin blocks thromboxane-mediated "
    "platelet aggregation, which is not the dominant mechanism there, so it is substantially inferior "
    "to anticoagulation for stroke prevention in atrial fibrillation. To prevent a fibrin-rich clot "
    "you must interrupt the coagulation cascade — which is what apixaban does at factor Xa.\n\n"
    "The same logic explains why aspirin is not an answer for a deep vein thrombosis, and why, after "
    "venous thromboembolism, extended prevention with a low-dose direct oral anticoagulant is "
    "markedly better than aspirin and no less safe.\n\n"
    "Educational objective: Platelet-rich arterial 'white clots' are treated with antiplatelet drugs, "
    "whereas fibrin-rich venous and stasis 'red clots' — including the atrial appendage clot of "
    "atrial fibrillation — require anticoagulation, because aspirin does not interrupt fibrin "
    "formation.",
    "Clots in fast-moving arteries are built mostly of platelets; clots in slow-moving blood are built "
    "mostly of fibrin mesh. Aspirin only handles the platelet kind.",
    exim="fig_slide_kp_antiplatelet",
    excap="The antiplatelet summary — mechanism by agent, and the arterial indications they serve.",
)

# ── 109. Monitoring low-molecular-weight heparin (card 41) ─────────────────────
q(
    "A 34-year-old woman at 26 weeks' gestation is treated with therapeutic-dose subcutaneous "
    "enoxaparin for a proximal deep vein thrombosis. Her body mass index is 41 kg/m2 and her "
    "creatinine clearance is 96 mL/min. On hospital day 2 the covering resident notes that the "
    "activated partial thromboplastin time is 32 seconds (N=25–40 sec) and proposes increasing the "
    "dose, concerned that she is under-anticoagulated. Which of the following is the most "
    "appropriate response?",
    {
        "Increase the enoxaparin dose until the partial thromboplastin time is prolonged":
            "This titrates to a test the drug barely affects, and would risk a substantial overdose "
            "in a pregnant patient.",
        "Measure an anti-factor Xa level rather than the partial thromboplastin time": "",
        "Measure the international normalized ratio instead":
            "The INR reflects the vitamin K-dependent factors and is the monitoring test for "
            "WARFARIN, which is teratogenic and contraindicated here.",
        "Switch to unfractionated heparin so the partial thromboplastin time can be followed":
            "Unfractionated heparin is a reasonable choice when renal function is poor or rapid "
            "reversal may be needed, but switching purely to use a familiar test is the wrong reason. "
            "Low-molecular-weight heparin is preferred in pregnancy.",
        "Switch to warfarin with a target international normalized ratio of 2 to 3":
            "Warfarin crosses the placenta and is teratogenic. Heparins do not cross and are the "
            "anticoagulants of pregnancy.",
        "Continue the current dose without any laboratory monitoring":
            "No monitoring is right for MOST patients on low-molecular-weight heparin — but pregnancy "
            "is one of the three situations where an anti-factor Xa level is checked, along with "
            "obesity and renal impairment. She has two of them.",
    },
    "Measure an anti-factor Xa level rather than the partial thromboplastin time",
    "Chain length decides which test works, and the mechanism is worth reciting.\n\n"
    "Heparins have no anticoagulant action of their own — they bind ANTITHROMBIN and accelerate it. "
    "To inactivate THROMBIN, antithrombin and thrombin must be BRIDGED together, and only a long "
    "heparin tail can span that bridge. To inactivate FACTOR Xa, no bridge is needed: once heparin "
    "has activated antithrombin, antithrombin does the job alone, and a short chain suffices.\n\n"
    "• UNFRACTIONATED heparin (long chains) — strong anti-thrombin AND anti-Xa activity → the aPTT "
    "works, target 1.5–2.5 times normal (anti-Xa 0.3–0.7 U/mL is also valid)\n"
    "• LOW-MOLECULAR-WEIGHT heparin and FONDAPARINUX (short chains) — weak anti-thrombin, strong "
    "anti-Xa → the aPTT has almost nothing to detect, so anti-factor Xa is the ONLY valid assay\n\n"
    "A normal aPTT on enoxaparin therefore says nothing about whether the patient is anticoagulated. "
    "Most patients need no monitoring at all — predictable dosing is the point of the drug — but "
    "check an anti-factor Xa level in PREGNANCY, OBESITY or RENAL IMPAIRMENT. Targets: 0.5–1.0 U/mL "
    "for twice-daily dosing, 1.0–2.0 U/mL for once-daily.\n\n"
    "Two related facts from the same mechanism: fondaparinux is the minimal five-sugar sequence, pure "
    "anti-Xa, does not bind platelet factor 4 (so it does not cause heparin-induced thrombocytopenia "
    "and can be used to treat it), and has no effective reversal agent — protamine fully reverses "
    "unfractionated heparin but only partially (about 60%) reverses low-molecular-weight heparin.\n\n"
    "Educational objective: Only long heparin chains bridge antithrombin to thrombin, so the aPTT "
    "monitors unfractionated heparin but not low-molecular-weight heparin or fondaparinux, which "
    "require an anti-factor Xa level — checked in pregnancy, obesity and renal impairment.",
    "This blood thinner mostly blocks one specific clotting step, and the usual clotting test barely "
    "notices it. A different blood test measures it properly.",
    exim="fig_slide_heparin_chem",
    excap="Heparin chain length — the long tail is what bridges antithrombin to thrombin, and what "
          "the aPTT detects.",
)

# ── 110. Pseudothrombocytopenia (card 27) ──────────────────────────────────────
q(
    "A 46-year-old woman comes to the office for a routine preoperative evaluation before elective "
    "cholecystectomy. She feels well. She has never had abnormal bleeding, including two uneventful "
    "vaginal deliveries and a wisdom tooth extraction. She takes no medications. Examination shows no "
    "petechiae, purpura or mucosal bleeding, and no splenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 13.4 g/dL (N=12.0–16.0 g/dL)\n"
    "Leukocyte count 6,900/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 19,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 13 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 31 sec (N=25–40 sec)\n\n"
    "The analyzer flags the sample. Which of the following is the most appropriate next step?",
    {
        "Admit for platelet transfusion before surgery":
            "Transfusing on an artefactual count exposes her to a transfusion reaction for no reason "
            "— one of the specific harms this flag exists to prevent.",
        "Begin corticosteroids for immune thrombocytopenia":
            "Immune thrombocytopenia is the commonest cause of a genuinely low platelet count, but it "
            "usually produces petechiae or mucosal bleeding at this level, and the diagnosis should "
            "not be made on an unverified number.",
        "Perform a bone marrow biopsy":
            "An invasive test for a number that has not yet been confirmed. Marrow examination is for "
            "unexplained pancytopenia or suspected primary marrow disease.",
        "Repeat the count on a citrate-anticoagulated sample and review the smear": "",
        "Send von Willebrand factor antigen and ristocetin cofactor activity assays":
            "Von Willebrand testing is the right move for mucocutaneous bleeding with a normal "
            "screen, because the plasma clotting assays cannot see platelet adhesion. She has no "
            "bleeding history at all.",
    },
    "Repeat the count on a citrate-anticoagulated sample and review the smear",
    "Pseudothrombocytopenia from EDTA-dependent platelet clumping — and the clue is the ABSENCE of "
    "bleeding. A platelet count of 19,000/µL in a completely asymptomatic outpatient should not be "
    "believed before it is checked; genuine thrombocytopenia at that level usually shows petechiae or "
    "mucosal bleeding.\n\n"
    "The mechanism is the analyzer's size window. Impedance counting assigns identity by SIZE, so "
    "anything the wrong size for its identity is counted as the wrong thing:\n"
    "• TOO SMALL, counted as platelets → schistocytes, microcytes and white cell fragments falsely "
    "RAISE the platelet count\n"
    "• TOO LARGE to be a platelet, therefore missed → platelet CLUMPS and giant platelets falsely "
    "LOWER it (clumps may even be counted as leukocytes)\n\n"
    "The responsible antibody is EDTA-dependent, so the fix is to redraw in a CITRATE (blue top) tube "
    "and confirm clumping directly on the smear. A fluorescent platelet count also helps, because it "
    "identifies platelets by staining their contents rather than by size, and correlates with "
    "CD41/CD61 flow cytometry.\n\n"
    "The harm of believing the number is concrete: it triggers a hematology referral, a marrow "
    "biopsy, a cancelled operation or a platelet transfusion the patient never needed.\n\n"
    "The habit worth taking from this: before acting on a startling complete blood count, ask whether "
    "the numbers are internally consistent — does the hematocrit fit the rule of three, is the MCHC "
    "physically possible, and was the tube full, fresh and properly inverted?\n\n"
    "Educational objective: EDTA-dependent platelet clumping produces pseudothrombocytopenia — a very "
    "low count in a patient with no bleeding — because clumps fall outside the analyzer's platelet "
    "size window; confirm on the smear and repeat the count in a citrate tube.",
    "Her platelets stuck together into clumps inside the collection tube, and the machine could not "
    "count clumps, so it reported far too few. The giveaway is that she has no bruising at all.",
    exim="fig_slide_coulter",
    excap="The Coulter principle — cells are identified by size, which is why anything the wrong size "
          "is counted as the wrong thing.",
)

# ── 111. Burr cells versus spur cells (card 28) ────────────────────────────────
q(
    "A 63-year-old man is evaluated for anemia. He has end-stage kidney disease and receives "
    "hemodialysis three times weekly. He drinks no alcohol, and hepatic function tests are normal "
    "with a normal albumin. Hemoglobin is 9.4 g/dL (N=13.5–17.5 g/dL), mean corpuscular volume is 89 "
    "µm3 (N=80–100 µm3) and the reticulocyte count is 0.6% (N=0.5%–1.5%). The peripheral smear, made "
    "promptly from a fresh sample, shows numerous erythrocytes bearing many short, blunt projections "
    "distributed evenly around the entire circumference of each cell. Which of the following terms "
    "best describes these cells, and what do they indicate?",
    {
        "Acanthocytes, indicating severe liver disease":
            "Acanthocytes (spur cells) have FEW, IRREGULAR, unevenly spaced projections and point to "
            "severe liver disease, abetalipoproteinemia or asplenia. His liver tests and albumin are "
            "normal.",
        "Codocytes, indicating a hemoglobinopathy":
            "Target cells have a central bull's-eye of hemoglobin and reflect excess membrane "
            "relative to contents — thalassemia, hemoglobin C, liver disease or post-splenectomy.",
        "Dacryocytes, indicating marrow fibrosis":
            "Tear-drop cells have a single pointed end and, with immature white cells and nucleated "
            "red cells, indicate marrow infiltration or myelofibrosis.",
        "Echinocytes, indicating uremia": "",
        "Schistocytes, indicating microangiopathy":
            "Schistocytes are angular FRAGMENTS with two pointed edges and no central pallor, "
            "produced by mechanical shearing in a microangiopathy or on a prosthetic valve.",
        "Spherocytes, indicating immune hemolysis":
            "Spherocytes are small, round and dense with no central pallor, from membrane loss in "
            "hereditary spherocytosis or antibody-mediated hemolysis.",
    },
    "Echinocytes, indicating uremia",
    "Burr cells versus spur cells — two spiky red cells that are constantly confused, and the "
    "distinction is worth having because one is a finding and the other is often an artefact.\n\n"
    "• ECHINOCYTE (burr cell) — MANY, REGULAR, EVENLY SPACED short spicules around the whole cell. "
    "Points to uremia and renal failure — or, very commonly, to a preparation artefact from slow "
    "drying, prolonged storage before smearing, or a stain pH problem. This smear was made promptly "
    "from a fresh sample, which is what makes the finding real here\n"
    "• ACANTHOCYTE (spur cell) — FEW, IRREGULAR, unevenly spaced blunt projections. Points to severe "
    "liver disease, abetalipoproteinemia and the post-splenectomy state\n\n"
    "The shortest version: BURR = kidney, SPUR = liver.\n\n"
    "His anemia itself is the anemia of chronic kidney disease — normocytic with a low reticulocyte "
    "count, because the failing kidney no longer makes enough erythropoietin.\n\n"
    "The rest of the morphology atlas, as one-line pairings: spherocyte (ball, no central pallor) → "
    "hereditary spherocytosis or autoimmune hemolysis; bite cell → G6PD deficiency; target cell "
    "(bull's-eye) → thalassemia, hemoglobin C, liver disease, post-splenectomy — and always send an "
    "electrophoresis, because thalassemia cannot be called from a smear; tear-drop cell → "
    "myelofibrosis or marrow infiltration; schistocyte (fragment) → microangiopathy; Howell-Jolly body "
    "→ absent or non-functioning spleen; polychromasia → reticulocytes, meaning the marrow is "
    "responding.\n\n"
    "Educational objective: Echinocytes (burr cells) have many evenly spaced spicules and indicate "
    "uremia or a smear artefact, whereas acanthocytes (spur cells) have few irregular projections and "
    "indicate severe liver disease — burr for kidney, spur for liver.",
    "Both kinds of cell look spiky, but the spikes differ: even, all-around spikes point to kidney "
    "failure, while a few uneven ones point to liver disease.",
    exim="fig_slide_morph_panel",
    excap="The red cell morphology panel — spherocytes, elliptocytes, stomatocytes, tear-drops, "
          "targets, acanthocytes and echinocytes side by side.",
)

# ── 112. Timing separates the immunodeficiencies (card 32) ─────────────────────
q(
    "Two infants are evaluated for recurrent infection. Infant A was entirely well until 7 months of "
    "age and has since had four episodes of otitis media, one pneumococcal pneumonia and a perineal "
    "abscess; he is growing normally, and examination shows no palpable tonsils. Infant B has had "
    "chronic diarrhea, oral thrush that recurs after treatment, and Pneumocystis jirovecii pneumonia, "
    "all beginning at 8 weeks of age; he is at the 3rd percentile for weight. Which of the following "
    "best explains the difference in the age at which their infections began?",
    {
        "Infant A has a phagocyte defect, which manifests later than a lymphoid defect":
            "Chronic granulomatous disease presents in childhood with catalase-positive abscesses and "
            "granulomas, and a normal neutrophil count. It is not defined by a 6-month window.",
        "Maternal antibody protects the antibody arm but not the cellular arm": "",
        "Maternal antibody protects the cellular arm but not the antibody arm":
            "The direction is reversed. Transferred antibody cannot substitute for T cells; it is the "
            "humoral arm that is temporarily covered.",
        "Maternal lymphocytes persist in the infant for several months after birth":
            "Maternal lymphocytes do not provide durable cellular immunity to the infant; engrafting "
            "donor lymphocytes cause graft-versus-host disease rather than protection.",
        "Solid food introduction at 6 months alters mucosal immunity":
            "Weaning changes antigen exposure, but it does not explain a T-cell pattern of infection "
            "from 8 weeks in the second infant.",
    },
    "Maternal antibody protects the antibody arm but not the cellular arm",
    "Timing is the discriminator between the two commonest patterns of primary immunodeficiency, and "
    "the explanation is a single piece of physiology: maternal IgG crosses the PLACENTA and protects "
    "the infant until it wanes at around 6 months. It replaces antibody — and only antibody.\n\n"
    "• INFANT A — well for about 6 months, then recurrent PYOGENIC bacterial infections (Haemophilus, "
    "Streptococcus, Staphylococcus) with absent tonsils. This is BRUTON X-LINKED "
    "AGAMMAGLOBULINEMIA: a BTK mutation blocks development at the pre-B cell stage. Flow cytometry "
    "shows NO CD19/CD20 B cells, all immunoglobulin classes are low, and lymphoid tissue is scanty "
    "because it is mostly B cells. Treat with monthly immunoglobulin infusions; transplant is "
    "currently the only cure\n"
    "• INFANT B — sick from the FIRST MONTHS with Pneumocystis, thrush, chronic diarrhea and failure "
    "to thrive. This is SEVERE COMBINED IMMUNODEFICIENCY, where maternal antibody never covered the "
    "T-cell arm. An absolute lymphocyte count below 2,000/µL warrants evaluation, and the newborn "
    "screen measures T-cell receptor excision circles — a by-product of normal T-cell receptor "
    "rearrangement, absent when no new T cells are being made. Untreated, death usually occurs within "
    "a year; outcome depends on allogeneic stem cell transplant, and the earlier the better\n\n"
    "Note the antibody arm dominates the whole category: antibody deficiencies are about 65% of "
    "primary immunodeficiencies, combined defects 15%, phagocyte disorders 10%, cellular defects 5% "
    "and complement 5%. And read the maturation tree from the top down — the higher the block, the "
    "worse the disease.\n\n"
    "Educational objective: Placentally transferred maternal IgG protects the humoral arm for about 6 "
    "months, so antibody deficiencies such as Bruton agammaglobulinemia present after that window "
    "with pyogenic infections, whereas T-cell and combined defects such as severe combined "
    "immunodeficiency present in the first months with opportunistic infection and failure to thrive.",
    "Babies borrow their mother's antibodies before birth, and those run out at about six months — so "
    "a baby missing his own antibodies looks fine until then. Nothing is borrowed for the T-cell side, "
    "so that kind of problem shows up almost immediately.",
    exim="fig_slide_maturation_tree",
    excap="The lymphocyte maturation tree with the block of each immunodeficiency marked — the higher "
          "the block, the more severe the disease.",
)

# ── 113. CD23 splits the CD5-positive B-cell neoplasms (card 47) ───────────────
q(
    "A 68-year-old man comes to the office due to 4 months of abdominal fullness and night sweats. "
    "Examination shows widespread lymphadenopathy and a spleen palpable 8 cm below the costal margin. "
    "Colonoscopy performed for iron deficiency shows multiple small mucosal polyps throughout the "
    "colon, and biopsy shows a monotonous infiltrate of small lymphoid cells with irregular nuclear "
    "contours. Flow cytometry of the blood shows a clonal B-cell population expressing CD19, CD20 and "
    "CD5, and negative for CD23. Which of the following additional findings is most likely?",
    {
        "BCL2 expression with t(14;18)":
            "That is follicular lymphoma, which is CD10 POSITIVE and CD5 negative, and grows in "
            "crowded back-to-back follicles rather than as a CD5-positive circulating clone.",
        "Cyclin D1 overexpression with t(11;14)": "",
        "MYC rearrangement with t(8;14)":
            "Burkitt lymphoma is CD10 positive, BCL2 negative, with a starry-sky pattern and a Ki-67 "
            "above 95% — a very different tempo and phenotype.",
        "MYD88 mutation with an IgM paraprotein":
            "This is lymphoplasmacytic lymphoma (Waldenström macroglobulinemia), which is CD5 "
            "negative and causes hyperviscosity.",
        "PML-RARA fusion from t(15;17)":
            "That defines acute promyelocytic leukemia, a myeloid disease presenting with a "
            "coagulopathy.",
        "Smudge cells with a mutated IgVH gene":
            "Smudge cells and IgVH mutation status belong to chronic lymphocytic leukemia — the CD23 "
            "POSITIVE member of this pair, and the indolent one.",
    },
    "Cyclin D1 overexpression with t(11;14)",
    "Mantle cell lymphoma. CD5 is normally a T-CELL marker, so a CD20-positive B-cell neoplasm that "
    "also expresses CD5 is distinctly unusual — and only two important diseases do it. CD23 splits "
    "them:\n"
    "• CD23 POSITIVE → chronic lymphocytic leukemia / small lymphocytic lymphoma — indolent, often "
    "never needs treatment, smudge cells on the smear\n"
    "• CD23 NEGATIVE → MANTLE CELL LYMPHOMA — t(11;14) placing cyclin D1 under the immunoglobulin "
    "heavy chain promoter, and 'aggressive, and everyone relapses'\n\n"
    "The distinction changes everything about prognosis and management, which is why it is worth a "
    "question on its own.\n\n"
    "Mantle cell features that fit this vignette: rare, about twice as common in men, median age 68, "
    "and about 90% have gastrointestinal involvement — the colonic polyps here are lymphomatous "
    "polyposis. Counter-intuitively, a leukemic phase ALONE is the LOW-risk group; high risk means "
    "symptomatic disease, 17p deletion, a blastoid variant, a raised lactate dehydrogenase or a high "
    "proliferation index.\n\n"
    "The wider framework for a mature B-cell neoplasm, which resolves most flow cytometry questions "
    "in two steps: CD5 positive → chronic lymphocytic leukemia or mantle cell (split by CD23). CD10 "
    "positive → germinal centre origin — follicular, Burkitt, a subset of diffuse large B-cell "
    "lymphoma. Both negative → marginal zone, lymphoplasmacytic or hairy cell leukemia.\n\n"
    "Educational objective: Chronic lymphocytic leukemia and mantle cell lymphoma are the two "
    "CD5-positive B-cell neoplasms; CD23 positivity indicates chronic lymphocytic leukemia, while CD23 "
    "negativity with t(11;14) and cyclin D1 overexpression indicates the far more aggressive mantle "
    "cell lymphoma.",
    "Two blood cancers look almost identical on the flow machine because both wear a marker that "
    "normally belongs to a different cell type. One extra marker tells them apart — and one is mild "
    "while the other always comes back.",
    exim="fig_lpd_neoplasm_origin_map",
    excap="The mature B-cell neoplasms mapped onto their normal counterparts, with the CD5 and CD10 "
          "split that resolves the differential.",
)

# ── 114. MGUS versus smoldering myeloma (card 48) ──────────────────────────────
q(
    "A 68-year-old woman is found to have a total protein of 8.6 g/dL on a routine panel. She feels "
    "well, with no bone pain, fatigue or infections.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 13.1 g/dL (N=12.0–16.0 g/dL)\n"
    "Calcium 9.3 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Creatinine 0.8 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Albumin 4.0 g/dL (N=3.5–5.5 g/dL)\n\n"
    "Serum protein electrophoresis shows an IgG monoclonal protein of 1.9 g/dL, serum free light "
    "chains are only mildly abnormal, bone marrow biopsy shows 7% clonal plasma cells, and a skeletal "
    "survey shows no lytic lesions. Which of the following is the most appropriate management?",
    {
        "Autologous stem cell transplantation":
            "Transplant is part of treatment for active multiple myeloma in a fit patient, not for a "
            "precursor state with no end organ damage.",
        "Begin bortezomib, lenalidomide and dexamethasone":
            "Triplet therapy treats ACTIVE myeloma. Neither precursor state is treated — end organ "
            "damage is what converts them into a disease requiring therapy.",
        "Begin monthly bisphosphonate therapy":
            "Bisphosphonates reduce skeletal events in myeloma with bone disease. She has no lytic "
            "lesions and a normal calcium.",
        "Repeat laboratory surveillance every 6 months": "",
        "Repeat positron emission tomography every 4 months":
            "More intensive surveillance — laboratory studies every 4 months and consideration of an "
            "annual PET scan — belongs to SMOLDERING myeloma, whose early risk is roughly ten times "
            "higher.",
    },
    "Repeat laboratory surveillance every 6 months",
    "Monoclonal gammopathy of undetermined significance (MGUS). Two numbers separate the precursor "
    "states, and they are worth memorizing as a pair — 10 and 3:\n"
    "• MGUS — marrow plasma cells UNDER 10% AND monoclonal protein UNDER 3 g/dL\n"
    "• SMOLDERING MYELOMA — plasma cells 10%–60% OR monoclonal protein 3 g/dL or more\n\n"
    "She is below both thresholds (7% and 1.9 g/dL) with no end organ damage, so this is MGUS.\n\n"
    "Neither precursor state is treated. What converts either into active myeloma requiring therapy "
    "is END ORGAN DAMAGE — the CRAB tetrad: hyperCalcemia, Renal failure, Anemia, Bone lesions. Her "
    "calcium, creatinine, hemoglobin and skeletal survey are all normal.\n\n"
    "The difference that drives surveillance intensity is the shape of the risk curve:\n"
    "• MGUS progresses at a FLAT 1% per year — so an older patient with MGUS is far more likely to "
    "die of something else. Surveillance is electrophoresis, serum free light chains, a complete blood "
    "count and a metabolic panel every 6 MONTHS, with a skeletal survey at least annually\n"
    "• SMOLDERING myeloma is FRONT-LOADED — 10% per year for the first 5 years, then 3% per year for "
    "5 years, then 1% per year. Hence laboratory studies every 4 MONTHS and consideration of an "
    "annual PET scan, with intensity relaxing once a patient has passed the early high-risk window\n\n"
    "The counseling point is real reassurance combined with genuine commitment to follow-up, because "
    "the 1% per year does not stop.\n\n"
    "Educational objective: MGUS is defined by fewer than 10% marrow plasma cells AND a monoclonal "
    "protein under 3 g/dL with no end organ damage, and progresses at a flat 1% per year, so it is "
    "monitored every 6 months rather than treated; smoldering myeloma exceeds either threshold and "
    "carries a front-loaded 10% annual risk in the first 5 years.",
    "She has an abnormal antibody in her blood but no damage anywhere — no bone holes, no kidney "
    "problem, no anemia. That gets watched with blood tests twice a year, not treated.",
)

# ── 115. The left internal jugular line and chylothorax (card 51) ──────────────
q(
    "A 58-year-old man in the intensive care unit requires central venous access for vasopressors. A "
    "resident attempts a LEFT internal jugular approach; the guidewire passes but the catheter will "
    "not thread, so the equipment is withdrawn and a second attempt on the same side is successful. "
    "The immediate post-procedure chest radiograph shows correct catheter position and no "
    "pneumothorax. Enteral feeding is started overnight. The following morning the patient is more "
    "hypoxic, and chest radiography shows complete opacification of the LEFT hemithorax. Thoracentesis "
    "yields milky, triglyceride-rich fluid. Which of the following structures was most likely injured?",
    {
        "Left brachiocephalic vein":
            "Venous laceration produces a hemothorax — blood, not chyle — and would usually declare "
            "itself promptly with hypotension and a falling hemoglobin.",
        "Left phrenic nerve":
            "Phrenic injury elevates the hemidiaphragm and impairs ventilation, but it produces no "
            "pleural fluid.",
        "Left subclavian artery":
            "Arterial puncture causes bleeding, a hematoma or a hemothorax — again blood rather than "
            "chyle, and typically evident at the time.",
        "Parietal pleural apex":
            "Pleural injury causes a pneumothorax, which the immediate film specifically excluded.",
        "Thoracic duct": "",
    },
    "Thoracic duct",
    "Chylothorax from thoracic duct injury during left internal jugular cannulation — the reason the "
    "left internal jugular is the line you should not place.\n\n"
    "The anatomy: the THORACIC DUCT drains everything except the right upper body — the entire lower "
    "body, the abdomen, the left thorax, the left arm and the left head and neck — and it enters the "
    "venous system at the POSTERIOR wall of the confluence of the LEFT subclavian and LEFT internal "
    "jugular veins. That is directly in the path of a left internal jugular needle. The RIGHT "
    "lymphatic duct drains only the right upper body and carries far less volume, so injury there "
    "matters much less.\n\n"
    "The mechanism of injury explains the delay in this vignette exactly: the needle and wire may "
    "enter the duct rather than the vein, and it is the DILATOR that does the damage. The catheter "
    "will not thread, so everything is withdrawn, a second attempt succeeds, and the immediate film "
    "looks entirely normal — because chyle has to accumulate. Overnight enteral feeding increases "
    "chyle flow, and by morning the hemithorax is white.\n\n"
    "Why it is so hard to fix: the duct is only 2–3 mm across and peripheral lymphatics are the width "
    "of pencil lead — you cannot sew pencil lead, which is why there is no good surgical option for "
    "lymphatic injury generally. Repair means entering the left chest at the lung apex, and about 90% "
    "of the time nothing can be done; the maneuver of last resort is high-fat feeding to make the "
    "leak visible enough to ligate.\n\n"
    "Use the RIGHT internal jugular, a subclavian or a femoral vein instead.\n\n"
    "Educational objective: The thoracic duct enters the posterior wall of the venous confluence on "
    "the LEFT, so a left internal jugular central line can lacerate it and cause a chylothorax that "
    "appears hours later, after the initial chest film is normal.",
    "The body's main lymph drainpipe empties into a vein just behind the left collarbone — exactly "
    "where that needle goes. Nicking it leaks milky lymph fluid into the chest overnight.",
    exim="fig_lymph_system",
    excap="The lymphatic system — the thoracic duct draining most of the body into the venous "
          "confluence on the left.",
)

# ── 116. Which direct oral anticoagulants need a heparin lead-in (card 53) ─────
q(
    "A 61-year-old man is diagnosed with an acute proximal deep vein thrombosis of the right leg. He "
    "is hemodynamically stable with no bleeding risk factors, his creatinine clearance is 88 mL/min, "
    "his weight is 84 kg, and he has no malignancy, antiphospholipid antibodies or prior thrombosis. "
    "He would prefer an oral agent he can start today without injections. Which of the following "
    "regimens is most appropriate?",
    {
        "Apixaban 10 mg twice daily for 1 week, then 5 mg twice daily": "",
        "Dabigatran 150 mg twice daily started today":
            "Dabigatran is a true oral agent, but its trials used 5–10 days of initial "
            "low-molecular-weight heparin before the switch — it is not a monotherapy starter.",
        "Edoxaban 60 mg daily started today":
            "The same problem as dabigatran: edoxaban requires days of parenteral lead-in first, "
            "despite being a factor Xa inhibitor rather than a thrombin inhibitor.",
        "Enoxaparin for 5 days, overlapping with warfarin until the INR exceeds 2":
            "This is a correct regimen and remains standard where a direct oral anticoagulant is "
            "contraindicated — but it requires the injections he is trying to avoid, plus monitoring, "
            "and carries more bleeding than a DOAC.",
        "Fondaparinux daily with no oral agent":
            "Fondaparinux is a subcutaneous injection, which he wants to avoid, and it has no "
            "effective reversal agent.",
    },
    "Apixaban 10 mg twice daily for 1 week, then 5 mg twice daily",
    "Only two direct oral anticoagulants can be started without a parenteral lead-in, and they are "
    "the two whose trials were designed that way.\n\n"
    "• ONE-DRUG (oral from the first dose, with a loading phase) — APIXABAN 10 mg twice daily for 1 "
    "week then 5 mg twice daily; RIVAROXABAN 15 mg twice daily for 3 weeks then 20 mg daily\n"
    "• TWO-DRUG (parenteral first) — DABIGATRAN and EDOXABAN were studied after 5–10 days of "
    "low-molecular-weight heparin, so they are not monotherapy starters. Warfarin needs bridging "
    "too: overlap with a heparin for at least 5 days AND until the INR has been above 2 for 24–48 "
    "hours\n\n"
    "The memory hook: the two that start with A and R go it alone. Note the trap — dabigatran is a "
    "direct thrombin inhibitor and edoxaban a factor Xa inhibitor, so they are otherwise unrelated; "
    "they share only the lead-in requirement.\n\n"
    "Why a direct oral anticoagulant at all: efficacy equals warfarin, bleeding (especially "
    "intracranial) is lower, and no monitoring is needed — which is why the 2021 CHEST guidance "
    "prefers them for initial and long-term treatment in patients without cancer. Apixaban is the "
    "least renally cleared and has the lowest bleeding rates of the class.\n\n"
    "The carve-outs matter more than the rule, and this patient has none of them: pregnancy or "
    "breastfeeding; massive embolism or iliofemoral thrombosis needing titration or thrombolysis; "
    "extremes of weight; gastric bypass; creatinine clearance below 30 mL/min; heparin-induced "
    "thrombocytopenia; splanchnic vein thrombosis; major enzyme-inducing drug interactions; and above "
    "all ANTIPHOSPHOLIPID SYNDROME, where randomized evidence shows HARM and warfarin is required.\n\n"
    "Educational objective: Apixaban and rivaroxaban can be started orally with a loading dose and no "
    "parenteral lead-in, whereas dabigatran and edoxaban require 5–10 days of low-molecular-weight "
    "heparin first and warfarin requires bridging until the INR is therapeutic.",
    "Two of the newer clot pills can be swallowed from day one at a higher starting dose; the other "
    "two only work in trials after several days of injections first.",
)

# ── 117. Acetaminophen, never NSAIDs, in viral hemorrhagic fever (card 56) ─────
q(
    "A 30-year-old man comes to the emergency department due to 4 days of fever to 39.4 C (102.9 F), "
    "severe headache, pain behind both eyes and severe pain in his lower back and long bones. He "
    "returned 6 days ago from a 2-week stay in Puerto Rico. Examination shows a faint blanching "
    "macular rash over the trunk and scattered petechiae on both shins. Hemoglobin is 15.8 g/dL "
    "(N=13.5–17.5 g/dL), platelet count is 82,000/mm3 (N=150,000–400,000/mm3), and aspartate "
    "aminotransferase is 96 U/L (N=12–38 U/L). Multiplex reverse transcriptase polymerase chain "
    "reaction is positive for dengue virus. Which of the following is the most appropriate analgesic "
    "and antipyretic for this patient?",
    {
        "Acetaminophen": "",
        "Aspirin":
            "Aspirin irreversibly inhibits platelet cyclooxygenase for the platelet's entire 7–10 day "
            "life, which is the last thing to add to a patient who is already thrombocytopenic and "
            "bleeding into the skin. It also risks Reye syndrome in children with a viral illness.",
        "Diclofenac":
            "Another nonsteroidal anti-inflammatory drug, with the same platelet inhibition and an "
            "added gastrointestinal bleeding risk.",
        "Ibuprofen":
            "The commonest wrong answer, because it is the reflex antipyretic. Nonsteroidal "
            "anti-inflammatory drugs inhibit platelet function and increase bleeding risk in a "
            "patient already hemorrhaging into skin and mucosa.",
        "Indomethacin":
            "Also a nonsteroidal anti-inflammatory drug — the class rule applies to all of them.",
        "Ketorolac":
            "A parenteral nonsteroidal anti-inflammatory drug, and among the most potent platelet "
            "inhibitors in the group.",
    },
    "Acetaminophen",
    "Dengue fever — 'breakbone fever' — and the prescribing rule here spans the entire viral "
    "hemorrhagic fever block.\n\n"
    "ACETAMINOPHEN for fever and pain. NEVER nonsteroidal anti-inflammatory drugs — not ibuprofen, "
    "not naproxen, not aspirin. NSAIDs inhibit platelet function and increase bleeding risk, and this "
    "patient is already bleeding into skin and mucosa with a falling platelet count. The rule is "
    "stated for dengue and repeated verbatim for Crimean-Congo hemorrhagic fever; treat it as a class "
    "rule for every agent in the group.\n\n"
    "The diagnosis is built from the classic tier-1 features: travel to an endemic area (Puerto Rico "
    "accounts for most United States dengue), an incubation of 4–7 days, fever with severe headache "
    "and RETRO-ORBITAL pain, musculoskeletal and lumbar 'breakbone' pain, rash, and thrombocytopenia "
    "with transaminitis.\n\n"
    "Watch for progression, because the severity tiers are defined by counting features: moderate "
    "dengue is the base syndrome PLUS ANY TWO of abdominal tenderness, persistent vomiting or mucosal "
    "bleeding; SEVERE dengue is dengue plus ANY ONE of hypovolemic shock, severe bleeding or organ "
    "failure — so a single episode of hypotension reclassifies him.\n\n"
    "There is no antiviral for dengue, hantavirus or Crimean-Congo fever; only Lassa has one "
    "(ribavirin, and it is weak). Management is fluids to prevent dehydration — the single most "
    "important intervention — plus hospitalization for severe cases. Prevention is Aedes vector "
    "control, and the vaccine Dengvaxia is given ONLY to people with documented prior dengue "
    "infection.\n\n"
    "Educational objective: In dengue and every other viral hemorrhagic fever, fever and pain are "
    "treated with acetaminophen and never with nonsteroidal anti-inflammatory drugs, which add "
    "platelet inhibition to an existing bleeding diathesis; care is otherwise supportive with careful "
    "fluid management.",
    "He already has too few platelets and is bleeding into his skin, and the usual fever pills make "
    "platelets work worse. Plain acetaminophen brings the fever down without touching them.",
    exim="fig_dengue_rash",
    excap="The dengue rash — not diagnostic on its own, and more common in children than adults.",
)

# ── 118. Managing an acute porphyria attack (card 61) ──────────────────────────
q(
    "A 29-year-old woman is admitted to the hospital due to 3 days of severe diffuse abdominal pain "
    "with vomiting and constipation, on a background of two similar episodes in the past year. She "
    "began a very low-carbohydrate weight-loss diet 3 weeks ago and has been eating roughly 700 "
    "kcal/day. She is anxious and tearful and reports new weakness climbing stairs. Blood pressure is "
    "158/94 mm Hg and pulse is 116/min. The abdomen is soft and non-tender despite her distress, and "
    "computed tomography shows no abnormality. Serum sodium is 124 mEq/L (N=136–146 mEq/L). A spot "
    "urine collected during the pain shows porphobilinogen 38 times and δ-aminolevulinic acid 15 "
    "times the upper limit of normal. Which of the following is the most appropriate treatment?",
    {
        "Diagnostic laparoscopy":
            "Severe pain with a soft abdomen and normal imaging is the point of the vignette. "
            "Operating adds a major surgical stress, which makes an attack worse.",
        "Hemin and intravenous dextrose": "",
        "Intravenous deferoxamine infusion":
            "Deferoxamine chelates iron in acute iron poisoning. Iron is not the problem here.",
        "Oral hydroxychloroquine":
            "Hydroxychloroquine is used for the SKIN symptoms of porphyria cutanea tarda, the "
            "photocutaneous porphyria. She has no skin lesions and a neurovisceral presentation.",
        "Therapeutic phlebotomy":
            "Phlebotomy unloads iron in porphyria cutanea tarda, which is fundamentally an "
            "iron-related disease. It has no role in an acute neurovisceral attack.",
    },
    "Hemin and intravenous dextrose",
    "An acute intermittent porphyria attack, precipitated by fasting. Both treatments work through "
    "the same feedback loop, which is why understanding the loop is worth more than memorizing the "
    "drugs.\n\n"
    "HEME inhibits ALA SYNTHASE 1, the first and rate-limiting enzyme of heme synthesis. When a "
    "downstream enzyme is deficient → less heme is made → less inhibition reaches ALA synthase 1 → "
    "the enzyme revs up → the pathway floods with the precursors that accumulate above the block. "
    "Porphyria is therefore a disease of PRECURSOR ACCUMULATION, not of heme deficiency itself.\n\n"
    "That explains every precipitant — anything that raises demand for heme or upregulates ALA "
    "synthase 1: FASTING and low carbohydrate intake (through PGC-1alpha, and her 700 kcal "
    "low-carbohydrate diet is the trigger here), cytochrome P450-inducing drugs (which consume heme), "
    "sex hormones including menstruation, infection, stress, alcohol, illicit drugs and smoking.\n\n"
    "And it explains both treatments:\n"
    "• GLUCOSE/dextrose — glucose and insulin suppress PGC-1alpha, and therefore ALA synthase 1. That "
    "is the entire rationale for carbohydrate loading\n"
    "• HEMIN — restores the end-product negative feedback directly, switching ALA synthase 1 off from "
    "the other end\n"
    "Alongside these: remove every provoking factor, manage the hyponatremia (often from the syndrome "
    "of inappropriate antidiuretic hormone secretion), and refer to a porphyria centre for genetic "
    "confirmation.\n\n"
    "The diagnosis was made correctly here: a SPOT urine collected DURING the symptoms, sent for "
    "porphobilinogen, δ-aminolevulinic acid and creatinine, with more than 2–4 times the upper limit "
    "confirming an attack. Both precursors are raised, which places the block at PBG deaminase; lead "
    "poisoning blocks one step earlier, so ALA rises while PBG stays NORMAL.\n\n"
    "Educational objective: Acute porphyria attacks are driven by upregulation of ALA synthase 1, so "
    "they are precipitated by fasting, enzyme-inducing drugs and hormones, and treated with hemin "
    "(restoring end-product inhibition) plus glucose (suppressing PGC-1alpha) along with removal of "
    "the precipitant.",
    "Her crash diet revved up the first enzyme of a pathway that is blocked further down, so toxic "
    "half-made chemicals piled up and poisoned her nerves. Sugar and a heme infusion both switch that "
    "first enzyme back off.",
    exim="fig_porph_alas1",
    excap="Why fasting provokes an attack: low carbohydrate intake drives PGC-1alpha, which "
          "upregulates ALA synthase 1.",
)

# ── 119. The two CD4 thresholds and prophylaxis (card 22) ──────────────────────
q(
    "A 36-year-old man is newly diagnosed with HIV infection after presenting with 3 months of oral "
    "thrush and 7 kg of weight loss. He has no fever, cough or breathlessness, and no neurologic "
    "symptoms. His CD4 count is 140/mm3 and HIV RNA is 320,000 copies/mL. Toxoplasma IgG is negative, "
    "a tuberculin skin test is negative, and cryptococcal antigen is negative. Antiretroviral therapy "
    "is started today. Which of the following prophylactic regimens is most appropriate now?",
    {
        "Azithromycin weekly":
            "Prophylaxis against disseminated Mycobacterium avium complex is considered at CD4 counts "
            "below 50/mm3, and is largely unnecessary when antiretroviral therapy is started "
            "promptly. His count is 140.",
        "Fluconazole daily":
            "Antifungal prophylaxis is not routine. His cryptococcal antigen is negative, and "
            "candidiasis is treated when it occurs rather than prevented.",
        "No prophylaxis is indicated at this CD4 count":
            "The threshold for Pneumocystis prophylaxis is 200/mm3, and he is well below it. This is "
            "the trap of confusing the two CD4 numbers.",
        "Trimethoprim-sulfamethoxazole daily": "",
        "Valganciclovir daily":
            "Cytomegalovirus disease — retinitis, esophagitis, colitis — occurs below 50/mm3, and "
            "prophylaxis is not standard; surveillance and treatment of established disease are.",
    },
    "Trimethoprim-sulfamethoxazole daily",
    "Two CD4 numbers do different jobs, and confusing them is the commonest error here:\n"
    "• CD4 BELOW 200/mm3 (or under 14%) DEFINES AIDS — CDC stage 3 — and is the threshold for "
    "Pneumocystis jirovecii prophylaxis. An AIDS-defining opportunistic infection also defines stage "
    "3 at any CD4 count\n"
    "• CD4 BELOW 50/mm3 is where opportunistic infection risk is GREATEST — cytomegalovirus, "
    "Mycobacterium avium complex, cryptococcus, primary central nervous system lymphoma\n\n"
    "At 140/mm3 he needs trimethoprim-sulfamethoxazole, continued until the immune system "
    "reconstitutes on therapy. The prophylaxis table by threshold:\n"
    "• Below 200 — trimethoprim-sulfamethoxazole for Pneumocystis; check a cryptococcal antigen\n"
    "• Below 100 — prophylaxis in Toxoplasma IgG-POSITIVE patients, and trimethoprim-sulfamethoxazole "
    "covers both (his toxoplasma serology is negative, so that indication does not arise)\n"
    "• Any CD4 count — treat latent tuberculosis if the skin test or interferon-gamma release assay "
    "is positive\n\n"
    "Also worth holding: the CD4 count is the STAGING variable — it measures immune damage and drives "
    "prophylaxis — while the viral load is the TRANSMISSION and treatment-response variable, and the "
    "basis of undetectable equals untransmittable. A useful shortcut when the CD4 has not returned: "
    "an absolute lymphocyte count below 1,000/mm3 predicts a CD4 below 200.\n\n"
    "And the live vaccine rule that follows from the same threshold: varicella, yellow fever and "
    "measles-mumps-rubella may be given only when CD4 is 200/mm3 or above; the recombinant zoster "
    "vaccine is the one to use in immunocompromised patients.\n\n"
    "Educational objective: A CD4 count below 200/mm3 defines AIDS and is the threshold for "
    "Pneumocystis prophylaxis with trimethoprim-sulfamethoxazole, whereas below 50/mm3 is where "
    "cytomegalovirus, Mycobacterium avium complex and cryptococcal disease risk is greatest — two "
    "different numbers with two different purposes.",
    "Two different CD4 numbers matter: under 200 means AIDS and time to start a preventive antibiotic; "
    "under 50 is where the rarest, nastiest infections appear. He is in the first group.",
    exim="fig_slide_cd4_oi",
    excap="Opportunistic organisms by CD4 threshold, with the clinical clue for each.",
)

# ── 120. One mutation kills a whole antiretroviral class (card 24) ─────────────
q(
    "A 42-year-old woman with HIV infection has taken a regimen of tenofovir, emtricitabine and "
    "efavirenz for 3 years, with an undetectable viral load until 6 months ago. She reports missing "
    "doses frequently during a period of housing instability. Her HIV RNA is now 68,000 copies/mL and "
    "her CD4 count has fallen from 620 to 410/mm3. Genotypic resistance testing identifies a single "
    "amino acid substitution at position 103 of reverse transcriptase, in a conserved region of the "
    "enzyme's allosteric pocket. Which of the following best describes the consequence of this single "
    "mutation?",
    {
        "It abolishes activity of all non-nucleoside reverse transcriptase inhibitors": "",
        "It abolishes activity of all integrase strand transfer inhibitors":
            "Integrase resistance arises from mutations altering integrase structure, not reverse "
            "transcriptase, and would not follow from a change in this enzyme.",
        "It confers resistance only to the specific drug she is taking":
            "That would be true if the drugs bound different sites — but the entire non-nucleoside "
            "class shares one allosteric pocket, which is precisely why the barrier is so low.",
        "It confers high-level resistance to all protease inhibitors":
            "Protease inhibitors have a HIGH genetic barrier; resistance is uncommon unless the "
            "patient has previously been treated with one, and it requires accumulated mutations.",
        "It prevents nucleoside analogues from being incorporated into viral DNA chains":
            "Nucleoside analogue resistance occurs through point mutations that reduce binding "
            "affinity, and generally requires accumulated mutations rather than a single change.",
    },
    "It abolishes activity of all non-nucleoside reverse transcriptase inhibitors",
    "The non-nucleoside reverse transcriptase inhibitors have the LOWEST genetic barrier to "
    "resistance of any antiretroviral class, and the reason is structural: every member — efavirenz, "
    "doravirine and the rest — binds the SAME allosteric pocket on reverse transcriptase, "
    "non-competitively, causing a conformational change that disables the enzyme. A single point "
    "mutation in that conserved pocket therefore knocks out the whole class at once.\n\n"
    "Compare the rest of the spectrum:\n"
    "• NRTIs — nucleoside analogues that bind competitively at the active site and cause chain "
    "termination. Resistance mutations reduce binding AFFINITY rather than abolishing it, so it "
    "generally takes accumulated mutations\n"
    "• PROTEASE INHIBITORS — a HIGH barrier; resistance is uncommon unless the patient has previously "
    "been treated with one\n"
    "• LENACAPAVIR (capsid inhibitor) — the extreme case in the other direction: a single capsid "
    "mutation confers more than 80,000-fold resistance\n"
    "• INSTIs — resistance arises from mutations altering integrase structure and reducing drug "
    "binding\n\n"
    "The upstream cause is always the same: reverse transcriptase has a high error rate, which "
    "generates the variant pool that selection acts on — and poor adherence supplies the selection "
    "pressure by keeping drug levels in the range where resistant virus outgrows wild type. That is "
    "why adherence support, not simply a new prescription, is half the management here.\n\n"
    "Practical consequence: she needs a new regimen guided by the genotype, and the non-nucleoside "
    "class is closed to her — not just the single drug she was taking.\n\n"
    "Educational objective: All non-nucleoside reverse transcriptase inhibitors bind the same "
    "allosteric pocket, so one point mutation in that conserved region confers resistance to the "
    "entire class; nucleoside analogues generally require accumulated mutations and protease "
    "inhibitors have a high genetic barrier.",
    "Every drug in that family grabs the same handle on the virus's copying enzyme. Change the shape "
    "of that one handle and all of them stop working at once, not just the one she was taking.",
    exim="fig_slide_nnrti",
    excap="The non-nucleoside mechanism — the inhibitor binds reverse transcriptase at an allosteric "
          "pocket shared by the whole class.",
)
