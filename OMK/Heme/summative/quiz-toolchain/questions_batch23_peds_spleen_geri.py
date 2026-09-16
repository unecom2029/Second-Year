# Batch 23 — Pediatrics, spleen & prescribing (10) · Trauma, edema & metastasis (10) · Geriatrics (5)
# §51 s46-pediatric · §52 s47-hypersplenism · §11 s10-spleen · §55 s52-splenic-trauma
# §54 s49-prescription · §56 s53-traumatic-edema · §57 s54-lymphatic-spread
# §53 s48-aging · §58 s55-geriatric-assessment
# Native LOs: 34, 47, 51, 60, 65, 67, 73, 77, 78

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


# ═════════════════════════════════════════════════════════════════════════════
# GROUP 1 — PEDIATRICS, SPLEEN & PRESCRIBING
# ═════════════════════════════════════════════════════════════════════════════

# §51 — the pancytopenic child and childhood leukemia prognosis (LO 65, 67)

q(
    "A 4-year-old boy is brought to the emergency department because of 3 weeks of pallor, bruising "
    "and pain in both legs that wakes him at night. He looks unwell and will not bear weight. He has "
    "small cervical and axillary nodes, and the spleen is palpable 5 cm below the left costal "
    "margin.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 6.8 g/dL (N=11.5–15.5 g/dL)\n"
    "Hematocrit 20% (N=35%–45%)\n"
    "Leukocyte count 2,900/mm3 (N=5,000–15,000/mm3)\n"
    "Platelet count 24,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 0.4% (N=0.5%–1.5%)\n\n"
    "A peripheral blood smear is shown. Which of the following findings would most strongly support "
    "this diagnosis over aplastic anemia?",
    {
        "A hypercellular marrow packed with immature cells": "",
        "An acellular marrow with fatty replacement":
            "This is the defining marrow finding of APLASTIC ANEMIA — hematopoietic tissue replaced by "
            "fat. It is the answer to the opposite question.",
        "A normal prothrombin time and partial thromboplastin time":
            "Normal coagulation studies are typical of aplastic anemia. In leukemia they MAY be "
            "deranged, particularly in acute promyelocytic leukemia — so a normal result argues weakly "
            "the other way.",
        "Mild generalized lymphadenopathy":
            "Both conditions produce mild generalized lymphadenopathy. It is the accompanying "
            "SPLENOMEGALY that separates them, which is why lymphadenopathy alone cannot do this work.",
        "Reticulocytopenia with a normocytic anemia":
            "A low reticulocyte count simply means the marrow is not producing, which is true whether "
            "the marrow is empty or packed with something that is not making red cells.",
    },
    "A hypercellular marrow packed with immature cells",
    "The first question in a pancytopenic child is not 'which disease' — it is 'how does the child "
    "look?' That single observation splits the differential before any test returns.\n\n"
    "• APLASTIC ANEMIA — a WELL-appearing child. Mild generalized lymphadenopathy but NO organomegaly. "
    "Pancytopenia including a low reticulocyte count. Normal coagulation studies and metabolic panel. "
    "Marrow ACELLULAR, fat having replaced hematopoietic tissue. Most often idiopathic in children, but "
    "also inherited syndromes, drugs, toxins, parvovirus and hepatitis. Definitive treatment is marrow "
    "transplant from a matched sibling.\n"
    "• LEUKEMIA — a SICK-appearing child. Lymphadenopathy WITH splenomegaly. Cytopenias with blasts. "
    "Coagulation may be deranged. Marrow PACKED with lymphoblasts or myeloblasts. Treatment is "
    "risk-stratified chemotherapy.\n\n"
    "This child is sick-appearing with splenomegaly and bone pain — the bone pain coming from marrow "
    "expansion under the periosteum, which is a childhood leukemia sign in its own right. Roughly 80% "
    "of childhood acute leukemia is acute lymphoblastic leukemia and 20% acute myeloid; within acute "
    "lymphoblastic leukemia about 80% is precursor-B and 20% precursor-T.\n\n"
    "Note the trap in the leukocyte count. It is LOW here, not high. Leukemia does not require a raised "
    "white count — the marrow is packed with blasts that are not being released or are not being "
    "counted as normal leukocytes, and the mature cells that should be there are gone.",
    "Two diseases both empty the blood counts. The question is what the marrow looks like: in one it "
    "is empty and replaced by fat, in the other it is crammed full of useless immature cells. And the "
    "child with the crammed marrow is the one who looks sick and has a big spleen.",
    image="fig_all_lymphoblasts",
    imcap="Peripheral blood smear: numerous large cells with scant cytoplasm, fine open chromatin and "
          "no cytoplasmic granules, among a reduced number of erythrocytes.",
    exim="fig_marrow_cellularity",
    excap="Marrow cellularity for comparison — hypercellular, normocellular and hypocellular, top to "
          "bottom. Normal cellularity is roughly (100 − the patient's age) percent.",
)

q(
    "Two children are evaluated for cytopenias. The first is a 6-year-old girl of short stature with "
    "café-au-lait macules, low-set ears, bilaterally absent thumbs and progressive pancytopenia. The "
    "second is a 9-month-old boy with bilaterally absent radii, PRESENT thumbs, and isolated "
    "thrombocytopenia that has been improving since birth. Which of the following statements about "
    "these two children is correct?",
    {
        "Both children should undergo chromosome breakage testing to confirm the diagnosis":
            "The breakage assay is the confirmatory test for Fanconi anemia only. The second child's "
            "syndrome is autosomal recessive and caused by RBM8A, and does not produce increased "
            "chromosome breaks.",
        "The first child has thrombocytopenia with absent radii and the second has Fanconi anemia":
            "This is the correct pair of diagnoses assigned to the wrong children — the single most "
            "likely error, and what the stem is built to catch.",
        "The first child's condition carries no increased malignancy risk":
            "Fanconi anemia carries a markedly raised lifetime risk of myelodysplasia, acute myeloid "
            "leukemia and squamous cell carcinoma, and that risk also alters transplant conditioning.",
        "The presence of thumbs in the second child excludes Fanconi anemia": "",
        "The second child's thrombocytopenia will progress to pancytopenia":
            "Thrombocytopenia with absent radii gives an ISOLATED thrombocytopenia that becomes LESS "
            "severe over time. Progressive pancytopenia belongs to Fanconi anemia.",
    },
    "The presence of thumbs in the second child excludes Fanconi anemia",
    "The radial ray is the whole discriminator, and it is worth memorizing in one line: **absent radii "
    "WITH thumbs present = thrombocytopenia with absent radii (TAR). Absent thumbs = Fanconi anemia.** "
    "Fanconi takes the thumbs; TAR leaves them.\n\n"
    "What makes a child's marrow failure inherited rather than acquired is almost always something "
    "visible on the general examination. Learn the extra-hematologic tell for each:\n\n"
    "• FANCONI ANEMIA — short stature, café-au-lait macules, absent or hypoplastic thumbs and radial "
    "ray anomalies, low-set ears. Progressive macrocytic pancytopenia with a low reticulocyte count "
    "and a hypocellular marrow. Confirm with a chromosome breakage assay (diepoxybutane or mitomycin "
    "C) showing increased breaks and radial forms — the defect is in DNA interstrand cross-link "
    "repair.\n"
    "• TAR — bilaterally absent radii with thumbs present. Isolated thrombocytopenia in infancy that "
    "becomes less severe with time. Autosomal recessive, RBM8A.\n"
    "• DIAMOND-BLACKFAN — craniofacial anomalies and triphalangeal thumbs, with PURE RED CELL aplasia: "
    "anemia and reticulocytopenia but normal white cells and platelets.\n"
    "• SHWACHMAN-DIAMOND — exocrine pancreatic insufficiency and metaphyseal dysostosis, with "
    "neutropenia as the dominant cytopenia. Malabsorption is the clue.\n"
    "• WISKOTT-ALDRICH — eczema and recurrent infection, with SMALL platelets, which is unusual since "
    "most thrombocytopenias give large ones. X-linked recessive.\n"
    "• TRANSIENT ERYTHROBLASTOPENIA OF CHILDHOOD — no findings at all outside the blood, in a "
    "previously well toddler after a viral illness. Isolated normocytic anemia with "
    "reticulocytopenia, and it resolves on its own. The benign one you must not over-investigate.",
    "Both children are missing bones in the forearm region, and the thumbs decide which syndrome it "
    "is. One condition takes the thumbs away; the other leaves them. That single detail changes the "
    "diagnosis, the test and the outlook completely.",
)

q(
    "An 11-month-old boy has had three episodes of otitis media, one pneumococcal pneumonia, and a "
    "persistent eczematous rash since 3 months of age. He bruises easily.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 11.0 g/dL (N=10.5–13.5 g/dL)\n"
    "Hematocrit 33% (N=33%–39%)\n"
    "Platelet count 34,000/mm3 (N=150,000–400,000/mm3)\n"
    "Mean platelet volume 5.1 fL (N=7.5–11.5 fL)\n"
    "Leukocyte count 8,400/mm3 (N=6,000–17,000/mm3)\n\n"
    "Which of the following is the most likely diagnosis?",
    {
        "Diamond-Blackfan anemia":
            "This is pure red cell aplasia — anemia with reticulocytopenia and NORMAL white cells and "
            "platelets — presenting in infancy with craniofacial anomalies and triphalangeal thumbs. "
            "His hemoglobin is normal and his platelets are not.",
        "Immune thrombocytopenia":
            "This typically follows a viral illness in an otherwise well child and produces LARGE "
            "platelets, because the marrow releases young ones to compensate. It explains neither the "
            "eczema nor the recurrent infections.",
        "Shwachman-Diamond syndrome":
            "The dominant cytopenia here is neutropenia, and the extra-hematologic tell is exocrine "
            "pancreatic insufficiency with steatorrhea, failure to thrive and metaphyseal dysostosis. "
            "His leukocyte count is normal.",
        "Thrombocytopenia with absent radii":
            "This gives isolated thrombocytopenia that improves with time, in a child with bilaterally "
            "absent radii and present thumbs. There is no eczema, no immunodeficiency, and the "
            "skeletal finding is absent here.",
        "Wiskott-Aldrich syndrome": "",
    },
    "Wiskott-Aldrich syndrome",
    "The triad is eczema, immunodeficiency and microthrombocytopenia, and it is X-linked recessive — "
    "which fits a boy.\n\n"
    "The platelet SIZE is the buried clue and the reason the mean platelet volume is given. Most "
    "thrombocytopenias produce LARGE platelets, because a marrow under pressure releases young, big "
    "ones; immune thrombocytopenia is the everyday example. Wiskott-Aldrich produces unusually SMALL "
    "platelets, which is the opposite of what a hurried reader expects and is therefore exactly what "
    "gets tested.\n\n"
    "The infections here are the immunodeficiency half of the triad — 'the baby gets sick a lot' — and "
    "encapsulated organisms such as pneumococcus feature because antibody responses to polysaccharide "
    "antigens are impaired.\n\n"
    "Set it against the rest of the inherited marrow failure family by asking what is visible outside "
    "the blood: radial ray and pigmentation in Fanconi, absent radii with thumbs in TAR, craniofacial "
    "anomalies with triphalangeal thumbs in Diamond-Blackfan, malabsorption in Shwachman-Diamond, and "
    "nothing at all in transient erythroblastopenia of childhood.",
    "A baby boy with itchy skin, frequent infections and easy bruising — three problems from one gene. "
    "The giveaway is that his platelets are unusually SMALL, which almost no other cause of low "
    "platelets does.",
)

