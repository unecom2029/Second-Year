# Batch 20 — Hematologic Malignancy, part 2 (lymphoid)
# Review sections §40 (s36-all-lymphoma), §41 (s36b-lpd), §42 (s37-plasma-cell)
# Native LOs: 3, 21, 30, 40, 41, 56, 57, 67
#
# NOTE: options are supplied as a dict {option text: wrong-answer explanation}.
# The helper alphabetises them (case-insensitive, matching the validator), applies the
# letter prefixes, computes `correct`, and re-keys wrongExplanations. Hand-alphabetising
# was the single largest source of defects in batches 11-19; this removes it.

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
# §40 — Acute lymphoblastic leukemia and the lymphomas, clinical
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 5-year-old boy is brought to the physician because of 3 weeks of pallor, easy bruising and "
    "leg pain that wakes him at night. He has bilateral cervical and axillary lymphadenopathy, and "
    "the spleen is palpable 4 cm below the left costal margin.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.4 g/dL (N=11.5–15.5 g/dL)\n"
    "Hematocrit 22% (N=35%–45%)\n"
    "Leukocyte count 31,000/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 28,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Bone marrow aspiration shows 82% blasts that are positive for terminal deoxynucleotidyl "
    "transferase, CD19 and CD10, and negative for CD3 and myeloperoxidase.\n\n"
    "In addition to systemic multiagent chemotherapy, which of the following is most important to "
    "include in this patient's treatment plan?",
    {
        "Allogeneic hematopoietic stem cell transplantation in first remission":
            "Transplantation in first remission is reserved for high-risk disease. This child has the "
            "favorable profile — age 2–5 years, precursor-B immunophenotype — and chemotherapy alone "
            "cures over 90% of such children.",
        "All-trans retinoic acid":
            "This would be the answer if the blasts had been myeloid with abnormal promyelocytes and "
            "t(15;17). All-trans retinoic acid releases the maturation block of acute promyelocytic "
            "leukemia; it does nothing in a lymphoblastic disease.",
        "Intrathecal methotrexate": "",
        "Rituximab":
            "This would be the answer if the neoplasm were a mature CD20-positive B-cell lymphoma. "
            "Lymphoblasts are CD19-positive but express little or no CD20, and rituximab is not part "
            "of standard pediatric induction.",
        "Splenic irradiation":
            "This would be the answer if splenomegaly were causing refractory hypersplenic cytopenias "
            "or intractable pain in a disease unresponsive to systemic therapy. Here the spleen is "
            "infiltrated by a chemosensitive leukemia and shrinks with induction.",
    },
    "Intrathecal methotrexate",
    "Acute lymphoblastic leukemia is defined clinically by the fact that it leaves the marrow. "
    "Lymphadenopathy, splenomegaly and central nervous system involvement are the three "
    "extramedullary features that separate it from acute myeloid leukemia at the bedside — and the "
    "meninges are the problem, because systemic chemotherapy penetrates the cerebrospinal fluid "
    "poorly.\n\n"
    "The meninges therefore act as a sanctuary site: blasts survive there through induction and seed "
    "a systemic relapse later. Every standard regimen consequently includes central nervous system "
    "prophylaxis — intrathecal chemotherapy, with or without cranial irradiation — whether or not "
    "there is neurologic disease at diagnosis.\n\n"
    "The immunophenotype here is precursor-B: terminal deoxynucleotidyl transferase marks a "
    "lymphoblast (it is the enzyme that diversifies antigen receptor genes, expressed only by "
    "immature lymphoid cells), CD19 and CD10 are B-lineage, and the myeloperoxidase negativity "
    "excludes a myeloid blast. This is the 85% of childhood cases.",
    "Leukemia cells hide in the fluid around the brain, where drugs given into a vein barely reach. "
    "So doctors inject chemotherapy directly into that fluid. They do it for every child, even when "
    "no brain symptoms exist.",
    exim="fig_lpd_neoplasm_origin_map",
    excap="Each lymphoid neoplasm mapped onto the normal cell it came from — the lymphoblastic "
          "diseases sit at the far left, before the node.",
)

q(
    "Five children are evaluated in a pediatric oncology clinic, each with newly diagnosed acute "
    "lymphoblastic leukemia. Which of the following findings is associated with the most favorable "
    "prognosis?",
    {
        "Age 3 years at the time of diagnosis": "",
        "Central nervous system involvement at diagnosis":
            "This would be the answer if you were asked for an adverse feature. Leukemic meningitis at "
            "presentation is unfavorable and requires intensified central nervous system-directed "
            "therapy.",
        "Persistent measurable residual disease after induction":
            "This would be the answer if you were asked which finding most strongly predicts relapse. "
            "Slow early response and persistent measurable residual disease are among the most powerful "
            "adverse factors, and often trigger intensification or transplantation.",
        "Presenting leukocyte count of 180,000/mm3":
            "This would be the answer if a high tumor burden were favorable. It is not: a high "
            "presenting white count is a classic adverse factor and also predicts tumor lysis syndrome "
            "when treatment begins.",
        "T-cell immunophenotype":
            "This would be the answer if lineage did not matter. T-cell disease accounts for about 15% "
            "of cases and carries a worse prognosis than precursor-B disease, which is the favorable "
            "85%.",
    },
    "Age 3 years at the time of diagnosis",
    "Age 2–5 years is the favorable band — which is the counterintuitive part, because that is also "
    "the peak incidence group. The children who get the disease most often are the children who do "
    "best with it.\n\n"
    "The favorable list: age 2–5 years, precursor-B immunophenotype, favorable cytogenetics, a low "
    "presenting leukocyte count, and rapid clearance of blasts with a good early response to "
    "induction.\n\n"
    "The unfavorable list: infancy or adolescence and adulthood, T-cell disease, BCR::ABL1 or other "
    "adverse cytogenetics, a high presenting leukocyte count, central nervous system involvement, and "
    "a slow early response with persistent measurable residual disease.\n\n"
    "This is also why survival falls from over 90% in children to 50–70% in adolescents and young "
    "adults and about 30% in older adults. It is not only that children tolerate intensive protocols "
    "better; adult disease is genuinely enriched for adverse cytogenetics, BCR::ABL1 among them. Same "
    "disease name, three different diseases.",
    "Being a young child with this leukemia is actually the good version. The cancer's genetics are "
    "usually the friendly kind at that age, and the treatment works far better.",
)

q(
    "A 54-year-old man is diagnosed with precursor-B acute lymphoblastic leukemia. Fluorescence in "
    "situ hybridization on the marrow aspirate demonstrates a BCR::ABL1 fusion arising from t(9;22). "
    "Which of the following additions to his multiagent chemotherapy is most likely to improve his "
    "outcome?",
    {
        "Arsenic trioxide":
            "This would be the answer if the disease were acute promyelocytic leukemia, where arsenic "
            "trioxide is paired with all-trans retinoic acid. It has no role against a BCR::ABL1-driven "
            "lymphoblastic leukemia.",
        "Brentuximab vedotin":
            "This would be the answer if the neoplasm expressed CD30 — classic Hodgkin lymphoma or "
            "anaplastic large cell lymphoma. Lymphoblasts do not.",
        "Dasatinib": "",
        "Hydroxyurea":
            "This would be the answer if the goal were rapid cytoreduction of an extreme leukocytosis "
            "as a temporizing measure. It is not disease-directed therapy and does not address the "
            "fusion protein.",
        "Rituximab":
            "This would be the answer if the blasts expressed CD20 at useful density. Some adult "
            "precursor-B cases do and derive benefit, but the finding that changes management here is "
            "the fusion gene, not CD20.",
    },
    "Dasatinib",
    "A subset of precursor-B acute lymphoblastic leukemia carries BCR::ABL1 — the very same fusion "
    "that defines chronic myeloid leukemia — and therefore the very same drug target. Adding an oral "
    "tyrosine kinase inhibitor such as dasatinib or imatinib to chemotherapy transformed what was "
    "historically the worst-prognosis subgroup.\n\n"
    "Note what this does to the age gradient. BCR::ABL1 is rare in childhood disease and common in "
    "adults, and it is a large part of why adult acute lymphoblastic leukemia does so much worse. "
    "The targeted agent does not erase that gap, but it narrows it substantially.\n\n"
    "The general principle is worth carrying: whenever a leukemia is defined by a constitutively "
    "active kinase, ask whether an inhibitor of that kinase exists. The fusion is not merely a "
    "prognostic label, it is an address.",
    "This leukemia carries the same broken gene as chronic myeloid leukemia, and there is already a "
    "pill that switches that gene's protein off. Adding it to chemotherapy turns the worst version of "
    "the disease into a treatable one.",
)

q(
    "A 16-year-old boy is brought to the emergency department because of 1 week of facial swelling, "
    "a cough, and shortness of breath that is worse when he lies flat. The neck veins are distended. "
    "A chest CT shows a 9-cm anterior mediastinal mass. Biopsy shows sheets of intermediate-sized "
    "cells with fine chromatin and scant cytoplasm, positive for terminal deoxynucleotidyl "
    "transferase, CD3 and CD7, and negative for CD19 and CD20. Which of the following is the most "
    "likely diagnosis?",
    {
        "B-lymphoblastic leukemia":
            "This would be the answer if the blasts were CD19 and CD10 positive and CD3 negative. "
            "Precursor-B disease arises in the marrow and presents with cytopenias, not with a "
            "thymic mass.",
        "Burkitt lymphoma":
            "This would be the answer if the cells were mature B cells — CD10 and CD20 positive, "
            "terminal deoxynucleotidyl transferase negative — with a starry-sky pattern and a jaw or "
            "abdominal mass. Burkitt lymphoma does not express CD3.",
        "Nodular sclerosis classic Hodgkin lymphoma":
            "This would be the answer if the biopsy had shown scattered large binucleate cells in a "
            "polymorphous, eosinophil-rich background divided by collagen bands. The age and the "
            "mediastinal location fit, but sheets of terminal deoxynucleotidyl transferase-positive "
            "blasts do not.",
        "Primary mediastinal large B-cell lymphoma":
            "This would be the answer if the cells were large and CD19 and CD20 positive. It also "
            "arises in the thymus of young adults, which is exactly why the immunophenotype has to be "
            "read — the radiology alone cannot separate them.",
        "T-lymphoblastic lymphoma": "",
    },
    "T-lymphoblastic lymphoma",
    "Terminal deoxynucleotidyl transferase makes this a precursor (lymphoblastic) neoplasm rather "
    "than a mature lymphoma, and CD3 with CD7 makes it T-lineage. The location then names it.\n\n"
    "The suffix tells you where the disease is, not what it is. T-lymphoblastic leukemia means the "
    "marrow and blood; T-lymphoblastic lymphoma means a mass — and the mass is in the thymus, "
    "because the thymus is where T cells mature. An anterior mediastinal mass in an adolescent with "
    "superior vena cava obstruction is the classic presentation.\n\n"
    "The same naming logic runs through the whole lymphoid section: chronic lymphocytic leukemia in "
    "the blood and marrow is small lymphocytic lymphoma in the node; mycosis fungoides in the skin is "
    "Sézary syndrome in the blood. One disease, two addresses.\n\n"
    "A practical heuristic for a stem full of unfamiliar markers: low CD numbers (CD2, 3, 4, 5, 7, 8) "
    "suggest a T cell; numbers in the twenties (CD19, CD20, CD22, CD79a) suggest a B cell.",
    "T cells grow up in the thymus, which sits behind the breastbone. When immature T cells turn "
    "cancerous there, they build a mass that presses on the airway and the big veins — hence the "
    "puffy face and breathlessness.",
)

