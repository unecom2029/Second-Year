# Hardest Exam — batch H1 of 5 (questions 1–20)
# Sections §1–§14: hematopoiesis, marrow, anemia evaluation, iron, B12/folate, anemia of chronic
# disease, porphyria and lead, hemolysis, membrane/enzyme/globin defects, spleen, transfusion.
# UWorld house style: "due to" openers, two-step asks, alphabetized options, an
# "Educational objective:" line closing every explanation. Pathology-weighted, stem images.

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


# ── 1. Fetal hematopoiesis — the liver at mid-gestation (§1) ────────────────────
q(
    "A 26-year-old woman at 23 weeks' gestation comes to the emergency department due to 2 days of "
    "decreased fetal movement. She and her partner were each previously told they have mildly "
    "microcytic red cell indices with normal iron studies. Ultrasonography shows fetal ascites, "
    "bilateral pleural effusions, scalp edema, and absent cardiac activity. At autopsy, the fetal "
    "liver is markedly enlarged, and sections show numerous clusters of nucleated erythroid "
    "precursors lying between the hepatic cords. The marrow cavities of the long bones are only "
    "sparsely cellular. Hemoglobin analysis of fetal blood shows that nearly all of the hemoglobin "
    "is a tetramer of four identical non-alpha chains. In a healthy fetus of this gestational age, "
    "which of the following is the principal site of blood cell production?",
    {
        "Liver": "",
        "Marrow of the axial skeleton":
            "This is the ADULT pattern — vertebrae, ribs, sternum and pelvis — after the marrow of "
            "the long bones converts to fat. It is the reason a marrow biopsy is taken from the "
            "posterior iliac crest, not from a fetus's hematopoietic sites.",
        "Marrow of the long bones":
            "Bone marrow takes over in the LATE fetus and is the dominant site by birth, and in "
            "childhood the long bones are still red. At 23 weeks the long-bone marrow is only "
            "beginning to populate, as this autopsy shows.",
        "Spleen":
            "The fetal spleen contributes to blood formation, but it is the secondary site. The "
            "liver is dominant through mid-gestation.",
        "Thymus":
            "The thymus educates T cells that have already been made — it is a site of lymphocyte "
            "maturation, not a primary site of hematopoiesis at any age.",
        "Yolk sac":
            "The yolk sac makes the first, primitive wave of blood in the EMBRYO (the first weeks "
            "after conception, making embryonic hemoglobins). By the second trimester it has been "
            "replaced by the liver.",
    },
    "Liver",
    "Hydrops fetalis from alpha thalassemia with all four alpha genes deleted. Both parents carry "
    "alpha thalassemia trait (microcytosis with normal iron studies). With no alpha genes, the fetus "
    "makes excess gamma chains → gamma-chain tetramers (hemoglobin Barts) → extreme oxygen affinity → "
    "oxygen is bound and never released → profound tissue hypoxia → heart failure and hydrops.\n\n"
    "The liver finding is a trap only if you forget the timeline. The lifetime sequence is:\n"
    "• Embryo → yolk sac (the first, primitive wave)\n"
    "• Fetus → LIVER (dominant mid-gestation), with a contribution from the spleen\n"
    "• Late fetus onward → bone marrow\n"
    "• Adult → the axial skeleton (vertebrae, ribs, sternum, pelvis); the long bones turn to fat\n\n"
    "So clusters of erythroid precursors in the liver at 23 weeks are expected, and hypoxia would "
    "only exaggerate them. In a CHILD or ADULT the same finding would mean extramedullary "
    "hematopoiesis — the body reopening a site it abandoned under extreme demand (thalassemia major, "
    "severe chronic hemolysis, marrow fibrosis).\n\n"
    "Educational objective: Hematopoiesis moves from the yolk sac (embryo) to the liver and spleen "
    "(fetus) to the bone marrow (late fetus onward), and in adults retreats to the axial skeleton. "
    "Liver hematopoiesis is normal mid-gestation but, after birth, signals extramedullary "
    "hematopoiesis from severe marrow demand.",
    "Before you are born, your liver is the blood factory. Later the job moves into your bones, and "
    "in grown-ups only the bones in the middle of the body keep doing it. If a grown-up's liver "
    "starts making blood again, the body is in serious trouble.",
    exim="fig_hx_fetal_hemato",
    excap="Sites of hematopoiesis across development (yolk sac → liver and spleen → bone marrow) "
          "plotted against the globin chains being made at each stage — note gamma chains dominating "
          "through fetal life, which is why an alpha-less fetus forms gamma tetramers.",
)

# ── 2. Pediatric aplastic anemia after hepatitis (§2, §51) ───────────────────────
q(
    "An 8-year-old boy is brought to the office by his mother due to 3 weeks of fatigue, easy "
    "bruising, and bleeding gums when he brushes his teeth. Two months ago, he was hospitalized "
    "for acute hepatitis; viral serologies for hepatitis A, B, and C were negative, and his liver "
    "enzymes have since normalized. He takes no medications. He appears well and is at the 50th "
    "percentile for height. There are scattered petechiae on the legs. Both thumbs and forearms "
    "are normal, and there are no skin pigment changes. There is no lymphadenopathy or "
    "hepatosplenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 6.9 g/dL (N=11.5–15.5 g/dL)\n"
    "Hematocrit 21% (N=35%–45%)\n"
    "Mean corpuscular volume 94 µm3 (N=77–95 µm3)\n"
    "Leukocyte count 1,700/mm3 (N=4,500–13,500/mm3)\n"
    "Platelet count 11,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 0.2% (N=0.5%–1.5%)\n\n"
    "Peripheral smear shows no blasts. A posterior iliac crest core biopsy is shown. Which of the "
    "following is the most likely mechanism of this patient's cytopenias?",
    {
        "Antibody destruction of circulating platelets":
            "This is immune thrombocytopenia: an ISOLATED low platelet count with a normal or "
            "increased number of megakaryocytes. It does not lower the hemoglobin, the white count "
            "and the reticulocytes, and it does not empty the marrow.",
        "Immune destruction of hematopoietic stem cells": "",
        "Inherited defect in DNA cross-link repair":
            "This is Fanconi anemia, which also gives pancytopenia with an empty marrow in a "
            "well-appearing child — but announces itself outside the blood with short stature, "
            "café-au-lait macules and absent or hypoplastic thumbs. This boy has none of those.",
        "Ineffective hematopoiesis from vitamin deficiency":
            "Megaloblastic anemia gives a HYPERcellular marrow (precursors are made, then die "
            "inside it) and a macrocytic MCV. This marrow is nearly all fat.",
        "Marrow replacement by lymphoblasts":
            "Acute lymphoblastic leukemia produces a sick-appearing child, often with splenomegaly "
            "and bone pain, a PACKED marrow and blasts. The biopsy here is empty.",
        "Splenic sequestration of blood cells":
            "Hypersplenism lowers all three lineages, but it needs a big spleen, and the marrow is "
            "normal or hypercellular as it compensates. There is no splenomegaly here.",
    },
    "Immune destruction of hematopoietic stem cells",
    "Acquired aplastic anemia, here following seronegative hepatitis. A well-appearing child with "
    "pancytopenia, a low reticulocyte count, no organomegaly and an acellular marrow is the aplastic "
    "picture in the pediatric differential; the sick-appearing child with splenomegaly is the "
    "leukemic one.\n\n"
    "Mechanism: a trigger (hepatitis, drugs, toxins, viruses, or most often nothing identifiable) → "
    "T cell–mediated attack on the self-renewing hematopoietic stem cells → the stem cell pool "
    "collapses → every lineage fails together → fat fills the empty marrow space.\n\n"
    "Why the biopsy matters: cellularity is a core biopsy reading, not an aspirate reading, because "
    "only the core keeps the architecture — trabeculae and the ratio of cells to fat. Normal "
    "cellularity is roughly 100 minus the patient's age, so an 8-year-old should be about 90% "
    "cellular. A marrow that is mostly fat is hypocellular.\n\n"
    "The inherited mimics are separated by what you can see on examination: Fanconi anemia (short "
    "stature, café-au-lait macules, absent thumbs; confirm with a chromosome breakage assay), "
    "Diamond-Blackfan anemia (red cells only), Shwachman-Diamond syndrome (pancreatic "
    "insufficiency, neutropenia) and thrombocytopenia with absent radii (thumbs present). Definitive "
    "treatment for severe aplastic anemia in a child is a matched sibling marrow transplant.\n\n"
    "Educational objective: Aplastic anemia is immune-mediated loss of hematopoietic stem cells, "
    "producing pancytopenia, reticulocytopenia and a fatty, hypocellular marrow on core biopsy. "
    "Leukemia and megaloblastic anemia also cause cytopenias but leave the marrow hypercellular.",
    "The boy's blood factory has lost the special seed cells that make every kind of blood cell, so "
    "all of his counts dropped at once. The picture of his bone shows mostly fat where busy blood "
    "cells should be.",
    image="fig_hx_aplastic",
    imcap="Core biopsy of bone marrow (hematoxylin and eosin). Pink bony trabeculae border a marrow "
          "space occupied almost entirely by large empty fat cells, with only a single small cluster "
          "of hematopoietic cells.",
)

