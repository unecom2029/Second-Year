# Hardest Exam — batch H4 of 5 (questions 61–80)
# Sections §36–§42 plus §51: the core construct and the acute leukemia emergencies, acute myeloid
# leukemia and acute promyelocytic leukemia, myelodysplastic syndrome and chronic myeloid leukemia,
# the myeloproliferative neoplasms, acute lymphoblastic leukemia and the lymphomas, plasma cell
# disorders, and childhood leukemia prognosis.

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


# ── 61. The grade paradox — aggressive disease is the curable one (§36) ─────────
q(
    "Two patients are seen in the hematology clinic on the same afternoon. The first is a 34-year-old "
    "man with a 6-week history of a rapidly enlarging neck mass, drenching night sweats and 8 kg of "
    "weight loss; biopsy shows sheets of large atypical B cells with a proliferation index of 85%, "
    "and he is started on combination chemoimmunotherapy with curative intent. The second is a "
    "71-year-old woman with 3 years of slowly enlarging, painless nodes in several sites, no "
    "systemic symptoms and normal blood counts; biopsy shows small cleaved cells in crowded "
    "follicles with a proliferation index of 10%, and she is observed without treatment. Which of "
    "the following best explains why the more aggressive disease is the one treated with curative "
    "intent?",
    {
        "Aggressive lymphomas are diagnosed at an earlier stage":
            "The reverse is closer to the truth — indolent lymphoma is usually already stage III or "
            "IV at diagnosis, and in indolent disease that fact changes very little.",
        "Aggressive lymphomas arise from more differentiated cells":
            "The opposite. In the core construct, the LESS differentiated the transformed cell, the "
            "more aggressive the disease; indolent lymphomas arise from more mature cells.",
        "Cytotoxic drugs act on cells that are actively dividing": "",
        "Indolent lymphomas are more often resistant to rituximab":
            "Both are typically CD20 positive and respond to anti-CD20 antibodies. Indolent disease "
            "responds, relapses and responds again — response is not the problem, durability is.",
        "Indolent lymphomas have a higher rate of secondary mutations":
            "Transformation of follicular lymphoma to large cell lymphoma does occur (about 30% over "
            "10 years), but accumulating mutations is not why the aggressive disease is curable.",
    },
    "Cytotoxic drugs act on cells that are actively dividing",
    "The grade paradox, and it inverts the usual intuition about what a bad diagnosis means.\n\n"
    "The core construct of hematologic malignancy: a cell acquires mutations that arrest the "
    "differentiation and maturation of its progeny, and where on the path from stem cell to mature "
    "cell that happens determines the disease. LESS differentiated → aggressive. MORE differentiated "
    "→ indolent.\n\n"
    "Then the treatment consequence:\n"
    "• HIGH GRADE / aggressive — untreated death in 3–6 months, but a high proliferation fraction "
    "means nearly the whole population is exposed to a drug that kills dividing cells, so treatment "
    "intent is CURE\n"
    "• LOW GRADE / indolent — compatible with decades of life, but most cells are not cycling when "
    "the drug is present, so standard therapy does not cure. A third of follicular lymphoma patients "
    "are never treated at all\n\n"
    "The corollary is tumour lysis syndrome: the same rapid turnover that makes aggressive disease "
    "curable makes it dangerous to treat.\n\n"
    "Stage behaves differently in each. In aggressive lymphoma advanced stage drives urgency; in "
    "indolent lymphoma it is the norm at diagnosis and changes nothing. And molecular findings can "
    "outweigh clinical stage entirely — double hit lymphoma (MYC rearranged with BCL2 or BCL6) has "
    "about 30% overall survival, worse than the highest International Prognostic Index score of 4–5, "
    "which carries 50%.\n\n"
    "Educational objective: Aggressive hematolymphoid neoplasms arise from less differentiated cells "
    "and have a high proliferation fraction, which is precisely why cytotoxic therapy can cure them; "
    "indolent neoplasms arise from more mature cells, divide slowly, and are generally incurable "
    "though compatible with many years of life.",
    "Chemotherapy kills cells while they are dividing. The fast cancer has almost every cell "
    "dividing, so the drug wipes it out; the slow one keeps most of its cells asleep, where the drug "
    "cannot reach them.",
    exim="fig_slide_maturation_tree",
    excap="The core construct — where on the maturation path transformation occurs determines which "
          "disease results and how fast it moves.",
)

# ── 62. Assigning lineage in acute leukemia (§37) ───────────────────────────────
q(
    "A 57-year-old woman comes to the office due to 3 weeks of progressive fatigue and bruising that "
    "appears without injury. She has no lymphadenopathy, hepatosplenomegaly or bone tenderness. "
    "Pulse is 110/min and she is pale.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 6.2 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 19% (N=36%–46%)\n"
    "Leukocyte count 87,000/mm3 (N=4,500–11,000/mm3)\n"
    "Segmented neutrophils 1% (N=54%–62%)\n"
    "Platelet count 45,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Ninety percent of circulating leukocytes are large cells with scant cytoplasm, fine chromatin "
    "and prominent nucleoli. A bone marrow biopsy is shown. Which of the following findings would "
    "best establish the lineage of this patient's disease?",
    {
        "CD41 and CD61 expression":
            "These are the platelet glycoproteins IIb and IIIa, marking megakaryocytic "
            "differentiation — a rare acute megakaryoblastic leukemia, not the default answer in this "
            "presentation.",
        "Cytoplasmic myeloperoxidase": "",
        "Glycophorin A expression":
            "Glycophorin A is an erythroid marker, used when a pure erythroid leukemia is being "
            "considered.",
        "Terminal deoxynucleotidyl transferase":
            "TdT is a DNA polymerase found only in LYMPHOBLASTS, so it would indicate acute "
            "lymphoblastic leukemia — a real alternative here, but it establishes the other lineage.",
        "Surface CD3 expression":
            "CD3 marks T lymphocytes and would point to a T-lymphoblastic neoplasm, which typically "
            "presents in a younger patient with a mediastinal mass.",
    },
    "Cytoplasmic myeloperoxidase",
    "Acute leukemia — over 20% blasts in the marrow OR the blood is the diagnostic line, and either "
    "compartment suffices. Note the trilineage marrow failure: anemia, thrombocytopenia and "
    "functional neutropenia despite a white count of 87,000, because blasts are non-functional "
    "cells. That is why infection is one of the two things most likely to kill her this week, the "
    "other being hemorrhage.\n\n"
    "Morphology alone does NOT assign lineage — flow cytometry and cytochemistry do. Myeloperoxidase "
    "is the myeloid enzyme (it is the same enzyme that crystallizes into Auer rods, which are "
    "pathognomonic for a myeloid blast when seen). Myeloid blasts also express CD13, CD33 and CD117; "
    "lymphoblasts express TdT with CD19, CD10 and CD20 (B) or CD2, CD3, CD5 and CD7 (T).\n\n"
    "The clinical contrast is worth holding alongside the immunophenotype: acute LYMPHOBLASTIC "
    "leukemia characteristically leaves the marrow and colonizes lymphoid tissue and the meninges — "
    "lymphadenopathy, splenomegaly and central nervous system involvement — which is why its "
    "treatment includes central nervous system prophylaxis. This patient has none of those.\n\n"
    "Initial management is to 'extinguish the fire' before subtyping: transfusion support "
    "(hemoglobin below 7, platelets below 10,000, or below 50,000 if bleeding), identify and treat "
    "infection, and cytoreduce a very high white count with hydroxyurea while the workup proceeds.\n\n"
    "Educational objective: Acute leukemia requires more than 20% blasts in marrow or blood and "
    "presents with trilineage marrow failure even when the total white count is high, because blasts "
    "are non-functional. Lineage is assigned by flow cytometry and cytochemistry — myeloperoxidase "
    "and CD13/CD33/CD117 for myeloid, TdT with CD19/CD10 or CD3 for lymphoid.",
    "Her marrow is packed with immature cells that cannot do any real work, so she is anemic, "
    "bruising and at risk of infection all at once. Looking at them is not enough — a stain for a "
    "myeloid enzyme tells you which family they came from.",
    image="fig_hx_blasts_marrow",
    imcap="Bone marrow biopsy at high power, hematoxylin and eosin, shown at two fields. The marrow "
          "space is filled by a uniform population of large cells with scant cytoplasm, high "
          "nuclear-to-cytoplasmic ratios, finely dispersed chromatin and conspicuous nucleoli; "
          "normal maturing hematopoietic elements are absent.",
    exim="fig_auer_rods",
    excap="A myeloblast containing an Auer rod — fused azurophilic granules, and proof of myeloid "
          "lineage on morphology alone.",
)