q(
    "A 58-year-old woman is diagnosed with diffuse large B-cell lymphoma. She has Ann Arbor stage II "
    "disease with no extranodal sites, an ECOG performance status of 0, and a serum lactate "
    "dehydrogenase concentration of 310 U/L (N=45–90 U/L). Fluorescence in situ hybridization "
    "demonstrates rearrangement of MYC together with rearrangement of BCL2. Which of the following "
    "features of her disease is most strongly associated with reduced overall survival?",
    {
        "An Ann Arbor stage of II":
            "This would be the answer if she had stage III or IV disease, which scores a point on the "
            "International Prognostic Index. Stage II does not.",
        "An ECOG performance status of 0":
            "This would be the answer if her performance status were 2 or more, which scores a point. "
            "A status of 0 is favorable.",
        "An elevated serum lactate dehydrogenase concentration":
            "This scores one point on the International Prognostic Index and is genuinely adverse — "
            "but a score of 1 predicts about 81% overall survival, far better than the molecular "
            "finding here.",
        "Concurrent MYC and BCL2 rearrangements": "",
        "Patient age of 58 years":
            "This would be the answer if she were over 60, which scores a point on the International "
            "Prognostic Index. At 58 she does not score.",
    },
    "Concurrent MYC and BCL2 rearrangements",
    "Her International Prognostic Index score is 1 — only the lactate dehydrogenase scores — which "
    "on the clinical index alone predicts about 81% overall survival. The index runs: age over 60, "
    "raised lactate dehydrogenase, ECOG 2 or more, Ann Arbor stage III or IV, and more than one "
    "extranodal site, one point each. Scores of 0–1, 2, 3 and 4–5 predict roughly 81%, 69%, 53% and "
    "50% survival.\n\n"
    "Double hit lymphoma — a rearrangement placing MYC next to BCL2 or BCL6 — predicts approximately "
    "30%. That is worse than the worst possible clinical score. Molecular biology outranks the "
    "clinical index here, and that single fact is why every newly diagnosed diffuse large B-cell "
    "lymphoma is tested for MYC rearrangement with BCL2 or BCL6.\n\n"
    "Mechanistically it is the two routes to a lymphoid neoplasm combined in one cell: MYC drives "
    "proliferation, BCL2 blocks apoptosis. A cell told both to divide faster and not to die is a "
    "worse problem than either alone — grow-fast and die-slow in the same clone.",
    "Her clinical score looks good on paper. But her lymphoma carries two broken genes at once — one "
    "telling cells to multiply, the other telling them not to die — and that combination outweighs "
    "everything the score measures.",
)

q(
    "A 68-year-old woman has a complete blood count performed before an elective knee replacement. "
    "She feels well, has no palpable lymphadenopathy or splenomegaly, and has had no fevers, night "
    "sweats or weight loss.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 13.4 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 40% (N=36%–46%)\n"
    "Leukocyte count 68,000/mm3 (N=4,500–11,000/mm3)\n"
    "Lymphocytes 91% (N=24%–44%)\n"
    "Platelet count 212,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "A peripheral blood smear is shown. Flow cytometry of the blood demonstrates a population that "
    "is CD5, CD19, CD20 and CD23 positive and CD10 negative, with dim surface immunoglobulin light "
    "chain expression. Which of the following is the most appropriate next step in management?",
    {
        "Bendamustine with rituximab immunochemotherapy":
            "This would be the answer if she had a treatment indication — most often progressive "
            "cytopenias or bulky symptomatic disease. Treating an asymptomatic patient exposes her to "
            "toxicity without improving survival.",
        "Ibrutinib":
            "This would be the answer if she required treatment, and it would be the preferred choice "
            "if she carried del(17p), which responds poorly to chemoimmunotherapy. She requires no "
            "treatment at present.",
        "Observation with periodic reassessment": "",
        "Splenectomy":
            "This would be the answer in splenic marginal zone lymphoma, or for refractory "
            "hypersplenic cytopenias. Her spleen is not even palpable.",
        "Venetoclax":
            "This would be the answer if treatment were indicated; venetoclax inhibits BCL-2 and, like "
            "the Bruton tyrosine kinase inhibitors, is favored in del(17p) disease. The issue here is "
            "whether to treat at all.",
    },
    "Observation with periodic reassessment",
    "The immunophenotype is diagnostic of chronic lymphocytic leukemia: a B-cell population (CD19, "
    "CD20) that aberrantly expresses the T-cell marker CD5, is CD23 positive and CD10 negative, with "
    "dim surface light chain. Most cases are found exactly this way — as an incidental lymphocytosis "
    "on routine bloods.\n\n"
    "The buried point is what is NOT a treatment indication. The indications are pancytopenia, bulky "
    "lymphadenopathy, severe symptoms (malaise, weight loss, night sweats), and threatened end organ "
    "function. A rising or high lymphocyte count on its own is not among them, however alarming "
    "68,000/mm3 looks. She has a normal hemoglobin and a normal platelet count, no adenopathy, and no "
    "B symptoms.\n\n"
    "Risk stratification still happens now, even though treatment does not: fluorescence in situ "
    "hybridization (del(13q14.3) favorable; trisomy 12 or a negative result intermediate; del(17p) "
    "and del(11q) high risk), IgVH mutation status — where mutated is the favorable result, which is "
    "counterintuitive — and TP53 status, which is adverse wherever it appears.",
    "Her white count looks frightening, but the cells are not hurting her: blood counts normal, no "
    "lumps, no symptoms. In this leukemia a big number alone is not a reason to start treatment — "
    "you watch and recheck.",
    image="fig_lpd_smudge_cells",
    imcap="Peripheral blood smear showing monotonous small lymphocytes with coarsely clumped "
          "chromatin, together with several fragile cells disrupted during smear preparation "
          "(arrows).",
)

q(
    "A 72-year-old man with a 4-year history of chronic lymphocytic leukemia, managed with "
    "observation, reports 6 weeks of increasing fatigue and dyspnea on exertion. He has no new "
    "lymphadenopathy, and the spleen is unchanged in size. His hemoglobin concentration was 12.8 "
    "g/dL six months ago.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.1 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 24% (N=41%–53%)\n"
    "Reticulocyte count 9.2% (N=0.5%–1.5%)\n"
    "Lactate dehydrogenase 480 U/L (N=45–90 U/L)\n"
    "Haptoglobin <10 mg/dL (N=30–200 mg/dL)\n"
    "Total bilirubin 3.1 mg/dL (N=0.1–1.0 mg/dL)\n"
    "Platelet count 198,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Which of the following is the most appropriate next diagnostic test?",
    {
        "Bone marrow aspiration and biopsy":
            "This would be the answer if the reticulocyte count were LOW, indicating that the marrow "
            "had been replaced by the leukemic clone. A corrected reticulocyte count of about 5% says "
            "the marrow is working hard, so the red cells are being lost in the periphery.",
        "Direct antiglobulin test": "",
        "Excisional lymph node biopsy":
            "This would be the answer if he had a rapidly enlarging node or splenic mass with fever and "
            "a rising lactate dehydrogenase, suggesting Richter transformation to diffuse large B-cell "
            "lymphoma. His nodes and spleen are unchanged.",
        "Serum erythropoietin concentration":
            "This would be the answer if the question were whether an erythropoiesis-stimulating agent "
            "might help an underproduction anemia. The hemolysis panel here has already localized the "
            "problem to destruction.",
        "Serum protein electrophoresis":
            "This would be the answer if you suspected a paraprotein-driven process such as myeloma or "
            "lymphoplasmacytic lymphoma. Hypogammaglobulinemia, not a monoclonal spike, is the antibody "
            "problem of chronic lymphocytic leukemia.",
    },
    "Direct antiglobulin test",
    "The hemolysis panel moves as a unit here and points away from the tumor bulk: a high "
    "reticulocyte count, a high lactate dehydrogenase, an undetectable haptoglobin and an unconjugated "
    "hyperbilirubinemia mean red cells are being destroyed in the periphery while the marrow "
    "responds normally.\n\n"
    "This is the trap the lecture calls out explicitly. A falling hemoglobin in chronic lymphocytic "
    "leukemia may be autoimmune hemolysis rather than marrow infiltration — and the two have "
    "completely different treatments. Marrow replacement means the disease has progressed and needs "
    "cytotoxic or targeted therapy; warm autoimmune hemolysis is treated with corticosteroids, and "
    "the leukemia itself may still need no treatment. The direct antiglobulin test separates them in "
    "an afternoon.\n\n"
    "The mechanism is not mysterious: a disease of dysregulated B cells produces diseases of antibody "
    "function. The set is autoimmune hemolytic anemia, immune thrombocytopenia, and "
    "hypogammaglobulinemia causing recurrent sinopulmonary infection — all quite separate from how "
    "big the nodes are.",
    "His body is destroying its own red cells, not failing to make them — the marrow is actually "
    "working overtime. In this leukemia the immune system often turns on the red cells, and a simple "
    "blood test proves it.",
)