# ── 3. Anemia of chronic kidney disease — the missing regulator (§1) ─────────────
q(
    "A 64-year-old man comes to the office for follow-up of end-stage kidney disease due to "
    "diabetic nephropathy. He has received hemodialysis 3 times weekly for 2 years and reports "
    "progressive fatigue and exertional dyspnea. He does not use alcohol. There is no "
    "splenomegaly. Stool is negative for occult blood.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.6 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 26% (N=41%–53%)\n"
    "Mean corpuscular volume 88 µm3 (N=80–100 µm3)\n"
    "Reticulocyte count 0.4% (N=0.5%–1.5%)\n"
    "Ferritin 310 ng/mL (N=20–250 ng/mL)\n"
    "Transferrin saturation 29% (N=20%–50%)\n"
    "Lactate dehydrogenase 160 U/L (N=45–200 U/L)\n"
    "Erythropoietin 11 mU/mL (N=4–26 mU/mL)\n\n"
    "The peripheral smear shows normocytic, normochromic erythrocytes. Which of the following is "
    "the most likely primary mechanism of this patient's anemia?",
    {
        "Hepcidin-mediated iron sequestration":
            "This is anemia of chronic disease: iron is locked in macrophages, so serum iron and "
            "the TRANSFERRIN SATURATION fall. His saturation is a healthy 29%, so iron is reaching "
            "the marrow.",
        "Immune destruction of stem cells":
            "Aplastic anemia fails ALL lineages. Only the red cells are affected here.",
        "Impaired DNA synthesis in precursors":
            "Megaloblastic anemia is macrocytic (MCV over 100) with hypersegmented neutrophils and "
            "a raised lactate dehydrogenase. His MCV is 88 and his LDH is normal.",
        "Inadequate erythropoietin production": "",
        "Marrow replacement by fibrosis":
            "Primary myelofibrosis gives teardrop cells, a leukoerythroblastic smear and massive "
            "splenomegaly from extramedullary hematopoiesis. None are present.",
        "Peripheral red cell destruction":
            "Hemolysis drives the reticulocyte count UP, with a raised LDH. His reticulocytes are "
            "low and his LDH is normal — a production problem.",
    },
    "Inadequate erythropoietin production",
    "Anemia of chronic kidney disease. The loop: the kidney samples oxygen delivery → when delivery "
    "falls it releases erythropoietin → erythropoietin drives committed erythroid progenitors to "
    "divide and mature → reticulocytes enter the blood.\n\n"
    "In kidney failure the sensor and the factory foreman are the same failed organ. A normocytic "
    "anemia with a LOW reticulocyte count and replete iron (ferritin 310, saturation 29%) means the "
    "marrow has the raw material but is never given the order.\n\n"
    "The trap is the erythropoietin value: 11 mU/mL sits inside the reference interval, but for a "
    "hemoglobin of 8.6 g/dL it should be many times higher. An 'inappropriately normal' "
    "erythropoietin in the face of anemia is a production failure — the same logic as a 'normal' "
    "reticulocyte count during severe anemia.\n\n"
    "Each lineage has its own dispatcher, and each has become a drug class: erythropoietin (red "
    "cells; epoetin, darbepoetin), thrombopoietin (platelets), granulocyte and granulocyte-macrophage "
    "colony-stimulating factors (myeloid cells; filgrastim, sargramostim), and growth hormone with "
    "insulin-like growth factor (lymphoid cells). An erythropoiesis-stimulating agent works only if "
    "iron stores are repleted first.\n\n"
    "Educational objective: Erythropoietin is made by the kidney in response to reduced oxygen "
    "delivery, so chronic kidney disease causes a hypoproliferative normocytic anemia with low "
    "reticulocytes. An erythropoietin level within the reference range is inappropriately low when "
    "the patient is significantly anemic.",
    "The kidney is the boss that tells the bone marrow to make red blood cells. When the kidney "
    "breaks, the boss stops shouting, so the factory slows down even though it has all its supplies.",
    exim="fig_slide_erythropoiesis",
    excap="Erythropoiesis from committed progenitor to reticulocyte — erythropoietin acts on the "
          "early committed erythroid cells.",
)

# ── 4. Megaloblastic marrow — hypercellular with low reticulocytes (§5) ──────────
q(
    "A 57-year-old woman comes to the office due to 4 months of fatigue and a sore, smooth tongue. "
    "She has hypothyroidism treated with levothyroxine. She does not drink alcohol. Her sclerae "
    "are mildly icteric. There is no splenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.8 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 23% (N=36%–46%)\n"
    "Mean corpuscular volume 118 µm3 (N=80–100 µm3)\n"
    "Leukocyte count 3,600/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 128,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 0.6% (N=0.5%–1.5%)\n"
    "Bilirubin, total 2.1 mg/dL (N=0.1–1.0 mg/dL)\n"
    "Lactate dehydrogenase 1,850 U/L (N=45–200 U/L)\n\n"
    "Direct antiglobulin test is negative. A bone marrow aspirate is shown. Which of the following "
    "best explains the combination of this marrow appearance and the reticulocyte count?",
    {
        "Cytokine suppression of erythroid proliferation":
            "This is one of the four mechanisms of anemia of chronic disease, which is normocytic or "
            "microcytic with a normal lactate dehydrogenase and a normal or hypocellular marrow — "
            "not a macrocytic anemia with an LDH of 1,850.",
        "Intramedullary death of erythroid precursors": "",
        "Marrow infiltration by myeloid blasts":
            "Acute leukemia also fills the marrow, but with uniform blasts and usually circulating "
            "blasts on the smear. These precursors are maturing, enlarged cells of several lineages.",
        "Peripheral destruction of mature erythrocytes":
            "Hemolysis also raises LDH and indirect bilirubin, but an intact marrow answers with a "
            "HIGH reticulocyte count. Hers is 0.6% at a hematocrit of 23% — a corrected count of "
            "about 0.3%.",
        "Viral lysis of erythroid progenitors":
            "Parvovirus B19 halts erythropoiesis and leaves the marrow DEVOID of red cell "
            "precursors apart from occasional giant pronormoblasts. It does not create a crowded "
            "marrow or lower all three lineages.",
    },
    "Intramedullary death of erythroid precursors",
    "Megaloblastic anemia (autoimmune thyroid disease plus glossitis points to pernicious anemia). "
    "The marrow is hypercellular yet the reticulocyte count is low — the signature of INEFFECTIVE "
    "erythropoiesis.\n\n"
    "Mechanism: B12 or folate deficiency → too little thymidine → DNA synthesis stalls while "
    "cytoplasmic hemoglobin synthesis continues (nuclear–cytoplasmic asynchrony) → large precursors "
    "with fine, open chromatin (megaloblasts) accumulate → many die inside the marrow before release "
    "→ few reticulocytes reach the blood, and the dying cells release lactate dehydrogenase and "
    "indirect bilirubin.\n\n"
    "That is why this patient looks 'hemolytic' on chemistry (very high LDH, mild jaundice) but "
    "'hypoproliferative' on the reticulocyte count. The defect hits every dividing cell, so the "
    "white count and platelets are also mildly low, and granulocyte precursors are giant.\n\n"
    "Ineffective hematopoiesis is also the mechanism in thalassemia, myelodysplastic syndrome, "
    "sideroblastic anemia and severe iron deficiency.\n\n"
    "Educational objective: Ineffective hematopoiesis means precursors are made in excess but die "
    "within the marrow, giving a hypercellular marrow with a low reticulocyte count, raised lactate "
    "dehydrogenase and indirect bilirubin. Megaloblastic anemia is the classic example; true "
    "hemolysis raises the reticulocyte count instead.",
    "Her bone marrow is working very hard and is full of cells, but the cells cannot finish growing "
    "because they are missing a vitamin, so most of them break apart before they ever leave. That "
    "is why the factory looks busy but very few new cells reach the blood.",
    image="fig_megaloblastic_marrow",
    imcap="Bone marrow aspirate (high power). The field is highly cellular. Many precursor cells "
          "are enlarged, with nuclei showing finely dispersed, open chromatin, and several "
          "granulocytic cells are larger than expected.",
    exim="fig_slide_b12_tree",
    excap="The lecture's decision tree for megaloblastic anemia.",
)

# ── 5. Pernicious anemia → gastric carcinoma surveillance (§5) ───────────────────
q(
    "A 58-year-old woman comes to the office due to 5 months of fatigue and numbness in both feet. "
    "She has vitiligo and Hashimoto thyroiditis. She eats a mixed diet and does not drink "
    "alcohol. Examination shows decreased vibration and position sense in both great toes and a "
    "positive Romberg sign.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.1 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 27% (N=36%–46%)\n"
    "Mean corpuscular volume 114 µm3 (N=80–100 µm3)\n"
    "Methylmalonic acid 1,240 nmol/L (N=70–270 nmol/L)\n"
    "Homocysteine 38 µmol/L (N=5–15 µmol/L)\n\n"
    "Anti-parietal cell antibodies are positive. The peripheral smear is shown. After replacement "
    "therapy is begun, this patient requires ongoing surveillance for which of the following?",
    {
        "Colonic adenocarcinoma":
            "Colonic cancer is the lesion hunted for in an adult man or postmenopausal woman with "
            "IRON deficiency — a microcytic anemia from occult bleeding. This is a macrocytic "
            "anemia from failed absorption.",
        "Enteropathy-associated T-cell lymphoma":
            "This is the malignancy of long-standing celiac disease, itself a cause of iron and "
            "B12 malabsorption. Celiac disease is marked by anti-tissue transglutaminase "
            "antibodies, not anti-parietal cell antibodies.",
        "Esophageal adenocarcinoma":
            "This arises from Barrett metaplasia in chronic acid reflux. Pernicious anemia "
            "produces the opposite state — a stomach that can no longer make acid.",
        "Gastric adenocarcinoma": "",
        "Hepatocellular carcinoma":
            "This is the cancer of cirrhosis, including cirrhosis from hemochromatosis. Nothing in "
            "this autoimmune gastric disease damages the liver.",
    },
    "Gastric adenocarcinoma",
    "Pernicious anemia. Autoimmunity (vitiligo, Hashimoto thyroiditis) → anti-parietal cell "
    "antibodies → destruction of the gastric body mucosa → loss of parietal cells → no intrinsic "
    "factor (and no acid) → no B12–intrinsic factor complex to absorb at the terminal ileum → B12 "
    "deficiency however much the patient eats.\n\n"
    "The B12 deficiency is confirmed by the RAISED methylmalonic acid (normal in folate deficiency; "
    "homocysteine rises in both). The dorsal column signs (vibration, position sense, Romberg) are "
    "B12's second job — myelin maintenance — failing; folate has no such role.\n\n"
    "Pernicious anemia is three problems, not one:\n"
    "1. Megaloblastic anemia (macro-ovalocytes, hypersegmented neutrophils)\n"
    "2. Atrophic gastritis with intestinal metaplasia → increased risk of GASTRIC CARCINOMA → "
    "ongoing surveillance\n"
    "3. Myelin degeneration of the dorsal and lateral columns (subacute combined degeneration)\n\n"
    "B12 must be given by a route that does not need intrinsic factor: intramuscular injection, or "
    "high-dose oral therapy absorbed by passive diffusion. Anti-parietal cell antibodies are more "
    "sensitive (85%–90%); anti-intrinsic factor antibodies are more specific (75%).\n\n"
    "Educational objective: Pernicious anemia is autoimmune destruction of gastric parietal cells, "
    "causing intrinsic factor deficiency, B12 malabsorption and atrophic gastritis with intestinal "
    "metaplasia. Beyond B12 replacement, patients need surveillance for gastric carcinoma.",
    "Her immune system attacked the part of her stomach that helps her soak up vitamin B12. That "
    "damaged stomach lining can slowly turn into cancer, so doctors keep checking it for years.",
    image="fig_hx_hyperseg",
    imcap="Peripheral blood smear (Wright-Giemsa). Several neutrophils have nuclei divided into six "
          "or more lobes; the surrounding erythrocytes are large and many are oval.",
)