# ── 63. Acute promyelocytic leukemia (§37) ──────────────────────────────────────
q(
    "A 46-year-old man is brought to the emergency department due to 5 days of gum bleeding, "
    "nosebleeds and a spreading purpuric rash. Temperature is 37.6 C (99.7 F) and blood pressure is "
    "112/70 mm Hg. He has oozing from a peripheral intravenous site.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.8 g/dL (N=13.5–17.5 g/dL)\n"
    "Leukocyte count 2,900/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 22,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 22 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 51 sec (N=25–40 sec)\n"
    "Fibrinogen 78 mg/dL (N=200–400 mg/dL)\n"
    "D-dimer 8,900 ng/mL (N=less than 250 ng/mL)\n\n"
    "The peripheral smear shows occasional schistocytes and a population of abnormal cells with "
    "heavily granulated cytoplasm, some containing bundles of needle-shaped cytoplasmic inclusions. "
    "Cytogenetic studies are pending. Which of the following is the most appropriate immediate "
    "treatment?",
    {
        "All-trans retinoic acid": "",
        "Cytarabine with an anthracycline":
            "Standard '7 + 3' induction is the backbone for other subtypes of acute myeloid leukemia, "
            "but here it does not address the coagulopathy, which is what kills in the first days.",
        "Hydroxyurea":
            "Hydroxyurea is cytoreduction for an unchecked white count while the workup proceeds. His "
            "white count is LOW, and cytoreduction does nothing for the coagulopathy.",
        "Imatinib":
            "Imatinib targets the BCR-ABL1 tyrosine kinase of chronic myeloid leukemia and "
            "BCR-ABL1-positive lymphoblastic leukemia — a different fusion, and a different disease.",
        "Plasma exchange":
            "Plasma exchange is the emergency treatment of thrombotic thrombocytopenic purpura, where "
            "PT, aPTT and fibrinogen are NORMAL. Here they are all deranged — this is consumption, "
            "not a microangiopathy alone.",
        "Rituximab":
            "Anti-CD20 therapy treats B-cell neoplasms. These are granulated myeloid cells.",
    },
    "All-trans retinoic acid",
    "Acute promyelocytic leukemia (APL) with disseminated intravascular coagulation — the single "
    "highest-yield emergency in the malignancy block.\n\n"
    "Recognition: an acute leukemia whose cells are heavily granulated promyelocytes, some packed "
    "with bundles of Auer rods ('faggot cells'), together with a florid coagulopathy — prolonged PT "
    "and aPTT, low fibrinogen, very high D-dimer, thrombocytopenia and schistocytes. The lesion is "
    "t(15;17), creating the PML-RARA fusion gene.\n\n"
    "Why you cannot wait: patients with unrecognized APL die of HEMORRHAGE, often within days, "
    "before cytogenetics return. So the rule is to start all-trans retinoic acid ON SUSPICION, "
    "alongside aggressive product support for the coagulopathy. The cost of being wrong is small; "
    "the cost of waiting is a fatal bleed.\n\n"
    "Why the drug works, and why it proves the core construct: all-trans retinoic acid is not "
    "cytotoxic. It releases the differentiation block so the arrested promyelocytes MATURE, after "
    "which they die naturally. A drug that cures a leukemia without killing cells is only conceivable "
    "if the disease was a maturation problem in the first place. Recognized and treated, overall "
    "survival is about 90% — the most rapidly lethal leukemia becomes the most curable one.\n\n"
    "Educational objective: Acute promyelocytic leukemia carries t(15;17)/PML-RARA and causes severe "
    "disseminated intravascular coagulation, which is the usual cause of early death. All-trans "
    "retinoic acid, which forces the arrested promyelocytes to differentiate, must be started on "
    "clinical suspicion before cytogenetic confirmation.",
    "His leukemia cells are stuck halfway through growing up, and they leak substances that use up "
    "his clotting proteins, so he bleeds everywhere. The treatment is not a poison — it unfreezes the "
    "cells so they finish maturing and then die naturally.",
    exim="fig_apl_faggot",
    excap="Acute promyelocytic leukemia — heavily granulated promyelocytes, several containing "
          "bundles of Auer rods.",
)

# ── 64. Fitness, not age, decides AML induction (§37) ───────────────────────────
q(
    "A 78-year-old man is diagnosed with acute myeloid leukemia after a bone marrow biopsy shows 42% "
    "myeloblasts. He has heart failure with an ejection fraction of 30%, chronic kidney disease with "
    "a creatinine clearance of 34 mL/min, and requires assistance with bathing and dressing; he "
    "spends more than half of each day in a chair. Cytogenetics show a complex karyotype. His "
    "daughter asks whether he can have 'the strong chemotherapy that cures this'. Which of the "
    "following is the most appropriate treatment?",
    {
        "Allogeneic stem cell transplantation":
            "Transplant is consolidation for intermediate or high risk disease in a patient fit "
            "enough to survive induction first, and it carries substantial treatment-related "
            "mortality. It is not an alternative to induction in an unfit patient.",
        "All-trans retinoic acid":
            "This treats acute PROMYELOCYTIC leukemia, defined by t(15;17). He has a complex "
            "karyotype and no coagulopathy.",
        "Azacitidine with venetoclax": "",
        "Cytarabine infusion with daunorubicin":
            "This is '7 + 3' induction — the curative-intent arm. It requires a 3–4 week "
            "hospitalization through profound marrow aplasia, and an anthracycline in a man with an "
            "ejection fraction of 30% adds cardiotoxicity to that.",
        "Imatinib":
            "A BCR-ABL1 tyrosine kinase inhibitor, for chronic myeloid leukemia and BCR-ABL1-positive "
            "lymphoblastic leukemia.",
        "Observation with transfusion support alone":
            "Pure supportive care is appropriate when a patient declines disease-directed therapy or "
            "is at the end of life. Hypomethylating therapy is generally tolerable and improves "
            "outcomes over transfusions alone.",
    },
    "Azacitidine with venetoclax",
    "Acute myeloid leukemia treated with palliative rather than curative intent — and the decision "
    "turns on FITNESS, not on a birthday.\n\n"
    "The two pathways:\n"
    "• CURATIVE INTENT (younger or fit) — '7 + 3' induction: 7 days of cytarabine plus 3 days of "
    "daunorubicin or idarubicin, requiring at least 3–4 weeks in hospital, then consolidation "
    "chemotherapy, with allogeneic stem cell transplant for intermediate or high risk disease\n"
    "• PALLIATIVE INTENT (older or unfit) — a hypomethylating agent (azacitidine or decitabine) with "
    "or without venetoclax, plus supportive care\n\n"
    "The question to ask is whether the patient can survive a month of marrow aplasia in hospital. "
    "This man cannot: an ejection fraction of 30% (and anthracyclines are cardiotoxic), significant "
    "renal impairment, and a performance status in which he spends more than half the day in a chair "
    "and depends on others for self-care.\n\n"
    "His cytogenetics reinforce the point. Prognosis in acute myeloid leukemia is driven by age, "
    "performance status, comorbidities, prior cytotoxic chemotherapy or radiation, antecedent myeloid "
    "disorders such as myelodysplastic syndrome, and cytogenetic and molecular findings — and a "
    "complex karyotype is adverse risk, the group that does worst with intensive therapy.\n\n"
    "Educational objective: The choice between intensive '7 + 3' induction and a hypomethylating "
    "agent in acute myeloid leukemia is determined by the patient's fitness, performance status and "
    "comorbidities rather than by chronological age, because induction requires surviving 3–4 weeks "
    "of profound marrow aplasia.",
    "The strong chemotherapy empties the bone marrow for about a month, and you have to be well "
    "enough to live through that. With a weak heart and needing help to wash and dress, he is safer "
    "with the gentler tablet-and-injection regimen.",
)

# ── 65. Tumour lysis syndrome (§36) ─────────────────────────────────────────────
q(
    "A 19-year-old man is admitted to the hospital due to a rapidly enlarging abdominal mass, and "
    "biopsy shows a high-grade B-cell lymphoma with a proliferation index above 95%. Chemotherapy is "
    "started. Two days later he becomes oliguric and reports muscle cramps and perioral tingling. "
    "ECG shows peaked T waves.\n\n"
    "Laboratory studies show:\n"
    "Potassium 6.6 mEq/L (N=3.5–5.0 mEq/L)\n"
    "Phosphorus 8.2 mg/dL (N=3.0–4.5 mg/dL)\n"
    "Calcium 6.4 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Uric acid 16.4 mg/dL (N=3.0–8.2 mg/dL)\n"
    "Creatinine 3.1 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Lactate dehydrogenase 2,940 U/L (N=45–200 U/L)\n\n"
    "Prothrombin time, partial thromboplastin time and fibrinogen are normal, and no schistocytes "
    "are seen. Which of the following is the most appropriate agent for this patient's uric acid?",
    {
        "Allopurinol":
            "Allopurinol inhibits xanthine oxidase and so PREVENTS further urate formation, which "
            "makes it the prophylactic agent. It does nothing about the 16.4 mg/dL already "
            "circulating and precipitating in his tubules.",
        "Calcium gluconate":
            "Calcium stabilizes the myocardium against hyperkalemia and may be needed here, but "
            "calcium replacement is used cautiously in tumour lysis because the driver is "
            "hyperphosphatemia — and it does not lower urate.",
        "Cryoprecipitate":
            "Cryoprecipitate replaces fibrinogen in disseminated intravascular coagulation — the "
            "OTHER first-week emergency in acute leukemia. His clotting times and fibrinogen are "
            "normal.",
        "Rasburicase": "",
        "Sodium polystyrene sulfonate":
            "This binds potassium in the gut and is part of managing his hyperkalemia, which is the "
            "arrhythmia risk — but it is not the treatment for hyperuricemia.",
    },
    "Rasburicase",
    "Tumour lysis syndrome — the metabolic emergency of the first week, occurring spontaneously or "
    "on starting treatment in acute leukemias and aggressive lymphomas, Burkitt above all.\n\n"
    "The pattern in one line: everything goes UP except calcium. Massive cell death releases "
    "intracellular contents → potassium up (arrhythmia), phosphate up, uric acid up (renal failure), "
    "and calcium DOWN, because the released phosphate binds and precipitates it. If a stem lists "
    "three highs and one low in a patient starting chemotherapy, this is the diagnosis.\n\n"
    "Treatment by derangement:\n"
    "• Hyperuricemia → allopurinol to PREVENT; rasburicase when urate is already high, because it is "
    "a recombinant urate oxidase that DEGRADES existing urate to allantoin rather than merely "
    "blocking its production\n"
    "• Hyperkalemia → sodium polystyrene sulfonate, with urgent attention to arrhythmia risk\n"
    "• Hyperphosphatemia → binders, and it drives the hypocalcemia\n"
    "• Hypocalcemia → replace only if symptomatic\n"
    "Aggressive intravenous hydration underlies all of it.\n\n"
    "Note the deliberate contrast with the other first-week emergency: disseminated intravascular "
    "coagulation is a COAGULOPATHY (low fibrinogen, prolonged clotting times, schistocytes) and is "
    "most associated with acute promyelocytic leukemia. Tumour lysis is METABOLIC. Both appear in "
    "week one; they are not the same problem.\n\n"
    "Educational objective: Tumour lysis syndrome causes hyperkalemia, hyperphosphatemia and "
    "hyperuricemia with hypocalcemia after treatment of a rapidly proliferating malignancy. "
    "Allopurinol prevents urate formation, whereas rasburicase degrades urate already present and is "
    "used for established severe hyperuricemia.",
    "Killing a huge number of cancer cells at once dumps their insides into the blood. The uric acid "
    "released clogs the kidneys, and this drug chews up the uric acid that is already there instead "
    "of just preventing more.",
)