q(
    "A 23-year-old woman has a 2-month history of painless, progressively enlarging left cervical "
    "lymph nodes. She has generalized itching, and reports that the nodes ache within minutes of "
    "drinking a glass of wine. She has had no fevers or weight loss. Examination shows a 4-cm firm, "
    "rubbery, non-tender cervical node.\n\n"
    "Laboratory studies show:\n"
    "Leukocyte count 9,800/mm3 (N=4,500–11,000/mm3)\n"
    "Eosinophils 11% (N=1%–5%)\n"
    "Erythrocyte sedimentation rate 54 mm/h (N=0–20 mm/h)\n\n"
    "Which of the following is the most appropriate diagnostic procedure?",
    {
        "Bone marrow aspiration and biopsy":
            "This would be the answer if she had unexplained cytopenias or if staging required it after "
            "the diagnosis were made. The marrow does not establish the diagnosis when the disease is "
            "in a palpable node.",
        "Core needle biopsy of the largest node":
            "This would be the answer if the node were inaccessible — deep mediastinal or retroperitoneal "
            "— and imaging guidance were the only route. A core is usually insufficient here, because "
            "the diagnosis depends on architecture around very rare malignant cells.",
        "Excisional lymph node biopsy": "",
        "Fine-needle aspiration with flow cytometry":
            "This would be the answer if the suspected disease were a monomorphous small B-cell "
            "neoplasm whose diagnosis rests on immunophenotype. An aspirate samples cells without "
            "architecture and may return only the reactive background — missing the diagnosis "
            "entirely.",
        "Positron emission tomography with computed tomography":
            "This is the correct STAGING investigation once tissue confirms the diagnosis, together "
            "with the erythrocyte sedimentation rate. It cannot tell you what the disease is.",
    },
    "Excisional lymph node biopsy",
    "Alcohol-induced pain in involved nodes is rare but essentially specific for Hodgkin lymphoma. "
    "Combine it with pruritus, peripheral eosinophilia and painless cervical adenopathy in a patient "
    "in the first peak of the bimodal 15–35 and over-55 distribution, and the clinical diagnosis is "
    "made before any tissue exists.\n\n"
    "The tissue requirement is the testing point. Reed-Sternberg and Hodgkin cells make up less than "
    "10% of the cellularity — often only 1–2%. What fills the node is a reactive polymorphous "
    "infiltrate of lymphocytes, histiocytes, plasma cells, neutrophils, eosinophils and fibroblasts. "
    "The diagnosis therefore depends on seeing scattered large cells in the right architectural "
    "context, which needs a whole node.\n\n"
    "Staging is with positron emission tomography, computed tomography, and the erythrocyte "
    "sedimentation rate — the sedimentation rate being an unusual staging element worth remembering. "
    "The disease is curable; treatment is ABVD (doxorubicin, bleomycin, vinblastine, dacarbazine).",
    "The cancer cells in this disease are rare — most of the swollen node is ordinary immune tissue "
    "reacting around them. A needle sample would probably miss them, so the whole node has to come "
    "out.",
    exim="fig_lpd_reed_sternberg_cell",
    excap="Lymph node, hematoxylin and eosin: a single large binucleate cell with two cherry-red "
          "macronucleoli and perinuclear clearing sits among abundant small lymphocytes — the "
          "classic owl-eye appearance.",
)

q(
    "A 71-year-old man is brought to the emergency department because of 3 days of blurred vision, "
    "vertigo, and unsteady gait. Examination shows nystagmus, ataxia, and diffuse non-tender "
    "lymphadenopathy. Funduscopy shows dilated, sausage-shaped retinal veins.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.6 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 29% (N=41%–53%)\n"
    "Total protein 10.8 g/dL (N=6.0–7.8 g/dL)\n"
    "Serum IgM 6,200 mg/dL (N=40–230 mg/dL)\n"
    "Serum viscosity 5.1 (N=1.4–1.8)\n"
    "Serum calcium 9.4 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Creatinine 1.0 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "Which of the following is the most appropriate immediate treatment?",
    {
        "Bortezomib":
            "This would be the answer if the question were how to treat the underlying clone over the "
            "following weeks. Disease-directed therapy does not lower viscosity fast enough to protect "
            "a brain today — and the paraprotein can transiently RISE when treatment starts.",
        "Intravenous immunoglobulin":
            "This would be the answer if he had recurrent infection from hypogammaglobulinemia. Giving "
            "more immunoglobulin to a patient whose problem is too much immunoglobulin would worsen "
            "the viscosity.",
        "Plasmapheresis": "",
        "Red blood cell transfusion":
            "This would be the answer if symptomatic anemia were the problem. Transfusing raises the "
            "hematocrit and therefore raises viscosity further — it can precipitate the stroke you are "
            "trying to prevent.",
        "Rituximab":
            "This would be the answer once he is stabilized, as part of therapy directed at the "
            "CD20-positive clone. It is also the agent most associated with the IgM flare, so it is "
            "not what you reach for while he is symptomatic.",
    },
    "Plasmapheresis",
    "This is hyperviscosity syndrome from lymphoplasmacytic lymphoma — Waldenström macroglobulinemia. "
    "Vertigo, blurred vision, headache, nystagmus and ataxia are the syndrome; untreated it "
    "progresses to stroke, coma and delirium. The immediate treatment is emergent plasmapheresis to "
    "physically remove the paraprotein.\n\n"
    "Why IgM and not IgG: IgM is a pentamer, five antibody units joined together. That bulk keeps it "
    "in the intravascular space and raises viscosity at concentrations an IgG paraprotein would "
    "tolerate easily. One molecular property explains four separate syndromes — hyperviscosity, "
    "interference with fibrin polymerization causing bleeding, cold agglutinin hemolysis, and "
    "cryoglobulinemia.\n\n"
    "Note the negatives in the laboratory panel. Normal calcium and normal creatinine are what "
    "separate this from myeloma, whose signature is CRAB: hypercalcemia, renal failure, anemia and "
    "bone lesions. Waldenström thickens the blood and injures nerves; myeloma attacks the skeleton "
    "and the kidney.\n\n"
    "Once he is stabilized, treat the clone — but watch for the IgM flare, a transient rise at the "
    "start of therapy that worsens viscosity just as you begin to help.",
    "His blood has become as thick as syrup because it is loaded with a huge antibody, and thick "
    "blood cannot get through the small vessels of the brain and eye. A machine filters the antibody "
    "out of his plasma right away.",
)

q(
    "A 61-year-old man has a 6-month history of dyspepsia. Upper endoscopy shows thickened, eroded "
    "gastric folds, and biopsy specimens are obtained. Histologic sections are shown. The lymphoid "
    "cells are positive for CD20 and negative for CD5, CD10 and BCL6. Urease testing and histology "
    "both demonstrate Helicobacter pylori. Which of the following is the most appropriate initial "
    "therapy?",
    {
        "Helicobacter pylori eradication therapy": "",
        "R-CHOP chemoimmunotherapy":
            "This would be the answer if the biopsy had shown sheets of large cells — transformation to "
            "diffuse large B-cell lymphoma. A low-grade marginal zone lesion does not need "
            "anthracycline-based therapy up front.",
        "Radiation therapy to the involved stomach field":
            "This would be the answer in Helicobacter-negative disease, or in disease that fails to "
            "regress after successful eradication. Radiation is effective but is not the first move "
            "when the antigenic driver is still present and treatable.",
        "Rituximab monotherapy":
            "This is a reasonable alternative when eradication fails or the organism is absent. It "
            "treats the clone but leaves the stimulus that produced it in place.",
        "Total gastrectomy":
            "This would be the answer for a resectable gastric ADENOCARCINOMA. Surgery for a lymphoma "
            "that may regress with a two-week antibiotic course would be a serious overtreatment.",
    },
    "Helicobacter pylori eradication therapy",
    "Extranodal marginal zone lymphoma of mucosa-associated lymphoid tissue — gastric MALT lymphoma. "
    "The two named morphologic features are monocytoid cells (round nuclei, condensed chromatin, "
    "abundant pale cytoplasm producing clearing around each nucleus, with admixed plasma cells) and "
    "the lymphoepithelial lesion, in which the lymphoid cells invade and destroy the glands.\n\n"
    "The phenotype places the cell of origin. CD5 negative excludes the CD5 group (chronic "
    "lymphocytic leukemia, mantle cell); CD10 and BCL6 negative exclude a germinal center origin "
    "(follicular, Burkitt). The marginal zone lies OUTSIDE the germinal center, so germinal center "
    "markers should be absent — the anatomy predicts the phenotype rather than the other way round.\n\n"
    "Eradicating the organism can cure the cancer. Marginal zone lymphomas arise on a background of "
    "chronic antigenic stimulation, and early in their course the clone remains dependent on that "
    "drive. Remove it and the lymphoma regresses. This is the clearest demonstration in oncology that "
    "chronic inflammation, not only an intrinsic genetic lesion, can sustain a malignancy — the same "
    "logic links hepatitis C to nodal marginal zone lymphoma, celiac disease to enteropathy-associated "
    "T-cell lymphoma, and breast implants to anaplastic large cell lymphoma.\n\n"
    "The stomach is the commonest site (about a third of cases), followed by the orbit. Other "
    "organism–site pairs: Campylobacter jejuni in the small intestine, Borrelia burgdorferi in skin, "
    "Chlamydia psittaci in the conjunctiva.",
    "This stomach lymphoma is being fed by a bacterial infection. Kill the bacteria with antibiotics "
    "and the cancer often melts away on its own — one of the very few cancers antibiotics can cure.",
    image="fig_lpd_lymphoepithelial_lesion",
    imcap="Gastric biopsy, hematoxylin and eosin: a dense infiltrate of small lymphoid cells with "
          "abundant pale cytoplasm expands the lamina propria and invades the glandular epithelium, "
          "which is disrupted and effaced.",
)

