# Key Findings — vignette highlights for Hardest Exam questions 91–120.
# Authoring rules and categories: see highlights_hardest_001_030.py and QUIZ_BUILD_METHOD.md.

F, M, T, P, W = "finding", "mechanism", "term", "pattern", "workup"
EYEBROW = {F: "FINDING", M: "MECHANISM", T: "KEY TERM", P: "PATTERN", W: "WHAT'S ASKED"}


def h(text, cat, title, body):
    return {"text": text, "cat": cat, "eyebrow": EYEBROW[cat], "title": title, "body": body}


HIGHLIGHTS = {

91: [
 h("known vertebral metastases", F, "The tissue at risk",
   "A surge in testosterone is harmless in most men. In a man with established vertebral disease it "
   "expands tumour that already abuts the cord."),
 h("is started on leuprolide alone", M, "The flare phenomenon",
   "A gonadotropin-releasing hormone AGONIST initially STIMULATES the pituitary, raising luteinizing "
   "hormone and testosterone for one to two weeks before receptor downregulation produces the "
   "intended castrate level. Continuous stimulation is what eventually switches the axis off — but "
   "not at first."),
 h("Twelve days later", F, "The timing is diagnostic",
   "Symptoms appearing in the second week after the first dose fit the testosterone surge exactly, "
   "not disease progression, which would not accelerate this abruptly."),
 h("Which of the following would most likely have prevented this complication?", W,
   "Block the receptor before the surge arrives",
   "An anti-androgen such as bicalutamide, started days before the agonist and continued for "
   "several weeks, blocks the androgen receptor so the surge has nowhere to act. The alternative is "
   "a gonadotropin-releasing hormone ANTAGONIST such as degarelix, which lowers testosterone "
   "immediately with no flare at all."),
],

92: [
 h("deep, boring calf pain that she rates 9 out of 10 despite intravenous opioids", F,
   "Pain out of proportion",
   "The earliest and most reliable sign of compartment syndrome. Pain that opioids cannot touch, in "
   "an injury that should not hurt this much, is the finding that should trigger action."),
 h("Passive dorsiflexion of the toes reproduces severe pain", F, "Pain on passive stretch",
   "Stretching the muscle within the swollen compartment reproduces the pain. Together with a tense "
   "compartment, this is enough to make the diagnosis clinically."),
 h("Dorsalis pedis and posterior tibial pulses are palpable and the foot is warm and pink", P,
   "Normal pulses do NOT exclude it",
   "The single most dangerous misconception here. Compartment pressure rises far above the pressure "
   "in thin-walled capillaries and venules long before it approaches systolic arterial pressure, so "
   "tissue is already ischemic while the pulse remains easily palpable. Pulselessness is a late and "
   "ominous sign, not a diagnostic criterion."),
 h("The cast is bivalved, with no relief", W, "The reversible cause has been addressed",
   "Releasing the cast removes external compression. Persistent pain afterwards means the pressure "
   "is inside the compartment, and only fasciotomy will decompress it. Waiting for pressure "
   "measurements or for more signs risks irreversible muscle necrosis within hours."),
],

93: [
 h("Seven weeks ago she underwent an open right inguinal hernia repair", M,
   "Surgery interrupted the drainage",
   "The inguinal nodes and their afferent channels drain the whole leg. Disrupting them removes the "
   "route by which interstitial protein and fluid return to the circulation, and the delay of weeks "
   "to months before swelling appears is typical."),
 h("the toes, which appear squared off", T, "Square toes",
   "Protein-rich fluid trapped in the interstitium causes fibrosis, and the toes take on a boxy "
   "appearance. It is a feature of lymphedema and not of venous or cardiac edema."),
 h("the skin over the dorsum of the foot is thickened and cannot be lifted between finger and thumb "
   "at the second web space", T, "A positive Stemmer sign",
   "Inability to pinch and lift the skin at the base of the second toe is close to pathognomonic for "
   "lymphedema. It is a bedside test with no equipment and it is frequently omitted."),
 h("Compression ultrasonography of the right leg shows no deep vein thrombosis", W,
   "The competing diagnosis is excluded",
   "A unilaterally swollen leg is a deep vein thrombosis until proven otherwise, which is why the "
   "stem proves otherwise. With that removed and the skin changes present, the lymphatics are the "
   "answer."),
],

94: [
 h("a firm, non-tender, 2 cm node fixed to underlying tissue above the left clavicle", T,
   "Virchow node",
   "A hard, fixed LEFT supraclavicular node. Firm, painless and immobile describes malignant "
   "infiltration; a reactive node is soft, tender and mobile."),
 h("epigastric discomfort, early satiety and 8 kg of weight loss", F, "An upper abdominal primary",
   "Gastric carcinoma is the classic source, though pancreatic, esophageal and other abdominal "
   "primaries do the same thing."),
 h("There is no cervical, axillary or inguinal lymphadenopathy elsewhere", P,
   "One node, and the side matters",
   "Isolated left-sided supraclavicular adenopathy is an anatomical statement, not a coincidence. "
   "Generalized adenopathy would suggest lymphoma or a systemic process instead."),
 h("Which of the following best explains why an abdominal primary tumour presents at this site?", W,
   "Follow the plumbing",
   "The thoracic duct carries lymph from the entire abdomen and both legs — everything below the "
   "diaphragm — and empties at the junction of the LEFT subclavian and internal jugular veins. "
   "Tumour cells travelling that route lodge in the last nodes before the venous system. The right "
   "lymphatic duct drains only the right upper body, which is why the finding is left-sided."),
],

95: [
 h("a radiolabelled colloid and blue dye are injected around the tumour", M,
   "The sentinel node concept",
   "The tracer follows the same lymphatic channels a tumour cell would. The first node to take it "
   "up is the first node the tumour would reach, so its status predicts the rest of the basin."),
 h("Which of the following compartments of the node should be examined first?", W,
   "Afferent lymph arrives in one place",
   "Afferent lymphatics pierce the capsule and empty into the SUBCAPSULAR (marginal) SINUS. Tumour "
   "cells arrive there first, so that is where the earliest micrometastatic deposits are found — "
   "which is why sentinel nodes are serially sectioned and examined with cytokeratin stains "
   "focused on that compartment. Flow then continues through cortical and medullary sinuses to the "
   "efferent vessel at the hilum."),
],

96: [
 h("left shoulder pain that worsens when the stretcher is laid flat", T, "Kehr sign",
   "Blood beneath the left hemidiaphragm irritates the phrenic nerve (C3–C5), which is referred to "
   "the left shoulder. Lying flat lets blood track up to the diaphragm, which is why the position "
   "matters."),
 h("blood pressure is 118/74 mm Hg, which remains stable after 1 L of crystalloid", W,
   "Hemodynamic stability decides the pathway",
   "This is the fork in blunt splenic trauma. A STABLE patient can be imaged and managed "
   "non-operatively; an UNSTABLE one goes to the operating room without a CT scan."),
 h("a focus of active contrast extravasation contained within the capsule", F,
   "A contrast blush",
   "Active arterial bleeding. It predicts failure of observation alone, which is precisely what "
   "makes angioembolization the right answer rather than simple monitoring."),
 h("Which of the following is the most appropriate next step in management?", W,
   "Save the spleen if you can",
   "Splenic preservation is the goal, because splenectomy commits the patient to lifelong risk of "
   "overwhelming post-splenectomy infection. Angiographic embolization controls the bleeding while "
   "preserving splenic function."),
],

97: [
 h("blood pressure is 78/44 mm Hg; after 2 L of crystalloid and 2 units of red blood cells, blood "
   "pressure is 82/50 mm Hg and pulse is 128/min", W, "A non-responder",
   "Persistent hypotension despite adequate resuscitation means ongoing hemorrhage. This patient "
   "does not get a CT scan and does not get embolization — she goes to the operating room."),
 h("total splenectomy for a shattered spleen", M, "Two functions lost at once",
   "The spleen filters poorly opsonized encapsulated organisms from the blood and houses the "
   "marginal-zone B cells that respond to polysaccharide antigens. Both are gone, permanently."),
 h("Which of the following is most appropriate before her discharge?", W,
   "The discharge is the intervention",
   "Vaccinate against the ENCAPSULATED organisms — pneumococcus, meningococcus and Haemophilus "
   "influenzae type b — ideally about 14 days after surgery, plus annual influenza. Add antibiotic "
   "prophylaxis and a written warning to seek care urgently with any fever. The patient who "
   "develops overwhelming post-splenectomy infection years later is usually the one who never "
   "received this."),
],

98: [
 h("the instrument reports values ranging from 208,000 to 222,000/mm3", F,
   "Every result is low",
   "Not scattered around the true value of 250,000 but consistently below it. A consistent "
   "displacement in one direction is bias, not random error."),
 h("a standard deviation of 3,600/mm3", F, "Excellent precision",
   "A tight standard deviation means the measurements agree closely with one another. The "
   "instrument is highly REPRODUCIBLE."),
 h("Repeat runs of the same sample agree closely with one another", P,
   "Precision is not accuracy",
   "The distinction the question turns on. PRECISION is agreement among repeated measurements; "
   "ACCURACY is agreement with the true value. An instrument can be exquisitely precise and "
   "consistently wrong — like a tight grouping of shots well off the bullseye."),
 h("Which of the following best describes this instrument's performance, and what should be done?",
   W, "Systematic error is correctable",
   "A reproducible offset from a known standard is a calibration problem, and calibration is the "
   "fix. Random imprecision would instead point to instrument instability or operator technique — "
   "a different problem with a different remedy."),
],

99: [
 h("Jane Doe, date of birth 14 Mar 1998, 14 Elm Street", W, "Patient identifiers are present",
   "Name, date of birth and address are all given, along with the date. Work through the required "
   "elements one at a time rather than reading the prescription as a block — that is the only way "
   "to notice what is absent."),
 h("Ferrous sulfate 325 mg tablets", W, "Drug, strength and formulation are present",
   "The medication itself is fully specified. Note that the ferrous SULFATE 325 mg tablet contains "
   "about 65 mg of elemental iron, which is the number that actually matters clinically."),
 h("Take 1 tablet by mouth three times daily with vitamin C", P,
   "Directions are not a quantity",
   "The Sig tells the patient how to take it — dose, route and frequency are all there — but does "
   "not tell the pharmacist how much to hand over. Frequency and duration together imply a number, "
   "but implying is not prescribing."),
 h("Refills: 2.", W, "The missing element is the amount to dispense",
   "Refills are specified, but a refill of an unspecified quantity means nothing. Without a "
   "QUANTITY the prescription cannot be filled, however complete the rest looks. The prescriber's "
   "name and signature are required as well."),
],

100: [
 h("she has become agitated and restless in the evenings and sleeps poorly", T, "Sundowning",
   "Late-day worsening of confusion and agitation in dementia. It is a behavioural pattern with "
   "identifiable contributors — fatigue, poor light, disrupted routine, unmet needs — rather than a "
   "symptom requiring sedation."),
 h("has had no fever, cough, dysuria or change in bowel habit, and examination and basic laboratory "
   "studies including a urinalysis are unremarkable", W, "Reversible causes excluded",
   "Delirium superimposed on dementia is the first thing to exclude — infection, pain, "
   "constipation, urinary retention, dehydration or a new medication. The stem has done that work."),
 h("Her medications are lisinopril, atorvastatin and acetaminophen", P,
   "No anticholinergic burden",
   "Drugs are a common and reversible cause of agitation in older adults. This list is clean, which "
   "closes another door."),
 h("Her son asks for 'something to calm her down at night'", W,
   "The requested drug is the wrong answer",
   "Antipsychotics in older adults with dementia carry a boxed warning for increased mortality, "
   "along with stroke, falls and extrapyramidal effects, and benzodiazepines worsen confusion and "
   "falls. Non-pharmacologic management comes FIRST: a consistent routine, daytime light and "
   "activity, reduced evening stimulation, and support for the caregiver — whose distress is a real "
   "part of the presentation."),
],

101: [
 h("He follows a strict vegan diet", F, "The dietary source",
   "Vitamin B12 is found almost exclusively in animal products. Hepatic stores last three to five "
   "years, which is why deficiency from diet alone takes so long to appear."),
 h("a wide-based gait, absent ankle reflexes, reduced vibration sense to both knees, and a positive "
   "Romberg sign", F, "Subacute combined degeneration",
   "Demyelination of the dorsal columns and corticospinal tracts. B12 is a cofactor for "
   "methylmalonyl-CoA mutase, and without it abnormal fatty acids are incorporated into myelin. "
   "Folate has no role in this pathway."),
 h("The intern starts oral folic acid 1 mg daily while awaiting further results", P,
   "The error, in one sentence",
   "Folate and B12 both feed the methionine synthase reaction that supplies thymidine for DNA "
   "synthesis. Giving folate bypasses the block in the MARROW, so the blood count improves — while "
   "the separate, B12-dependent neurologic pathway is untouched and continues to degenerate."),
 h("the hemoglobin is 12.8 g/dL and the mean corpuscular volume is 94 µm3, but the patient now "
   "cannot feel his feet and has fallen twice more", W, "Improvement that conceals harm",
   "The most dangerous kind of response: the laboratory markers that would have prompted further "
   "investigation have normalized, removing the signal, while the disease progresses. Never treat "
   "a macrocytic anemia with folate alone — check B12 first, and if both are low, replace B12 "
   "first."),
],

102: [
 h("Mean corpuscular volume  62 µm3", F, "Microcytosis out of proportion",
   "A mean volume this low with a hemoglobin of only 10.6 g/dL is disproportionate. Iron deficiency "
   "severe enough to produce an MCV of 62 would cause a far lower hemoglobin."),
 h("Erythrocyte count  5.6 million/mm3", F, "A HIGH red cell count",
   "The most useful single discriminator. Thalassemia trait produces many small cells, so the count "
   "is normal or raised. Iron deficiency produces FEW small cells, so the count is low. Small cells "
   "in large numbers means thalassemia."),
 h("Red cell distribution width  13.1%", P, "A uniform population",
   "Normal distribution width means the cells are uniformly small. Iron deficiency raises it, "
   "because newly made microcytes circulate alongside older normal cells."),
 h("Ferritin  68 ng/mL", W, "Iron deficiency excluded",
   "Normal iron stores and a normal transferrin saturation remove the default cause of a microcytic "
   "anemia — and mean that empirical iron would be both useless and potentially harmful."),
 h("Which of the following is the most appropriate next step in management?", W,
   "Three microcytic anemias, three managements",
   "Hemoglobin ELECTROPHORESIS quantifies HbA2 and HbF; a raised HbA2 confirms beta-thalassemia "
   "trait. The point of making the diagnosis in an asymptomatic child is not treatment — trait "
   "needs none — but genetic counselling, and protecting him from a lifetime of unnecessary iron."),
],

103: [
 h("She is hemodynamically stable on no vasopressors, is euvolemic, and has had no bleeding", W,
   "No physiologic trigger",
   "Transfusion decisions rest on the patient, not the number. No active bleeding, no instability "
   "and no symptoms of impaired oxygen delivery means no indication."),
 h("She has stable coronary artery disease and reports no chest pain", P,
   "The tempting exception that does not apply",
   "Stable coronary disease is often used to justify a higher threshold, but the evidence does not "
   "support it. Acute coronary syndrome is a different situation; stable disease without ischemic "
   "symptoms is not."),
 h("Hemoglobin  7.6 g/dL", F, "Above the restrictive threshold",
   "The threshold for a stable, non-bleeding inpatient is 7 g/dL — 8 g/dL after cardiac or "
   "orthopedic surgery, or with symptomatic cardiovascular disease. At 7.6 she is above it."),
 h("reasoning that a higher hemoglobin will speed her recovery", P, "The intuition the trial killed",
   "The TRICC trial and those after it showed a restrictive strategy is at least as good as a "
   "liberal one, and better in some groups. More blood is not more oxygen delivery in a stable "
   "patient — it is more exposure to alloimmunization, circulatory overload, lung injury and cost."),
],

104: [
 h("platelet count is 14,000/mm3", F, "Below the prophylactic threshold",
   "The thresholds to know: 10,000/mm3 for prophylaxis in a stable patient, 20,000/mm3 with fever "
   "or sepsis, and 50,000/mm3 before an invasive procedure or for active bleeding — 100,000/mm3 for "
   "neurosurgery or the posterior eye."),
 h("He has no bleeding, no petechiae and no fever", P, "Two thresholds, and the lower one applies now",
   "With no fever and no bleeding, the stable threshold of 10,000 governs today — but that is not "
   "the end of the question."),
 h("A diagnostic lumbar puncture is planned for tomorrow", W, "The procedure changes the target",
   "A lumbar puncture requires roughly 50,000/mm3 because bleeding into the spinal canal can cause "
   "cord compression. The count must be raised for the procedure, not merely kept above the "
   "prophylactic floor."),
 h("Which of the following is the most appropriate transfusion plan?", W,
   "Transfused platelets last 3–4 days at most",
   "A unit given today will not still be supporting him tomorrow, and the count immediately after "
   "transfusion does not predict the count at the time of the procedure. The plan has to cover both "
   "the current threshold and the procedural one."),
],

105: [
 h("She has had no bleeding, and there is no bruising or mucosal bleeding on examination", W,
   "The clinical picture outranks the number",
   "An INR of 1.4 in cirrhosis does not predict bleeding. The patient's actual hemostatic "
   "performance is the better guide, and here it is intact."),
 h("International normalized ratio  1.4", M, "The INR is the wrong tool here",
   "The INR was designed and calibrated to monitor WARFARIN, not to measure bleeding risk in liver "
   "disease. It reflects only procoagulant factors and is blind to the parallel fall in protein C, "
   "protein S and antithrombin — so cirrhosis is a REBALANCED hemostatic state, not an "
   "anticoagulated one. Patients with cirrhosis also develop thrombosis."),
 h("The surgical intern requests 2 units of fresh frozen plasma to 'normalize the INR'", P,
   "Treating a number, not a patient",
   "Plasma carries real risks — circulatory overload, transfusion-related acute lung injury, "
   "allergic reactions — and here it would achieve nothing. Paracentesis is a low-risk procedure "
   "that does not require correction at these values."),
 h("Which of the following is the best reason to decline?", W, "The ocean and the teacup",
   "Only about 30% of normal factor activity is needed for surgical hemostasis, and an INR of 1.4 "
   "corresponds to activity well above that. Plasma contains factors at roughly normal "
   "concentration, so adding a teacup of it to an ocean of plasma volume barely moves the level — "
   "which is why the INR so often fails to correct after transfusion."),
],

106: [
 h("severe combined immunodeficiency", M, "No T cells to reject with",
   "Donor units contain viable donor T lymphocytes. A normal recipient recognizes and destroys "
   "them. A patient with no functioning T cells cannot, so those donor cells engraft and attack "
   "the host — transfusion-associated graft-versus-host disease, which is almost uniformly fatal."),
 h("His mother, who is ABO compatible, asks to donate the unit herself", P,
   "Directed donation from a relative is MORE dangerous",
   "The counterintuitive core of this question. A first-degree relative is more likely to be "
   "haploidentical — homozygous for an HLA haplotype the recipient carries — so the recipient's "
   "immune system sees the donor cells as self while the donor cells see the recipient as foreign. "
   "One-way recognition is exactly what causes graft-versus-host disease, and blood from relatives "
   "must ALWAYS be irradiated."),
 h("so that her son receives 'family blood'", P, "A reasonable-sounding request",
   "Families often assume related blood is safer. The instinct is understandable and, in this "
   "specific respect, exactly backwards. Irradiation inactivates donor lymphocytes so they cannot "
   "proliferate and resolves the problem."),
],

107: [
 h("blood pressure is 186/96 mm Hg (baseline 138/78 mm Hg)", P, "HYPERtension, not hypotension",
   "The discriminator from transfusion-related acute lung injury, which is accompanied by fever and "
   "HYPOtension. Circulatory overload raises the blood pressure."),
 h("Jugular venous pressure is elevated to the angle of the jaw", F, "Raised filling pressures",
   "With an S3 and peripheral signs of congestion, this is hydrostatic pulmonary edema. TRALI "
   "produces permeability edema with normal filling pressures and a normal jugular venous "
   "pressure."),
 h("2 units of red blood cells over 90 minutes", M, "The rate is the cause",
   "Two units delivered quickly to an 82-year-old with chronic kidney disease and a stiff, "
   "non-compliant ventricle. Slow transfusion, one unit at a time, with or without diuretic cover, "
   "is how this is prevented."),
 h("Brain natriuretic peptide is markedly elevated", W, "Volume overload confirmed",
   "Together with upper lobe vessel prominence and effusions on the radiograph, this establishes a "
   "hydrostatic rather than an inflammatory mechanism — and therefore that the treatment is "
   "diuresis and oxygen, not supportive ventilation alone."),
],

108: [
 h("newly diagnosed atrial fibrillation", M, "A red clot forms in stasis",
   "Blood stagnating in the left atrial appendage activates the coagulation cascade. The resulting "
   "thrombus is fibrin-rich and red — trapped red cells in a fibrin mesh — and forms with little "
   "platelet involvement."),
 h("He has hypertension and diabetes mellitus", W, "Risk is high enough to treat",
   "Age, hypertension and diabetes give a CHA2DS2-VASc score that mandates anticoagulation rather "
   "than observation."),
 h("he would prefer to take low-dose aspirin, which he already takes for cardiovascular prevention",
   P, "The right drug for a different clot",
   "Aspirin is genuinely effective — against ARTERIAL, platelet-rich WHITE clots forming on "
   "ruptured atherosclerotic plaque under high shear. It is simply the wrong mechanism for this "
   "clot."),
 h("Which of the following best explains why an anticoagulant is recommended instead?", W,
   "Match the drug to the clot",
   "Aspirin irreversibly inhibits cyclooxygenase-1 and blocks thromboxane A2-mediated platelet "
   "AGGREGATION. It does nothing to thrombin generation or fibrin formation, which is what builds "
   "an atrial thrombus. Trials confirm it: aspirin is substantially inferior to anticoagulation for "
   "stroke prevention in atrial fibrillation, without being meaningfully safer."),
],

109: [
 h("the activated partial thromboplastin time is 32 seconds", P, "The wrong test entirely",
   "Low molecular weight heparin has little effect on the partial thromboplastin time, so a normal "
   "value is EXPECTED and says nothing about whether the patient is anticoagulated. Increasing the "
   "dose on this basis risks bleeding."),
 h("subcutaneous enoxaparin", M, "Chain length decides which test works",
   "Inhibiting THROMBIN requires the heparin molecule to bridge antithrombin and thrombin together, "
   "which needs a long chain — at least 18 saccharide units. Inhibiting factor Xa needs only the "
   "pentasaccharide sequence that binds antithrombin. Low molecular weight heparin has mostly short "
   "chains, so it inhibits Xa well and thrombin poorly, and the thrombin-dependent aPTT barely "
   "moves."),
 h("Her body mass index is 41 kg/m2", W, "A genuine reason to measure something",
   "Monitoring is not routine, but it is indicated at the extremes of weight, in renal impairment "
   "and in pregnancy — and this patient has two of the three. The right test is a peak anti-factor "
   "Xa level, drawn about 4 hours after a dose."),
 h("at 26 weeks' gestation", F, "Pregnancy alters the pharmacokinetics",
   "Increased volume of distribution and glomerular filtration change enoxaparin clearance through "
   "pregnancy, which is the other accepted indication for anti-Xa monitoring."),
],

110: [
 h("She has never had abnormal bleeding, including two uneventful vaginal deliveries and a wisdom "
   "tooth extraction", P, "The number does not fit the person",
   "A platelet count of 19,000 with two uncomplicated deliveries behind her is internally "
   "inconsistent. When the laboratory and the patient disagree this sharply, suspect the "
   "laboratory."),
 h("Examination shows no petechiae, purpura or mucosal bleeding", W, "Nothing to find",
   "A genuine count of 19,000 usually produces at least petechiae. A completely normal examination "
   "supports an artefact."),
 h("The analyzer flags the sample", F, "The instrument is reporting doubt",
   "Automated counters flag results they cannot interpret. The flag is information, and overriding "
   "it without looking at a smear is how spurious results reach the chart."),
 h("Which of the following is the most appropriate next step?", W,
   "EDTA-dependent pseudothrombocytopenia",
   "In roughly 1 in 1,000 people, EDTA exposes a platelet membrane epitope that an autoantibody "
   "binds, clumping the platelets in the tube. The analyzer counts each clump as one cell, so the "
   "count falls in vitro only. Recollecting in CITRATE or heparin and examining a smear for clumps "
   "confirms it — and prevents an unnecessary marrow biopsy, steroids or a cancelled operation."),
],

111: [
 h("many short, blunt projections distributed evenly around the entire circumference of each cell",
   T, "Echinocytes, or burr cells",
   "Ten to thirty short, regular, evenly spaced spicules. Regularity and even distribution are what "
   "define them."),
 h("made promptly from a fresh sample", W, "Artefact excluded",
   "Echinocyte-like change is readily produced by delayed processing, excess EDTA, or a high-pH "
   "glass slide. The stem specifies a fresh prompt preparation so the finding can be trusted."),
 h("end-stage kidney disease and receives hemodialysis three times weekly", M,
   "Burr equals kidney",
   "Retained uremic toxins alter the membrane lipid bilayer, expanding the outer leaflet so the "
   "cell crenates evenly. The change is reversible."),
 h("He drinks no alcohol, and hepatic function tests are normal with a normal albumin", P,
   "Spur cells excluded",
   "The look-alike is the ACANTHOCYTE (spur cell), which has FEW, IRREGULAR, long spicules of "
   "varying length and unequal distribution and indicates severe LIVER disease — cholesterol "
   "loading of the membrane in cirrhosis, or abetalipoproteinemia. Burr = kidney, spur = liver."),
],

112: [
 h("Infant A was entirely well until 7 months of age", M, "The maternal antibody window",
   "Maternal IgG crosses the placenta in the third trimester and protects the infant until it wanes "
   "at around 6 months. A child who is well for half a year and then starts getting pyogenic "
   "infections has an ANTIBODY defect that was masked until the borrowed antibody ran out."),
 h("four episodes of otitis media, one pneumococcal pneumonia and a perineal abscess", F,
   "Pyogenic, encapsulated organisms",
   "Haemophilus, Streptococcus and Staphylococcus — the organisms that require opsonizing antibody. "
   "This is the infection signature of X-linked (Bruton) agammaglobulinemia."),
 h("examination shows no palpable tonsils", F, "Absent lymphoid tissue",
   "Tonsils and lymph nodes are largely B cells, so they never develop. Expect no CD19 or CD20 B "
   "cells on flow cytometry, low immunoglobulins of every class, and a BTK mutation."),
 h("Pneumocystis jirovecii pneumonia, all beginning at 8 weeks of age", F,
   "The T-cell pattern, from the start",
   "Chronic diarrhea, persistent thrush, Pneumocystis and failure to thrive within the first weeks "
   "of life is severe combined immunodeficiency. Confirm with an absolute lymphocyte count — below "
   "2,000/mm3 warrants evaluation — and the newborn screen for T-cell receptor excision circles "
   "should have flagged it."),
 h("Which of the following best explains the difference in the age at which their infections "
   "began?", W, "Timing is the discriminator",
   "Maternal IgG substitutes for the infant's own antibody but can do nothing for a missing "
   "CELLULAR arm. So an antibody defect declares itself at around 6 months, while a combined defect "
   "declares itself immediately."),
],

113: [
 h("multiple small mucosal polyps throughout the colon", T, "Lymphomatous polyposis",
   "Numerous lymphoid polyps through the gastrointestinal tract are a characteristic and "
   "distinctive presentation of mantle cell lymphoma."),
 h("expressing CD19, CD20 and CD5, and negative for CD23", W, "CD23 splits the CD5-positive cells",
   "Two mature B-cell neoplasms are CD5 POSITIVE, which is unusual because CD5 is normally a T-cell "
   "marker. CD23 separates them: chronic lymphocytic leukemia is CD23 POSITIVE, mantle cell "
   "lymphoma is CD23 NEGATIVE. That single marker is the whole differential here."),
 h("a monotonous infiltrate of small lymphoid cells with irregular nuclear contours", F,
   "Small cells, but aggressive",
   "The morphology looks indolent — small cells, low-grade appearance — but mantle cell lymphoma "
   "behaves aggressively and is generally incurable. It is the classic exception to the rule that "
   "small cell size predicts an indolent course."),
 h("Which of the following additional findings is most likely?", W, "t(11;14) and cyclin D1",
   "The translocation places CCND1 under the immunoglobulin heavy chain promoter, driving cyclin D1 "
   "overexpression and forcing cells through the G1/S checkpoint. Cyclin D1 immunostaining is "
   "essentially diagnostic; SOX11 is the alternative marker."),
],

114: [
 h("She feels well, with no bone pain, fatigue or infections", W, "No CRAB features",
   "hyperCalcemia, Renal insufficiency, Anemia and Bone lesions define end-organ damage. Calcium, "
   "creatinine, hemoglobin and the skeletal survey are all normal here, so there is no myeloma to "
   "treat."),
 h("an IgG monoclonal protein of 1.9 g/dL", F, "Under the 3 g/dL threshold",
   "The definitions are numeric. MGUS: paraprotein below 3 g/dL AND clonal plasma cells below 10% "
   "AND no end-organ damage. SMOLDERING myeloma: paraprotein 3 g/dL or more OR plasma cells 10% or "
   "more, still with no damage. Active myeloma: any end-organ damage."),
 h("bone marrow biopsy shows 7% clonal plasma cells", F, "Under the 10% threshold",
   "Both criteria fall below their cut-offs, so this is monoclonal gammopathy of undetermined "
   "significance."),
 h("Which of the following is the most appropriate management?", W, "Surveillance, not treatment",
   "MGUS progresses to myeloma at about 1% per year, and that risk never disappears — which is why "
   "monitoring is lifelong rather than time-limited. Treating it confers no benefit; the point of "
   "follow-up is to catch progression early."),
],

115: [
 h("A resident attempts a LEFT internal jugular approach", P, "The side is the whole question",
   "The thoracic duct ascends on the LEFT and arches over the pleura to join the venous system near "
   "the left internal jugular–subclavian junction. It is essentially never at risk on the right — "
   "which is why the left internal jugular route is avoided where there is a choice."),
 h("the guidewire passes but the catheter will not thread, so the equipment is withdrawn and a "
   "second attempt on the same side is successful", F, "Repeated instrumentation",
   "Difficult, repeated passes in that confined space are what injure the duct. The complication is "
   "mechanical, and the difficulty described is the clue that it happened."),
 h("The immediate post-procedure chest radiograph shows correct catheter position and no "
   "pneumothorax", P, "A normal early film proves nothing",
   "Chyle accumulates only once lymph flow rises. The immediate film is reassuring about the "
   "pneumothorax and irrelevant to this injury."),
 h("Enteral feeding is started overnight", M, "Feeding turns the tap on",
   "Dietary long-chain fat is absorbed into intestinal lacteals as chylomicrons and carried up the "
   "thoracic duct. Starting enteral feed multiplies lymph flow several-fold, converting an "
   "unnoticed duct injury into a rapidly filling chylothorax — hence the milky, triglyceride-rich "
   "fluid and the timing overnight."),
],

116: [
 h("He would prefer an oral agent he can start today without injections", W,
   "Only two DOACs go it alone",
   "APIXABAN and RIVAROXABAN can be started directly, each with a higher loading dose first — "
   "apixaban 10 mg twice daily for 7 days, then 5 mg twice daily; rivaroxaban 15 mg twice daily for "
   "21 days, then 20 mg daily. DABIGATRAN and EDOXABAN require 5–10 days of parenteral "
   "anticoagulation first, because their trials were designed that way. A and R go it alone."),
 h("his creatinine clearance is 88 mL/min, his weight is 84 kg", W, "No reason to exclude a DOAC",
   "Normal renal function and an unremarkable weight mean no dose adjustment and no contraindication."),
 h("he has no malignancy, antiphospholipid antibodies or prior thrombosis", P,
   "The exceptions are closed off",
   "These are the situations where a direct oral anticoagulant is the wrong choice — "
   "antiphospholipid syndrome in particular, where warfarin remains standard. The stem removes them "
   "so the straightforward answer applies."),
],

117: [
 h("pain behind both eyes and severe pain in his lower back and long bones", T, "Breakbone fever",
   "Retro-orbital pain with severe musculoskeletal and lumbar pain is the classic dengue "
   "presentation and is what named the disease."),
 h("He returned 6 days ago from a 2-week stay in Puerto Rico", F, "The right geography and timing",
   "Most United States dengue cases occur in Puerto Rico. The intrinsic incubation period is 4–7 "
   "days, which fits precisely."),
 h("platelet count is 82,000/mm3", F, "Thrombocytopenia",
   "Present with a faint macular rash and petechiae. This is why the choice of analgesic is not a "
   "trivial question."),
 h("Which of the following is the most appropriate analgesic and antipyretic for this patient?", W,
   "Acetaminophen, never NSAIDs",
   "Treat this as a class rule for EVERY viral hemorrhagic fever. Non-steroidal anti-inflammatory "
   "drugs — ibuprofen, naproxen, aspirin — inhibit platelet function and add to the bleeding risk "
   "in a patient who is already thrombocytopenic and bleeding into skin and mucosa. Aspirin in a "
   "young patient with a viral illness also raises the question of Reye syndrome."),
],

118: [
 h("She began a very low-carbohydrate weight-loss diet 3 weeks ago and has been eating roughly 700 "
   "kcal/day", M, "Fasting provokes the attack",
   "Caloric restriction upregulates delta-aminolevulinic acid synthase, the rate-limiting and "
   "inducible first enzyme of heme synthesis. With a downstream block, driving that enzyme floods "
   "the pathway with the neurotoxic precursors that cause the attack. Other triggers are "
   "cytochrome P450-inducing drugs, alcohol, infection and the luteal phase."),
 h("The abdomen is soft and non-tender despite her distress, and computed tomography shows no "
   "abnormality", P, "Pain without physical findings",
   "Severe abdominal pain with an unremarkable abdomen and normal imaging is the hallmark. The pain "
   "is NEUROVISCERAL — autonomic neuropathy, not peritoneal inflammation — which is why these "
   "patients so often undergo negative laparotomy before the diagnosis is made."),
 h("Serum sodium is 124 mEq/L", F, "Hyponatremia",
   "Usually from the syndrome of inappropriate antidiuretic hormone secretion, and part of the "
   "classic picture alongside tachycardia, hypertension, proximal weakness and psychiatric "
   "symptoms."),
 h("porphobilinogen 38 times and δ-aminolevulinic acid 15 times the upper limit of normal", W,
   "Porphobilinogen is what makes it porphyria",
   "Both precursors are markedly raised, confirming acute intermittent porphyria. Contrast LEAD "
   "poisoning, where delta-aminolevulinic acid rises but porphobilinogen stays NORMAL — the "
   "single discriminator between them."),
 h("Which of the following is the most appropriate treatment?", W, "Switch the pathway off",
   "HEMIN provides the end-product whose absence releases the feedback brake, shutting down "
   "ALA synthase directly. Intravenous DEXTROSE does the same thing more weakly by relieving the "
   "caloric deprivation, and is started immediately while hemin is obtained."),
],

119: [
 h("His CD4 count is 140/mm3", W, "Below 200 is the prophylaxis threshold",
   "A CD4 count under 200/mm3 — the same number that defines AIDS — is the threshold for "
   "Pneumocystis jirovecii prophylaxis, continued until the count recovers on antiretroviral "
   "therapy. Under 100/mm3 adds toxoplasmosis prophylaxis, and under 50/mm3 is where opportunistic "
   "infection risk is greatest."),
 h("Toxoplasma IgG is negative", W, "One prophylaxis not needed",
   "Toxoplasmosis prophylaxis applies to seroPOSITIVE patients with a CD4 count under 100/mm3, "
   "because the disease is reactivation of latent infection. A negative IgG means there is nothing "
   "to reactivate — and his count is above that threshold anyway."),
 h("a tuberculin skin test is negative, and cryptococcal antigen is negative", W,
   "The other prophylaxes excluded",
   "Latent tuberculosis is treated at any CD4 count if testing is positive, and cryptococcal "
   "antigen is checked below 200/mm3. Both negative here."),
 h("3 months of oral thrush and 7 kg of weight loss", F, "Already immunosuppressed",
   "Persistent candidiasis with weight loss confirms clinically what the CD4 count states "
   "numerically."),
],

120: [
 h("She reports missing doses frequently during a period of housing instability", M,
   "Intermittent adherence selects resistance",
   "Partial adherence is the worst case — drug levels high enough to select resistant variants but "
   "too low to suppress replication. Reverse transcriptase has a high error rate, so the variant "
   "pool already exists and selection simply acts on it."),
 h("a single amino acid substitution at position 103 of reverse transcriptase", F,
   "K103N, the classic mutation",
   "A single substitution — not an accumulation. That distinction is what the question is testing."),
 h("in a conserved region of the enzyme's allosteric pocket", W, "One pocket, one whole class",
   "All non-nucleoside reverse transcriptase inhibitors bind the SAME allosteric pocket "
   "non-competitively. Change that pocket and every member of the class loses its grip at once. "
   "This is the LOWEST genetic barrier in antiretroviral therapy."),
 h("tenofovir, emtricitabine and efavirenz", P, "Only one drug in the regimen is affected",
   "Tenofovir and emtricitabine are NRTIs — nucleoside analogues that bind COMPETITIVELY at the "
   "active site and cause chain termination. Their resistance requires ACCUMULATED mutations, so "
   "they survive this one. Contrast protease inhibitors, which have a high genetic barrier, and "
   "lenacapavir, where one capsid mutation confers more than 80,000-fold resistance."),
],

}
