# Hardest Exam — batch H7 (questions 121–140): microbiology depth.
# The six infectious-disease sections of the review file (sepsis, HIV virology, HIV clinical,
# vector-borne organisms, viral hemorrhagic fevers, primary immunodeficiency) hold twelve
# objectives but carried only nineteen of the first 120 questions. This batch works those
# sections in detail: LO 5 (babesiosis/malaria), 22 (Bartonella), 23 (plague), 13 (the
# hemorrhagic fevers and filoviruses), 1 and 75 (sepsis), 14 and 24 (HIV virology),
# 77 (HIV clinical).

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


# ── 121. Babesiosis — the New England ring, and the drug doxycycline does not cover ──────────
q(
    "A 71-year-old man comes to the emergency department due to 8 days of fever, drenching sweats "
    "and fatigue. He lives on Nantucket and gardens daily. Ten days ago another physician "
    "prescribed doxycycline for presumed Lyme disease; he has taken every dose and feels worse. He "
    "recalls no tick bite. Temperature is 39.1 C (102.4 F), blood pressure is 106/64 mm Hg and "
    "pulse is 104/min. There is scleral icterus and mild splenomegaly. The urine is dark.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.9 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 26% (N=41%–53%)\n"
    "Platelet count 74,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 6.8% (N=0.5%–1.5%)\n"
    "Lactate dehydrogenase 690 U/L (N=45–200 U/L)\n"
    "Haptoglobin <10 mg/dL (N=30–200 mg/dL)\n"
    "Aspartate aminotransferase 88 U/L (N=10–40 U/L)\n\n"
    "A Giemsa-stained peripheral smear is shown. Which of the following is the most appropriate "
    "treatment?",
    {
        "Azithromycin and atovaquone": "",
        "Artemether and lumefantrine":
            "Artemisinin-based combination therapy treats chloroquine-resistant malaria. Malaria "
            "would require travel to the tropics and would not be acquired while gardening on "
            "Nantucket, and artemisinins are not the treatment for babesiosis.",
        "Ceftriaxone and continued doxycycline":
            "This covers Lyme disease and anaplasmosis, the two infections that share this "
            "patient's reservoir and vector. Doxycycline has already failed here, and that failure "
            "is the clue — it has no useful activity against Babesia.",
        "Chloroquine phosphate":
            "Chloroquine blocks heme polymerase, the enzyme with which Plasmodium detoxifies the "
            "heme released by digesting hemoglobin. Babesia is a different organism with a "
            "different metabolism, and chloroquine is not used to treat it.",
        "Gentamicin and ciprofloxacin":
            "This is the regimen for plague. Yersinia pestis is a bipolar-staining gram-negative "
            "rod acquired from rodents in the western United States, and it does not live inside "
            "red cells.",
    },
    "Azithromycin and atovaquone",
    "Babesiosis, caused by Babesia microti. Every element of the stem points to it: coastal New "
    "England in the warm months, a flu-like illness, and the laboratory triad of hemolytic anemia "
    "(low hemoglobin, high reticulocytes and lactate dehydrogenase, unmeasurable haptoglobin), "
    "thrombocytopenia and transaminase elevation. The smear shows small intra-erythrocytic ring "
    "forms — trophozoites 1–2 µm across, the size of bacteria.\n\n"
    "Two features of the stem are doing specific work. First, the absence of a remembered tick "
    "bite is expected rather than reassuring: the vector is the NYMPH of Ixodes scapularis, about "
    "the size of the dot over an 'i', and it feeds unnoticed. Second, the failure of doxycycline "
    "is the discriminator. Babesia, Borrelia burgdorferi (Lyme disease) and Anaplasma "
    "phagocytophilum share one reservoir (the white-footed mouse) and one vector (the Ixodes "
    "nymph), so co-infection is common and a single bite can deliver more than one organism. "
    "Doxycycline treats the other two and does nothing for this one. A New England patient who "
    "fails to improve on doxycycline for Lyme disease should be evaluated for babesiosis.\n\n"
    "Treatment is azithromycin PLUS atovaquone, given intravenously in severe disease. Atovaquone "
    "acts on the parasite's electron transport system. This man is in the severe-disease group by "
    "age alone; the elderly and the immunocompromised develop acute respiratory distress syndrome, "
    "disseminated intravascular coagulation, profound hemolysis and shock, while more than 40% of "
    "infections in healthy people are entirely asymptomatic.\n\n"
    "Educational objective: Babesiosis presents as hemolytic anemia with thrombocytopenia and "
    "transaminitis in a patient from the Northeast or upper Midwest, with ring forms inside red "
    "cells on a Giemsa smear. Treat with azithromycin plus atovaquone — doxycycline covers the "
    "Lyme and anaplasmosis co-infections but not Babesia.",
    "A tick the size of a poppy seed put a parasite inside his red blood cells. The parasite "
    "splits the cells open, which is why he is yellow, anemic and passing dark urine. The "
    "antibiotic he was given works on a different bug that the same tick also carries — so he "
    "needs the two drugs that actually kill this one.",
    image="fig_babesia_rings",
    imcap="Giemsa-stained peripheral smear, oil immersion",
)

# ── 122. Why the nymph is the vector, and why no one remembers the bite ───────────────────────
q(
    "A 38-year-old man is admitted with babesiosis confirmed on a Giemsa-stained smear. He hikes "
    "in coastal Connecticut every weekend and checks himself for ticks after every hike. He is "
    "certain he has not been bitten, and he asks how he could have caught a tick-borne infection. "
    "The four life stages of the vector are shown, photographed together at the same "
    "magnification.\n\n"
    "Which of the following best explains why this patient has no history of a tick bite?",
    {
        "Nymphal ticks are too small to be seen and removed": "",
        "Babesia is acquired by inhaling aerosolized rodent excreta":
            "That is the route for hantavirus and Lassa fever, neither of which has an arthropod "
            "vector at all. Babesia must be deposited under the skin by a feeding tick.",
        "Only the adult female tick is capable of transmitting Babesia":
            "The reverse is true. An adult tick is conspicuous enough to be found and removed, "
            "which is precisely why it transmits less often than the nymph does.",
        "Ticks hatch already infected, so no blood meal is required":
            "There is no transovarial transmission — an infected female does not pass the organism "
            "to her eggs. Every tick must acquire Babesia by feeding on an infected white-footed "
            "mouse, which is why the nymph, the first stage to feed after moulting, is the vector.",
        "Transmission occurs through the bite of the cat flea":
            "The cat flea transmits Bartonella henselae between cats, and the rat flea transmits "
            "Yersinia pestis. Neither has any role in babesiosis.",
    },
    "Nymphal ticks are too small to be seen and removed",
    "The nymph of Ixodes scapularis is the principal vector of babesiosis, and of Lyme disease and "
    "anaplasmosis with it. Two facts combine, and they compound.\n\n"
    "First, ticks are not born infected. There is no transovarial transmission, so every tick must "
    "acquire the organism by feeding. The nymph is the first stage to feed after moulting, and it "
    "takes that meal from the white-footed mouse (Peromyscus leucopus) — the reservoir for "
    "babesiosis, Lyme disease, anaplasmosis, Powassan virus and hantavirus. One mouse and one "
    "tick account for five northeastern diseases, which is also why co-infection is common.\n\n"
    "Second, and decisively, a nymph cannot be seen. As the photograph shows, the size drop from "
    "adult to nymph is dramatic; a nymph is roughly the size of a printed full stop and is "
    "routinely mistaken for a freckle. It therefore stays attached long enough to transmit. An "
    "adult tick is noticed and pulled off. Transmission here is a function of going unnoticed "
    "rather than of biological potency — so a careful tick check is not the protection this "
    "patient believes it to be, and a negative bite history must never be used to argue against "
    "the diagnosis.\n\n"
    "Educational objective: The Ixodes scapularis nymph transmits babesiosis because it is the "
    "first stage to feed after acquiring the organism from the white-footed mouse and because it "
    "is too small to be seen and removed. Most patients report no tick bite, and that absence does "
    "not weigh against the diagnosis.",
    "Baby ticks are about the size of a period at the end of a sentence, and they look like a "
    "freckle. Freckles do not move, but nobody looks that closely. The adult tick is big enough to "
    "spot and flick off — so the one you never see is the one that gives you the disease.",
    image="fig_hx_ixodes_stages",
    imcap="The four life stages of Ixodes scapularis, at one magnification",
)