q(
    "A 4-year-old girl is diagnosed with precursor-B acute lymphoblastic leukemia. Her presenting "
    "leukocyte count is 9,000/mm3, there is no central nervous system involvement, and blasts have "
    "cleared from the blood by day 8 of induction. Which additional finding would place her in a "
    "HIGH-risk category requiring intensified therapy and consideration of transplantation?",
    {
        "A hyperdiploid karyotype with 58 chromosomes":
            "Hyperdiploidy — 51 to 65 chromosomes — is a FAVORABLE ploidy finding. It is hypodiploidy, "
            "43 or fewer chromosomes, that is adverse.",
        "A precursor-B immunophenotype":
            "Precursor-B disease is the favorable immunophenotype and accounts for about 80% of "
            "childhood acute lymphoblastic leukemia. It is precursor-T disease that is unfavorable.",
        "Age of 4 years at diagnosis":
            "Age 2–10 years is the favorable band, and peak incidence at around 4 years does best. "
            "Under 1 year, or adolescent and adult, is unfavorable.",
        "Rapid clearance of blasts by day 8 of induction":
            "A rapid early response is favorable; a slow early response with persistent measurable "
            "residual disease is one of the most powerful adverse factors.",
        "t(9;22) producing a BCR-ABL1 fusion": "",
    },
    "t(9;22) producing a BCR-ABL1 fusion",
    "The Philadelphia chromosome is the single finding that would move an otherwise favorable child "
    "into a high-intensity, transplant-directed protocol. Historically it was the worst-prognosis "
    "group in acute lymphoblastic leukemia — and it is also why adding a tyrosine kinase inhibitor "
    "transformed that subgroup's outlook.\n\n"
    "The prognostic table, which is what the objective asks for:\n\n"
    "| Variable | Favorable | Unfavorable |\n"
    "| Age | 2–10 years | Under 1 year, or adolescent/adult |\n"
    "| Immunophenotype | Precursor B | Precursor T |\n"
    "| Ploidy | Hyperdiploid, 51–65 chromosomes | Hypodiploid, 43 or fewer |\n"
    "| Translocation | t(12;21) → ETV6-RUNX1 | t(9;22) → BCR-ABL1; t(1;19) → TCF3-PBX1 |\n"
    "| Presenting leukocyte count | Low | High |\n"
    "| Central nervous system | Not involved | Involved at diagnosis |\n"
    "| Early response | Rapid blast clearance | Slow early response |\n\n"
    "Risk-based treatment follows directly: favorable disease gets low-intensity standard "
    "chemotherapy, unfavorable disease gets high-intensity therapy and transplantation.\n\n"
    "Two hooks worth stealing. B-cell markers are the big numbers (CD19, CD20, CD22); T-cell markers "
    "are the small ones (CD2, CD3, CD4, CD7, CD8). And T-ALL means a Thymic mass in a Teenager — about "
    "70% present with a mediastinal mass, more often in adolescent males.\n\n"
    "Morphology does not predict immunophenotype, so immunophenotyping is mandatory to assign risk. "
    "Total treatment runs about 2.5 years — induction, consolidation (which clears the sanctuary "
    "sites), interim maintenance, delayed intensification, then roughly 18 months of maintenance.",
    "Everything about this child is in the good column — her age, her cell type, her low white count, "
    "her fast response. One particular gene swap would override all of it and move her to the "
    "toughest treatment plan.",
)

# §52 / §11 — hypersplenism and the asplenic patient (LO 73, 51)

q(
    "A 54-year-old man with alcohol-associated cirrhosis is referred because of abnormal blood "
    "counts. He has no bleeding and no infections.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 10.6 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 32% (N=41%–53%)\n"
    "Leukocyte count 2,700/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 58,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "The spleen is palpable 7 cm below the costal margin. The peripheral smear shows normal "
    "morphology with no dysplasia, blasts or schistocytes. Bone marrow biopsy is normocellular with "
    "adequate, morphologically normal megakaryocytes. Which of the following is the most appropriate "
    "management?",
    {
        "Eltrombopag to raise the platelet count":
            "A thrombopoietin receptor agonist addresses underproduction. His megakaryocytes are "
            "adequate and his marrow is normocellular — production is not the problem.",
        "Management directed at his portal hypertension": "",
        "Prednisone for presumed immune destruction":
            "Immune thrombocytopenia gives an isolated thrombocytopenia, splenomegaly is rare, and it "
            "would not explain three depressed cell lines with a 7 cm spleen.",
        "Splenectomy to correct the cytopenias":
            "Splenectomy is generally NOT indicated for portal hypertension. The cytopenias of "
            "congestive hypersplenism are usually moderate and do not themselves require treatment, and "
            "removing the spleen strips a cirrhotic patient of encapsulated-organism defence for a "
            "problem that was not threatening his life.",
        "Splenic artery embolization to reduce splenic inflow":
            "This is used in selected refractory cases, but it carries infarction and abscess risk and "
            "does not address the portal pressure that is driving the congestion.",
    },
    "Management directed at his portal hypertension",
    "Secondary hypersplenism from congestive splenomegaly — and portal hypertension is the most "
    "common cause of secondary hypersplenism.\n\n"
    "The logic is in the marrow and the smear. Three cell lines are down while the marrow is "
    "normocellular with adequate megakaryocytes and the morphology is normal: the cells are being "
    "MADE properly and removed peripherally. Hypersplenism is functional hyperactivity of the spleen "
    "causing loss of one or more cell populations — the cells themselves are normal, and an enlarged, "
    "overactive organ simply removes too many of them.\n\n"
    "The anatomy explains why cirrhosis does this. The spleen's ONLY venous outflow runs through the "
    "portal system, so anything raising portal pressure backs blood up and the organ engorges.\n\n"
    "The normal morphology also does the differential work: no schistocytes excludes a thrombotic "
    "microangiopathy and disseminated intravascular coagulation, no dysplasia excludes myelodysplasia, "
    "and adequate megakaryocytes with a normocellular marrow exclude marrow failure and alcohol-"
    "induced marrow toxicity.\n\n"
    "Distinguish primary hypersplenism — functional change with no underlying hematologic disorder or "
    "infection, rare, and far more common in women — from secondary hypersplenism, which is what you "
    "will actually see.",
    "His liver disease has dammed up the blood trying to leave the spleen, so the spleen has swollen "
    "and is eating too many normal blood cells. The fix is the dam, not the spleen — and removing the "
    "spleen would leave him defenceless against infection.",
    exim="fig_splenomegaly_causes",
    excap="The three mechanisms of splenomegaly — congestion from decreased drainage is the column this "
          "patient sits in.",
)

q(
    "A 47-year-old man with a history of two episodes of alcohol-associated pancreatitis presents "
    "with hematemesis. Upper endoscopy shows large gastric fundal varices with a recent bleeding "
    "stigma; the esophagus is normal. Liver function tests are normal and there is no ascites. "
    "Contrast-enhanced computed tomography shows a normal liver and a thrombosed splenic vein. Which "
    "of the following is the definitive treatment?",
    {
        "Nonselective beta blockade":
            "This reduces portal pressure in cirrhotic portal hypertension. His liver is normal and his "
            "portal pressure is not the problem — the obstruction is isolated to the splenic vein.",
        "Splenectomy": "",
        "Systemic anticoagulation alone":
            "Anticoagulation is used in acute splenic vein thrombosis without bleeding, but in a "
            "patient who is actively bleeding from varices it treats neither the varices nor the "
            "collateral circulation that created them.",
        "Transjugular intrahepatic portosystemic shunt":
            "A shunt decompresses the PORTAL vein in cirrhosis. It cannot decompress a segment "
            "obstructed upstream of it, and the normal liver means there is no portal hypertension to "
            "shunt.",
        "Endoscopic band ligation of the gastric varices":
            "Band ligation is effective for esophageal varices and is technically difficult and often "
            "unsuccessful for fundal gastric varices. It is also a temporizing measure that leaves the "
            "cause in place.",
    },
    "Splenectomy",
    "This is 'left-sided' or sinistral portal hypertension, and splenectomy is CURATIVE.\n\n"
    "The anatomy: the splenic vein runs along the LOWER (inferior) border of the pancreas, directly "
    "behind it, before joining the superior mesenteric vein to form the portal vein. That course is "
    "why pancreatitis is the most common cause of splenic vein thrombosis — an inflamed pancreas or a "
    "pseudocyst compresses and thromboses the low-pressure vein long before it troubles the artery, "
    "which runs along the SUPERIOR border.\n\n"
    "The consequence is specific: the short gastric veins drain into the splenic vein, so when it "
    "occludes they become the collateral route and enlarge into GASTRIC FUNDAL varices — with normal "
    "esophageal veins and a normal liver, which is exactly the pattern in this stem. Removing the "
    "spleen removes the inflow that is feeding those collaterals, and the varices decompress.\n\n"
    "Artery above, vein below, and the asymmetry matters: it takes a lot to compress an artery and "
    "very little to compress a low-pressure vein. That is why splenic vein thrombosis is a recognized "
    "complication of pancreatitis and splenic artery thrombosis is not.",
    "His pancreatitis clotted off the vein draining the spleen, so blood found a detour through the "
    "stomach wall and blew those veins up into bleeding varices. Removing the spleen removes the blood "
    "supply feeding the detour.",
    exim="fig_splenic_vein",
    excap="The splenic vein running below and behind the pancreas to join the superior mesenteric vein, "
          "with the gastric tributaries that become varices when it occludes.",
)

