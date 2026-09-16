# Batch 24 — Porphyria & lead (§7) and the anemia differential (§3). The last coverage gap.
# Native LOs: 35, 42, 55

Q = []


def q(stem, opts, correct, explanation, eli5, image=None, imcap=None, exim=None, excap=None):
    assert correct in opts, correct
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


# ─────────────────────────────────────────────────────────────────────────────
# §7 — the porphyrias and lead (LO 35)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 27-year-old woman has 3 days of severe, diffuse abdominal pain with vomiting and constipation. "
    "She is anxious and tearful, and reports new weakness climbing stairs. She has had two similar "
    "episodes in the past year. Six weeks ago she was started on a combined oral contraceptive for "
    "menstrual irregularity. Her abdomen is soft and non-tender despite her distress, and computed "
    "tomography shows diffuse bowel dilation with no obstructing lesion. There are no skin lesions. "
    "Her blood pressure is 162/96 mm Hg and pulse 118/min.\n\n"
    "Laboratory studies show:\n"
    "Sodium 122 mEq/L (N=136–146 mEq/L)\n"
    "Hemoglobin 13.1 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 39% (N=36%–46%)\n"
    "Leukocyte count 8,100/mm3 (N=4,500–11,000/mm3)\n"
    "Lipase 32 U/L (N=14–60 U/L)\n\n"
    "A urine specimen collected now darkens on standing in the light. Which of the following is the "
    "most appropriate diagnostic test?",
    {
        "Blood lead concentration":
            "This is the right test if δ-aminolevulinic acid is elevated with a NORMAL porphobilinogen, "
            "because lead blocks the pathway one step earlier. It is the exclusion to run on an "
            "abnormal result, not the first test.",
        "Diagnostic laparoscopy":
            "Severe pain with a soft abdomen and normal imaging is the point of the vignette — pain out "
            "of all proportion to the examination. Operating on a porphyria attack adds a surgical "
            "stress that makes the attack worse.",
        "Serum ceruloplasmin and a 24-hour urinary copper excretion":
            "These test for Wilson disease, which can give neuropsychiatric symptoms and liver disease "
            "— but not episodic abdominal pain with autonomic instability and hyponatremia, and not "
            "urine that darkens on standing.",
        "Skin biopsy of a sun-exposed area":
            "This belongs to the CUTANEOUS branch of the porphyria workflow. She has no skin lesions, "
            "and the two branches use entirely different tests.",
        "Spot urine porphobilinogen and δ-aminolevulinic acid": "",
    },
    "Spot urine porphobilinogen and δ-aminolevulinic acid",
    "Acute intermittent porphyria. The triad is present: visceral abdominal pain, neurologic "
    "dysfunction (proximal weakness), and psychiatric disturbance (anxiety). Add the features that "
    "make the vignette recognizable — hypertension, tachycardia, hyponatremia often through the "
    "syndrome of inappropriate antidiuretic hormone secretion, constipation, and urine that darkens on "
    "standing.\n\n"
    "How the diagnosis is actually made:\n"
    "• Collect the urine DURING the symptoms. That is the moment to send it.\n"
    "• A SPOT urine is sufficient — a 24-hour collection is not needed.\n"
    "• Send δ-aminolevulinic acid, porphobilinogen AND creatinine. The creatinine is there to "
    "normalize the result, because reference ranges are expressed per gram of creatinine, indexing to "
    "muscle mass and urine concentration.\n"
    "• Greater than 2–4 times the upper limit of normal confirms an acute attack. Do not use urine "
    "total porphyrins as a screening test.\n\n"
    "The precipitant is in the history: an estrogen-containing oral contraceptive started six weeks "
    "ago. That is very nearly the lecturer's own vignette — a young woman given the pill for menstrual "
    "irregularity who then develops abdominal pain, which everyone attributes to ordinary side "
    "effects. The full precipitant list is medications, infection, fasting or low caloric intake, sex "
    "hormones including menstruation, stress, illicit drugs, alcohol and smoking.\n\n"
    "Acute intermittent porphyria is autosomal dominant, caused by partial deficiency of porphobilinogen "
    "deaminase — about half of normal activity, which is why onset is delayed to the second or third "
    "decade. It is the most common ACUTE porphyria at 80% of acute cases, though not the most common "
    "porphyria overall, which is porphyria cutanea tarda.\n\n"
    "Note the clarifier from the workflow: fever, a raised C-reactive protein or a palpable abdominal "
    "mass would point to the PROVOKING factor, not to the attack itself.",
    "She has crippling belly pain but a completely soft belly and normal scans — the pain is coming "
    "from her nerves, not her bowel. Catch the chemical that is flooding her system by testing her "
    "urine while she is still in the attack.",
    exim="fig_porph_pathway",
    excap="Heme biosynthesis with the enzyme defect of each porphyria marked — note lead poisoning "
          "sitting one step BELOW the acute intermittent porphyria block.",
)