# ── 123. Thick versus thin — what each preparation is for ─────────────────────────────────────
q(
    "A 27-year-old man comes to the emergency department due to 4 days of fever, rigors and "
    "drenching sweats occurring without any discernible pattern. He returned 12 days ago from "
    "6 weeks in rural Nigeria and took no chemoprophylaxis. Temperature is 39.8 C (103.6 F). "
    "Examination shows scleral icterus and he is intermittently confused.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.2 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 25% (N=41%–53%)\n"
    "Platelet count 62,000/mm3 (N=150,000–400,000/mm3)\n"
    "Total bilirubin 4.6 mg/dL (N=0.1–1.2 mg/dL)\n\n"
    "Two Giemsa-stained preparations of his blood are shown. Preparation A establishes that "
    "parasites are present. Which of the following is the principal reason to examine "
    "preparation B as well?",
    {
        "It allows the infecting species to be identified": "",
        "It can be prepared and read without a Giemsa stain":
            "Both preparations use a Giemsa stain, and both require time and a proficient "
            "microscopist. The stain is not what separates them.",
        "It concentrates the parasites by lysing the red cells first":
            "That describes preparation A. Pre-lysing the red cells releases the parasites and "
            "concentrates them on the slide, which is what makes the thick film the sensitive "
            "screening test.",
        "It detects circulating parasite antigen within 10 minutes":
            "That is a rapid diagnostic test, not a stained film. Rapid tests matter because "
            "malaria is common where microscopes and polymerase chain reaction are not available, "
            "but they are a separate method.",
        "It is substantially more sensitive at low parasite densities":
            "Sensitivity runs the other way. Far less blood is examined per field when the red "
            "cells are left intact, so this preparation is the less sensitive of the two.",
    },
    "It allows the infecting species to be identified",
    "This is malaria, almost certainly Plasmodium falciparum: sub-Saharan travel without "
    "prophylaxis, an irregular rather than a clockwork fever, hemolytic anemia with "
    "thrombocytopenia and jaundice, and confusion indicating cerebral involvement. Falciparum is "
    "both the most common and the most virulent species, and its erythrocytic cycles are not "
    "synchronized — which is why the fever has no period and why there is no fever-free window in "
    "which the patient recovers. The synchronized species do have a clock: 24 hours for "
    "P. knowlesi, 48 for P. vivax and P. ovale, 72 for P. malariae. The interval is simply the "
    "length of the erythrocytic cycle, because each wave of red cell lysis releases a wave of "
    "merozoites.\n\n"
    "The two films answer two different questions.\n\n"
    "THICK film (A) — is it there? The red cells are lysed before staining, releasing and "
    "concentrating the parasites, so far more blood is examined per field. It is the sensitive "
    "presence-or-absence screen, but the cell context is destroyed and the species cannot be "
    "called.\n\n"
    "THIN film (B) — which one? Parasites are seen inside intact red cells. Preserved morphology "
    "allows the species to be identified and the parasite density to be estimated, at the cost of "
    "sensitivity.\n\n"
    "Species and density are not academic here. Severe falciparum disease with neurologic "
    "involvement is a medical emergency in which patients can die within 24 hours, and the "
    "parasite density guides how aggressively it is treated.\n\n"
    "Educational objective: The thick blood film screens for the presence of malaria parasites by "
    "lysing red cells and concentrating the organisms; the thin film preserves red cell morphology "
    "so that the species can be identified and the parasite density estimated. Thick asks whether "
    "parasites are there, thin asks which one.",
    "Two ways of looking at the same blood. The first squashes lots of blood onto the slide and "
    "pops the red cells, so you can spot whether any parasites are hiding in there. The second "
    "leaves the cells whole, so you can see which parasite it is — which tells you how frightened "
    "to be and which drug to use.",
    image="fig_hx_thick_thin",
    imcap="Two Giemsa-stained preparations from the same patient: A and B",
)

# ── 124. Cat scratch disease — the claw is the needle, not the source ─────────────────────────
q(
    "A 7-year-old girl is brought to the office due to a tender lump in the right side of her neck "
    "for 5 days. Twelve days ago the family adopted a kitten, which scratched her right cheek and "
    "forearm during play. Temperature is 37.9 C (100.2 F). Examination shows a 3-cm tender, mobile "
    "right cervical lymph node and the healing lesions shown. The remainder of the examination is "
    "normal. Her mother has bathed the kitten twice and asks how the infection was transmitted.\n\n"
    "Which of the following is the most likely source of the organism?",
    {
        "Flea feces deposited on the kitten's fur and claws": "",
        "Aerosolized oocysts from the kitten's litter tray":
            "That is the route for Toxoplasma gondii, which causes a mononucleosis-like illness in "
            "immunocompetent hosts and congenital or reactivation disease otherwise. It is not "
            "transmitted by a scratch.",
        "Bacteria multiplying within the keratin of the claw":
            "Intuitive, and wrong. The claw is the delivery needle rather than the reservoir; it "
            "becomes contaminated from the coat. This distinction is what makes flea control on "
            "the cat genuine prevention.",
        "Larvae of a tick carried on the kitten's coat":
            "Ticks transmit babesiosis, Lyme disease and anaplasmosis, none of which produce an "
            "inoculation papule at a scratch line followed by a single draining node.",
        "Staphylococcus aureus from the child's own skin":
            "A staphylococcal wound infection produces local cellulitis or an abscess within days, "
            "not a solitary tender node appearing one to three weeks after a healing scratch.",
    },
    "Flea feces deposited on the kitten's fur and claws",
    "Cat scratch disease, caused by Bartonella henselae — a fastidious, pleomorphic gram-negative "
    "COCCOBACILLUS. The presentation is textbook: a child under 10, a kitten (kittens are the most "
    "likely source), an inoculation papule at the scratch line, and tender regional lymphadenopathy "
    "draining that site. The timings fit as well — incubation 3–10 days, the papular stage at 3–14 "
    "days, the nodal stage at 1–3 weeks.\n\n"
    "The mechanism is the point of the question. The organism does not live on the cat's claws. It "
    "circulates between cats by the CAT FLEA, and it is present in FLEA FECES, which contaminate "
    "the fur and claws as the cat grooms and scratches. The claw inoculates that material through "
    "the skin. This is why the Centers for Disease Control figure of the life cycle is mostly "
    "flea, and why flea control on the cat prevents disease in the household.\n\n"
    "Management: do NOT send a culture. Bartonella is fastidious and takes weeks to grow, which is "
    "useless clinically. Use enzyme immunoassay for IgG and IgM, or polymerase chain reaction of "
    "node material when definitive proof is needed; a Warthin–Starry silver stain will show the "
    "organisms in tissue. Treat with azithromycin, adding rifampin only if severe. The illness is "
    "self-limiting over 5–6 weeks with an excellent prognosis.\n\n"
    "Two deliberate traps: Bartonella is not BORDETELLA (whooping cough), and the disease is cat "
    "scratch DISEASE, not cat scratch fever.\n\n"
    "Educational objective: Cat scratch disease follows inoculation of flea feces — not claw flora "
    "— through the skin by a cat scratch, producing a papule and then tender regional "
    "lymphadenopathy. Diagnose with serology or polymerase chain reaction rather than culture, and "
    "treat with azithromycin.",
    "The bug does not live on the cat's claws. It lives in flea poo, which ends up all over the "
    "cat's fur when it grooms. The claw is just the needle that pushes it under the skin. That is "
    "why getting rid of the cat's fleas actually protects the child.",
    image="fig_hx_csd_papule",
    imcap="Healing lesions along the scratch line",
)

# ── 125. The silver stain and its very short differential ────────────────────────────────────
q(
    "A 9-year-old boy undergoes excisional biopsy of a 4-cm tender left axillary lymph node that "
    "has been enlarging for 3 weeks. He has had a low-grade fever and sore throat. Culture of the "
    "node has been negative at 5 days and remains in the incubator. Histologic sections show "
    "necrotizing granulomatous inflammation with stellate microabscesses. A Warthin–Starry silver "
    "stain of the node is shown.\n\n"
    "Which of the following organisms is most likely responsible?",
    {
        "Bartonella henselae": "",
        "Bordetella pertussis":
            "The look-alike name is the trap, and the diseases are unrelated: Bordetella pertussis "
            "causes whooping cough, a paroxysmal cough illness with no lymphadenitis and no "
            "argyrophilic staining.",
        "Helicobacter pylori":
            "Also argyrophilic — this is a fair distractor rather than a silly one — but it is "
            "found in gastric mucosa, where it causes gastritis and peptic ulceration. It does not "
            "cause a necrotizing axillary lymphadenitis in a child.",
        "Legionella pneumophila":
            "Argyrophilic as well, and demonstrated by silver stain in lung tissue in a severe "
            "pneumonia. The clinical context here is a node, not a lung.",
        "Treponema pallidum":
            "Spirochetes take up silver, and syphilis can cause lymphadenopathy — but it would be "
            "generalized and painless, in an adult, with a chancre or a rash rather than a "
            "solitary tender axillary node in a 9-year-old.",
    },
    "Bartonella henselae",
    "Warthin–Starry silver staining demonstrates ARGYROPHILIC (literally 'silver-loving') "
    "organisms, which appear black against a pale background. Only a short list of organisms does "
    "this, which is what makes it such a clean examination question:\n\n"
    "• Bartonella — a lymph node, after a cat exposure\n"
    "• Spirochetes, such as Treponema\n"
    "• Legionella — lung, in a pneumonia\n"
    "• Helicobacter pylori — gastric mucosa\n\n"
    "The stain narrows the field to four; the clinical context picks the winner. A child with a "
    "tender node draining an upper limb, necrotizing granulomas with stellate microabscesses, and "
    "a culture that is going nowhere is cat scratch disease.\n\n"
    "The negative culture is itself a finding rather than a disappointment. Bartonella is "
    "fastidious and takes two to three weeks to grow, so culture should not have been the strategy: "
    "serology (enzyme immunoassay for IgG and IgM) or polymerase chain reaction of node material "
    "is how the diagnosis is made. Treat with azithromycin.\n\n"
    "Worth keeping alongside this: Bartonella is one of the three coccobacilli to be able to name "
    "on sight — Bartonella, Haemophilus and Bordetella — and the same organism causes an entirely "
    "different disease in an immunocompromised host, namely bacillary angiomatosis.\n\n"
    "Educational objective: A Warthin–Starry silver stain showing black bacilli narrows the "
    "differential to Bartonella, spirochetes, Legionella and Helicobacter pylori. In a lymph node "
    "after a cat exposure, the organism is Bartonella henselae.",
    "A special stain coats certain bugs in silver so they turn black and you can actually see "
    "them. Only about four bugs do this, so the stain plus the body part almost always gives you "
    "the answer: black rods in a swollen gland after a kitten scratch is Bartonella.",
    image="fig_warthin_starry",
    imcap="Warthin–Starry silver stain of the excised lymph node",
)