# ── 66. Myelodysplastic syndrome — what actually kills (§38) ────────────────────
q(
    "A 74-year-old man comes to the office due to 8 months of progressive fatigue. He has required "
    "two red cell transfusions in the past 3 months. He has never received chemotherapy or "
    "radiation. There is no lymphadenopathy or splenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.1 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 25% (N=41%–53%)\n"
    "Mean corpuscular volume 104 µm3 (N=80–100 µm3)\n"
    "Leukocyte count 2,600/mm3 (N=4,500–11,000/mm3)\n"
    "Segmented neutrophils 42% (N=54%–62%)\n"
    "Platelet count 88,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 0.4% (N=0.5%–1.5%)\n"
    "Vitamin B12 620 pg/mL (N=200–900 pg/mL)\n\n"
    "Bone marrow biopsy shows a hypercellular marrow with dysplastic erythroid and granulocytic "
    "precursors, ring sideroblasts on iron staining, and 8% blasts. Which of the following is the "
    "most likely cause of death in this patient?",
    {
        "Overwhelming infection or hemorrhage": "",
        "Hyperviscosity from a paraprotein":
            "This belongs to lymphoplasmacytic lymphoma, where a pentameric IgM thickens the blood — "
            "not to a dysplastic marrow.",
        "Progression to acute myeloid leukemia":
            "This is the feared outcome and it does occur — but in about 30% of patients, making it "
            "the LESS common cause of death. The blast count is what would define transformation: "
            "above 20% makes it acute myeloid leukemia.",
        "Thrombosis from a myeloproliferative neoplasm":
            "Thrombosis is the danger in polycythemia vera and essential thrombocythemia, where the "
            "marrow makes an excess of NORMAL cells. This marrow makes abnormal ones and the patient "
            "is cytopenic.",
        "Transformation to chronic myeloid leukemia":
            "Chronic myeloid leukemia is a distinct disease defined by t(9;22)/BCR-ABL1 and arises de "
            "novo; myelodysplastic syndrome does not turn into it.",
    },
    "Overwhelming infection or hemorrhage",
    "Myelodysplastic syndrome — and its defining paradox is that the marrow is cellular, often "
    "HYPERcellular, while the patient is cytopenic. Production is not reduced; it is WASTED, because "
    "the cells being made are structurally abnormal and die before or shortly after release. That is "
    "why the reticulocyte count is low despite a busy marrow.\n\n"
    "On the map of hematologic malignancy, myelodysplastic syndrome occupies the middle box: not "
    "undifferentiated like acute myeloid leukemia, not normally differentiated like the "
    "myeloproliferative neoplasms, but ABNORMALLY differentiated.\n\n"
    "The outcome data are counterintuitive and examinable: about 50% of patients die of bleeding or "
    "infection — that is, of the cytopenias themselves — while about 30% progress to acute myeloid "
    "leukemia. The feared outcome is the less common one.\n\n"
    "The pathophysiology is EPIGENETIC: genes are silenced by methylation rather than deleted, which "
    "is exactly why hypomethylating agents (azacitidine, decitabine) are the disease-directed "
    "treatment — the same class used for unfit acute myeloid leukemia, which makes sense because the "
    "two sit on one continuum separated by the 20% blast line. Supportive care is transfusions, "
    "growth factors and antibiotics; allogeneic stem cell transplant is the only curative option.\n\n"
    "Educational objective: Myelodysplastic syndrome produces cytopenias despite a hypercellular, "
    "dysplastic marrow because hematopoiesis is ineffective. About half of patients die of infection "
    "or bleeding from the cytopenias and about 30% progress to acute myeloid leukemia, which is "
    "defined by a blast count above 20%.",
    "His bone marrow is full of cells, but they are built wrong and die before they can work. Most "
    "patients with this die of an infection or a bleed from having too few working cells — not from "
    "it turning into leukemia.",
)

# ── 67. Chronic myeloid leukemia versus a leukemoid reaction (§38) ──────────────
q(
    "A 52-year-old woman comes to the office for evaluation of an abnormal blood count found at a "
    "routine visit. She feels well apart from early satiety and mild left upper quadrant fullness. "
    "She has no fever, cough, wounds or recent illness. The spleen is palpable 6 cm below the left "
    "costal margin.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 11.9 g/dL (N=12.0–16.0 g/dL)\n"
    "Leukocyte count 82,000/mm3 (N=4,500–11,000/mm3)\n"
    "Segmented neutrophils 48% (N=54%–62%)\n"
    "Basophils 7% (N=0%–0.75%)\n"
    "Eosinophils 6% (N=1%–3%)\n"
    "Platelet count 612,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "The peripheral smear shows the full spectrum of granulocyte maturation, including myelocytes "
    "and metamyelocytes, with 3% blasts. There is no toxic granulation. Which of the following "
    "additional findings is most likely in this patient?",
    {
        "A leukocyte alkaline phosphatase score that is low": "",
        "A t(15;17) translocation on cytogenetic studies":
            "PML-RARA defines acute promyelocytic leukemia, which presents with a coagulopathy and "
            "abnormal promyelocytes rather than a mature myeloid expansion with splenomegaly.",
        "An elevated erythropoietin concentration":
            "A high erythropoietin points to a SECONDARY erythrocytosis from hypoxia or a tumour. "
            "Her problem is a white cell and platelet expansion, and she is mildly anemic.",
        "Döhle bodies and prominent toxic granulation":
            "These are the reactive changes of a leukemoid reaction — a neutrophil working hard "
            "against a stimulus such as severe infection or tissue necrosis. The stem states there "
            "is no toxic granulation and no trigger.",
        "More than 20% blasts in the bone marrow":
            "That would make this acute leukemia (blast phase), which is a different clinical "
            "picture. Her blast count is 3% and she feels well.",
    },
    "A leukocyte alkaline phosphatase score that is low",
    "Chronic myeloid leukemia. The defining lesion has three names worth knowing together: t(9;22) "
    "is the translocation, BCR-ABL1 is the fusion gene and protein, and the Philadelphia chromosome "
    "is the derivative chromosome 22. The fusion protein is a constitutively active tyrosine kinase "
    "— permanently switched on — which is why a small molecule that blocks its active site works so "
    "well.\n\n"
    "Distinguishing it from a leukemoid reaction, which also produces a striking neutrophilia:\n"
    "• BCR-ABL1 — POSITIVE, and the definitive test; negative in a leukemoid reaction\n"
    "• BASOPHILIA — present, and the distinctive finding, since few other conditions raise basophils; "
    "absent in reactive states\n"
    "• Eosinophilia — present; absent\n"
    "• Trigger — none, because this is a clonal neoplasm; a leukemoid reaction has a driving "
    "stimulus (severe infection, inflammation, tissue necrosis, corticosteroids)\n"
    "• Spleen — enlarged; usually normal\n"
    "• Smear — the whole myeloid series at all maturation stages including blasts; versus mature "
    "neutrophils with toxic granulation and Döhle bodies\n"
    "• LEUKOCYTE ALKALINE PHOSPHATASE — LOW in chronic myeloid leukemia, HIGH in a leukemoid reaction\n\n"
    "Phases matter and turn on two numbers that both sit near 20: blasts of 10%–19% or basophils of "
    "20% or more indicate ACCELERATED phase, while more than 20% BLASTS means BLAST phase — it has "
    "become an acute leukemia. Read the cell type before the number.\n\n"
    "Treatment transformed this disease: median survival was 2–5 years before tyrosine kinase "
    "inhibitors and is now about 95% alive at 10 years with imatinib and its successors.\n\n"
    "Educational objective: Chronic myeloid leukemia is driven by t(9;22)/BCR-ABL1 and presents with "
    "a mature myeloid leukocytosis, basophilia, eosinophilia, thrombocytosis and splenomegaly, with a "
    "LOW leukocyte alkaline phosphatase. A leukemoid reaction has a driving stimulus, toxic "
    "granulation, no basophilia and a HIGH leukocyte alkaline phosphatase.",
    "Her bone marrow has a stuck-on switch that makes it churn out white cells non-stop. A reaction "
    "to infection looks similar, but the cells here are a cancer clone — they lack an enzyme that "
    "hard-working normal neutrophils have plenty of.",
    exim="fig_slide_granulocyte_series",
    excap="The granulocyte maturation series — chronic myeloid leukemia puts the whole spectrum into "
          "the blood, whereas a reactive left shift keeps the normal proportions.",
)

# ── 68. The T315I gatekeeper mutation (§38) ─────────────────────────────────────
q(
    "A 44-year-old man with chronic myeloid leukemia has taken imatinib for 3 years with an "
    "excellent molecular response and no missed doses. Over the past 4 months his BCR-ABL1 "
    "transcript level has risen on three successive measurements, his white cell count has increased "
    "from 6,200/mm3 to 28,000/mm3, and his spleen is again palpable. Mutational analysis of the "
    "BCR-ABL1 kinase domain identifies a T315I substitution. Marrow blasts are 4%. Which of the "
    "following is the most appropriate next treatment?",
    {
        "Azacitidine":
            "A hypomethylating agent for myelodysplastic syndrome and for acute myeloid leukemia in "
            "unfit patients. It does not target BCR-ABL1.",
        "Dasatinib":
            "A second-generation tyrosine kinase inhibitor that overcomes many imatinib-resistant "
            "mutations — but not T315I, which is precisely the gatekeeper substitution that blocks "
            "this whole generation.",
        "Hydroxyurea alone":
            "Hydroxyurea lowers the white count without touching the driver mutation. It is "
            "cytoreduction while a plan is made, not a treatment for resistant disease.",
        "Nilotinib":
            "Also second generation, and also blocked by T315I. Switching within a generation that "
            "the mutation defeats will not restore response.",
        "Ponatinib": "",
        "Rituximab":
            "An anti-CD20 antibody for B-cell neoplasms. Chronic myeloid leukemia is a myeloid "
            "disease and does not express CD20.",
    },
    "Ponatinib",
    "Acquired resistance to imatinib through the T315I gatekeeper mutation.\n\n"
    "Tyrosine kinase inhibitors work by occupying the ATP-binding pocket of the constitutively active "
    "BCR-ABL1 kinase. The threonine at position 315 sits at the entrance to that pocket — the "
    "'gatekeeper' residue. Substituting isoleucine both removes a hydrogen bond the drugs depend on "
    "and adds bulk that sterically blocks the pocket, so imatinib and the second-generation agents "
    "(nilotinib, dasatinib, bosutinib) can no longer bind.\n\n"
    "The agents that retain activity against T315I are ponatinib and omacetaxine. Switching within "
    "the earlier generations is the trap.\n\n"
    "Read the rest of the case as a monitoring lesson: a rising BCR-ABL1 transcript on serial "
    "measurement in an adherent patient is how resistance declares itself, before the counts move and "
    "well before blast phase. He remains in chronic phase (blasts under 10%), which is where you want "
    "to intervene — accelerated phase is defined by 10%–19% blasts or 20% or more basophils, and "
    "blast phase by more than 20% blasts.\n\n"
    "Note also what a deep and durable response makes possible: selected patients in sustained deep "
    "molecular remission can attempt treatment-free remission under close monitoring.\n\n"
    "Educational objective: The T315I gatekeeper mutation of BCR-ABL1 confers resistance to imatinib "
    "and to the second-generation tyrosine kinase inhibitors; ponatinib or omacetaxine is required. "
    "A rising BCR-ABL1 transcript level in an adherent patient is the earliest sign of resistance.",
    "His tablet works by plugging a specific keyhole in the cancer protein. The cancer changed the "
    "shape of the keyhole, so that key and its close cousins no longer fit — he needs the one drug "
    "built for the new shape.",
)