q(
    "A 4-year-old boy living in a house built in 1925 has 2 months of irritability, intermittent "
    "abdominal pain and declining school-readiness skills. His gums show a bluish line at the "
    "margins.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.4 g/dL (N=11.5–15.5 g/dL)\n"
    "Hematocrit 28% (N=35%–45%)\n"
    "Mean corpuscular volume 71 µm3 (N=75–87 µm3)\n"
    "Urine δ-aminolevulinic acid 14 times the upper limit of normal (N=less than 1 times ULN)\n"
    "Urine porphobilinogen 0.9 times the upper limit of normal (N=less than 1 times ULN)\n\n"
    "The peripheral smear shows microcytic erythrocytes with coarse basophilic stippling. Which "
    "enzyme is directly inhibited by the responsible agent?",
    {
        "δ-Aminolevulinic acid dehydratase": "",
        "δ-Aminolevulinic acid synthase 1":
            "This is the first and RATE-LIMITING enzyme, which is upregulated in porphyria rather than "
            "inhibited. Loss of end-product feedback from heme drives it, which is what floods the "
            "pathway with precursors.",
        "Glucose-6-phosphate dehydrogenase":
            "Deficiency of this enzyme causes oxidative hemolysis with bite cells and Heinz bodies "
            "after an oxidant exposure. It is not part of heme synthesis.",
        "Porphobilinogen deaminase":
            "This is the defect in acute intermittent porphyria, and it sits one step LATER in the "
            "pathway — which is exactly why that disease raises BOTH precursors while this patient's "
            "porphobilinogen is normal.",
        "Uroporphyrinogen decarboxylase":
            "This is the defect in porphyria cutanea tarda, the blistering photocutaneous porphyria. It "
            "produces skin disease, not a microcytic anemia with basophilic stippling.",
    },
    "δ-Aminolevulinic acid dehydratase",
    "Lead poisoning, and the urine pattern is the discriminator that names it.\n\n"
    "Read the pathway in order: δ-aminolevulinic acid → (ALA dehydratase) → porphobilinogen → (PBG "
    "deaminase) → hydroxymethylbilane → … → heme.\n\n"
    "• LEAD blocks ALA DEHYDRATASE. The block sits BEFORE porphobilinogen is made, so "
    "δ-aminolevulinic acid piles up while porphobilinogen is never overproduced and stays NORMAL.\n"
    "• ACUTE INTERMITTENT PORPHYRIA blocks PBG DEAMINASE, one step later — so BOTH precursors pile "
    "up.\n\n"
    "One line answers most questions in this section: **ALA up + PBG up → acute porphyria. ALA up + "
    "PBG NORMAL → lead.** This is also why the diagnostic workflow carries the footnote that if only "
    "δ-aminolevulinic acid is elevated, you check a blood lead level and urine organic acids — the "
    "latter to exclude hereditary tyrosinemia, where succinylacetone inhibits the same enzyme.\n\n"
    "Lead additionally inhibits FERROCHELATASE, the final step that inserts iron into protoporphyrin "
    "IX. That is why zinc protoporphyrin accumulates and can be used as a screening test reflecting "
    "the previous 3 months, and it is part of why the anemia is microcytic. Confirm with a serum lead "
    "level; above 10 µg/dL is unsafe.\n\n"
    "The clinical signs to recognize: facial pallor (earliest), Burton's lines — the gingival lead "
    "line in this stem, with dense metaphyseal lines at the epiphyses of long bones on radiograph — "
    "colic, wrist drop or foot drop, encephalopathy, and 'saturnine' gout from lead nephropathy. "
    "Coarse basophilic stippling on the smear is the classic hematologic clue.\n\n"
    "Three diseases, one pathway: sideroblastic anemia (iron cannot enter protoporphyrin, so it stacks "
    "in mitochondria → ringed sideroblasts), lead, and the porphyrias.",
    "Lead jams one particular step of the assembly line that builds haemoglobin. Because it jams it "
    "early, only the first ingredient piles up — and that pattern in the urine is what separates lead "
    "from the inherited disease that looks similar.",
    exim="fig_porph_lead",
    excap="Lead inhibits δ-aminolevulinic acid dehydratase and ferrochelatase — the block sits one step "
          "above porphobilinogen, which is why porphobilinogen stays normal.",
)