# ── 126. Bacillary angiomatosis — why the serology is meaningless, and what to do instead ─────
q(
    "A 38-year-old man with AIDS comes to the office due to skin lesions for 6 weeks. He stopped "
    "antiretroviral therapy 2 years ago. His CD4 count is 40/mm3. Examination shows more than "
    "twenty friable, cherry-red cutaneous papules on the trunk and arms, several with a collarette "
    "of scale, and a 2-cm violaceous nodule on the left forearm. Bartonella IgG and IgM serology "
    "is negative.\n\n"
    "Which of the following is the most appropriate next step in management?",
    {
        "Biopsy of a cutaneous lesion for histopathology": "",
        "Blood culture incubated for 3 weeks to recover the organism":
            "Bartonella is fastidious and takes two to three weeks to grow, so culture is too slow "
            "to be useful and is not how either of its diseases is diagnosed.",
        "Empiric azithromycin for presumed cat scratch disease":
            "Azithromycin is the drug for cat scratch disease in an immunocompetent host. "
            "Bacillary angiomatosis is treated with erythromycin and/or doxycycline — and the "
            "diagnosis must be secured first, because the differential includes a malignancy.",
        "Measurement of human herpesvirus 8 viral load in blood":
            "Human herpesvirus 8 drives Kaposi sarcoma, which is exactly the lesion that must be "
            "excluded here — but the two are separated histologically, on tissue, not by a "
            "serum viral load.",
        "Repeat Bartonella serology in 4 weeks to show seroconversion":
            "Repeating a test that is unreliable in this population will not help. Waiting a month "
            "also risks visceral dissemination of an infection that can be fatal untreated.",
    },
    "Biopsy of a cutaneous lesion for histopathology",
    "This is bacillary angiomatosis — Bartonella henselae (occasionally B. quintana) in a severely "
    "immunocompromised host, producing a vascular proliferation of small vessels in skin and "
    "viscera. Note the fork: ONE organism causes TWO diseases, and the variable that decides which "
    "is the state of the patient's immune system. Immunocompetent gets cat scratch disease — a "
    "papule and a tender draining node. Immunocompromised gets bacillary angiomatosis — "
    "cherry-red vascular papules and nodules that are progressive and fatal if untreated.\n\n"
    "Two things make biopsy the answer.\n\n"
    "First, the negative serology means almost nothing here. Serology detects the HOST's antibody "
    "response, and this host has a CD4 count of 40 and may not be producing much antibody. A test "
    "that looks for the patient's own response will underperform in exactly the population that "
    "gets this disease. Contrast cat scratch disease in a healthy child, where serology works well "
    "— the same organism, a different test strategy, because the host is different.\n\n"
    "Second, the critical differential is Kaposi sarcoma, an HHV-8-driven vascular malignancy that "
    "occurs in the same patients and looks very similar. The two cannot be told apart by "
    "inspection, and one is a curable bacterial infection while the other is a cancer. That is "
    "precisely why the diagnosis rests on lesion biopsy with histopathologic examination, "
    "supported by polymerase chain reaction.\n\n"
    "Once confirmed, treat with erythromycin and/or doxycycline AND restart antiretroviral "
    "therapy. Antibiotics alone will not hold the line in a host who cannot help.\n\n"
    "Educational objective: In bacillary angiomatosis, negative Bartonella serology does not "
    "exclude the diagnosis, because the immunocompromised host may not mount an antibody response. "
    "Diagnose by lesion biopsy with histopathology — which also distinguishes it from the Kaposi "
    "sarcoma it clinically resembles.",
    "His immune system is too weak to make antibodies, so a blood test that looks for his "
    "antibodies will come back negative even though he is infected. And these red bumps look "
    "exactly like a cancer that happens in the same patients. Both problems are solved the same "
    "way: cut one out and look at it under the microscope.",
)

# ── 127. Secondary plague pneumonia — the infection-control point ─────────────────────────────
q(
    "A 44-year-old man is hospitalized in New Mexico due to abrupt fever to 39.9 C (103.8 F), "
    "chills and an exquisitely tender 5-cm right inguinal mass. He had been camping and had handled "
    "several dead ground squirrels. Aspirate of the mass shows gram-negative rods that stain darkly "
    "at both ends, and gentamicin is begun. On hospital day 3 he develops a productive cough with "
    "blood-streaked frothy sputum and worsening hypoxemia. His chest radiograph is shown.\n\n"
    "Which of the following is the most appropriate infection-control measure?",
    {
        "Respiratory isolation and prophylaxis of close contacts": "",
        "Contact precautions only, since transmission requires a flea":
            "The flea delivered the original infection. Once the organism reaches the lungs the "
            "patient himself generates infectious aerosols, and the flea is no longer the relevant "
            "route.",
        "Isolation of the household pets and residential flea control":
            "Environmental and veterinary measures matter for preventing further cases from the "
            "original source, but they do nothing about the person who is aerosolizing Yersinia "
            "pestis in the ward tonight.",
        "No isolation, as the infiltrates represent pulmonary infarction":
            "Septic pulmonary infarcts would not explain bloody frothy sputum in a patient with "
            "proven plague, and dismissing the lung findings here would permit a ward outbreak of "
            "a disease that is 100% fatal untreated.",
        "Standard precautions, since bubonic plague is not contagious":
            "Bubonic plague itself is not spread person to person — which is exactly the reasoning "
            "trap. This patient no longer has purely bubonic plague; hematogenous spread has "
            "seeded his lungs.",
    },
    "Respiratory isolation and prophylaxis of close contacts",
    "This patient began with BUBONIC plague — Yersinia pestis, from a flea bite acquired handling "
    "rodents in the western United States, with a bubo in the node draining the bite and bipolar "
    "'safety pin' gram-negative rods on aspirate. He has now developed SECONDARY plague pneumonia: "
    "organisms reach the lymphatics, then the blood, and are filtered through the lungs, producing "
    "cough, hemorrhagic consolidation and bloody frothy sputum a couple of days into the illness.\n\n"
    "The distinction from PRIMARY plague pneumonia is the source, not the severity. Primary "
    "pneumonia follows direct inhalation of the bacillus and has a very short incubation of 1–3 "
    "days. Secondary pneumonia follows hematogenous spread from a bubo. Both are approximately 50% "
    "fatal even treated and 100% fatal untreated, and — the point of this question — BOTH TRANSMIT "
    "BY AEROSOL.\n\n"
    "So you do not need exposure to a labelled 'pneumonic plague' case to catch pneumonic plague. "
    "An ordinary bubonic admission that progresses is enough, and that chain is probably what made "
    "the 14th-century pandemic so catastrophic: bubonic case → secondary pneumonia → aerosol → "
    "primary pneumonia in the next person, which is rapidly fatal and itself highly "
    "transmissible.\n\n"
    "Continue gentamicin (or a fluoroquinolone); naturally occurring plague shows very little drug "
    "resistance. Send a rapid antigen test, which is 100% sensitive and 100% specific, and culture "
    "for sensitivities. Notify public health.\n\n"
    "Educational objective: Bubonic plague that spreads hematogenously to the lungs becomes "
    "secondary plague pneumonia, which transmits by aerosol just as primary plague pneumonia does. "
    "Such a patient requires respiratory isolation and prophylaxis of contacts.",
    "He caught plague from a flea, and it started as a swollen gland in the groin. Now the "
    "bacteria have travelled through his blood into his lungs — and a person coughing plague "
    "bacteria can give it straight to the next person through the air. So he has to be isolated "
    "and the people around him need antibiotics.",
    image="fig_plague_cxr",
    imcap="Chest radiograph on hospital day 3",
)

# ── 128. Resistant plague is a public-health signal, not a pharmacology problem ───────────────
q(
    "Over 4 days, six previously healthy adults in a midwestern city are admitted with fulminant "
    "pneumonia, hemoptysis and shock. None has left the city and none has had rodent contact; no "
    "rodent die-off has been reported in the region. Blood and sputum cultures from all six grow "
    "Yersinia pestis. Sensitivity testing shows high-level resistance to gentamicin, doxycycline, "
    "ciprofloxacin and trimethoprim-sulfamethoxazole.\n\n"
    "Which of the following best explains these findings?",
    {
        "Deliberate release of a deliberately altered organism": "",
        "Acquisition of resistance genes from the flea's gut flora":
            "Fleas are not a reservoir of antibiotic resistance genes for this organism, and in "
            "any case no vector exposure occurred — six simultaneous cases without rodent or flea "
            "contact is itself the anomaly.",
        "Chromosomal mutation under antibiotic pressure in rodents":
            "Naturally occurring plague shows very little drug resistance, and rodents are not "
            "exposed to the antibiotic pressure that would select for it. There is also no "
            "epizootic here to have supplied the organism.",
        "Misidentification of the less virulent Yersinia pseudotuberculosis":
            "Yersinia pestis evolved from Yersinia pseudotuberculosis, but the latter causes "
            "enterocolitis and mesenteric adenitis, not fulminant hemorrhagic pneumonia with "
            "shock, and modern identification methods separate them reliably.",
        "Loss of the plasmid that permits the entry of antibiotics":
            "Antibiotic entry is not plasmid-encoded in this way. Resistance in Enterobacterales "
            "is typically GAINED — usually on a plasmid — rather than conferred by losing one.",
    },
    "Deliberate release of a deliberately altered organism",
    "Three things in this vignette do not belong together, and each one on its own should prompt "
    "the question.\n\n"
    "First, the geography and exposure are wrong. Plague is endemic in at least 17 mostly Pacific "
    "Coast and Western states — New Mexico, Colorado, California, Texas, Arizona, Oregon, Nevada — "
    "and there have been only about 150 United States cases since 2000. Human infection follows "
    "rodent or flea contact, because humans are a DEAD-END host that plague gains nothing from "
    "infecting. Six cases with no rodent contact and no epizootic is not a natural pattern.\n\n"
    "Second, the presentation is primary plague pneumonia — direct inhalation, incubation 1–3 "
    "days, sudden fever with dyspnea, hypoxia and hemoptysis. That is the form suited to aerosol "
    "dissemination.\n\n"
    "Third, and most specifically, the resistance pattern. Naturally occurring Yersinia pestis "
    "shows very little drug resistance, which is why gentamicin or a fluoroquinolone reliably "
    "works. High-level resistance across four unrelated antibiotic classes at once has to be "
    "explained, and human alteration is the explanation that fits. Plague has a long history as a "
    "biological weapon: rapid onset, high mortality, and aerosol transmissibility in the pneumonic "
    "form.\n\n"
    "The action is to notify public health and law enforcement immediately, isolate the patients "
    "with respiratory precautions, and provide prophylaxis to contacts.\n\n"
    "Educational objective: Yersinia pestis is characteristically susceptible to antibiotics, so "
    "highly resistant isolates — particularly in a cluster of primary pneumonic cases outside the "
    "endemic west and without rodent exposure — should raise the possibility of a deliberately "
    "engineered organism and prompt immediate notification of public health.",
    "Plague is normally easy to kill with antibiotics and normally comes from rodents in the "
    "American west. Here the germ shrugs off four different antibiotics, nobody touched a rodent, "
    "and six people got sick at once in the wrong part of the country. Germs do not do that by "
    "themselves — somebody made it happen.",
)

