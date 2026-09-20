# Key Findings — vignette highlights for Hardest Exam questions 1–30.
#
# The quiz engine already supports these: getStemHTMLForDisplay() wraps each matched phrase in
# <mark class="vh vh-cat-...">, but ONLY once questionIsSubmitted(index) is true, so nothing is
# revealed until the learner has answered. Clicking a mark opens the side panel; a legend appears
# under the stem listing the categories used.
#
# Rules for authoring:
#   • "text" must appear in the stem VERBATIM. Matching is whitespace-normalised, so a phrase may
#     span the rendered lab table — "Ferritin 6 ng/mL" matches the row whose cells are
#     "Ferritin" / "6 ng/mL" / "20–250 ng/mL" — but never include the "(N=…)" part.
#   • Phrases must not overlap each other; the marker skips a phrase already inside a mark.
#   • Categories: finding | mechanism | term | pattern | workup
#     finding  = the discriminating clinical or laboratory fact
#     mechanism= the process that explains it
#     term     = a named sign or entity worth knowing by name
#     pattern  = an item-writing pattern — a trap, a red herring, or a deliberately closed door
#     workup   = what the question is actually asking, or what a test result rules in or out

F, M, T, P, W = "finding", "mechanism", "term", "pattern", "workup"
EYEBROW = {F: "FINDING", M: "MECHANISM", T: "KEY TERM", P: "PATTERN", W: "WHAT'S ASKED"}


def h(text, cat, title, body):
    return {"text": text, "cat": cat, "eyebrow": EYEBROW[cat], "title": title, "body": body}