q(
    "A 52-year-old man receiving maintenance hemodialysis has a 6-month history of fragile skin on "
    "the backs of both hands, with blisters that break down into shallow erosions, small white "
    "papules, and patchy hyper- and hypopigmentation. He has also noticed new hair growth over his "
    "cheeks and temples. His urine is tea-coloured. He has chronic hepatitis C infection and drinks "
    "four beers most evenings. Which of the following additional investigations is most likely to "
    "reveal a second, related diagnosis?",
    {
        "Antinuclear antibody and anti-double-stranded DNA":
            "Lupus is also a photosensitive disease and is usually considered first, which is the trap. "
            "But blistering with hypertrichosis and tea-coloured urine pulls you across to a "
            "porphyria.",
        "Hemochromatosis gene testing with iron studies": "",
        "Serum ceruloplasmin":
            "Wilson disease causes hepatic and neuropsychiatric disease with Kayser-Fleischer rings. It "
            "has no photocutaneous manifestation.",
        "Spot urine porphobilinogen during an attack":
            "This is the test for the ACUTE branch of the workflow — the neurovisceral porphyrias. He "
            "has a cutaneous presentation with no abdominal pain, and the two branches use different "
            "tests.",
        "Thyroid-stimulating hormone and free thyroxine":
            "Thyroid disease causes hair and skin change, but not blistering photosensitivity with "
            "milia and tea-coloured urine.",
    },
    "Hemochromatosis gene testing with iron studies",
    "Porphyria cutanea tarda — the most common porphyria overall, and the one you will actually see. "
    "(Contrast acute intermittent porphyria, which is the most common ACUTE porphyria.) The enzyme "
    "defect is uroporphyrinogen decarboxylase.\n\n"
    "The second diagnosis is HEMOCHROMATOSIS. Heterozygous hemochromatosis gene mutations are found in "
    "about two-thirds of patients with porphyria cutanea tarda, because this is fundamentally an "
    "iron-related disease. The lecture flags it explicitly as a great board question — one patient "
    "carrying two diseases affecting two different systems.\n\n"
    "Every association in this stem is classic: hepatitis C, alcohol use, iron overload, and advanced "
    "kidney disease on dialysis. The skin findings are the full set — blisters and bullae on "
    "sun-exposed skin, milia (the small white papules), hyper- and hypopigmentation, and hypertrichosis "
    "of the cheeks, temples and eyebrows. One word for all of it: blistering photosensitivity.\n\n"
    "Hypertrichosis is the feature that does not photograph well but is dramatic in life — a patient's "
    "own description was growing hair in places God did not intend hair to grow. New facial hair with "
    "blistering on the backs of the hands is porphyria cutanea tarda.\n\n"
    "Urine colour separates the two porphyrias in this section: TEA-COLOURED here, from uroporphyrins "
    "spilling out of the liver, versus the red-brown or purple urine of an acute attack that darkens "
    "on standing in the light.\n\n"
    "Treatment follows the associations: direct-acting antivirals if it is secondary to hepatitis C "
    "(which cures the hepatitis C as well), phlebotomy for the iron overload, hydroxychloroquine for "
    "the skin, and sun avoidance until porphyrins normalize.",
    "His hands blister in sunlight, he is growing hair on his cheeks, and his urine looks like tea — "
    "a skin porphyria. And because that disease runs on iron overload, most of these patients are also "
    "carrying a hemochromatosis gene.",
    exim="fig_porph_pct_hands",
    excap="Porphyria cutanea tarda of the hands — blisters that have broken down into erosions, with "
          "crusting and scarring on sun-exposed skin.",
)