# ── 129. Why a vaccinated health worker still caught Ebola ────────────────────────────────────
q(
    "A 29-year-old nurse who has been working in an Ebola treatment unit in eastern Democratic "
    "Republic of the Congo develops fever, vomiting and profuse diarrhea. On day 7 a maculopapular "
    "rash appears on her face and spreads to her neck and upper trunk. She received Ervebo, the "
    "licensed Ebola vaccine, 2 years ago and has documented anti-glycoprotein antibodies. "
    "Reverse-transcriptase polymerase chain reaction of blood is positive for Ebola virus.\n\n"
    "Which of the following best explains this outcome?",
    {
        "The outbreak strain differs from the vaccine strain": "",
        "Antibody to the nucleoprotein does not neutralize the intact virion":
            "True of nucleoprotein antibody in general, but not the explanation here — Ervebo "
            "encodes the surface GLYCOPROTEIN, and her documented antibodies are against that "
            "glycoprotein.",
        "Live attenuated vaccines do not generate durable antibody":
            "Live attenuated platforms characteristically generate strong, durable responses, and "
            "in any case her antibodies are documented as present.",
        "Prior filovirus infection blocks the response to the vector":
            "Anti-vector immunity is a genuine limitation of viral-vector vaccines, but there is "
            "no history of prior filovirus infection and she did respond to the vaccine.",
        "The vaccine requires a booster dose every twelve months":
            "There is no annual booster schedule for Ervebo, and an inadequate titre is not the "
            "problem in a patient with documented antibody.",
    },
    "The outbreak strain differs from the vaccine strain",
    "Strain mismatch. Every licensed product against Ebola was built against ZAIRE ebolavirus, "
    "because Zaire was the strain rampant when they were developed:\n\n"
    "• Ervebo — a live attenuated recombinant vesicular stomatitis virus (VSV) vector in which the "
    "VSV glycoprotein genes are replaced by Ebola glycoprotein genes. Zaire only. (VSV is a "
    "rhabdovirus, the family that includes rabies — it is not a poxvirus.)\n"
    "• Inmazeb and Ebanga — monoclonal antibodies, both targeting the surface glycoproteins. Zaire "
    "only.\n\n"
    "The current outbreak is driven by BUNDIBUGYO ebolavirus, against which there is very little "
    "cross-protection, whether the patient received the vaccine or the monoclonals. That is why a "
    "vaccinated health worker can still develop Ebola, and why the Zaire-directed treatments are "
    "underperforming in this outbreak. AstraZeneca (viral vector) and Moderna (mRNA) candidates "
    "carrying Bundibugyo glycoprotein are in trials.\n\n"
    "The rest of the vignette is classic filovirus disease: an ssRNA virus of the Filoviridae with "
    "an extraordinarily wide host cell range — monocytes and macrophages (the cytokine storm and "
    "the courier system), dendritic cells (early immunosuppression), endothelium (leak and "
    "hemorrhage), hepatocytes (transaminase rise and failed clotting factor synthesis) and adrenal "
    "cells (hypotension). The reservoir is the Egyptian rousette fruit bat; there is NO insect "
    "vector for any filovirus. The day 6–7 rash spreading face → neck and trunk → limbs is "
    "expected, and it is harder to see on darker skin, where its apparent absence must not be "
    "taken as evidence against the diagnosis.\n\n"
    "Manage with early supportive care and rehydration, which reliably improves survival, plus "
    "experimental remdesivir and pan-Ebola monoclonals.\n\n"
    "Educational objective: Ervebo, Inmazeb and Ebanga were all developed against Zaire ebolavirus "
    "glycoproteins and provide little cross-protection against other Ebola strains. Infection in a "
    "vaccinated patient during a Bundibugyo outbreak reflects strain mismatch.",
    "Her vaccine taught her immune system to recognise one particular version of Ebola. The "
    "version circulating now is a different cousin, and her antibodies do not grip it properly — "
    "like a key cut for a lock that has since been changed.",
    exim="fig_filovirus_em",
    excap="Filovirus on electron micrograph — the filament and its shepherd's-crook hook",
)

# ── 130. Marburg — the same disease, and nothing approved to give ─────────────────────────────
q(
    "A 34-year-old geologist is admitted 9 days after returning from Uganda, where he spent a week "
    "surveying a cave system inhabited by fruit bats. He has fever, severe myalgia, vomiting and, "
    "since day 6, a maculopapular rash. He now has bleeding from the gums and oozing from every "
    "venipuncture site. Temperature is 39.4 C (102.9 F) and blood pressure is 88/50 mm Hg. "
    "Reverse-transcriptase polymerase chain reaction is positive for Marburg virus. An electron "
    "micrograph of a culture specimen is shown.\n\n"
    "Which of the following is the most appropriate treatment?",
    {
        "Supportive care directed at preventing shock": "",
        "Convalescent plasma from a recovered Ebola patient":
            "Ebola and Marburg are morphologically identical filoviruses with the same reservoir, "
            "but they are different viruses. Antibody raised against one does not reliably "
            "neutralize the other, and convalescent plasma is not an approved therapy for either.",
        "Inmazeb, a monoclonal antibody combination":
            "Inmazeb targets Ebola Zaire surface glycoproteins. No monoclonal antibody is approved "
            "for Marburg virus.",
        "Post-exposure vaccination with Ervebo":
            "Ervebo is a Zaire-directed Ebola vaccine. There is no licensed Marburg vaccine, and "
            "vaccinating a patient who is already viremic and bleeding would not help.",
        "Ribavirin, a guanosine analogue":
            "Ribavirin is the one antiviral with any evidence in this block, and it belongs to "
            "Lassa fever — where it is used despite mixed results. It has no established role in "
            "filovirus disease.",
    },
    "Supportive care directed at preventing shock",
    "Marburg virus disease. The tell is CAVE exposure: Marburg is classically acquired from "
    "infected Egyptian rousette fruit bats, especially in caves, and the prominent hemorrhage fits "
    "— bleeding is MORE common in Marburg than in Ebola.\n\n"
    "Marburg and Ebola are the same family, the same morphology (ssRNA filoviruses, roughly 80 nm "
    "by up to 800 nm, with the characteristic filament and hook), the same reservoir bat, and the "
    "same human-to-human route by body fluids. Marburg simply does it harder, by three mechanisms "
    "worth being able to state: it blocks the type I interferon response more effectively "
    "(removing the innate antiviral brake is the founding event of the whole pathogenesis); it is "
    "far more likely to induce a massive cytokine storm; and it destroys blood vessels directly, "
    "which is why hemorrhage is more prominent. Fatality is about 50%, reaching 88–90% in severe "
    "outbreaks.\n\n"
    "Where the two diverge completely is treatment. Ebola has two licensed monoclonals (Inmazeb, "
    "Ebanga) and a licensed vaccine (Ervebo). For Marburg there are NO approved monoclonals, NO "
    "approved antivirals and NO approved vaccine. Management is supportive care aimed at avoiding "
    "shock: fluids, blood pressure support, oxygenation and correction of what the coagulopathy has "
    "consumed. Confirm with reverse-transcriptase polymerase chain reaction.\n\n"
    "The reason for the gap is economic rather than scientific — Marburg produces a handful of "
    "cases a year, too few to justify commercial development, and the platform that produced "
    "Ervebo would very likely work. That is what makes a disease 'neglected'.\n\n"
    "Also remember the naming point: Marburg is the one filovirus not named after an African "
    "place. It is a German university town, where laboratory workers handling African green monkey "
    "tissue from Uganda were infected in the first recognized outbreak.\n\n"
    "Educational objective: Marburg virus is acquired from fruit bats, classically in caves, and "
    "causes a filovirus hemorrhagic fever with more bleeding and higher mortality than Ebola. No "
    "antiviral, monoclonal antibody or vaccine is approved, so treatment is supportive care aimed "
    "at preventing shock.",
    "It is Ebola's meaner cousin, caught from bats in caves. There is no drug and no vaccine for "
    "it at all — so all doctors can do is keep his blood pressure up, replace fluids and blood "
    "products, and let his body fight.",
    image="fig_hx_marburg_em",
    imcap="Electron micrograph of the isolate",
)

