# Key Findings — vignette highlights for Hardest Exam questions 121–140 (the microbiology batch).
# Authoring rules and categories: see highlights_hardest_001_030.py and QUIZ_BUILD_METHOD.md.

F, M, T, P, W = "finding", "mechanism", "term", "pattern", "workup"
EYEBROW = {F: "FINDING", M: "MECHANISM", T: "KEY TERM", P: "PATTERN", W: "WHAT'S ASKED"}


def h(text, cat, title, body):
    return {"text": text, "cat": cat, "eyebrow": EYEBROW[cat], "title": title, "body": body}


HIGHLIGHTS = {

121: [
 h("He lives on Nantucket and gardens daily", F, "Geography and exposure first",
   "Coastal New England in the warm months is babesiosis country. The lecturer's own rule for this "
   "block: find the geography and the exposure before reading a single laboratory value."),
 h("prescribed doxycycline for presumed Lyme disease; he has taken every dose and feels worse", P,
   "Failing doxycycline IS the clue",
   "Babesia, Borrelia burgdorferi and Anaplasma share one reservoir (the white-footed mouse) and "
   "one vector (the Ixodes nymph), so co-infection is common. Doxycycline treats the other two and "
   "has NO useful activity against Babesia. A New England patient not improving on doxycycline for "
   "Lyme disease should be evaluated for babesiosis."),
 h("He recalls no tick bite", P, "Expected, not reassuring",
   "The vector is the NYMPH, about the size of the dot over an 'i'. Most patients never see it, so "
   "a negative bite history must never weigh against the diagnosis."),
 h("Reticulocyte count  6.8%", F, "Hemolysis with a responding marrow",
   "With an unmeasurable haptoglobin, a raised lactate dehydrogenase and scleral icterus, red cells "
   "are being destroyed and the marrow is compensating."),
 h("Platelet count  74,000/mm3", F, "The babesiosis triad",
   "Hemolytic anemia, THROMBOCYTOPENIA and raised transaminases together. Age over 50, asplenia and "
   "immunosuppression define the severe-disease group."),
],

122: [
 h("checks himself for ticks after every hike", P, "Why careful checking fails",
   "The patient is doing the right thing and it still did not protect him. An adult tick is "
   "conspicuous and gets removed; a nymph is not — so the stage that transmits is the stage no one "
   "finds."),
 h("The four life stages of the vector are shown, photographed together at the same magnification",
   W, "The size drop is the epidemiology",
   "Larva, nymph, adult male and adult female. The step down to the nymph is dramatic, and that "
   "size difference explains the entire transmission pattern."),
 h("Which of the following best explains why this patient has no history of a tick bite?", W,
   "Two facts that compound",
   "First, ticks are NOT born infected — there is no transovarial transmission, so each tick must "
   "acquire the organism by feeding, and the nymph is the first stage to feed after moulting. "
   "Second, a nymph is unnoticeable and stays attached long enough to transmit. Transmission is a "
   "function of going unseen, not of biological potency."),
],

123: [
 h("fever, rigors and drenching sweats occurring without any discernible pattern", P,
   "Irregular fever points at falciparum",
   "The fever interval equals the erythrocytic cycle length: 24 hours for knowlesi, 48 for vivax "
   "and ovale, 72 for malariae. Falciparum's cycles are not synchronized, so there is no rhythm — "
   "and no fever-free window in which the patient recovers."),
 h("He returned 12 days ago from 6 weeks in rural Nigeria and took no chemoprophylaxis", F,
   "Sub-Saharan Africa means falciparum",
   "The most common and most virulent species. The incubation of 1–4 weeks reflects the silent "
   "pre-erythrocytic LIVER stage — the step Babesia does not have."),
 h("he is intermittently confused", T, "Cerebral malaria",
   "Infected red cells sequester in cerebral capillaries causing infarction and capillary leak. "
   "Severe disease can kill within 24 hours, which is why species and parasite density matter "
   "urgently."),
 h("Which of the following is the principal reason to examine preparation B as well?", W,
   "Thick = is it there; thin = which one",
   "The THICK film pre-lyses the red cells, concentrating parasites and examining far more blood "
   "per field — a sensitive presence-or-absence SCREEN that destroys the cell context, so it cannot "
   "speciate. The THIN film keeps parasites inside intact cells, so morphology identifies the "
   "SPECIES and quantifies the parasite density, at the cost of sensitivity."),
],

124: [
 h("Twelve days ago the family adopted a kitten, which scratched her right cheek and forearm", F,
   "Child, kitten, scratch",
   "Cat scratch disease is commonest in children under 10, and kittens are the likeliest source. "
   "Incubation is 3–10 days, so the patient usually still remembers the scratch."),
 h("a 3-cm tender, mobile right cervical lymph node", F, "Regional lymphadenopathy",
   "Stage two of three: a papule at 3–14 days, then a tender node draining that site at 1–3 weeks, "
   "then in a minority systemic infection. The node drains the scratch, which is why the cheek "
   "lesion gives a cervical node."),
 h("Her mother has bathed the kitten twice", P, "Bathing misses the point",
   "The organism is not simply sitting on the cat's surface waiting to be washed off. Flea control "
   "is what prevents the disease, because the flea is what maintains it in the cat population."),
 h("Which of the following is the most likely source of the organism?", W,
   "The claw is the needle, not the source",
   "Bartonella henselae passes from cat to cat in the CAT FLEA, and it is present in FLEA FECES, "
   "which contaminate fur and claws during grooming. The scratch inoculates that material. Do not "
   "culture — it is fastidious and takes weeks; use serology or PCR of node material, and treat "
   "with azithromycin."),
],

125: [
 h("Culture of the node has been negative at 5 days and remains in the incubator", P,
   "The negative culture is a finding",
   "Bartonella is fastidious and takes two to three weeks to grow, so culture should never have "
   "been the strategy. A node culture going nowhere at five days supports the diagnosis rather than "
   "arguing against it."),
 h("necrotizing granulomatous inflammation with stellate microabscesses", F,
   "Stellate microabscesses",
   "Star-shaped necrotic centres ringed by palisading histiocytes. Characteristic of cat scratch "
   "disease, though also seen in lymphogranuloma venereum and tularemia."),
 h("A Warthin–Starry silver stain of the node is shown", W, "Argyrophilic — a four-item list",
   "Silver-loving organisms appear black. The whole list is Bartonella, spirochetes (such as "
   "Treponema), Legionella and Helicobacter pylori. The stain narrows the field to four and the "
   "clinical context picks the winner: a node after a cat exposure is Bartonella."),
 h("a 4-cm tender left axillary lymph node", F, "The node drains an upper limb",
   "Head, neck and upper extremity nodes are the usual sites, because that is where children get "
   "scratched."),
],

126: [
 h("His CD4 count is 40/mm3", M, "Why the serology fails",
   "Serology detects the HOST's antibody response. A patient this immunosuppressed may not be "
   "making much antibody, so the test underperforms in exactly the population that gets this "
   "disease."),
 h("more than twenty friable, cherry-red cutaneous papules", F, "Vascular proliferation",
   "Bacillary angiomatosis — Bartonella driving proliferation of small vessels in skin and viscera. "
   "The SAME organism causes cat scratch disease in an immunocompetent host; the patient's immune "
   "status decides which disease appears."),
 h("Bartonella IgG and IgM serology is negative", P, "A near-meaningless negative",
   "Contrast cat scratch disease in a healthy child, where serology works well. Same organism, "
   "different test strategy, because the host is different."),
 h("Which of the following is the most appropriate next step in management?", W,
   "Kaposi sarcoma is the reason to biopsy",
   "These lesions look very like Kaposi sarcoma, which occurs in the same patients and cannot be "
   "distinguished by inspection — one is a curable bacterial infection, the other an HHV-8-driven "
   "vascular malignancy. That is why the diagnosis rests on lesion biopsy with histopathology. "
   "Then treat with erythromycin and/or doxycycline AND restart antiretroviral therapy."),
],

127: [
 h("had handled several dead ground squirrels", F, "A named epizootic host",
   "United States plague epizootics occur in squirrels, prairie dogs and chipmunks. Handling dead "
   "animals exposes a person to fleas leaving a cooling host."),
 h("gram-negative rods that stain darkly at both ends", T, "Bipolar 'safety pin' staining",
   "Dark at both ends, pale in the middle, on Gram or Giemsa stain. Together with the bubo this "
   "establishes Yersinia pestis."),
 h("he develops a productive cough with blood-streaked frothy sputum", F,
   "Secondary plague pneumonia",
   "Organisms reach the lymph, then the blood, and are filtered through the lungs. PRIMARY plague "
   "pneumonia instead follows direct inhalation with a 1–3 day incubation. Both are about 50% fatal "
   "treated and 100% untreated."),
 h("Which of the following is the most appropriate infection-control measure?", W,
   "A bubonic case can seed an airborne one",
   "Once plague reaches the lungs the patient generates infectious AEROSOLS, whatever the original "
   "route. You do not need exposure to a labelled 'pneumonic plague' case to catch pneumonic "
   "plague — an ordinary bubonic admission that progresses is enough. That chain is probably what "
   "made the 14th-century pandemic so lethal."),
],

128: [
 h("None has left the city and none has had rodent contact; no rodent die-off has been reported in "
   "the region", P, "The epidemiology is wrong",
   "Plague is endemic in the western United States and reaches humans through rodents and their "
   "fleas. Humans are a DEAD-END host. Six cases with no animal contact and no epizootic is not how "
   "this organism behaves."),
 h("fulminant pneumonia, hemoptysis and shock", F, "Primary pneumonic plague",
   "The form that follows direct inhalation, with a very short 1–3 day incubation — and the form "
   "suited to deliberate aerosol dissemination."),
 h("high-level resistance to gentamicin, doxycycline, ciprofloxacin and trimethoprim-"
   "sulfamethoxazole", W, "Naturally occurring plague is susceptible",
   "Wild-type Yersinia pestis shows very little drug resistance, which is why gentamicin or a "
   "fluoroquinolone reliably works. Simultaneous high-level resistance across four unrelated "
   "classes has to be explained, and deliberate alteration is the explanation that fits. Notify "
   "public health immediately."),
],

129: [
 h("has documented anti-glycoprotein antibodies", P, "The vaccine worked",
   "She mounted the intended response. This closes off vaccine failure, non-response and waning "
   "immunity, and forces the answer toward WHAT the antibodies recognize."),
 h("a maculopapular rash appears on her face and spreads to her neck and upper trunk", F,
   "The filovirus rash",
   "Appears around day 6–7 and follows a route: face, then neck and upper trunk, then limbs. It is "
   "harder to see on darker skin, and assuming its absence there is a real diagnostic error."),
 h("Which of the following best explains this outcome?", W, "Strain mismatch",
   "Every licensed product was built against ZAIRE ebolavirus — Ervebo (a live attenuated "
   "recombinant vesicular stomatitis virus vector carrying Ebola glycoprotein genes), and the "
   "monoclonals Inmazeb and Ebanga. Against the Bundibugyo strain driving the current outbreak "
   "there is very little cross-protection. If a question asks why a vaccinated patient still got "
   "Ebola, this is the answer."),
],

130: [
 h("a cave system inhabited by fruit bats", F, "Caves mean Marburg",
   "Both filoviruses share the Egyptian rousette fruit bat reservoir, but Marburg acquisition is "
   "specifically linked to cave exposure. Ebola is more often contact with a sick person, a corpse "
   "at a funeral, or bushmeat."),
 h("bleeding from the gums and oozing from every venipuncture site", F, "More hemorrhage than Ebola",
   "Marburg blocks the interferon response more effectively, induces a larger cytokine storm and "
   "destroys blood vessels directly — which is why bleeding is more prominent and fatality reaches "
   "88%–90% in severe outbreaks."),
 h("Which of the following is the most appropriate treatment?", W, "Nothing is approved",
   "The divergence from Ebola is total. Ebola has two licensed monoclonals and a licensed vaccine; "
   "Marburg has NO approved monoclonal, NO antiviral and NO vaccine. Management is supportive care "
   "aimed at avoiding shock. The gap is economic rather than scientific — too few cases a year to "
   "attract development."),
],

131: [
 h("a village with a heavy rodent infestation", M, "Mastomys natalensis",
   "The multimammate rat, abundant across West Africa. Three routes in, all involving the rodent: "
   "contact with urine, feces or body fluids; inhalation of aerosolized excreta; and eating the "
   "rodent. There is NO arthropod vector."),
 h("facial and neck edema, conjunctival injection and 2+ proteinuria", F, "Stage III Lassa fever",
   "The staged natural history: stage I is a mild febrile illness where about 80% stop; stage II "
   "adds sore throat, retrosternal pain, vomiting and diarrhea; stage III adds head and neck edema, "
   "conjunctival injection and proteinuria; stage IV is altered mental status and bleeding."),
 h("She is given ribavirin", P, "The only antiviral in the whole block",
   "Ribavirin is a guanosine analogue inhibiting viral RNA synthesis. The evidence is mixed and it "
   "is not a good drug, but Lassa is the ONLY agent here with any specific therapy — dengue, "
   "hantavirus and Crimean–Congo have none."),
 h("Which of the following long-term complications should she be counselled about?", W,
   "The sequela that identifies Lassa",
   "New BILATERAL SENSORINEURAL HEARING LOSS after a febrile illness acquired in West Africa is "
   "Lassa until proven otherwise — roughly a third of survivors are affected, and no other agent in "
   "this block does it. Survivors also report hair loss, tremor and balance difficulty."),
],

132: [
 h("45-year-old sheep farmer in eastern Turkey", F, "Geography and occupation",
   "Crimean–Congo hemorrhagic fever concentrates in Africa, the Middle East, Asia and southeastern "
   "Europe, with a dense band across Turkey, the Balkans, the Caucasus and Iran. Livestock contact "
   "is the occupational exposure."),
 h("His flock is healthy", P, "A healthy reservoir is the rule",
   "Livestock and birds carry the virus and stay completely well. The same is true of the fruit bat "
   "with filoviruses. A normal-looking herd is not evidence against the diagnosis — the detail is "
   "in the stem on purpose."),
 h("The engorged arthropod shown was removed from his groin 8 days ago", W, "Hyalomma, not Ixodes",
   "The vector is the genus HYALOMMA, recognizable by its banded legs. If a stem names Ixodes "
   "scapularis it is pointing at Lyme disease, babesiosis or anaplasmosis in the northeastern "
   "United States — a different tick on a different continent."),
 h("Platelet count is 28,000/mm3", F, "Thrombocytopenia and the prescribing rule",
   "With bleeding gums and petechiae, this is why the class rule matters: acetaminophen for fever "
   "and pain, NEVER non-steroidal anti-inflammatory drugs, in any viral hemorrhagic fever. "
   "Mortality is about 30% among symptomatic patients, though roughly 88% of infections are "
   "subclinical."),
],

133: [
 h("He has never had a febrile illness diagnosed as dengue, and serologic testing shows no evidence "
   "of previous dengue infection", W, "Seronegative is the contraindication",
   "This is the entire question. The dengue vaccine is licensed ONLY for people with a documented "
   "PRIOR dengue infection; in the dengue-naive a subsequent natural infection can run a rougher "
   "course. A vaccine with a prior-infection prerequisite is unusual enough to be worth a question "
   "on its own."),
 h("A 15-year-old boy who lives in Puerto Rico", F, "The right setting",
   "Most United States dengue cases occur in Puerto Rico rather than the continental states, and "
   "the vaccine is licensed for children aged 9–16 in endemic areas — so everything about him fits "
   "except the one disqualifying feature."),
 h("Two classmates were hospitalized with dengue last month", P, "Local risk does not change the rule",
   "Real exposure risk makes vaccination tempting, and prevention here is vector control instead. "
   "Humans are the dengue reservoir and about 76% of infections are asymptomatic yet transmissible, "
   "which is why controlling Aedes aegypti — not isolating cases — is the strategy."),
],

134: [
 h("respirations are 26/min", W, "qSOFA criterion one",
   "Respiratory rate 22/min or more — the most sensitive early vital sign change, and the one most "
   "often not counted."),
 h("blood pressure is 96/58 mm Hg", W, "qSOFA criterion two",
   "Systolic 100 mm Hg or LESS. Note the threshold: ≤ 100, not < 90, so the score catches patients "
   "BEFORE frank hypotension."),
 h("He is alert and fully oriented, with a Glasgow Coma Scale score of 15", W,
   "The third criterion is the one he does not meet",
   "Altered mentation is the remaining qSOFA element, so it is the only finding that can move him "
   "from 2 to 3."),
 h("Temperature is 38.4 C (101.1 F)", P,
   "Temperature and pulse belong to a different score",
   "Temperature, heart rate, respiratory rate and white cell count are the four SIRS criteria — and "
   "SIRS is no longer a defining criterion for sepsis, though Medicare and Medicaid still use it. "
   "qSOFA has exactly three criteria and requires no laboratory value at all."),
],

135: [
 h("Blood, urine and peritoneal fluid cultures drawn before antibiotics remain negative", P,
   "Negative cultures do not exclude sepsis",
   "No organism is identified in 30%–50% of sepsis cases, and these were drawn correctly before "
   "antibiotics. Sepsis is defined by the dysregulated host RESPONSE, not by a positive culture."),
 h("Leukocyte count  9,200/mm3 with 16% band forms", P, "A normal count that is not normal",
   "The criterion is satisfied by leukocytosis above 12,000, leukopenia below 4,000, OR a normal "
   "count with more than 10% immature forms. A left shift with a normal total ticks the box — but "
   "it grades the response, not the cause."),
 h("Procalcitonin  14 ng/mL", W, "The only cause-specific marker",
   "Everything else in the sepsis laboratory panel — white cells, platelets, creatinine, lactate, "
   "bilirubin, C-reactive protein, oxygenation, glucose, urine output, cortisol — measures how "
   "badly the patient is doing. PROCALCITONIN is the one that points at a BACTERIAL etiology."),
 h("C-reactive protein  240 mg/L", P, "Sensitive but useless here",
   "C-reactive protein rises in viral infection, trauma, surgery, autoimmune disease and malignancy "
   "alike. A high value in a post-operative patient with organ failure adds nothing."),
 h("following a perforated diverticulum", F, "The source predicts the organisms",
   "Sites of infection in order of frequency: respiratory > urinary > abdominal > head > other. An "
   "abdominal source means Escherichia coli, Bacteroides fragilis, mixed anaerobes and Candida — "
   "and is a major reason 20% of sepsis cases are polymicrobial."),
],

136: [
 h("has been neutropenic for 18 days following induction chemotherapy and has had a tunnelled "
   "central venous catheter for 6 weeks", F, "The textbook candidemia risk profile",
   "Prolonged neutropenia plus a long-dwelling central line. Fungal sepsis — about 80% Candida, "
   "10% Aspergillus — is increasing in immunocompromised patients."),
 h("Serum 1,3-beta-D-glucan is markedly elevated", W, "The assay measures the answer",
   "Beta-D-glucan is fungal cell wall material circulating in the blood. The same assay supports a "
   "diagnosis of Pneumocystis jirovecii pneumonia, whose wall is also rich in beta-1,3-D-glucan."),
 h("Which of the following molecules is the principal trigger of the host response in this "
   "patient?", W, "Match the trigger to the organism class",
   "Gram-negative bacteria → LIPOPOLYSACCHARIDE (the most prominent trigger overall). Gram-positive "
   "→ LIPOTEICHOIC ACID and peptidoglycan. FUNGI → BETA-GLUCANS, MANNANS and CHITIN, all "
   "polysaccharides. Viruses → DAMPs from host tissue, not pathogen patterns at all — the exception "
   "in the list and therefore the likely question."),
],

137: [
 h("Eighteen days ago he had receptive anal intercourse with a new partner of unknown HIV status",
   W, "Past the eclipse period",
   "Day 0 to about day 10 is the ECLIPSE period, when NO test detects HIV. At 18 days he is beyond "
   "it — which matters, because the eclipse period is the tempting wrong answer."),
 h("NON-exudative pharyngitis", P, "The discriminator from strep throat",
   "Acute retroviral syndrome gives non-exudative pharyngitis. More than half of newly infected "
   "people develop this transient illness, most often mistaken for mononucleosis — which the "
   "negative heterophile test argues against here."),
 h("An HIV-1/2 antigen/antibody immunoassay is REACTIVE. The reflex HIV-1/HIV-2 antibody "
   "differentiation immunoassay is NEGATIVE", W, "Discordance is the expected pattern",
   "A fourth-generation assay detects antibody AND p24 ANTIGEN; the differentiation assay detects "
   "antibody only. Reactive-then-negative therefore means antigen without antibody — acute "
   "infection. The next step is an HIV-1 nucleic acid test, the third tier of the algorithm."),
 h("a diffuse maculopapular rash involving the trunk and palms", F, "A rash that includes the palms",
   "Palm and sole involvement narrows a rash considerably — secondary syphilis, Rocky Mountain "
   "spotted fever, hand-foot-and-mouth disease and acute HIV. Frequencies in primary HIV: fever "
   "~75%, fatigue ~68%, rash ~48%, headache ~45%, pharyngitis ~40%."),
],

138: [
 h("darunavir/cobicistat", M, "The booster is not an antiretroviral",
   "Cobicistat and ritonavir are pharmacokinetic ENHANCERS. They inhibit CYP3A4 so the "
   "antiretroviral is cleared more slowly — and that inhibition applies to every other CYP3A4 "
   "substrate the patient takes. Being asked to identify them as non-antiretrovirals is itself a "
   "classic distractor."),
 h("an over-the-counter intranasal fluticasone spray", P, "Bought without a prescription",
   "Nasal steroids are sold over the counter, so no prescription record reveals them and the "
   "patient will not think to mention them. Fluticasone normally undergoes extensive first-pass "
   "CYP3A4 metabolism; block that and it accumulates systemically."),
 h("Morning cortisol  1.1 µg/dL", W, "LOW cortisol is the giveaway",
   "Endogenous Cushing syndrome raises cortisol. A CUSHINGOID patient with a SUPPRESSED cortisol "
   "and a suppressed corticotropin has an exogenous glucocorticoid on board — the hypothalamic-"
   "pituitary-adrenal axis has been switched off by a steroid the history barely mentions."),
 h("wide violaceous abdominal striae and proximal muscle weakness", P,
   "Not lipodystrophy",
   "Antiretroviral lipodystrophy affects about half of patients and causes abdominal "
   "lipohypertrophy, facial lipoatrophy and a dorsocervical fat pad — but never striae, proximal "
   "myopathy, hypokalemia or a suppressed cortisol."),
],

139: [
 h("His CD4 count is 28/mm3", F, "Well below 200",
   "Pneumocystis jirovecii pneumonia occurs typically below 200/mm3, and below 50/mm3 opportunistic "
   "infection risk is greatest. The count sets the differential before any imaging is seen."),
 h("Auscultation of the chest is unremarkable", P, "A normal chest examination is common",
   "About half of patients have a normal examination, and the chest radiograph can be normal in up "
   "to 25%. A normal high-resolution CT, by contrast, argues strongly against the diagnosis."),
 h("the alveolar-arterial oxygen gradient is 48 mm Hg", W, "The number that adds the steroid",
   "Corticosteroids are indicated in moderate-to-severe disease — PaO2 below 70 mm Hg OR an "
   "alveolar-arterial gradient of 35 mm Hg or more. At 48 he qualifies, and steroids reduce "
   "respiratory failure and mortality."),
 h("Intravenous trimethoprim-sulfamethoxazole is begun", M, "Cholesterol, not ergosterol",
   "Pneumocystis is an atypical fungus: it will not grow in fungal culture, and its cell wall "
   "contains CHOLESTEROL rather than ergosterol — which is exactly why ergosterol-targeting "
   "antifungals fail and an antifolate combination is the treatment. Expect WORSENING for 2–3 days "
   "as organisms die; that is not immune reconstitution, which comes far later."),
],

140: [
 h("His CD4 count is 22/mm3", W, "Organize opportunists by CD4 threshold",
   "Above 500, community-acquired organisms. 200–500, tuberculosis. Below 200, Pneumocystis, "
   "Cryptosporidium, Candida. Below 100, toxoplasmosis and esophagitis. Below 50: CYTOMEGALOVIRUS, "
   "Cryptococcus, Mycobacterium avium complex and primary CNS lymphoma."),
 h("6 days of floaters and painless loss of the temporal field of the right eye", F,
   "Painless visual loss",
   "Floaters and a progressive field defect without pain or redness. CMV retinitis is a full-"
   "thickness necrotizing retinitis that advances over days and threatens the whole retina."),
 h("He is afebrile and has no headache, neck stiffness or focal weakness", W,
   "The other CD4-under-50 diseases excluded",
   "Cryptococcal meningoencephalitis would bring headache and altered mentation; toxoplasmosis "
   "would bring focal deficits and ring-enhancing brain lesions; Mycobacterium avium complex would "
   "bring fever, sweats and weight loss. The isolated eye finding is the point."),
 h("He stopped antiretroviral therapy 18 months ago", M, "The preventable cause",
   "Treatment restores the CD4 count and is the definitive management alongside ganciclovir or "
   "valganciclovir. It also means anticipating immune recovery uveitis, a form of immune "
   "reconstitution in the treated eye."),
],

}