q(
    "A 31-year-old woman with known acute intermittent porphyria is admitted with a severe attack "
    "precipitated by a 3-day fast before a religious observance. She has abdominal pain, vomiting and "
    "a serum sodium of 126 mEq/L (N=136–146 mEq/L). Which of the following best explains why fasting "
    "provoked this attack?",
    {
        "Fasting depletes hepatic glycogen, reducing substrate for porphobilinogen deaminase":
            "The deficient enzyme's problem is a genetic partial deficiency, not a shortage of "
            "substrate. Its substrate, porphobilinogen, is in excess — that is the whole problem.",
        "Fasting induces PGC-1α, which upregulates δ-aminolevulinic acid synthase 1": "",
        "Fasting increases hepatic cytochrome P450 activity, consuming porphobilinogen":
            "Cytochrome P450 induction IS a genuine precipitant, but it works by consuming HEME — "
            "reducing the end-product feedback on the pathway. Cytochromes do not consume "
            "porphobilinogen.",
        "Fasting lowers serum iron, impairing insertion of iron into protoporphyrin IX":
            "Ferrochelatase inserts iron at the final step, and it is inhibited by lead rather than by "
            "fasting. Iron availability is not the limiting factor in an acute porphyria attack.",
        "Fasting raises endogenous cortisol, which directly inhibits uroporphyrinogen decarboxylase":
            "Uroporphyrinogen decarboxylase is the enzyme of porphyria cutanea tarda, a cutaneous "
            "disease. Nothing in an acute attack turns on that enzyme.",
    },
    "Fasting induces PGC-1α, which upregulates δ-aminolevulinic acid synthase 1",
    "One negative feedback loop explains every precipitant and every treatment in this topic.\n\n"
    "HEME INHIBITS ALAS1, the first and rate-limiting enzyme of the pathway. When a downstream enzyme "
    "is deficient, less heme is made → less inhibition reaches ALAS1 → ALAS1 revs up → the pathway "
    "floods with the precursors that accumulate ABOVE the block. Porphyria is therefore a disease of "
    "precursor accumulation, not of heme deficiency as such — and it is δ-aminolevulinic acid and "
    "porphobilinogen, not a lack of heme, that cause the attack.\n\n"
    "Anything that increases demand for heme or upregulates ALAS1 triggers an attack:\n"
    "• Fasting and low-carbohydrate intake — via PGC-1α, a transcriptional co-activator induced by "
    "fasting that drives ALAS1\n"
    "• Cytochrome P450-inducing drugs — the cytochromes consume heme, so less feedback reaches ALAS1\n"
    "• Steroid hormones, including menstruation and the oral contraceptive pill\n"
    "• Alcohol, infection, smoking and stress\n\n"
    "The treatments run the same loop in reverse. GLUCOSE and insulin suppress PGC-1α and therefore "
    "ALAS1 — that is the entire rationale for carbohydrate loading. HEMIN works from the other end, "
    "restoring the end-product negative feedback that inhibits ALAS1 directly. Alongside those: "
    "eliminate every provoking factor (here, resume eating), manage the hyponatremia, and refer to a "
    "porphyria expert centre, with genetic testing to determine which specific acute hepatic porphyria "
    "it is.\n\n"
    "Understanding the loop is worth more than memorizing the precipitant list, because the list is "
    "simply every way of doing the same thing.",
    "Going without food flips a switch that makes the first enzyme of the pathway work much harder. "
    "With a blockage further down, all that extra output piles up as the chemicals that cause the "
    "attack — which is why sugar is the immediate treatment.",
    exim="fig_porph_alas1",
    excap="Why fasting provokes an attack — PGC-1α induced by fasting drives ALAS1, the rate-limiting "
          "enzyme, while heme normally inhibits it.",
)

