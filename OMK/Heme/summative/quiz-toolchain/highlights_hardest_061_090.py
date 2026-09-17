# Key Findings — vignette highlights for Hardest Exam questions 61–90.
# Authoring rules and categories: see highlights_hardest_001_030.py and QUIZ_BUILD_METHOD.md.

F, M, T, P, W = "finding", "mechanism", "term", "pattern", "workup"
EYEBROW = {F: "FINDING", M: "MECHANISM", T: "KEY TERM", P: "PATTERN", W: "WHAT'S ASKED"}


def h(text, cat, title, body):
    return {"text": text, "cat": cat, "eyebrow": EYEBROW[cat], "title": title, "body": body}


HIGHLIGHTS = {

61: [
 h("a proliferation index of 85%", F, "Fast-dividing",
   "The proliferation index is the fraction of cells actively cycling. At 85% almost the whole "
   "tumour is in cycle at any moment, so almost the whole tumour is exposed to a cytotoxic drug."),
 h("a proliferation index of 10%", F, "Slow-dividing",
   "At 10%, nine cells in ten are resting at any given time. Cytotoxic chemotherapy passes over "
   "them, so the tumour is reduced but never eradicated — which is why it recurs."),
 h("she is observed without treatment", P, "Watchful waiting is a real answer",
   "Treating an indolent lymphoma earlier does not prolong life, so observation is standard until "
   "symptoms, cytopenias or organ compromise appear. Reflexively treating every cancer is the trap."),
 h("Which of the following best explains why the more aggressive disease is the one treated with "
   "curative intent?", W, "Grow-fast, die-fast",
   "The counterintuitive rule of lymphoma: AGGRESSIVE lymphomas are potentially CURABLE, and "
   "INDOLENT lymphomas are generally INCURABLE but compatible with years of life. Cytotoxic drugs "
   "act on dividing cells, so the disease that divides fastest is the one they can eradicate."),
],

62: [
 h("Leukocyte count  87,000/mm3", F, "Hyperleukocytosis",
   "A very high count composed almost entirely of blasts. Above 100,000/mm3 this risks leukostasis "
   "— sludging in cerebral and pulmonary microvessels."),
 h("Segmented neutrophils  1%", M, "Marrow failure despite a huge count",
   "The count is enormous but functionally empty: the blasts have crowded out normal "
   "hematopoiesis, which is why she is anemic, thrombocytopenic and effectively neutropenic all at "
   "once."),
 h("large cells with scant cytoplasm, fine chromatin and prominent nucleoli", F, "Blasts",
   "Immature chromatin and prominent nucleoli identify a blast. Morphology alone establishes that "
   "this is an acute leukemia — but NOT which lineage, which is what the question turns on."),
 h("Which of the following findings would best establish the lineage of this patient's disease?", W,
   "Myeloid versus lymphoid",
   "More than 20% blasts defines acute leukemia; lineage needs a marker. MYELOPEROXIDASE — "
   "whether as a stain or as the Auer rods that are crystallized MPO-containing granules — "
   "establishes myeloid lineage. Terminal deoxynucleotidyl transferase with CD19 or CD3 would "
   "indicate lymphoid."),
],

63: [
 h("a population of abnormal cells with heavily granulated cytoplasm, some containing bundles of "
   "needle-shaped cytoplasmic inclusions", T, "Faggot cells",
   "Bundles of Auer rods within a single hypergranular promyelocyte. Auer rods are crystallized "
   "primary granule contents; a sheaf of them is essentially diagnostic of acute promyelocytic "
   "leukemia."),
 h("Fibrinogen  78 mg/dL", F, "Disseminated intravascular coagulation",
   "Prolonged clotting times, a very low fibrinogen, a very high D-dimer and schistocytes. The "
   "promyelocyte granules are rich in tissue factor and annexin II, so the cells drive both "
   "coagulation and fibrinolysis as they release their contents."),
 h("Cytogenetic studies are pending", P, "Do not wait for the karyotype",
   "This is the entire point of the question. Confirming t(15;17) takes days, and the leading "
   "cause of early death in acute promyelocytic leukemia is intracranial or pulmonary hemorrhage "
   "within those days."),
 h("Which of the following is the most appropriate immediate treatment?", W,
   "Treat on suspicion",
   "All-trans retinoic acid is started the moment the diagnosis is SUSPECTED. It forces the "
   "malignant promyelocytes to differentiate, which switches off the coagulopathy — the one "
   "hematologic malignancy where a specific drug is given before the diagnosis is confirmed."),
],

64: [
 h("He has heart failure with an ejection fraction of 30%", P, "Anthracyclines are off the table",
   "Standard intensive induction — the '7+3' of cytarabine plus an anthracycline — requires a "
   "heart that can tolerate daunorubicin. This one cannot."),
 h("requires assistance with bathing and dressing; he spends more than half of each day in a chair",
   F, "Poor performance status",
   "Functional status predicts treatment-related mortality better than age alone. Dependence in "
   "activities of daily living and more than half the day spent sitting or lying describes a "
   "patient intensive induction would likely kill."),
 h("Cytogenetics show a complex karyotype", F, "Adverse-risk disease",
   "A complex karyotype predicts a poor response to intensive chemotherapy, so the treatment most "
   "likely to cause harm is also the one least likely to work."),
 h("His daughter asks whether he can have 'the strong chemotherapy that cures this'", P,
   "The question behind the question",
   "Fitness, not diagnosis, selects the regimen. A hypomethylating agent with venetoclax achieves "
   "meaningful remission rates in patients who could never survive induction — and saying so "
   "plainly is part of the answer."),
],

65: [
 h("a proliferation index above 95%", F, "The precondition for tumour lysis",
   "A large, exquisitely chemosensitive, rapidly dividing tumour. Massive simultaneous cell death "
   "dumps intracellular contents into the circulation faster than the kidney can clear them."),
 h("Potassium  6.6 mEq/L", M, "Everything up except calcium",
   "Potassium, phosphate and uric acid are all intracellular and all rise. Calcium is the "
   "exception: it FALLS, because released phosphate binds it and precipitates as calcium "
   "phosphate — which is also what causes the cramps and perioral tingling."),
 h("Uric acid  16.4 mg/dL", M, "Nucleic acid breakdown",
   "Released DNA is catabolized to uric acid, which crystallizes in the renal tubules and "
   "precipitates acute kidney injury — and the failing kidney then worsens every other "
   "abnormality."),
 h("Prothrombin time, partial thromboplastin time and fibrinogen are normal, and no schistocytes "
   "are seen", W, "Not a microangiopathy",
   "The stem removes disseminated intravascular coagulation, which can also complicate an "
   "aggressive lymphoma and would change management entirely."),
 h("Which of the following is the most appropriate agent for this patient's uric acid?", W,
   "Destroy it, do not just stop making it",
   "Allopurinol blocks xanthine oxidase and prevents FURTHER uric acid formation, but does nothing "
   "about the 16.4 mg/dL already circulating. RASBURICASE is a recombinant urate oxidase that "
   "converts existing uric acid to soluble allantoin, so it is the agent for established tumour "
   "lysis. Avoid it in G6PD deficiency — it generates hydrogen peroxide."),
],

66: [
 h("Mean corpuscular volume  104 µm3", F, "Macrocytosis without a vitamin deficiency",
   "A raised mean volume with a normal B12 level and no alcohol history should raise myelodysplasia "
   "in an older patient. Dysplastic erythropoiesis produces large, poorly made cells."),
 h("He has never received chemotherapy or radiation", F, "Primary, not therapy-related",
   "Therapy-related myelodysplasia carries a worse prognosis and different cytogenetics. This is "
   "de novo disease."),
 h("a hypercellular marrow with dysplastic erythroid and granulocytic precursors", M,
   "The central paradox",
   "A FULL marrow with an EMPTY blood count. Production is abundant but ineffective — precursors "
   "die within the marrow by apoptosis before they can be released. That is why the reticulocyte "
   "count is low despite a packed marrow."),
 h("8% blasts", W, "Below the leukemia threshold",
   "More than 20% blasts would define acute myeloid leukemia. At 8% this is myelodysplasia with "
   "excess blasts — a higher-risk category, but not yet leukemia."),
 h("Which of the following is the most likely cause of death in this patient?", W,
   "Cytopenias kill before transformation does",
   "Only about a third of patients progress to acute leukemia. The majority die of the "
   "consequences of the cytopenias they already have — infection from neutropenia and dysfunctional "
   "neutrophils, or hemorrhage from thrombocytopenia."),
],

67: [
 h("Basophils  7%", F, "Basophilia is the giveaway",
   "Basophilia, usually with eosinophilia, is characteristic of chronic myeloid leukemia and is "
   "rare in a reactive leukocytosis. This is the mirror image of the leukemoid reaction, where the "
   "basophil count is zero."),
 h("She has no fever, cough, wounds or recent illness", P, "No reason for a reactive count",
   "A leukemoid reaction needs something to react to. An incidental count of 82,000 in a well "
   "patient with no infective source points at a clonal process."),
 h("The spleen is palpable 6 cm below the left costal margin", F, "Splenomegaly",
   "Early satiety and left upper quadrant fullness from an enlarged spleen are typical of the "
   "chronic phase, and splenomegaly is unusual in a reactive leukocytosis."),
 h("There is no toxic granulation", P, "The neutrophils are not activated",
   "Toxic granulation, Döhle bodies and vacuolization mark a neutrophil responding to infection. "
   "Their absence, with the full spectrum of maturation present, indicates clonal overproduction "
   "rather than a reaction."),
 h("Which of the following additional findings is most likely in this patient?", W,
   "Leukocyte alkaline phosphatase separates them",
   "The score is LOW in chronic myeloid leukemia, because the neoplastic granulocytes are not "
   "normally activated cells, and HIGH in a leukemoid reaction. It is the classic discriminator, "
   "although BCR-ABL1 testing has replaced it in practice."),
],

68: [
 h("has taken imatinib for 3 years with an excellent molecular response and no missed doses", P,
   "Adherence is excluded",
   "Non-adherence is the commonest reason a tyrosine kinase inhibitor stops working, so the stem "
   "closes it off. A true loss of response after a durable remission means resistance."),
 h("his BCR-ABL1 transcript level has risen on three successive measurements", F,
   "Molecular relapse comes first",
   "The transcript level rises before the blood count does and long before symptoms. Serial "
   "molecular monitoring exists precisely to catch this point."),
 h("a T315I substitution", M, "The gatekeeper mutation",
   "Threonine 315 sits at the entrance to the kinase's ATP-binding pocket and forms a hydrogen "
   "bond with imatinib. Substituting the bulkier isoleucine both removes that bond and physically "
   "obstructs the pocket, so imatinib, dasatinib, nilotinib and bosutinib all fail together."),
 h("Which of the following is the most appropriate next treatment?", W, "One drug fits the pocket",
   "Switching to another second-generation inhibitor is futile against T315I. PONATINIB is the "
   "third-generation agent designed with a carbon-carbon triple bond that accommodates the bulkier "
   "residue — at the cost of significant arterial thrombotic risk. Asciminib, which binds the "
   "myristoyl pocket instead, is the other option."),
],

69: [
 h("intense itching that begins within minutes of a hot shower", T, "Aquagenic pruritus",
   "Itching triggered specifically by water, classically a hot shower, and lasting up to an hour. "
   "It is thought to reflect mast cell and basophil degranulation and is highly characteristic of "
   "polycythemia vera."),
 h("episodes of burning pain and redness in both hands and feet", T, "Erythromelalgia",
   "Burning, red, hot extremities from platelet-mediated microvascular occlusion. It typically "
   "responds to aspirin, which is part of the treatment."),
 h("Erythropoietin  2 mU/mL", W, "Suppressed, which means primary",
   "This single value separates the two halves of the differential. In a SECONDARY polycythemia "
   "— hypoxia, a tumour producing erythropoietin — the hormone is HIGH and driving the marrow. In "
   "polycythemia vera the marrow is autonomous, so feedback suppresses it to a low level."),
 h("Oxygen saturation is 98% on room air", P, "Hypoxic causes closed off",
   "With no smoking history and no cardiopulmonary disease, a normal saturation removes chronic "
   "hypoxia — the commonest cause of a secondary erythrocytosis."),
 h("Which of the following is the most appropriate initial treatment?", W,
   "Lower the hematocrit first",
   "The immediate risk is thrombosis from hyperviscosity. PHLEBOTOMY to a hematocrit below 45% is "
   "the foundation of treatment, with low-dose aspirin; hydroxyurea is added for high-risk "
   "patients. Iron deficiency from repeated phlebotomy is expected and is not corrected."),
],

70: [
 h("a firm spleen palpable 12 cm below the left costal margin", F, "Massive splenomegaly",
   "Extramedullary hematopoiesis. When the marrow is obliterated by fibrosis, blood production "
   "restarts in the organ that did it in fetal life — which is why the spleen becomes enormous and "
   "why bone pain and constitutional symptoms accompany it."),
 h("Attempted bone marrow aspiration yields no material", T, "A dry tap",
   "The needle cannot draw marrow because the space has been replaced by fibrous tissue. A dry tap "
   "is a positive finding, and it mandates a CORE biopsy — the aspirate can never make this "
   "diagnosis."),
 h("The peripheral smear is shown", W, "Expect a leukoerythroblastic picture",
   "Teardrop red cells (dacrocytes), nucleated red cells and immature granulocytes. The teardrops "
   "are cells physically deformed as they squeeze out of a fibrotic marrow and through the spleen."),
 h("Which of the following is most likely to be found on the core biopsy?", W,
   "Fibrosis is the answer, but it is secondary",
   "The fibroblasts are NOT part of the clone. A clonal megakaryocyte population releases "
   "platelet-derived growth factor and transforming growth factor beta, which drive normal "
   "fibroblasts to lay down reticulin and then collagen. The malignancy recruits the fibrosis "
   "rather than being made of it."),
],

71: [
 h("3 weeks of leg pain that wakes her at night", F, "Bone pain in a child",
   "Pain from marrow expansion that wakes a child at night, with tenderness over the long bones, "
   "is a classic presentation of acute lymphoblastic leukemia and is easily dismissed as growing "
   "pains."),
 h("cells expressing CD19, CD10 and terminal deoxynucleotidyl transferase", T,
   "Precursor B immunophenotype",
   "CD19 establishes B lineage, CD10 (the common ALL antigen) marks the precursor stage, and "
   "terminal deoxynucleotidyl transferase confirms immaturity — it is expressed only in lymphoid "
   "precursors."),
 h("cytogenetics show hyperdiploidy", F, "A favourable karyotype",
   "More than 50 chromosomes carries a good prognosis, as does t(12;21). Hypodiploidy and t(9;22) "
   "are the adverse counterparts."),
 h("which of the following is required in the treatment of this patient?", W,
   "A sanctuary site must be treated blind",
   "The central nervous system is a pharmacologic sanctuary that systemic chemotherapy does not "
   "penetrate. Without prophylactic intrathecal therapy, relapse there is common — so it is given "
   "to EVERY patient, whether or not blasts are found in the cerebrospinal fluid. The testis is "
   "the other sanctuary site."),
],

72: [
 h("His presenting leukocyte count is 9,000/mm3", F, "A favourable presenting count",
   "Below 50,000/mm3 at diagnosis is a good-risk feature. A very high presenting count is adverse."),
 h("marrow blasts have cleared to under 1% by day 8 of induction", F, "Rapid early response",
   "Speed of clearance is one of the strongest prognostic variables in childhood leukemia, and "
   "minimal residual disease at the end of induction is stronger still. This is an excellent "
   "response."),
 h("cerebrospinal fluid examination shows no blasts", F, "No central nervous system disease",
   "Another favourable feature — although intrathecal prophylaxis is given regardless."),
 h("Which of the following additional findings would most strongly worsen this patient's "
   "prognosis?", W, "Cytogenetics outrank everything else",
   "Age 1–10, a count under 50,000, rapid clearance and hyperdiploidy or t(12;21) are all "
   "favourable. The t(9;22) BCR-ABL1 rearrangement — Philadelphia-positive ALL — is the adverse "
   "finding that overrides them, and it changes treatment: a tyrosine kinase inhibitor is added to "
   "chemotherapy."),
],

73: [
 h("a large anterior mediastinal mass", F, "The typical distribution",
   "Nodular sclerosis Hodgkin lymphoma characteristically involves the mediastinum and the lower "
   "cervical and supraclavicular nodes in a young patient — and it is the only Hodgkin subtype "
   "with a female predominance."),
 h("Scattered large cells with abundant pale cytoplasm lie within clear spaces", T, "Lacunar cells",
   "The Reed-Sternberg variant of this subtype. The clear space is a retraction artefact of "
   "formalin fixation around the cytoplasm, giving the appearance of a cell sitting in a lacuna."),
 h("CD30 and CD15 positive, CD45 negative", F, "The Hodgkin immunophenotype",
   "CD30 and CD15 positive with CD45 (the common leukocyte antigen) NEGATIVE and PAX5 only weakly "
   "positive. A non-Hodgkin large B-cell lymphoma would be the reverse — CD45 and CD20 strongly "
   "positive."),
 h("Which of the following features distinguishes this subtype of Hodgkin lymphoma from mixed "
   "cellularity disease?", W, "The subtypes differ by background, not by the malignant cell",
   "The Reed-Sternberg cell is the same in both. NODULAR SCLEROSIS is defined by broad birefringent "
   "COLLAGEN BANDS dividing the node into nodules, plus lacunar cells. MIXED CELLULARITY has no "
   "bands and a mixed inflammatory background, is commoner in older patients and in HIV, and is "
   "more often Epstein-Barr virus positive."),
],

74: [
 h("scattered very large cells with bilobed nuclei and prominent eosinophilic nucleoli", T,
   "Reed-Sternberg cells",
   "The classic 'owl eye' binucleate cell with inclusion-like nucleoli. They are a small minority "
   "of the tumour — most of what is seen is a reactive inflammatory background they have "
   "recruited."),
 h("CD20 negative, OCT2 negative and PAX5 weakly positive", M, "A B cell that stopped acting like one",
   "Reed-Sternberg cells ARE of germinal center B-cell origin, but they have switched off the B-cell "
   "transcriptional program: OCT2 and BOB1 are lost, PAX5 is only weakly retained, and surface "
   "immunoglobulin and CD20 are gone. Losing that program is what lets them survive despite having "
   "no functional immunoglobulin."),
 h("His brother, who has diffuse large B-cell lymphoma, receives rituximab", P,
   "Same lineage, different target",
   "A fair question from the family, and the answer is mechanistic. Rituximab is an anti-CD20 "
   "antibody, so it can only work where CD20 is expressed."),
 h("Which of the following best explains this?", W, "No antigen, no antibody therapy",
   "Classic Hodgkin cells are CD20 NEGATIVE, so rituximab has nothing to bind. Brentuximab vedotin "
   "— an anti-CD30 antibody-drug conjugate — is the targeted agent used here instead, because CD30 "
   "is what these cells do express."),
],

75: [
 h("a dense monotonous sheet of intermediate-sized cells with numerous mitotic figures, interrupted "
   "by evenly spaced pale macrophages containing cellular debris", T, "The starry sky",
   "The 'stars' are tingible body macrophages clearing apoptotic tumour cells against the dark "
   "'sky' of densely packed lymphoma. It reflects an extraordinary rate of both proliferation AND "
   "cell death."),
 h("BCL2 NEGATIVE", P, "Death is not blocked here",
   "The contrast with follicular lymphoma is the whole point. Follicular lymphoma accumulates cells "
   "because BCL2 stops them dying. Burkitt lymphoma is BCL2 negative — its cells die freely, which "
   "is why the macrophages are so busy."),
 h("the Ki-67 proliferation index is 99%", F, "Essentially every cell is cycling",
   "The highest proliferation index of any human tumour, with a doubling time of about 24 hours. "
   "This is why it presents as a rapidly growing mass and why tumour lysis syndrome is such a risk "
   "when treatment starts."),
 h("Which of the following best explains the accumulation of malignant cells in this patient?", W,
   "Accelerator, not brake",
   "Two ways a tumour can accumulate cells: push the accelerator (excess proliferation) or remove "
   "the brake (blocked apoptosis). Burkitt lymphoma is the accelerator — t(8;14) places MYC, a "
   "master proliferation transcription factor, under immunoglobulin heavy chain control. It is "
   "also curable, because cytotoxic drugs kill dividing cells."),
],

76: [
 h("Reticulocyte count  9.2%", F, "A hyperproliferative anemia",
   "With a high lactate dehydrogenase, unmeasurable haptoglobin and raised bilirubin, cells are "
   "being destroyed and the marrow is compensating. That excludes the other common anemia in "
   "chronic lymphocytic leukemia — marrow replacement, which would give a LOW reticulocyte count."),
 h("spherocytes and polychromasia", F, "Extravascular immune hemolysis",
   "Macrophages in the spleen remove portions of antibody-coated membrane, and the cell reseals as "
   "a sphere. Spherocytes plus a high reticulocyte count point at warm autoimmune hemolysis."),
 h("small mobile cervical nodes unchanged from previous visits", P, "The disease has not progressed",
   "Stable nodes and a stable lymphocyte count mean the anemia is not from advancing leukemia. "
   "Autoimmune complications of chronic lymphocytic leukemia can occur at any stage and do not "
   "track disease bulk."),
 h("Which of the following is the most appropriate next diagnostic test?", W,
   "The Coombs test settles the spherocyte",
   "Spherocytes have two common causes — an inherited membrane defect and warm autoimmune "
   "hemolysis. The DIRECT ANTIGLOBULIN TEST separates them in one step, and in a patient with "
   "chronic lymphocytic leukemia a positive result is expected: the disordered B cells produce "
   "autoantibodies against red cells."),
],

77: [
 h("a dense infiltrate of small lymphoid cells with abundant pale cytoplasm expands the lamina "
   "propria and invades and destroys the gastric glands", T, "Lymphoepithelial lesions",
   "Neoplastic marginal zone cells invading and destroying the glandular epithelium. This is the "
   "defining histologic feature of extranodal marginal zone (MALT) lymphoma."),
 h("CD5 negative, CD10 negative and BCL6 negative", W, "Negatives place the cell of origin",
   "The mature B-cell differential is cut into thirds by two markers. CD5 positive means chronic "
   "lymphocytic leukemia or mantle cell lymphoma; CD10 positive means follicular or Burkitt "
   "lymphoma. NEGATIVE for both points at marginal zone lymphoma."),
 h("Immunostaining for Helicobacter pylori is positive", M, "Chronic antigen drives the clone",
   "The stomach has no native lymphoid tissue. Helicobacter infection recruits it, and years of "
   "continuous antigenic stimulation eventually allow a clone to emerge — one that remains "
   "DEPENDENT on that stimulation."),
 h("Which of the following is the most appropriate initial treatment?", W,
   "Cure the lymphoma with antibiotics",
   "Because the clone still depends on the antigenic drive, eradicating Helicobacter pylori causes "
   "regression in roughly 75% of cases. It is the outstanding example of a malignancy treated by "
   "removing its stimulus. Tumours with t(11;18) are the ones that do not respond."),
],

78: [
 h("Monocytes  0%", F, "Monocytopenia",
   "Absolute absence of monocytes is unusual and highly characteristic of hairy cell leukemia. It "
   "helps explain the susceptibility to mycobacterial and other opportunistic infection."),
 h("a spleen palpable 10 cm below the left costal margin", P, "Massive spleen, NO nodes",
   "The combination is the discriminator. Hairy cell leukemia infiltrates the splenic RED pulp and "
   "characteristically spares the lymph nodes — the opposite of chronic lymphocytic leukemia, "
   "where adenopathy is prominent."),
 h("Attempted bone marrow aspiration yields only hemodilute blood with no spicules", T, "A dry tap",
   "The malignant cells induce marrow reticulin fibrosis, so the aspirate fails and a core biopsy "
   "is required. Myelofibrosis is the other classic cause of a dry tap."),
 h("Which of the following is the most likely diagnosis?", W, "Pancytopenia plus a huge spleen",
   "Look for cells with fine cytoplasmic projections, positive for CD11c, CD25, CD103 and CD123, "
   "tartrate-resistant acid phosphatase positive, and carrying the BRAF V600E mutation. It responds "
   "dramatically to purine analogues such as cladribine."),
],

79: [
 h("Urinalysis shows 1+ protein on dipstick with no cells or casts on microscopy, but a 24-hour "
   "urine collection contains 4.2 g of protein", W, "The dipstick–collection discrepancy",
   "This is the single most informative finding. The urine dipstick detects ALBUMIN and is nearly "
   "blind to immunoglobulin light chains. Heavy proteinuria that the dipstick barely registers "
   "means the protein is not albumin — it is Bence Jones protein."),
 h("Total protein  8.2 g/dL", F, "A protein gap",
   "Total protein well above normal while albumin is normal means the excess is globulin. "
   "Subtracting one from the other is a quick bedside screen for a paraprotein."),
 h("multiple punched-out lytic lesions in the skull and vertebrae", F, "Purely lytic bone disease",
   "Myeloma cells secrete RANK ligand and other factors that activate osteoclasts while "
   "suppressing osteoblasts, so there is no reactive bone formation. That is why the lesions are "
   "punched out and why a bone scan can be falsely negative."),
 h("Calcium  11.8 mg/dL", F, "Hypercalcemia from bone resorption",
   "Part of the CRAB tetrad — hyperCalcemia, Renal failure, Anemia, Bone lesions — and itself a "
   "contributor to the renal injury through volume depletion."),
 h("Which of the following best explains this patient's renal failure?", W,
   "In myeloma the damage comes from the protein",
   "Filtered free light chains precipitate with Tamm-Horsfall protein in the distal tubules, "
   "forming casts that obstruct them and provoke inflammation — cast nephropathy, the 'myeloma "
   "kidney'. Hypercalcemia, dehydration and bisphosphonates contribute, but the light chain is the "
   "mechanism."),
],

80: [
 h("blurred vision, headache and unsteadiness", F, "The hyperviscosity triad",
   "Visual changes, neurologic symptoms and mucosal bleeding. IgM is a pentamer, so a modest molar "
   "concentration produces a disproportionate rise in serum viscosity."),
 h("dilated, tortuous retinal veins with scattered hemorrhages", T, "Sausage-link retinal veins",
   "Segmental dilation of the retinal veins with hemorrhages is the visible manifestation of "
   "sludging. The fundus is where hyperviscosity can actually be seen."),
 h("A skeletal survey shows no lytic lesions", P, "This is not myeloma",
   "Normal calcium, normal creatinine and no lytic lesions exclude the CRAB features. IgM "
   "paraprotein with a lymphoplasmacytic marrow infiltrate and an MYD88 mutation is "
   "Waldenström macroglobulinemia — a lymphoma, not a plasma cell myeloma."),
 h("Which of the following is the most appropriate immediate treatment?", W,
   "Remove the protein before treating the clone",
   "Symptomatic hyperviscosity is an emergency, and PLASMAPHERESIS removes the circulating IgM "
   "within hours. It works particularly well here because IgM is largely INTRAVASCULAR. Definitive "
   "therapy directed at the clone follows — but not first."),
],

81: [
 h("rituximab, cyclophosphamide, doxorubicin, vincristine and prednisone", M,
   "Five agents, five mechanisms",
   "An anti-CD20 antibody, an alkylating agent, a topoisomerase II inhibitor and DNA intercalator, "
   "a microtubule poison, and a corticosteroid. No two share a mechanism of action."),
 h("why five drugs are needed rather than a higher dose of the single most effective one", W,
   "Non-overlapping toxicity is the reason",
   "Each drug is dose-limited by a DIFFERENT toxicity — cardiac for doxorubicin, neurologic for "
   "vincristine, bladder and marrow for cyclophosphamide. Because the toxicities do not overlap, "
   "each agent can be given at its own full effective dose. Escalating one drug instead simply "
   "reaches that drug's ceiling toxicity. Combination therapy also attacks resistant subclones "
   "from several directions at once."),
],

82: [
 h("progresses again within 8 weeks despite never having received either drug", P,
   "Resistance to drugs never given",
   "This is the observation that has to be explained. Resistance arising against agents the "
   "patient has never been exposed to cannot be target-specific."),
 h("The three agents are structurally unrelated and act by different mechanisms", W,
   "Cross-resistance across classes",
   "An anthracycline, a vinca alkaloid and an epipodophyllotoxin share no target and no structure. "
   "A single resistance mechanism covering all three must act on something they DO share."),
 h("Which of the following best explains the pattern of resistance in this patient?", W,
   "The multidrug efflux pump",
   "P-glycoprotein, encoded by MDR1/ABCB1, is an ATP-dependent membrane pump with very broad "
   "substrate specificity for large hydrophobic natural-product drugs — anthracyclines, vinca "
   "alkaloids, taxanes and epipodophyllotoxins. Upregulating one transporter confers resistance to "
   "all of them at once, which is what MULTIDRUG resistance means."),
],

83: [
 h("doxorubicin, bleomycin, vinblastine and dacarbazine", W, "Predict toxicity from the class",
   "The ABVD regimen, and each letter has a signature toxicity: doxorubicin is cardiotoxic, "
   "BLEOMYCIN is pulmonary, vinblastine is myelosuppressive (unlike vincristine, which is "
   "neurotoxic), and dacarbazine causes nausea. Match the organ to the drug."),
 h("Oxygen saturation is 94% at rest and 87% after walking", F, "Desaturation on exertion",
   "A resting saturation that falls sharply with exercise is characteristic of a diffusion defect. "
   "The falling carbon monoxide diffusing capacity is the earliest change in bleomycin lung injury "
   "and is what surveillance looks for."),
 h("Fine inspiratory crackles are heard at both lung bases", F, "Interstitial fibrosis",
   "Dry basal crackles with basal reticular opacities describe pulmonary fibrosis, not infection or "
   "heart failure."),
 h("His hemoglobin is 12.6 g/dL, leukocyte count is 5,800/mm3 and platelet count is 214,000/mm3", P,
   "Normal counts point away from the others",
   "Bleomycin is notably NOT myelosuppressive, which is why it is included in the regimen. Normal "
   "counts with new lung disease fit bleomycin and argue against a neutropenic infection. The lung "
   "is uniquely vulnerable because it has little bleomycin hydrolase, the enzyme that inactivates "
   "the drug elsewhere."),
],

84: [
 h("high-dose cyclophosphamide", M, "The toxic metabolite is renally excreted",
   "Cyclophosphamide is metabolized to phosphoramide mustard, the therapeutic alkylator, and "
   "ACROLEIN, a urotoxic by-product that concentrates in the bladder and injures the urothelium "
   "directly."),
 h("suprapubic pain, urinary frequency and gross hematuria with clots", T,
   "Hemorrhagic cystitis",
   "Within 24–48 hours of a high dose. Cystoscopy shows diffuse mucosal edema and punctate "
   "hemorrhage rather than a discrete lesion, because the injury is chemical and affects the whole "
   "surface."),
 h("Urine culture shows no growth, urine cytology shows no malignant cells, and her platelet count "
   "is 96,000/mm3 with normal coagulation studies", W, "The alternatives are excluded",
   "Infection, malignancy and a coagulopathy are all removed, leaving direct chemical injury."),
 h("Which of the following would most likely have prevented this complication?", W,
   "Neutralize the metabolite, not the drug",
   "MESNA contains a sulfhydryl group that binds acrolein in the urine and inactivates it, without "
   "affecting the antitumour phosphoramide mustard. Aggressive hydration with frequent voiding is "
   "the other half. Ifosfamide carries the same risk and always requires mesna."),
],

85: [
 h("numbness and tingling in his fingertips and toes", F, "A length-dependent neuropathy",
   "Symptoms begin in the longest axons — fingertips and toes — and ascend. Loss of ankle reflexes "
   "is typically the earliest objective sign."),
 h("His hemoglobin is 11.9 g/dL, leukocyte count is 6,200/mm3 and platelet count is 226,000/mm3", P,
   "The counts are the point",
   "Essentially normal blood counts during treatment. Vincristine is remarkable for being "
   "relatively NON-myelosuppressive, which is why it can be combined with drugs that are."),
 h("Which of the following best characterizes this drug's dose-limiting toxicity relative to other "
   "agents in its class?", W, "Two vincas, two ceilings",
   "Both bind tubulin and block microtubule assembly in metaphase. What differs is what stops you "
   "escalating: VINCRISTINE is limited by NEUROTOXICITY and spares the marrow, while VINBLASTINE "
   "is limited by MYELOSUPPRESSION. Vincristine is also fatal if given intrathecally — it must "
   "always be dispensed in a minibag, never a syringe."),
],

86: [
 h("Two candidates are monoclonal antibodies of about 145,000 daltons, and two are small molecules "
   "of a few hundred daltons", M, "Size dictates where a drug can act",
   "A 145 kDa immunoglobulin cannot cross an intact plasma membrane. A few-hundred-dalton molecule "
   "diffuses through it readily. This one physical fact determines which targets each modality can "
   "reach."),
 h("the extracellular domain of the epidermal growth factor receptor, the extracellular domain of "
   "HER2, the BCR-ABL1 kinase, and mechanistic target of rapamycin (mTOR)", W,
   "Sort the targets by location",
   "The first two are EXTRACELLULAR and accessible to an antibody from outside — which is why "
   "cetuximab and trastuzumab work. BCR-ABL1 and mTOR are INTRACELLULAR, and reachable only by a "
   "small molecule such as imatinib or everolimus."),
 h("no activity in cell-based assays despite high binding affinity for purified protein", P,
   "Affinity is not access",
   "The antibodies bind their targets perfectly well in a tube, where the protein is exposed. They "
   "fail in cells because they can never get to it. Strong binding in a purified assay with no "
   "cellular activity is the signature of a delivery problem, not a potency problem."),
],

87: [
 h("has completed four cycles of doxorubicin and cyclophosphamide", P, "A compounding exposure",
   "Anthracycline cardiotoxicity is cumulative, dose-dependent and largely IRREVERSIBLE, mediated "
   "by iron-dependent free radical injury. Prior doxorubicin substantially increases the risk of "
   "trastuzumab-associated dysfunction, which is why the two are given sequentially rather than "
   "together."),
 h("a left ventricular ejection fraction of 38%, reduced from 62% before treatment", W,
   "Baseline and serial imaging exist for this",
   "The fall is what matters, and it is only interpretable because a pretreatment value was "
   "recorded. Serial monitoring of ejection fraction is mandatory during HER2-directed therapy."),
 h("Which property of trastuzumab best explains this complication?", W,
   "On-target, off-tumour toxicity",
   "HER2 (ERBB2) is not tumour-specific. It is expressed on CARDIOMYOCYTES, where its signalling "
   "supports survival and repair under stress. Blocking it there produces the cardiac dysfunction "
   "— the drug doing exactly what it was designed to do, in the wrong tissue. Unlike anthracycline "
   "injury, it is usually REVERSIBLE on stopping the drug."),
],

88: [
 h("is receiving nivolumab", M, "Checkpoint blockade releases the brake",
   "Anti-PD-1 antibodies block an inhibitory signal that normally restrains T cells. The resulting "
   "immune-related adverse events are autoimmunity — the mechanism of benefit and the mechanism of "
   "harm are the same."),
 h("Six weeks after the first dose", F, "Typical timing",
   "Immune-related colitis usually appears within the first few weeks to months, and is one of the "
   "commonest and most dangerous toxicities of this class."),
 h("Stool studies are negative for Clostridioides difficile toxin, ova and parasites, and bacterial "
   "pathogens", W, "Infection excluded first",
   "Essential before immunosuppressing a patient with bloody diarrhea. Clostridioides difficile is "
   "the critical exclusion, because treating it with steroids would be harmful."),
 h("a lymphocytic infiltrate with crypt abscesses and apoptotic bodies", F,
   "Histology of immune-mediated colitis",
   "The picture resembles inflammatory bowel disease, which is precisely the point — this is drug-"
   "induced autoimmunity."),
 h("Which of the following is the most appropriate treatment?", W, "Suppress the immune response",
   "High-dose corticosteroids are first-line for grade 3–4 immune-related colitis, with infliximab "
   "or vedolizumab if steroid-refractory. The instinct to treat an infection or to simply stop the "
   "drug is not enough — untreated immune colitis can perforate."),
],

89: [
 h("Eight hours after the infusion", F, "The timing of cytokine release syndrome",
   "Within hours to a few days of the infusion, as the chimeric antigen receptor T cells engage "
   "their target and expand. This is far too early for infection acquired in hospital."),
 h("blood pressure of 80/48 mm Hg that does not respond to 2 L of crystalloid", F,
   "Fluid-refractory shock",
   "Massive release of interleukin-6, interferon gamma and tumour necrosis factor by activated T "
   "cells and bystander macrophages produces distributive shock indistinguishable from sepsis — "
   "which is why cultures are drawn and antibiotics given anyway."),
 h("She is alert and fully oriented, with no focal neurologic findings", W,
   "The other syndrome is excluded",
   "Immune effector cell-associated neurotoxicity syndrome is the second major complication, "
   "presenting with confusion, dysphasia and seizures. It responds to corticosteroids rather than "
   "to interleukin-6 blockade, so distinguishing them changes the drug."),
 h("Which of the following is the most appropriate specific treatment?", W,
   "Block interleukin-6, not the T cells",
   "TOCILIZUMAB is an anti-interleukin-6 receptor antibody and is first-line for severe cytokine "
   "release syndrome. It is preferred over corticosteroids because it does not impair the "
   "engineered T cells, which are the therapy itself."),
],

90: [
 h("has taken tamoxifen for 4 years after surgery for estrogen receptor-positive breast cancer", M,
   "A selective estrogen receptor MODULATOR",
   "Tamoxifen is not a pure blocker. Whether it antagonizes or activates the receptor depends on "
   "which coactivator and corepressor proteins a given tissue expresses."),
 h("3 weeks of vaginal bleeding", F, "Postmenopausal bleeding is never normal",
   "Any bleeding after menopause requires endometrial assessment, and in a woman on tamoxifen the "
   "threshold is lower still."),
 h("an endometrial stripe of 12 mm", F, "An abnormally thick endometrium",
   "Above 4–5 mm in a postmenopausal woman warrants biopsy. Tamoxifen raises the risk of "
   "endometrial hyperplasia, polyps and carcinoma roughly two to three-fold."),
 h("Which of the following best explains this finding?", W, "Antagonist in breast, agonist in uterus",
   "The defining property of the drug. Tamoxifen ANTAGONIZES the estrogen receptor in breast tissue "
   "— the therapeutic effect — while acting as an AGONIST in the endometrium and in bone, which is "
   "why it also preserves bone density. Aromatase inhibitors, which remove estrogen altogether, do "
   "not carry this risk but do accelerate bone loss."),
],

}