# ── 6. Folic acid timing — the neural tube closes before pregnancy is known (§5) ─
q(
    "A newborn boy is evaluated in the nursery due to the lesion shown. He was born at 39 weeks' "
    "gestation to a 29-year-old woman whose pregnancy was unplanned. She had no chronic medical "
    "conditions and took no medications before conception. When a home pregnancy test became "
    "positive at 9 weeks' gestation, she began a daily prenatal vitamin containing 0.8 mg of folic "
    "acid and took it for the rest of the pregnancy. Her serum folate at the first prenatal visit "
    "was within normal limits. The lesion is covered only by a thin membrane through which neural "
    "tissue is visible, and the infant does not move his lower extremities. For folic acid to have "
    "reduced this infant's risk of this malformation, when should supplementation have begun?",
    {
        "At a positive pregnancy test":
            "This is what the mother did, and it was too late. By the time most pregnancies are "
            "recognized, the neural tube has already closed or failed to close.",
        "At the first trimester ultrasound examination":
            "Dating ultrasound usually happens at 8–13 weeks — after the 4-week window in which the "
            "neural tube closes.",
        "At the start of the second trimester":
            "Folate needs do rise throughout pregnancy, but a supplement started at 13 weeks cannot "
            "influence an event that finished at 4 weeks.",
        "Before conception in any woman able to conceive": "",
        "Only if the maternal diet lacks green vegetables":
            "Supplementation is recommended for ALL women of childbearing potential, regardless of "
            "diet, because intake cannot be assumed to cover the higher requirement at the moment it "
            "matters. A normal serum folate later in pregnancy does not reassure about week 4.",
    },
    "Before conception in any woman able to conceive",
    "Myelomeningocele — a neural tube defect in which the caudal neural tube failed to close, "
    "leaving exposed spinal cord and meninges over the lumbosacral spine (hence the paralyzed legs).\n\n"
    "Why folate: folate is required for DNA synthesis, and the neural tube is one of the fastest-"
    "dividing tissues in the early embryo. Folic acid supplementation prevents neural tube defects — "
    "spina bifida and anencephaly — which is why prenatal vitamins contain more folic acid than a "
    "general multivitamin.\n\n"
    "Why timing is the whole point: the neural tube closes at about 4 WEEKS after conception → "
    "often before a period is even recognized as missed → a supplement started at a positive test "
    "(here, 9 weeks) arrives after the event it was meant to protect. The recommendation is "
    "therefore to supplement before conception, in all women who could become pregnant, and to "
    "continue because pregnancy is itself a state of increased folate requirement (as are infancy, "
    "chronic hemolysis and dialysis).\n\n"
    "Educational objective: Folic acid prevents neural tube defects, but the neural tube closes "
    "around week 4 of gestation, frequently before pregnancy is recognized. Supplementation must "
    "therefore begin before conception in every woman of childbearing potential, not after a "
    "positive pregnancy test.",
    "The baby's spine closes very early, about a month into pregnancy, before most moms even know "
    "they are pregnant. The vitamin that helps it close only works if mom is already taking it "
    "before the baby starts growing.",
    image="fig_hx_mmc",
    imcap="Newborn photographed prone. An oval defect over the lumbosacral spine (arrowhead) exposes "
          "red neural tissue covered by a thin membrane, with a purplish border of surrounding skin.",
)

# ── 7. Iron deficiency in an older man → occult colonic cancer (§4) ─────────────
q(
    "A 67-year-old man comes to the office due to 3 months of fatigue and shortness of breath when "
    "climbing stairs. He has no abdominal pain and has not noticed black or bloody stools. He eats "
    "a varied diet that includes red meat. He takes no medications. A guaiac-based fecal occult "
    "blood test 6 months ago was negative. His conjunctivae are pale. Abdominal and rectal "
    "examinations are normal.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.2 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 28% (N=41%–53%)\n"
    "Mean corpuscular volume 71 µm3 (N=80–100 µm3)\n"
    "Red cell distribution width 18.6% (N=11.5%–14.5%)\n"
    "Platelet count 462,000/mm3 (N=150,000–400,000/mm3)\n"
    "Iron 28 µg/dL (N=65–175 µg/dL)\n"
    "Total iron-binding capacity 468 µg/dL (N=250–400 µg/dL)\n"
    "Ferritin 6 ng/mL (N=20–250 ng/mL)\n\n"
    "The peripheral smear is shown. Further evaluation of this patient is most likely to reveal "
    "which of the following?",
    {
        "Adenocarcinoma of the cecum": "",
        "Atrophy of duodenal villi":
            "Celiac disease causes iron deficiency by malabsorption, but it is the answer in a "
            "YOUNGER patient, or in iron deficiency that fails oral therapy — usually with "
            "diarrhea or dermatitis herpetiformis. In a 67-year-old man, blood loss comes first.",
        "Loss of two alpha-globin genes":
            "Alpha thalassemia trait is microcytic with NORMAL iron studies and a high red cell "
            "count. This patient's ferritin is 6 and TIBC is high — genuine iron deficiency.",
        "Mitochondrial iron in erythroblasts":
            "Ringed sideroblasts mark sideroblastic anemia, where iron is HIGH and cannot be "
            "incorporated into heme. Here iron is absent.",
        "Parietal cell loss in the stomach":
            "Pernicious anemia gives a MACROcytic anemia with hypersegmented neutrophils. Achlorhydria "
            "can impair iron absorption, but it is not the expected finding in this patient.",
    },
    "Adenocarcinoma of the cecum",
    "Iron deficiency anemia: microcytic, hypochromic cells with pencil forms, a high RDW, reactive "
    "thrombocytosis, low ferritin (the earliest and most useful marker), low serum iron, and a HIGH "
    "total iron-binding capacity (empty transferrin 'cups', so the capacity to bind more is high).\n\n"
    "Iron deficiency is a symptom, not a diagnosis — always ask where the iron went. In an adult man "
    "or a postmenopausal woman, it is gastrointestinal blood loss until proven otherwise, because "
    "colorectal adenocarcinoma can present with iron deficiency and nothing else. Right-sided "
    "(cecal, ascending) tumors are bulky, exophytic and ulcerated → slow, silent bleeding into "
    "liquid stool → iron deficiency without visible blood or change in bowel habit. Left-sided "
    "tumors more often present with obstruction or visible blood.\n\n"
    "The negative fecal occult blood test is the decoy: bleeding is intermittent, and a single "
    "negative guaiac test does not exclude a tumor. The next step is bidirectional endoscopy "
    "(colonoscopy plus upper endoscopy), with iron replacement given alongside — treat the iron and "
    "find the leak. In a premenopausal woman with menorrhagia, by contrast, the gastrointestinal "
    "search is not automatic.\n\n"
    "Educational objective: Iron deficiency anemia in an adult man or postmenopausal woman is "
    "presumed to be from gastrointestinal blood loss until proven otherwise and requires endoscopic "
    "evaluation, even with a negative fecal occult blood test. Right-sided colon cancer classically "
    "presents as isolated iron deficiency.",
    "This man's blood cells are small and pale because he has run out of iron. Grown men don't "
    "usually lose iron, so doctors look for a hidden slow bleed, and a tumor in the gut is the main "
    "worry.",
    image="fig_hx_ida_smear",
    imcap="Peripheral blood smear. The erythrocytes are small and pale, with central pallor "
          "occupying well over one third of each cell; there is variation in size and several "
          "elongated forms. A small lymphocyte is present for size comparison.",
    exim="fig_hx_colon_exophytic",
    excap="Resected colon with a bulky, ulcerated, exophytic adenocarcinoma (diamond) — the kind of "
          "right-sided tumor that bleeds slowly and silently.",
)