q(
    "A 34-year-old woman has a 2-year history of recurrent, unexplained severe abdominal pain. She "
    "has been given diagnoses of irritable bowel syndrome, endometriosis and a somatic symptom "
    "disorder, and has had a negative diagnostic laparoscopy. During her current episode she is "
    "hypertensive and tachycardic with a sodium of 124 mEq/L (N=136–146 mEq/L), and her spot urine "
    "porphobilinogen is 38 times the upper limit of normal. Which of the following best characterizes "
    "the principal obstacle to diagnosing this condition?",
    {
        "The available laboratory tests lack sensitivity and specificity":
            "The tests are straightforward and the threshold is low — greater than 2–4 times the upper "
            "limit of normal confirms an attack. Her result is 38 times normal.",
        "A definitive diagnosis requires genetic testing that is not widely available":
            "Genetic testing determines WHICH specific acute hepatic porphyria it is, after the "
            "biochemical diagnosis has been made. It is a refinement, not the barrier.",
        "It must be confirmed on a 24-hour urine collection that patients rarely complete":
            "A spot urine is sufficient — and is what was used here. The requirement is about TIMING, "
            "not volume: the sample must be collected during symptoms.",
        "Neurovisceral symptoms are indistinguishable from those of lead poisoning":
            "Lead is a genuine mimic, but it is separated in a single step: lead blocks the pathway one "
            "enzyme earlier, so δ-aminolevulinic acid rises with a NORMAL porphobilinogen.",
        "The diagnosis is rarely included in the differential in the first place": "",
    },
    "The diagnosis is rarely included in the differential in the first place",
    "The lecture is unusually direct about this: 'It's not a very challenging type of diagnosis. The "
    "most challenging part of it is actually thinking about it within your differential diagnosis.' "
    "Which leads to the maxim worth carrying out of this whole course: **you will never get the right "
    "diagnosis unless you first generate a differential diagnosis.**\n\n"
    "About 26% of patients with acute hepatic porphyria are initially misdiagnosed, and her label "
    "history is the typical one — irritable bowel syndrome, endometriosis, a somatic symptom disorder, "
    "and a negative laparoscopy. These patients are, in the lecturer's words, maligned and often "
    "thought to be crazy.\n\n"
    "The unifying question that finds it is an Occam's razor question: which single diagnosis explains "
    "abdominal pain, neuropathy AND psychiatric symptoms at once?\n\n"
    "Where in the sequence you actually make the diagnosis matters too. An acute attack runs in three "
    "phases:\n"
    "1. PRODROME — behaviour change, anxiety, restlessness, sleeplessness. You will essentially never "
    "diagnose porphyria here; as the lecturer put it, that describes much of the population at any "
    "given time.\n"
    "2. ABDOMINAL PAIN — this is the tier where the diagnosis gets made. Specifically UNEXPLAINED "
    "abdominal pain: severe pain with no tenderness or rigidity and normal imaging, with tachycardia, "
    "hypertension, hyponatremia, nausea, vomiting, constipation and red or red-brown urine.\n"
    "3. NEUROLOGICAL SIGNS — weakness, paresthesia, paralysis, tetraplegia, convulsions. You want the "
    "diagnosis before this.\n\n"
    "Think acute porphyria when you see: unexplained attacks of abdominal pain; a mood disorder PLUS a "
    "neuropathy; hypertension and tachycardia; hyponatremia; dark urine during the attack; and "
    "multiple precipitants in the history.",
    "The test is easy and her result is wildly abnormal — nobody had simply thought to order it. For "
    "two years she was told the pain was in her head, because this diagnosis never made it onto "
    "anyone's list of possibilities.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §3 — defining, measuring and classifying anemia (LO 42, 55)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A medical student is asked to classify several causes of anemia by mechanism using the standard "
    "framework of blood loss, increased destruction, and impaired production. Which of the following "
    "is an EXTRINSIC cause of increased red cell destruction?",
    {
        "Glucose-6-phosphate dehydrogenase deficiency":
            "This is an INTRINSIC cause — an enzyme deficiency of the red cell itself. The defect "
            "travels with the cell.",
        "Hereditary spherocytosis":
            "This is an INTRINSIC cause — a membrane disorder. The spleen destroys the cells, but the "
            "fault is in the cell, which is why splenectomy helps without correcting the defect.",
        "Hypersplenism": "",
        "Sickle cell disease":
            "This is an INTRINSIC cause — structurally abnormal globin chains. The abnormality is "
            "encoded in the cell's own haemoglobin.",
        "Vitamin B12 deficiency":
            "This sits in a different bucket entirely: impaired PRODUCTION through defective DNA "
            "synthesis, alongside folate deficiency.",
    },
    "Hypersplenism",
    "The mechanistic classification is the slide the lecture returned to before every new topic, and "
    "the extrinsic/intrinsic split within hemolysis is the part most often confused.\n\n"
    "**Blood loss** — acute (trauma) or chronic (gastrointestinal tract, gynecologic).\n\n"
    "**Increased destruction (hemolytic anemia)**\n"
    "• INTRINSIC — the fault is in the cell: membrane disorders (hereditary spherocytosis), enzyme "
    "deficiencies (glucose-6-phosphate dehydrogenase), deficient globin chain synthesis "
    "(thalassemias), structurally abnormal globin chains (sickle cell disease).\n"
    "• EXTRINSIC — the cell is normal and the environment destroys it: antibody-mediated destruction, "
    "mechanical trauma (microangiopathic hemolysis), and HYPERSPLENISM.\n\n"
    "**Impaired production** — defective haemoglobin synthesis (iron deficiency), defective DNA "
    "synthesis (vitamin B12 and folate), and the marrow's response to inflammation (anemia of chronic "
    "disease).\n\n"
    "Hypersplenism is the cleanest example of extrinsic destruction because the cells themselves are "
    "demonstrably normal — an enlarged, overactive organ simply removes too many of them, which is why "
    "the smear shows normal morphology and the marrow is normocellular.\n\n"
    "Reduce the whole tree to one question: **factory, or the road home?** A factory problem means not "
    "enough cells are built, and reticulocytes are LOW. A road-home problem means cells are built fine "
    "and then destroyed or lost, and reticulocytes are HIGH because the marrow is compensating. One "
    "cheap test splits the tree down the middle.",
    "Some anemias happen because the red cell itself is faulty; others because the cell is fine and "
    "something outside it destroys them. An oversized spleen eating perfectly good cells is the "
    "clearest example of the second kind.",
)