q(
    "A 22-year-old woman is scheduled for elective splenectomy for hereditary spherocytosis. Which of "
    "the following is the most appropriate approach to reducing her risk of overwhelming "
    "post-splenectomy infection?",
    {
        "Administer pneumococcal, meningococcal and Haemophilus influenzae type b vaccines 2 weeks "
        "before the operation": "",
        "Administer the vaccines at the first postoperative clinic visit":
            "This is the correct approach after an UNPLANNED, emergency splenectomy, where "
            "pre-operative vaccination is impossible — commonly about 14 days postoperatively, when the "
            "immune response is better. Her operation is elective, so the better option is available.",
        "Begin lifelong daily penicillin and omit vaccination":
            "Antibiotic prophylaxis and vaccination are complementary, not alternatives. Daily "
            "penicillin is the standard of care in CHILDREN, particularly in sickle cell disease where "
            "the spleen is functionally gone in the first years of life.",
        "No prophylaxis is required, because overwhelming post-splenectomy infection occurs in fewer "
        "than 1% of patients":
            "The incidence is genuinely rare, under 1% — but the mortality is what makes it matter. "
            "Rare and lethal is precisely the profile that justifies prevention.",
        "Reserve vaccination until a febrile illness occurs":
            "Vaccination takes weeks to generate protection. By the time fever appears, the window for "
            "prevention has closed — at that point the action is immediate empiric antibiotics.",
    },
    "Administer pneumococcal, meningococcal and Haemophilus influenzae type b vaccines 2 weeks before "
    "the operation",
    "The rule is simple and the timing is what gets tested: for an ELECTIVE splenectomy, vaccinate 2 "
    "weeks before operating. For an UNPLANNED splenectomy that is impossible, so vaccinate before "
    "discharge. A trivalent preparation covering all three organisms is available.\n\n"
    "Mechanism: the spleen is the body's principal filter for encapsulated organisms, and without it "
    "opsonized encapsulated bacteria are not cleared. A bloodstream infection can then progress to "
    "overwhelming sepsis within HOURS rather than days. The organisms are Streptococcus pneumoniae "
    "(the dominant risk by a wide margin), Neisseria meningitidis, and Haemophilus influenzae type b.\n\n"
    "Timing of the risk: most septic episodes occur within 2 years of splenectomy, and risk is "
    "greatest if the spleen is removed in the first 2–4 years of life — which is exactly why elective "
    "splenectomy for hereditary spherocytosis is deferred past age 4.\n\n"
    "Presentation is the danger: nonspecific, mild, influenza-like symptoms that progress rapidly to "
    "high fever, shock and death. The intervention that actually saves lives is educating the patient "
    "and family that ANY fever is an emergency requiring immediate evaluation and empiric antibiotics "
    "without waiting for cultures — if symptoms begin, start penicillin immediately.\n\n"
    "Splenectomy works in hereditary spherocytosis because the spleen is the site of DESTRUCTION, not "
    "the site of the defect. The cells remain spherocytic afterwards, but without the splenic cords to "
    "trap them their lifespan approaches normal.",
    "Her spleen is the organ that clears bacteria wearing a sugar coat. Once it is gone those bacteria "
    "can kill in hours, so she is vaccinated two weeks beforehand — while the spleen is still there to "
    "help her respond to the vaccine.",
    exim="fig_opsi",
    excap="Overwhelming post-splenectomy sepsis — purpura fulminans and peripheral gangrene, the "
          "endpoint the vaccination schedule exists to prevent.",
)

q(
    "A 9-year-old boy with homozygous sickle cell disease is brought to the emergency department with "
    "a temperature of 39.2°C (102.6°F) and a mild cough. He is alert and well-perfused, with no focal "
    "findings. His last transfusion was 2 years ago. A peripheral smear shows sickled cells, target "
    "cells and several erythrocytes containing small, dense, round basophilic inclusions. Which of the "
    "following is the most appropriate immediate action?",
    {
        "Administer broad-spectrum antibiotics after obtaining blood cultures": "",
        "Arrange outpatient follow-up in 24 hours with oral antipyretics":
            "This would be reasonable in a well child without sickle cell disease. In functional "
            "asplenia the window between a nonspecific febrile illness and overwhelming sepsis is "
            "measured in hours.",
        "Begin exchange transfusion":
            "Exchange transfusion is used for acute chest syndrome, stroke and other severe "
            "vaso-occlusive complications. He has no evidence of any of those, and it does not treat "
            "bacteremia.",
        "Obtain a bone marrow aspirate to assess erythroid precursors":
            "This would be directed at an aplastic crisis from parvovirus B19, which is identified by a "
            "FALLING reticulocyte count rather than by fever, and is not an emergency procedure.",
        "Palpate for splenomegaly and transfuse immediately if the spleen is enlarged":
            "Splenic sequestration is the crisis that kills in hours, but it occurs in infants under 2 "
            "with homozygous disease — and by age 9 his spleen has autoinfarcted, which is precisely "
            "what the smear is telling you.",
    },
    "Administer broad-spectrum antibiotics after obtaining blood cultures",
    "Fever above 38.5°C (101.1°F) in a child with sickle cell disease is an EMERGENCY. Obtain basic "
    "diagnostic labs and administer broad-spectrum antibiotics immediately — do not wait for a source "
    "or for culture results.\n\n"
    "The buried clue is the smear. The small, dense, round basophilic inclusions are Howell-Jolly "
    "bodies — retained nuclear DNA fragments that a working spleen would have pitted out. Their "
    "presence means the spleen is absent or non-functional. In sickle cell disease this happens "
    "through repeated infarction over the first years of life: autosplenectomy, with an infection risk "
    "identical to that of a surgically asplenic patient.\n\n"
    "Functional asplenia also explains the rest of his risk profile — increased risk of stroke and "
    "acute chest syndrome — and it is why these children need earlier pneumococcal and meningococcal "
    "vaccination than the standard schedule, plus daily penicillin prophylaxis in childhood.\n\n"
    "For the pediatric crises as a set:\n"
    "• SPLENIC SEQUESTRATION — sudden trapping of blood in the spleen, usually in infants under 2 with "
    "homozygous disease (later in HbSC or sickle-β-thalassemia, whose spleens survive longer). The "
    "spleen is enlarged, hemoglobin falls more than 2 g/dL below baseline with relative "
    "thrombocytopenia, and it can be fatal within hours. Fluids, transfusion, and splenectomy for "
    "recurrent episodes.\n"
    "• APLASTIC CRISIS — parvovirus B19 halts erythropoiesis; the RETICULOCYTE count falls, which is "
    "what separates it from every other crisis.\n"
    "• VASO-OCCLUSIVE CRISIS — ischemic pain in chest, abdomen and joints.",
    "Years of sickling have destroyed his spleen, so the bacteria it used to filter can overwhelm him "
    "within hours. In a child with this disease, a fever is not something to watch — antibiotics go in "
    "straight away.",
)

# §54 — writing a prescription (LO 78)

q(
    "A resident writes the following prescription for a patient with newly diagnosed iron deficiency "
    "anemia:\n\n"
    "  Ferrous sulfate 325 mg tablets\n"
    "  Sig: Take 1 tablet by mouth three times daily with vitamin C\n"
    "  Indication: iron deficiency anemia\n"
    "  Refills: 2\n\n"
    "The pharmacist telephones to say the prescription cannot be filled. Which element is missing?",
    {
        "The dosage form":
            "This is present — 'tablets.' Dosage form matters wherever a drug exists in more than one "
            "form, which is especially common in pediatrics.",
        "The indication":
            "This is present, and the lecture flags it with an exclamation mark. It lets the pharmacist "
            "catch a drug-indication mismatch and matters most for an as-needed medication, where the "
            "patient otherwise has no way to know when to take it.",
        "The quantity to dispense": "",
        "The route of administration":
            "This is present — 'by mouth,' within the Sig. The Sig should carry dose, route and "
            "frequency, and duration where relevant.",
        "The number of refills":
            "This is present and correctly specified as a number. Leaving refills blank creates "
            "ambiguity, which is why a number — including zero — is always written.",
    },
    "The quantity to dispense",
    "Without 'Disp: #90' the pharmacist has no way to know whether to supply one month or three, and "
    "cannot fill the prescription at all.\n\n"
    "The lecture reduces a prescription to a bare minimum of five things. If a question asks what is "
    "missing, check these first: **drug, dose, indication, amount to dispense, and refills.**\n\n"
    "The fuller element list, which is standard prescribing practice:\n"
    "• Date written — determines validity; controlled substances expire\n"
    "• Patient identifiers — full name, date of birth, address. The date of birth is the safety check "
    "against dispensing to the wrong person and against age-inappropriate dosing\n"
    "• Drug name — generic preferred, because brand names look alike and sound alike\n"
    "• Strength — most drugs come in several\n"
    "• Dosage form — tablet, capsule, solution, suspension, patch\n"
    "• Quantity to dispense\n"
    "• Sig — dose, route, frequency, and duration where relevant. The single most-read line on the "
    "label, and vague directions are the commonest cause of patient dosing error\n"
    "• Indication\n"
    "• Refills — a number, including zero\n"
    "• Prescriber — signature, printed name, and identifying number\n\n"
    "Nothing else here is wrong: there is no trailing zero, no missing leading zero, and no "
    "error-prone abbreviation. Those are the other things to scan for on any prescription question.\n\n"
    "One drug-specific point on this prescription: specify the SALT, because the percentage of "
    "elemental iron differs — ferrous fumarate 33%, ferrous sulfate 20%, ferrous gluconate about 12%.",
    "Everything is there except how many pills to hand over. The pharmacist cannot guess whether to "
    "give a month's worth or three months' worth, so the prescription is simply unfillable.",
)