# ── 8. Anemia of chronic disease — iron is present but locked in (§6) ────────────
q(
    "A 62-year-old woman comes to the office due to fatigue. She has had rheumatoid arthritis for "
    "15 years, with persistently swollen metacarpophalangeal joints despite treatment. She has no "
    "gastrointestinal symptoms and is postmenopausal. Colonoscopy a year ago was normal.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.8 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 29% (N=36%–46%)\n"
    "Mean corpuscular volume 81 µm3 (N=80–100 µm3)\n"
    "Reticulocyte count 0.6% (N=0.5%–1.5%)\n"
    "Iron 34 µg/dL (N=50–170 µg/dL)\n"
    "Total iron-binding capacity 198 µg/dL (N=250–400 µg/dL)\n"
    "Ferritin 390 ng/mL (N=10–120 ng/mL)\n"
    "C-reactive protein 4.8 mg/dL (N=less than 0.5 mg/dL)\n\n"
    "Because of mild thrombocytosis, a bone marrow aspirate is obtained; a Prussian blue stain is "
    "shown. Which of the following is the most likely mechanism of this patient's anemia?",
    {
        "Hepcidin-mediated ferroportin degradation": "",
        "Impaired duodenal iron absorption":
            "Malabsorption (celiac disease, bypass surgery, acid suppression) empties iron STORES — "
            "ferritin would be low, TIBC high and the marrow stain blank.",
        "Lead inhibition of ferrochelatase":
            "Lead poisoning is microcytic with basophilic stippling and raised zinc protoporphyrin. "
            "It does not produce a low TIBC with iron-laden macrophages in a patient with active "
            "inflammation.",
        "Mitochondrial iron trapping in erythroblasts":
            "Sideroblastic anemia puts iron in a RING around the nucleus of erythroid precursors "
            "and raises serum iron. Here the iron is in macrophages and serum iron is low.",
        "Occult gastrointestinal blood loss":
            "Chronic bleeding is the classic cause of iron deficiency: low ferritin, HIGH TIBC and "
            "no stainable marrow iron — the mirror image of this patient.",
        "Reduced alpha-globin synthesis":
            "Thalassemia trait is microcytic with entirely NORMAL iron studies and a high red cell "
            "count; it does not lower serum iron or TIBC.",
    },
    "Hepcidin-mediated ferroportin degradation",
    "Anemia of chronic disease (anemia of inflammation) from active rheumatoid arthritis.\n\n"
    "Mechanism: inflammation → interleukin-6 → hepatic hepcidin synthesis ↑ → hepcidin degrades "
    "ferroportin, the only exit iron has from macrophages and enterocytes → recycled and dietary "
    "iron is trapped → serum iron falls although body iron is normal or high → the marrow is "
    "iron-starved. Three further hits add to it: cytokines blunt erythropoietin release, suppress "
    "erythroid proliferation directly, and augment hemophagocytosis.\n\n"
    "Reading the iron row:\n"
    "• Ferritin HIGH — iron is stored, and ferritin is also an acute phase reactant\n"
    "• TIBC LOW — transferrin is a negative acute phase reactant, so there are fewer 'cups'\n"
    "• Serum iron low — none is circulating (low in iron deficiency too, so it discriminates nothing)\n"
    "• Marrow iron INCREASED, inside macrophages — the stain shown\n\n"
    "Ferritin and TIBC move in opposite directions in the two diseases, and that pair is what "
    "separates them. Oral iron does not help — it is pushed at a locked door. Treatment is control "
    "of the underlying disease.\n\n"
    "Educational objective: In anemia of chronic disease, interleukin-6–driven hepcidin degrades "
    "ferroportin and traps iron in macrophages, giving low serum iron, low TIBC, normal-to-high "
    "ferritin and abundant marrow macrophage iron. Iron deficiency shows the reverse ferritin and "
    "TIBC pattern with absent marrow iron.",
    "Her body has plenty of iron, but the swelling in her joints tells her body to lock the iron "
    "away in storage cells. The blood factory can't reach it, so it makes fewer red cells.",
    image="fig_hx_prussian",
    imcap="Bone marrow aspirate, Prussian blue stain. A large macrophage in the center contains "
          "abundant coarse blue-staining granules; the surrounding hematopoietic cells are "
          "counterstained pink-red.",
    exim="fig_hepcidin",
    excap="Hepcidin and iron regulation — hepcidin blocks ferroportin on enterocytes and macrophages.",
)

# ── 9. The normal MCV that hides two deficiencies (§3) ───────────────────────────
q(
    "A 51-year-old woman comes to the office due to 6 months of fatigue and tingling in her feet. "
    "Seven years ago she underwent Roux-en-Y gastric bypass surgery and lost 55 kg (121 lb). She "
    "stopped taking her prescribed supplements 3 years ago. She has not had a menstrual period in "
    "2 years. Vibration sense is decreased at both ankles.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.4 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 28% (N=36%–46%)\n"
    "Mean corpuscular volume 90 µm3 (N=80–100 µm3)\n"
    "Red cell distribution width 22.4% (N=11.5%–14.5%)\n"
    "Reticulocyte count 0.5% (N=0.5%–1.5%)\n"
    "Ferritin 5 ng/mL (N=10–120 ng/mL)\n"
    "Vitamin B12 118 pg/mL (N=200–900 pg/mL)\n"
    "Creatinine 0.8 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "Which of the following best explains the mean corpuscular volume in this patient?",
    {
        "Averaging of microcytic and macrocytic cells": "",
        "Early iron depletion before microcytosis develops":
            "Early iron deficiency can be normocytic, but it does not widen the RDW to 22% and does "
            "not explain a B12 of 118 with neuropathy. Two deficiencies are present.",
        "Erythropoietin deficiency with normocytic cells":
            "This is the anemia of chronic kidney disease. Her creatinine is normal, and it would "
            "not produce a markedly raised RDW.",
        "Red cell agglutination artifact in the analyzer":
            "Cold agglutinins falsely RAISE the MCV and lower the red cell count, with a hemoglobin "
            "that does not match three times the hematocrit. Her indices are internally consistent.",
        "Reticulocytosis offsetting microcytic erythrocytes":
            "Reticulocytes are large and can lift the MCV — but only when the marrow is responding. "
            "Her reticulocyte count is low.",
    },
    "Averaging of microcytic and macrocytic cells",
    "Combined iron and B12 deficiency after gastric bypass. The operation bypasses the duodenum "
    "(where iron is absorbed) and the acid- and intrinsic factor–producing stomach (needed for B12), "
    "so both deficiencies develop together and require lifelong monitoring.\n\n"
    "Why the MCV is normal: the MCV is an AVERAGE. Iron deficiency → small cells (extra divisions "
    "before maturation). B12 deficiency → large cells (nucleus cannot divide) → the two populations "
    "average out to a 'normal' 90 µm3.\n\n"
    "Two clues expose it:\n"
    "• A very high RDW — two populations of different size\n"
    "• A dimorphic smear — small pale cells alongside large oval ones\n\n"
    "Management follows the etiology: replace BOTH — iron (often intravenously, since the duodenum "
    "is bypassed) and B12 by a route that does not need intrinsic factor. Giving folate alone would "
    "risk masking the B12 deficiency while the neuropathy progresses.\n\n"
    "Educational objective: A normal MCV does not exclude nutritional anemia, because coexisting "
    "microcytic and macrocytic deficiencies average to a normocytic value. A markedly raised RDW and "
    "a dimorphic smear reveal the combination, which is common after bariatric surgery and in "
    "malnutrition.",
    "The machine reports the average size of her blood cells. Half are too small and half are too "
    "big, so the average looks normal even though both kinds are wrong.",
    exim="fig_slide_anemia_algorithm",
    excap="The lecture's anemia algorithm — split on MCV first, then on the reticulocyte count.",
)

# ── 10. Lead poisoning — the extra finding (§7) ───────────────────────────────────
q(
    "A 3-year-old girl is brought to the office by her father due to 2 months of irritability, "
    "intermittent abdominal pain, and constipation. She no longer uses several words she had "
    "learned. The family moved 4 months ago into a house built in 1938 that is being renovated, "
    "and she often chews on windowsills. Abdominal examination is benign.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.6 g/dL (N=11.0–14.0 g/dL)\n"
    "Hematocrit 29% (N=33%–42%)\n"
    "Mean corpuscular volume 69 µm3 (N=70–86 µm3)\n"
    "Ferritin 46 ng/mL (N=10–120 ng/mL)\n"
    "Transferrin saturation 24% (N=20%–50%)\n"
    "Zinc protoporphyrin 180 µg/dL (N=less than 35 µg/dL)\n\n"
    "A peripheral smear is shown. Which of the following is most likely to be found on further "
    "evaluation of this patient?",
    {
        "Dense metaphyseal lines on radiographs": "",
        "Elevated hemoglobin A2 fraction":
            "Beta-thalassemia trait is also microcytic and can also show stippling — but it does "
            "not raise zinc protoporphyrin, and it does not cause colic or developmental regression.",
        "Elevated urine porphobilinogen":
            "Porphobilinogen rises in acute intermittent porphyria, where the block is at PBG "
            "deaminase. Lead blocks the step BEFORE porphobilinogen is made, so it stays normal.",
        "Hypersegmented neutrophils on the blood smear":
            "These mark megaloblastic anemia, which is macrocytic. This anemia is microcytic.",
        "Increased red cell osmotic fragility":
            "This is the confirmatory finding in hereditary spherocytosis, a normocytic hemolytic "
            "anemia with spherocytes rather than stippled microcytes.",
        "Positive direct antiglobulin test":
            "This identifies antibody-coated red cells in immune hemolysis. Lead injures heme "
            "synthesis, not the red cell surface.",
    },
    "Dense metaphyseal lines on radiographs",
    "Lead poisoning: an old house under renovation, pica, colic, constipation, developmental "
    "regression (encephalopathy), a microcytic anemia with coarse basophilic stippling, and a raised "
    "zinc protoporphyrin with NORMAL iron studies.\n\n"
    "Mechanism: lead inhibits ALA dehydratase and ferrochelatase →\n"
    "• ALA dehydratase block → δ-aminolevulinic acid accumulates, porphobilinogen stays normal "
    "(the discriminator from acute porphyria)\n"
    "• Ferrochelatase block → iron cannot enter protoporphyrin → zinc is inserted instead → zinc "
    "protoporphyrin rises (a screen reflecting the prior 3 months)\n"
    "• Impaired ribosomal RNA degradation → aggregated ribosomes → basophilic stippling\n\n"
    "Lead also deposits where bone is actively growing, producing dense transverse lines at the ends "
    "of long bones on radiographs — part of the 'Burton lines' family (gingival lead lines plus "
    "dense lines at the growing ends of long bones). Other signs: facial pallor (earliest), wrist or "
    "foot drop, and saturnine gout. Confirm with a blood lead level (over 10 µg/dL is unsafe).\n\n"
    "Educational objective: Lead inhibits ALA dehydratase and ferrochelatase, producing a microcytic "
    "anemia with basophilic stippling, raised zinc protoporphyrin, raised urine ALA with normal "
    "porphobilinogen, gingival lines, and dense lines at the growing ends of long bones.",
    "Lead from old paint jams the machine that builds the iron part of blood, so the red cells come "
    "out small and speckled. Lead also sticks in growing bones, which shows up as bright white bands "
    "on an x-ray.",
    image="fig_hx_stipple_wright",
    imcap="Peripheral blood smear (Wright stain). The erythrocyte marked by the arrowhead contains "
          "numerous fine, dark blue-purple granules scattered evenly through its cytoplasm. A small "
          "lymphocyte is present at lower left.",
    exim="fig_porph_lead",
    excap="Lead inhibits ALA dehydratase and ferrochelatase within the heme synthesis pathway.",
)