q(
    "A 71-year-old woman who underwent gastric bypass surgery 6 years ago reports fatigue and "
    "exertional dyspnea.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.8 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 29% (N=36%–46%)\n"
    "Mean corpuscular volume 91 µm3 (N=80–100 µm3)\n"
    "Red cell distribution width 21.4% (N=11.5%–14.5%)\n"
    "Reticulocyte count 0.6% (N=0.5%–1.5%)\n\n"
    "A colleague suggests that the normal mean corpuscular volume excludes a nutritional deficiency. "
    "Which of the following best explains the flaw in that reasoning?",
    {
        "A normal mean corpuscular volume can be the average of two opposing populations": "",
        "Mean corpuscular volume is a measured value and is unreliable at low hemoglobin levels":
            "Mean corpuscular volume is one of the values a modern analyser measures directly, and it "
            "is not invalidated by a low haemoglobin. The error is conceptual, not technical.",
        "Mean corpuscular volume rises only after 120 days, the lifespan of a red cell":
            "Indices change as new cells enter the circulation, well before a full cohort turns over. "
            "In any case a delay would not produce a wide distribution width.",
        "The mean corpuscular volume reference range does not apply to older adults":
            "Red cell indices are not age-adjusted in the way marrow cellularity is. Anemia thresholds "
            "and indices apply regardless of age — 'anemia of the elderly' is not a diagnosis.",
        "Reticulocytes are larger than mature red cells and raise the mean corpuscular volume":
            "This is true, and marked reticulocytosis is a listed cause of macrocytosis — but her "
            "reticulocyte count is 0.6%, which is low. Nothing is inflating her index from that "
            "direction.",
    },
    "A normal mean corpuscular volume can be the average of two opposing populations",
    "The mean corpuscular volume is a MEAN. A patient with both iron deficiency (microcytic) and "
    "vitamin B12 or folate deficiency (macrocytic) can average out to a perfectly normocytic value. "
    "That combination is real and common — in malnutrition, malabsorption, bariatric surgery and older "
    "adults — and her gastric bypass supplies all three risks at once.\n\n"
    "Two clues expose it, and one of them is already on her panel:\n"
    "• A raised RED CELL DISTRIBUTION WIDTH, which measures the SPREAD of cell sizes rather than the "
    "average. At 21.4% hers is markedly wide, meaning the population is heterogeneous even though its "
    "midpoint looks normal.\n"
    "• A smear showing a DIMORPHIC population — both small pale cells and large oval ones in the same "
    "field.\n\n"
    "The lesson the lecture draws from it is broader than the arithmetic: **patients do not always "
    "have exactly one diagnosis.** A single index that reads normal is not permission to stop.\n\n"
    "The index-based classification she should be worked up against:\n"
    "• MICROCYTIC (< 80 fL) — iron deficiency first; then thalassemia, anemia of chronic disease "
    "(which can be low-normal), sideroblastic anemia, lead poisoning.\n"
    "• NORMOCYTIC (80–100 fL) — anemia of chronic disease and acute blood loss first; then chronic "
    "kidney disease, early iron deficiency, hemolysis, marrow failure, and mixed deficiency.\n"
    "• MACROCYTIC (> 100 fL) — B12 or folate deficiency first; then alcohol, liver disease, "
    "hypothyroidism, myelodysplastic syndrome, drugs (methotrexate, hydroxyurea, zidovudine), and "
    "marked reticulocytosis.",
    "The MCV is an average, and averages hide things. She has some very small cells and some very "
    "large ones, which average out to normal — the giveaway is how spread out the sizes are.",
    exim="fig_slide_anemia_algorithm",
    excap="The practical approach — split on the mean corpuscular volume first, then on reticulocytes "
          "within the normocytic column. Note 'mixed deficiency' listed there.",
)