q(
    "A 58-year-old woman is found to have asymptomatic bilateral axillary and inguinal "
    "lymphadenopathy. Excisional biopsy shows a nodal marginal zone lymphoma. She has no B symptoms, "
    "her blood counts are normal, and she has no organ dysfunction. Serologic testing is positive "
    "for hepatitis C virus antibody, and hepatitis C virus RNA is detectable at 1.2 million IU/mL. "
    "Which of the following is the most appropriate initial management?",
    {
        "Autologous hematopoietic stem cell transplantation":
            "This would be the answer for relapsed aggressive disease in a fit patient. It is far too "
            "much for an asymptomatic indolent lymphoma with a treatable driver.",
        "Direct-acting antiviral therapy": "",
        "Helicobacter pylori eradication therapy":
            "This would be the answer for a GASTRIC marginal zone lymphoma with a demonstrated "
            "organism. The principle is identical; the antigen here is a virus in the blood, not a "
            "bacterium in the stomach.",
        "Involved-field radiation therapy":
            "This would be the answer for localized marginal zone disease with no identifiable "
            "antigenic driver. Her disease is bilateral and her driver is both identified and "
            "curable.",
        "Splenectomy":
            "This would be the answer in SPLENIC marginal zone lymphoma, where splenectomy is standard. "
            "Her disease is nodal.",
    },
    "Direct-acting antiviral therapy",
    "Nodal marginal zone lymphoma is associated with chronic hepatitis C, and antiviral therapy may "
    "cure the lymphoma. It is the same principle as Helicobacter and the stomach, moved to a "
    "different antigen: chronic antigenic stimulation drives the clone, and removing the stimulus "
    "removes the growth signal.\n\n"
    "The indolent-lymphoma framing matters too. She is asymptomatic with normal counts and no organ "
    "dysfunction, so there is no indication for cytotoxic therapy — treatment of indolent disease is "
    "triggered by B symptoms, cytopenias or threatened end organ function, not by the existence of "
    "the diagnosis. Treating the virus does something useful while doing nothing harmful.\n\n"
    "The marginal zone family divides by site: nodal (hepatitis C), extranodal or MALT (Helicobacter "
    "pylori and the other chronic inflammatory states — rheumatoid arthritis, thyroiditis, Sjögren "
    "syndrome, lupus), and splenic (splenectomy).",
    "Her lymphoma is being driven by a chronic virus infection. Modern antiviral pills clear that "
    "virus in a couple of months, and the lymphoma can disappear along with it.",
)

q(
    "A 68-year-old man has 4 months of progressive generalized lymphadenopathy. Colonoscopy performed "
    "for iron deficiency shows numerous small polyps throughout the colon, and biopsies of the polyps "
    "contain the same lymphoid population as the node. Flow cytometry shows cells positive for CD5, "
    "CD19 and CD20 and negative for CD10 and CD23. Which of the following additional findings is most "
    "likely in this patient's neoplasm?",
    {
        "Activating BRAF V600E mutation of the MAP kinase pathway":
            "This would be the answer in hairy cell leukemia, where over 90% carry an activating MAP "
            "kinase pathway mutation — and where the phenotype is CD5 negative and CD10 negative with "
            "CD11c, CD25, CD103 and annexin A1.",
        "BCL2 overexpression from t(14;18)":
            "This would be the answer in follicular lymphoma, which is CD10 POSITIVE and CD5 negative. "
            "Both translocations place an oncogene under the immunoglobulin heavy chain promoter, but "
            "the partner gene and the phenotype differ.",
        "Cyclin D1 overexpression from t(11;14)": "",
        "MYC rearrangement from t(8;14)":
            "This would be the answer in Burkitt lymphoma — CD10 positive, BCL2 negative, Ki-67 above "
            "95%, with a starry-sky pattern. Nothing here suggests that tempo.",
        "MYD88 mutation with an IgM paraprotein":
            "This would be the answer in lymphoplasmacytic lymphoma, where the complications follow "
            "from the pentameric IgM. That neoplasm is CD5 negative.",
    },
    "Cyclin D1 overexpression from t(11;14)",
    "A CD5-positive B-cell neoplasm is the diagnostic oddity that starts this differential: CD5 is "
    "normally a T-cell marker, and only two important diseases break the rule — chronic lymphocytic "
    "leukemia / small lymphocytic lymphoma, and mantle cell lymphoma.\n\n"
    "CD23 is the discriminator. Chronic lymphocytic leukemia is CD23 POSITIVE; mantle cell lymphoma "
    "is CD23 NEGATIVE and carries t(11;14), placing cyclin D1 under the immunoglobulin heavy chain "
    "promoter. So the single negative marker in this stem is the whole answer.\n\n"
    "The supporting clinical detail is the gastrointestinal involvement, present in about 90% of "
    "mantle cell cases and classically appearing as lymphomatoid polyposis. The disease is twice as "
    "common in men, with a median age of 68.\n\n"
    "The distinction matters enormously. Chronic lymphocytic leukemia is indolent and often needs no "
    "treatment at all; mantle cell is aggressive and, in the lecture's phrase, everyone relapses. "
    "Counterintuitively, leukemic-phase-only disease is the LOW-risk group; high risk means "
    "symptomatic disease, del(17p), the blastoid variant, a raised lactate dehydrogenase, or a high "
    "proliferation index.",
    "Two cancers wear the same unusual badge (CD5). One extra badge tells them apart — and this "
    "patient is missing it, which points to the aggressive one that also carpets the bowel with "
    "polyps.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §41 — The lymphomas in depth: pattern, cell of origin, phenotype, translocation
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 24-year-old woman has cervical lymphadenopathy and a mediastinal mass. An excisional lymph "
    "node biopsy is shown. The node is divided into discrete nodules, within which large cells with "
    "abundant cytoplasm sit in apparent empty spaces among numerous eosinophils. The large cells are "
    "positive for CD30 and CD15, weakly positive for PAX5, and negative for CD20 and CD45. Which of "
    "the following features most reliably distinguishes this subtype from mixed cellularity disease?",
    {
        "Broad bands of collagen dividing the node": "",
        "Eosinophil-rich polymorphous inflammatory background":
            "Both subtypes show this. Mixed cellularity has somewhat fewer reactive cells overall, but "
            "eosinophils, plasma cells and lymphocytes are present in both — so it cannot separate "
            "them.",
        "Expression of CD30 by the large cells":
            "All four subtypes of classic Hodgkin lymphoma share the same neoplastic cell and the same "
            "immunophenotype. CD30 confirms the disease, not the subtype.",
        "Presence of Reed-Sternberg cells":
            "Reed-Sternberg cells define classic Hodgkin lymphoma as a whole. Mixed cellularity in fact "
            "shows MANY typical Reed-Sternberg cells, whereas nodular sclerosis is dominated by the "
            "lacunar variant.",
        "Weak PAX5 staining of the large cells":
            "This is shared by every subtype of classic Hodgkin lymphoma and is a diagnostic clue for "
            "the disease, not a subtyping criterion.",
    },
    "Broad bands of collagen dividing the node",
    "This is nodular sclerosis classic Hodgkin lymphoma, and fibrosis is what names it. Broad bands "
    "of collagen carve the node into nodules; mixed cellularity has no bands. The cells sitting in "
    "empty spaces are lacunar cells — the clearing is retraction artifact — and they are "
    "characteristic of this subtype.\n\n"
    "All four subtypes share one neoplastic cell and one immunophenotype. What differs is who gets "
    "it, how much reactive background there is, how many Reed-Sternberg cells you see, and whether "
    "there is fibrosis — and those variables map cleanly onto prognosis:\n\n"
    "• Nodular sclerosis — young adults, female-to-male 1:1, early stage, mediastinal disease, "
    "numerous lacunar cells, broad collagen bands. Excellent prognosis.\n"
    "• Lymphocyte-rich — usually early stage, background predominantly small lymphocytes, Reed-"
    "Sternberg cells often rosetted. Good.\n"
    "• Mixed cellularity — elderly males and children, high stage, many typical Reed-Sternberg cells, "
    "NO bands. Aggressive.\n"
    "• Lymphocyte-depleted — elderly males, HIV-associated, usually disseminated, sparse background "
    "inflammatory cells. Very aggressive.\n\n"
    "One caution on this case: when the Hodgkin and Reed-Sternberg variants predominate and look "
    "cohesive, it is the syncytial variant of nodular sclerosis, which can mimic a carcinoma or "
    "anaplastic large cell lymphoma — which is why an ALK stain is run whenever Hodgkin lymphoma is "
    "being considered.",
    "Both versions of this cancer look similar under the microscope — same cells, same background. "
    "The difference is scar tissue: this one has thick ropes of collagen slicing the node into "
    "chunks.",
    image="fig_lpd_nodular_sclerosis_lowpower",
    imcap="Lymph node at low power, hematoxylin and eosin: thick pink fibrous bands separate the "
          "darkly staining lymphoid tissue into discrete rounded nodules.",
)

q(
    "A hematopathologist is evaluating a lymph node biopsy from a 29-year-old man with suspected "
    "classic Hodgkin lymphoma. Scattered large atypical cells are present in a polymorphous "
    "background. On immunostaining, the large atypical cells show weak nuclear PAX5 staining, while "
    "the surrounding small lymphocytes stain strongly. CD20 is negative in the large cells. The "
    "pathologist describes PAX5 as the more helpful of the two stains. Which of the following best "
    "explains why?",
    {
        "PAX5 gives a graded result that the background B cells internally control": "",
        "PAX5 is a T-cell marker whose loss confirms B-cell lineage":
            "PAX5 is a B-cell transcription factor, not a T-cell marker. The aberrant T-cell marker in "
            "this section is CD5, expressed by chronic lymphocytic leukemia and mantle cell lymphoma.",
        "PAX5 is expressed only by Reed-Sternberg cells and not by any normal B cells":
            "The reverse is true, and it is the whole point: normal B cells stain STRONGLY for PAX5 and "
            "Reed-Sternberg cells stain weakly. If PAX5 were exclusive to the malignant cells there "
            "would be no internal comparison.",
        "PAX5 is the therapeutic target of brentuximab vedotin":
            "Brentuximab vedotin is an antibody-drug conjugate directed at CD30, which is both the "
            "diagnostic marker and the therapeutic target. PAX5 is a nuclear transcription factor and "
            "is not druggable in this way.",
        "PAX5 staining is required for the diagnosis, whereas CD20 is optional":
            "No single stain is required; the diagnosis rests on morphology plus a panel. CD15, for "
            "example, is positive in only about 75% of cases and is helpful when present rather than "
            "mandatory.",
    },
    "PAX5 gives a graded result that the background B cells internally control",
    "Reed-Sternberg and Hodgkin cells are of B-cell lineage but have switched their own B-cell "
    "program OFF, expressing B-cell repressors and silencing B-cell differentiation genes. The "
    "immunostain panel is designed to detect exactly that loss.\n\n"
    "CD20 simply comes back negative, and many things are CD20 negative — a binary negative carries "
    "little information. PAX5 comes back WEAK, and weak is only meaningful relative to something: the "
    "small reactive B cells in the same section stain darkly. One slide therefore carries its own "
    "positive control, and the comparison itself is the finding.\n\n"
    "The rest of the panel follows the same logic of a defective B-cell program. CD30 is strongly and "
    "uniformly positive with Golgi accentuation (and is the target of brentuximab vedotin); CD15 is "
    "positive in about 75%; MUM1 is strong; OCT2 and BOB1 are negative; CD19, CD20 and CD79a are "
    "negative despite B-cell lineage — which is precisely why rituximab does not work; CD45 is "
    "typically negative, separating this from nodular lymphocyte predominant disease and from B-cell "
    "non-Hodgkin lymphomas; and ALK is negative, excluding anaplastic large cell lymphoma.",
    "The cancer cells are faded B cells — they still show the B-cell stain, just dimly. Because "
    "normal B cells right next to them glow brightly on the same slide, the dimness itself is the "
    "proof.",
    exim="fig_lpd_chl_pax5",
    excap="PAX5 immunostain: the large atypical cells show pale nuclear staining, clearly weaker than "
          "the darkly stained small background B cells in the same field.",
)