q(
    "A hospital patient-safety committee reviews four medication orders written overnight. Which of "
    "the following is written correctly according to standard patient-safety conventions?",
    {
        "Enoxaparin 40 mg subcutaneously daily": "",
        "Heparin 5000 U subcutaneously every 8 hours":
            "'U' is misread as a zero, turning 5000 U into 50000. Write the word 'units' out in full. "
            "This is the classic insulin and heparin error.",
        "Hydromorphone 1.0 mg intravenously every 4 hours as needed":
            "A trailing zero is dangerous: if the decimal point is missed, 1.0 mg reads as 10 mg — a "
            "tenfold overdose. Write 1 mg.",
        "MS 2 mg intravenously every 2 hours as needed for pain":
            "'MS' has been used for both morphine sulfate and magnesium sulfate — two completely "
            "different drugs. Spell the drug name out in full.",
        "Warfarin .5 mg by mouth QD":
            "Two errors in one line. A missing leading zero means .5 mg reads as 5 mg if the decimal is "
            "missed — write 0.5 mg. And QD is readily confused with QOD and QID — write 'daily' out.",
    },
    "Enoxaparin 40 mg subcutaneously daily",
    "This order has a full generic drug name, a whole number with no trailing zero, a spelled-out "
    "route, and a spelled-out frequency. Nothing in it can be misread.\n\n"
    "The patient-safety conventions, which are what actually get tested:\n\n"
    "| Rule | Write this | Never this | Why |\n"
    "| No trailing zero | 1 mg | 1.0 mg | A missed decimal point reads as 10 mg — tenfold overdose |\n"
    "| Always a leading zero | 0.5 mg | .5 mg | A missed decimal point reads as 5 mg — tenfold "
    "overdose |\n"
    "| Write 'units' out | 10 units | 10 U | 'U' is misread as a zero — 10 U becomes 100 |\n"
    "| Write frequency out | daily, every other day, four times daily | QD, QOD, QID | These three are "
    "readily confused with each other |\n"
    "| Spell the drug fully | morphine sulfate, magnesium sulfate | MS, MSO₄, MgSO₄ | 'MS' has meant "
    "both |\n"
    "| Quantity in words too | #90 (ninety) | #90 alone, for controlled substances | Prevents "
    "alteration of the numeral |\n\n"
    "Notice that every one of these rules exists because of a specific, documented, fatal error — they "
    "are not stylistic preferences. Two of them (the trailing zero and the missing leading zero) "
    "produce the same catastrophe by opposite routes: a tenfold overdose from one misread character.",
    "Each of these rules exists because someone died from a misread scribble. A stray decimal, a 'U' "
    "that looks like a zero, or an abbreviation meaning two different drugs — all of them turn into "
    "tenfold overdoses.",
)

# ═════════════════════════════════════════════════════════════════════════════
# GROUP 2 — TRAUMA, EDEMA & METASTASIS
# ═════════════════════════════════════════════════════════════════════════════

# §55 — splenic injury (LO 47, 73)

q(
    "A 31-year-old man is brought in after a high-speed motor vehicle collision. He is pale and "
    "diaphoretic with a pulse of 138/min and blood pressure 78/44 mm Hg, which rises only transiently "
    "to 92/56 mm Hg after 2 L of crystalloid. There is bruising across the left chest wall and "
    "abdomen. Bedside focused assessment with sonography for trauma shows free fluid in the "
    "splenorenal recess and the pelvis. Which of the following is the most appropriate next step?",
    {
        "Admission for non-operative management with serial hematocrits":
            "Non-operative management is for the haemodynamically STABLE patient with no blush and no "
            "peritonitis. It requires a patient whose physiology allows you to watch, and his does not.",
        "Angiography with splenic artery embolization":
            "Embolization is rung 2 of the ladder and requires a stable patient. Taking a "
            "fluid-unresponsive hypotensive patient to the angiography suite has the same problem as "
            "taking him to the scanner — he is bleeding faster than the rung can work.",
        "Computed tomography of the abdomen and pelvis with intravenous contrast":
            "This is the correct study for the STABLE patient — it grades the injury and detects a "
            "contrast blush. An unstable trauma patient does not go to the scanner.",
        "Diagnostic peritoneal lavage":
            "This has been largely replaced by bedside ultrasound, and here it would add nothing: the "
            "ultrasound has already demonstrated free fluid in a patient who needs an operation.",
        "Immediate laparotomy": "",
    },
    "Immediate laparotomy",
    "The diagnostic fork is decided by haemodynamic stability, and that single rule is worth more "
    "marks than the whole grading table:\n\n"
    "• UNSTABLE → bedside focused assessment with sonography for trauma. Free fluid on ultrasound in an "
    "unstable patient means the OPERATING ROOM. Do not send an unstable trauma patient to computed "
    "tomography.\n"
    "• STABLE → computed tomography with intravenous contrast, which grades the injury and detects the "
    "contrast blush.\n\n"
    "He is a transient responder — an initial rise that does not hold means ongoing haemorrhage. The "
    "three-rung management ladder therefore skips straight to rung 3:\n\n"
    "1. MEDICAL / non-operative management — stable, no blush, no peritonitis, regardless of grade in "
    "most modern protocols. Monitored bed, bed rest, serial haemoglobin and haematocrit, serial "
    "abdominal examination, type and cross held active. It is the default and succeeds in the large "
    "majority, more often in children, whose splenic capsules are thicker.\n"
    "2. INTERVENTIONAL — angiography with splenic artery embolization, for the stable patient with a "
    "blush, a pseudoaneurysm, an arteriovenous fistula, or a grade IV–V injury.\n"
    "3. SURGICAL — instability despite resuscitation, peritonitis, or failure of the rungs above. "
    "Spleen-preserving options exist (splenorrhaphy, partial splenectomy) but the unstable patient "
    "gets a total splenectomy, because the correct operation in a crashing patient is the fast one.\n\n"
    "The practical threshold the lecturer quoted: if they are going to need more than 2 units of blood, "
    "take it out.",
    "His blood pressure keeps dropping no matter how much fluid goes in, and the ultrasound shows "
    "blood in his belly. There is no time for a scan — the bleeding has to be stopped in the operating "
    "room.",
)

q(
    "A 27-year-old man is brought in after a motor vehicle collision. He is alert, with a pulse of "
    "104/min and blood pressure 118/74 mm Hg that remains stable after 1 L of crystalloid. He has "
    "left-sided lower rib tenderness and left shoulder pain that worsens when the bed is laid flat. "
    "Computed tomography of the abdomen with intravenous contrast is shown; it demonstrates a 4-cm "
    "intraparenchymal splenic laceration with a focus of active contrast extravasation contained "
    "within the splenic capsule. Which of the following is the most appropriate next step?",
    {
        "Angiography with splenic artery embolization": "",
        "Admission for observation with serial abdominal examinations":
            "This would be the answer if the scan showed a laceration with NO blush. Active "
            "extravasation means the spleen is bleeding at the moment of the scan, and that is the "
            "finding that moves him up a rung.",
        "Immediate laparotomy with total splenectomy":
            "This is for the unstable patient, for peritonitis, or for failure of the rungs above. He "
            "is stable after 1 L of fluid, and the extravasation is contained within the capsule.",
        "Repeat computed tomography in 48 hours":
            "Follow-up imaging is obtained in higher-grade injuries to look for a developing "
            "pseudoaneurysm. It is surveillance, not treatment, and it does nothing about bleeding "
            "that is visible right now.",
        "Splenorrhaphy with mesh wrap":
            "Suture repair and mesh wrap are spleen-preserving SURGICAL options. Taking him to theatre "
            "is unnecessary when an interventional radiologist can stop the bleeding without an "
            "incision.",
    },
    "Angiography with splenic artery embolization",
    "The finding that drives this is the contrast BLUSH. Active extravasation means the spleen is "
    "bleeding at the moment of the scan, and that is what separates a patient who can simply be "
    "observed from one whose bleeding must be stopped. The grade — this is grade IV by the presence of "
    "contained active bleeding — is not the deciding variable on its own.\n\n"
    "Two things kept him off the operating table: he is haemodynamically stable after fluid, and the "
    "extravasation is contained within the capsule. Embolization is the rung that converts a patient "
    "who would once have lost the spleen into one who keeps it. PROXIMAL embolization drops perfusion "
    "pressure while letting collaterals preserve the organ; DISTAL (selective) embolization targets "
    "the bleeding vessel itself.\n\n"
    "The other indications for rung 2 are a pseudoaneurysm, an arteriovenous fistula, and a high-grade "
    "(IV–V) injury.\n\n"
    "The left shoulder pain worse when supine is KEHR SIGN — blood irritating the left hemidiaphragm "
    "and referring along the C3–C5 phrenic nerve to the shoulder dermatome. It names the organ but "
    "does not decide the management. Left lower rib fractures work the same way: the ribs that protect "
    "the spleen are the ribs that lacerate it, and rib tenderness should trigger imaging even if the "
    "abdomen is initially soft.",
    "The scan catches dye leaking out of a torn vessel — the spleen is bleeding right now. But his "
    "blood pressure is holding and the blood is still inside the capsule, so a radiologist can plug the "
    "vessel through a catheter instead of a surgeon removing the organ.",
    image="fig_splenic_injury_ct",
    imcap="Contrast-enhanced axial computed tomography of the upper abdomen: the spleen is "
          "heterogeneous with surrounding low-attenuation fluid, and a rounded focus of bright "
          "contrast lies within the parenchyma near the hilum (arrow and arrowhead).",
)