q(
    "A 63-year-old man with stage 4 chronic kidney disease reports 4 months of fatigue and dyspnea on "
    "climbing stairs that used to be easy. He has no bleeding, no weight loss and no bone pain.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.2 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 28% (N=41%–53%)\n"
    "Mean corpuscular volume 88 µm3 (N=80–100 µm3)\n"
    "Red cell distribution width 13.1% (N=11.5%–14.5%)\n"
    "Reticulocyte count 0.4% (N=0.5%–1.5%)\n"
    "Creatinine 3.6 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Ferritin 180 ng/mL (N=15–200 ng/mL)\n"
    "Transferrin saturation 27% (N=20%–50%)\n\n"
    "Which of the following is the most appropriate next step in management?",
    {
        "Begin an erythropoiesis-stimulating agent": "",
        "Begin oral ferrous sulfate three times daily":
            "His ferritin and transferrin saturation are both adequate, so he is not iron-deficient. "
            "Iron would be required if he were, because an erythropoiesis-stimulating agent cannot work "
            "without substrate — functional iron deficiency is the commonest cause of apparent "
            "resistance to one.",
        "Bidirectional endoscopy for occult gastrointestinal blood loss":
            "This is mandatory when IRON DEFICIENCY is demonstrated in an adult man. His iron studies "
            "are normal and his distribution width is normal, so there is no evidence of chronic blood "
            "loss.",
        "Bone marrow aspiration and biopsy":
            "This would be appropriate for an unexplained cytopenia, a macrocytic anemia suggesting "
            "myelodysplasia, or the presence of blasts or dysplasia. His anemia has a sufficient "
            "explanation already.",
        "Transfuse two units of packed red blood cells":
            "The restrictive threshold is 7 g/dL in a stable patient, and he is neither actively "
            "bleeding nor haemodynamically compromised. Transfusion also risks alloimmunization in "
            "someone who may need a transplant.",
    },
    "Begin an erythropoiesis-stimulating agent",
    "Work the algorithm in order, and the management plan falls out of the etiology.\n\n"
    "1. CONFIRM the anemia — haemoglobin below the sex-specific reference range. Yes, 9.2 g/dL.\n"
    "2. READ THE MEAN CORPUSCULAR VOLUME FIRST — 88 µm3 is normocytic, so the differential splits into "
    "the middle column.\n"
    "3. GET A RETICULOCYTE COUNT — this is the branch point within that column. His is 0.4%, which is "
    "LOW: a production problem, not destruction or loss. Factory, not road home.\n"
    "4. ORDER THE TARGETED STUDIES — a normocytic anemia with low reticulocytes points to inflammation, "
    "kidney disease or early marrow disease. His creatinine of 3.6 mg/dL names it.\n"
    "5. LOOK AT THE SMEAR — a normal red cell distribution width and no dysplasia argue against a "
    "mixed deficiency or myelodysplasia.\n\n"
    "The anemia of chronic kidney disease is primarily an ERYTHROPOIETIN deficiency — the failing "
    "kidney no longer produces enough of the hormone that drives erythropoiesis — which is exactly why "
    "replacing it is the treatment. The prescribing threshold is explicit: start an "
    "erythropoiesis-stimulating agent only when haemoglobin is below 10 g/dL, and only for the anemia "
    "of chronic kidney disease or of non-curative chemotherapy. He meets both conditions.\n\n"
    "Two things to have confirmed before starting, and this stem supplies both: adequate iron stores "
    "(ferritin 180 ng/mL, transferrin saturation 27%), because functional iron deficiency is the "
    "commonest reason an agent appears not to work; and the absence of another explanation for the "
    "anemia.\n\n"
    "The boxed warnings then govern how you use it: do not exceed a haemoglobin of 11 g/dL, and do not "
    "raise it faster than 1 g/dL per 2 weeks — overshooting increases thrombotic and cardiovascular "
    "events.",
    "His kidneys have stopped making the hormone that tells the marrow to build red cells — the "
    "marrow is willing but has not been asked. Replacing the hormone is the fix, and his iron stores "
    "are already stocked so it will have something to work with.",
)