HIGHLIGHTS = {

1: [
 h("mildly microcytic red cell indices with normal iron studies", F, "Both parents are carriers",
   "Microcytosis with normal iron studies is thalassemia trait until proven otherwise. Two carrier "
   "parents of the same type is what makes a severe fetal hemoglobinopathy possible."),
 h("fetal ascites, bilateral pleural effusions, scalp edema", T, "Hydrops fetalis",
   "Abnormal fluid in two or more fetal compartments. In this context it is the consequence of "
   "profound intrauterine anemia and high-output cardiac failure."),
 h("a tetramer of four identical non-alpha chains", T, "Hemoglobin Barts",
   "Four gamma chains with no alpha chains at all — the signature of deletion of all four alpha "
   "genes. Hemoglobin Barts has an extremely high oxygen affinity and delivers almost no oxygen "
   "to the tissues."),
 h("numerous clusters of nucleated erythroid precursors lying between the hepatic cords", F,
   "Hematopoiesis in the liver",
   "Erythroid precursors sitting between hepatocytes are the normal fetal picture at this age — "
   "which is exactly what the question is testing, not the pathology."),
 h("In a healthy fetus of this gestational age, which of the following is the principal site of "
   "blood cell production?", W, "Read the ask, not the diagnosis",
   "The vignette hands you a diagnosis of alpha-thalassemia major, then asks something else "
   "entirely: where blood is normally made at 23 weeks. Yolk sac (3–8 weeks) → LIVER (6 weeks to "
   "birth, peak in the second trimester) → marrow (from about 18 weeks, dominant after birth)."),
],

2: [
 h("he was hospitalized for acute hepatitis; viral serologies for hepatitis A, B, and C were "
   "negative", P, "Seronegative hepatitis is the trigger",
   "Hepatitis-associated aplastic anemia classically follows a seronegative hepatitis by one to "
   "three months. The negative serologies are not a dead end — they are the clue."),
 h("Both thumbs and forearms are normal, and there are no skin pigment changes", P,
   "The stem closes a door",
   "Absent or malformed thumbs, short stature and café-au-lait macules would point to Fanconi "
   "anemia, the inherited alternative. These normals are placed here deliberately to exclude it."),
 h("There is no lymphadenopathy or hepatosplenomegaly", W, "Against an infiltrative cause",
   "Leukemia and marrow infiltration usually enlarge nodes, liver or spleen. An empty examination "
   "with a very empty marrow points to failure rather than replacement."),
 h("Reticulocyte count  0.2%", F, "Hypoproliferative",
   "A reticulocyte count this low with a hemoglobin of 6.9 g/dL proves the marrow is not "
   "responding. The problem is production, not destruction or loss."),
 h("Peripheral smear shows no blasts", W, "Pancytopenia without blasts",
   "Three lineages down with no circulating blasts shifts the differential toward aplastic anemia "
   "and away from acute leukemia — but the marrow biopsy is what settles it."),
],

3: [
 h("hemodialysis 3 times weekly for 2 years", F, "The source of the deficiency",
   "The peritubular fibroblasts that sense hypoxia and make erythropoietin are lost as kidney "
   "tissue is destroyed. Dialysis replaces filtration, not endocrine function."),
 h("Erythropoietin  11 mU/mL", F, "Inappropriately normal",
   "This is the trap. The value sits inside the reference range, but that range applies to people "
   "with a normal hemoglobin. At a hemoglobin of 8.6 g/dL a healthy kidney would drive "
   "erythropoietin many-fold higher. Normal here means failed."),
 h("Transferrin saturation  29%", P, "Iron is not the problem",
   "Adequate saturation with a ferritin above the reference range rules out iron deficiency as the "
   "primary cause — a common confounder in dialysis patients, deliberately excluded here."),
 h("Stool is negative for occult blood", W, "Against blood loss",
   "Together with a normal spleen and a normal lactate dehydrogenase, this narrows the tree: not "
   "loss, not destruction, therefore underproduction."),
],

4: [
 h("a sore, smooth tongue", T, "Atrophic glossitis",
   "Loss of the filiform papillae from megaloblastic change in a rapidly dividing epithelium. The "
   "same DNA synthesis defect that enlarges the red cells also affects the tongue and gut."),
 h("hypothyroidism treated with levothyroxine", P, "An autoimmune cluster",
   "Autoimmune thyroid disease travels with autoimmune gastritis. One autoimmune diagnosis in the "
   "stem is an invitation to look for another."),
 h("Lactate dehydrogenase  1,850 U/L", F, "Enormous lactate dehydrogenase",
   "Values in the thousands, far higher than most peripheral hemolysis produces, come from cells "
   "dying inside the marrow before they ever reach the circulation."),
 h("Reticulocyte count  0.6%", P, "The paradox that names the mechanism",
   "Hemolysis markers are up — high lactate dehydrogenase, raised bilirubin — yet the reticulocyte "
   "count is not. Destruction with no compensatory output means the cells are being destroyed "
   "where they are made. That is ineffective erythropoiesis."),
 h("Direct antiglobulin test is negative", W, "Not autoimmune",
   "A negative direct Coombs test removes autoimmune hemolytic anemia, the obvious competing "
   "explanation for a raised bilirubin and lactate dehydrogenase."),
],

5: [
 h("vitiligo and Hashimoto thyroiditis", P, "The autoimmune neighbourhood",
   "Vitiligo and Hashimoto thyroiditis cluster with autoimmune atrophic gastritis. The stem is "
   "pointing at pernicious anemia before a single laboratory value appears."),
 h("decreased vibration and position sense in both great toes and a positive Romberg sign", F,
   "Dorsal column disease",
   "Subacute combined degeneration — demyelination of the dorsal columns and corticospinal tracts. "
   "It is caused by vitamin B12 deficiency and NOT by folate deficiency, which is why the two must "
   "never be treated interchangeably."),
 h("Methylmalonic acid  1,240 nmol/L", F, "The test that separates B12 from folate",
   "Methylmalonic acid rises only in B12 deficiency; homocysteine rises in both. Elevated MMA "
   "makes this B12, not folate."),
 h("Anti-parietal cell antibodies are positive", M, "Autoimmune destruction of parietal cells",
   "No parietal cells means no intrinsic factor, so B12 cannot be absorbed in the terminal ileum — "
   "and it also means achlorhydria and chronic atrophic gastritis."),
 h("requires ongoing surveillance for which of the following", W, "The ask is long-term risk",
   "Replacing B12 fixes the anemia and halts the neurologic damage, but it does nothing about the "
   "atrophied stomach. Pernicious anemia carries a roughly threefold increased risk of gastric "
   "adenocarcinoma, and also of gastric carcinoid."),
],

6: [
 h("When a home pregnancy test became positive at 9 weeks' gestation, she began a daily prenatal "
   "vitamin", P, "Correct supplement, wrong week",
   "This is the entire question. The neural tube closes by about the fourth week after conception "
   "— before most women know they are pregnant. Supplementation starting at 9 weeks cannot prevent "
   "a defect that formed five weeks earlier."),
 h("Her serum folate at the first prenatal visit was within normal limits", P, "A red herring",
   "A normal folate level measured after the tube has already closed tells you nothing about "
   "folate status during the window that mattered. Do not let a reassuring number distract from "
   "the timeline."),
 h("covered only by a thin membrane through which neural tissue is visible", T, "Myelomeningocele",
   "Neural tissue within the sac distinguishes myelomeningocele from a meningocele, which contains "
   "only meninges and cerebrospinal fluid and spares motor function."),
 h("the infant does not move his lower extremities", F, "Neurological deficit below the lesion",
   "Motor loss confirms that functioning neural tissue is involved rather than merely displaced."),
],

7: [
 h("A guaiac-based fecal occult blood test 6 months ago was negative", P,
   "A negative screen does not exclude a tumour",
   "Colonic neoplasms bleed intermittently, so a single negative guaiac test is weak evidence. "
   "Proven iron deficiency in an older adult overrides a negative stool test every time."),
 h("He has no abdominal pain and has not noticed black or bloody stools", P, "Silence is expected",
   "Right-sided lesions bleed slowly into a large-calibre, liquid-content caecum. The blood is "
   "diluted and digested, so the patient presents with anemia rather than with visible bleeding — "
   "which is precisely why they present late."),
 h("Mean corpuscular volume  71 µm3", F, "Microcytosis",
   "Too little hemoglobin per cell means smaller cells. The microcytic differential is iron "
   "deficiency, thalassemia, anemia of chronic disease and sideroblastic anemia."),
 h("Ferritin  6 ng/mL", F, "Empty iron stores",
   "A ferritin this low is essentially diagnostic of iron deficiency — one of the few numbers in "
   "hematology that needs no supporting evidence. Ferritin is an acute-phase reactant, so it can "
   "be falsely raised, but it is never falsely low."),
 h("Red cell distribution width  18.6%", F, "Anisocytosis",
   "A raised distribution width says the cell population is not uniform — new small cells being "
   "produced alongside older normal ones. It rises early in iron deficiency and is typically "
   "normal in thalassemia trait."),
],

8: [
 h("rheumatoid arthritis for 15 years, with persistently swollen metacarpophalangeal joints "
   "despite treatment", F, "Active, ongoing inflammation",
   "Not merely a history of inflammatory disease but uncontrolled disease now — which is what "
   "drives the interleukin-6 and hepcidin response."),
 h("Total iron-binding capacity  198 µg/dL", F, "Low, and that is the discriminator",
   "This single value separates the two commonest microcytic anemias. In iron deficiency, "
   "transferrin production rises and the binding capacity goes UP. In anemia of inflammation it "
   "goes DOWN. They move in opposite directions."),
 h("Ferritin  390 ng/mL", F, "Stores are full",
   "Ferritin is both an iron-storage protein and an acute-phase reactant, so it rises twice over "
   "here. High ferritin with low serum iron means the iron exists but is locked away."),
 h("Colonoscopy a year ago was normal", W, "Occult loss excluded",
   "The stem removes gastrointestinal bleeding, which would otherwise be the obvious explanation "
   "for a low serum iron in an older patient."),
],

9: [
 h("Mean corpuscular volume  90 µm3", P, "A normal number hiding two diseases",
   "The mean corpuscular volume is a MEAN. A population of very small iron-deficient cells mixed "
   "with very large B12-deficient cells averages to something normal. A normal value never "
   "excludes a mixed deficiency."),
 h("Red cell distribution width  22.4%", F, "The number that gives it away",
   "This is what exposes the average. A markedly raised distribution width with a normal mean "
   "volume is the fingerprint of two coexisting populations — always look at it before trusting "
   "the mean."),
 h("Roux-en-Y gastric bypass surgery", M, "One operation, two deficiencies",
   "The bypass excludes the duodenum and proximal jejunum, where iron is absorbed, and reduces "
   "acid and intrinsic factor, which B12 needs. Both deficiencies follow from one anatomical "
   "change."),
 h("She stopped taking her prescribed supplements 3 years ago", F, "The precipitant",
   "Post-bypass supplementation is lifelong. Hepatic B12 stores last years, which is why the "
   "interval between stopping and symptoms is so long."),
],

10: [
 h("a house built in 1938 that is being renovated, and she often chews on windowsills", F,
   "Lead exposure, spelled out",
   "Housing built before the 1978 residential lead paint ban, active renovation disturbing that "
   "paint, and pica. The exposure history is doing most of the diagnostic work."),
 h("She no longer uses several words she had learned", F, "Developmental regression",
   "Losing acquired milestones is never normal and is a hallmark of lead neurotoxicity in a "
   "toddler. Cognitive effects occur at levels well below those that cause anemia."),
 h("Zinc protoporphyrin  180 µg/dL", M, "Ferrochelatase is blocked",
   "Lead inhibits ferrochelatase, the enzyme that inserts iron into protoporphyrin IX. Zinc takes "
   "iron's place instead, so zinc protoporphyrin accumulates. Lead also inhibits "
   "delta-aminolevulinic acid dehydratase earlier in the pathway."),
 h("Ferritin  46 ng/mL", P, "Microcytic, but not iron deficient",
   "Normal iron stores exclude the default explanation for a microcytic anemia in a toddler and "
   "force you toward the other causes — here, impaired heme synthesis."),
],

11: [
 h("blisters on the backs of his hands that appear after he works in his garden and heal with "
   "scarring", F, "Photosensitive blistering",
   "Accumulated porphyrins absorb light and generate reactive oxygen species in sun-exposed skin. "
   "The dorsum of the hand is the classic site, and healing with scarring and milia is typical."),
 h("new, darker hair growing over his cheeks and temples", T, "Hypertrichosis",
   "Excess facial hair in the malar and temporal regions is a characteristic and often overlooked "
   "feature of porphyria cutanea tarda."),
 h("He has no abdominal pain, weakness, or mood change", P, "The negatives sort the porphyrias",
   "Porphyria cutanea tarda is purely cutaneous. Acute intermittent porphyria is the opposite — "
   "neurovisceral attacks with abdominal pain, weakness and psychiatric change, and NO skin "
   "findings. The stem separates them for you."),
 h("chronic hepatitis C infection and drinks 6 beers daily", M, "Iron-loading cofactors",
   "Hepatitis C, alcohol, estrogen and HFE mutations all inhibit hepatic uroporphyrinogen "
   "decarboxylase by increasing hepatic iron. Their common thread is iron — which is what the "
   "question is driving at."),
],

12: [
 h("mechanical aortic valve replacement", M, "A mechanical cause of hemolysis",
   "Red cells are sheared as they pass a prosthetic surface or a high-velocity regurgitant jet. "
   "This is macroangiopathic hemolysis — the same physics as a march hemoglobinuria, at a "
   "different scale from the microangiopathies."),
 h("new moderate paravalvular leak", F, "The new lesion explains the new anemia",
   "A leak around the sewing ring creates a narrow, high-velocity jet. Blood forced through it at "
   "speed is destroyed in the circulation, not in the spleen."),
 h("The plasma of a centrifuged blood sample is pink", F, "Free hemoglobin in plasma",
   "Pink plasma means hemoglobin has been released INSIDE the vessels. In extravascular hemolysis "
   "the cells are removed intact by macrophages and the plasma stays straw-coloured."),
 h("Haptoglobin less than  10 mg/dL", M, "Haptoglobin has been consumed",
   "Haptoglobin binds free plasma hemoglobin and the complex is cleared by the liver. An "
   "unmeasurable level means the binding capacity has been saturated and exceeded."),
 h("Direct antiglobulin test is negative", W, "Mechanical, not immune",
   "This removes autoimmune hemolysis and confirms that the destruction is physical. The question "
   "then follows the iron: filtered hemoglobin is reabsorbed by tubular cells, stored as "
   "hemosiderin, and shed in the urine days later."),
],

13: [
 h("Her father had his spleen removed as a teenager", P, "Autosomal dominant inheritance",
   "An affected parent who needed a splenectomy at the same age is the family pattern of "
   "hereditary spherocytosis, which is dominant in about 75% of cases."),
 h("Mean corpuscular hemoglobin concentration  37.8%", F, "A genuinely rare abnormality",
   "The MCHC is almost always normal. A value above 36% has a very short differential: hereditary "
   "spherocytosis, cold agglutinins or a lipemic sample. Losing membrane without losing hemoglobin "
   "concentrates the contents of the cell."),
 h("episodes of yellow eyes since early childhood, usually during viral illnesses", F,
   "Chronic compensated hemolysis",
   "Lifelong intermittent jaundice that worsens with intercurrent illness indicates a chronic "
   "hemolytic state that is usually compensated and tips over under stress."),
 h("Direct antiglobulin test is negative", W, "Spherocytes without antibody",
   "Spherocytes have two common causes: a membrane protein defect and warm autoimmune hemolysis. "
   "A negative Coombs test removes the second, leaving the vertical cytoskeletal linkage — most "
   "often ankyrin."),
],

14: [
 h("Three days ago he began trimethoprim-sulfamethoxazole", F, "An oxidant drug",
   "Sulfonamides, dapsone, nitrofurantoin, primaquine and rasburicase impose oxidative stress. In "
   "a G6PD-deficient cell there is no spare reducing capacity to absorb it."),
 h("His family emigrated from Sardinia", P, "Geography names the variant",
   "The Mediterranean variant has far lower residual enzyme activity than the African A− variant, "
   "so the hemolysis is more severe and involves cells of all ages rather than only the oldest."),
 h("a similar episode as a child after eating broad beans", T, "Favism",
   "Fava beans contain divicine and isouramil, which generate reactive oxygen species directly. A "
   "recurrent trigger-related history makes an inherited enzyme defect far more likely than an "
   "acquired process."),
 h("Direct antiglobulin test is negative", W, "Not an antibody problem",
   "Episodic hemolysis tied to specific exposures, with a negative Coombs test, points to an "
   "intrinsic enzyme defect rather than to immune destruction."),
],

15: [
 h("His parents are first cousins of Cypriot descent", P, "Consanguinity plus geography",
   "Two carriers of a recessive condition from a high-prevalence Mediterranean population — the "
   "set-up for a homozygous beta-globin defect."),
 h("was well until about 6 months of age", M, "The globin switch is the clock",
   "Fetal hemoglobin uses gamma chains and needs no beta chains, so an affected infant is "
   "protected in utero and in early infancy. Disease appears only as gamma production falls and "
   "beta should take over — and cannot."),
 h("frontal bossing, prominent maxillae", F, "Marrow expansion",
   "Extreme erythropoietic drive expands the marrow cavity and thins the cortex, producing the "
   "facial changes and the hair-on-end skull. These are the bony consequences of ineffective "
   "erythropoiesis."),
 h("Hemoglobin A is not detected", F, "Beta-zero, not beta-plus",
   "Absent rather than reduced hemoglobin A means no functional beta chains are made at all. The "
   "alpha chains produced in normal quantity then have no partner."),
],

16: [
 h("emergency splenectomy for a shattered spleen", M, "The filter is gone",
   "The spleen clears poorly opsonized encapsulated organisms from the blood and houses the "
   "marginal-zone B cells that mount T-independent responses to polysaccharide antigens. Both "
   "functions are lost."),
 h("he did not attend follow-up visits", P, "The preventable part",
   "Vaccination against pneumococcus, meningococcus and Haemophilus influenzae type b, and "
   "antibiotic prophylaxis, are what stand between an asplenic patient and this presentation."),
 h("gram-positive, lancet-shaped diplococci that are optochin-sensitive", T,
   "Streptococcus pneumoniae",
   "Lancet-shaped gram-positive diplococci that are optochin-sensitive and bile-soluble. It is the "
   "commonest cause of overwhelming post-splenectomy infection by a wide margin."),
 h("Platelet count is 31,000/mm3, fibrinogen is 70 mg/dL, and prothrombin time is prolonged", F,
   "Disseminated intravascular coagulation",
   "Consumption of platelets and fibrinogen with prolonged clotting times. The skin changes that "
   "follow are purpura fulminans — dermal microvascular thrombosis with hemorrhagic necrosis."),
],

17: [
 h("time-averaged mean maximum velocity of 228 cm/sec in the left middle cerebral artery", F,
   "An abnormal transcranial Doppler",
   "Velocity of 200 cm/sec or more marks a child at high risk of a first overt stroke — of the "
   "order of 10% per year untreated. Flow is fast because the vessel lumen is narrowed."),
 h("confirmed on repeat study", W, "Confirm before committing",
   "A single abnormal study is repeated before starting a therapy that means transfusion every "
   "three to four weeks for years, with the iron overload that follows."),
 h("She takes hydroxyurea and folic acid", P, "The trap is to escalate what she is on",
   "Hydroxyurea raises fetal hemoglobin and reduces pain crises and acute chest syndrome. It is "
   "not the evidence-based answer to an abnormal transcranial Doppler — the STOP trial established "
   "chronic transfusion for primary stroke prevention."),
 h("She has had two vaso-occlusive pain episodes this year", P, "A different problem",
   "Pain frequency and stroke risk are separate axes. The Doppler is not telling you about her "
   "pain, and treating her pain will not address what the Doppler found."),
],

18: [
 h("a low-grade fever and a red rash on both cheeks", T, "Slapped cheek",
   "Erythema infectiosum — fifth disease — from parvovirus B19. In a healthy child the rash IS the "
   "illness; in a child with chronic hemolysis it is a warning shot."),
 h("Reticulocyte count  0.1%", F, "The switch that makes the diagnosis",
   "Sudden anemia in a chronic hemolytic patient has two explanations, and the reticulocyte count "
   "separates them. HIGH means the cells are being lost or destroyed faster. LOW means production "
   "has stopped — a transient aplastic crisis."),
 h("Hemoglobin  3.9 g/dL", F, "A precipitous fall from baseline",
   "From a baseline of 8.2 g/dL. Red cell survival in sickle cell disease is roughly 10–20 days "
   "instead of 120, so even a brief halt in production causes the hemoglobin to collapse."),
 h("The spleen is not palpable", W, "Splenic sequestration excluded",
   "The other cause of abrupt anemia in sickle cell disease is splenic sequestration — but that "
   "presents with a rapidly ENLARGING spleen and a HIGH reticulocyte count. By age 4 this child "
   "has probably already auto-infarcted the organ."),
],

19: [
 h("Placental abruption", M, "A massive tissue factor load",
   "Decidual and placental tissue is extraordinarily rich in tissue factor. Releasing it into the "
   "maternal circulation triggers systemic thrombin generation — the classic obstetric cause of "
   "disseminated intravascular coagulation."),
 h("Fibrinogen  78 mg/dL", F, "The critical deficit",
   "Fibrinogen is the substrate thrombin converts to clot, and in obstetric hemorrhage it is the "
   "first factor to reach a critical level. Below roughly 100–150 mg/dL, bleeding will not stop "
   "whatever else is corrected."),
 h("She has already received 4 units of red blood cells and 4 units of plasma", P,
   "Plasma has already failed here",
   "Plasma contains fibrinogen, but too dilutely to raise a level this low without enormous "
   "volumes. Cryoprecipitate is the concentrated source — fibrinogen, factor VIII, von Willebrand "
   "factor, factor XIII and fibronectin."),
 h("D-dimer  6,400 ng/mL", F, "Thrombin and plasmin are both active",
   "D-dimer is a cross-linked fibrin degradation product, so it proves that clot has been formed "
   "and then broken down. Together with the low fibrinogen and the fragments on the smear it "
   "confirms consumption rather than dilution."),
],

20: [
 h("The implicated plasma came from a woman with 4 prior pregnancies", F, "A multiparous donor",
   "Pregnancy exposes a woman to paternal HLA antigens, and repeated pregnancies generate "
   "anti-HLA antibodies — 14%–20% of women who have been pregnant carry them. Donor anti-HLA or "
   "anti-NEUTROPHIL antibodies bind the recipient's neutrophils, which are activated and sequestered "
   "in the pulmonary capillaries, damaging the endothelium and causing permeability edema. This is "
   "why blood centres screen female donors and avoid high-plasma-volume products from them."),
 h("Jugular venous pressure is not elevated", P, "The finding that splits the differential",
   "Transfusion-related acute lung injury and circulatory overload both present with dyspnea and "
   "bilateral infiltrates within hours. Overload raises filling pressures; TRALI does not."),
 h("serum brain natriuretic peptide is normal", W, "Against volume overload",
   "A normal natriuretic peptide with a normal cardiac silhouette argues that the edema is "
   "permeability-driven rather than hydrostatic."),
 h("blood pressure is 84/50 mm Hg", P, "TRALI is hypotensive",
   "Another discriminator pointing the same way: circulatory overload typically raises blood "
   "pressure, whereas TRALI is usually accompanied by fever and hypotension."),
],

21: [
 h("started on warfarin; no parenteral anticoagulant was given", P, "The omission is the answer",
   "Warfarin must be overlapped with a parenteral anticoagulant precisely because of what happens "
   "in the first days. Starting it alone is what allows this lesion."),
 h("Her brother had an unprovoked pulmonary embolism at age 30", F, "An inherited deficiency",
   "A young unprovoked event in a first-degree relative suggests hereditary protein C or protein S "
   "deficiency — patients whose baseline level is already low have the least reserve to lose."),
 h("fibrin thrombi occluding dermal and subcutaneous venules", F, "Thrombosis, not inflammation",
   "Occlusion of small vessels by fibrin with necrosis of the tissue they supply confirms a "
   "thrombotic lesion. Fat-rich areas — breast, buttock, thigh — are characteristically affected."),
 h("no vasculitis", W, "A competing diagnosis excluded",
   "Absence of vessel wall inflammation removes vasculitis, which would otherwise be a reasonable "
   "explanation for a painful necrotic skin lesion."),
],

22: [
 h("with an international normalized ratio consistently between 2.2 and 2.6 at monthly checks", P,
   "Years of stability means look for a change",
   "A patient stable for three years has not suddenly become warfarin-sensitive. When a stable "
   "level moves sharply, something new was added."),
 h("Five days ago he was prescribed fluconazole", F, "The new variable",
   "Azole antifungals are potent inhibitors of CYP2C9, the enzyme that clears the more active "
   "S-enantiomer of warfarin. Less clearance means more drug and a higher INR, and the timing — "
   "days, not hours — fits the turnover of the clotting factors."),
 h("He takes no other new medications, has not changed his diet, and does not drink alcohol", P,
   "The stem closes every other door",
   "Dietary vitamin K, alcohol and other interacting drugs are all explicitly excluded, which is "
   "the item writer telling you the answer is the one exposure that is left."),
 h("International normalized ratio  6.9", F, "Markedly supratherapeutic",
   "The degree of prolongation, not just its presence, drives management — and with active "
   "bleeding it means reversal rather than simply withholding doses."),
],

23: [
 h("began 90 minutes ago", P, "Inside the window",
   "Thrombolysis was appropriately given. The complication that follows is an inherent risk of the "
   "drug, not a protocol error — do not look for a mistake that is not there."),
 h("Noncontrast head computed tomography shows no hemorrhage", W, "The scan that permitted the drug",
   "Its only job before thrombolysis is to exclude hemorrhage. It does not need to show the "
   "infarct, which is usually invisible this early."),
 h("intravenous alteplase is started", M, "A plasminogen activator",
   "Alteplase is recombinant tissue plasminogen activator. It converts plasminogen to plasmin, and "
   "plasmin degrades fibrin — in the occluding thrombus, and equally in hemostatic plugs "
   "elsewhere."),
 h("he develops a severe headache, vomiting, and a declining level of consciousness", F,
   "Hemorrhagic transformation",
   "Sudden headache, vomiting and falling consciousness after thrombolysis is intracranial "
   "hemorrhage until proven otherwise. It complicates 2%–6% of treated strokes."),
],

24: [
 h("at 9 weeks' gestation", P, "Pregnancy decides the drug class",
   "Warfarin is teratogenic and crosses the placenta; the direct oral anticoagulants are not "
   "established in pregnancy and also cross. Low molecular weight heparin is a large, negatively "
   "charged molecule that does not cross at all."),
 h("noncompressible left popliteal vein with thrombus extending into the femoral vein", F,
   "Proximal deep vein thrombosis",
   "Loss of compressibility is the diagnostic finding on ultrasonography. Proximal extension means "
   "full anticoagulation rather than surveillance."),
 h("Serum creatinine is 0.7 mg/dL", W, "Renal function permits it",
   "Low molecular weight heparin is renally cleared and accumulates when the creatinine clearance "
   "falls below about 30 mL/min. Normal function here makes it safe and removes the need for "
   "unfractionated heparin."),
],

25: [
 h("which he has taken without missing a dose", P, "Non-adherence is deliberately excluded",
   "Stopping antiplatelet therapy is the commonest cause of stent thrombosis, so the stem removes "
   "it explicitly. When the obvious answer is closed off, look for a pharmacologic reason."),
 h("Two weeks ago his primary physician added omeprazole", F, "The new drug",
   "Omeprazole inhibits CYP2C19, and the timing fits: the stent was fine for a week on clopidogrel "
   "alone and thrombosed two weeks after the interacting drug started."),
 h("clopidogrel", M, "A prodrug, and that is the whole point",
   "Clopidogrel is inactive as swallowed and needs CYP2C19 to generate its active metabolite, "
   "which then irreversibly blocks P2Y12. Inhibit that enzyme and you inhibit the drug. Prasugrel "
   "and ticagrelor do not depend on CYP2C19, and pantoprazole is the safer acid suppressant."),
 h("a fresh occlusive thrombus within the previously placed stent", F, "Stent thrombosis",
   "A platelet-rich white clot on an incompletely endothelialized stent strut. It presents as an "
   "ST-elevation infarct and carries high mortality."),
],

26: [
 h("multiple radiopaque tablets in the stomach", F, "Iron is radiopaque",
   "Most tablets are invisible on radiography; iron salts are not. Visible tablets both confirm "
   "the ingestion and justify whole-bowel irrigation."),
 h("vomited five times, twice with blood, and has had two episodes of bloody diarrhea", F,
   "Direct corrosive injury",
   "Stage one of iron poisoning is local: iron is directly caustic to gastrointestinal mucosa, "
   "producing hematemesis and bloody diarrhea within the first six hours."),
 h("Anion gap  24 mEq/L", M, "Free iron poisons mitochondria",
   "Iron beyond the binding capacity of transferrin enters cells and uncouples oxidative "
   "phosphorylation, forcing anaerobic metabolism. The resulting lactic acidosis is what the wide "
   "anion gap is measuring."),
 h("She is lethargic", W, "A marker of systemic toxicity",
   "Lethargy, shock and acidosis define systemic rather than purely local poisoning, and that is "
   "the threshold for chelation with deferoxamine."),
],

27: [
 h("His hemoglobin was 9.2 g/dL two weeks ago and is 10.9 g/dL today", F, "Rising too fast",
   "A rise of more than about 1 g/dL in two weeks is itself an indication to reduce the dose, "
   "independent of the absolute value. The rate of change matters as much as the destination."),
 h("Blood pressure is 176/102 mm Hg, compared with 138/84 mm Hg before treatment was started", F,
   "Erythropoiesis-stimulating agent hypertension",
   "New or worsening hypertension is the commonest serious adverse effect, driven by rising "
   "viscosity and direct vasoconstriction. The pre-treatment comparison is given so the change is "
   "unmistakable."),
 h("He reports a dull headache for several days", F, "A warning symptom",
   "Headache accompanying a rapid hemoglobin rise and new hypertension is a recognized prelude to "
   "hypertensive encephalopathy and seizures."),
 h("Ferritin is 420 ng/mL", P, "Not an iron problem",
   "Iron stores are replete and the saturation is adequate, so the answer is not to add iron — "
   "which is otherwise the commonest reason an erythropoiesis-stimulating agent is not working."),
],

28: [
 h("Two weeks ago she misread a new prescription label and has been taking 15 mg daily", F,
   "Weekly dose taken daily",
   "The classic and frequently fatal methotrexate error. A weekly rheumatologic dose given daily "
   "produces a cumulative exposure resembling chemotherapy."),
 h("confluent oral ulceration", F, "Mucositis",
   "The gut epithelium and the marrow are the two fastest-dividing tissues in the body, so both "
   "declare an antimetabolite toxicity first. Mucositis and pancytopenia together are the "
   "signature."),
 h("macro-ovalocytes and hypersegmented neutrophils", M, "A megaloblastic picture without a "
   "vitamin deficiency",
   "Methotrexate inhibits dihydrofolate reductase, blocking regeneration of tetrahydrofolate and "
   "so halting thymidine synthesis. The marrow cannot tell the difference between this and dietary "
   "folate deficiency, which is why the smear looks identical."),
 h("Creatinine  1.1 mg/dL", W, "Renal function is preserved",
   "Methotrexate is renally excreted, so impairment would both explain the toxicity and change "
   "management. A normal creatinine points at the dosing error as the sole cause — and means "
   "rescue therapy can be expected to work."),
],

29: [
 h("Temperature is 35.6 C (96.1 F)", P, "Hypothermia counts too",
   "Three of the four SIRS criteria are bidirectional. A LOW temperature satisfies the criterion "
   "exactly as a fever does, and in an older patient it carries a worse prognosis — yet it is "
   "routinely misread as evidence against infection."),
 h("leukocyte count is 3,200/mm3 with 14% band forms", P, "A low count with a left shift",
   "Leukopenia below 4,000/mm3 qualifies, and so would a normal count with more than 10% immature "
   "forms. Both boxes are ticked here. A 'normal-looking' white cell count is not reassurance."),
 h("serum lactate is 4.6 mmol/L", M, "The metabolic acidosis",
   "Hypoperfusion forces anaerobic metabolism and lactate accumulates, consuming bicarbonate. This "
   "is also the marker of the cellular and metabolic derangement in the septic shock definition, "
   "which is why it sits in the treatment bundle."),
 h("respirations are 26/min", M, "The respiratory alkalosis",
   "Tachypnea blows off carbon dioxide, lowering the PaCO2 and raising the pH. It occurs alongside "
   "the acidosis rather than after it, which is why the classic sepsis gas shows both "
   "simultaneously."),
],

30: [
 h("positive for influenza A by polymerase chain reaction", F, "A viral trigger",
   "Sepsis is defined by the host response, not by the organism. A virus can produce identical "
   "organ dysfunction, and viral causes are consistently underdiagnosed."),
 h("Blood, urine and sputum cultures show no growth at 48 hours", P,
   "Negative cultures do not exclude sepsis",
   "No organism is identified in 30%–50% of all sepsis cases. Culture negativity is so common that "
   "it carries almost no weight against the diagnosis."),
 h("procalcitonin is within normal limits", W, "Against a bacterial trigger",
   "Procalcitonin is the one marker in the sepsis laboratory panel that points at a cause rather "
   "than at severity, and elevation indicates bacterial infection. A normal value here argues "
   "against bacterial co-infection."),
 h("serum beta-D-glucan is negative", W, "Against a fungal trigger",
   "Beta-D-glucan detects fungal cell wall polysaccharide. A negative result removes the third "
   "class of pathogen and leaves the virus as the initiating insult — which acts through "
   "damage-associated molecular patterns released from injured host tissue, not through "
   "pathogen-associated patterns."),
],

}