q(
    "A 19-year-old woman sustained a grade III splenic laceration in a fall and has been managed "
    "non-operatively. She has been stable with a steady hematocrit for 5 days. On the morning of day "
    "6 she develops sudden severe left upper quadrant pain and lightheadedness. Her pulse is 128/min "
    "and blood pressure 84/50 mm Hg.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 6.9 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 21% (N=36%–46%)\n"
    "Platelet count 198,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Which of the following best explains this deterioration?",
    {
        "An expanding subcapsular hematoma that has ruptured": "",
        "A splenic abscess arising in devascularized parenchyma":
            "Infarcted tissue can become superinfected — usually with Staphylococcus aureus or "
            "Streptococcus — but that presents with fever and left upper quadrant pain over days, not "
            "with abrupt haemorrhagic shock.",
        "Overwhelming post-splenectomy infection":
            "She still has her spleen, which is the point of non-operative management. Overwhelming "
            "post-splenectomy infection also occurs over months to years, usually within 2 years of a "
            "splenectomy.",
        "Portal vein thrombosis from the post-traumatic platelet surge":
            "Splenic and portal vein thrombosis do occur after splenectomy, favoured by the platelet "
            "surge and low stump flow — but her platelet count is normal and she has not had surgery.",
        "Reactive thrombocytosis causing splenic infarction":
            "Reactive thrombocytosis follows splenectomy, and aspirin is started if the platelet count "
            "exceeds 1 million. Hers is entirely normal.",
        "Splenosis seeding the peritoneum with splenic tissue":
            "Splenosis is autotransplanted splenic tissue seeded after rupture and spillage. It has no "
            "reliable function, is usually left alone, and does not cause acute haemorrhage.",
    },
    "An expanding subcapsular hematoma that has ruptured",
    "DELAYED RUPTURE — and the timing is the examinable detail. An initially contained subcapsular "
    "haematoma expands and bursts, classically on DAY 5–6 of non-operative management.\n\n"
    "This is precisely why non-operative management means inpatient observation rather than "
    "reassurance: admission to a monitored bed, bed rest, serial haemoglobin and haematocrit, serial "
    "abdominal examination, and an active type and cross. After successful non-operative management "
    "the lecturer's rule is to watch 2–4 days before discharge.\n\n"
    "She has now failed rung 1 and is haemodynamically unstable, so she goes straight to rung 3 — "
    "laparotomy and splenectomy.\n\n"
    "The related late complication to keep beside it is the SPLENIC PSEUDOANEURYSM: a contained "
    "arterial disruption within the injured parenchyma. It may be absent on the initial scan and "
    "appear later, and it can rupture after the patient looks well — which is why follow-up imaging is "
    "obtained in higher-grade injuries and why finding one is an indication for embolization rather "
    "than observation.\n\n"
    "The other post-splenectomy complications worth carrying: postoperative haemorrhage from the "
    "splenic pedicle or short gastrics; subphrenic abscess, characteristically with a left pleural "
    "effusion; reactive thrombocytosis, with aspirin started above 1 million; injury to the tail of "
    "the pancreas at the hilum causing a leak; and gastric wall necrosis from careless division of the "
    "short gastric vessels.",
    "A bruise trapped under the spleen's capsule had been quietly growing all week. On day six it "
    "burst, and all that blood went into her abdomen at once — which is exactly why this injury is "
    "watched in hospital rather than sent home.",
)

q(
    "A 20-year-old college rugby player has a 10-day history of sore throat, fever and fatigue. He "
    "collapses during a tackle drill and arrives with left upper quadrant pain, left shoulder pain, "
    "and a blood pressure of 88/52 mm Hg. Which underlying condition most likely predisposed him to "
    "this injury?",
    {
        "Hereditary spherocytosis":
            "Chronic splenic enlargement in spherocytosis does raise rupture risk, which is part of why "
            "splenectomy is offered — but it is a lifelong hemolytic disease, not something that "
            "develops over ten days with a sore throat.",
        "Infectious mononucleosis": "",
        "Immune thrombocytopenia":
            "This causes bleeding from a low platelet count, but splenomegaly is RARE in immune "
            "thrombocytopenia — which is one of its distinguishing features.",
        "Iron deficiency anemia":
            "This causes no splenomegaly and no predisposition to splenic rupture. It would not explain "
            "a 10-day febrile illness either.",
        "Sickle cell trait":
            "Sickle cell trait is largely asymptomatic. In sickle cell DISEASE the adult spleen is "
            "small and fibrotic from repeated infarction — the opposite problem.",
    },
    "Infectious mononucleosis",
    "Spontaneous or pathologic rupture is one of the four mechanisms of splenic injury: a spleen "
    "enlarged by disease ruptures under trivial or no force. Infectious mononucleosis is the classic "
    "setting, which is precisely why contact sports are restricted during and after the illness — "
    "typically for at least 3 to 4 weeks, and longer for collision sports.\n\n"
    "The four mechanisms, all of which end the same way — the capsule tears or the parenchyma splits, "
    "and a low-pressure, high-flow organ bleeds into the peritoneum:\n"
    "1. BLUNT TRAUMA — the leading cause overall. Motor vehicle collision, fall, handlebar or contact-"
    "sport blow to the left flank. Left lower rib fractures are the warning sign.\n"
    "2. PENETRATING TRAUMA — less common, but far more likely to involve the hilum and the adjacent "
    "tail of pancreas.\n"
    "3. IATROGENIC — usually retractor injury during upper abdominal surgery. The operating room "
    "accounts for about 20% of all splenectomies.\n"
    "4. SPONTANEOUS / PATHOLOGIC — mononucleosis, and also malaria, typhoid, leukemia and infiltrative "
    "disease.\n\n"
    "The spleen is a highly vascular organ taking roughly 5% of cardiac output, wrapped in a thin "
    "capsule and suspended behind ribs 9–11. It is the most commonly injured solid organ in blunt "
    "abdominal trauma.\n\n"
    "One other spontaneous catastrophe worth naming: splenic ARTERY ANEURYSM, which carries a higher "
    "risk in women and classically ruptures during childbirth — the patient crashes and is bleeding "
    "from something that is not the uterus.",
    "The virus that causes mono swells the spleen until it is a thin-walled bag of blood sitting under "
    "the lower ribs. A tackle that any other player would shrug off tears it open — which is why mono "
    "means no contact sport.",
)

q(
    "A 46-year-old woman undergoes total splenectomy for a grade V injury. On postoperative day 10 "
    "she is recovering well.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 10.8 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 33% (N=36%–46%)\n"
    "Leukocyte count 13,200/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 1,240,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "She is afebrile with a soft abdomen. Which of the following is the most appropriate management "
    "of the platelet count?",
    {
        "Aspirin": "",
        "Hydroxyurea to reduce the platelet count":
            "Cytoreduction is used for essential thrombocythemia, a clonal myeloproliferative neoplasm. "
            "This is a reactive, self-limited rise after removal of the organ that normally sequesters "
            "platelets.",
        "Immediate platelet apheresis":
            "Plateletpheresis is reserved for acute symptomatic thrombosis or bleeding at extreme "
            "counts in a clonal disorder. She is asymptomatic and this is an expected postoperative "
            "response.",
        "No intervention, as the count will normalize":
            "Reactive thrombocytosis after splenectomy is indeed expected and self-limited — but the "
            "lecturer gives an explicit threshold above which you act, and she has crossed it.",
        "Therapeutic anticoagulation with a direct oral anticoagulant":
            "Full anticoagulation would be the answer if she had a demonstrated splenic or portal vein "
            "thrombosis. Prophylaxis at this count is antiplatelet, not anticoagulant.",
    },
    "Aspirin",
    "Reactive thrombocytosis is expected after splenectomy — the organ that normally sequesters about a "
    "third of the platelet mass is gone. The explicit threshold from the lecture is simple: **if the "
    "platelet count exceeds 1 million, start aspirin.**\n\n"
    "The concern is thrombosis, and specifically splenic and portal vein thrombosis, which is favoured "
    "by two things at once: the post-splenectomy platelet surge, and low flow in the ligated splenic "
    "vein stump. Portal vein thrombosis after splenectomy presents with abdominal pain, fever and "
    "sometimes bowel ischemia, and is easy to dismiss as ordinary postoperative discomfort.\n\n"
    "The full post-splenectomy complication list is worth running through as a set:\n"
    "• Postoperative haemorrhage — inadequate haemostasis of the splenic pedicle or the short gastric "
    "vessels\n"
    "• Subphrenic abscess — characteristically accompanied by a left pleural effusion, because the "
    "diaphragm sits directly above the space the spleen vacated\n"
    "• Thrombocytosis and venous thrombosis — above\n"
    "• Pancreatic leak or fistula — the tail of the pancreas lies at the hilum, so blind clamping "
    "injures it. Suspect it when drain output stays high and drain amylase is raised\n"
    "• Gastric wall necrosis — from careless division of the short gastric vessels in the "
    "gastrosplenic ligament\n"
    "• Colonic injury — the splenic flexure lies immediately below\n"
    "• Overwhelming post-splenectomy infection — the one that kills late",
    "Her spleen used to hold a large share of her platelets. With it gone, the count has rocketed and "
    "her blood is now prone to clotting, so low-dose aspirin is started until it settles.",
)

q(
    "A 52-year-old man underwent emergency total splenectomy for a shattered spleen after a fall from "
    "a ladder. A closed suction drain was left in the left upper quadrant. On postoperative day 4 he "
    "has a low-grade fever and left upper quadrant discomfort, and the drain continues to produce 350 "
    "mL of cloudy fluid daily.\n\n"
    "Laboratory studies show:\n"
    "Leukocyte count 14,800/mm3 (N=4,500–11,000/mm3)\n"
    "Serum amylase 96 U/L (N=25–125 U/L)\n"
    "Drain fluid amylase 8,400 U/L (N=25–125 U/L)\n\n"
    "Injury to which structure best explains these findings?",
    {
        "The left hemidiaphragm":
            "Diaphragmatic injury gives a left pleural effusion and referred left shoulder pain, and it "
            "is also the setting for a subphrenic abscess — but it does not produce amylase-rich drain "
            "output.",
        "The short gastric vessels":
            "Careless division of these, which run in the gastrosplenic ligament, devascularizes the "
            "greater curve and causes gastric wall necrosis. That presents as peritonitis and sepsis, "
            "not as a high-amylase fistula.",
        "The splenic flexure of the colon":
            "The splenic flexure lies immediately below the spleen and can be injured. A colonic leak "
            "gives feculent drainage and peritonitis, with no reason for the amylase to be raised.",
        "The splenic vein":
            "Injury here causes haemorrhage at operation, and its later thrombosis is favoured by the "
            "post-splenectomy platelet surge. Neither produces an amylase-rich collection.",
        "The tail of the pancreas": "",
    },
    "The tail of the pancreas",
    "The tail of the pancreas lies MEDIAL to the spleen and reaches the splenic hilum, which is why "
    "blind clamping or hurried dissection at the hilum injures it. The result is a pancreatic leak or "
    "fistula, and the way you find it is exactly as described here: drain output that stays high, with "
    "a raised DRAIN amylase. The serum amylase can be entirely normal — the enzyme is going into the "
    "drain, not into the blood.\n\n"
    "The anatomy that dictates the operation, and the complications that follow from it:\n"
    "• The splenic ARTERY runs along the SUPERIOR border of the pancreas from the celiac trunk to the "
    "hilum; the splenic VEIN runs along the INFERIOR border, behind the pancreas, joining the superior "
    "mesenteric vein to form the portal vein. The vein's course is why pancreatitis causes splenic "
    "vein thrombosis, and why hilar dissection risks the pancreatic tail.\n"
    "• The GASTROSPLENIC LIGAMENT carries the short gastric vessels — divide them carelessly and the "
    "greater curve of the stomach loses its blood supply.\n"
    "• The spleen is a SEGMENTAL organ, with relatively avascular planes between arterial segments. "
    "That is what makes partial splenectomy and splenorrhaphy anatomically possible rather than "
    "wishful.\n"
    "• ACCESSORY SPLEENS are present in about 10–20% of people, most often at the hilum. They matter "
    "twice: they are why an immune thrombocytopenia splenectomy relapses, and why a 'completed' "
    "splenectomy can leave residual splenic function.\n\n"
    "Management of a low-output pancreatic fistula is usually conservative — keep the drain in, "
    "nutritional support, and it closes. Persistently high output may need endoscopic stenting.",
    "The tail of the pancreas tucks right up against the spleen, so it is easy to nick while taking "
    "the spleen out. The digestive enzyme pouring into his drain — while his blood level is normal — "
    "is the proof.",
    exim="fig_splenic_artery",
    excap="The splenic artery running along the superior border of the pancreas to the hilum — and the "
          "pancreatic tail reaching the spleen, the structure injured here.",
)