q(
    "A 38-year-old man has a 3-cm isolated right cervical lymph node. He has no fever, night sweats "
    "or weight loss. Excisional biopsy shows effaced architecture with vaguely nodular areas "
    "containing scattered large cells with multilobated nuclei, pale chromatin and irregular "
    "nucleoli, rosetted by small lymphocytes. The large cells are positive for CD20, OCT2, BOB1 and "
    "CD45, and negative for CD30 and CD15. Which of the following therapies is directed at an antigen "
    "expressed by this patient's neoplastic cells?",
    {
        "Blinatumomab":
            "This would be the answer in precursor-B acute lymphoblastic leukemia; blinatumomab is a "
            "bispecific engager linking CD19 to CD3. The neoplastic cells here are mature B cells, and "
            "the agent named in this section is the anti-CD20 antibody.",
        "Brentuximab vedotin":
            "This would be the answer in classic Hodgkin lymphoma or anaplastic large cell lymphoma, "
            "the two CD30-positive lymphomas. These cells are explicitly CD30 negative.",
        "Imatinib":
            "This would be the answer where a BCR::ABL1 fusion drives the disease — chronic myeloid "
            "leukemia or Philadelphia-positive acute lymphoblastic leukemia. No fusion kinase is "
            "implicated here.",
        "Nivolumab":
            "PD-1 blockade is exceptionally effective in CLASSIC Hodgkin lymphoma, because that tumor "
            "is mostly reactive infiltrate and depends on evading it. It is not the antigen-directed "
            "answer the question asks for.",
        "Rituximab": "",
    },
    "Rituximab",
    "This is nodular lymphocyte predominant Hodgkin lymphoma — increasingly called nodular lymphocyte "
    "predominant B-cell lymphoma, and the name change tells the whole story. The diagnostic cell is "
    "the popcorn cell: multilobated, with vesicular (cleared-out) chromatin and an irregular "
    "nucleolus.\n\n"
    "Unlike classic Hodgkin lymphoma, this entity retains its B-cell program completely — CD20, OCT2, "
    "BOB1 and CD45 all positive, with strong PAX5 — while CD30 and CD15 are negative. It is the "
    "mirror image of the classic disease at every marker. Because CD20 is retained, rituximab has a "
    "target, and R-CHOP is a rational regimen; in classic Hodgkin lymphoma, which is CD20 negative, "
    "rituximab does nothing and brentuximab vedotin is used instead.\n\n"
    "The clinical picture supports it: a man aged 30–50 (male-to-female 3:1) with localized cervical "
    "disease — about 80% present at stage I–II — and no B symptoms, which are uncommon here and "
    "common in classic disease. The rosetting cells are T-follicular helper cells: CD4, CD57 and PD-1 "
    "positive.\n\n"
    "Prognosis is the best of any Hodgkin subtype, with over 80% ten-year survival in localized "
    "disease, but it recurs repeatedly over time. Children with localized disease are watched rather "
    "than treated.",
    "This is the Hodgkin lymphoma that never gave up being a B cell. Because it still wears the B-cell "
    "marker, the antibody drug that targets that marker actually works — which it does not in the "
    "usual kind.",
    exim="fig_lpd_popcorn_cells",
    excap="Lymph node, hematoxylin and eosin: a large cell with a folded, multilobated nucleus and "
          "pale chromatin sits among small lymphocytes.",
)

q(
    "A 62-year-old man has 3 months of fatigue and early satiety. Positron emission tomography with "
    "computed tomography shows avid para-aortic and mesenteric lymphadenopathy, splenic involvement, "
    "and enlargement of the Waldeyer ring. The cervical, supraclavicular, axillary and mediastinal "
    "nodal regions are normal. Which of the following features of this distribution argues most "
    "strongly against Hodgkin lymphoma?",
    {
        "Abdominal disease with a clear neck and chest": "",
        "An elevated serum lactate dehydrogenase concentration":
            "This is not part of the distribution, and it is non-specific: a raised lactate "
            "dehydrogenase indicates tumor burden and cell turnover in either family, and is an adverse "
            "prognostic factor in both.",
        "Involvement of the spleen":
            "Splenic involvement occurs in Hodgkin lymphoma and is explicitly part of Ann Arbor stage "
            "III. In the usual contiguous sequence it follows para-aortic disease.",
        "Painless, rubbery lymphadenopathy":
            "This describes malignant lymphadenopathy of any kind and does not separate the two "
            "families. It separates malignant from reactive nodes, which are soft, tender and mobile.",
        "The presence of B symptoms":
            "B symptoms — drenching night sweats, unexplained weight loss and fever — occur in both "
            "families and are part of Ann Arbor staging for both.",
    },
    "Abdominal disease with a clear neck and chest",
    "The distribution of disease separates the two families before any tissue exists, and question "
    "stems are written around exactly these contrasts.\n\n"
    "Hodgkin lymphoma involves a single AXIAL group — cervical, mediastinal, para-aortic — and spreads "
    "ORDERLY, by contiguity from one node group to the adjacent one. The rule that makes this stem "
    "work: abdominal nodes are not affected unless cervical or mediastinal nodes are involved first. "
    "The usual sequence runs para-aortic → spleen → liver or bone marrow, and left supraclavicular "
    "disease is typically followed by abdominal para-aortic nodes, while right supraclavicular disease "
    "associates with mediastinal involvement.\n\n"
    "Non-Hodgkin lymphoma involves multiple PERIPHERAL nodes and spreads NONCONTIGUOUSLY. It commonly "
    "involves the mesenteric nodes and the Waldeyer ring, which Hodgkin lymphoma rarely does, and "
    "presents extranodally far more often (Hodgkin extranodal disease is rare, and when it occurs the "
    "sites are bone, lung, spleen and liver).\n\n"
    "So this patient has two independent non-Hodgkin signatures: the skip to the abdomen over an "
    "uninvolved neck and chest, and mesenteric plus Waldeyer ring involvement.",
    "One of these cancers creeps politely from one node group to the next, always starting in the "
    "neck or chest. This patient's disease jumped straight to the belly with a clean neck — so it is "
    "the other kind.",
    exim="fig_lpd_hodgkin_vs_nonhodgkin_table",
    excap="The four clinical discriminators as the lecture presented them — nodal distribution, "
          "pattern of spread, mesenteric and Waldeyer ring involvement, and extranodal disease.",
)

q(
    "A 7-year-old boy in rural Kenya is brought to a clinic because of a mass of the right mandible "
    "that has doubled in size in 3 weeks and now prevents him from closing his mouth. Biopsy is shown. "
    "The cells are of intermediate size and uniform, and are positive for CD10, CD20 and BCL6 and "
    "negative for BCL2; the Ki-67 proliferation index exceeds 95%. Which of the following molecular "
    "findings is most likely?",
    {
        "A BCR::ABL1 fusion from t(9;22)":
            "This would be the answer in chronic myeloid leukemia or Philadelphia-positive acute "
            "lymphoblastic leukemia. It is a myeloid or precursor lesion, not a mature germinal center "
            "B-cell one.",
        "A PML::RARA fusion from t(15;17)":
            "This would be the answer in acute promyelocytic leukemia, which is treated on suspicion "
            "because of its coagulopathy. It is a myeloid disease with no relationship to this "
            "phenotype.",
        "Cyclin D1 expression driven by t(11;14)":
            "This would be the answer in mantle cell lymphoma, which is CD5 positive and CD10 negative. "
            "The mantle zone lies outside the germinal center, so CD10 positivity here excludes it.",
        "MYC translocated to the immunoglobulin heavy chain locus": "",
        "Overexpression of BCL2 driven by the t(14;18) translocation":
            "This would be the answer in follicular lymphoma. Both are germinal center neoplasms and "
            "both are CD10 and BCL6 positive — but this tumor is explicitly BCL2 NEGATIVE, which is the "
            "finding that separates them.",
    },
    "MYC translocated to the immunoglobulin heavy chain locus",
    "Endemic Burkitt lymphoma: a child in equatorial Africa with a rapidly growing jaw mass, a "
    "starry-sky pattern (pale tingible body macrophages standing out against a dark monotonous "
    "sheet), and a Ki-67 above 95%. The defining lesion is t(8;14), placing MYC from chromosome 8 "
    "under the immunoglobulin heavy chain promoter on chromosome 14.\n\n"
    "Burkitt and follicular lymphoma are the deliberate contrast. Both are CD10 and BCL6 positive, so "
    "both are germinal center neoplasms — but the mechanisms are opposite:\n\n"
    "• Follicular lymphoma is BCL2 POSITIVE through t(14;18). Anti-apoptosis is restored and the cells "
    "accumulate because they cannot die. Indolent.\n"
    "• Burkitt lymphoma is BCL2 NEGATIVE; the driver is MYC. The cells accumulate because they divide "
    "furiously. Aggressive, and simultaneously highly apoptotic — which is why the macrophages have so "
    "much debris to clear, producing the starry sky.\n\n"
    "Die-slow versus grow-fast, from two translocations that use the same trick. Both put an oncogene "
    "under the immunoglobulin heavy chain promoter, which is the general mechanism of lymphoid "
    "oncogenesis: potentially oncogenic mutations occur most often in germinal center B cells, because "
    "those cells deliberately break and rejoin their own DNA during class switch recombination and "
    "somatic hypermutation.\n\n"
    "The three subtypes: endemic (Epstein-Barr virus, jaw mass), sporadic (abdominal, often omental, "
    "and a cause of volvulus), and immunodeficiency-associated (HIV, nodal).",
    "This tumor doubles in size every couple of days because one gene that tells cells to divide has "
    "been jammed permanently on. It is the fastest-growing human cancer — and for that reason also one "
    "of the most curable.",
    image="fig_lpd_burkitt_starry_sky",
    imcap="Biopsy at medium power, hematoxylin and eosin: a dense monotonous sheet of intermediate-"
          "sized dark cells interrupted by numerous evenly spaced pale cells containing cellular "
          "debris.",
)

