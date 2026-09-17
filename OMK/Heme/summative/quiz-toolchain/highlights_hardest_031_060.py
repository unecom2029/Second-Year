# Key Findings — vignette highlights for Hardest Exam questions 31–60.
# Authoring rules and categories: see highlights_hardest_001_030.py and QUIZ_BUILD_METHOD.md.

F, M, T, P, W = "finding", "mechanism", "term", "pattern", "workup"
EYEBROW = {F: "FINDING", M: "MECHANISM", T: "KEY TERM", P: "PATTERN", W: "WHAT'S ASKED"}


def h(text, cat, title, body):
    return {"text": text, "cat": cat, "eyebrow": EYEBROW[cat], "title": title, "body": body}


HIGHLIGHTS = {

31: [
 h("resistance testing shows mutations affecting reverse transcriptase, integrase and protease", P,
   "Every pol product is already lost",
   "Reverse transcriptase, integrase and protease are all encoded by pol. With all three "
   "compromised, salvage has to attack a different step of the life cycle — which is why an entry "
   "inhibitor was chosen."),
 h("subcutaneous enfuvirtide", T, "The fusion inhibitor",
   "Enfuvirtide binds gp41 and prevents the conformational change that fuses the viral and cell "
   "membranes. It is the only antiretroviral given by subcutaneous injection, which is itself a "
   "clue to its identity."),
 h("a new amino acid substitution in the viral fusion protein, which no longer binds the drug", M,
   "One substitution is enough",
   "gp41 IS the fusion protein. A single amino acid change in its drug-binding domain abolishes "
   "enfuvirtide binding — a low genetic barrier, like the NNRTIs and unlike the protease "
   "inhibitors."),
 h("The altered protein is a product of which of the following viral genes?", W,
   "The ask is the gene, not the drug",
   "Work backwards: drug → target protein → gene. env encodes a gp160 precursor that HOST protease "
   "cleaves into gp120 (binds CD4 and a chemokine co-receptor) and gp41 (fusion). gag gives p24, "
   "p17 and the nucleocapsid proteins; pol gives the three enzymes."),
],

32: [
 h("antiretroviral therapy was started the same week", F, "A very recent start",
   "Immune reconstitution inflammatory syndrome occurs in the first few months after starting "
   "therapy, at a median of about 48 days. The interval here fits exactly."),
 h("she had no opportunistic infection at that time", P, "Unmasking, not paradoxical",
   "This is the fork. PARADOXICAL IRIS worsens an infection already diagnosed and being treated. "
   "UNMASKING IRIS reveals one that was never diagnosed — the inflammation is what makes it "
   "visible."),
 h("Today her CD4 count is 165/mm3 and her HIV RNA is 780 copies/mL", F,
   "A robust response is a risk factor",
   "A very low pretreatment CD4 count with a high viral load, followed by a steep fall in viral "
   "load and a rising CD4 count, is the setting for IRIS. Improving numbers alongside a "
   "deteriorating patient is the combination that separates it from treatment failure."),
 h("several new areas of faint peripheral enhancement and surrounding edema", M,
   "Enhancement is the immune system arriving",
   "Progressive multifocal leukoencephalopathy normally produces non-enhancing lesions with no "
   "mass effect, because there is no immune response to mount. New enhancement and edema mean "
   "recovering lymphocytes have reached the lesions."),
],

33: [
 h("fever with rigors and sweats occurring at no discernible interval", P,
   "Irregular fever names the species",
   "The fever period equals the erythrocytic cycle length — 24 hours for P. knowlesi, 48 for vivax "
   "and ovale, 72 for malariae. Falciparum's cycles are NOT synchronized, so there is no rhythm "
   "and no fever-free window in which the patient recovers."),
 h("returned 2 weeks ago from a 3-month stay in Nigeria and took no chemoprophylaxis", F,
   "Geography plus no prophylaxis",
   "Sub-Saharan Africa means falciparum until proven otherwise. The two-week interval fits the 1–4 "
   "week incubation created by the silent pre-erythrocytic liver stage."),
 h("confusion and a generalized seizure", T, "Cerebral malaria",
   "Infected red cells sequester in cerebral capillaries, causing infarction and capillary leak. "
   "It is a medical emergency — patients can die within 24 hours."),
 h("dark brown-black granular pigment", M, "Hemozoin, and the drug target",
   "The parasite digests hemoglobin for amino acids, liberating heme that is toxic to itself. Heme "
   "polymerase converts it to inert hemozoin. Chloroquine, quinine and mefloquine block that step "
   "so the parasite is poisoned by its own waste."),
],

34: [
 h("He has several cats at home, one of them a kitten", F, "The exposure",
   "Bartonella henselae passes between cats by the cat flea and reaches humans through a scratch "
   "carrying flea feces. Kittens are the likeliest source."),
 h("a lobular proliferation of small capillaries lined by plump endothelial cells", F,
   "Vascular proliferation, not malignancy",
   "This is what separates bacillary angiomatosis from Kaposi sarcoma on tissue. Kaposi shows "
   "spindle cells forming slit-like vascular spaces; here the vessels are capillaries with plump "
   "endothelium and neutrophils."),
 h("stain black on Warthin-Starry silver stain", F, "Argyrophilic organisms",
   "The granular purple clumps are masses of bacteria, and silver confirms it. The short "
   "argyrophilic list is Bartonella, spirochetes, Legionella and Helicobacter pylori."),
 h("Bartonella serology is negative", P, "A meaningless negative",
   "Serology measures the host's antibody response, and a patient with a CD4 count of 44 may make "
   "very little. This is why bacillary angiomatosis is diagnosed on biopsy."),
 h("which of the following is the most appropriate treatment?", W, "Two diseases, two drugs",
   "Same organism, different disease, different antibiotic. Cat scratch disease in an "
   "immunocompetent host gets AZITHROMYCIN. Bacillary angiomatosis gets ERYTHROMYCIN and/or "
   "DOXYCYCLINE — plus antiretroviral therapy, because antibiotics alone will not hold a host who "
   "cannot help."),
],

35: [
 h("camping in rural New Mexico", F, "The endemic geography",
   "Plague is endemic in at least 17 mostly Pacific Coast and Western states, with New Mexico, "
   "Colorado, California, Arizona and Nevada named repeatedly. A febrile patient with rodent "
   "contact in the western United States is the plague stem."),
 h("handled several dead prairie dogs", F, "A named epizootic host",
   "United States epizootics occur in squirrels, prairie dogs and chipmunks. Handling dead animals "
   "exposes the patient to their fleas, which leave a dying host in search of another."),
 h("an exquisitely tender, boggy 5 cm mass in the right inguinal region", T, "The bubo",
   "Rapid multiplication at the bite site, spread to the draining node, then intense hemorrhage "
   "and swelling. The tenderness is out of proportion — this is the lesion that names bubonic "
   "plague."),
 h("a small crusted papule on the right calf", M, "The flea bite, and the anatomy",
   "The bite is 1–2 cm at most and easily missed. Its location matters: a calf lesion drains to "
   "the inguinal nodes, which is exactly where the bubo is."),
 h("There is no pharyngitis and no genital ulcer", P, "Competing causes closed off",
   "Tender inguinal adenopathy has other causes — chancroid, lymphogranuloma venereum, "
   "tularemia — and the stem removes them so the exposure history carries the diagnosis."),
],

36: [
 h("renovating a long-disused grain barn heavily soiled with rodent droppings", F,
   "An aerosol-generating exposure",
   "Hantavirus is shed in rodent urine, feces and saliva and is acquired by inhaling it. The "
   "classic history is someone disturbing dust in a contaminated building."),
 h("Five weeks ago", P, "Do not dismiss a remote exposure",
   "The incubation period is 3 to 9 WEEKS — far longer than the 4–7 days of dengue. An exposure a "
   "month or two ago is still well within the window."),
 h("He recalls no insect or tick bites and no animal bites", W, "No vector at all",
   "Hantavirus and Lassa fever are the only two agents in this block with no arthropod vector. "
   "The absence of a bite is a positive finding here, not a gap in the history."),
 h("creatinine is 5.1 mg/dL", F, "One organ failing out of proportion",
   "Every other hemorrhagic fever kills through generalized multi-organ failure. Hantavirus "
   "hemorrhagic fever with renal syndrome is the exception, and acute kidney injury is the usual "
   "cause of death. Renal failure out of proportion to everything else is this diagnosis."),
 h("interstitial hemorrhage with a dense mononuclear infiltrate", M, "Immunopathologic injury",
   "The lesion is an acute tubulointerstitial nephritis produced by cytokines, cytotoxic T cells, "
   "complement and bradykinin attacking endothelium marked as infected — not by the virus lysing "
   "kidney tissue. That is why there is no antiviral to give."),
],

37: [
 h("a dusky blue discoloration of her fingertips that appears when she goes outdoors", F,
   "Cold-induced acrocyanosis",
   "IgM cold agglutinins bind red cells in the cooler acral circulation and clump them, obstructing "
   "flow. It resolves on rewarming, which is the whole clue."),
 h("atypical pneumonia treated with azithromycin 6 weeks ago", M, "The trigger",
   "Mycoplasma pneumoniae induces cold agglutinins directed against the I antigen; Epstein-Barr "
   "virus induces anti-i. The interval of a few weeks is typical."),
 h("Mean corpuscular hemoglobin concentration  44.6%", P, "A physically impossible value",
   "A red cell cannot hold hemoglobin at this concentration. An MCHC above about 37% has a very "
   "short differential and most of it is artefact — agglutination, lipemia, or hereditary "
   "spherocytosis."),
 h("Erythrocyte count  2.1 million/mm3", M, "The analyzer is counting clumps",
   "Agglutinated cells pass the aperture as one large particle, so the count falls and the "
   "measured volume rises. The hemoglobin is measured chemically after lysis and stays accurate, "
   "so MCHC = Hgb ÷ (falsely low count × falsely high volume) becomes absurd."),
 h("Which of the following is the most appropriate next step?", W, "Fix the specimen, not the patient",
   "The numbers are an artefact of temperature. Warming the sample to 37 C disperses the "
   "agglutinates and the indices normalize — before treating an anemia that is partly illusory."),
],

38: [
 h("Leukocyte count  600/mm3", F, "Profound leukopenia",
   "Day 12 after induction chemotherapy is the expected nadir. The total count alone is not the "
   "number that matters, though — the neutrophil fraction has to be applied to it."),
 h("Segmented neutrophils  12%", W, "Calculate the absolute neutrophil count",
   "ANC = total white cells × (segmented neutrophils + bands). Here 600 × 0.12 ≈ 72/mm3. The "
   "thresholds to know are 1,000 (mild risk), 500 (serious risk) and 200 (profound, with no "
   "inflammatory response at all)."),
 h("tenderness lateral to the anus with minimal erythema and no fluctuance", P,
   "Pus is made of neutrophils",
   "Erythema, induration, fluctuance and drainage are all neutrophil products. A patient with "
   "essentially no neutrophils cannot generate them, so severe deep infection presents with pain "
   "and fever and almost nothing to see."),
 h("chest radiography shows no infiltrate, although she reports a cough", P,
   "The same principle in the lung",
   "A pulmonary infiltrate is largely inflammatory exudate. Its absence in a profoundly "
   "neutropenic patient does not exclude pneumonia — which is why fever alone in neutropenia is "
   "treated as an emergency."),
],

39: [
 h("Leukocyte count  58,000/mm3", F, "Extreme leukocytosis",
   "Above 50,000/mm3 the differential is a leukemoid reaction versus chronic myeloid leukemia. "
   "Everything else in this vignette exists to separate those two."),
 h("coarse dark cytoplasmic granules, pale blue cytoplasmic inclusions and vacuoles", T,
   "Toxic granulation, Döhle bodies, vacuolization",
   "The triad of an activated, reactive neutrophil responding to severe infection. Leukemic cells "
   "do not show these changes."),
 h("Basophils  0%", P, "The absent finding that decides it",
   "Chronic myeloid leukemia almost always has basophilia, and often eosinophilia. A basophil "
   "count of zero argues strongly against it. Leukocyte alkaline phosphatase is high in a "
   "leukemoid reaction and low in CML."),
 h("blasts account for less than 1% of cells", W, "A left shift without blasts",
   "Reactive marrow releases immature but maturing forms — myelocytes and metamyelocytes. A "
   "leukemic process spills blasts. Reactive is busy; malignant is young."),
 h("He has no lymphadenopathy, splenomegaly, night sweats or weight loss", P,
   "No myeloproliferative features",
   "Splenomegaly and constitutional symptoms would point to CML. Their absence, with an obvious "
   "infective source that has just been drained, predicts that the count will simply normalize."),
],

40: [
 h("a liver abscess at age 2 that grew Serratia marcescens", F, "A near-specific organism",
   "Serratia rarely infects healthy children. With Staphylococcus aureus and Aspergillus it "
   "completes the catalase-positive set — S. aureus, Aspergillus, Serratia, Nocardia and "
   "Burkholderia."),
 h("Leukocyte count is 9,400/mm3 with 58% segmented neutrophils", P,
   "The count is normal, and that is the point",
   "This is a QUALITATIVE defect, not a quantitative one. The neutrophils are present in normal "
   "numbers and phagocytose perfectly well — they simply cannot kill what they have eaten."),
 h("serum IgG, IgA and IgM concentrations are normal", W, "Not an antibody deficiency",
   "Antibody deficiencies are 65% of primary immunodeficiencies and would be the default guess. "
   "Normal immunoglobulins with recurrent abscesses and granulomas redirect you to the phagocyte."),
 h("granulomas with multinucleated giant cells", M, "The standoff",
   "Organisms that are ingested but not killed survive inside the phagocyte, so the immune system "
   "walls them off instead. A necrotic centre of live organisms, a macrophage barrier and "
   "surrounding T cells holding the line — a siege, which is where the disease gets its name."),
 h("The organisms that have infected this patient share which of the following properties?", W,
   "Why only some organisms",
   "A cell without NADPH oxidase makes no hydrogen peroxide of its own — but it can borrow the "
   "peroxide many bacteria produce as a by-product. CATALASE-POSITIVE organisms destroy their own, "
   "leaving the defective phagocyte nothing to work with. Catalase-negative organisms are still "
   "killed."),
],

41: [
 h("a large thigh hematoma after a vaccination in infancy", F, "Deep bleeding",
   "Bleeding into muscles and joints, delayed after trauma, is the signature of a clotting factor "
   "deficiency — secondary hemostasis failing after the platelet plug has formed."),
 h("He has never had nosebleeds, gum bleeding or petechiae", P, "Where they bleed tells you which half",
   "Mucocutaneous bleeding — epistaxis, gums, petechiae, menorrhagia — indicates a platelet or von "
   "Willebrand problem. Its absence points away from primary hemostasis entirely."),
 h("His maternal uncle has a bleeding disorder", P, "X-linked inheritance",
   "An affected maternal uncle with an unaffected mother is the pedigree of an X-linked recessive "
   "condition. Hemophilia A (factor VIII) is about four times as common as hemophilia B (factor "
   "IX)."),
 h("A 1:1 mix of the patient's plasma with normal pooled plasma corrects the partial thromboplastin "
   "time to 33 seconds", W, "Corrects means missing",
   "The mixing study is the fork in the road. CORRECTION means the patient lacks something that "
   "normal plasma supplied — a factor deficiency. FAILURE to correct means something in the "
   "patient's plasma is blocking the assay — an inhibitor."),
],

42: [
 h("She has never had abnormal bleeding, including after a hysterectomy at age 46 and two dental "
   "extractions", P, "Lifelong normal hemostasis",
   "Two major hemostatic challenges passed without incident rules out an inherited deficiency. A "
   "bleeding disorder appearing for the first time at 74 must be ACQUIRED."),
 h("She has rheumatoid arthritis", F, "The company it keeps",
   "Acquired hemophilia A is associated with autoimmune disease, malignancy, the postpartum period "
   "and drugs — although about half of cases are idiopathic."),
 h("immediately after mixing gives a partial thromboplastin time of 35 seconds", P,
   "The immediate result is the trap",
   "Read too quickly, this looks like correction and therefore like a factor deficiency. It is not "
   "the result that matters."),
 h("after incubation at 37 C for 60 minutes, the mixed sample measures 61 seconds", W,
   "Time- and temperature-dependence is the signature",
   "An anti-factor VIII autoantibody neutralizes factor VIII progressively rather than instantly, "
   "so the mix looks corrected at first and prolongs again after incubation. A lupus anticoagulant "
   "by contrast fails to correct IMMEDIATELY. This is why the incubated mixing study exists."),
],

43: [
 h("heavy menstrual bleeding", F, "A mucocutaneous pattern",
   "Menorrhagia from menarche, epistaxis and easy bruising point at primary hemostasis — platelets "
   "or von Willebrand factor — rather than at the coagulation cascade."),
 h("Her mother and older sister have similar symptoms", P, "Autosomal dominant",
   "Affected females in consecutive generations distinguishes von Willebrand disease, the "
   "commonest inherited bleeding disorder, from the X-linked hemophilias."),
 h("von Willebrand factor antigen  62%", F, "The protein is there",
   "Antigen measures how much von Willebrand factor is present, and this is within the reference "
   "range. A type 1 (quantitative) deficiency would show a low antigen level."),
 h("Ristocetin cofactor activity  20%", F, "But it does not work",
   "Ristocetin cofactor activity measures FUNCTION — the ability to bind platelet glycoprotein Ib. "
   "Activity far below antigen, giving a ratio well under 0.7, defines a qualitative (type 2) "
   "defect."),
 h("She is blood group A", P, "A confounder removed",
   "Blood group O lowers von Willebrand factor by roughly 25% and is a common reason for a "
   "borderline result. Group A removes that explanation, so the low activity has to be real."),
],

44: [
 h("Three weeks ago he had a cold that resolved", F, "A post-viral trigger",
   "Childhood immune thrombocytopenia characteristically follows a viral illness by one to four "
   "weeks. Antibodies raised against the virus cross-react with platelet glycoproteins."),
 h("He is well and playing in the examination room", P, "A well child with a terrible number",
   "The mismatch between a platelet count of 14,000 and a completely well child is the classic "
   "picture. A child with leukemia looks ill."),
 h("There is no lymphadenopathy, hepatomegaly, splenomegaly or bone tenderness", W,
   "Leukemia excluded on examination",
   "These are the findings that would demand a marrow before treatment. Their absence, with "
   "isolated thrombocytopenia, supports immune thrombocytopenia — where marrow examination is not "
   "routinely required."),
 h("occasional large forms", M, "Young platelets",
   "Large platelets are newly released and hemostatically more active. Their presence tells you "
   "the marrow is responding, which is why bleeding is often milder than the count suggests."),
 h("which of the following would most likely be found?", W, "Destruction, not failure",
   "Antibody-coated platelets are cleared by splenic macrophages, and the marrow compensates by "
   "increasing megakaryocytes. Reduced megakaryocytes would mean a production problem — a "
   "different disease entirely."),
],

45: [
 h("her platelet count rose to 186,000/mm3 and remained normal for 5 months", P,
   "A genuine response, then relapse",
   "The operation worked, so the diagnosis was right and the spleen was the site of destruction. "
   "Something has restored that capacity."),
 h("The peripheral smear shows reduced platelets and no Howell-Jolly bodies", F,
   "The finding that solves it",
   "Howell-Jolly bodies are nuclear remnants that a functioning spleen pits from red cells. After "
   "a complete splenectomy they should APPEAR permanently. Their absence means functioning splenic "
   "tissue is still present."),
 h("She underwent laparoscopic splenectomy 8 months ago", M, "Accessory spleens get missed",
   "Accessory splenic tissue is present in 10%–20% of people, usually at the splenic hilum or in "
   "the gastrosplenic ligament, and is more easily overlooked laparoscopically. It hypertrophies "
   "over months and resumes destroying antibody-coated platelets."),
],

46: [
 h("He has received nothing by mouth since surgery and has been treated with broad-spectrum "
   "antibiotics", M, "Both sources of vitamin K removed",
   "Dietary vitamin K1 comes from green vegetables, and vitamin K2 is made by colonic bacteria. "
   "Nil by mouth removes the first and broad-spectrum antibiotics remove the second. Body stores "
   "last only weeks."),
 h("there is no jaundice, ascites or splenomegaly", P, "Liver disease excluded clinically",
   "Hepatic failure is the main competing cause of a prolonged prothrombin time, and it would "
   "reduce factor V as well — which is exactly what the question is testing."),
 h("Albumin  3.6 g/dL", W, "Synthetic function is intact",
   "A normal albumin and bilirubin argue against liver failure, so the factors the liver makes "
   "independently of vitamin K should be normal."),
 h("Fibrinogen  340 mg/dL", W, "Consumption excluded",
   "A normal fibrinogen with a normal D-dimer and a normal platelet count rules out disseminated "
   "intravascular coagulation."),
 h("Prothrombin time  26 sec", F, "PT prolonged more than aPTT",
   "Factor VII has the shortest half-life of the vitamin K-dependent factors (about 4–6 hours), so "
   "the extrinsic pathway fails first. The vitamin K-dependent factors are II, VII, IX and X, plus "
   "proteins C and S; factor V is NOT among them and stays normal."),
],

47: [
 h("2 days of confusion and slurred speech", F, "Neurologic predominance",
   "Brain means thrombotic thrombocytopenic purpura; kidney means hemolytic uremic syndrome. Both "
   "organs can be involved in either, but which one dominates is the discriminator."),
 h("has had no diarrhea", P, "Shiga toxin excluded",
   "Typical hemolytic uremic syndrome follows bloody diarrhea from Shiga toxin-producing "
   "Escherichia coli, usually in a child. Its absence in an adult with neurologic signs points the "
   "other way."),
 h("Creatinine  1.4 mg/dL", P, "The kidney is relatively spared",
   "Only mildly raised, despite catastrophic hemolysis and thrombocytopenia. That disproportion is "
   "the point."),
 h("Lactate dehydrogenase  1,460 U/L", F, "Microangiopathic hemolysis",
   "With an unmeasurable haptoglobin, a high reticulocyte count and schistocytes on the smear, red "
   "cells are being sheared as they pass platelet-rich microthrombi."),
 h("Fibrinogen  330 mg/dL", W, "Normal clotting times exclude DIC",
   "All the thrombotic microangiopathies have a NORMAL prothrombin time, partial thromboplastin "
   "time and fibrinogen. Disseminated intravascular coagulation consumes clotting factors; these "
   "diseases consume platelets only."),
],

48: [
 h("She has had no diarrhea", W, "Not the typical form",
   "With negative stool culture and Shiga toxin testing, typical hemolytic uremic syndrome is "
   "excluded."),
 h("a maternal cousin developed kidney failure in childhood", P, "An inherited regulatory defect",
   "A relapsing course and a family history point to inherited loss of a complement regulatory "
   "protein — factor H, factor I, membrane cofactor protein or thrombomodulin."),
 h("Complement C3  58 mg/dL", M, "The alternative pathway is running unchecked",
   "Low C3 with a normal C4 indicates consumption through the alternative pathway specifically. "
   "Unrestrained C5b-9 assembly on endothelium is what drives the microangiopathy."),
 h("ADAMTS13 activity is 68%", W, "Thrombotic thrombocytopenic purpura excluded",
   "TTP requires severely deficient ADAMTS13, conventionally below 10%. Normal activity with a "
   "normal prothrombin time and partial thromboplastin time leaves complement-mediated (atypical) "
   "hemolytic uremic syndrome — treated with a terminal complement inhibitor, not with plasma "
   "exchange alone."),
],

49: [
 h("nephrotic syndrome from membranous nephropathy, with 9 g of protein", M,
   "The protein lost is not only albumin",
   "Antithrombin is a 58 kDa plasma protein, close in size to albumin, and it is lost in the urine "
   "alongside it. Nephrotic syndrome is prothrombotic for exactly this reason — and membranous "
   "nephropathy carries the highest thrombotic risk of all."),
 h("Intravenous unfractionated heparin is started", M, "Heparin has no activity of its own",
   "Heparin is a catalyst. It binds antithrombin and accelerates its inhibition of thrombin and "
   "factor Xa roughly a thousandfold. With little antithrombin present there is nothing for it to "
   "accelerate."),
 h("Despite three dose increases over 24 hours, the activated partial thromboplastin time remains "
   "at 30–33 seconds", F, "Heparin resistance",
   "Escalating doses producing no anticoagulant effect at all is the defining observation. Note "
   "that the anti-factor Xa level is low too, so this is genuine under-anticoagulation rather than "
   "an assay artefact."),
 h("The infusion pump and line have been checked and the drug is being delivered", P,
   "The mundane explanation is closed off",
   "The commonest cause of an unresponsive heparin infusion is that it is not actually going in. "
   "The stem removes it, which means the answer is pharmacologic."),
],

50: [
 h("on hospital day 2 the admitting team sends a full thrombophilia panel", P,
   "The wrong moment to test",
   "Functional assays are unreliable during an acute thrombosis and while on anticoagulation. "
   "Testing at the point of maximum confounding is a common real-world error and a favourite "
   "examination scenario."),
 h("an antithrombin activity of 52%", M, "Two reasons it could be low without a deficiency",
   "Heparin binds and consumes antithrombin, lowering the measured level. An acute clot consumes "
   "it as well. A low result here cannot distinguish an inherited deficiency from an entirely "
   "acquired one — it must be repeated off heparin, weeks after the event."),
 h("heterozygous factor V Leiden", P, "Genetic tests are not time-sensitive",
   "A DNA-based result is valid whenever it is drawn, because the genotype does not change. It is "
   "the FUNCTIONAL assays — antithrombin, protein C, protein S — that acute illness and "
   "anticoagulants confound."),
 h("which developed 2 weeks after she started a combined oral contraceptive", F,
   "A provoked event anyway",
   "An estrogen-provoked first thrombosis is treated for three months and the trigger removed, "
   "whatever the panel shows. Duration follows the clot, not the genotype — so the test was "
   "unlikely to change management even if it had been correctly timed."),
],

51: [
 h("three consecutive spontaneous abortions at 7, 8 and 9 weeks' gestation, all with normal fetal "
   "karyotypes", F, "A clinical criterion",
   "Three or more unexplained consecutive losses before 10 weeks is one of the clinical criteria "
   "for antiphospholipid syndrome. Normal karyotypes remove the commonest alternative explanation."),
 h("A rapid plasma reagin test performed during her first pregnancy was positive, but "
   "treponemal-specific testing was negative", P, "A biological false positive",
   "The RPR is a cardiolipin-based assay, so antiphospholipid antibodies make it positive without "
   "any treponemal infection. A false-positive syphilis serology has pointed at this diagnosis "
   "since long before the antibodies could be measured directly."),
 h("She has never bled abnormally, including after a tonsillectomy", P,
   "The name is wrong on both counts",
   "A 'lupus anticoagulant' is neither specific to lupus nor an anticoagulant in the patient. It "
   "prolongs a test tube reaction while causing THROMBOSIS in vivo. A prolonged partial "
   "thromboplastin time with no bleeding history should prompt this thought immediately."),
 h("A 1:1 mix with normal plasma does not correct the partial thromboplastin time, but adding "
   "excess phospholipid does", W, "Two steps, two conclusions",
   "Failure to correct on mixing proves an INHIBITOR rather than a factor deficiency. Correction "
   "on adding excess phospholipid proves the inhibitor is aimed at the PHOSPHOLIPID in the reagent "
   "rather than at a specific clotting factor — which is the definition of a lupus anticoagulant."),
],

52: [
 h("Lupus anticoagulant testing and anti-beta-2-glycoprotein-1 antibodies were positive at the "
   "time of the embolism and again today, 12 weeks apart", W, "The 12-week rule",
   "Antiphospholipid antibodies must be positive on two occasions at least 12 weeks apart, because "
   "transient positives are common with acute illness and infection. Both the laboratory and the "
   "clinical criteria are satisfied here."),
 h("a history of an unprovoked deep vein thrombosis at age 33", F, "A second unprovoked event",
   "Recurrent unprovoked venous thrombosis in a young man means indefinite anticoagulation, "
   "independent of the antibody result."),
 h("He asks to take a once-daily tablet that does not require monitoring", P,
   "The stem is steering you wrong on purpose",
   "Everything about the request describes a direct oral anticoagulant, and in almost any other "
   "patient that would be right. In antiphospholipid syndrome — particularly triple-positive "
   "disease — trials found MORE thrombotic events on rivaroxaban than on warfarin. A "
   "vitamin K antagonist with INR monitoring remains the standard, and the patient's preference "
   "does not override it."),
],

53: [
 h("His platelet count was 265,000/mm3 on admission and is 78,000/mm3 today", F,
   "A greater than 50% fall on day 8",
   "The timing is the diagnosis: heparin-induced thrombocytopenia appears 5–10 days after exposure "
   "in a patient not previously sensitized. The proportional fall matters more than the absolute "
   "count, which often stays above 20,000."),
 h("a cold, painful right foot", P, "Thrombocytopenia that clots",
   "The central paradox. Antibody-coated platelets are activated before they are cleared, so the "
   "complication is THROMBOSIS — arterial or venous — not bleeding. This is the white clot, "
   "platelet-rich and pale, as opposed to the red fibrin-rich clot of stasis."),
 h("There is no bleeding at the surgical site and no petechiae", P, "Absence of bleeding is a clue",
   "Any other cause of a platelet count of 78,000 would raise the question of bleeding. Here the "
   "entire risk is on the other side — which is why stopping heparin is not enough and an "
   "alternative non-heparin anticoagulant must be started."),
 h("the peripheral smear shows no schistocytes", W, "Microangiopathy excluded",
   "No fragments, with a normal prothrombin time, partial thromboplastin time and fibrinogen, "
   "removes disseminated intravascular coagulation and the thrombotic microangiopathies."),
],

54: [
 h("6 days after an open hysterectomy, during which she was on bedrest for 4 days", F,
   "A major transient provoking factor",
   "Surgery with immobility within the preceding 3 months is a major provoking factor. The "
   "provocation is gone and will not recur."),
 h("She has no personal or family history of thrombosis, no known malignancy", P,
   "Nothing to extend treatment for",
   "The reasons to continue beyond three months are an unprovoked event, recurrence, active cancer "
   "or antiphospholipid syndrome. None is present."),
 h("Age-appropriate cancer screening is up to date", W, "No occult malignancy hunt",
   "A provoked thrombosis with a clear explanation does not warrant extensive cancer screening — "
   "that question arises with an unprovoked event."),
 h("She asks how long she needs to keep taking the medication", W,
   "Duration follows the clot, not the genotype",
   "Provoked by a major transient risk factor, treatment stops at 3 months. Unprovoked, it is "
   "extended or indefinite with periodic reassessment. Thrombophilia testing would not change "
   "either answer, which is why it is not indicated here."),
],

55: [
 h("Fourteen months ago he had a large bilateral pulmonary embolism", F, "The antecedent event",
   "Chronic thromboembolic pulmonary hypertension follows acute pulmonary embolism in about 2%–4% "
   "of patients, when thrombus organizes into fibrotic material that does not lyse."),
 h("Chest radiography shows clear lung fields, spirometry is normal", P, "The lungs are innocent",
   "Clear films and normal spirometry exclude parenchymal and obstructive disease as the cause of "
   "this degree of breathlessness and desaturation, which forces attention onto the pulmonary "
   "vasculature."),
 h("an estimated pulmonary artery systolic pressure of 62 mm Hg with a dilated right ventricle", F,
   "Established pulmonary hypertension",
   "With a loud pulmonary second sound, elevated natriuretic peptide and peripheral edema, the "
   "right ventricle is failing against a high afterload."),
 h("Which of the following is the most appropriate next diagnostic test?", W,
   "The one place V/Q beats CT",
   "Ventilation-perfusion scanning is MORE sensitive than CT pulmonary angiography for chronic "
   "organized thromboembolic disease, which is flat, wall-adherent and easily missed on CT. A "
   "normal V/Q scan effectively excludes the diagnosis, which is why it is the screening test of "
   "choice — and this matters because the disease is surgically curable."),
],

56: [
 h("the zone between the follicles is markedly expanded", T, "The paracortex",
   "The interfollicular or paracortical zone. Node architecture is worth holding as three "
   "compartments: cortex with B-cell follicles, PARACORTEX with T cells, and medulla with plasma "
   "cells and sinuses."),
 h("numerous pale cells having abundant cytoplasm and irregular nuclear contours", F,
   "Interdigitating dendritic cells",
   "These are the antigen-presenting cells of the T-cell zone. They are the normal partners of "
   "paracortical T lymphocytes, and their prominence here reflects chronic antigen delivery from "
   "the skin."),
 h("melanin-laden macrophages", T, "Dermatopathic lymphadenitis",
   "Pigment carried to the node from chronically inflamed, scratched skin. It identifies the "
   "reaction as draining a dermatitis rather than as a lymphoma."),
 h("an intact capsule and preserved follicles", P, "Architecture preserved means reactive",
   "Lymphoma effaces nodal architecture and breaches the capsule. An intact capsule with preserved "
   "follicles and an expanded but recognizable paracortex is the pattern of hyperplasia."),
],

57: [
 h("the follicles are closely apposed and of similar size", F, "Back-to-back monotonous follicles",
   "Reactive germinal centers vary in size and shape and are spaced apart. Crowded follicles of "
   "uniform size, extending beyond the cortex, indicate a neoplastic follicular proliferation."),
 h("tingible body macrophages are absent", M, "No apoptosis, and that is the mechanism",
   "A reactive germinal center is a site of rapid proliferation AND rapid apoptosis, so it is full "
   "of macrophages containing nuclear debris — the 'starry sky'. The t(14;18) translocation places "
   "BCL2 under the immunoglobulin heavy chain promoter, blocking apoptosis, so the debris "
   "disappears."),
 h("mantle zones are attenuated", F, "The neoplastic follicle crowds out the mantle",
   "The residual mantle of small naive B cells is compressed and thinned as the neoplastic centre "
   "expands."),
 h("painless, progressive swelling of nodes", P, "Grow-slow, die-slow",
   "Widespread painless adenopathy in a well patient over months is the indolent pattern. These "
   "lymphomas are often incurable but compatible with long survival — the opposite trade-off from "
   "the aggressive ones."),
 h("Which of the following immunohistochemical results is most likely in the follicle centers of "
   "this biopsy?", W, "A normal germinal center is BCL2 NEGATIVE",
   "This is the single most useful stain here. Normal follicle center B cells are BCL2 NEGATIVE, "
   "because they must be able to die if they fail selection. BCL2 positivity within follicle "
   "centers marks them as neoplastic."),
],

58: [
 h("more than 10% are large with abundant basophilic cytoplasm", T, "Atypical lymphocytes",
   "Downey cells — activated CD8 T lymphocytes responding to EBV-infected B cells. They are the "
   "host response, not the infected cells themselves."),
 h("the underlying architecture is only partially effaced", P, "Partial effacement favours reactive",
   "Classic Hodgkin lymphoma effaces the node. Preserved sinuses and recognizable underlying "
   "architecture, with a mottled expanded paracortex, point to an exuberant reaction."),
 h("scattered very large cells with prominent nucleoli that stain strongly for CD30", P,
   "CD30 does not settle it",
   "The trap. EBV-transformed immunoblasts can be large, binucleate, nucleolated and CD30-positive "
   "— closely mimicking Reed-Sternberg cells. This is why infectious mononucleosis is a classic "
   "misdiagnosis as Hodgkin lymphoma."),
 h("Which of the following additional findings would most strongly argue against classic Hodgkin "
   "lymphoma?", W, "Hodgkin cells LOSE the B-cell program",
   "Reed-Sternberg cells are of germinal center B-cell origin but have switched off their B-cell "
   "identity: CD15 and CD30 positive, and CD20 usually NEGATIVE or only weakly and patchily "
   "positive. Large cells with strong, uniform CD20 have kept their B-cell program — the "
   "mononucleosis pattern."),
],

59: [
 h("Ten days of doxycycline produced no improvement", P, "The usual suspects are closed off",
   "Doxycycline covers the common infectious causes of a tender cervical node, including cat "
   "scratch disease and tularemia. The stem also removes pets, travel and sick contacts."),
 h("Leukocyte count is 2,800/mm3 with neutropenia and lymphopenia", F, "Cytopenias with adenopathy",
   "Leukopenia alongside fever, night sweats and a raised sedimentation rate is characteristic, "
   "and is one reason this disease is so often mistaken for lymphoma or lupus."),
 h("histiocytes with crescent-shaped nuclei", T, "Crescentic histiocytes",
   "Along with plasmacytoid dendritic cells, these are the characteristic cell. They stain for "
   "CD68 and myeloperoxidase, confirming histiocytic rather than lymphoid lineage."),
 h("Neutrophils are absent", P, "Necrosis WITHOUT neutrophils",
   "The single most discriminating feature. Necrosis in a node normally means suppuration, and "
   "suppuration means neutrophils. Abundant karyorrhectic debris with NO neutrophils and no "
   "granulomas is this diagnosis — a self-limiting condition that resolves in one to four months."),
 h("Antinuclear antibody is negative", W, "Lupus lymphadenitis excluded",
   "The one condition that is histologically near-identical is lupus lymphadenitis, which shows "
   "hematoxylin bodies and abundant plasma cells. A negative antinuclear antibody makes it "
   "unlikely — though these patients warrant follow-up, as a minority later develop lupus."),
],

60: [
 h("many containing intact lymphocytes and plasma cells within clear spaces in their cytoplasm", T,
   "Emperipolesis",
   "Intact, undamaged cells sitting inside a histiocyte within a clear halo. This is not "
   "phagocytosis — the engulfed cells are alive and pass through unharmed. It is the defining "
   "feature of Rosai-Dorfman disease."),
 h("markedly expanded lymph node sinuses", F, "Sinus histiocytosis",
   "The disease is formally called sinus histiocytosis with massive lymphadenopathy, and the "
   "sinusoidal location of the histiocytes is half of that name."),
 h("They stain strongly for S100 and CD68", P, "S100 cannot separate them",
   "This is the trap. S100 is positive in BOTH Rosai-Dorfman disease and Langerhans cell "
   "histiocytosis, so it establishes the lineage without resolving the differential."),
 h("Which of the following additional findings would best exclude Langerhans cell histiocytosis?", W,
   "CD1a and langerin are the discriminators",
   "Langerhans cells are S100 positive AND CD1a positive AND CD207 (langerin) positive, with "
   "Birbeck granules on electron microscopy and grooved, coffee-bean nuclei. Rosai-Dorfman "
   "histiocytes are S100 positive but CD1a and CD207 NEGATIVE — so it is the absent stains that "
   "carry the answer."),
],

}