# §56 — post-traumatic edema (LO 34)

q(
    "A 38-year-old man on no medications strikes his left thigh against a car door. Within minutes a "
    "firm, tender, discolored swelling appears over the lateral thigh. Over the next 4 hours it "
    "enlarges noticeably and becomes fluctuant at its center; the surrounding compartment remains "
    "soft, and passive knee flexion does not provoke disproportionate pain. Which of the following "
    "best describes the mechanism and the feature that should concern you most?",
    {
        "Blood dissecting into soft tissue; the concern is its expanding size": "",
        "Inflammatory capillary leak; the concern is the fluctuance":
            "Inflammatory leak produces a local, warm, tender, PITTING swelling that peaks at 24–72 "
            "hours — it does not appear within minutes, and a protein-rich exudate spread through "
            "tissue does not become fluctuant.",
        "Lymphatic disruption; the concern is that it will not resolve":
            "Lymphatic disruption develops over weeks to months, does not resolve with elevation, "
            "becomes non-pitting and fibrotic, and is often permanent. Nothing about it appears within "
            "minutes.",
        "Rising intracompartmental pressure; the concern is impending muscle ischemia":
            "This is compartment syndrome and it is the diagnosis you must always exclude — but the "
            "stem explicitly gives a soft compartment and no pain on passive stretch, which are its two "
            "earliest reliable signs.",
        "Venous obstruction; the concern is pulmonary embolism":
            "A deep vein thrombosis announces itself DAYS later, characteristically when swelling that "
            "was improving begins to worsen again, and gives a unilateral, whole-limb, pitting swelling "
            "with calf tenderness.",
    },
    "Blood dissecting into soft tissue; the concern is its expanding size",
    "A hematoma is the second of the six post-traumatic mechanisms, and the timing names it: IMMEDIATE, "
    "with expansion possible over hours. The character is focal, firm, discolored and often fluctuant "
    "— quite different from the diffuse pitting swelling of an inflammatory exudate.\n\n"
    "The pathophysiology has two phases. First a mass effect, as blood dissects into the soft tissue "
    "planes. Then an osmotic load, as red cells and protein break down and draw water in — which is "
    "why a hematoma keeps a limb swollen long after the bleeding itself has stopped.\n\n"
    "Expanding size is the alarm feature, because it means bleeding is ongoing. In a patient on an "
    "anticoagulant that is a reason to check coagulation and consider reversal; in a patient with no "
    "such history it raises the question of an unrecognized bleeding disorder or a vascular injury.\n\n"
    "The six mechanisms in the order they appear, all instances of one of the four Starling variables:\n"
    "1. Inflammatory / increased permeability — minutes to hours, peaking 24–72 h. Local, warm, tender, "
    "pitting. The expected swelling.\n"
    "2. Hematoma — immediate. Focal, firm, discolored, fluctuant.\n"
    "3. Venous obstruction (deep vein thrombosis) — days later. Unilateral, whole-limb, pitting.\n"
    "4. Lymphatic disruption — weeks to months. Becomes non-pitting and fibrotic.\n"
    "5. Hypoalbuminemia / resuscitation dilution — days. Generalized and dependent.\n"
    "6. Compartment syndrome — hours. Tense and wood-hard; the emergency.\n\n"
    "Read the clock, then read the feel.",
    "The blow tore small vessels and blood is pooling inside the thigh. Some swelling is expected — "
    "what matters is that it is still getting bigger, which means something is still bleeding.",
)

# §57 — lymphatic dissemination (LO 60)

q(
    "A sentinel lymph node is removed during breast cancer surgery and sent for intraoperative "
    "evaluation. Which compartment of the node should the pathologist examine first for metastatic "
    "deposits?",
    {
        "The germinal centers of the superficial cortical follicles":
            "These are the B-cell reactive compartment, where somatic hypermutation and affinity "
            "maturation occur. They are where follicular lymphoma arises, not where arriving carcinoma "
            "cells land.",
        "The medullary cords":
            "These contain plasma cells and macrophages and sit near the hilum, where lymph collects "
            "before leaving by the efferent lymphatic. Tumor reaches them only after traversing the "
            "node.",
        "The paracortex":
            "This is the T-cell zone, which expands in viral infection and is where peripheral T-cell "
            "lymphomas arise. It is deep to where afferent lymph first arrives.",
        "The perinodal fat and capsule":
            "Extranodal extension through the capsule is an important prognostic finding — it is what "
            "makes a node feel fixed — but it is a LATE event, after the node has been colonized.",
        "The subcapsular sinus": "",
    },
    "The subcapsular sinus",
    "Afferent lymphatics pierce the capsule on the convex surface of the node and empty into the "
    "SUBCAPSULAR (marginal) SINUS. That is where arriving tumor cells first land, where metastatic "
    "deposits are first seen, and therefore the first compartment the pathologist examines in a "
    "sentinel node.\n\n"
    "Contrast it with the node's reactive compartments, which serve immune function rather than "
    "receiving traffic: follicles in the superficial cortex for B cells, paracortex for T cells, "
    "medulla for plasma cells and outflow.\n\n"
    "The full pathway of lymphatic dissemination, step by step:\n"
    "1. LOCAL INVASION — carcinoma cells lose E-cadherin-mediated adhesion, degrade the basement "
    "membrane with matrix metalloproteinases, and enter the stroma.\n"
    "2. LYMPHOVASCULAR INVASION — cells enter a lymphatic capillary.\n"
    "3. TRANSPORT along afferent lymphatics.\n"
    "4. ARRIVAL in the subcapsular sinus.\n"
    "5. PROGRESSIVE EFFACEMENT of the node, then exit by the efferent lymphatic at the hilum to the "
    "next echelon.\n"
    "6. ENTRY INTO THE SYSTEMIC CIRCULATION — lymph ultimately reaches the thoracic duct, which empties "
    "at the junction of the left subclavian and left internal jugular veins. Lymphatic spread becomes "
    "haematogenous spread at that point; the two routes are sequential, not alternative.\n\n"
    "Spread is usually orderly, echelon by echelon — but SKIP METASTASES occur when lymphatics are "
    "obstructed by tumor and flow is diverted around the expected node.",
    "Lymph enters a node from the outside edge, so cancer cells that travelled there get stuck in the "
    "thin space just under the node's skin. That is the first place the pathologist puts under the "
    "microscope.",
)

q(
    "A pathologist examines two malignancies. The first, a carcinoma of the breast, shows tumor within "
    "lymphatic channels and metastases confined to axillary nodes. The second, a high-grade "
    "leiomyosarcoma of the thigh, shows pulmonary metastases with uninvolved inguinal nodes. Which "
    "structural feature of lymphatic capillaries best explains why carcinomas favor the lymphatic "
    "route?",
    {
        "Lymphatic capillaries are lined by fenestrated endothelium that filters plasma proteins":
            "Fenestrated endothelium is a feature of specialized blood capillaries in the glomerulus, "
            "gut and endocrine organs. Lymphatic capillaries are defined by the absence of a basement "
            "membrane and by their overlapping junctions.",
        "Lymphatic capillaries carry a higher hydrostatic pressure that draws tumor cells in":
            "Pressure within lymphatic vessels is LOWER than in blood vessels and flow is slower. Low "
            "pressure is part of why they are easy to enter, not a driving force.",
        "Lymphatic capillaries lack a basement membrane and have loose, overlapping junctions": "",
        "Lymphatic capillaries lack valves, allowing tumor cells to travel in either direction":
            "Lymphatic vessels DO have valves and behave much like veins. Retrograde flow occurs only "
            "when obstruction forces it, which is the mechanism of skip metastases.",
        "Lymphatic capillaries are surrounded by pericytes that secrete matrix metalloproteinases":
            "Matrix metalloproteinases are secreted by the TUMOR to degrade the basement membrane "
            "during local invasion. They are part of step one of the pathway, not a property of the "
            "vessel.",
    },
    "Lymphatic capillaries lack a basement membrane and have loose, overlapping junctions",
    "That single structural fact is why carcinoma prefers this route: a lymphatic capillary is simply "
    "easier to penetrate than a blood capillary, which has a continuous basement membrane and tight "
    "endothelial junctions. Tumors also actively drive lymphangiogenesis through VEGF-C and VEGF-D, "
    "building themselves more of the easier road.\n\n"
    "The governing rule that opens this whole objective: **carcinomas spread preferentially by "
    "lymphatics; sarcomas spread preferentially by blood.** The two cases in this stem are the worked "
    "illustration — an epithelial malignancy in the nodes, a mesenchymal one in the lungs with the "
    "nodes clean.\n\n"
    "The clinical consequences of lymphatic dissemination are three:\n"
    "• It sets the N stage, and therefore the prognosis and the adjuvant therapy decision.\n"
    "• Nodal obstruction — or the dissection performed to stage it — produces secondary lymphedema, "
    "the commonest cause in the developed world.\n"
    "• Involvement or injury of the thoracic duct produces a chylous effusion or chylothorax: milky, "
    "triglyceride-rich fluid.\n\n"
    "And read the node at the bedside: metastatic nodes are hard, painless, FIXED, often matted and "
    "progressively enlarging. Fixation means tumor has breached the capsule — extranodal extension, "
    "which independently worsens prognosis.",
    "Blood capillaries are sealed tubes with a firm outer wall. Lymph capillaries are more like "
    "overlapping roof tiles with no wall behind them — far easier for a wandering cancer cell to slip "
    "between.",
)