# ── 11. Porphyria cutanea tarda and the iron connection (§7) ─────────────────────
q(
    "A 54-year-old man comes to the office due to 4 months of blisters on the backs of his hands "
    "that appear after he works in his garden and heal with scarring. He has also noticed new, "
    "darker hair growing over his cheeks and temples, and his urine has become tea-colored. He "
    "has chronic hepatitis C infection and drinks 6 beers daily. He has no abdominal pain, "
    "weakness, or mood change. His left hand is shown. Serum "
    "aminotransferases are twice the upper limit of normal and a positive urine porphyrin screen. "
    "Evaluation for which of the following coexisting conditions is most likely to be revealing "
    "in this patient?",
    {
        "Acute intermittent porphyria":
            "This is the NEUROVISCERAL porphyria — attacks of abdominal pain, neuropathy and "
            "psychiatric change with urine that darkens on standing — and it has no skin findings. "
            "The two porphyria branches are separate diseases with separate tests.",
        "Alpha-1 antitrypsin deficiency":
            "This causes liver disease and emphysema, but it has no connection to the heme pathway "
            "or to blistering photosensitivity.",
        "Hereditary hemochromatosis": "",
        "Systemic lupus erythematosus":
            "Lupus is the photosensitive disease most people think of first, which is exactly why "
            "this patient could be misdiagnosed. Blistering with milia, hypertrichosis and "
            "tea-colored urine pull the diagnosis away from lupus.",
        "Wilson disease":
            "Wilson disease causes liver and neuropsychiatric disease in YOUNG patients through copper "
            "accumulation. It does not cause a photocutaneous porphyria.",
    },
    "Hereditary hemochromatosis",
    "Porphyria cutanea tarda (PCT) — the most common porphyria overall, from deficient "
    "uroporphyrinogen decarboxylase.\n\n"
    "The recognition set: blistering photosensitivity on sun-exposed skin with erosions, scarring "
    "and milia; hypertrichosis of the cheeks and temples; and tea-colored urine from uroporphyrins "
    "spilling out of the liver. The associations are the precipitants in this man: hepatitis C, "
    "alcohol, iron overload, and end-stage kidney disease.\n\n"
    "Why hemochromatosis: PCT is fundamentally an IRON-related disease. Hepatic iron → oxidative "
    "generation of an inhibitor of uroporphyrinogen decarboxylase → porphyrins accumulate → "
    "photosensitizing porphyrins reach the skin. Heterozygous hemochromatosis gene mutations are "
    "found in about two-thirds of patients — a classic 'one patient, two diseases in two systems' "
    "board question. Check iron studies.\n\n"
    "Treatment: direct-acting antivirals to cure the hepatitis C, phlebotomy to remove iron, "
    "hydroxychloroquine for skin symptoms, and sun avoidance until porphyrins normalize.\n\n"
    "Educational objective: Porphyria cutanea tarda presents with blistering photosensitivity, "
    "hypertrichosis and tea-colored urine, and is precipitated by hepatitis C, alcohol and iron "
    "overload. Heterozygous hemochromatosis mutations are present in about two-thirds of patients, "
    "so iron studies are required and phlebotomy is a core treatment.",
    "His liver is holding too much iron, and that iron jams one step of the machine that makes the "
    "red part of blood. The half-made pieces build up, travel to the skin, and blister when sunlight "
    "hits them.",
    image="fig_hx_pct",
    imcap="Dorsum of the left hand. A tense fluid-filled bulla sits on the index finger, with "
          "hemorrhagic crusted erosions over the knuckles and several small white papules and "
          "scaly scars on the back of the hand.",
    exim="fig_porph_pathway",
    excap="Heme biosynthesis with the enzyme defect of each porphyria marked — porphyria cutanea "
          "tarda sits at uroporphyrinogen decarboxylase.",
)

# ── 12. Mechanical valve → intravascular hemolysis (§8) ──────────────────────────
q(
    "A 66-year-old man comes to the office due to 6 weeks of fatigue and intermittently dark urine. "
    "Eight years ago he underwent mechanical aortic valve replacement, and he takes warfarin. "
    "Echocardiography shows a new moderate paravalvular leak. There is no splenomegaly. The "
    "plasma of a centrifuged blood sample is pink.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.0 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 27% (N=41%–53%)\n"
    "Mean corpuscular volume 92 µm3 (N=80–100 µm3)\n"
    "Reticulocyte count 6.8% (N=0.5%–1.5%)\n"
    "Lactate dehydrogenase 890 U/L (N=45–200 U/L)\n"
    "Haptoglobin less than 10 mg/dL (N=41–165 mg/dL)\n"
    "Bilirubin, total 2.4 mg/dL (N=0.1–1.0 mg/dL)\n\n"
    "Direct antiglobulin test is negative. A peripheral smear is shown. Which of the following is "
    "most likely to be found in this patient?",
    {
        "Absent hemoglobin A on electrophoresis":
            "No hemoglobin A band is the diagnostic finding in homozygous sickle cell disease, which "
            "would have presented in childhood with sickle cells on the smear.",
        "Heinz bodies on supravital stain":
            "Heinz bodies are precipitated oxidized hemoglobin in G6PD deficiency after an oxidant "
            "exposure, removed by splenic macrophages to leave bite cells.",
        "Hemosiderin in urine sediment": "",
        "Increased osmotic fragility":
            "This belongs to hereditary spherocytosis — a lifelong EXTRAVASCULAR hemolysis with "
            "splenomegaly and spherocytes, not fragments.",
        "Palpable splenic enlargement":
            "Splenomegaly is the sign of EXTRAVASCULAR hemolysis, where the spleen does the "
            "destroying. These cells are being shredded inside the circulation.",
    },
    "Hemosiderin in urine sediment",
    "Intravascular hemolysis from a leaking mechanical valve — a macroangiopathic cause of "
    "fragmentation hemolysis.\n\n"
    "Chain: turbulent jet → shear force → red cells torn apart inside the vessel (schistocytes, "
    "helmet cells) → free hemoglobin enters plasma (pink plasma = hemoglobinemia) → haptoglobin, "
    "the plasma 'mop', is consumed (undetectable) → once haptoglobin is saturated, free hemoglobin "
    "is filtered by the glomerulus (hemoglobinuria: dipstick positive for blood with no red cells on "
    "microscopy) → proximal tubular cells take up the hemoglobin, store its iron as hemosiderin and "
    "shed into the urine → urine hemosiderin, which persists for weeks after an episode.\n\n"
    "Intravascular versus extravascular:\n"
    "• Intravascular — pink plasma, absent haptoglobin, hemoglobinuria and hemosiderinuria, "
    "schistocytes, normal spleen, HIGH kidney risk (free heme is nephrotoxic)\n"
    "• Extravascular — yellow plasma, mildly low haptoglobin, no hemoglobinuria, spherocytes, "
    "splenomegaly\n"
    "• Both — raised LDH, raised unconjugated bilirubin, raised reticulocytes\n\n"
    "Long-standing loss of iron in the urine can also make these patients iron deficient.\n\n"
    "Educational objective: Intravascular hemolysis releases free hemoglobin into plasma, producing "
    "hemoglobinemia, undetectable haptoglobin, hemoglobinuria and urine hemosiderin, with a risk of "
    "acute kidney injury. Extravascular hemolysis instead produces spherocytes and splenomegaly "
    "without free plasma hemoglobin.",
    "His new heart valve is chopping red cells to pieces inside his blood vessels. The spilled red "
    "stuff leaks into his pee, and the kidney keeps some of its iron and sheds it, which the lab can "
    "find.",
    image="fig_hx_schisto",
    imcap="Peripheral blood smear. Among normal-appearing erythrocytes are numerous small, "
          "irregular red cell fragments — triangular, helmet-shaped and spiculated forms. A "
          "lymphocyte is present at right.",
    exim="fig_slide_maha",
    excap="The lecture's microangiopathic and mechanical hemolysis slide.",
)

# ── 13. Pigment stones in a teenager → hereditary spherocytosis (§9) ─────────────
q(
    "A 15-year-old girl undergoes cholecystectomy due to recurrent right upper quadrant pain after "
    "meals. The opened gallbladder is shown. She has had episodes of yellow eyes since early "
    "childhood, usually during viral illnesses. Her father had his spleen removed as a teenager. "
    "The spleen tip is palpable 4 cm below the left costal margin.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 10.2 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 27% (N=36%–46%)\n"
    "Mean corpuscular volume 84 µm3 (N=80–100 µm3)\n"
    "Mean corpuscular hemoglobin concentration 37.8% (N=31%–36%)\n"
    "Reticulocyte count 9.5% (N=0.5%–1.5%)\n"
    "Bilirubin, total 3.1 mg/dL (N=0.1–1.0 mg/dL)\n"
    "Bilirubin, direct 0.2 mg/dL (N=0.0–0.3 mg/dL)\n\n"
    "Direct antiglobulin test is negative. This patient's underlying condition is most likely "
    "caused by a defect in which of the following?",
    {
        "Ankyrin": "",
        "Beta-globin chain":
            "Beta-globin mutations cause sickle cell disease and beta thalassemia. Thalassemia gives "
            "a LOW MCV and MCHC; sickle cell disease gives sickle cells and eventual loss, not "
            "enlargement, of the spleen.",
        "CD55 and CD59":
            "Loss of these complement regulators is paroxysmal nocturnal hemoglobinuria — an "
            "acquired INTRAVASCULAR hemolysis with hemoglobinuria and thrombosis, not a dominantly "
            "inherited disease with splenomegaly.",
        "Glucose-6-phosphate dehydrogenase":
            "G6PD deficiency is X-linked and episodic, triggered by oxidants, with bite cells and a "
            "normal MCHC. It does not give a raised MCHC or pass father to daughter as a dominant "
            "trait with splenectomy.",
        "Pyruvate kinase":
            "Pyruvate kinase deficiency is an autosomal recessive glycolytic defect causing chronic "
            "hemolysis without spherocytes or a raised MCHC.",
    },
    "Ankyrin",
    "Hereditary spherocytosis. The gallbladder contains black pigment (calcium bilirubinate) stones — "
    "in a teenager, almost never ordinary gallbladder disease, and a signal of chronic hemolysis.\n\n"
    "The chronic extravascular quartet is complete: anemia, jaundice (unconjugated — direct fraction "
    "normal), a big spleen, and pigment gallstones. Autosomal dominant inheritance shows in the "
    "father's teenage splenectomy.\n\n"
    "Mechanism: defective cytoskeletal protein (ankyrin most commonly; also band 3, beta-spectrin, "
    "alpha-spectrin, protein 4.2) → the lattice cannot hold the biconcave shape → membrane is lost → "
    "the cell becomes a sphere with the least surface area for its volume → it cannot deform through "
    "the splenic cords → splenic macrophages remove it (extravascular hemolysis) → chronic bilirubin "
    "load → pigment stones.\n\n"
    "Supporting findings: a HIGH MCHC (10.2 ÷ 27 = 37.8%; the cell is small for its hemoglobin), "
    "increased osmotic fragility, a high reticulocyte count, and — the value that excludes the "
    "look-alike — a NEGATIVE direct antiglobulin test (warm autoimmune hemolysis also makes "
    "spherocytes but is antibody-coated). Viral illnesses can trigger hemolytic crises (reticulocytes "
    "high) or, with parvovirus B19, aplastic crises (reticulocytes low).\n\n"
    "Educational objective: Hereditary spherocytosis is an autosomal dominant defect of red cell "
    "cytoskeletal proteins such as ankyrin and spectrin, causing extravascular hemolysis with "
    "splenomegaly, a high MCHC, increased osmotic fragility and early pigment gallstones. A negative "
    "direct antiglobulin test separates it from warm autoimmune hemolytic anemia.",
    "Her red blood cells are missing a piece of their inside scaffolding, so they become little balls "
    "instead of flexible discs. The spleen keeps grabbing and breaking them, and all that broken "
    "blood turns into black stones in her gallbladder.",
    image="fig_hx_pigment_stones",
    imcap="Opened gallbladder with a 4 cm scale bar. The lumen is packed with numerous small, hard, "
          "jet-black granular stones; the mucosa is green and bile-stained.",
    exim="fig_hx_spherocytes",
    excap="Peripheral smear from the same disease: small, dense erythrocytes lacking central pallor "
          "(arrow) among normal biconcave cells.",
)