# ── 69. Polycythemia vera (§39) ─────────────────────────────────────────────────
q(
    "A 58-year-old man comes to the office due to 6 months of intense itching that begins within "
    "minutes of a hot shower and lasts about an hour, along with episodes of burning pain and "
    "redness in both hands and feet. He also reports headaches and a feeling of fullness after small "
    "meals. He has never smoked and has no cardiopulmonary disease. Oxygen saturation is 98% on room "
    "air. The spleen is palpable 4 cm below the costal margin.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 19.8 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 59% (N=41%–53%)\n"
    "Leukocyte count 13,400/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 588,000/mm3 (N=150,000–400,000/mm3)\n"
    "Erythropoietin 2 mU/mL (N=4–26 mU/mL)\n\n"
    "Testing for the JAK2 V617F mutation is positive. Which of the following is the most appropriate "
    "initial treatment?",
    {
        "Eculizumab":
            "An anti-C5 complement inhibitor, used in atypical hemolytic uremic syndrome and "
            "paroxysmal nocturnal hemoglobinuria. It has no role here.",
        "Imatinib":
            "Targets BCR-ABL1, which defines chronic myeloid leukemia. This is a JAK2-driven "
            "myeloproliferative neoplasm.",
        "Intravenous iron":
            "Repeated phlebotomy will make him iron deficient, and that iron restriction is part of "
            "how the treatment limits red cell production. Replacing iron works against the therapy.",
        "Ruxolitinib":
            "A JAK inhibitor, reserved for disease refractory to standard measures — and the agent "
            "that improves symptoms and survival in high-risk myelofibrosis. It is not the initial "
            "step here.",
        "Supplemental oxygen":
            "This treats a SECONDARY erythrocytosis from hypoxia, in which the erythropoietin level "
            "is HIGH. His saturation is 98% and his erythropoietin is suppressed.",
        "Therapeutic phlebotomy": "",
    },
    "Therapeutic phlebotomy",
    "Polycythemia vera. Two features make it recognizable at the bedside: AQUAGENIC PRURITUS — "
    "itching triggered by contact with water, classically after a hot shower — and ERYTHROMELALGIA, "
    "episodic burning pain with redness and warmth in the extremities. Add headaches from "
    "hyperviscosity, splenomegaly, and a raised white count and platelet count alongside the raised "
    "hematocrit.\n\n"
    "The single most useful laboratory discriminator is the erythropoietin level: it is SUPPRESSED in "
    "polycythemia vera, because the marrow is driving itself through constitutive JAK2/STAT "
    "signalling, and ELEVATED in secondary erythrocytosis from hypoxia, renal disease or an "
    "erythropoietin-secreting tumour.\n\n"
    "Initial treatment is therapeutic phlebotomy to a target hematocrit below 45 in men (below 42 in "
    "women), plus low-dose aspirin. Hydroxyurea is added for higher-risk patients — prior thrombosis, "
    "age over 60, white cells above 11,000, hematocrit above 45, platelets above 400,000 — and "
    "ruxolitinib is for refractory disease.\n\n"
    "The shared danger of the myeloproliferative neoplasms is THROMBOSIS rather than marrow failure, "
    "because the cells produced are normal, mature and functional — just far too many. These are "
    "among the few hematologic conditions causing arterial as well as venous events, which is why a "
    "myocardial infarction or stroke in a young person with a high hematocrit should prompt the "
    "thought, and why JAK2 testing belongs in the workup of an unexplained splanchnic vein "
    "thrombosis. Long term, about 10% progress to post-polycythemia vera myelofibrosis and about 1% "
    "to acute myeloid leukemia.\n\n"
    "Educational objective: Polycythemia vera is a JAK2-driven myeloproliferative neoplasm with a "
    "raised hematocrit and a SUPPRESSED erythropoietin level, presenting with aquagenic pruritus, "
    "erythromelalgia and thrombosis. Initial treatment is phlebotomy to a hematocrit below 45 in men, "
    "plus aspirin.",
    "His marrow has a stuck-on growth switch and makes far too many red cells, so his blood is thick "
    "and clots easily. The first treatment is simply to remove blood regularly until it thins out.",
    exim="fig_slide_maturation_tree",
    excap="Where the myeloproliferative neoplasms sit — normally differentiated cells produced in "
          "excess, so the danger is thrombosis rather than marrow failure.",
)

# ── 70. Primary myelofibrosis (§39) ─────────────────────────────────────────────
q(
    "A 69-year-old woman comes to the office due to 9 months of fatigue, drenching night sweats, "
    "bone pain and 9 kg of weight loss. Examination shows a firm spleen palpable 12 cm below the "
    "left costal margin. There is no lymphadenopathy.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.3 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 25% (N=36%–46%)\n"
    "Leukocyte count 3,100/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 74,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "The peripheral smear is shown. Attempted bone marrow aspiration yields no material. Which of "
    "the following is most likely to be found on the core biopsy?",
    {
        "Dense reticulin and collagen fibrosis": "",
        "Fatty replacement with absent hematopoietic cells":
            "An empty, fatty marrow is aplastic anemia — which also gives pancytopenia, but without "
            "massive splenomegaly, tear-drop cells or a leukoerythroblastic smear.",
        "Granulomas containing acid-fast organisms":
            "Disseminated mycobacterial infection can infiltrate marrow and cause cytopenias, but the "
            "smear findings here point to mechanical distortion of the marrow architecture.",
        "Ring sideroblasts with dysplastic precursors":
            "This is myelodysplastic syndrome, which produces cytopenias from ineffective "
            "hematopoiesis — but the marrow aspirates readily and the spleen is not massively "
            "enlarged.",
        "Sheets of plasma cells replacing the marrow":
            "Myeloma occupies the marrow and causes anemia, but with lytic bone lesions, "
            "hypercalcemia, renal impairment and a monoclonal protein rather than this smear.",
        "Sheets of myeloblasts exceeding 20% of cells":
            "That defines acute leukemia. Blasts are not the dominant finding on this smear, and the "
            "tempo has been 9 months.",
    },
    "Dense reticulin and collagen fibrosis",
    "Primary myelofibrosis — the myeloproliferative neoplasm that ends in marrow failure.\n\n"
    "Every element of the case follows from fibrous replacement of the marrow:\n"
    "• The DRY TAP — no material aspirates from a fibrotic marrow, so the core biopsy is what makes "
    "the diagnosis\n"
    "• The LEUKOERYTHROBLASTIC smear — immature granulocytes plus nucleated red cells, forced out of "
    "a marrow whose architecture is disturbed\n"
    "• TEAR-DROP cells (dacryocytes) — red cells mechanically distorted as they squeeze out of a "
    "scarred marrow\n"
    "• PANCYTOPENIA — the marrow eventually stops producing\n"
    "• MASSIVE SPLENOMEGALY — extramedullary hematopoiesis, the body reopening a fetal site under "
    "extreme demand\n"
    "• The symptom burden itself — bone pain, night sweats, weight loss — which is a treatment "
    "indication in its own right\n\n"
    "Like polycythemia vera and essential thrombocythemia it is driven through the JAK2/STAT "
    "pathway, but unlike them it ends in failure rather than excess. Ruxolitinib is used for "
    "intermediate-2 and high risk disease and improves symptoms AND survival — but it does NOT "
    "improve the cytopenias, which is the examinable caveat. Allogeneic stem cell transplant is the "
    "only curative-intent treatment.\n\n"
    "Educational objective: Primary myelofibrosis replaces the marrow with fibrous tissue, producing "
    "a dry tap, a leukoerythroblastic smear with tear-drop red cells, pancytopenia and massive "
    "splenomegaly from extramedullary hematopoiesis. Ruxolitinib improves symptoms and survival but "
    "not the cytopenias; only transplant is curative.",
    "Scar tissue is slowly taking over her bone marrow, so the needle draws nothing and blood cells "
    "get squeezed out misshapen. Her spleen has taken over blood production, which is why it is "
    "enormous.",
    image="fig_hx_leukoerythroblastic",
    imcap="Peripheral blood smear. Immature granulocytes at several stages of maturation are present "
          "(triangle), together with a nucleated red cell (square) and erythrocytes drawn out into a "
          "tear-drop shape with a single pointed end (diamond).",
    exim="fig_teardrop",
    excap="A tear-drop erythrocyte — mechanical distortion as the cell exits a scarred marrow.",
)