# ── 131. Lassa — the sequela that names the virus ─────────────────────────────────────────────
q(
    "A 29-year-old aid worker is admitted after returning from rural Nigeria, where she lived in a "
    "village with a heavy rodent infestation. She has had 10 days of fever, sore throat, "
    "retrosternal chest pain, vomiting and diarrhea, and now has facial and neck edema, "
    "conjunctival injection and 2+ proteinuria. Enzyme-linked immunosorbent assay for Lassa virus "
    "IgM is positive. She is given ribavirin and supportive care, and improves over 2 weeks.\n\n"
    "Which of the following long-term complications should she be counselled about?",
    {
        "Bilateral sensorineural hearing loss": "",
        "Chronic kidney disease requiring dialysis":
            "Renal failure out of proportion to everything else is the signature of hantavirus "
            "hemorrhagic fever with renal syndrome, where acute kidney injury is the usual cause "
            "of death. Lassa can cause proteinuria acutely but is not a cause of chronic dialysis "
            "dependence.",
        "Chronic destructive polyarthritis of the hands":
            "Persistent joint disease follows chikungunya, an alphavirus taught with the "
            "musculoskeletal block, not Lassa fever.",
        "Progressive visual loss from chorioretinitis":
            "Retinitis in this context suggests cytomegalovirus in advanced HIV, not an "
            "arenavirus.",
        "Recurrent febrile relapses at 48-hour intervals":
            "A fever on a 48-hour clock is Plasmodium vivax or ovale, whose synchronized "
            "erythrocytic cycles set the interval. Lassa does not relapse on a schedule.",
    },
    "Bilateral sensorineural hearing loss",
    "Lassa fever, an Arenaviridae infection. New bilateral sensorineural hearing loss after a "
    "febrile illness acquired in West Africa is Lassa until proven otherwise — no other agent in "
    "this block produces that sequela, and roughly a third of survivors are affected. Survivors "
    "also report hair loss, tremor, balance difficulty and difficulty speaking, and post-Lassa "
    "encephalitis has been described.\n\n"
    "The reservoir is the multimammate rat, Mastomys natalensis, which is abundant across Nigeria "
    "and neighbouring countries. There is NO arthropod vector. Three routes in, and all of them "
    "involve the rodent: direct contact with its urine, feces or bodily fluids; inhalation of "
    "aerosolized excreta; and eating the rodent as food. Human-to-human transmission then follows "
    "blood, tissue, secretions and excretions — which is why the first notable United States "
    "experience with Lassa was laboratory-acquired, in a research group at Yale.\n\n"
    "Her course maps onto the staged natural history: stage I is a mild febrile illness where "
    "about 80% of patients stop; stage II adds sore throat, retrosternal chest pain, vomiting and "
    "diarrhea; stage III adds head and neck edema, conjunctival injection, proteinuria and "
    "hypotension; stage IV is altered mental status, convulsions and bleeding. Overall mortality is "
    "about 1%, far below the ~30% of Crimean–Congo hemorrhagic fever.\n\n"
    "Lassa is also the ONLY agent in this group with any specific drug: ribavirin, a guanosine "
    "analogue that inhibits viral RNA synthesis. The evidence is mixed and it is not a good drug, "
    "but it is used. Dengue, hantavirus and Crimean–Congo have no antiviral at all.\n\n"
    "Educational objective: Lassa fever is acquired from the multimammate rat Mastomys natalensis "
    "in West Africa, with no arthropod vector. Its characteristic sequela is new bilateral "
    "sensorineural hearing loss, and it is the only viral hemorrhagic fever in this group for "
    "which an antiviral — ribavirin — is used.",
    "The virus came from rat droppings in her village. Most people who survive are fine, but a "
    "large minority come out of it deaf in both ears, permanently. That deafness is so "
    "characteristic that it is almost the virus signing its name.",
)

# ── 132. Crimean–Congo — the tick, and the animals that stay well ─────────────────────────────
q(
    "A 45-year-old sheep farmer in eastern Turkey is admitted due to 4 days of abrupt fever, severe "
    "headache, myalgia, conjunctivitis and abdominal pain. Today he has bleeding gums, widespread "
    "petechiae and hemoptysis. His flock is healthy. The engorged arthropod shown was removed from "
    "his groin 8 days ago. Platelet count is 28,000/mm3 and aspartate aminotransferase is 640 U/L "
    "(N=10–40 U/L). Reverse-transcriptase polymerase chain reaction is positive for Crimean–Congo "
    "hemorrhagic fever virus.\n\n"
    "Which of the following best describes how the arthropod became infected?",
    {
        "By feeding on livestock that carry the virus asymptomatically": "",
        "By feeding on an infected human during a previous outbreak":
            "Human-to-tick transmission is not how this cycle is maintained. Humans are incidental "
            "here; the virus circulates between ticks and vertebrate animals.",
        "By hatching from eggs laid by an infected female mosquito":
            "The vector is a tick, not a mosquito, and mosquito-borne hemorrhagic fever in this "
            "block means dengue, whose reservoir is humans and whose vector is Aedes aegypti.",
        "By ingesting the virus from rodent urine in the environment":
            "Environmental rodent excreta transmit hantavirus and Lassa fever, and neither has an "
            "arthropod vector at all.",
        "By mechanical carriage of virus on its mouthparts after a bite":
            "An arthropod that merely carries a pathogen on its mouthparts delivers far too small "
            "an inoculum. A true vector amplifies the organism inside its own body first — that is "
            "what makes it a vector rather than a contaminated needle.",
    },
    "By feeding on livestock that carry the virus asymptomatically",
    "Crimean–Congo hemorrhagic fever, a Nairovirus within the Bunyaviridae, and a small disease "
    "with a disproportionate examination footprint — roughly 1,000 cases a year worldwide, "
    "concentrated in Africa, the Middle East, Asia and southeastern Europe, with a dense band "
    "across Turkey, the Balkans, the Caucasus and Iran.\n\n"
    "The vector is the HYALOMMA tick, recognizable by its banded legs. It acquires the virus by "
    "feeding on livestock and birds — which carry it and remain completely well. A healthy-looking "
    "reservoir animal is the rule across this whole block, not the exception: the Egyptian fruit "
    "bat with filoviruses is not sick either. So a farmer whose flock looks perfectly healthy is "
    "not evidence against the diagnosis, and the detail is in the stem deliberately.\n\n"
    "A second route exists and this patient has access to it: direct contact with infected animal "
    "or human blood, which is why slaughterhouse and veterinary exposures count.\n\n"
    "Do not confuse Hyalomma with Ixodes. Both are hard ticks, but Ixodes scapularis points at "
    "Lyme disease, babesiosis and anaplasmosis in the northeastern United States, not at "
    "Crimean–Congo.\n\n"
    "Numbers worth carrying: about 88% of infections are subclinical, and mortality among those "
    "who do become symptomatic is about 30% — far higher than dengue or Lassa. There is no "
    "antiviral. Treatment is supportive, and the prescribing rule that spans every viral "
    "hemorrhagic fever applies: acetaminophen for fever and pain, NEVER non-steroidal "
    "anti-inflammatory drugs, which inhibit platelet function in a patient who is already bleeding.\n\n"
    "Educational objective: Crimean–Congo hemorrhagic fever virus is transmitted by the Hyalomma "
    "tick, which acquires it from livestock and birds that carry the virus without becoming ill. "
    "Direct contact with infected animal blood is a second route, mortality among symptomatic "
    "patients is about 30%, and treatment is supportive with acetaminophen rather than "
    "anti-inflammatory drugs.",
    "The tick picked the virus up from his sheep — but the sheep were never sick, so nobody "
    "suspected them. Plenty of these viruses live quietly in animals that look completely healthy, "
    "and only cause havoc once they get into a person.",
    image="fig_hx_hyalomma",
    imcap="The arthropod removed from the patient's groin",
)

# ── 133. Dengvaxia — the vaccine with a prerequisite ──────────────────────────────────────────
q(
    "A 15-year-old boy who lives in Puerto Rico comes to the office with his mother for a "
    "well-child visit. Two classmates were hospitalized with dengue last month, and his mother "
    "asks about the dengue vaccine. He is healthy and takes no medications. He has never had a "
    "febrile illness diagnosed as dengue, and serologic testing shows no evidence of previous "
    "dengue infection.\n\n"
    "Which of the following is the most appropriate response?",
    {
        "Withhold the vaccine because he has no prior dengue infection": "",
        "Vaccinate him now, since protection is greatest before any exposure":
            "This inverts the indication. In a dengue-naive recipient the course of a subsequent "
            "natural infection can be more severe, which is the whole reason the prerequisite "
            "exists.",
        "Vaccinate him only after confirming he is seronegative for all four serotypes":
            "Seronegativity is the contraindication, not the entry criterion. A documented prior "
            "infection is what qualifies a patient.",
        "Withhold the vaccine because live vaccines cannot be given in endemic areas":
            "Living in an endemic area is an indication for vaccination, not a barrier to it. "
            "Dengvaxia is licensed precisely for endemic settings.",
        "Withhold the vaccine and give him doxycycline prophylaxis instead":
            "There is no antibacterial prophylaxis for a flavivirus. Prevention of dengue rests on "
            "Aedes mosquito control.",
    },
    "Withhold the vaccine because he has no prior dengue infection",
    "Dengvaxia is the single most examinable fact about dengue prevention, because it is an "
    "unusual vaccine: it is indicated ONLY for people with a documented previous dengue infection. "
    "In someone who has never had dengue, a subsequent natural infection after vaccination can run "
    "a rougher course. A vaccine with a prior-infection prerequisite is rare enough to be worth a "
    "question on its own.\n\n"
    "The construction of the vaccine is worth knowing as well: it is live attenuated, tetravalent "
    "and recombinant, built on the attenuated YELLOW FEVER vaccine virus as a backbone, into which "
    "genes encoding the surface proteins of all four dengue serotypes (DENV-1 to DENV-4) have been "
    "inserted. It was approved by the Food and Drug Administration in 2019.\n\n"
    "The rest of dengue prevention is vector control, and the reason is epidemiologic: HUMANS are "
    "the reservoir — no animal amplifier has been identified in the Western Hemisphere — and only "
    "about 24% of infections are clinically apparent, so roughly three quarters of the reservoir is "
    "invisible while remaining fully able to infect a feeding mosquito. You cannot isolate your way "
    "out of that; you control Aedes aegypti instead.\n\n"
    "Puerto Rico is the right setting for the question: most United States dengue cases occur "
    "there rather than in the continental states.\n\n"
    "Educational objective: The dengue vaccine (Dengvaxia) is indicated only for patients with a "
    "documented prior dengue infection and should be withheld from dengue-naive patients. "
    "Prevention otherwise depends on Aedes mosquito control, because humans are the reservoir and "
    "most infections are asymptomatic yet transmissible.",
    "This is a backwards vaccine: you can only have it if you have already had the disease once. "
    "Given to someone who has never had dengue, it can make a future infection worse rather than "
    "better — so he does not get it.",
)