# ── 14. G6PD deficiency — the failed antioxidant chain (§9) ──────────────────────
q(
    "A 24-year-old man comes to the emergency department due to 1 day of dark urine and "
    "yellow eyes. Three days ago he began trimethoprim-sulfamethoxazole for a urinary tract "
    "infection. His family emigrated from Sardinia. He had a similar episode as a child after "
    "eating broad beans. There is scleral icterus; the spleen is not palpable.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.1 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 24% (N=41%–53%)\n"
    "Mean corpuscular volume 94 µm3 (N=80–100 µm3)\n"
    "Reticulocyte count 7.2% (N=0.5%–1.5%)\n"
    "Lactate dehydrogenase 760 U/L (N=45–200 U/L)\n"
    "Haptoglobin 12 mg/dL (N=41–165 mg/dL)\n\n"
    "Direct antiglobulin test is negative. A peripheral smear is shown. Which of the following is "
    "the most likely underlying cause of this patient's hemolysis?",
    {
        "Antibody-mediated red cell opsonization":
            "Drug-induced IMMUNE hemolysis also follows a new drug, but the cells are antibody-coated "
            "and the direct antiglobulin test is positive. Here it is negative.",
        "Complement-mediated lysis of unprotected cells":
            "This is paroxysmal nocturnal hemoglobinuria (loss of CD55 and CD59) — chronic "
            "intravascular hemolysis with thrombosis, not an episode triggered by a sulfonamide.",
        "Cytoskeletal loss of membrane surface":
            "Hereditary spherocytosis gives chronic hemolysis with spherocytes, splenomegaly and a "
            "high MCHC, not bite cells after an oxidant drug.",
        "Deficient ATP generation through glycolysis":
            "Pyruvate kinase deficiency is chronic, not oxidant-triggered, and does not produce "
            "bite cells or Heinz bodies.",
        "Impaired regeneration of reduced glutathione": "",
        "Shear injury from platelet-rich microthrombi":
            "Thrombotic microangiopathies fragment cells into schistocytes and lower the platelet "
            "count. These cells have had a smooth bite removed, not been torn.",
    },
    "Impaired regeneration of reduced glutathione",
    "G6PD deficiency (Mediterranean variant, WHO class II), with hemolysis triggered by a "
    "sulfonamide, after a childhood episode of favism.\n\n"
    "The antioxidant chain: glucose-6-phosphate dehydrogenase → NADPH (the red cell's ONLY "
    "meaningful source) → glutathione reductase regenerates reduced glutathione → reduced "
    "glutathione neutralizes hydrogen peroxide. Break the first link → peroxide accumulates → "
    "hemoglobin is oxidized → it denatures and precipitates as Heinz bodies on the inner membrane "
    "→ splenic macrophages bite out the inclusion (bite and blister cells) → hemolysis, largely "
    "intravascular during a crisis.\n\n"
    "Why it is episodic: the variant enzyme is UNSTABLE. Old cells run out of activity; young cells "
    "are protected. A red cell has no nucleus and no mitochondria, so it cannot make replacement "
    "enzyme or find another NADPH source.\n\n"
    "Triggers: infections (the commonest), drugs (primaquine, chloroquine, sulfonamides, "
    "nitrofurantoin, dapsone) and fava beans. The enzyme assay can be falsely NORMAL during the "
    "crisis, because depleted old cells are gone and reticulocytes carry high enzyme levels — repeat "
    "it 2–3 months later or send a genetic test.\n\n"
    "Educational objective: G6PD deficiency limits NADPH production, so red cells cannot regenerate "
    "reduced glutathione to detoxify peroxide; oxidant stress (infection, sulfonamides, "
    "antimalarials, fava beans) precipitates hemoglobin as Heinz bodies, producing bite cells and "
    "episodic hemolysis with a negative direct antiglobulin test.",
    "His red cells are missing the helper that cleans up harmful 'rust' chemicals. The new medicine "
    "made a lot of that rust, so the cells got damaged, the spleen took bites out of them, and many "
    "burst.",
    image="fig_bite_cells",
    imcap="Peripheral blood smear. Several erythrocytes have a smooth semicircular defect at the "
          "edge, as though a portion had been removed, and appear smaller and more densely stained "
          "than the surrounding cells.",
    exim="fig_g6pd_pathway",
    excap="G6PD generates NADPH, which keeps glutathione reduced so it can neutralize peroxide.",
)

# ── 15. Beta thalassemia major — the unpaired chain is the poison (§10) ─────────
q(
    "A 2-year-old boy is brought to the office due to progressive pallor and poor weight gain. He "
    "was born at term and was well until about 6 months of age. His parents are first cousins of "
    "Cypriot descent. Examination shows frontal bossing, prominent maxillae, and a liver and spleen "
    "palpable 3 cm and 6 cm below the costal margins, respectively. A lateral skull radiograph is "
    "shown.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 6.1 g/dL (N=11.0–14.0 g/dL)\n"
    "Hematocrit 20% (N=33%–42%)\n"
    "Mean corpuscular volume 61 µm3 (N=70–86 µm3)\n"
    "Reticulocyte count 6.5% (N=0.5%–1.5%)\n"
    "Hemoglobin F 88% (N=less than 2%)\n"
    "Hemoglobin A2 5.4% (N=1.5%–3.5%)\n\n"
    "Hemoglobin A is not detected. Which of the following is the primary mechanism of this "
    "patient's anemia?",
    {
        "Formation of beta-chain tetramers":
            "Beta-chain tetramers are hemoglobin H, which forms in ALPHA thalassemia with one "
            "working alpha gene — the opposite chain imbalance.",
        "Formation of gamma-chain tetramers":
            "Gamma-chain tetramers are hemoglobin Barts, formed in a fetus with NO alpha genes, "
            "causing hydrops fetalis. This child has abundant alpha chains.",
        "Impaired heme synthesis in mitochondria":
            "This is sideroblastic anemia, with ringed sideroblasts and high iron — a heme defect, "
            "not a globin defect, and it would not alter the hemoglobin fractions.",
        "Oxidative denaturation of hemoglobin":
            "This is the G6PD mechanism — episodic, trigger-driven hemolysis with bite cells, not "
            "lifelong transfusion-level anemia with a globin switch failure.",
        "Polymerization of deoxygenated hemoglobin":
            "This is sickle cell disease, a QUALITATIVE beta-chain defect with sickle cells and "
            "hemoglobin S on electrophoresis.",
        "Precipitation of unpaired alpha chains": "",
    },
    "Precipitation of unpaired alpha chains",
    "Beta thalassemia major (homozygous beta-zero): no hemoglobin A, very high hemoglobin F, raised "
    "hemoglobin A2.\n\n"
    "Why it hurts: too few beta chains → a relative EXCESS of normal alpha chains with nothing to "
    "pair with → free alpha chains aggregate into insoluble inclusions → (1) erythroid precursors "
    "die in the marrow (ineffective erythropoiesis) and (2) the survivors are removed by the spleen "
    "(extravascular hemolysis). Severity tracks the chain you have too MUCH of — free alpha chains "
    "are more damaging than free beta chains, which at least form hemoglobin H.\n\n"
    "Why onset at 6 months: fetal hemoglobin (two alpha, two gamma) needs no beta chains, so the "
    "newborn is well; the anemia appears as the globin switch turns gamma off and beta fails to "
    "take over.\n\n"
    "Why the skull: ineffective erythropoiesis drives massive marrow expansion → the diploic space "
    "widens with vertical trabeculae ('hair-on-end') → frontal bossing and maxillary prominence; "
    "extramedullary hematopoiesis enlarges the liver and spleen.\n\n"
    "Management: lifelong transfusion every 3–4 weeks with iron chelation (the body cannot excrete "
    "iron), folic acid, genetic counseling (25% risk each pregnancy), and evaluation for transplant "
    "or gene therapy. Never give iron.\n\n"
    "Educational objective: In beta thalassemia, the relative excess of alpha-globin chains "
    "precipitates, killing erythroid precursors in the marrow and shortening red cell survival. "
    "Symptoms begin at 3–6 months as fetal hemoglobin declines, and marrow expansion produces bony "
    "deformities of the skull and face.",
    "His body can't make one of the two building blocks of hemoglobin, so the other building block "
    "piles up with no partner and clumps inside the cells, killing them. His bone marrow grows "
    "bigger and bigger trying to keep up, which changes the shape of his skull.",
    image="fig_hair_on_end",
    imcap="Lateral radiograph of the skull in a child. The space between the inner and outer tables "
          "of the cranial vault is widened, and fine striations run perpendicular to the skull "
          "surface.",
    exim="fig_electrophoresis",
    excap="Hemoglobin electrophoresis patterns — beta thalassemia shows an enlarged hemoglobin F "
          "band because beta chains are missing.",
)