q(
    "A 64-year-old woman has 8 months of painless cervical, axillary and inguinal lymphadenopathy. "
    "She feels well. Excisional biopsy is shown; the node is effaced by crowded, back-to-back "
    "follicles of relatively uniform size, with attenuated mantle zones and no tingible body "
    "macrophages. Bone marrow biopsy shows lymphoid aggregates hugging the bony trabeculae. Which of "
    "the following immunohistochemical results would best confirm that the follicles are neoplastic "
    "rather than reactive?",
    {
        "BCL2 positivity within the follicles": "",
        "CD3 positivity within the follicles":
            "CD3 marks T cells. A germinal center is a B-cell structure, so CD3 positivity within the "
            "follicles would suggest a T-cell process such as angioimmunoblastic T-cell lymphoma, not "
            "confirm a follicular B-cell neoplasm.",
        "CD5 positivity of the follicular cells":
            "This would point to chronic lymphocytic leukemia or mantle cell lymphoma. Follicular "
            "lymphoma is CD5 NEGATIVE and CD10 positive — the two groups are mutually exclusive in this "
            "framework.",
        "Cyclin D1 positivity of the follicular cells":
            "This would indicate mantle cell lymphoma with t(11;14). Mantle cell can produce a vaguely "
            "nodular pattern, but the cell of origin is the mantle zone, not the germinal center.",
        "Ki-67 above 95% within the follicles":
            "This would indicate Burkitt lymphoma, which is also CD10 positive but diffuse, BCL2 "
            "negative and MYC-driven. A proliferation index that high is incompatible with an indolent "
            "disease that has been present for months.",
    },
    "BCL2 positivity within the follicles",
    "Normal germinal center B cells are BCL2 NEGATIVE, and the reason is functional. The germinal "
    "center exists to run somatic hypermutation and then delete the cells whose new receptors fail — "
    "so those cells must be easy to kill, which means switching the anti-apoptotic protein off.\n\n"
    "Follicular lymphoma is defined by the reverse. t(14;18) places BCL2 (chromosome 18) under the "
    "transcriptionally hyperactive immunoglobulin heavy chain promoter (chromosome 14), forcing it "
    "permanently on. Germinal-center-origin cells then accumulate because they cannot die — which is "
    "why the disease is indolent rather than fast. A positive BCL2 stain inside a follicle is "
    "therefore abnormal, and it is the single stain that separates follicular lymphoma from follicular "
    "hyperplasia.\n\n"
    "The supporting phenotype is CD10 positive, CD20 positive, BCL6 positive, BCL2 positive, CD5 "
    "negative. The morphologic clues in the stem support it too: reactive follicles vary in size and "
    "shape, have well-formed mantle zones and contain tingible body macrophages (the visible evidence "
    "of the apoptosis that is supposed to happen). Their absence is the same fact seen down the "
    "microscope.\n\n"
    "The paratrabecular marrow pattern is characteristic, present in 40–70%. Median survival exceeds "
    "17 years, with waxing and waning of involved sites — but transformation to diffuse large B-cell "
    "lymphoma occurs at 1–3% per year, which is why a new intensely avid site is biopsied "
    "specifically to look for it.",
    "A healthy germinal center deliberately keeps its self-destruct switch available, so faulty cells "
    "can be discarded. This lymphoma has glued that switch shut — and the stain that shows the switch "
    "is stuck is the diagnosis.",
    image="fig_lpd_follicular_lymphoma_back_to_back",
    imcap="Lymph node at low power, hematoxylin and eosin: crowded, closely apposed follicles of "
          "similar size fill the section, with little intervening tissue and poorly defined "
          "surrounding cuffs.",
    exim="fig_lpd_follicular_lymphoma_vs_reactive",
    excap="Side-by-side comparison of a neoplastic follicle and a reactive germinal center.",
)

q(
    "A 56-year-old man has 3 months of fatigue and left upper quadrant fullness. The spleen is "
    "palpable 8 cm below the costal margin. There is no lymphadenopathy.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.2 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 28% (N=41%–53%)\n"
    "Leukocyte count 2,100/mm3 (N=4,500–11,000/mm3)\n"
    "Monocytes 0% (N=3%–6%)\n"
    "Platelet count 64,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Bone marrow aspiration yields only hemodilute blood with no spicules. A peripheral blood smear "
    "is shown. Which of the following is the most likely diagnosis?",
    {
        "Chronic lymphocytic leukemia":
            "This would be the answer with a high lymphocyte count, smudge cells and a CD5-positive, "
            "CD23-positive phenotype. Chronic lymphocytic leukemia raises the white count rather than "
            "lowering it, and does not cause a dry tap.",
        "Hairy cell leukemia": "",
        "Mantle cell lymphoma":
            "This would be the answer with generalized lymphadenopathy, gastrointestinal involvement "
            "and a CD5-positive, CD23-negative phenotype with cyclin D1. He has no lymphadenopathy and "
            "no circulating atypical population of that kind.",
        "Myelodysplastic syndrome":
            "This would be the answer with dysplastic changes across lineages and a HYPERcellular marrow "
            "showing ineffective hematopoiesis. Myelodysplasia does not produce massive splenomegaly, "
            "selective monocytopenia, or a dry tap from fibrosis.",
        "Primary myelofibrosis":
            "This is the best distractor — it also gives a dry tap and massive splenomegaly. It is "
            "distinguished by leukoerythroblastosis with teardrop cells on the smear, and by the "
            "absence of both monocytopenia and the hairy lymphoid cells.",
    },
    "Hairy cell leukemia",
    "Three findings converge. The circulating mononuclear cells have fine cytoplasmic projections "
    "feathering the cell edge. The aspirate is a dry tap — hemodilute blood, no spicules — caused by "
    "the marrow fibrosis that the infiltrating hairy cells induce, so the needle cannot draw "
    "particles. And the monocyte count is zero.\n\n"
    "Monocytopenia is the stem's real giveaway. A lymphoproliferative disease of blood and marrow "
    "accompanied by monocytopenia should raise hairy cell leukemia specifically — it is unusual for a "
    "lymphoid neoplasm to suppress a myeloid lineage so selectively, and few other diseases do it.\n\n"
    "Demographics: middle-aged white men, median age 55, male-to-female 5:1. Over 90% carry an "
    "activating MAP kinase pathway mutation — BRAF — which is targetable with BRAF inhibitors. The "
    "immunophenotype is essentially specific: CD19, CD20, CD11c, CD25, CD103 and annexin A1 positive, "
    "with CD5 and CD10 both NEGATIVE, placing it in the same group as marginal zone and "
    "lymphoplasmacytic lymphoma.\n\n"
    "Note the paradox worth remembering: diffuse marrow involvement produces marrow failure and "
    "pancytopenia, and the spleen is large — yet the course is indolent. The main hazard is "
    "infection.",
    "His marrow is so scarred that the needle draws nothing but blood, and one particular white cell "
    "type has vanished completely. Those two clues, plus fuzzy-edged cells on the smear, name the "
    "disease.",
    image="fig_lpd_hairy_cell",
    imcap="Peripheral blood smear: a mononuclear cell with an oval nucleus and pale cytoplasm whose "
          "border shows fine, irregular projections.",
)