# ── 134. qSOFA has three criteria, and heart rate is not one of them ──────────────────────────
q(
    "A 68-year-old man is on a surgical ward on postoperative day 2 after a hemicolectomy. The "
    "nurse calls because he looks unwell. Temperature is 38.4 C (101.1 F), blood pressure is "
    "96/58 mm Hg, pulse is 112/min and respirations are 26/min. He is alert and fully oriented, "
    "with a Glasgow Coma Scale score of 15. The resident calculates a quick Sequential Organ "
    "Failure Assessment (qSOFA) score of 2.\n\n"
    "Which of the following new findings would raise his qSOFA score to 3?",
    {
        "New disorientation to time, place and person": "",
        "Heart rate increasing to 130/min":
            "Tachycardia above 90/min is a SIRS criterion, not a qSOFA criterion. qSOFA "
            "deliberately omits heart rate.",
        "Leukocyte count increasing to 18,000/mm3":
            "Leukocytosis above 12,000/mm3 is a SIRS criterion. qSOFA is a bedside score that "
            "requires no laboratory value at all — that is the point of it.",
        "Serum lactate increasing to 4.0 mmol/L":
            "Lactate reflects tissue hypoperfusion, sits in the treatment bundle, and is part of "
            "the cellular and metabolic abnormality that defines septic shock. It is not one of "
            "the three qSOFA criteria.",
        "Temperature increasing to 39.6 C (103.3 F)":
            "Temperature is a SIRS criterion — and a bidirectional one, since hypothermia counts "
            "as well. It has no place in qSOFA.",
    },
    "New disorientation to time, place and person",
    "qSOFA has exactly THREE criteria, all available at the bedside without a single laboratory "
    "test:\n\n"
    "• Respiratory rate ≥ 22/min — the most sensitive early vital sign change\n"
    "• Systolic blood pressure ≤ 100 mm Hg — note ≤ 100, not < 90, so the score catches patients "
    "BEFORE frank hypotension\n"
    "• Altered mentation, assessed by Glasgow Coma Scale\n\n"
    "This patient already meets two (respirations 26/min, systolic 96 mm Hg) and is scoring 2. The "
    "only remaining criterion is mentation, so new confusion is what takes him to 3.\n\n"
    "Everything else offered belongs to a different instrument. Temperature, heart rate, "
    "respiratory rate and white cell count are the four SIRS criteria — and SIRS is no longer a "
    "defining criterion for sepsis, although the United States Centers for Medicare and Medicaid "
    "Services still uses it. Note also how bidirectional SIRS is: hypothermia below 38 C or "
    "hyperthermia above it, leukopenia below 4,000/mm3 or leukocytosis above 12,000/mm3, or more "
    "than 10% bands. A septic patient can be cold and leukopenic, which is easy to misread as 'not "
    "infected'.\n\n"
    "The wider point is that no single assessment is good enough. There are five competing scores "
    "— SIRS, SOFA, qSOFA, NEWS2, MEWS — precisely because none has adequate sensitivity and "
    "specificity, and that in turn is because the damage in sepsis comes from the dysregulated "
    "HOST RESPONSE rather than from any particular organism.\n\n"
    "Educational objective: The three qSOFA criteria are a respiratory rate ≥ 22/min, a systolic "
    "blood pressure ≤ 100 mm Hg, and altered mentation. Heart rate, temperature and white cell "
    "count belong to SIRS, and lactate belongs to the septic shock definition and the treatment "
    "bundle.",
    "The quick bedside sepsis check asks only three things: is he breathing fast, is his blood "
    "pressure low, and is he confused? He already ticks the first two. Getting confused is the "
    "only thing left that moves the number.",
)

# ── 135. Which marker actually points at a cause ──────────────────────────────────────────────
q(
    "A 74-year-old woman is in the intensive care unit on day 3 of treatment for life-threatening "
    "organ dysfunction following a perforated diverticulum. Blood, urine and peritoneal fluid "
    "cultures drawn before antibiotics remain negative. Temperature is 38.7 C (101.7 F), blood "
    "pressure is 88/50 mm Hg on norepinephrine, and urine output is 0.3 mL/kg/hr.\n\n"
    "Laboratory studies show:\n"
    "Leukocyte count 9,200/mm3 with 16% band forms (N=4,000–11,000/mm3)\n"
    "Platelet count 88,000/mm3 (N=150,000–400,000/mm3)\n"
    "Creatinine 2.4 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Lactate 3.8 mmol/L (N=0.5–2.2 mmol/L)\n"
    "C-reactive protein 240 mg/L (N=<5 mg/L)\n"
    "Procalcitonin 14 ng/mL (N=<0.1 ng/mL)\n\n"
    "The team is asked whether the negative cultures argue against a bacterial infection. Which of "
    "the following findings most specifically supports a bacterial cause?",
    {
        "The elevated procalcitonin": "",
        "The elevated C-reactive protein":
            "C-reactive protein is a sensitive but entirely non-specific marker of inflammation. "
            "It rises in viral infection, trauma, surgery, autoimmune disease and malignancy "
            "alike.",
        "The elevated lactate":
            "Lactate reflects tissue hypoperfusion, which is why it is central to the septic shock "
            "definition and sits in the treatment bundle. It measures severity, not etiology.",
        "The leukocyte count with 16% band forms":
            "A normal total white cell count with more than 10% immature forms does satisfy the "
            "sepsis laboratory criterion — and it is worth noticing rather than dismissing — but a "
            "left shift indicates marrow output under stress, not which organism caused it.",
        "The platelet count of 88,000/mm3":
            "Thrombocytopenia below 100,000/mm3 reflects consumption and coagulopathy. It grades "
            "the severity of the response and says nothing about the trigger.",
    },
    "The elevated procalcitonin",
    "PROCALCITONIN is the one cause-specific marker in the sepsis laboratory panel: elevation "
    "points at a BACTERIAL etiology. Everything else on the list — white cell count, platelets, "
    "coagulation times, creatinine, lactate, bilirubin, C-reactive protein, oxygenation, glucose, "
    "urine output, cortisol — measures how badly the patient is doing, not what started it.\n\n"
    "The answer to the team's question is that negative cultures do not argue against bacterial "
    "sepsis at all. NO ORGANISM IS IDENTIFIED IN 30–50% OF CASES, and these were drawn from a "
    "patient with an obvious abdominal source. Sepsis is defined by the host response, not by a "
    "positive culture — which is exactly why no organism defines the syndrome and why no single "
    "criterion has adequate sensitivity or specificity.\n\n"
    "Her source fits the epidemiology. Sites of infection in order of frequency are respiratory > "
    "urinary > abdominal > head > other. An abdominal source points at Escherichia coli, "
    "Bacteroides fragilis, mixed anaerobes and Candida — and abdominal sources are a major reason "
    "20% of sepsis cases are polymicrobial.\n\n"
    "Note also the white cell count. It is 9,200/mm3 — squarely normal — with 16% bands. A normal "
    "count with more than 10% immature forms satisfies the criterion just as leukocytosis or "
    "leukopenia would. In sepsis a normal-looking number can still be an abnormal response.\n\n"
    "Educational objective: Procalcitonin is the only laboratory marker in the sepsis panel that "
    "indicates a bacterial etiology; C-reactive protein, lactate, platelet count and the "
    "differential grade severity rather than cause. Cultures are negative in 30–50% of sepsis "
    "cases, so a negative culture does not exclude the diagnosis.",
    "Most of her blood tests show how sick she is, not what is making her sick. One of them — "
    "procalcitonin — goes up specifically with bacteria. And the fact that nothing grew in the "
    "cultures means very little: in up to half of all sepsis cases, nothing ever grows.",
)