# ── 16. Overwhelming post-splenectomy infection (§11, §55) ───────────────────────
q(
    "A 34-year-old man is brought to the emergency department due to 12 hours of fever, confusion, "
    "and a rapidly spreading rash. Four years ago he underwent emergency splenectomy for a "
    "shattered spleen after a motorcycle collision; he did not attend follow-up visits. "
    "Temperature is 39.8 C (103.6 F) and blood pressure is 76/40 mm Hg. Over the next day, the "
    "rash progresses to the changes shown in the extremities. Platelet count is 31,000/mm3, "
    "fibrinogen is 70 mg/dL, and prothrombin time is prolonged. Blood cultures grow gram-positive, "
    "lancet-shaped diplococci that are optochin-sensitive. Which of the following is the most "
    "important virulence factor of the causative organism in this patient?",
    {
        "IgA protease":
            "IgA protease helps pneumococci, meningococci and Haemophilus colonize mucosa. It does "
            "not explain why the organism overwhelms a patient WITHOUT A SPLEEN once it is in the "
            "blood.",
        "Lipooligosaccharide endotoxin":
            "This drives the fulminant sepsis of Neisseria meningitidis — also an encapsulated "
            "post-splenectomy pathogen — but meningococci are gram-negative diplococci.",
        "M protein":
            "M protein is the antiphagocytic factor of Streptococcus pyogenes, a beta-hemolytic "
            "chain-forming coccus that is not optochin-sensitive.",
        "Polysaccharide capsule": "",
        "Protein A":
            "Protein A binds the Fc portion of IgG for Staphylococcus aureus, which grows in "
            "clusters and is not a characteristic post-splenectomy pathogen.",
    },
    "Polysaccharide capsule",
    "Overwhelming post-splenectomy infection with Streptococcus pneumoniae, complicated by "
    "disseminated intravascular coagulation and purpura fulminans with peripheral gangrene.\n\n"
    "Why the spleen matters: encapsulated bacteria resist direct phagocytosis → clearance depends on "
    "opsonization plus the splenic red pulp filter (its cords and sinusoids are the body's 'oil "
    "filter') and on marginal zone B cells that make antibody against polysaccharide antigens → "
    "without a spleen, opsonized encapsulated bacteria circulate unchecked → sepsis progresses in "
    "HOURS, not days.\n\n"
    "The organisms that matter: Streptococcus pneumoniae (dominant, by a wide margin), Neisseria "
    "meningitidis and Haemophilus influenzae type b. Functional asplenia (sickle cell "
    "autosplenectomy) carries the same risk, and Howell-Jolly bodies on the smear announce it.\n\n"
    "Prevention is three-part: vaccinate against all three (before an elective splenectomy; after an "
    "emergency one — which this man never received), daily penicillin prophylaxis in children, and "
    "education that any fever is an emergency needing immediate empiric antibiotics without waiting "
    "for cultures.\n\n"
    "Educational objective: The spleen clears opsonized encapsulated bacteria from the blood, so "
    "anatomic or functional asplenia predisposes to fulminant sepsis from Streptococcus pneumoniae, "
    "Neisseria meningitidis and Haemophilus influenzae type b, whose polysaccharide capsules are "
    "their key virulence factor. Vaccination, pediatric penicillin prophylaxis and fever education "
    "prevent it.",
    "Some germs wear a slippery coat that makes them hard to grab. The spleen is the body's best net "
    "for catching them, so without a spleen those germs can take over the blood in just a few hours.",
    image="fig_opsi",
    imcap="Four panels of the patient's extremities over the following days: confluent purple-black "
          "discoloration of the hand and forearm and of the foot and leg, progressing to dry, "
          "blackened, necrotic digits with a sharply demarcated border of sloughing skin.",
    exim="fig_postsplen_uw",
    excap="Why asplenia predisposes to encapsulated-organism sepsis.",
)

# ── 17. Sickle cell disease — stroke prevention (§10) ───────────────────────────
q(
    "A 6-year-old girl with homozygous sickle cell disease is brought to the office for a routine "
    "health maintenance examination. She takes hydroxyurea and folic acid, and her vaccinations "
    "are up to date. She has had two vaso-occlusive pain episodes this year. Neurologic "
    "examination is normal. Screening transcranial Doppler ultrasonography shows a "
    "time-averaged mean maximum velocity of 228 cm/sec in the left middle cerebral artery "
    "(normal: less than 170 cm/sec), confirmed on repeat study. A peripheral smear is shown. "
    "Which of the following is the most appropriate intervention to reduce this patient's risk "
    "of the most likely serious complication?",
    {
        "Chronic red cell transfusion": "",
        "Continued daily penicillin prophylaxis":
            "Penicillin prevents pneumococcal sepsis in functionally asplenic young children. It "
            "does nothing about the cerebral vasculopathy the Doppler has detected.",
        "Elective laparoscopic splenectomy":
            "Splenectomy is for recurrent splenic sequestration crises or massive splenomegaly — "
            "not for stroke risk, and it would worsen her infection risk.",
        "Iron chelation with deferasirox":
            "Chelation treats iron overload that develops AFTER years of transfusion. It is a "
            "consequence of the correct answer, not a substitute for it.",
        "Long-term warfarin anticoagulation":
            "Sickle cell stroke is driven by sickling vasculopathy of large cerebral arteries, not "
            "by a cardioembolic or venous clot. Anticoagulation adds bleeding risk without "
            "addressing hemoglobin S.",
        "Low-dose daily aspirin therapy":
            "Aspirin is the secondary-prevention agent for atherosclerotic stroke in adults. It does "
            "not lower the hemoglobin S fraction, which is what drives sickle cell stroke.",
    },
    "Chronic red cell transfusion",
    "Sickle cell disease with an abnormal transcranial Doppler — high flow velocity through a "
    "narrowed middle cerebral artery → very high risk of ischemic stroke.\n\n"
    "Mechanism: deoxygenated hemoglobin S polymerizes (valine for glutamic acid exposes a "
    "hydrophobic patch) → rigid sickled cells → vaso-occlusion plus hemolysis-driven vasculopathy "
    "(free hemoglobin scavenges nitric oxide) → progressive narrowing of large cerebral arteries.\n\n"
    "Every sickle cell therapy attacks the same variable — the proportion and concentration of "
    "hemoglobin S. Chronic transfusion adds hemoglobin A, and randomized trial evidence shows that "
    "keeping hemoglobin S BELOW 30% significantly decreases stroke risk; this is done every 3–4 "
    "weeks, often by exchange transfusion so the patient is not made hyperviscous. Its costs are "
    "iron overload (→ chelation), alloimmunization (→ extended antigen-matched units), and "
    "infectious risk. Hydroxyurea (raises hemoglobin F), penicillin, vaccination and folic acid "
    "continue alongside it.\n\n"
    "Educational objective: Children with sickle cell disease and an abnormal transcranial Doppler "
    "velocity are at high risk of stroke and should receive chronic red cell transfusion to keep "
    "hemoglobin S below 30%. Transfusion carries the long-term costs of iron overload and "
    "alloimmunization.",
    "Her sticky, bent blood cells are slowly narrowing a big blood vessel in her brain. Giving her "
    "regular healthy blood dilutes the bent cells so the vessel is less likely to block and cause a "
    "stroke.",
    image="fig_hx_sickle",
    imcap="Peripheral blood smear. Many erythrocytes are elongated, crescent-shaped and pointed at "
          "both ends (arrow); a few oval and round cells are present.",
    exim="fig_slide_sickle_complications",
    excap="The lecture's summary of sickle cell complications.",
)

# ── 18. Sickle cell disease — the crisis with a low reticulocyte count (§10, §51) ─
q(
    "A 4-year-old boy with homozygous sickle cell disease is brought to the emergency department "
    "due to 2 days of lethargy and pallor. One week ago he had a low-grade fever and a red rash on "
    "both cheeks. He has not had pain and has not received a transfusion in the past year. His "
    "baseline hemoglobin is 8.2 g/dL. The spleen is not palpable.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 3.9 g/dL (N=11.0–14.0 g/dL)\n"
    "Hematocrit 12% (N=33%–42%)\n"
    "Mean corpuscular volume 84 µm3 (N=70–86 µm3)\n"
    "Leukocyte count 7,800/mm3 (N=5,500–15,500/mm3)\n"
    "Platelet count 290,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 0.1% (N=0.5%–1.5%)\n\n"
    "The peripheral smear shows sickled cells without hypersegmented neutrophils. Which of the "
    "following is the most likely cause of this patient's current condition?",
    {
        "Alloantibody-mediated delayed hemolysis":
            "A delayed hemolytic transfusion reaction appears 2–10 days after a transfusion, with a "
            "positive direct antiglobulin test and a HIGH reticulocyte count. He has not been "
            "transfused.",
        "Folate depletion from high cell turnover":
            "Folate deficiency also lowers the reticulocyte count in chronic hemolysis, but it "
            "develops gradually and produces macrocytosis and hypersegmented neutrophils, which are "
            "absent.",
        "Oxidant injury to hemoglobin":
            "Oxidant hemolysis (G6PD deficiency) would raise the reticulocyte count and produce "
            "bite cells.",
        "Splenic pooling of sickled cells":
            "Splenic sequestration also crashes the hemoglobin, but the spleen is suddenly ENORMOUS, "
            "the reticulocytes are HIGH, and platelets are often low. His spleen is not palpable.",
        "Vaso-occlusion in bone marrow":
            "Vaso-occlusive crises present with severe PAIN, and the hemoglobin is usually near "
            "baseline. He has no pain and has lost more than half his red cell mass.",
        "Viral infection of erythroid precursors": "",
    },
    "Viral infection of erythroid precursors",
    "Transient aplastic crisis from parvovirus B19 (the 'slapped cheek' rash of erythema "
    "infectiosum a week earlier).\n\n"
    "Mechanism: parvovirus B19 uses the erythrocyte P antigen to enter erythroid progenitors → lytic "
    "infection → red cell production stops for about a week → harmless in a healthy person, whose "
    "red cells live 120 days → catastrophic in chronic hemolysis, where cells live only 10–20 days "
    "and survival depends on a marrow running at maximum → hemoglobin halves, and the reticulocyte "
    "count falls to almost zero.\n\n"
    "Three crises, three reticulocyte counts:\n"
    "• Aplastic → reticulocytes LOW (production stopped)\n"
    "• Sequestration → reticulocytes HIGH, spleen suddenly enormous, often low platelets (cells are "
    "alive but trapped)\n"
    "• Vaso-occlusive → hemoglobin near baseline; the problem is pain and ischemia\n\n"
    "The same crisis occurs in hereditary spherocytosis and other chronic hemolytic anemias. "
    "Management is transfusion and supportive care until the marrow recovers; the patient is "
    "contagious, so isolate him from pregnant staff and immunocompromised patients.\n\n"
    "Educational objective: Parvovirus B19 infects erythroid precursors and halts red cell "
    "production, causing an aplastic crisis with a precipitous hemoglobin fall and "
    "reticulocytopenia in patients with chronic hemolysis. Splenic sequestration also drops the "
    "hemoglobin but with reticulocytosis and a suddenly enlarged spleen.",
    "A virus shut down his blood factory for a week. Most kids wouldn't notice, but his red cells "
    "die very fast, so without new ones his blood count fell dangerously low.",
    exim="fig_parvo_pronormoblast",
    excap="Parvovirus B19 in the marrow — a giant pronormoblast with intranuclear inclusions, and "
          "an absence of maturing red cell precursors.",
)