q(
    "A 58-year-old man has a 12-year history of scaly, sharply demarcated red-brown plaques over the "
    "buttocks, groin and lower trunk, previously treated as eczema. Over the past 4 months he has "
    "developed diffuse erythroderma. Skin biopsy shows small atypical lymphocytes with folded nuclei "
    "and clear perinuclear halos, some forming clusters within the epidermis; a section is shown.\n\n"
    "Laboratory studies show:\n"
    "Leukocyte count 14,200/mm3 (N=4,500–11,000/mm3)\n"
    "Absolute Sézary cell count 1,800/mm3 (N=0/mm3)\n\n"
    "Flow cytometry of the blood shows an expanded CD4-positive population with a CD4:CD8 ratio of "
    "18:1 and loss of CD7 and CD26. Which of the following studies would best confirm the diagnosis?",
    {
        "Bone marrow aspiration and biopsy with cytogenetics":
            "This would be the answer if you suspected a primary marrow neoplasm. Mycosis fungoides is "
            "staged by skin, node, viscera and blood, and the marrow is not the site that settles this "
            "diagnosis.",
        "Direct immunofluorescence of lesional and perilesional skin":
            "This would be the answer in an autoimmune blistering disease such as pemphigus or bullous "
            "pemphigoid, where immune deposits define the diagnosis. There is no immune deposition "
            "here.",
        "Patch testing for contact allergens":
            "This would be the answer if the eruption were an allergic contact dermatitis. A 12-year "
            "course with atypical cerebriform lymphocytes invading the epidermis is not eczema, "
            "although it is very commonly treated as such for years.",
        "Serum immunoglobulin E concentration":
            "This would be the answer if you suspected atopic dermatitis or a hyper-IgE syndrome. "
            "Neither explains a clonal CD4 population with marker loss.",
        "T-cell receptor gene rearrangement in blood and skin": "",
    },
    "T-cell receptor gene rearrangement in blood and skin",
    "Mycosis fungoides progressing to Sézary syndrome. All three Sézary criteria are met: "
    "erythroderma, an absolute Sézary cell count above 1,000/mm3, and flow cytometry showing an "
    "expanded CD4 population with a CD4:CD8 ratio above 10:1 plus loss of CD7 and CD26.\n\n"
    "But Sézary cells alone are not specific — reactive lymphocytes can look convoluted. What cements "
    "the diagnosis is demonstrating the SAME clone in the blood and in the skin by T-cell receptor "
    "gene rearrangement. Clonality is the proof; morphology and flow are the suspicion.\n\n"
    "The four microscopic features of mycosis fungoides: small to medium haloed lymphocytes with "
    "hyperchromatic, hyperconvoluted (cerebriform) nuclei; epidermotropism, the preferential migration "
    "of atypical lymphocytes up into the epidermis; Pautrier microabscesses, clusters of those "
    "lymphocytes within the upper epidermis; and large cell transformation, defined as more than 25% "
    "large cells.\n\n"
    "The distribution in the stem is the classic one — sun-protected axilla and groin plus lower trunk "
    "and buttocks, the bathing trunk distribution. The naming convention applies again: mycosis "
    "fungoides is the skin, Sézary syndrome is the blood.\n\n"
    "The phenotype is a disrupted T-cell program: CD2, CD3 and CD5 positive (CD5 sometimes lost), CD4 "
    "positive and CD8 negative, CD7 dim or partially lost. Infections through the broken skin barrier "
    "are a leading cause of hospitalization and sepsis.",
    "Odd-looking immune cells are not enough — normal skin can have those. Proving cancer means "
    "showing the identical cell clone in both the skin and the bloodstream, which is what the gene "
    "test does.",
    image="fig_lpd_pautrier_microabscesses",
    imcap="Skin biopsy, hematoxylin and eosin: several sharply defined intraepidermal collections are "
          "packed with small dark lymphoid cells, with a band-like infiltrate in the underlying "
          "dermis.",
    exim="fig_lpd_mycosis_fungoides_plaques",
    excap="Sharply demarcated scaling red-brown plaques over the lower trunk and buttocks — the "
          "bathing trunk distribution of sun-protected sites.",
)

q(
    "A 61-year-old woman with a 9-year history of mycosis fungoides is noted to have a 2.5-cm "
    "axillary lymph node. Excisional biopsy shows preserved but distorted nodal architecture with "
    "reactive germinal centers in the superficial cortex, and a paracortex that is expanded and pale "
    "at low power, filled with bland histiocytes and dendritic cells together with numerous "
    "pigment-laden macrophages. Atypical lymphocytes are not identified. Which of the following is "
    "the most appropriate interpretation?",
    {
        "Dermatopathic lymphadenopathy, a reactive change": "",
        "Kikuchi-Fujimoto lymphadenitis":
            "This would be the answer with patchy necrosis containing abundant karyorrhectic debris and "
            "crescentic myeloperoxidase-positive histiocytes, and conspicuously NO neutrophils. There "
            "is no necrosis here.",
        "Metastatic melanoma involving the node":
            "This would be the answer if the pigment lay within large atypical cells filling the "
            "subcapsular sinus, positive for S100 and other melanocytic markers. Here the pigment is "
            "inside bland macrophages, which is what phagocytosed skin pigment looks like.",
        "Nodal involvement by the patient's cutaneous lymphoma":
            "This would be the answer if the paracortex were expanded by ATYPICAL cerebriform "
            "lymphocytes matching the skin lesion's phenotype, with architectural effacement. It is the "
            "error the question is built around.",
        "Rosai-Dorfman disease":
            "This would be the answer with massively distended sinuses containing large S100-positive "
            "histiocytes showing emperipolesis — intact lymphocytes within their cytoplasm. That is a "
            "sinus process, not a paracortical one.",
    },
    "Dermatopathic lymphadenopathy, a reactive change",
    "Dermatopathic lymphadenopathy is the reactive response of a node draining chronically inflamed "
    "skin, and patients with mycosis fungoides develop it dramatically. Recognizing it matters because "
    "mycosis fungoides is staged by skin, node, viscera and blood — calling a reactive node involved "
    "would upstage the patient incorrectly and change treatment.\n\n"
    "The three recognition features are all in the stem. Architecture is preserved though distorted. "
    "The superficial cortex still shows reactive germinal centers. And the paracortical expansion is "
    "PALE at low power because it is filled with histiocytes and dendritic cells plus pigment-laden "
    "macrophages — the pigment having been carried in from the skin — rather than with atypical "
    "lymphocytes.\n\n"
    "The paracortex is the T-cell zone, so paracortical expansion in a patient with a T-cell lymphoma "
    "is exactly the right thing to be suspicious about. The resolution is to compare the node's "
    "immunophenotype and flow cytometry with the skin lesion's: true involvement carries the same "
    "aberrant phenotype, with loss of CD7 and CD26.",
    "Skin that has been inflamed for years sends pigment and cleanup cells to the nearest lymph node, "
    "which swells as a result. That swelling is not the cancer spreading — and mistaking it for spread "
    "would wrongly make the disease look far more advanced.",
)

q(
    "A 14-year-old girl has a 3-cm cervical lymph node and a subcutaneous nodule on the forearm. "
    "Excisional biopsy of the node is shown; it shows uniform sheets of very large atypical cells, "
    "many with eccentric, horseshoe-shaped nuclei and a pale paranuclear zone. The cells are strongly "
    "and diffusely positive for CD30, and positive for CD4, EMA and CD45; CD3 and CD15 are negative. "
    "Which of the following additional immunostain results would confirm the diagnosis and carry the "
    "most favorable prognostic information?",
    {
        "ALK positivity": "",
        "CD15 positivity":
            "CD15 is positive in about 75% of classic Hodgkin lymphoma and is the marker this case is "
            "explicitly negative for. It is already reported as negative in the stem.",
        "CD20 positivity":
            "This would point to a B-cell neoplasm — nodular lymphocyte predominant Hodgkin lymphoma, or "
            "a large B-cell lymphoma. It would contradict the CD4-positive T-cell-associated profile "
            "described.",
        "Cyclin D1 positivity":
            "This would indicate mantle cell lymphoma with t(11;14), a small CD5-positive B-cell "
            "neoplasm. Nothing about sheets of enormous CD30-positive cells fits it.",
        "Weak PAX5 staining":
            "Weak PAX5 against strongly stained background B cells is the signature of CLASSIC Hodgkin "
            "lymphoma — the entity being excluded here, not confirmed.",
    },
    "ALK positivity",
    "Anaplastic large cell lymphoma. The diagnostic cell is the hallmark cell: eccentric, "
    "horseshoe-shaped (crescentic or kidney-shaped) nucleus with a pale paranuclear area. The "
    "doughnut cell is the same cell cut in a different plane.\n\n"
    "Anaplastic large cell lymphoma and classic Hodgkin lymphoma are the two CD30-positive lymphomas, "
    "which is why brentuximab vedotin works in both — and why CD30 cannot separate them. Two things "
    "do. First, architecture: here the atypical cells form uniform SHEETS, whereas in classic Hodgkin "
    "lymphoma the Reed-Sternberg cell is never the predominant cell (under 10%, often 1–2%). Second, "
    "the stain: ALK is positive in a substantial fraction of anaplastic large cell lymphoma and always "
    "negative in classic Hodgkin lymphoma. EMA and CD45 positivity also support it, since classic "
    "Hodgkin lymphoma is CD45 negative.\n\n"
    "ALK status is what matters prognostically: ALK positive gives long-term survival around 80% and "
    "is more common in adolescents; ALK negative gives about 50% five-year overall survival.\n\n"
    "The diagnostic hazard is that these cells often do not look lymphoid at all. A sinusoidal pattern "
    "with cohesive-looking cells mimics metastatic carcinoma or melanoma, especially in adults, and a "
    "nodular pattern with fibrous bands mimics nodular sclerosis. Keep it on the differential for any "
    "undifferentiated malignancy in a node — and note that CD3 is often negative, which makes proving "
    "T-cell lineage harder.",
    "Two different lymphomas both carry the same marker, so that marker cannot tell them apart. One "
    "extra stain does — and in this cancer, a positive result is actually good news for survival.",
    image="fig_lpd_alcl_hallmark_cells",
    imcap="Lymph node, hematoxylin and eosin: sheets of very large cells with abundant cytoplasm; "
          "several have eccentric, indented horseshoe-shaped nuclei with a pale zone beside the "
          "nucleus (arrows).",
)