# ── 71. Acute lymphoblastic leukemia and the sanctuary site (§40) ───────────────
q(
    "A 4-year-old girl is brought to the emergency department by her parents due to 3 weeks of leg "
    "pain that wakes her at night, pallor and fever. Examination shows cervical and axillary "
    "lymphadenopathy, a spleen palpable 5 cm below the costal margin, and tenderness over both "
    "tibiae.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.4 g/dL (N=11.5–15.5 g/dL)\n"
    "Leukocyte count 42,000/mm3 (N=4,500–13,500/mm3)\n"
    "Platelet count 38,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "The peripheral smear is shown. Flow cytometry of the marrow shows cells expressing CD19, CD10 "
    "and terminal deoxynucleotidyl transferase, and cytogenetics show hyperdiploidy. In addition to "
    "systemic chemotherapy, which of the following is required in the treatment of this patient?",
    {
        "All-trans retinoic acid":
            "Differentiation therapy for acute promyelocytic leukemia, defined by t(15;17). These "
            "blasts are lymphoid.",
        "Intrathecal chemotherapy": "",
        "Plasma exchange":
            "Plasma exchange treats thrombotic thrombocytopenic purpura and IgM hyperviscosity. "
            "Neither applies.",
        "Splenectomy":
            "Splenomegaly here reflects leukemic infiltration and resolves with treatment of the "
            "disease. Splenectomy has no role.",
        "Therapeutic phlebotomy":
            "Phlebotomy lowers the hematocrit in polycythemia vera. She is anemic.",
        "Upfront allogeneic stem cell transplantation":
            "Transplant is reserved for high-risk or relapsed disease. She has several favourable "
            "features, and standard chemotherapy cures over 90% of children.",
    },
    "Intrathecal chemotherapy",
    "Acute lymphoblastic leukemia — the most common childhood malignancy, with a bimodal peak at 2–5 "
    "years and again over 50. About 85% is precursor B-cell (CD19, CD10 and TdT positive, as here) "
    "and 15% T-cell.\n\n"
    "What distinguishes it clinically from acute myeloid leukemia is that the disease LEAVES the "
    "marrow: lymphadenopathy, splenomegaly and central nervous system involvement. The bone pain "
    "waking a child at night comes from marrow expansion.\n\n"
    "The central nervous system is a pharmacologic SANCTUARY SITE — systemic chemotherapy does not "
    "reliably cross the blood-brain barrier, so leukemic cells there survive treatment that clears "
    "the marrow and then seed a relapse. Every patient therefore receives central nervous system "
    "prophylaxis with intrathecal chemotherapy, historically alongside cranial irradiation.\n\n"
    "Her prognostic features are favourable: age 2–5 years (the peak incidence group does best), a "
    "precursor-B immunophenotype and hyperdiploidy. Overall survival exceeds 90% in children, against "
    "50%–70% in adolescents and young adults and about 30% in older adults — the same disease name "
    "behaving as three different diseases, largely because adult disease is enriched for adverse "
    "cytogenetics such as BCR-ABL1.\n\n"
    "Total treatment duration is roughly 2.5 years: induction, consolidation (which clears sanctuary "
    "sites), interim maintenance, delayed intensification and about 18 months of maintenance.\n\n"
    "Educational objective: Acute lymphoblastic leukemia colonizes lymphoid tissue and the meninges, "
    "and the central nervous system is a sanctuary site that systemic chemotherapy penetrates poorly, "
    "so intrathecal chemotherapy is required in every patient. Age 2–10 years, precursor-B "
    "phenotype and hyperdiploidy are favourable prognostic features.",
    "Her leukemia hides in the fluid around the brain and spinal cord, where medicine given into a "
    "vein cannot reach well. So a small dose is injected directly into that fluid to stop the "
    "leukemia coming back from there.",
    image="fig_all_lymphoblasts",
    imcap="Peripheral blood smear: numerous large cells with scant cytoplasm, fine open chromatin and "
          "no cytoplasmic granules, among a reduced number of erythrocytes.",
)

# ── 72. Prognostic factors in childhood leukemia (§40, §51) ─────────────────────
q(
    "A 6-year-old boy is diagnosed with precursor B-cell acute lymphoblastic leukemia. His "
    "presenting leukocyte count is 9,000/mm3, cerebrospinal fluid examination shows no blasts, and "
    "marrow blasts have cleared to under 1% by day 8 of induction. His parents are told that most "
    "children with this disease are cured. Which of the following additional findings would most "
    "strongly worsen this patient's prognosis?",
    {
        "Age of 4 years at diagnosis":
            "Age 2–10 years is FAVOURABLE, and the peak incidence group at about 4 years does best "
            "of all. Infancy and adolescence are the unfavourable ends.",
        "A hyperdiploid karyotype with 55 chromosomes":
            "Hyperdiploidy (51–65 chromosomes) is a favourable finding. Hypodiploidy — 43 or fewer — "
            "is the adverse counterpart.",
        "A t(12;21) ETV6-RUNX1 rearrangement":
            "This is the classic FAVOURABLE translocation of childhood acute lymphoblastic leukemia.",
        "A t(9;22) BCR-ABL1 rearrangement": "",
        "Expression of CD19 and CD10 on blasts":
            "This is the precursor-B immunophenotype he already has, and precursor-B disease is "
            "favourable compared with T-cell disease.",
    },
    "A t(9;22) BCR-ABL1 rearrangement",
    "The Philadelphia chromosome is the single finding that would move an otherwise favourable child "
    "into a high-intensity, transplant-directed protocol.\n\n"
    "The prognostic table for childhood acute lymphoblastic leukemia:\n"
    "• AGE — favourable 2–10 years; unfavourable under 1 year, or adolescent and adult\n"
    "• IMMUNOPHENOTYPE — favourable precursor B; unfavourable precursor T\n"
    "• PLOIDY — favourable hyperdiploid (51–65 chromosomes); unfavourable hypodiploid (43 or fewer)\n"
    "• TRANSLOCATION — favourable t(12;21) ETV6-RUNX1; unfavourable t(9;22) BCR-ABL1 and t(1;19) "
    "TCF3-PBX1\n"
    "• PRESENTING WHITE COUNT — favourable low; unfavourable high\n"
    "• CENTRAL NERVOUS SYSTEM — favourable not involved; unfavourable involved at diagnosis\n"
    "• EARLY RESPONSE — favourable rapid blast clearance, for example by day 8 of induction; "
    "unfavourable a slow early response with persistent measurable residual disease\n\n"
    "This boy has five favourable features already, which is why the conversation with his parents is "
    "an optimistic one. Note the modern coda: BCR-ABL1-positive disease, historically the "
    "worst-prognosis group, is now treated by ADDING an oral tyrosine kinase inhibitor to "
    "chemotherapy — the same targeted principle that transformed chronic myeloid leukemia.\n\n"
    "Risk-based treatment follows directly: favourable features get standard-intensity chemotherapy, "
    "adverse features get intensified therapy and consideration of transplant.\n\n"
    "Educational objective: In childhood acute lymphoblastic leukemia, age 2–10 years, precursor-B "
    "phenotype, hyperdiploidy, t(12;21), a low presenting white count, absent central nervous system "
    "disease and rapid early response are favourable; t(9;22) BCR-ABL1, hypodiploidy, T-cell disease, "
    "a high white count, CNS involvement and slow response are adverse.",
    "Doctors sort childhood leukemia into risk groups using age, the type of cell, and which "
    "chromosome swaps are present. One particular swap, the Philadelphia chromosome, moves a child "
    "straight into the hardest-to-treat group.",
)

# ── 73. Nodular sclerosis versus mixed cellularity Hodgkin lymphoma (§41) ───────
q(
    "A 23-year-old woman comes to the office due to 2 months of a painless lump above her left "
    "collarbone and a persistent dry cough. She has had drenching night sweats. Chest radiography "
    "shows a large anterior mediastinal mass. An excisional supraclavicular lymph node biopsy is "
    "shown. Scattered large cells with abundant pale cytoplasm lie within clear spaces, and "
    "immunostaining shows these cells are CD30 and CD15 positive, CD45 negative, and PAX5 weakly "
    "positive relative to background B cells. Which of the following features distinguishes this "
    "subtype of Hodgkin lymphoma from mixed cellularity disease?",
    {
        "Absence of Epstein-Barr virus in the malignant cells":
            "Epstein-Barr virus is associated with about half of Hodgkin lymphoma overall and "
            "particularly with the lymphocyte-depleted subtype. Its presence or absence does not "
            "define nodular sclerosis.",
        "Broad bands of collagen dividing the node": "",
        "Expression of CD30 by the malignant cells":
            "CD30 is strongly and uniformly positive in ALL subtypes of classic Hodgkin lymphoma — "
            "which is why it is both the diagnostic marker and the target of brentuximab vedotin.",
        "Numerous eosinophils in the background":
            "A polymorphous background including eosinophils occurs in both subtypes and is "
            "characteristic of mixed cellularity in particular.",
        "Preservation of the B-cell program in the malignant cells":
            "Classic Hodgkin cells of every subtype have LOST their B-cell program — that is why "
            "PAX5 is weak and CD20 negative. Retention of the program characterizes nodular "
            "lymphocyte predominant disease, a separate entity.",
        "Presence of binucleate Reed-Sternberg cells":
            "Reed-Sternberg cells and their variants define classic Hodgkin lymphoma as a whole; "
            "mixed cellularity in fact contains many typical ones.",
    },
    "Broad bands of collagen dividing the node",
    "Nodular sclerosis classic Hodgkin lymphoma — the commonest subtype, and the one that fits this "
    "patient exactly: a young adult woman with supraclavicular nodes and a mediastinal mass.\n\n"
    "All four classic subtypes share the same neoplastic cell and the same immunophenotype. What "
    "differs is who gets it, how much background inflammation there is, how many Reed-Sternberg "
    "cells are present, and whether there is FIBROSIS:\n"
    "• NODULAR SCLEROSIS — young adults, equal sex ratio, early stage; numerous lacunar cells (the "
    "clear space around each cell is retraction artifact); BROAD COLLAGEN BANDS; excellent prognosis\n"
    "• LYMPHOCYTE-RICH — background largely small lymphocytes; good prognosis\n"
    "• MIXED CELLULARITY — males, elderly, higher stage; many typical Reed-Sternberg cells; NO "
    "collagen bands, which is the key separation; more aggressive\n"
    "• LYMPHOCYTE-DEPLETED — males, elderly, HIV-associated; sparse background; poor prognosis\n\n"
    "The immunophenotype in the stem is the classic Hodgkin signature: CD30 positive (strong, "
    "membranous with Golgi accentuation), CD15 positive in about 75%, CD45 negative, and PAX5 WEAK "
    "compared with the background B cells, which act as a built-in positive control.\n\n"
    "Two practical points: diagnosis requires an EXCISIONAL biopsy, because Reed-Sternberg cells are "
    "only 1%–2% of the tissue and the surrounding architecture is part of the diagnosis; and staging "
    "uses PET/CT plus an erythrocyte sedimentation rate, which is unusual as a staging element. "
    "Treatment is ABVD, with brentuximab vedotin (anti-CD30) or a PD-1 antibody at relapse.\n\n"
    "Educational objective: Nodular sclerosis classic Hodgkin lymphoma is defined by broad collagen "
    "bands dividing the node into nodules, with lacunar cells, in young adults with mediastinal "
    "disease; mixed cellularity shares the CD30-positive, PAX5-weak immunophenotype but lacks the "
    "fibrous bands and occurs in older men at higher stage.",
    "All the Hodgkin types have the same cancer cell, so the difference is what surrounds it. In this "
    "one, thick ropes of scar tissue carve the lymph node into islands.",
    image="fig_lpd_nodular_sclerosis_lowpower",
    imcap="Lymph node at low power, hematoxylin and eosin: thick pink fibrous bands separate the "
          "darkly staining lymphoid tissue into discrete rounded nodules.",
    exim="fig_lpd_reed_sternberg_cell",
    excap="The Reed-Sternberg cell — binucleate, with cherry-red macronucleoli and a perinuclear "
          "halo.",
)