q(
    "A 52-year-old woman has a 2.1-cm invasive ductal carcinoma in the MEDIAL upper quadrant of the "
    "left breast. Sentinel node biopsy of the left axilla returns two nodes, both free of tumor. Which "
    "of the following is the most important limitation of this result?",
    {
        "A medial tumor may drain to internal mammary nodes that were not sampled": "",
        "Carcinomas metastasize preferentially by the haematogenous route":
            "The opposite is true — carcinomas spread preferentially by lymphatics, and sarcomas by "
            "blood. That rule is what makes nodal sampling worth doing in the first place.",
        "Sentinel node biopsy cannot distinguish reactive from metastatic nodes":
            "Distinguishing the two is exactly what histologic examination does, and the pathologist "
            "examines the subcapsular sinus first for that purpose.",
        "The absence of nodal disease means the tumor cannot have spread haematogenously":
            "Nodal status correlates with, but does not exclude, distant spread. It is also not a "
            "limitation specific to the sentinel technique or to a medial tumor.",
        "Two nodes is an inadequate sample and a full dissection is always required":
            "The entire logic of the technique is that if the sentinel node is free of tumor, the nodes "
            "downstream are almost certainly free too — which is what allows a full dissection, and its "
            "lymphedema risk, to be avoided.",
    },
    "A medial tumor may drain to internal mammary nodes that were not sampled",
    "About 75% of breast lymph drains to the AXILLA — levels I to III, defined by their relation to "
    "pectoralis minor — and that is where lateral and upper quadrant tumors go. MEDIAL quadrants drain "
    "to the INTERNAL MAMMARY chain, which lies beside the sternum and is not sampled by a standard "
    "axillary sentinel procedure.\n\n"
    "So a medial tumor with negative axillary nodes may still harbour internal mammary disease. This "
    "is the examinable point about the breast on the drainage map, and it is a real limitation rather "
    "than a technical failure.\n\n"
    "The rest of the map worth memorizing:\n"
    "• Stomach, pancreas and other abdominal viscera — celiac and para-aortic → thoracic duct → LEFT "
    "supraclavicular node. Virchow's node; the palpable finding is Troisier sign\n"
    "• Testis and ovary — para-aortic/retroperitoneal, NOT inguinal, because both organs descended "
    "from the posterior abdominal wall. The scrotal SKIN drains to superficial inguinal nodes\n"
    "• Anal canal — above the dentate line to internal iliac and inferior mesenteric; below it to "
    "superficial inguinal\n"
    "• Lung — hilar → mediastinal → supraclavicular; mediastinal status is the pivot of resectability\n"
    "• Prostate — obturator and internal iliac, preceding the classic osteoblastic bone metastases\n"
    "• Head and neck mucosa — cervical chains, levels I–VI\n"
    "• Lower limb, vulva and penile skin — superficial inguinal\n\n"
    "The other acknowledged caveat of sentinel biopsy is the skip metastasis, when tumor obstructs "
    "lymphatics and diverts flow around the expected node.",
    "Most of the breast drains to the armpit, but the inner part drains inward toward the breastbone "
    "instead. A clean armpit therefore does not fully clear a tumor sitting on the inner side.",
)

# ═════════════════════════════════════════════════════════════════════════════
# GROUP 3 — GERIATRICS
# ═════════════════════════════════════════════════════════════════════════════

q(
    "An 82-year-old man undergoes bone marrow biopsy during evaluation of an unexplained macrocytic "
    "anemia. The pathology report describes the marrow as 25% cellular with a myeloid-to-erythroid "
    "ratio of 3:1 and no increase in blasts. Which of the following is the correct interpretation of "
    "the cellularity?",
    {
        "Hypercellular, indicating a myeloproliferative process":
            "A hypercellular marrow in an octogenarian would be well above 20%. A raised "
            "myeloid-to-erythroid ratio and increased cellularity would point that way; his ratio is "
            "normal.",
        "Hypocellular, indicating aplastic anemia":
            "Aplastic anemia gives a markedly ACELLULAR marrow with fatty replacement and pancytopenia "
            "including reticulocytopenia. A cellularity of 25% at age 82 is not hypocellular at all.",
        "Hypocellular, indicating marrow suppression from a recent illness":
            "This assumes the same misreading of the number. Cellularity has to be judged against age "
            "before any conclusion about suppression can be drawn.",
        "Normal for his age": "",
        "Uninterpretable without a comparison to a previous biopsy":
            "A single biopsy is entirely interpretable, because the expected value can be calculated "
            "from age. That is why every marrow report states cellularity against age.",
    },
    "Normal for his age",
    "Normal marrow cellularity = **(100 − the patient's age) percent.** An 82-year-old should have "
    "roughly 18–20% cells and 80% fat, so 25% is normal-to-slightly-high for him. A young adult is "
    "around 70–80% cellular.\n\n"
    "This is why 'hypocellular for age' is a completely different judgement in a child than in an "
    "octogenarian, and why a marrow report always states cellularity against age rather than as a bare "
    "number.\n\n"
    "Alongside it, the myeloid-to-erythroid ratio is normally about 3:1 — most of what is in a marrow "
    "is granulocyte precursors, because their lifespan is short. A FALL in that ratio means erythroid "
    "hyperplasia (as in polycythemia vera or a brisk haemolytic response); a RISE means the opposite. "
    "His 3:1 is normal.\n\n"
    "What his report does NOT exclude is the diagnosis the clinical picture is pointing at. An "
    "unexplained macrocytic cytopenia in an older adult is MYELODYSPLASTIC SYNDROME until proven "
    "otherwise — median age at diagnosis 77 — and myelodysplasia characteristically gives a normal or "
    "hypercellular marrow with dysplastic changes, not a hypocellular one. The answer to his anemia "
    "lies in the morphology and cytogenetics, not the cell count.",
    "Marrow gets fattier with age, and there is a simple sum for it: subtract the person's age from "
    "100. At 82, about a fifth of his marrow should be cells — so 25% is right where it should be.",
    exim="fig_marrow_cellularity",
    excap="Marrow cellularity for comparison — hypercellular, normocellular and hypocellular. What "
          "counts as normal depends entirely on the patient's age.",
)

q(
    "A 79-year-old man is seen for a routine visit. He feels well. His hemoglobin was 14.8 g/dL three "
    "years ago.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 12.6 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 38% (N=41%–53%)\n"
    "Mean corpuscular volume 76 µm3 (N=80–100 µm3)\n"
    "Ferritin 11 ng/mL (N=15–200 ng/mL)\n"
    "Serum iron 28 µg/dL (N=50–170 µg/dL)\n"
    "Total iron-binding capacity 448 µg/dL (N=250–400 µg/dL)\n\n"
    "Which of the following is the most appropriate next step?",
    {
        "Attribute the anemia to age and repeat the count in 1 year":
            "'Anemia of the elderly' is not a diagnosis. The World Health Organization thresholds — "
            "under 13 g/dL in men and under 12 g/dL in women — apply regardless of age, and a fall of "
            "more than 10% from a patient's own baseline warrants investigation even if the absolute "
            "value still looks normal.",
        "Begin an erythropoiesis-stimulating agent":
            "These are started only when hemoglobin is below 10 g/dL, and only for anemia of chronic "
            "kidney disease or of non-curative chemotherapy. Neither applies, and his marrow has no "
            "iron to work with in any case.",
        "Bidirectional endoscopy": "",
        "Measure serum erythropoietin and a reticulocyte index":
            "These would help characterize an unexplained normocytic anemia. His iron studies have "
            "already given the mechanism; the question is now where the iron is going.",
        "Start oral ferrous sulfate and recheck in 3 months":
            "Iron replacement is part of the management, but giving it without investigating is the "
            "error — it corrects the number while leaving a potentially curable lesion undiagnosed for "
            "three months.",
    },
    "Bidirectional endoscopy",
    "Two age-related traps are being tested at once.\n\n"
    "First: **anemia is never 'just age.'** The World Health Organization thresholds are hemoglobin "
    "under 13 g/dL in men and under 12 g/dL in women, regardless of age, and a fall of more than 10% "
    "from a patient's OWN baseline should be investigated even when the absolute number still reads as "
    "normal. His hemoglobin has fallen 2.2 g/dL from 14.8 — a 15% drop — and he is below the threshold "
    "as well.\n\n"
    "Second: **iron deficiency in an older adult is a gastrointestinal lesion until proven otherwise.** "
    "In an adult man or a postmenopausal woman, iron deficiency should be treated as a gastrointestinal "
    "bleed until proven otherwise, and age makes this MORE urgent rather than less, because the "
    "prevalence of colorectal carcinoma rises with it.\n\n"
    "The iron studies form one coherent row and confirm true deficiency rather than anemia of chronic "
    "disease: low iron, low ferritin, and a HIGH total iron-binding capacity. Anemia of chronic disease "
    "gives low iron with a LOW binding capacity and a normal or raised ferritin.\n\n"
    "A normal-looking result in an older adult deserves the same scepticism. Age-banded prevalence is "
    "a diagnostic prior, not a permission to stop thinking: an unexplained macrocytic cytopenia in an "
    "older adult is myelodysplasia until proven otherwise, and a small monoclonal spike is usually "
    "monoclonal gammopathy of undetermined significance — present in 3% over 50 and 5% over 70 — but "
    "it still converts at about 1% per year.",
    "His blood count has quietly dropped and his iron stores are empty. In a man his age that means "
    "blood is leaking somewhere in the gut — often from something curable if you find it now. Iron "
    "tablets alone would hide the clue.",
)