q(
    "A 66-year-old man who emigrated from Japan 20 years ago has 2 months of generalized "
    "lymphadenopathy, infiltrated skin plaques, and hepatosplenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Leukocyte count 38,000/mm3 (N=4,500–11,000/mm3)\n"
    "Serum calcium 13.8 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Lactate dehydrogenase 720 U/L (N=45–90 U/L)\n"
    "Creatinine 1.4 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "A peripheral blood smear is shown. Which of the following is the most likely causal agent?",
    {
        "Epstein-Barr virus":
            "This would be the answer in endemic Burkitt lymphoma, classic Hodgkin lymphoma — "
            "particularly the lymphocyte-depleted subtype — or Epstein-Barr virus-positive diffuse "
            "large B-cell lymphoma. None produces circulating multilobated T cells with hypercalcemia.",
        "Helicobacter pylori":
            "This would be the answer in gastric marginal zone (MALT) lymphoma, driven by chronic "
            "antigenic stimulation and treatable by eradication. It is a mucosal B-cell disease.",
        "Human herpesvirus 8":
            "This would be the answer in primary effusion lymphoma, which presents as a malignant "
            "effusion WITHOUT a mass; the same virus causes multicentric Castleman disease and Kaposi "
            "sarcoma.",
        "Human immunodeficiency virus":
            "HIV raises the risk of Burkitt lymphoma, primary central nervous system lymphoma and "
            "lymphocyte-depleted Hodgkin lymphoma. It does not produce flower cells or this "
            "geographic signature.",
        "Human T-lymphotropic virus 1": "",
    },
    "Human T-lymphotropic virus 1",
    "Adult T-cell leukemia/lymphoma. The circulating cells are flower cells — multilobated, with "
    "distinct petal-like lobes radiating from a center, like a clover.\n\n"
    "Geography is the intended clue and it is worth reading as a hard signal: Japan, the Caribbean, "
    "intertropical Africa, the Middle East, South America and Papua New Guinea are the endemic areas "
    "for human T-lymphotropic virus 1. Median age 68.\n\n"
    "The presentation is generalized lymphadenopathy, skin lesions, hepatosplenomegaly — and "
    "hypercalcemia, which is the laboratory signature. Four clinical subtypes (acute, lymphoma, "
    "chronic and smoldering) are defined by organ involvement, lactate dehydrogenase and calcium, and "
    "the degree of leukemic manifestation. The disease is aggressive.\n\n"
    "The deliberate contrast is with the Sézary cell. Both are abnormal circulating T cells with "
    "strange nuclei, but the shapes differ: the flower cell is MULTILOBATED, with separate petal-like "
    "lobes; the Sézary cell is CONVOLUTED or cerebriform — one folded mass with a brain-like surface, "
    "not separate lobes.",
    "A virus caught decades ago in a specific part of the world can eventually turn a T cell "
    "cancerous. The giveaways are where he grew up, the sky-high calcium, and cells whose nuclei look "
    "like flower petals.",
    image="fig_lpd_atll_flower_cells",
    imcap="Peripheral blood smear, four fields: lymphoid cells whose nuclei are divided into several "
          "rounded lobes radiating from the center.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §42 — Plasma cell disorders
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 66-year-old woman is evaluated after a routine serum protein electrophoresis performed for an "
    "elevated total protein shows a monoclonal spike. She is asymptomatic. A bone marrow biopsy shows "
    "22% plasma cells, and a skeletal survey shows no lytic lesions.\n\n"
    "Laboratory studies show:\n"
    "Monoclonal IgG 3.6 g/dL (N=0 g/dL)\n"
    "Hemoglobin 13.1 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 39% (N=36%–46%)\n"
    "Serum calcium 9.5 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Creatinine 0.9 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "Which of the following is the most appropriate management?",
    {
        "Autologous hematopoietic stem cell transplantation":
            "This would be the answer for a fit patient with ACTIVE myeloma after induction therapy. "
            "She has no end organ damage, so she has no myeloma to treat.",
        "Bortezomib, lenalidomide and dexamethasone":
            "This would be the answer if she had any CRAB feature — hypercalcemia, renal failure, anemia "
            "or bone lesions. Her calcium, creatinine, hemoglobin and skeletal survey are all normal.",
        "Observation with laboratory surveillance every 4 months": "",
        "Observation with laboratory surveillance every 6 months":
            "This is the correct interval for MGUS, which requires plasma cells under 10% AND a "
            "monoclonal protein under 3 g/dL. She exceeds both thresholds, so she is in the "
            "higher-risk precursor state.",
        "Palliative radiotherapy to the thoracolumbar spine":
            "This would be the answer for a painful focal lesion or threatened cord compression. She "
            "has no lesions and no symptoms.",
    },
    "Observation with laboratory surveillance every 4 months",
    "Two numbers separate the precursor states: 10 and 3. Under 10% marrow plasma cells AND under "
    "3 g/dL monoclonal protein is MGUS. At or above either threshold — up to 60% plasma cells — is "
    "smoldering myeloma. This patient has 22% plasma cells and 3.6 g/dL, so she is smoldering on both "
    "counts.\n\n"
    "Neither is treated. Both are watched. What converts either into active myeloma is END ORGAN "
    "DAMAGE — the CRAB tetrad of hypercalcemia, renal failure, anemia and bone lesions — and she has "
    "none.\n\n"
    "What changes with the label is the intensity of surveillance, because the risk differs tenfold. "
    "MGUS progresses at a flat 1% per year. Smoldering myeloma is front-loaded: 10% per year for the "
    "first 5 years, then 3% per year for 5 years, then 1% per year. That shape is why surveillance is "
    "heavier early.\n\n"
    "MGUS surveillance: serum protein electrophoresis, serum light chains, complete blood count and a "
    "comprehensive metabolic panel every 6 months, with a skeletal survey at least annually. "
    "Smoldering: the same, but labs every 4 months, and consider an annual positron emission "
    "tomography scan.",
    "She has a plasma cell problem that has not yet done any damage, so there is nothing to treat. "
    "But her numbers put her in the higher-risk waiting room, so she gets checked more often — every "
    "four months instead of every six.",
)

q(
    "A 70-year-old man has 3 months of lower back pain and fatigue. He has no fever.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.1 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 27% (N=41%–53%)\n"
    "Serum calcium 11.8 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Creatinine 3.4 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Total protein 7.4 g/dL (N=6.0–7.8 g/dL)\n\n"
    "Serum protein electrophoresis shows a monoclonal spike of only 0.9 g/dL. Urinalysis shows 1+ "
    "protein by dipstick and no cells or casts. Which of the following studies best explains his "
    "renal failure?",
    {
        "Renal ultrasonography":
            "This would be the answer if you suspected obstruction or chronic parenchymal disease. It "
            "would not explain why a patient with a barely abnormal electrophoresis has a creatinine of "
            "3.4 mg/dL.",
        "Serum beta-2 microglobulin concentration":
            "This is a marker of tumor burden and a prognostic factor in myeloma, and it rises in renal "
            "failure. It grades the disease rather than explaining the kidney.",
        "Serum free light chain assay": "",
        "Skeletal survey":
            "This is part of the standard workup and may well show lytic lesions explaining his back "
            "pain. It addresses the bone component of CRAB, not the renal one.",
        "Urine culture":
            "This would be the answer if the urinalysis showed pyuria, bacteriuria or white cell casts. "
            "A bland sediment with mild proteinuria argues against infection.",
    },
    "Serum free light chain assay",
    "An antibody is built from heavy chains and light chains. A myeloma clone can secrete free light "
    "chains in enormous excess, and because they are small they are filtered at the glomerulus and "
    "precipitate in the tubules — light chain cast nephropathy.\n\n"
    "The buried clue is the mismatch. Serum protein electrophoresis measures the intact paraprotein, "
    "so a light-chain-predominant clone produces only a modest spike (here 0.9 g/dL, with a total "
    "protein that is not even raised) while flooding the kidney. That is exactly why serum free light "
    "chains are measured SEPARATELY in the standard workup rather than being inferred from the "
    "electrophoresis.\n\n"
    "The second clue is the urinalysis. A dipstick detects albumin, not light chains, so cast "
    "nephropathy characteristically gives a modest dipstick result with a bland sediment — the "
    "protein that is doing the damage is invisible to the strip.\n\n"
    "He has three of the four CRAB features already: hypercalcemia, renal failure and anemia, with "
    "back pain suggesting the fourth. The full workup is serum protein electrophoresis, serum light "
    "chains, a comprehensive metabolic panel for calcium and renal function, a complete blood count, "
    "and a skeletal survey, with equivocal findings confirmed by positron emission tomography or "
    "magnetic resonance imaging.",
    "The antibody pieces wrecking his kidneys are too small to show up properly on the usual protein "
    "test — they slip through the filter and clog the tubes. You have to measure those small pieces "
    "directly.",
)

q(
    "A 74-year-old man has fatigue, weight loss and a monoclonal paraprotein. Which of the following "
    "findings, if present, would most strongly favor lymphoplasmacytic lymphoma (Waldenström "
    "macroglobulinemia) over multiple myeloma?",
    {
        "A serum calcium concentration of 12.4 mg/dL":
            "Hypercalcemia is common in myeloma — the C of CRAB, driven by osteoclastic bone "
            "destruction — and uncommon in lymphoplasmacytic lymphoma, which does not characteristically "
            "involve bone.",
        "Marrow plasma cells above 60%":
            "A plasma cell burden of this size indicates myeloma. Lymphoplasmacytic lymphoma is a "
            "neoplasm of lymphoplasmacytic cells — B cells with plasmacytic differentiation — not of "
            "fully differentiated plasma cells.",
        "Monoclonal IgM with diffuse lymphadenopathy": "",
        "Multiple lytic lesions on the skeletal survey":
            "Lytic lesions are characteristic of myeloma, which is why a skeletal survey is part of its "
            "workup. They are typically ABSENT in lymphoplasmacytic lymphoma.",
        "Renal failure from light chain cast nephropathy":
            "This is the renal lesion of myeloma. Renal failure is uncommon in lymphoplasmacytic "
            "lymphoma, whose paraprotein is a large pentamer that is not filtered.",
    },
    "Monoclonal IgM with diffuse lymphadenopathy",
    "The paraprotein class is the fastest discriminator. Myeloma usually secretes IgG or IgA (or "
    "light chains only); lymphoplasmacytic lymphoma secretes IgM — and the pentameric structure of "
    "IgM drives every one of its complications.\n\n"
    "The lymphadenopathy is the second half of the answer. Lymphoplasmacytic lymphoma is an indolent "
    "LYMPHOMA, so advanced diffuse lymphadenopathy with or without splenomegaly is expected; in "
    "myeloma, which is a marrow-based plasma cell disease, lymphadenopathy is uncommon.\n\n"
    "The rest of the comparison:\n"
    "• Cell of origin — fully differentiated plasma cell versus a lymphoplasmacytic cell.\n"
    "• Genetics — FISH abnormalities with 17p adverse, versus MYD88 mutation.\n"
    "• Bone lesions — characteristic versus typically absent.\n"
    "• Renal failure and hypercalcemia — common versus uncommon.\n"
    "• Hyperviscosity — uncommon versus characteristic, and an emergency needing plasmapheresis.\n"
    "• Signature complications — CRAB, versus hyperviscosity, peripheral neuropathy, cold agglutinin "
    "hemolysis, cryoglobulinemia, and bleeding from impaired fibrin polymerization.\n\n"
    "The memory hook: myeloma attacks the skeleton and the kidney; Waldenström thickens the blood and "
    "injures nerves. Lytic lesions, hypercalcemia and renal failure means myeloma. Blurred vision, "
    "vertigo, ataxia and a neuropathy in someone with lymphadenopathy means the IgM disease.",
    "Both cancers flood the blood with one antibody. Which antibody it is decides the disease: the "
    "big sticky IgM version clogs blood vessels and swells lymph nodes, while the other kind eats "
    "bone and clogs kidneys.",
)