# ── 74. Why rituximab does not work in classic Hodgkin lymphoma (§41) ───────────
q(
    "A 31-year-old man is diagnosed with classic Hodgkin lymphoma after an excisional cervical lymph "
    "node biopsy. A high-power field is shown: scattered very large cells with bilobed nuclei and "
    "prominent eosinophilic nucleoli lie in a mixed background of small lymphocytes, plasma cells, "
    "eosinophils and histiocytes. Immunostaining of the large cells shows CD30 strongly positive, "
    "CD15 positive, CD45 negative, CD20 negative, OCT2 negative and PAX5 weakly positive. His "
    "brother, who has diffuse large B-cell lymphoma, receives rituximab, and he asks why his own "
    "treatment does not include it. Which of the following best explains this?",
    {
        "The malignant cells are of T-cell rather than B-cell origin":
            "Reed-Sternberg cells are of B-cell LINEAGE — the weak PAX5 proves it. The point is that "
            "they no longer express the B-cell program, not that they came from a T cell.",
        "The malignant cells have silenced their B-cell program": "",
        "The malignant cells are too few to be targeted effectively":
            "Reed-Sternberg cells genuinely are only 1%–2% of the tissue — but brentuximab vedotin "
            "targets those same rare cells through CD30 and works well, so rarity is not the reason.",
        "The malignant cells are protected by surrounding fibrosis":
            "Collagen bands define the nodular sclerosis subtype but do not shield cells from a "
            "circulating antibody.",
        "The malignant cells express CD30 instead of CD45":
            "Both statements are true of the immunophenotype, but CD45 is a pan-hematopoietic marker "
            "and is not a therapeutic target; its loss is not why an anti-CD20 antibody fails.",
    },
    "The malignant cells have silenced their B-cell program",
    "Rituximab is an anti-CD20 antibody, and classic Hodgkin cells do not express CD20.\n\n"
    "The mechanism is the most elegant fact in this section: Reed-Sternberg and Hodgkin cells ARE of "
    "B-cell lineage, but they express B-cell repressors and silence their B-cell differentiation "
    "genes. The result is a cell that has abandoned its own identity — and the immunostain panel is "
    "designed to detect exactly that loss:\n"
    "• CD19, CD20, CD79a — NEGATIVE despite B-cell origin, which is why rituximab does not work\n"
    "• PAX5 — WEAK, not absent; the background small B cells are the built-in comparison, and that "
    "comparison is the most helpful single clue\n"
    "• OCT2 and BOB1 — negative\n"
    "• CD45 — typically negative, which separates classic Hodgkin lymphoma from non-Hodgkin B-cell "
    "lymphoma and from nodular lymphocyte predominant disease, both of which retain it\n"
    "• CD30 — strongly positive, and both diagnostic and therapeutic (brentuximab vedotin is an "
    "anti-CD30 antibody-drug conjugate)\n"
    "• CD15 — positive in about 75%\n"
    "• ALK1 — negative, which excludes ALK-positive anaplastic large cell lymphoma, the other "
    "CD30-positive lymphoma\n\n"
    "Contrast nodular lymphocyte predominant disease, increasingly called nodular lymphocyte "
    "predominant B-cell lymphoma precisely because it RETAINS the full B-cell program — and is "
    "therefore a rituximab target.\n\n"
    "The other reason immunotherapy works so well here: the tumour is mostly reactive infiltrate and "
    "is unusually dependent on evading the surrounding immune cells, which is why PD-1 blockade is "
    "exceptionally effective in Hodgkin lymphoma compared with most cancers.\n\n"
    "Educational objective: Reed-Sternberg cells are B cells that have silenced their B-cell program, "
    "so they are CD20, CD79a and OCT2 negative with weak PAX5 — which is why rituximab is "
    "ineffective in classic Hodgkin lymphoma. CD30 positivity makes brentuximab vedotin the "
    "antibody-directed option instead.",
    "His brother's cancer cells still wear the badge that the antibody drug grabs onto. Hodgkin cells "
    "started as the same kind of cell but threw that badge away, so the drug has nothing to hold.",
    image="fig_hx_rs_cell",
    imcap="Lymph node at high power, hematoxylin and eosin. A single very large cell with abundant "
          "pale cytoplasm and a bilobed nucleus containing prominent round eosinophilic nucleoli "
          "(arrow) sits among a mixed population of small lymphocytes, plasma cells and histiocytes; "
          "dense small lymphocytes fill the upper left.",
    exim="fig_lpd_chl_pax5",
    excap="PAX5 staining — the large malignant cells are visibly weaker than the dark background B "
          "cells, and that comparison is the diagnosis.",
)

# ── 75. Burkitt versus follicular lymphoma (§41) ────────────────────────────────
q(
    "A 9-year-old boy is brought to the emergency department due to 3 weeks of abdominal distension "
    "and vomiting. Computed tomography shows a large mass involving the ileocecal region and omental "
    "nodules. Biopsy is shown: a dense monotonous sheet of intermediate-sized cells with numerous "
    "mitotic figures, interrupted by evenly spaced pale macrophages containing cellular debris. The "
    "cells are CD20 positive, CD10 positive, BCL6 positive and BCL2 NEGATIVE, and the Ki-67 "
    "proliferation index is 99%. Which of the following best explains the accumulation of malignant "
    "cells in this patient?",
    {
        "Constitutive activation of a tyrosine kinase":
            "A constitutively active kinase drives chronic myeloid leukemia through BCR-ABL1 and the "
            "myeloproliferative neoplasms through JAK2 — myeloid diseases, and neither produces this "
            "histology.",
        "Failure of apoptosis from BCL2 overexpression":
            "This is follicular lymphoma, whose t(14;18) forces the anti-apoptotic BCL2 gene on so "
            "the cells cannot die. It is the mirror image of this case — and this tumour is "
            "explicitly BCL2 NEGATIVE.",
        "Loss of the B-cell differentiation program":
            "Silencing of the B-cell program characterizes the Reed-Sternberg cells of classic "
            "Hodgkin lymphoma. These cells are CD20 positive, so their program is intact.",
        "Massive proliferation driven by MYC translocation": "",
        "Sequestration of mature lymphocytes in tissue":
            "Accumulation of long-lived mature lymphocytes in blood, marrow and nodes describes "
            "chronic lymphocytic leukemia, which is CD5 positive and indolent.",
    },
    "Massive proliferation driven by MYC translocation",
    "Burkitt lymphoma — the fastest-growing tumour in this block. The sporadic (non-endemic) form "
    "presents in the ABDOMEN, often as an ileocecal or omental mass, and can cause intussusception "
    "or volvulus; the endemic, Epstein-Barr virus-associated form presents as a JAW mass in a child "
    "in equatorial Africa; the immunodeficiency-associated form (HIV) presents nodally.\n\n"
    "The histology is the STARRY SKY: a dark monotonous sheet of cells punctuated by pale tingible "
    "body macrophages clearing the debris of cells dying as fast as they are made. Ki-67 above 95% "
    "means essentially every cell is cycling.\n\n"
    "The contrast to hold is with follicular lymphoma, because both are germinal centre-derived "
    "(CD10 positive, BCL6 positive) yet behave in opposite ways:\n"
    "• BURKITT — t(8;14), MYC under the immunoglobulin heavy chain promoter → furious PROLIFERATION. "
    "BCL2 NEGATIVE. Aggressive, and curable\n"
    "• FOLLICULAR — t(14;18), BCL2 under the same promoter → failed APOPTOSIS. BCL2 POSITIVE. "
    "Indolent, and not curable\n\n"
    "Grow-fast versus die-slow. Both translocations exploit the same accident — the germinal centre B "
    "cell deliberately breaks and rejoins DNA at the immunoglobulin loci during class switching and "
    "somatic hypermutation, and an error can place an oncogene under that hyperactive promoter. The "
    "same mechanism explains t(11;14) cyclin D1 in mantle cell lymphoma.\n\n"
    "Clinically, the enormous turnover means tumour lysis syndrome is expected on treatment — the "
    "same property that makes the disease curable (90% in children, 60%–70% in adults).\n\n"
    "Educational objective: Burkitt lymphoma is a germinal centre-derived B-cell neoplasm with "
    "t(8;14) placing MYC under the immunoglobulin heavy chain promoter, giving a starry-sky pattern "
    "and a Ki-67 above 95%; it is BCL2 negative, in contrast to follicular lymphoma, where t(14;18) "
    "forces BCL2 on and cells accumulate because they cannot die.",
    "Two lymphomas start in the same place but fail in opposite ways: one piles up because its cells "
    "refuse to die, and this one piles up because its cells divide furiously. The 'starry sky' is the "
    "cleanup crew eating the cells that die from the sheer speed.",
    image="fig_lpd_burkitt_starry_sky",
    imcap="Biopsy at medium power, hematoxylin and eosin: a dense monotonous sheet of "
          "intermediate-sized dark cells interrupted by numerous evenly spaced pale cells containing "
          "cellular debris.",
)