q(
    "A 58-year-old man has taken antiretroviral therapy for 12 years with excellent adherence. His "
    "CD4 count is 720/µL and his viral load has been undetectable for a decade. He has newly "
    "diagnosed hypertension, a low-density lipoprotein cholesterol of 158 mg/dL, osteopenia on "
    "dual-energy radiographic absorptiometry, and mild word-finding difficulty. He asks why this is "
    "happening when his HIV is controlled. Which of the following best explains his findings?",
    {
        "Cumulative antiretroviral toxicity is the sole driver":
            "Drug toxicity genuinely contributes, particularly to bone (tenofovir) and renal function, "
            "and it influences regimen selection. But it does not account for the whole pattern, and "
            "the unifying mechanism is inflammatory.",
        "Immune reconstitution inflammatory syndrome":
            "This is a STARTING phenomenon, occurring within weeks to months of beginning antiretroviral "
            "therapy in someone with a low CD4 count. It does not appear twelve years into stable "
            "treatment.",
        "Ongoing low-level viral replication below the limit of detection":
            "His viral load has been undetectable for a decade, and the point of the concept being "
            "tested is precisely that these changes occur DESPITE full virologic suppression.",
        "Persistent immune activation and chronic inflammation": "",
        "Progressive immune failure with a falling CD4 count":
            "A CD4 count of 720/µL is normal. This is not immune failure, which is exactly what makes "
            "the pattern puzzling to the patient.",
    },
    "Persistent immune activation and chronic inflammation",
    "The mechanism is 'inflammaging' — age-associated immune activation and chronic inflammation that "
    "persists even when the virus is fully suppressed, affecting both innate and adaptive immunity. It "
    "is the single mechanism that ties his three apparently unrelated new problems together.\n\n"
    "People living with HIV now live close to normal lifespans, so the management plan has to extend "
    "past viral suppression into decades of cardiometabolic, bone, cognitive and cancer risk. "
    "'Undetectable equals untransmittable' settles transmission; it does not settle long-term "
    "comorbidity. Virologic suppression is necessary but not sufficient.\n\n"
    "What that obliges you to monitor:\n"
    "• CARDIOVASCULAR — accelerated atherosclerosis, with myocardial infarction and stroke at younger "
    "ages. Lipids and cardiovascular risk; treat cholesterol aggressively and control glucose. "
    "Conventional risk-factor modification matters MORE here, not less\n"
    "• BONE — osteopenia and osteoporosis, partly inflammatory and partly drug-related. Bone density "
    "and vitamin D\n"
    "• RENAL — chronic kidney disease. Creatinine and estimated glomerular filtration rate, which also "
    "drives antiretroviral dose adjustment\n"
    "• NEUROCOGNITIVE — word-finding and short-term memory difficulty. Cognitive screening at routine "
    "visits\n"
    "• MALIGNANCY — AIDS-defining (non-Hodgkin lymphoma, cervical cancer, Kaposi sarcoma) and "
    "non-AIDS-defining (lung, liver, anal, head and neck, Hodgkin lymphoma). Age-appropriate screening "
    "plus gynecologic or rectal cytology every 6–12 months as indicated\n"
    "• ROUTINE — complete blood count, metabolic panel, CD4 and viral load every 3–6 months",
    "His immune system has been running at a low simmer for years even though the virus is silenced, "
    "and that constant inflammation ages his arteries, bones and brain ahead of schedule. Controlling "
    "the virus was necessary — it was just never the whole job.",
)

q(
    "An 81-year-old woman lives alone. She bathes, dresses, toilets, transfers and feeds herself "
    "without help. Over the past year her daughter has taken over her bank accounts and now fills her "
    "weekly pill organizer, because her mother twice paid the same bill and once took a double dose "
    "of her anticoagulant. She stopped driving last year after getting lost. Which of the following "
    "best characterizes this functional pattern, and what does it most suggest?",
    {
        "A basic activity of daily living deficit, suggesting advanced dementia":
            "Her basic self-care is entirely intact — bathing, dressing, toileting, transferring, "
            "continence and feeding are the Katz activities of daily living. Those fail LATE.",
        "An instrumental activity of daily living deficit, suggesting early dementia": "",
        "Frailty, best assessed with the Fried Frailty Scale or the Clinical Frailty Scale":
            "Frailty is decreased physiologic reserve — weight loss, exhaustion, slowness — and is a "
            "real domain with its own scales. Nothing in this history describes it.",
        "Normal aging, requiring no further assessment":
            "Losing the ability to manage finances and medications is not normal aging, and the "
            "medication errors described have already caused a real anticoagulant overdose.",
        "A mobility limitation, best assessed with the Timed Up and Go test":
            "The Timed Up and Go and the 4-Stage Balance Test assess falls risk and gait. She has no "
            "reported gait change or assistive device.",
    },
    "An instrumental activity of daily living deficit, suggesting early dementia",
    "**Instrumental activities fail FIRST.** A patient who can still bathe and dress but has stopped "
    "managing her own finances and medications has an instrumental deficit with basic activities "
    "intact — the classic functional signature of mild cognitive impairment or early dementia.\n\n"
    "• ACTIVITIES OF DAILY LIVING (Katz) — basic self-care: bathing, dressing, toileting, transferring, "
    "continence, feeding.\n"
    "• INSTRUMENTAL ACTIVITIES (Lawton-Brody) — the tasks of running a life: finances, medication "
    "management, shopping, cooking, housekeeping, laundry, transport, telephone use.\n\n"
    "Why function rather than the problem list: function correlates with longevity, and the numbers "
    "make the point unarguable. Seventy-five-year-olds without limitations live about 5 years longer "
    "than those with an activity-of-daily-living limitation. **The life expectancy of an "
    "ADL-disabled 75-year-old is the same as that of an independent 85-year-old** — a disability is "
    "worth roughly ten years of age, and much more of the remaining time is spent disabled.\n\n"
    "Her history runs the 4Ms (What Matters, Medication, Mentation, Mobility) and lands squarely in "
    "haematology. Read the chain forward: cognitive impairment → medication mismanagement → "
    "anticoagulant overdose → a large haematoma from a low-energy fall. **Cognitive impairment is an "
    "anticoagulation safety problem** — the capacity to self-administer is part of choosing and "
    "continuing an anticoagulant, not a separate social issue.\n\n"
    "The escalation logic for the assessment: Mini-Cog → positive → MoCA, SLUMS or MMSE → positive → "
    "formal neuropsychiatric testing. Katz and Lawton-Brody deficits → occupational therapy. Falls and "
    "gait findings → physical therapy.",
    "She can still look after her own body, but she can no longer run her own life — the bills, the "
    "pills, the driving. That order of losing things, complicated tasks first, is the early signature "
    "of dementia.",
)

q(
    "An 84-year-old woman with moderate dementia is brought in by her son. She has become agitated "
    "and calls out in the late afternoon and evening, and is sleeping poorly. There is no fever, no "
    "dysuria, and no change in her medications. Her son asks for \"something to calm her down.\" "
    "Which of the following is the most appropriate response?",
    {
        "Non-pharmacologic management of the behavior": "",
        "Diphenhydramine at bedtime":
            "An anticholinergic — one of the four high-risk classes — and it appears on the Beers "
            "Criteria for exactly this reason. It worsens confusion and falls risk in the population "
            "least able to tolerate either.",
        "Doxepin at bedtime":
            "Doxepin and trazodone are the reluctant 'maybe, possibly, if you have to' options for "
            "INSOMNIA, and only after cognitive behavioural therapy and sleep restriction. The "
            "presenting problem here is the behavior, not the insomnia alone.",
        "Lorazepam as needed for episodes of agitation":
            "A sedative — another of the four high-risk classes — and benzodiazepines are conspicuously "
            "absent even from the lecture's reluctant second-line options for anxiety.",
        "Quetiapine at a low dose":
            "An antipsychotic is the most commonly reached-for agent and is still a sedative in a "
            "high-risk class. Antipsychotics carry a mortality warning in dementia, and the lecture "
            "offers no pharmacologic fallback at all for this indication.",
    },
    "Non-pharmacologic management of the behavior",
    "Three consecutive slides in this lecture open with the same sentence — 'There are no safe "
    "medications for…' — and each names a symptom, denies that a safe drug exists, offers a non-drug "
    "first line, then concedes a reluctant second line. The structure is the teaching point, and so is "
    "the exception:\n\n"
    "• INSOMNIA — first, cognitive behavioural therapy and sleep restriction or compression therapy. "
    "Only 'maybe, possibly, if you have to': doxepin or trazodone.\n"
    "• ANXIETY — first, cognitive behavioural therapy. Only if you have to: a selective serotonin "
    "reuptake inhibitor or a serotonin-norepinephrine reuptake inhibitor. Note what is conspicuously "
    "NOT offered: benzodiazepines.\n"
    "• NEUROCOGNITIVE SYMPTOMS OF DEMENTIA (the 'behaviours') — no safe medication, and here there is "
    "**no drug concession at all**. The stated treatment is love, compassion and creativity: meet the "
    "person where they are, not where you want them to be.\n\n"
    "Of the three, only dementia-related behaviours get no pharmacologic fallback. That is the "
    "discriminator to remember.\n\n"
    "Every tempting distractor sits in one of the four high-risk classes — opioids, anticholinergics, "
    "sedatives, antidepressants — and medications in older adults are linked to falls, delirium, "
    "dementia, disability and death. The tools that exist to catch this: the Beers Criteria "
    "(potentially inappropriate medications in adults 65 and older), the anticholinergic burden scale "
    "(which catches the patient on five individually mild drugs), STOPP (drugs to stop), START (drugs "
    "that should have been started — the under-prescribing half people forget), and the pharmacist.\n\n"
    "And the maxim, with its correction: 'Start low, go slow — BUT get somewhere.' Stopping at a "
    "sub-therapeutic dose because the patient is old is its own harm, which is what START exists to "
    "catch.",
    "There is no safe pill for this kind of agitation in dementia — every option makes falls and "
    "confusion worse. What helps is changing the surroundings and the routine, and meeting her where "
    "she is.",
)