# ── 19. DIC after abruption — which product fixes fibrinogen (§12) ───────────────
q(
    "A 31-year-old woman at 36 weeks' gestation is brought to the emergency department due to "
    "severe abdominal pain and heavy vaginal bleeding. Placental abruption is diagnosed, and "
    "emergency cesarean delivery is performed. During surgery, she oozes from the incision, "
    "intravenous catheter sites, and gums. She has already received 4 units of red blood cells "
    "and 4 units of plasma.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.6 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 23% (N=36%–46%)\n"
    "Platelet count 64,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 24 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 58 sec (N=25–40 sec)\n"
    "Fibrinogen 78 mg/dL (N=200–400 mg/dL)\n"
    "D-dimer 6,400 ng/mL (N=less than 250 ng/mL)\n\n"
    "A peripheral smear shows scattered red cell fragments. Which of the following blood products "
    "is most appropriate to correct this patient's most critical hemostatic deficit?",
    {
        "Albumin":
            "Albumin is a pathogen-inactivated colloid for volume expansion. It contains NO "
            "coagulation factors and does nothing for hemostasis.",
        "Cryoprecipitate": "",
        "Factor VIII concentrate":
            "A specific factor concentrate is the answer for an ISOLATED single-factor deficiency "
            "such as hemophilia A. This is a consumptive, multi-factor coagulopathy.",
        "Four-factor prothrombin complex concentrate":
            "This contains factors II, VII, IX and X and is the product of choice for urgent "
            "WARFARIN reversal. It provides no fibrinogen.",
        "Plasma":
            "Plasma carries fibrinogen only at physiologic concentration, so correcting a level of "
            "78 mg/dL would take a volume she cannot tolerate — and she has already had 4 units.",
        "Platelets":
            "Her platelet count is low but above the thresholds that would be the limiting problem. "
            "Without fibrinogen, platelets have no fibrin mesh to anchor.",
    },
    "Cryoprecipitate",
    "Disseminated intravascular coagulation (DIC) triggered by placental abruption — blood clotting "
    "and breaking down clot at the same time: consumption of platelets and factors (prolonged PT and "
    "aPTT, low platelets), a very LOW fibrinogen, a HIGH D-dimer, and schistocytes from "
    "microthrombi.\n\n"
    "Why fibrinogen first: the intrinsic and extrinsic pathways converge on thrombin converting "
    "fibrinogen to fibrin, the protein that actually forms and cross-links the clot. Obstetric "
    "hemorrhage drops patients into a low-fibrinogen state very quickly.\n\n"
    "Cryoprecipitate: thaw frozen plasma in the refrigerator (1–6 C) → a cold-insoluble precipitate "
    "forms → it is concentrated fibrinogen plus factor VIII, von Willebrand factor, factor XIII and "
    "fibronectin → the fibrinogen of many units of plasma in a fraction of the volume. It is "
    "indicated for low fibrinogen, DIC, obstetric hemorrhage, and periodically during massive "
    "transfusion.\n\n"
    "Product → deficit: red cells → oxygen-carrying capacity; platelets → thrombocytopenia (not "
    "immune thrombocytopenia or dengue); plasma → multiple factor deficiency with bleeding; "
    "cryoprecipitate → fibrinogen; 4-factor prothrombin complex concentrate plus vitamin K → "
    "warfarin reversal; factor VIII concentrate → hemophilia A; albumin → volume only. The "
    "underlying cause (delivery) is treated alongside.\n\n"
    "Educational objective: Cryoprecipitate is the concentrated source of fibrinogen (with factor "
    "VIII, von Willebrand factor and factor XIII) and is the product of choice for "
    "hypofibrinogenemia in DIC and obstetric hemorrhage, where plasma cannot deliver enough "
    "fibrinogen in a tolerable volume.",
    "Her blood used up all of its 'glue' protein by making tiny clots everywhere, so now she can't "
    "stop bleeding. Cryo is a small bag packed with that glue, so it replaces a lot of it quickly.",
    exim="fig_slide_dic",
    excap="The lecture's DIC mechanism slide — simultaneous consumption of clotting factors and "
          "fibrinolysis.",
)

# ── 20. TRALI — donor anti-HLA antibodies and diffuse alveolar damage (§14) ──────
q(
    "A 58-year-old woman receiving warfarin for atrial fibrillation is admitted to the hospital "
    "due to a hip fracture. Before surgery, she receives 2 units of plasma. Forty minutes into the "
    "second unit, she develops acute dyspnea. Temperature is 38.4 C (101.1 F), blood pressure is "
    "84/50 mm Hg, and oxygen saturation is 80% on room air. Jugular venous pressure is not "
    "elevated. Chest radiography shows new bilateral diffuse infiltrates with a normal cardiac "
    "silhouette, and serum brain natriuretic peptide is normal. Gram stain and culture of the "
    "remaining plasma show no organisms. Despite mechanical ventilation, she dies 3 days later. A "
    "section of her lung at autopsy is shown. The implicated plasma came from a woman with 4 prior "
    "pregnancies. Which of the following is the most likely mechanism of this patient's reaction?",
    {
        "Bacterial endotoxin from a contaminated unit":
            "A septic reaction also brings fever and hypotension, most often from a room-temperature "
            "PLATELET unit. Plasma is stored frozen, and the unit culture here is sterile.",
        "Donor anti-HLA antibodies against recipient leukocytes": "",
        "Donor lymphocytes engrafting in recipient tissue":
            "Transfusion-associated graft-versus-host disease appears 1–6 WEEKS later with "
            "pancytopenia, rash, diarrhea and liver dysfunction; it is prevented by irradiation.",
        "Hydrostatic pulmonary edema from excess infused volume":
            "Circulatory overload (TACO) gives HYPERtension, a raised jugular venous pressure and a "
            "raised brain natriuretic peptide, and it responds to diuresis. She is hypotensive with "
            "flat neck veins.",
        "Recipient anti-IgA antibodies against donor plasma proteins":
            "Anaphylaxis in an IgA-deficient recipient begins within minutes, after a tiny volume, "
            "with urticaria, throat tightness and wheeze rather than fever and noncardiogenic "
            "pulmonary edema.",
        "Recipient IgM antibodies against donor red cells":
            "ABO incompatibility produces acute INTRAVASCULAR hemolysis — flank pain, pink plasma, "
            "hemoglobinuria and a positive direct antiglobulin test. Plasma carries no donor red "
            "cells to attack.",
    },
    "Donor anti-HLA antibodies against recipient leukocytes",
    "Transfusion-related acute lung injury (TRALI) — hypoxemia with bilateral infiltrates within 6 "
    "hours of a plasma-containing product, with hypotension, fever, flat neck veins and a normal "
    "brain natriuretic peptide.\n\n"
    "Mechanism: pregnancy exposes a woman to fetal cells bearing paternal tissue antigens → she forms "
    "anti-HLA antibodies (14%–20% of women who have been pregnant; more with each pregnancy) → "
    "they do her no harm → she donates → her plasma carries the antibodies to the recipient → they "
    "bind recipient leukocytes → leukoagglutination and neutrophil activation in the pulmonary "
    "capillaries → capillary leak → noncardiogenic pulmonary edema → diffuse alveolar damage with "
    "hyaline membranes (the autopsy section), the acute respiratory distress syndrome picture.\n\n"
    "TRALI versus TACO — both are hypoxic with a white-out:\n"
    "• TRALI — immune capillary injury; blood pressure LOW, jugular venous pressure normal, diuresis "
    "does not help\n"
    "• TACO — too much volume too fast; blood pressure HIGH, jugular venous pressure raised, "
    "diuresis helps\n\n"
    "Prevention is a public health success: blood centers test female donors for anti-HLA antibodies "
    "and avoid making high-plasma-volume products from those who have them. Management is supportive.\n\n"
    "Educational objective: TRALI is caused by donor anti-HLA (anti-leukocyte) antibodies, most often "
    "from multiparous female donors, that activate recipient neutrophils in the pulmonary "
    "capillaries, producing hypoxemia, hypotension and bilateral infiltrates within 6 hours. "
    "Circulatory overload instead causes hypertension, raised jugular venous pressure and responds "
    "to diuresis.",
    "The blood donor's body had made tiny 'attack' proteins during her past pregnancies. When they "
    "went into this patient, they made her white blood cells clump in her lungs, and the lungs "
    "flooded with fluid.",
    image="fig_hx_hyaline",
    imcap="Lung, hematoxylin and eosin. Alveolar walls are thickened and congested; many alveolar "
          "spaces are lined by bands of homogeneous, glassy pink material, and there is scattered "
          "intra-alveolar hemorrhage. A bronchiole and a congested vessel run down the left side.",
    exim="fig_tx_reactions",
    excap="The transfusion reaction differential side by side.",
)