# ── 76. Autoimmune hemolysis complicating CLL (§41) ─────────────────────────────
q(
    "A 68-year-old man with chronic lymphocytic leukemia diagnosed 3 years ago comes to the office "
    "due to 4 weeks of increasing fatigue and yellow eyes. He has never required treatment and has "
    "had a stable lymphocyte count. He takes no medications. Examination shows scleral icterus and "
    "small mobile cervical nodes unchanged from previous visits.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.6 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 23% (N=41%–53%)\n"
    "Mean corpuscular volume 99 µm3 (N=80–100 µm3)\n"
    "Leukocyte count 64,000/mm3 (N=4,500–11,000/mm3)\n"
    "Lymphocytes 88% (N=25%–33%)\n"
    "Platelet count 186,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 9.2% (N=0.5%–1.5%)\n"
    "Lactate dehydrogenase 680 U/L (N=45–200 U/L)\n"
    "Haptoglobin less than 10 mg/dL (N=41–165 mg/dL)\n"
    "Bilirubin, total 3.4 mg/dL (N=0.1–1.0 mg/dL)\n\n"
    "The smear shows numerous small mature lymphocytes, smudge cells, spherocytes and "
    "polychromasia. Which of the following is the most appropriate next diagnostic test?",
    {
        "Bone marrow biopsy":
            "A marrow would show lymphocytic infiltration that is already known, and it cannot "
            "explain a reticulocyte count of 9.2% — marrow replacement suppresses the reticulocyte "
            "response rather than driving it.",
        "Direct antiglobulin test": "",
        "Serum erythropoietin level":
            "Useful for separating polycythemia vera from secondary erythrocytosis, not for "
            "investigating anemia with brisk reticulocytosis.",
        "Serum protein electrophoresis":
            "This detects a monoclonal protein in plasma cell disorders. It would not explain "
            "spherocytes with a raised lactate dehydrogenase and an undetectable haptoglobin.",
        "Serum vitamin B12 and folate":
            "The mean corpuscular volume is at the upper limit because of the reticulocytosis, not "
            "because of megaloblastic change — hypersegmented neutrophils are absent and the "
            "reticulocyte count is high.",
    },
    "Direct antiglobulin test",
    "Warm autoimmune hemolytic anemia complicating chronic lymphocytic leukemia — a paraneoplastic "
    "complication rather than tumour bulk, and the classic trap in this disease.\n\n"
    "The hemolysis is unmistakable once the panel is read as a set: anemia with a HIGH reticulocyte "
    "count (a marrow responding, not failing), raised lactate dehydrogenase, undetectable "
    "haptoglobin, unconjugated hyperbilirubinemia, and SPHEROCYTES with polychromasia on the smear. "
    "Spherocytes arise when splenic macrophages nibble membrane from antibody-coated cells — "
    "extravascular hemolysis.\n\n"
    "Why this matters: a falling hemoglobin in chronic lymphocytic leukemia may be autoimmune "
    "hemolysis rather than marrow infiltration, and the treatments are completely different — "
    "corticosteroids and immunosuppression for the antibody, versus disease-directed therapy for "
    "bulk. The direct antiglobulin test separates them in one step.\n\n"
    "Chronic lymphocytic leukemia is a disease of dysregulated B cells, so antibody-mediated problems "
    "follow: autoimmune hemolytic anemia, immune thrombocytopenia, and hypogammaglobulinemia with "
    "recurrent sinopulmonary infections treated with intravenous immunoglobulin.\n\n"
    "Note also what is NOT a treatment indication: a high or rising lymphocyte count alone. Treatment "
    "is indicated for pancytopenia, bulky lymphadenopathy, severe constitutional symptoms or "
    "threatened end organ function. The diagnostic immunophenotype is CD5 positive, CD10 negative, "
    "CD20 positive and CD23 positive — and CD23 is what separates it from mantle cell lymphoma, the "
    "other CD5-positive B-cell neoplasm, which instead carries t(11;14) with cyclin D1.\n\n"
    "Educational objective: A falling hemoglobin in chronic lymphocytic leukemia may reflect "
    "autoimmune hemolysis rather than marrow infiltration; reticulocytosis, spherocytes, raised "
    "lactate dehydrogenase, low haptoglobin and unconjugated hyperbilirubinemia point there, and a "
    "direct antiglobulin test confirms it.",
    "His slow leukemia has confused his immune system into attacking his own red blood cells. The "
    "clue is that his marrow is pumping out replacements as fast as it can, which would not happen if "
    "the leukemia were simply crowding it out.",
    image="fig_lpd_smudge_cells",
    imcap="Peripheral blood smear showing monotonous small lymphocytes with coarsely clumped "
          "chromatin, together with several fragile cells disrupted during smear preparation "
          "(arrows).",
    exim="fig_aiha",
    excap="Warm and cold autoimmune hemolytic anemia compared — antibody class, thermal amplitude "
          "and the direct antiglobulin pattern.",
)

# ── 77. Gastric MALT lymphoma (§41) ─────────────────────────────────────────────
q(
    "A 57-year-old man comes to the office due to 5 months of epigastric discomfort and early "
    "satiety. He has no weight loss, night sweats or lymphadenopathy. Upper endoscopy shows "
    "thickened, nodular gastric folds with superficial erosions. Biopsy is shown: a dense infiltrate "
    "of small lymphoid cells with abundant pale cytoplasm expands the lamina propria and invades and "
    "destroys the gastric glands. The cells are CD20 positive, CD5 negative, CD10 negative and BCL6 "
    "negative, and immunoglobulin gene rearrangement studies confirm a clonal B-cell population. "
    "Immunostaining for Helicobacter pylori is positive. Which of the following is the most "
    "appropriate initial treatment?",
    {
        "Antibiotic eradication therapy": "",
        "ABVD chemotherapy":
            "This is the regimen for Hodgkin lymphoma, which effaces lymph nodes with CD30-positive "
            "Reed-Sternberg cells in a mixed background.",
        "Ibrutinib":
            "A Bruton tyrosine kinase inhibitor used in chronic lymphocytic leukemia and mantle cell "
            "lymphoma — both CD5-POSITIVE B-cell neoplasms. This one is CD5 negative.",
        "R-CHOP combination chemoimmunotherapy":
            "First-line therapy for diffuse large B-cell lymphoma, which forms sheets of large cells "
            "and behaves aggressively. This is an indolent small-cell lymphoma.",
        "Total gastrectomy":
            "Surgery has essentially no role in an indolent lymphoma that frequently regresses "
            "completely once the antigenic drive is removed.",
    },
    "Antibiotic eradication therapy",
    "Extranodal marginal zone (MALT) lymphoma of the stomach — the clearest example in oncology of a "
    "malignancy driven by chronic antigenic stimulation rather than by an intrinsic genetic lesion "
    "alone. Remove the driver and the clone regresses: Helicobacter pylori eradication ALONE can cure "
    "gastric MALT lymphoma.\n\n"
    "The two morphologic buzzwords are in the stem: MONOCYTOID cells (round nuclei with abundant pale "
    "cytoplasm, producing clearing around each nucleus) and the LYMPHOEPITHELIAL LESION — lymphoid "
    "cells invading and destroying glandular epithelium.\n\n"
    "The immunophenotype is a diagnosis partly of exclusion, and it follows from anatomy: the "
    "marginal zone lies OUTSIDE the germinal centre, so germinal centre markers are absent. CD20 "
    "positive, CD5 NEGATIVE (excluding chronic lymphocytic leukemia and mantle cell lymphoma), CD10 "
    "and BCL6 NEGATIVE (excluding follicular and Burkitt lymphoma).\n\n"
    "The same principle applies elsewhere: nodal marginal zone lymphoma is associated with chronic "
    "hepatitis C and may resolve with antiviral therapy; other MALT sites are linked to Campylobacter "
    "jejuni (small intestine), Borrelia burgdorferi (skin) and Chlamydia psittaci (ocular adnexa), "
    "and to autoimmune disease — Sjögren syndrome, Hashimoto thyroiditis. Splenic marginal zone "
    "lymphoma is treated with splenectomy. If eradication fails or the disease persists, rituximab is "
    "the fallback.\n\n"
    "Educational objective: Gastric extranodal marginal zone (MALT) lymphoma is CD5, CD10 and BCL6 "
    "negative, shows monocytoid cells and lymphoepithelial lesions, and is driven by Helicobacter "
    "pylori — so antibiotic eradication alone can cure it.",
    "A long-running stomach infection kept his immune cells switched on until one clone turned into a "
    "slow cancer. Killing the bacteria removes the thing that was driving it, and the cancer often "
    "melts away.",
    image="fig_lpd_lymphoepithelial_lesion",
    imcap="Gastric biopsy, hematoxylin and eosin: a dense infiltrate of small lymphoid cells with "
          "abundant pale cytoplasm expands the lamina propria and invades the glandular epithelium, "
          "which is disrupted and effaced.",
)

# ── 78. Hairy cell leukemia (§41) ───────────────────────────────────────────────
q(
    "A 55-year-old man comes to the office due to 4 months of fatigue, early satiety and two "
    "episodes of pneumonia. Examination shows a spleen palpable 10 cm below the left costal margin. "
    "There is no lymphadenopathy.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.4 g/dL (N=13.5–17.5 g/dL)\n"
    "Leukocyte count 2,100/mm3 (N=4,500–11,000/mm3)\n"
    "Neutrophils 22% (N=54%–62%)\n"
    "Lymphocytes 76% (N=25%–33%)\n"
    "Monocytes 0% (N=3%–7%)\n"
    "Platelet count 62,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Attempted bone marrow aspiration yields only hemodilute blood with no spicules. The peripheral "
    "smear is shown. Which of the following is the most likely diagnosis?",
    {
        "Chronic lymphocytic leukemia":
            "CLL gives a high lymphocyte count with smudge cells and lymphadenopathy, and the marrow "
            "aspirates readily. This patient is pancytopenic with absent monocytes and no nodes.",
        "Chronic myeloid leukemia":
            "Splenomegaly fits, but CML produces a very HIGH white count with basophilia and the "
            "whole granulocyte series, driven by BCR-ABL1.",
        "Hairy cell leukemia": "",
        "Mantle cell lymphoma":
            "Mantle cell disease is CD5 positive with t(11;14) and cyclin D1, usually with widespread "
            "lymphadenopathy and gastrointestinal involvement.",
        "Primary myelofibrosis":
            "Myelofibrosis also gives a dry tap with massive splenomegaly — but its smear is "
            "leukoerythroblastic with tear-drop cells, and monocytopenia is not a feature.",
    },
    "Hairy cell leukemia",
    "Hairy cell leukemia. Three findings in this stem are the ones question-writers use.\n\n"
    "• MONOCYTOPENIA — a lymphoproliferative disorder in blood and marrow accompanied by absent "
    "monocytes should raise hairy cell leukemia immediately. It is also why he has had recurrent "
    "infections\n"
    "• The DRY TAP — aspiration yields hemodilute blood with no spicules, because the infiltrating "
    "cells provoke marrow fibrosis. The core biopsy is what makes the diagnosis\n"
    "• The CELLS — mononuclear cells with fine, irregular cytoplasmic projections, which give the "
    "disease its name\n\n"
    "Add the demographics (median age 55, male to female about 5:1), massive splenomegaly without "
    "lymphadenopathy, and pancytopenia. Immunophenotype: CD5 NEGATIVE and CD10 NEGATIVE, like "
    "marginal zone lymphoma; more than 90% carry activating MAP kinase pathway mutations — think "
    "BRAF — which makes the disease targetable with BRAF inhibitors, alongside the purine analogues "
    "that are standard therapy.\n\n"
    "The dry tap is worth keeping as a short differential of its own: hairy cell leukemia and primary "
    "myelofibrosis both give one, and the smear separates them — fine cytoplasmic projections with "
    "monocytopenia here, versus tear-drop cells and a leukoerythroblastic picture there.\n\n"
    "Educational objective: Hairy cell leukemia presents in middle-aged men with pancytopenia, "
    "MONOCYTOPENIA, massive splenomegaly without lymphadenopathy and a dry tap from marrow fibrosis; "
    "the cells show fine cytoplasmic projections, are CD5 and CD10 negative, and usually carry BRAF "
    "mutations.",
    "His spleen is huge and his blood counts are all low, and the marrow needle draws nothing because "
    "the marrow is scarred. The tell is that one particular white cell type — monocytes — has "
    "vanished completely.",
    image="fig_lpd_hairy_cell",
    imcap="Peripheral blood smear: a mononuclear cell with an oval nucleus and pale cytoplasm whose "
          "border shows fine, irregular projections.",
)