# ── 136. The trigger molecule depends on what kind of organism it is ──────────────────────────
q(
    "A 54-year-old woman with acute myeloid leukemia has been neutropenic for 18 days following "
    "induction chemotherapy and has had a tunnelled central venous catheter for 6 weeks. She "
    "develops fever to 39.2 C (102.6 F), hypotension and confusion. Two sets of blood cultures "
    "grow Candida albicans. Serum 1,3-beta-D-glucan is markedly elevated.\n\n"
    "Which of the following molecules is the principal trigger of the host response in this "
    "patient?",
    {
        "Beta-glucan of the fungal cell wall": "",
        "Host molecules released from damaged tissue":
            "Damage-associated molecular patterns are the mechanism by which VIRAL infection "
            "triggers sepsis — the virus damages host tissue and the debris drives the cytokine "
            "cascade. They are the exception in this list, and this is a fungal infection.",
        "Lipopolysaccharide of the outer membrane":
            "Lipopolysaccharide — endotoxin — is the trigger carried by gram-NEGATIVE bacteria, "
            "and the most prominent single trigger overall. Candida has no outer membrane and no "
            "lipopolysaccharide.",
        "Lipoteichoic acid of the cell wall":
            "Lipoteichoic acid and peptidoglycan are the gram-POSITIVE bacterial triggers. Fungal "
            "cell walls are built of polysaccharides instead.",
        "Toxic shock syndrome toxin 1, a superantigen":
            "Superantigens such as TSST-1 and streptococcal pyrogenic exotoxin are bacterial "
            "products that cross-link T-cell receptors to MHC class II non-specifically. They are "
            "not produced by Candida.",
    },
    "Beta-glucan of the fungal cell wall",
    "Microbial triggers of sepsis divide into PAMPs and DAMPs, and the pairings are worth having "
    "cold:\n\n"
    "• Gram-negative bacteria → LIPOPOLYSACCHARIDE (endotoxin) — PAMP, and the most prominent "
    "trigger overall\n"
    "• Gram-positive bacteria → LIPOTEICHOIC ACID and cell wall peptidoglycan — PAMP\n"
    "• Other bacterial products → superantigens (TSST-1, streptococcal pyrogenic exotoxin), plus "
    "bacterial DNA, RNA and surface glycoproteins — PAMP\n"
    "• FUNGI → BETA-GLUCANS, MANNANS and CHITIN — PAMP, and one rule covers all three: they are "
    "polysaccharides\n"
    "• Viruses → DAMPs, released from virus-damaged host tissue, not PAMPs. This is the exception "
    "in the list and therefore the likely question\n"
    "• Parasites → both\n\n"
    "PAMPs are pathogen-associated molecular patterns, carried by the organism itself. DAMPs are "
    "damage-associated molecular patterns, released by the host's own injured tissue.\n\n"
    "The stem gives the mechanism away twice over. The elevated serum 1,3-beta-D-glucan is a "
    "direct measurement of fungal cell wall material in the blood — the same assay used to support "
    "a diagnosis of Pneumocystis jirovecii pneumonia, whose cell wall is also rich in "
    "beta-1,3-D-glucan.\n\n"
    "Her risk profile is the textbook one for candidemia: prolonged neutropenia after "
    "chemotherapy and a long-dwelling central venous catheter. Fungal sepsis, overwhelmingly "
    "Candida (about 80%, with Aspergillus about 10%), is increasing in immunocompromised "
    "patients.\n\n"
    "Educational objective: Fungal sepsis is triggered by cell wall polysaccharides — beta-glucans, "
    "mannans and chitin. Lipopolysaccharide is the gram-negative trigger, lipoteichoic acid and "
    "peptidoglycan the gram-positive triggers, and viral sepsis is driven by host "
    "damage-associated molecular patterns rather than by pathogen patterns at all.",
    "Her immune system is reacting to the yeast's outer coat, which is built of sugar chains "
    "called beta-glucans. Different kinds of germ wave different flags: bacteria wave bits of "
    "their cell wall, yeasts wave sugars, and viruses do not wave anything — they just wreck cells "
    "and the wreckage sets off the alarm.",
)

# ── 137. A reactive screen with a negative differentiation assay ──────────────────────────────
q(
    "A 24-year-old man comes to the office due to 5 days of fever, sore throat, muscle aches and a "
    "rash. Eighteen days ago he had receptive anal intercourse with a new partner of unknown HIV "
    "status. Temperature is 38.6 C (101.5 F). Examination shows NON-exudative pharyngitis, a "
    "diffuse maculopapular rash involving the trunk and palms, generalized lymphadenopathy and mild "
    "splenomegaly. A heterophile antibody test is negative. An HIV-1/2 antigen/antibody "
    "immunoassay is REACTIVE. The reflex HIV-1/HIV-2 antibody differentiation immunoassay is "
    "NEGATIVE.\n\n"
    "Which of the following best explains these results?",
    {
        "p24 antigen was detected before antibody had developed": "",
        "Antibody is present but bound within immune complexes":
            "Immune complex sequestration is not a recognized cause of a negative differentiation "
            "assay in acute HIV infection, and it would not explain a reactive screening assay.",
        "He is infected with HIV-2 rather than with HIV-1":
            "The differentiation assay is what identifies HIV-2, and it would resolve to HIV-2 "
            "positive rather than reading negative.",
        "He is still within the eclipse period of infection":
            "The eclipse period is roughly day 0 to day 10, during which NO test detects HIV — "
            "including the screening assay that was reactive here. At 18 days he is past it.",
        "The screening immunoassay result is a false positive":
            "Possible in principle, but the false-positive rate for HIV testing with reflex is "
            "0.22%, and this patient has a textbook acute retroviral syndrome after a high-risk "
            "exposure. Do not reach for a laboratory error to explain a clinically expected "
            "result.",
    },
    "p24 antigen was detected before antibody had developed",
    "This is ACUTE HIV INFECTION (the acute retroviral syndrome), and the discordant results are "
    "the expected pattern rather than a laboratory problem.\n\n"
    "A fourth-generation antigen/antibody immunoassay detects TWO things: HIV antibodies and the "
    "HIV-1 p24 ANTIGEN. p24 is the capsid core protein, encoded by the GAG gene and cleaved from "
    "the p55 precursor by the VIRAL protease; it is the HIV protein most easily detected in serum. "
    "The marker sequence after infection is fixed: HIV RNA rises first, then p24 appears and peaks "
    "around day 30, and only then do antibodies begin to rise. At 18 days this man has p24 but no "
    "antibody — so the combination assay is reactive on antigen alone, and the antibody "
    "differentiation assay, which detects only antibody, is negative.\n\n"
    "The next step is the third tier of the Centers for Disease Control algorithm: an HIV-1 "
    "nucleic acid test. RNA detected with a negative differentiation assay establishes ACUTE HIV-1 "
    "infection. (The nucleic acid test is not used first because it costs roughly three times as "
    "much, is complex to run, and has real false-positive potential in low-risk people.)\n\n"
    "The clinical picture supports it. More than half of newly infected people develop a transient "
    "symptomatic illness, most often mistaken for mononucleosis — which the negative heterophile "
    "test argues against here. Fever occurs in about 75%, fatigue 68%, rash 48%, headache 45%, "
    "pharyngitis 40%, and the pharyngitis is NON-exudative, which is the discriminator from group "
    "A streptococcal infection. This is also the period of greatest transmission risk, because the "
    "viral load is enormous and the patient does not yet know their status.\n\n"
    "Educational objective: A reactive fourth-generation HIV antigen/antibody immunoassay with a "
    "negative HIV-1/HIV-2 antibody differentiation assay indicates acute HIV infection, in which "
    "p24 antigen — the gag-encoded capsid protein — is detectable weeks before antibody. Confirm "
    "with an HIV-1 nucleic acid test.",
    "The first test looks for two things: the virus's own protein and the body's antibodies. He "
    "has been infected recently enough that the protein is there but the antibodies have not been "
    "made yet — so the first test says yes and the antibody-only test says no. That mismatch is "
    "the fingerprint of a brand-new infection.",
    exim="fig_slide_hiv_markers",
    excap="Temporal appearance of the laboratory markers of HIV infection",
)

# ── 138. The booster is not an antiretroviral, and that is the whole problem ──────────────────
q(
    "A 41-year-old woman with HIV has had an undetectable viral load for 3 years on "
    "darunavir/cobicistat plus emtricitabine/tenofovir alafenamide. She comes to the office due to "
    "weight gain and fatigue for 4 months. She began an over-the-counter intranasal fluticasone "
    "spray for seasonal allergies 5 months ago and uses it daily. Blood pressure is 158/92 mm Hg. "
    "Examination shows facial rounding, supraclavicular fullness, wide violaceous abdominal striae "
    "and proximal muscle weakness.\n\n"
    "Laboratory studies show:\n"
    "Fasting glucose 168 mg/dL (N=70–99 mg/dL)\n"
    "Potassium 3.2 mEq/L (N=3.5–5.0 mEq/L)\n"
    "Morning cortisol 1.1 µg/dL (N=5–25 µg/dL)\n"
    "Corticotropin (ACTH) 4 pg/mL (N=10–60 pg/mL)\n\n"
    "Which of the following best explains her presentation?",
    {
        "Inhibition of cytochrome P450 3A4 by cobicistat": "",
        "Adrenal involvement by an opportunistic infection":
            "Adrenal infection would cause adrenal INSUFFICIENCY — hypotension, hyponatremia, "
            "hyperkalemia — with a HIGH corticotropin level. Her picture is the opposite in every "
            "respect.",
        "Ectopic corticotropin production by an occult tumour":
            "Ectopic corticotropin secretion does cause Cushing syndrome, but with a HIGH "
            "corticotropin level. Hers is suppressed, which points to an exogenous "
            "glucocorticoid.",
        "Fat redistribution caused by the protease inhibitor":
            "A genuinely close call: lipodystrophy affects about half of patients and produces "
            "abdominal lipohypertrophy, facial lipoatrophy and a dorsocervical fat pad. But it "
            "does not cause violaceous striae, proximal myopathy, hypokalemia or a suppressed "
            "cortisol and corticotropin.",
        "Immune reconstitution inflammatory syndrome from therapy":
            "Immune reconstitution syndrome occurs within the first few months of STARTING "
            "antiretroviral therapy — median 48 days — in a patient with a low pretreatment CD4 "
            "count, and it produces inflammatory disease, not Cushing syndrome. She has been "
            "suppressed for 3 years.",
    },
    "Inhibition of cytochrome P450 3A4 by cobicistat",
    "Iatrogenic Cushing syndrome with secondary adrenal suppression, caused by a drug interaction "
    "between a pharmacokinetic BOOSTER and an inhaled corticosteroid.\n\n"
    "Cobicistat and ritonavir are not antiretrovirals at all — a classic distractor in its own "
    "right. They are boosters, added to a regimen to inhibit CYP3A4 so that the antiretroviral is "
    "metabolized more slowly and its levels rise. That same inhibition applies to every other "
    "CYP3A4 substrate the patient takes. Intranasal and inhaled fluticasone undergo extensive "
    "first-pass CYP3A4 metabolism, and when that pathway is blocked the systemic concentration "
    "climbs to the point of producing exogenous glucocorticoid excess — hypertension, "
    "hyperglycemia, hypokalemia, striae, proximal myopathy and central fat redistribution — while "
    "suppressing the hypothalamic-pituitary-adrenal axis, hence the LOW cortisol with a LOW "
    "corticotropin. That combination is the giveaway: endogenous Cushing syndrome raises cortisol.\n\n"
    "The clinically important detail is that nasal steroids are sold OVER THE COUNTER, so no "
    "prescription record will reveal them and the patient will not think to mention them. Ask "
    "about non-prescription drugs, supplements and herbal preparations at every visit. The same "
    "CYP3A4 pathway governs several statins, which is why atorvastatin, low-dose rosuvastatin or "
    "pitavastatin are preferred in patients with HIV — a real concern given that people with HIV "
    "develop coronary disease roughly a decade early.\n\n"
    "Educational objective: Cobicistat and ritonavir are pharmacokinetic boosters that inhibit "
    "CYP3A4. Combined with an inhaled or intranasal corticosteroid, they raise systemic steroid "
    "levels enough to cause iatrogenic Cushing syndrome with adrenal suppression — low cortisol "
    "with low corticotropin.",
    "One of her HIV pills is not an HIV drug at all: its job is to block the liver enzyme that "
    "breaks drugs down, so the real HIV drug lasts longer. Unfortunately it blocks the breakdown "
    "of her over-the-counter nose spray too, so a steroid meant to stay in her nose has been "
    "flooding her whole body for months.",
)

# ── 139. Pneumocystis — why the antifungals fail and when to add steroids ─────────────────────
q(
    "A 36-year-old man is admitted due to 3 weeks of dry cough and progressive breathlessness on "
    "exertion. He was diagnosed with HIV 1 week ago and has not yet started antiretroviral therapy. "
    "His CD4 count is 28/mm3. Temperature is 38.6 C (101.5 F), respirations are 30/min and oxygen "
    "saturation is 86% on room air. Auscultation of the chest is unremarkable. Serum lactate "
    "dehydrogenase is 640 U/L (N=45–200 U/L) and the alveolar-arterial oxygen gradient is "
    "48 mm Hg. High-resolution chest CT is shown. Intravenous "
    "trimethoprim-sulfamethoxazole is begun.\n\n"
    "Which of the following should be added now?",
    {
        "Prednisone for 21 days": "",
        "Amphotericin B":
            "Amphotericin binds ERGOSTEROL in the fungal membrane. The Pneumocystis cell wall "
            "contains CHOLESTEROL rather than ergosterol, which is exactly why the standard "
            "antifungals do not work and why the treatment is an antifolate combination.",
        "Caspofungin monotherapy":
            "Echinocandins inhibit beta-glucan synthesis and have some theoretical appeal given "
            "this organism's beta-glucan-rich wall, but caspofungin is not an established "
            "treatment and is certainly not monotherapy for severe disease.",
        "Deferral of antiretroviral therapy":
            "The opposite is recommended: start antiretroviral therapy within 2 weeks of beginning "
            "treatment. Delaying to avoid immune reconstitution syndrome costs more than it saves.",
        "Inhaled pentamidine every month":
            "Inhaled pentamidine is a second-line PROPHYLACTIC agent for patients who cannot "
            "tolerate trimethoprim-sulfamethoxazole. It has no role in treating established severe "
            "pneumonia.",
    },
    "Prednisone for 21 days",
    "Pneumocystis jirovecii pneumonia, and the question is about the adjunct. Corticosteroids are "
    "indicated in MODERATE-TO-SEVERE disease because they reduce respiratory failure and "
    "mortality. The two triggers to know are a PaO2 below 70 mm Hg or an alveolar-arterial oxygen "
    "gradient of 35 mm Hg or more; his gradient is 48. Give prednisone for 21 days.\n\n"
    "The diagnosis is made on the pattern rather than on a culture, and empiric treatment is "
    "correct when suspicion is high. Here: CD4 below 200/mm3, the triad of fever, non-productive "
    "cough and progressive dyspnea, poor oxygenation with a widened A-a gradient, an elevated "
    "lactate dehydrogenase, and ground-glass opacities with peripheral sparing on CT. A normal "
    "chest examination is present in about half of patients and a chest radiograph can be normal "
    "in up to 25% — but a normal high-resolution CT argues strongly against the diagnosis.\n\n"
    "Pneumocystis is an ATYPICAL fungus, and each of its oddities has a consequence: it does not "
    "grow in fungal culture; its cell wall contains CHOLESTEROL rather than ergosterol, so "
    "ergosterol-targeting antifungals fail and trimethoprim-sulfamethoxazole is the drug; and its "
    "wall is rich in beta-1,3-D-glucan, which is the basis of the serum beta-D-glucan assay.\n\n"
    "Two timing points complete the picture. Expect the patient to WORSEN for the first 2–3 days "
    "of treatment, because killing the organism releases inflammatory material — that is not "
    "immune reconstitution syndrome, it is far too early. And start antiretroviral therapy within "
    "2 weeks; the risk of immune reconstitution is real but is managed by anticipating it, not by "
    "delaying treatment.\n\n"
    "Educational objective: Add corticosteroids to trimethoprim-sulfamethoxazole in Pneumocystis "
    "jirovecii pneumonia when the PaO2 is below 70 mm Hg or the alveolar-arterial gradient is "
    "35 mm Hg or greater. Ergosterol-targeting antifungals are ineffective because the organism's "
    "cell wall contains cholesterol instead.",
    "His lungs are full of an unusual fungus that ordinary antifungal drugs cannot touch, because "
    "its outer coat is built differently. The antibiotic he is on kills it — but as it dies it "
    "makes his lungs even angrier, so a steroid is added to keep the inflammation from stopping "
    "his breathing.",
    image="fig_pjp_ct",
    imcap="High-resolution chest CT on admission",
)

# ── 140. The retina at a CD4 of 22 ────────────────────────────────────────────────────────────
q(
    "A 44-year-old man with AIDS comes to the emergency department due to 6 days of floaters and "
    "painless loss of the temporal field of the right eye. He stopped antiretroviral therapy "
    "18 months ago. His CD4 count is 22/mm3 and his HIV RNA is 340,000 copies/mL. He is afebrile "
    "and has no headache, neck stiffness or focal weakness. Dilated funduscopic examination of the "
    "right eye is shown.\n\n"
    "Which of the following organisms is most likely responsible?",
    {
        "Cytomegalovirus": "",
        "Cryptococcus neoformans":
            "Cryptococcus is a threat at the same CD4 threshold, but it causes meningoencephalitis "
            "with headache and altered mentation, neither of which is present.",
        "JC virus":
            "JC virus causes progressive multifocal leukoencephalopathy, a demyelinating disease "
            "producing focal neurologic deficits and cognitive decline — not a retinal lesion.",
        "Mycobacterium avium complex":
            "Disseminated Mycobacterium avium complex also appears below a CD4 of 50, but with "
            "night sweats, weight loss, diarrhea and malaise rather than isolated visual loss.",
        "Toxoplasma gondii":
            "Toxoplasma can involve the retina, but in advanced HIV it characteristically presents "
            "as encephalitis with ring-enhancing lesions on brain imaging at a CD4 below 100, and "
            "the retinal lesion is typically a focal necrotizing lesion without this degree of "
            "hemorrhage.",
    },
    "Cytomegalovirus",
    "Cytomegalovirus retinitis. The funduscopic appearance is characteristic — confluent areas of "
    "retinal whitening (necrosis) following the vascular arcades with scattered intraretinal "
    "hemorrhage, sometimes described as a 'pizza pie' or 'cheese and ketchup' fundus — and the CD4 "
    "count places it exactly.\n\n"
    "Opportunistic infection risk in HIV is organized by CD4 threshold, and knowing the tiers "
    "converts a long differential into a short one:\n\n"
    "• > 500/mm3 — community-acquired organisms; herpes simplex and zoster reactivation\n"
    "• 200–500/mm3 — tuberculosis (hemoptysis, night sweats, weight loss)\n"
    "• < 200/mm3 — Pneumocystis jirovecii, Cryptosporidium, Candida, fungal pneumonia\n"
    "• < 100/mm3 — toxoplasmosis (ring-enhancing lesions on brain CT), Candida/HSV/CMV esophagitis\n"
    "• < 50/mm3 — CYTOMEGALOVIRUS (retinitis, esophagitis, enteritis, encephalitis), Cryptococcus, "
    "Mycobacterium avium complex, primary CNS lymphoma\n\n"
    "Two related thresholds are worth keeping apart, because confusing them is a common error. A "
    "CD4 count below 200/mm3 (or below 14%) DEFINES AIDS — CDC stage 3 — as does any "
    "AIDS-defining opportunistic infection at any CD4 count. A CD4 below 50/mm3 is where "
    "opportunistic infection risk is GREATEST. And when the complete blood count comes back before "
    "HIV-specific testing, an absolute lymphocyte count below 1,000/mm3 predicts a CD4 below "
    "200/mm3, which tells you immediately to start thinking about prophylaxis.\n\n"
    "Educational objective: Cytomegalovirus retinitis occurs at a CD4 count below 50/mm3 and "
    "presents with painless visual loss and floaters, with retinal necrosis and hemorrhage on "
    "funduscopy. Organizing opportunistic infections by CD4 threshold — 200, 100 and 50 — narrows "
    "the differential before any test is sent.",
    "His immune system has fallen so low that a virus most people carry harmlessly for life has "
    "started eating his retina. The pattern of white dead retina and streaks of blood is "
    "distinctive, and the CD4 count of 22 tells you which infections are even possible.",
    image="fig_hx_cmv_retinitis",
    imcap="Dilated funduscopic examination, right eye",
)