# ── 79. Myeloma and light chain cast nephropathy (§42) ──────────────────────────
q(
    "A 69-year-old woman comes to the office due to 3 months of mid-back pain and fatigue. She has "
    "no fever. Examination shows tenderness over the thoracic spine.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.2 g/dL (N=12.0–16.0 g/dL)\n"
    "Calcium 11.8 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Creatinine 3.4 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Albumin 3.8 g/dL (N=3.5–5.5 g/dL)\n"
    "Total protein 8.2 g/dL (N=6.0–7.8 g/dL)\n\n"
    "Serum protein electrophoresis shows a monoclonal spike of 1.1 g/dL. Urinalysis shows 1+ protein "
    "on dipstick with no cells or casts on microscopy, but a 24-hour urine collection contains 4.2 g "
    "of protein. Radiographs show multiple punched-out lytic lesions in the skull and vertebrae. A "
    "bone marrow biopsy is shown. Which of the following best explains this patient's renal "
    "failure?",
    {
        "Amyloid deposition within glomeruli":
            "Light chain amyloidosis does occur in plasma cell disorders and causes nephrotic-range "
            "albuminuria — but the dipstick, which detects albumin, would then be strongly positive. "
            "Here it is only 1+ despite 4.2 g of protein.",
        "Deposition of immune complexes in glomeruli":
            "Immune complex glomerulonephritis produces an active sediment with red cells and red "
            "cell casts. The microscopy here is bland.",
        "Hypercalcemia-induced nephrocalcinosis":
            "Hypercalcemia does contribute to renal injury in myeloma and should be treated, but it "
            "does not explain 4.2 g of non-albumin protein in the urine.",
        "Obstruction of tubules by filtered light chains": "",
        "Renal infiltration by malignant plasma cells":
            "Direct plasma cell infiltration of the kidney is rare; the damage in myeloma is done by "
            "what the cells secrete, not by where they grow.",
    },
    "Obstruction of tubules by filtered light chains",
    "Multiple myeloma with light chain cast nephropathy. The vignette gives the full CRAB tetrad — "
    "hyperCalcemia, Renal failure, Anemia, Bone lesions — which is the end organ damage that converts "
    "a watched precursor state into a treated cancer.\n\n"
    "Why the renal failure happens despite an unimpressive spike: an antibody is made of heavy and "
    "light chains, and a myeloma clone can secrete free LIGHT CHAINS in enormous quantity. Because "
    "they are small they are filtered at the glomerulus and precipitate in the tubules, obstructing "
    "them and injuring the epithelium. They contribute little to the serum electrophoresis peak — "
    "which is exactly why serum free light chains are measured SEPARATELY in the workup.\n\n"
    "The urine findings are the give-away and are worth understanding rather than memorizing: the "
    "dipstick detects ALBUMIN, so it is only 1+, while the 24-hour collection measures total protein "
    "and captures the 4.2 g of light chains the dipstick cannot see. A large dipstick-negative "
    "proteinuria is close to diagnostic.\n\n"
    "The workup is serum protein electrophoresis, serum free light chains, a metabolic panel for "
    "calcium and creatinine, a complete blood count, and a skeletal survey with PET/CT or magnetic "
    "resonance imaging for equivocal findings. Beyond CRAB, expect recurrent infection (the clone "
    "crowds out normal immunoglobulin production, so the patient is functionally "
    "hypogammaglobulinemic despite a high total protein), hyperviscosity and amyloidosis.\n\n"
    "Educational objective: In multiple myeloma, renal failure is usually caused by filtered free "
    "light chains precipitating in and obstructing renal tubules, which is why serum free light "
    "chains are measured separately and why a modest electrophoresis spike does not exclude "
    "significant disease. Urine dipstick underestimates the proteinuria because it detects only "
    "albumin.",
    "Her cancerous antibody-making cells pump out tiny protein fragments that the kidney filters and "
    "that then clog the kidney's drainpipes. The usual urine dipstick misses them, which is why the "
    "24-hour collection looks so much worse.",
    image="fig_hx_myeloma_marrow",
    imcap="Bone marrow biopsy at high power, hematoxylin and eosin. The marrow is replaced by sheets "
          "of medium to large cells with abundant cytoplasm and eccentrically placed round nuclei, "
          "several containing prominent nucleoli and occasional binucleate forms; normal "
          "hematopoietic elements are scarce.",
)

# ── 80. Waldenström macroglobulinemia and hyperviscosity (§42) ──────────────────
q(
    "A 72-year-old man is brought to the emergency department by his daughter due to 2 weeks of "
    "blurred vision, headache and unsteadiness, worse over the past 2 days. He has had fatigue and "
    "night sweats for 6 months. Examination shows nystagmus, an ataxic gait, and diffuse "
    "lymphadenopathy with a spleen palpable 5 cm below the costal margin. Funduscopy shows dilated, "
    "tortuous retinal veins with scattered hemorrhages.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.6 g/dL (N=13.5–17.5 g/dL)\n"
    "Calcium 9.4 mg/dL (N=8.4–10.2 mg/dL)\n"
    "Creatinine 1.0 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Total protein 10.4 g/dL (N=6.0–7.8 g/dL)\n\n"
    "Serum protein electrophoresis with immunofixation shows a monoclonal IgM of 5.8 g/dL. A "
    "skeletal survey shows no lytic lesions. Marrow biopsy shows a lymphoplasmacytic infiltrate with "
    "an MYD88 mutation. Which of the following is the most appropriate immediate treatment?",
    {
        "Bisphosphonate therapy":
            "Bisphosphonates treat the skeletal disease and hypercalcemia of myeloma. His calcium is "
            "normal and there are no lytic lesions — the two findings that separate this disease from "
            "myeloma.",
        "Intravenous immunoglobulin":
            "This replaces antibody in hypogammaglobulinemia and blocks splenic Fc receptors in "
            "immune thrombocytopenia. Adding more immunoglobulin to a hyperviscous patient is exactly "
            "wrong.",
        "Plasmapheresis": "",
        "Red blood cell transfusion":
            "His anemia is real, but transfusion raises viscosity further and can precipitate "
            "deterioration before the paraprotein is removed.",
        "Rituximab monotherapy":
            "Anti-CD20 therapy is part of definitive treatment — but it works over weeks, and it can "
            "provoke an IgM 'flare' that transiently worsens viscosity just as you start.",
        "Urgent hemodialysis":
            "Dialysis clears small solutes and is used for the renal failure of light chain disease. "
            "His creatinine is normal, and dialysis does not remove a large pentameric protein.",
    },
    "Plasmapheresis",
    "Hyperviscosity syndrome from lymphoplasmacytic lymphoma (Waldenström macroglobulinemia) — an "
    "emergency, and the immediate treatment is plasmapheresis to remove the circulating IgM.\n\n"
    "One molecular property explains nearly every complication: IgM is a PENTAMER — five antibody "
    "units joined together. That bulk keeps it in the intravascular space and raises viscosity "
    "dramatically at concentrations an IgG paraprotein would tolerate. Hence blurred vision with "
    "dilated tortuous retinal veins, headache, vertigo, nystagmus and ataxia, progressing to stroke, "
    "coma and delirium. The same bulk interferes with fibrin polymerization (bleeding), drives cold "
    "agglutinin hemolysis, and produces cryoglobulinemia.\n\n"
    "Myeloma versus Waldenström, which this vignette is built to separate:\n"
    "• Cell of origin — fully differentiated plasma cell versus a lymphoplasmacytic B cell, an "
    "indolent lymphoma\n"
    "• Paraprotein — usually IgG or IgA (or light chains only) versus IgM\n"
    "• Genetics — FISH abnormalities, 17p adverse, versus MYD88 mutation\n"
    "• Bone lesions, hypercalcemia and renal failure — characteristic of myeloma; uncommon here\n"
    "• Lymphadenopathy and splenomegaly — uncommon in myeloma; characteristic here\n"
    "• Signature complication — CRAB versus HYPERVISCOSITY, with neuropathy\n\n"
    "Bone and kidney versus thick blood and nerves. After plasmapheresis, treat the underlying "
    "lymphoma — while watching for the IgM flare, a transient rise at the start of therapy that can "
    "worsen viscosity just as treatment begins.\n\n"
    "Educational objective: An IgM paraprotein from lymphoplasmacytic lymphoma (Waldenström "
    "macroglobulinemia) causes hyperviscosity with visual disturbance, headache and neurologic signs, "
    "treated emergently with plasmapheresis. Lytic bone lesions, hypercalcemia and light chain renal "
    "failure point instead to multiple myeloma.",
    "His blood has become as thick as syrup because of a huge, bulky antibody, so it sludges in the "
    "small vessels of the eye and brain. The fastest fix is to filter that antibody out of his plasma.",
)
