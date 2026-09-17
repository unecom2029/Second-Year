# Hardest Exam — batch H5 of 5 (questions 81–100)
# Sections §43–§46 (antineoplastic pharmacology), §48 and §56–§57 (lymphatics, post-traumatic edema,
# lymphatic spread), §55 (splenic injury), §23 (accuracy vs precision) and §54 (prescribing).

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


# ── 81. Why combination chemotherapy (§43) ─────────────────────────────────────
q(
    "A 61-year-old man with newly diagnosed diffuse large B-cell lymphoma is to begin treatment. The "
    "planned regimen contains rituximab, cyclophosphamide, doxorubicin, vincristine and prednisone. "
    "His son asks why five drugs are needed rather than a higher dose of the single most effective "
    "one. Which of the following best explains the use of several agents together?",
    {
        "Agents with different mechanisms allow full dosing of each": "",
        "Combining agents allows each to be given at a lower, safer dose":
            "The aim is the opposite — non-overlapping toxicity is what permits each drug to be given "
            "at its OWN full dose. Dose reduction is what you are forced into when two agents share a "
            "toxicity.",
        "Each agent targets a different phase of the cell cycle":
            "Phase coverage is a real consideration, but two of these agents are cell cycle-NONspecific "
            "and one is an antibody. It is not what the combination principle rests on.",
        "Multiple agents shorten the total duration of therapy":
            "Cytotoxic therapy kills a constant FRACTION of cells per dose, so repeated cycles are "
            "mathematically necessary regardless of how many drugs are combined.",
        "Using several agents avoids the need for growth factor support":
            "Combining myelosuppressive agents makes growth factor support more likely to be needed, "
            "not less.",
    },
    "Agents with different mechanisms allow full dosing of each",
    "The principles that make a combination regimen better than a single agent:\n\n"
    "• A LARGER SPECTRUM OF ACTIVITY — a heterogeneous tumour contains subclones with different "
    "vulnerabilities, and more mechanisms hit more of them\n"
    "• DIFFERING MECHANISMS and DIFFERING TOXICITIES — different mechanisms give additive kill, and "
    "non-overlapping toxicity means each drug can be given at full dose. If two agents share an "
    "adverse effect you must dose-reduce, which is exactly what you are trying to avoid\n"
    "• A LOWER RATE OF RESISTANCE — the cell must acquire several independent resistance mechanisms "
    "at once rather than one\n\n"
    "R-CHOP is the worked example, and every letter is a different mechanism with a different "
    "toxicity: Rituximab (anti-CD20 antibody), Cyclophosphamide (alkylator — haemorrhagic cystitis), "
    "Hydroxydaunorubicin/doxorubicin (anthracycline — cardiomyopathy), Oncovin/vincristine (vinca — "
    "neurotoxicity), Prednisone (corticosteroid).\n\n"
    "Why repeated cycles are unavoidable: cytotoxic agents follow first-order kinetics, killing a "
    "constant FRACTION of cells per dose — the log-kill hypothesis. Taking a burden from 10⁸ to 10⁵ "
    "is a 3-log kill, and no single dose can ever sterilize a tumour because a fixed fraction always "
    "survives. Note also the 10⁹ cell (about 1 gram) threshold of clinical detectability: everything "
    "below it is the subclinical disease that adjuvant chemotherapy exists to treat.\n\n"
    "Educational objective: Combination chemotherapy uses agents with different mechanisms of action "
    "and non-overlapping toxicities so that each can be given at full dose, which broadens the "
    "spectrum of activity against a heterogeneous tumour and reduces the emergence of resistance.",
    "Five different drugs attack the cancer in five different ways and damage five different parts of "
    "the body. Because they do not pile up on the same organ, each can be given at its full strength.",
    exim="fig_chemo_man",
    excap="The Chemo Man mnemonic — each agent mapped onto the organ it damages, which is how "
          "non-overlapping toxicity is chosen in practice.",
)

# ── 82. Multi-drug resistance and P-glycoprotein (§43) ─────────────────────────
q(
    "A 58-year-old woman with metastatic breast cancer has a partial response to doxorubicin, then "
    "progresses after 7 months. She is switched to a regimen containing vinblastine and etoposide, "
    "and her disease progresses again within 8 weeks despite never having received either drug. The "
    "three agents are structurally unrelated and act by different mechanisms. Which of the following "
    "best explains the pattern of resistance in this patient?",
    {
        "Amplification of the target enzyme dihydrofolate reductase":
            "Target enzyme amplification is the resistance mechanism for METHOTREXATE specifically, "
            "and would not confer resistance to drugs acting on topoisomerase or microtubules.",
        "Increased efflux of drugs by a membrane transporter": "",
        "Increased repair of DNA adducts and cross-links":
            "Enhanced DNA repair confers resistance to alkylating agents and cisplatin — she received "
            "neither, and it would not affect a vinca alkaloid.",
        "Loss of the enzyme required to activate a prodrug":
            "This is how resistance develops to the purine and pyrimidine antimetabolites "
            "(mercaptopurine, cytarabine, fluorouracil), which must be converted to an active form. "
            "None of her drugs is a prodrug of that kind.",
        "Location of tumour within a pharmacologic sanctuary":
            "A sanctuary site — classically the central nervous system or the testis — shelters "
            "tumour behind a barrier the drug cannot cross. That would not produce systemic "
            "progression across three drug classes.",
    },
    "Increased efflux of drugs by a membrane transporter",
    "Multi-drug resistance from increased expression of MDR1, which encodes P-GLYCOPROTEIN — an "
    "ATP-dependent efflux pump in the cell membrane (the P stands for 'permeability').\n\n"
    "Because the pump recognizes a broad range of hydrophobic substrates, resistance selected by one "
    "drug extends to structurally unrelated drugs that happen to use the same exit: vincristine, "
    "vinblastine, doxorubicin, bleomycin and etoposide all leave through that door. This is ACQUIRED "
    "resistance (it developed after exposure) that is also CROSS-resistance.\n\n"
    "The full list of resistance mechanisms, each tied to its drugs:\n"
    "• Increased DNA repair — alkylating agents, cisplatin\n"
    "• Trapping agents (thiol-rich molecules that bind the drug) — bleomycin, cisplatin, "
    "anthracyclines\n"
    "• Altered or amplified target enzyme — methotrexate and dihydrofolate reductase\n"
    "• Decreased activation of a prodrug, or inactivation of the active drug — purine and pyrimidine "
    "antimetabolites\n"
    "• Decreased drug accumulation by efflux — many agents, and the answer here\n"
    "• Pharmacologic sanctuary — the central nervous system or testis\n\n"
    "The same transporter explains a long list of drug interactions elsewhere: verapamil, "
    "amiodarone, clarithromycin, ketoconazole and rifampin are all described as P-glycoprotein "
    "inhibitors or inducers, which is why they alter direct oral anticoagulant levels.\n\n"
    "Educational objective: Overexpression of MDR1 produces the P-glycoprotein efflux pump, which "
    "exports a broad range of structurally unrelated hydrophobic drugs — anthracyclines, vinca "
    "alkaloids, etoposide, bleomycin — so resistance to one agent confers cross-resistance to the "
    "others.",
    "The cancer cells have installed a pump in their outer wall that throws out anything that looks "
    "like a toxin. Because the pump is not fussy, drugs the cancer has never even met get thrown out "
    "too.",
    exim="fig_chemo_pgp",
    excap="The P-glycoprotein transporter spanning the cell membrane, using adenosine triphosphate to "
          "export a broad range of hydrophobic drugs.",
)

# ── 83. Bleomycin pulmonary toxicity (§44) ─────────────────────────────────────
q(
    "A 24-year-old man with Hodgkin lymphoma has completed four cycles of doxorubicin, bleomycin, "
    "vinblastine and dacarbazine. He comes to the office due to 5 weeks of dry cough and "
    "breathlessness climbing one flight of stairs. Temperature is 36.9 C (98.4 F). Oxygen saturation "
    "is 94% at rest and 87% after walking. Fine inspiratory crackles are heard at both lung bases. "
    "Chest radiography shows bilateral reticular opacities at the lung bases. His hemoglobin is 12.6 "
    "g/dL, leukocyte count is 5,800/mm3 and platelet count is 214,000/mm3. Which agent is most "
    "likely responsible for his symptoms?",
    {
        "Bleomycin": "",
        "Dacarbazine":
            "A triazene alkylating agent whose problems are nausea, vomiting and myelosuppression. "
            "(Its relative procarbazine is a monoamine oxidase inhibitor with the tyramine "
            "interaction.)",
        "Doxorubicin":
            "The anthracycline's signature toxicity is a dose-cumulative CARDIOMYOPATHY, which would "
            "present with orthopnea, edema and a raised jugular venous pressure rather than a dry "
            "cough with reticular opacities. It is also strongly myelosuppressive.",
        "Prednisone":
            "Corticosteroids cause hyperglycemia, immunosuppression, osteoporosis and mood change. "
            "This regimen does not contain one.",
        "Vinblastine":
            "Within the vinca class, vinblastine's dose-limiting toxicity is MYELOSUPPRESSION — and "
            "his counts are normal. Vincristine is the one whose limit is neurotoxicity.",
    },
    "Bleomycin",
    "Bleomycin-induced pulmonary fibrosis — 'bleomycin lung' — and the normal blood counts are the "
    "clue that makes the answer unambiguous.\n\n"
    "Bleomycin is one of only two traditional cytotoxic agents that essentially SPARE the marrow (the "
    "other is vincristine, and methotrexate given with leucovorin behaves similarly). So in a "
    "patient with normal counts and a new restrictive lung picture, the agent whose dose-limiting "
    "toxicity is not marrow is the one to suspect.\n\n"
    "Mechanism: the bleomycin-iron complex generates free oxygen radicals that break DNA strands. The "
    "lung is uniquely vulnerable because it lacks bleomycin hydrolase, the enzyme that inactivates "
    "the drug in other tissues. Monitoring is with pulmonary function testing, and the fibrosis may "
    "be irreversible.\n\n"
    "The six dose-limiting toxicity pairings to know as a block:\n"
    "• Haemorrhagic cystitis — cyclophosphamide, ifosfamide (prevent with mesna)\n"
    "• Pulmonary fibrosis — bleomycin\n"
    "• Ototoxicity, nephrotoxicity and severe emesis — cisplatin\n"
    "• Cardiotoxicity — doxorubicin, daunorubicin, and trastuzumab\n"
    "• Peripheral neuropathy — oxaliplatin, vincristine, taxanes\n"
    "• Potentially fatal diarrhoea — irinotecan\n\n"
    "Educational objective: Bleomycin causes pulmonary fibrosis because the lung lacks the "
    "inactivating enzyme bleomycin hydrolase, and it is one of the few cytotoxic drugs that spares "
    "the bone marrow — so a new restrictive lung picture with normal blood counts points to it.",
    "Most chemo drugs hit the bone marrow hardest, but this one hits the lungs, because the lungs "
    "lack the enzyme that disarms it elsewhere. His blood counts being normal is the tip-off.",
    exim="fig_chemo_man",
    excap="The Chemo Man mnemonic — each drug mapped onto the organ it damages, with bleomycin and "
          "busulfan on the pulmonary arm.",
)

# ── 84. Haemorrhagic cystitis and mesna (§43, §44) ─────────────────────────────
q(
    "A 52-year-old woman receives high-dose cyclophosphamide as part of conditioning before an "
    "autologous stem cell transplant. Thirty-six hours later she develops suprapubic pain, urinary "
    "frequency and gross hematuria with clots. She is afebrile. Urine culture shows no growth, urine "
    "cytology shows no malignant cells, and her platelet count is 96,000/mm3 with normal coagulation "
    "studies. Cystoscopy shows diffuse mucosal edema and punctate hemorrhage without a discrete "
    "lesion. Which of the following would most likely have prevented this complication?",
    {
        "Amifostine":
            "A cytoprotective agent used chiefly to reduce cisplatin nephrotoxicity and radiation "
            "xerostomia, not the bladder toxicity of the oxazaphosphorines.",
        "Dexrazoxane":
            "Dexrazoxane chelates intracellular iron so it cannot generate free radicals, and it "
            "protects the HEART from anthracyclines.",
        "Leucovorin":
            "Folinic acid rescues normal cells from methotrexate by supplying reduced folate beyond "
            "the blocked enzyme. Note the trap — with 5-fluorouracil the same molecule is an "
            "ENHANCER, not a rescue.",
        "Mesna": "",
        "Rasburicase":
            "Rasburicase degrades uric acid in tumour lysis syndrome. This patient's problem is local "
            "bladder toxicity, not a metabolic emergency.",
    },
    "Mesna",
    "Haemorrhagic cystitis from cyclophosphamide, and it is caused by a METABOLITE rather than by the "
    "parent drug. Cyclophosphamide and ifosfamide are metabolized to ACROLEIN, which is excreted in "
    "the urine and concentrates in the bladder, where it is directly toxic to the urothelium — hence "
    "diffuse mucosal edema and punctate hemorrhage rather than a discrete lesion.\n\n"
    "Mesna (mercaptoethanesulfonate) binds acrolein in the urine and neutralizes it before it can "
    "injure the mucosa. Given with aggressive hydration and frequent voiding, it is the standard "
    "prophylaxis whenever high-dose cyclophosphamide or any ifosfamide is used.\n\n"
    "The three rescue agents are worth learning as a set, because each is an antidote given ON "
    "PURPOSE alongside the drug:\n"
    "• LEUCOVORIN rescues from methotrexate — it supplies reduced folate downstream of the blocked "
    "dihydrofolate reductase. But with 5-fluorouracil it ENHANCES activity instead, so 'leucovorin = "
    "antidote' is not safe to assume\n"
    "• MESNA rescues from cyclophosphamide and ifosfamide by binding acrolein in the bladder\n"
    "• DEXRAZOXANE rescues the heart from anthracyclines by chelating intracellular iron\n\n"
    "Note also the alkylator class signature more broadly: myelosuppression with mucositis, "
    "neurotoxicity, and SECONDARY MALIGNANCIES — these drugs are mutagens, which is the mechanism "
    "behind therapy-related leukemia years later.\n\n"
    "Educational objective: Cyclophosphamide and ifosfamide are metabolized to acrolein, which "
    "concentrates in the bladder and causes haemorrhagic cystitis; mesna binds acrolein in the urine "
    "and, with hydration, prevents it.",
    "The chemotherapy breaks down into a chemical that is fine in the blood but burns the lining of "
    "the bladder where it collects. Mesna is given alongside to mop that chemical up in the urine.",
)

# ── 85. The vinca split (§44) ─────────────────────────────────────────────────
q(
    "A 46-year-old man receiving vincristine as part of treatment for acute lymphoblastic leukemia "
    "reports 3 weeks of numbness and tingling in his fingertips and toes, and he has begun tripping "
    "on stairs. Examination shows absent ankle reflexes, reduced vibration sense to the mid-shin "
    "bilaterally, and mild weakness of ankle dorsiflexion. His hemoglobin is 11.9 g/dL, leukocyte "
    "count is 6,200/mm3 and platelet count is 226,000/mm3. Which of the following best characterizes "
    "this drug's dose-limiting toxicity relative to other agents in its class?",
    {
        "It causes cardiomyopathy, unlike other vinca alkaloids":
            "Cardiomyopathy belongs to the anthracyclines and to trastuzumab. No vinca alkaloid is "
            "cardiotoxic in this way.",
        "It causes neurotoxicity, whereas vinblastine causes myelosuppression": "",
        "It causes pulmonary fibrosis, whereas vinblastine causes neuropathy":
            "Pulmonary fibrosis is bleomycin's toxicity and belongs to a different class entirely.",
        "It shares dose-limiting myelosuppression with all vinca alkaloids":
            "This is the trap. Vinblastine and vinorelbine are indeed dose-limited by myelosuppression "
            "— but vincristine is not, and his counts are normal.",
        "It stabilizes microtubules, unlike other vinca alkaloids":
            "Stabilizing microtubules and preventing disassembly is what the TAXANES do. All vinca "
            "alkaloids block tubulin assembly so the spindle dissolves.",
    },
    "It causes neurotoxicity, whereas vinblastine causes myelosuppression",
    "Vincristine neurotoxicity — a length-dependent sensorimotor peripheral neuropathy, presenting "
    "with distal paresthesias, loss of ankle reflexes and eventually foot drop.\n\n"
    "The split within one class is a classic distractor: vinCRIStine is dose-limited by NEUROtoxicity, "
    "while vinBLAStine and vinorelbine are dose-limited by MYELOsuppression. His normal counts with a "
    "florid neuropathy make the point.\n\n"
    "All the vincas share the same mechanism — they BLOCK assembly of tubulin dimers, so the mitotic "
    "spindle dissolves and the cell arrests in M phase. The taxanes (paclitaxel, docetaxel) do the "
    "opposite at the same target: they PROMOTE microtubule formation and prevent disassembly, "
    "freezing the cell in metaphase. Both end in mitotic arrest, and both cause peripheral "
    "neuropathy, because axonal transport depends on intact microtubules.\n\n"
    "One absolute safety rule belongs with this drug: vincristine is NEVER given intrathecally. "
    "Intrathecal administration causes a uniformly fatal ascending myeloencephalopathy, which is why "
    "most institutions dispense it in a minibag rather than a syringe — a syringe can be mistaken for "
    "an intrathecal dose.\n\n"
    "Educational objective: Vincristine's dose-limiting toxicity is peripheral neurotoxicity while "
    "vinblastine's and vinorelbine's is myelosuppression, even though all block tubulin assembly. "
    "Vincristine is fatal if given intrathecally and must never be administered by that route.",
    "Two drugs from the same family cause trouble in different places: one damages nerves, the other "
    "knocks down blood counts. His nerves are affected and his blood counts are fine, which tells you "
    "which one he is on.",
    exim="fig_chemo_microtubule",
    excap="Anti-microtubule agents — the vincas block tubulin assembly, the taxanes prevent "
          "disassembly, and both arrest mitosis.",
)

# ── 86. Why signal transduction inhibitors are small molecules (§45) ───────────
q(
    "An investigator is developing agents against several oncogenic targets. Two candidates are "
    "monoclonal antibodies of about 145,000 daltons, and two are small molecules of a few hundred "
    "daltons. The proposed targets are the extracellular domain of the epidermal growth factor "
    "receptor, the extracellular domain of HER2, the BCR-ABL1 kinase, and mechanistic target of "
    "rapamycin (mTOR). The investigator finds that antibody candidates directed at the last two "
    "targets have no activity in cell-based assays despite high binding affinity for purified "
    "protein. Which of the following best explains this finding?",
    {
        "Antibodies are degraded by intracellular proteases before reaching the target":
            "Degradation is not the limiting step; the antibody never enters the cytoplasm in the "
            "first place.",
        "Antibodies cannot cross the plasma membrane to reach intracellular targets": "",
        "Antibodies of the IgG4 subclass cannot activate complement":
            "True, and it is exactly why IgG4 is chosen for checkpoint inhibitors — you do not want "
            "to lyse the T cell you are trying to activate. It has nothing to do with reaching an "
            "intracellular kinase.",
        "Small molecules bind targets with higher affinity than antibodies":
            "Antibodies typically bind with very high affinity — the stem states affinity is high. "
            "Access, not affinity, is the problem.",
        "Small molecules are actively imported by membrane transporters":
            "Most cross by passive diffusion because they are small and lipophilic; active import is "
            "not the general explanation.",
    },
    "Antibodies cannot cross the plasma membrane to reach intracellular targets",
    "Size decides where a drug can act, and that single fact organizes the whole of targeted "
    "therapy.\n\n"
    "• An ANTIBODY is roughly 145,000 daltons and cannot cross the plasma membrane, so it can only "
    "engage the EXTRACELLULAR domain of a transmembrane receptor — EGFR (cetuximab, panitumumab), "
    "HER2 (trastuzumab, pertuzumab), VEGF (bevacizumab), CD20 (rituximab)\n"
    "• A SMALL MOLECULE of a few hundred daltons crosses the membrane and can inhibit an "
    "INTRACELLULAR kinase\n\n"
    "The consequence: every signal transduction inhibitor is a small molecule, because those targets "
    "— BCR-ABL, RAF, MEK, mTOR, BTK, PARP, PI3K, CDK4/6 — all sit inside the cell. There are no "
    "monoclonal antibodies in that group.\n\n"
    "The format also predicts the toxicity family, which is how most 'which adverse effect' questions "
    "are answered:\n"
    "• SMALL MOLECULE → pharmacokinetic problems (CYP3A4 interactions, food effects, most taken on an "
    "empty stomach) plus off-target kinase effects — QT prolongation, diarrhoea and raised liver "
    "enzymes are class effects\n"
    "• ANTIBODY → infusion reactions, and on-target toxicity in whatever normal tissue expresses the "
    "antigen — the acneiform rash of EGFR blockade is the cleanest example, since EGFR is highly "
    "expressed in normal skin\n\n"
    "Educational objective: Monoclonal antibodies are too large to cross the plasma membrane and can "
    "only target extracellular receptor domains, so all signal transduction inhibitors — BCR-ABL, "
    "RAF, MEK, mTOR, BTK, PARP, PI3K, CDK4/6 — are small molecules.",
    "Antibodies are huge and can only grab handles on the outside of a cell. If the target is inside, "
    "you need a tiny molecule that can slip through the wall.",
)

# ── 87. Trastuzumab cardiotoxicity (§45) ──────────────────────────────────────
q(
    "A 54-year-old woman with HER2-positive breast cancer has completed four cycles of doxorubicin "
    "and cyclophosphamide and is now receiving paclitaxel with trastuzumab. She comes to the office "
    "due to 3 weeks of exertional breathlessness and ankle swelling, and she now sleeps on two "
    "pillows. Blood pressure is 118/74 mm Hg and pulse is 96/min. Jugular venous pressure is "
    "elevated, and there are bibasal crackles and pitting edema to both mid-shins. Echocardiography "
    "shows a left ventricular ejection fraction of 38%, reduced from 62% before treatment. Which "
    "property of trastuzumab best explains this complication?",
    {
        "Generation of free radicals by an iron-drug complex":
            "This is how bleomycin injures the lung, and a related free-radical mechanism underlies "
            "anthracycline cardiotoxicity — which is why dexrazoxane chelates iron. It is not how a "
            "HER2 antibody damages the heart.",
        "Its target is also expressed on cardiomyocytes": "",
        "It carries an anti-microtubule payload to cardiac tissue":
            "Trastuzumab is a naked antibody. Ado-trastuzumab emtansine is the conjugate carrying an "
            "anti-microtubule payload, and its signature toxicities are thrombocytopenia, "
            "transaminitis and neuropathy.",
        "It inhibits vascular endothelial growth factor signalling":
            "VEGF blockade causes hypertension, impaired wound healing, thrombosis, bleeding and "
            "gastrointestinal perforation — a different toxicity profile altogether.",
        "It releases interleukin-6 from activated T cells":
            "Interleukin-6-driven cytokine release syndrome is the toxicity of T-cell engagers and "
            "CAR-T therapy, presenting with fever, hypotension and hypoxia within hours of a dose.",
    },
    "Its target is also expressed on cardiomyocytes",
    "Trastuzumab-associated cardiomyopathy — and it is the cleanest illustration of the governing "
    "principle of targeted therapy: TOXICITY FOLLOWS THE TARGET'S NORMAL TISSUE DISTRIBUTION, not the "
    "mitotic rate.\n\n"
    "HER2 is expressed on cardiomyocytes, where its signalling supports cell survival and the "
    "response to stress. Blocking it impairs that protective pathway and produces a decline in left "
    "ventricular ejection fraction with clinical heart failure — which is why trastuzumab sits on the "
    "cardiotoxicity arm of Chemo Man alongside doxorubicin and daunorubicin.\n\n"
    "Two clinically important contrasts with anthracycline cardiotoxicity: trastuzumab injury is "
    "usually not dose-cumulative and is often reversible on stopping the drug, whereas anthracycline "
    "cardiomyopathy is cumulative across a lifetime and largely irreversible — which is precisely why "
    "sequential exposure, as here, raises the risk and why serial echocardiography is standard during "
    "HER2-directed therapy.\n\n"
    "The same principle predicts the rest of the class: EGFR inhibitors cause an acneiform rash "
    "because EGFR is expressed in normal skin; VEGF inhibitors cause hypertension, bleeding and "
    "impaired wound healing because VEGF maintains vascular homeostasis; PI3K inhibitors cause "
    "autoimmunity and opportunistic infection because PI3K-delta is a lymphocyte signalling node; and "
    "mTOR inhibitors cause metabolic dysregulation because mTOR is the cell's nutrient sensor.\n\n"
    "Educational objective: Targeted therapy toxicity follows the normal tissue distribution of the "
    "target — trastuzumab causes heart failure because HER2 is expressed on cardiomyocytes, which is "
    "why left ventricular function is monitored during HER2-directed treatment.",
    "The drug blocks a receptor that breast cancer cells depend on — but heart muscle cells use the "
    "same receptor to stay healthy. Block it everywhere and the heart weakens.",
)

# ── 88. Immune-related colitis from a checkpoint inhibitor (§45) ───────────────
q(
    "A 63-year-old man with metastatic melanoma is receiving nivolumab. Six weeks after the first "
    "dose he comes to the emergency department due to 8 days of watery diarrhea, now 9 times daily "
    "with blood and mucus, and crampy abdominal pain. Temperature is 37.4 C (99.3 F). Stool studies "
    "are negative for Clostridioides difficile toxin, ova and parasites, and bacterial pathogens. "
    "Flexible sigmoidoscopy shows diffuse erythema, loss of vascular pattern and shallow "
    "ulcerations, and biopsy shows a lymphocytic infiltrate with crypt abscesses and apoptotic "
    "bodies. Which of the following is the most appropriate treatment?",
    {
        "High-dose corticosteroids": "",
        "Loperamide titrated to stool frequency":
            "Antimotility agents treat secretory or chemotherapy-associated diarrhea — irinotecan's, "
            "for example. Using them alone here treats a symptom and leaves an autoimmune colitis to "
            "progress toward perforation.",
        "Octreotide":
            "Used for refractory secretory diarrhea and neuroendocrine tumour syndromes. It does not "
            "address immune-mediated inflammation.",
        "Oral vancomycin with metronidazole":
            "The treatment for Clostridioides difficile colitis, which the stool toxin assay has "
            "excluded.",
        "Tocilizumab":
            "The anti-interleukin-6 receptor antibody is the specific treatment for CYTOKINE RELEASE "
            "SYNDROME after a T-cell engager or CAR-T therapy — fever, hypotension and hypoxia hours "
            "after a dose, not colitis weeks later.",
    },
    "High-dose corticosteroids",
    "Immune-mediated colitis, an immune-related adverse event of checkpoint blockade.\n\n"
    "The mechanism makes the treatment obvious once stated: checkpoint inhibitors work by REMOVING "
    "THE BRAKES that maintain self-tolerance. CTLA-4 downregulates T-cell activation and PD-1 dampens "
    "T cells in peripheral tissues; blocking either unleashes T cells against the tumour — and, "
    "predictably, against normal tissue. So the treatment for a serious immune-related adverse event "
    "is CORTICOSTEROIDS: you put a brake back on.\n\n"
    "Immune-related adverse events can affect essentially any organ, and the useful shorthand is 'any "
    "organ ending in -itis': colitis, dermatitis, pneumonitis, hepatitis, arthritis and myositis, "
    "thyroiditis, hypophysitis, adrenal insufficiency and new diabetes (endocrinopathies are often "
    "PERMANENT even when the inflammation settles), uveitis, and neurologic syndromes.\n\n"
    "Their behaviour differs sharply from the toxicity of T-cell engagers, which is a useful contrast: "
    "immune-related adverse events are largely unrelated to dose intensity, highly variable in "
    "profile, can affect any organ, occur at very variable times — even after therapy ends — and are "
    "largely unpredictable. T-cell engager toxicity is dose-related, stereotyped (cytokine release "
    "syndrome and neurologic events), occurs during step-up dosing, and is fairly predictable.\n\n"
    "Educational objective: Checkpoint inhibitors cause immune-related adverse events by removing "
    "the inhibitory signals that maintain self-tolerance, producing inflammation of virtually any "
    "organ; serious events such as immune-mediated colitis are treated with corticosteroids rather "
    "than with antimotility agents.",
    "The cancer drug works by taking the brakes off his immune system, and now that immune system is "
    "attacking his bowel. The fix is to put a brake back on with steroids.",
    exim="fig_chemo_checkpoint",
    excap="Mechanism of immune checkpoint inhibition — an antigen-presenting cell engaging a T cell, "
          "with the inhibitory checkpoints that the antibodies block.",
)

# ── 89. Cytokine release syndrome versus ICANS (§45) ───────────────────────────
q(
    "A 58-year-old woman with relapsed diffuse large B-cell lymphoma receives CD19-directed "
    "chimeric antigen receptor T-cell therapy. Eight hours after the infusion she develops a "
    "temperature of 39.5 C (103.1 F), blood pressure of 80/48 mm Hg that does not respond to 2 L of "
    "crystalloid, and an oxygen saturation of 88% on room air requiring high-flow oxygen. She is "
    "alert and fully oriented, with no focal neurologic findings. Blood cultures are drawn and "
    "broad-spectrum antibiotics started. Which of the following is the most appropriate specific "
    "treatment?",
    {
        "Dexamethasone alone":
            "Dexamethasone is chosen for ICANS specifically because it penetrates the central nervous "
            "system — and that syndrome appears 3–9 days after infusion with confusion, dysphasia or "
            "seizure. She is alert on day one.",
        "Diphenhydramine and acetaminophen":
            "Premedication manages a simple infusion reaction, which occurs within the first 6 hours "
            "and is generally AFEBRILE. Hers began at 8 hours with fever, hypotension and hypoxia.",
        "Levetiracetam":
            "A non-sedating anticonvulsant is part of ICANS management, where sedating agents would "
            "obscure the neurologic assessment. There is no seizure here.",
        "Intravenous immunoglobulin":
            "Replaces antibody in hypogammaglobulinemia, which is a late consequence of B-cell "
            "aplasia after CD19-directed therapy — not an emergency treatment for this presentation.",
        "Tocilizumab": "",
    },
    "Tocilizumab",
    "Cytokine release syndrome (CRS) — the commonest acute reaction to a CAR-T product or a bispecific "
    "T-cell engager.\n\n"
    "Recognition rests on timing plus a triad: FEVER, HYPOTENSION and HYPOXIA, typically 4–16 hours "
    "after a dose. An ordinary infusion reaction occurs within the first 6 hours and is generally "
    "afebrile, which is the discriminator built into this vignette.\n\n"
    "The syndrome is INTERLEUKIN-6 driven, so the specific treatment is TOCILIZUMAB, an anti-IL-6 "
    "receptor antibody, with corticosteroids and vasopressors added in severe cases. Sepsis looks "
    "identical and cannot be excluded early, which is why cultures and empiric antibiotics run in "
    "parallel — that is good practice, not the answer to the question.\n\n"
    "The contrast to hold is ICANS — immune effector cell-associated neurotoxicity syndrome — which "
    "appears LATER, at 3–9 days, with speech difficulty, confusion, behavioural change, headache or "
    "seizure. Its mechanism is endothelial and blood-brain barrier disturbance rather than an "
    "interleukin-6 storm, so TOCILIZUMAB IS NOT THE TREATMENT. Use dexamethasone, which penetrates "
    "the central nervous system, plus a non-sedating anticonvulsant so that sedation does not mask "
    "the neurologic examination.\n\n"
    "Two toxicities of adjacent agents worth naming cold: aldesleukin (interleukin-2) causes capillary "
    "leak syndrome, and the thalidomide derivatives cause thromboembolism and are contraindicated in "
    "pregnancy.\n\n"
    "Educational objective: Cytokine release syndrome follows CAR-T or T-cell engager therapy within "
    "hours with fever, hypotension and hypoxia and is treated with tocilizumab plus corticosteroids; "
    "ICANS occurs at 3–9 days with neurologic features and is treated with dexamethasone, not "
    "tocilizumab.",
    "The engineered immune cells are attacking the cancer so vigorously that the whole body floods "
    "with alarm signals, dropping her blood pressure. A drug that blocks the main alarm chemical "
    "switches it off.",
    exim="fig_chemo_irae_tce",
    excap="Adverse-event profiles compared — immune checkpoint inhibitors against T-cell engagers, by "
          "dose relationship, variability, organs affected, time course and predictability.",
)

# ── 90. Tamoxifen versus an aromatase inhibitor (§46) ──────────────────────────
q(
    "A 58-year-old postmenopausal woman has taken tamoxifen for 4 years after surgery for estrogen "
    "receptor-positive breast cancer. She comes to the office due to 3 weeks of vaginal bleeding. "
    "She has had no bleeding since menopause at age 51. Pelvic examination is unremarkable, and "
    "transvaginal ultrasonography shows an endometrial stripe of 12 mm. Which of the following best "
    "explains this finding?",
    {
        "Agonist activity of the drug at endometrial estrogen receptors": "",
        "Depletion of estrogen synthesis in peripheral tissues by aromatase blockade":
            "That is what an AROMATASE INHIBITOR does, and it is why those drugs cause osteoporosis, "
            "hot flashes and arthralgias — but no endometrial stimulation at all.",
        "Downregulation of pituitary gonadotropin secretion":
            "This is the action of a GnRH agonist after its initial flare, used for ovarian "
            "suppression and in prostate cancer. It lowers estrogen rather than stimulating the "
            "endometrium.",
        "Degradation of the estrogen receptor itself":
            "Fulvestrant is the pure antiestrogen that inhibits receptor dimerisation and promotes "
            "receptor degradation, with no agonist activity anywhere.",
        "Inhibition of CYP17 in the adrenal cortex":
            "Abiraterone inhibits CYP17 to block androgen synthesis in prostate cancer, and its "
            "signature toxicity is mineralocorticoid excess with hypokalemia.",
    },
    "Agonist activity of the drug at endometrial estrogen receptors",
    "Tamoxifen-associated endometrial pathology — and postmenopausal bleeding in a woman on tamoxifen "
    "is endometrial carcinoma until proven otherwise, so this needs endometrial sampling.\n\n"
    "Tamoxifen is a SELECTIVE estrogen receptor modulator: antagonist in some tissues and agonist in "
    "others. Antagonist in BREAST — the therapeutic effect. Agonist in ENDOMETRIUM — proliferation, "
    "and an increased risk of endometrial carcinoma. Agonist in BONE — which is why it preserves bone "
    "mineral density, and why raloxifene is used for osteoporosis. It also carries thromboembolic "
    "risk, and causes vaginal dryness and discharge.\n\n"
    "The pathway makes the class differences predictable: adrenal androgens → [AROMATASE] → estrogens "
    "→ [RECEPTOR] → tumour growth. Aromatase inhibitors (anastrozole, letrozole, exemestane) cut it "
    "UPSTREAM by depleting the hormone; selective estrogen receptor modulators and fulvestrant block "
    "it DOWNSTREAM at the receptor.\n\n"
    "Bone is the giveaway on an exam: a SERM PROTECTS bone but stimulates endometrium; an aromatase "
    "inhibitor removes estrogen from every tissue, so it causes OSTEOPOROSIS, hot flashes and "
    "arthralgias but no endometrial effect.\n\n"
    "One more rule from the same pathway: aromatase inhibitors work only AFTER menopause. In a "
    "premenopausal woman the ovary makes estrogen directly, far more than peripheral aromatisation "
    "accounts for, so blocking aromatase cannot suppress it — use tamoxifen, or ovarian suppression "
    "with a GnRH agonist first.\n\n"
    "Educational objective: Tamoxifen is an estrogen receptor antagonist in breast but an AGONIST in "
    "endometrium and bone, so it increases endometrial carcinoma risk while protecting bone density; "
    "aromatase inhibitors deplete estrogen everywhere and instead cause osteoporosis, hot flashes and "
    "arthralgias.",
    "Her breast cancer pill blocks estrogen in the breast but acts like estrogen in the womb lining, "
    "so that lining keeps growing. New bleeding after menopause on this drug always needs checking "
    "for cancer.",
    exim="fig_chemo_antiestrogen",
    excap="Anti-estrogen mechanisms — the aromatase step upstream and the estrogen receptor "
          "downstream, with the drug class acting at each.",
)

# ── 91. GnRH agonist tumour flare (§46) ────────────────────────────────────────
q(
    "A 71-year-old man with metastatic prostate cancer and known vertebral metastases is started on "
    "leuprolide alone. Twelve days later he comes to the emergency department due to severe mid-back "
    "pain, new weakness of both legs and difficulty passing urine. Examination shows bilateral lower "
    "extremity weakness with a sensory level at the umbilicus and a palpable bladder. Magnetic "
    "resonance imaging shows epidural extension of a T10 metastasis with cord compression. Which of "
    "the following would most likely have prevented this complication?",
    {
        "Adding an anti-androgen before starting the agonist": "",
        "Adding prednisone to suppress adrenal androgen precursors":
            "Prednisone is given WITH abiraterone, to suppress the ACTH drive that would otherwise "
            "generate mineralocorticoid excess — hypokalemia, fluid retention and hypertension. It "
            "does not cover a gonadotropin surge.",
        "Giving a bisphosphonate before the first dose":
            "Bone-directed agents reduce skeletal-related events over months. They do not prevent an "
            "acute testosterone surge from stimulating tumour.",
        "Starting an aromatase inhibitor concurrently":
            "Aromatase inhibitors block conversion of androgens to estrogens and are used in "
            "postmenopausal breast cancer. They have no role in prostate cancer.",
        "Using a lower initial dose of the agonist":
            "The flare is a mechanistic consequence of agonist activity at the receptor, not a "
            "dose-related overshoot, so dose reduction does not reliably avoid it.",
    },
    "Adding an anti-androgen before starting the agonist",
    "Tumour flare from a GnRH (LHRH) AGONIST — and the mechanism is counterintuitive enough to be a "
    "reliable exam question.\n\n"
    "Leuprolide, goserelin and triptorelin bind LHRH receptors on pituitary gonadotropes. Because "
    "they are AGONISTS, the first effect is an INCREASE in luteinizing hormone and follicle-"
    "stimulating hormone — and therefore a surge in testosterone — before continuous stimulation "
    "downregulates the receptor and shuts the axis down.\n\n"
    "In a man with bony metastatic prostate cancer that transient surge stimulates the tumour: "
    "worsening bone pain, urinary obstruction, or — as here — spinal cord compression. The mandated "
    "prevention is concurrent ANTI-ANDROGEN therapy (bicalutamide, flutamide or nilutamide) started "
    "before or with the agonist to cover the flare window.\n\n"
    "The rest of the hormonal block for contrast: anti-androgens are receptor antagonists causing "
    "gynecomastia and rare hepatotoxicity; abiraterone DEPLETES androgen by inhibiting CYP17 and is "
    "given with prednisone because blocking CYP17 shunts precursors into the mineralocorticoid "
    "pathway, producing hypokalemia, fluid retention and hypertension; and GnRH agonists themselves "
    "cause hot flashes, sexual dysfunction and reduced bone mineral density — the toxicity of "
    "androgen withdrawal.\n\n"
    "Cord compression itself is an emergency requiring corticosteroids and urgent neurosurgical or "
    "radiation oncology involvement.\n\n"
    "Educational objective: GnRH agonists initially raise luteinizing hormone and testosterone before "
    "downregulating the pituitary, causing a tumour flare that can precipitate cord compression in "
    "metastatic prostate cancer; concurrent anti-androgen therapy prevents it.",
    "The drug that eventually shuts off testosterone starts by switching it up for a couple of weeks. "
    "That short surge fed his spine tumours, which is why a blocking drug should be started first.",
    exim="fig_chemo_gnrh",
    excap="The hypothalamic-pituitary-gonadal axis with the sites of action of the anti-androgens and "
          "the GnRH/LHRH agonists.",
)

# ── 92. Acute compartment syndrome (§56) ──────────────────────────────────────
q(
    "A 24-year-old woman sustains a closed tibial shaft fracture in a soccer match and is placed in "
    "a long-leg cast. Six hours later she reports deep, boring calf pain that she rates 9 out of 10 "
    "despite intravenous opioids. The cast is bivalved, with no relief. The leg is swollen and the "
    "anterior compartment is tense and firm. Passive dorsiflexion of the toes reproduces severe "
    "pain. Dorsalis pedis and posterior tibial pulses are palpable and the foot is warm and pink. "
    "Which of the following is the most appropriate next step in management?",
    {
        "Compression ultrasonography of the leg":
            "A deep vein thrombosis is worth considering when swelling that had improved worsens "
            "again DAYS after an injury — not at 6 hours, and it does not produce a wood-hard "
            "compartment with pain on passive stretch.",
        "Elevation of the limb above the level of the heart":
            "Elevation above heart level lowers arterial inflow pressure and can worsen compartment "
            "perfusion. The limb is kept at heart level while the operating room is prepared.",
        "Emergency fasciotomy": "",
        "Measurement of serum creatine kinase":
            "Creatine kinase, myoglobinuria, hyperkalemia and acute kidney injury are the downstream "
            "consequences of muscle necrosis and must be watched for — but waiting on that result "
            "means waiting for the muscle to die.",
        "Observation with serial neurovascular checks":
            "Serial checks are the answer when the diagnosis is genuinely in doubt. Here two early "
            "reliable signs are already present, and the ischemia is progressing hour by hour.",
    },
    "Emergency fasciotomy",
    "Acute compartment syndrome — the true emergency among the causes of post-traumatic limb "
    "swelling.\n\n"
    "Mechanism: edema accumulates inside a non-compliant fascial compartment → interstitial pressure "
    "rises above capillary perfusion pressure → capillaries and thin-walled veins collapse → ischemia "
    "→ ischemia increases capillary permeability → more edema. It is a self-amplifying cycle that "
    "does not break on its own.\n\n"
    "The two early RELIABLE signs are both here: pain OUT OF PROPORTION to the injury, and pain on "
    "PASSIVE STRETCH of the muscles in the compartment. The classic 'six Ps' are a trap — "
    "pulselessness, pallor and paralysis are LATE, and waiting for them means waiting for dead "
    "muscle.\n\n"
    "Why the normal pulses are irrelevant: this is a CAPILLARY perfusion problem. Compartment "
    "pressure only has to exceed capillary perfusion pressure to make muscle ischemic, and that is "
    "far below the pressure needed to obliterate flow in a named artery. If pressures are measured, "
    "a delta pressure (diastolic minus compartment pressure) below 30 mm Hg is the usual operative "
    "threshold — but the diagnosis is clinical, and splitting the cast is only a holding measure.\n\n"
    "Read the clock, then read the feel, across the six mechanisms of post-traumatic swelling: HOURS "
    "→ inflammatory edema, hematoma, compartment syndrome; DAYS → deep vein thrombosis, "
    "hypoalbuminemia from resuscitation; WEEKS → lymphedema. Then texture decides: hard and "
    "exquisitely painful is compartment; soft, pitting and one leg is a clot; soft, pitting, both "
    "legs and the sacrum is oncotic; firm, non-pitting with square toes is lymphatic.\n\n"
    "Educational objective: Acute compartment syndrome presents within hours of injury with pain out "
    "of proportion and pain on passive stretch, and palpable pulses do not exclude it because the "
    "lesion is at capillary perfusion pressure. Treatment is emergency fasciotomy.",
    "Swelling inside a tight sleeve of tissue is squeezing her muscle's tiny blood vessels shut, even "
    "though the big artery is still flowing. The only fix is to cut the sleeve open and release the "
    "pressure.",
)

# ── 93. Lymphedema versus deep vein thrombosis (§48) ───────────────────────────
q(
    "A 54-year-old woman comes to the office due to 3 weeks of a heavy, aching right leg. Seven "
    "weeks ago she underwent an open right inguinal hernia repair. She has no chest pain or "
    "breathlessness. The right leg is diffusely swollen to the toes, which appear squared off; the "
    "skin over the dorsum of the foot is thickened and cannot be lifted between finger and thumb at "
    "the second web space. There is no calf tenderness. Compression ultrasonography of the right leg "
    "shows no deep vein thrombosis. Photographs of comparable findings in another patient are shown. "
    "Which of the following is the most likely cause of this patient's swelling?",
    {
        "Chronic venous insufficiency":
            "Venous insufficiency gives ankle swelling with hemosiderin staining, varicosities and "
            "sometimes ulceration above the medial malleolus — and the web space skin remains "
            "pinchable.",
        "Congestive heart failure":
            "Heart failure gives BILATERAL dependent edema. Unilateral swelling is doing real work in "
            "this vignette and excludes it.",
        "Filarial infection of lymphatic vessels":
            "Wuchereria bancrofti is the commonest cause of secondary lymphedema WORLDWIDE and "
            "produces elephantiasis — but it requires residence in an endemic region, and unlike "
            "surgical injury it is treatable with medication.",
        "Recurrent deep vein thrombosis":
            "A clot causes acute swelling over hours to days with calf tenderness and a negative "
            "Stemmer sign — and the ultrasound is negative.",
        "Surgical disruption of inguinal lymphatics": "",
    },
    "Surgical disruption of inguinal lymphatics",
    "Secondary lymphedema from iatrogenic injury to the groin lymphatics — the commonest cause of "
    "lymphedema in developed countries, where lymphatic trauma, nodal dissection, cancer and "
    "radiotherapy dominate the list.\n\n"
    "The discriminating triad in this vignette:\n"
    "• UNILATERAL — so not heart failure, which is bilateral\n"
    "• NEGATIVE ULTRASOUND — so not a deep vein thrombosis. Order the ultrasound FIRST, always, "
    "because a clot can kill and lymphedema cannot\n"
    "• SQUARE TOES with a positive STEMMER SIGN — the inability to tent the skin of the interdigital "
    "web space, which is what names the diagnosis\n\n"
    "Add the timing: lymphedema develops gradually over weeks to months, characteristically 6–8 weeks "
    "after a groin operation, whereas a clot appears over hours to days. Pain is aching or heaviness; "
    "severe pain is rare and should make you think of infection or ischemia instead.\n\n"
    "Pathophysiology: lymph production exceeds the transport capacity of the conduits, so protein and "
    "cellular metabolites accumulate in the interstitium, drawing water and triggering collagen "
    "deposition. That protein load is why chronic lymphedema becomes firm, fibrotic and NON-pitting, "
    "with hyperkeratosis, lichenification and peau d'orange.\n\n"
    "Confirm with lymphoscintigraphy if needed. Management is conservative and lifelong — elevation, "
    "exercise, manual lymphatic massage and compression garments — plus meticulous skin hygiene and "
    "infection prevention. Surgery is a late resort. Watch for the late complication: "
    "lymphangiosarcoma.\n\n"
    "Educational objective: Unilateral limb swelling with square toes and a positive Stemmer sign "
    "after a negative venous ultrasound is lymphedema; in developed countries the leading cause is "
    "iatrogenic injury to lymphatics, and worldwide it is filariasis.",
    "The surgery cut the tiny drainage channels in her groin, so fluid has nowhere to go and the leg "
    "stays swollen. The giveaway is that the skin on her toes is so tough you cannot pinch it.",
    image="fig_lymphedema_chronic",
    imcap="Clinical photographs of an arm and both legs with gross, disfiguring swelling; the skin is "
          "thickened and irregular with a dimpled surface and deep creases at the wrist and ankle.",
    exim="fig_stemmer",
    excap="Normal versus lymphedematous limb — the Stemmer sign, in which the skin of the web space "
          "cannot be lifted away from the underlying tissue.",
)

# ── 94. Virchow node and the thoracic duct (§57) ───────────────────────────────
q(
    "A 61-year-old man comes to the office due to 3 months of epigastric discomfort, early satiety "
    "and 8 kg of weight loss. Examination shows a firm, non-tender, 2 cm node fixed to underlying "
    "tissue above the left clavicle. There is no cervical, axillary or inguinal lymphadenopathy "
    "elsewhere. Fine needle aspiration of the node shows adenocarcinoma. Which of the following best "
    "explains why an abdominal primary tumour presents at this site?",
    {
        "Retrograde flow through incompetent lymphatic valves":
            "Valve incompetence with flow reversal is a mechanism of lymphEDEMA distal to an "
            "obstruction, not the route by which tumour reaches a supraclavicular node.",
        "The right lymphatic duct drains the abdominal viscera":
            "The right lymphatic duct drains only the right side of the head and neck, the right arm "
            "and the right hemithorax — which is exactly why a RIGHT supraclavicular node points to a "
            "lung, esophageal, mediastinal or head and neck primary instead.",
        "The thoracic duct terminates at the left subclavian vein": "",
        "Tumour cells enter the bloodstream before reaching any node":
            "Carcinomas spread preferentially by LYMPHATICS; sarcomas prefer the bloodstream. "
            "Lymphatic and hematogenous spread are sequential here, not alternatives — lymph "
            "eventually empties into the venous system.",
        "Tumour spreads directly across the diaphragm to the neck":
            "There is no direct anatomic route from the stomach to the supraclavicular fossa. The "
            "connection is the lymphatic chain.",
    },
    "The thoracic duct terminates at the left subclavian vein",
    "Virchow's node — an enlarged LEFT supraclavicular node from metastatic abdominal carcinoma, "
    "classically gastric. The palpable finding carries its own eponym, Troisier sign.\n\n"
    "The anatomy: lymph from the stomach passes through celiac and para-aortic nodes into the cisterna "
    "chyli, then ascends the THORACIC DUCT, which drains essentially the whole body below the "
    "diaphragm plus the left side above it, and empties at the junction of the LEFT subclavian and "
    "left internal jugular veins. The last nodal station before tumour cells enter the systemic "
    "venous circulation therefore sits in the left supraclavicular fossa — which is also why "
    "lymphatic spread becomes hematogenous spread at that point.\n\n"
    "Why carcinoma travels this way at all: lymphatic capillaries have no basement membrane and loose, "
    "overlapping endothelial junctions, so they are far easier to penetrate than blood capillaries. "
    "Carcinomas spread preferentially by lymphatics; sarcomas preferentially by blood.\n\n"
    "Reading the node at the bedside: hard, painless, FIXED and progressively enlarging is metastatic, "
    "and fixation specifically implies extranodal extension through the capsule, which independently "
    "worsens prognosis. Soft, mobile, tender and regressing after a local infection is reactive.\n\n"
    "The rest of the drainage map worth carrying: breast → axillary (about 75%) with internal mammary "
    "for medial tumours; testis → PARA-AORTIC, not inguinal, because it descended from the posterior "
    "abdominal wall (scrotal SKIN drains to inguinal nodes); anal canal → above the dentate line to "
    "internal iliac, below it to superficial inguinal; lung → hilar then mediastinal; prostate → "
    "obturator and internal iliac.\n\n"
    "Educational objective: The thoracic duct drains the abdomen and empties at the junction of the "
    "left subclavian and left internal jugular veins, so abdominal carcinoma classically presents as "
    "an enlarged left supraclavicular (Virchow) node; a right supraclavicular node instead suggests a "
    "thoracic or head and neck primary.",
    "All the lymph fluid from the belly travels up one big drainpipe that empties into a vein just "
    "behind the left collarbone. Cancer cells riding that pipe get stuck at the last filter, which is "
    "the lump you can feel there.",
    exim="fig_lymph_system",
    excap="The lymphatic system — the thoracic duct draining the abdomen and the left side of the "
          "body into the left subclavian vein.",
)

# ── 95. The sentinel node and the subcapsular sinus (§57, §35) ─────────────────
q(
    "A 49-year-old woman with a 1.8 cm invasive ductal carcinoma of the left breast and no palpable "
    "axillary nodes is scheduled for lumpectomy. Before surgery, a radiolabelled colloid and blue "
    "dye are injected around the tumour, and two axillary nodes take up the tracer and are excised. "
    "The pathologist is asked to examine them for metastatic deposits. Which of the following "
    "compartments of the node should be examined first?",
    {
        "Germinal centers of the follicles":
            "Germinal centers are where B cells undergo somatic hypermutation and selection. They "
            "expand in reactive hyperplasia and are the site of follicular lymphoma — not the "
            "landing site of carcinoma.",
        "Medullary cords":
            "The medullary cords contain plasma cells and lymphocytes near the hilum, at the EXIT of "
            "the node. Tumour reaches them only after passing through the sinus first.",
        "Paracortex":
            "The paracortex is the T-cell zone with high endothelial venules; it expands in viral "
            "infections and dermatopathic lymphadenopathy.",
        "Perinodal fat":
            "Tumour in perinodal fat means extranodal EXTENSION — a late, prognostically adverse "
            "finding that occurs after the node is substantially involved.",
        "Subcapsular sinus": "",
    },
    "Subcapsular sinus",
    "Afferent lymphatics pierce the capsule on the convex surface of the node and empty into the "
    "SUBCAPSULAR (marginal) SINUS, so that is the first place tumour cells arrive and the first "
    "compartment the pathologist examines. A small cohesive cluster sitting in a sinus is the "
    "earliest metastatic finding.\n\n"
    "The route in full: local invasion (loss of E-cadherin adhesion, basement membrane degradation by "
    "matrix metalloproteinases) → lymphovascular invasion, which is easy because lymphatic capillaries "
    "have no basement membrane and loose endothelial junctions → transport along afferent lymphatics "
    "→ arrival in the subcapsular sinus → progressive effacement of the node → exit by the efferent "
    "lymphatic at the hilum to the next echelon → eventually the thoracic duct and the systemic "
    "circulation.\n\n"
    "The sentinel node is the first node draining the tumour bed, located with blue dye and "
    "radiolabelled colloid. The logic is conditional: if the sentinel node is free of tumour, nodes "
    "downstream are almost certainly free too, and a full axillary dissection can be avoided. That "
    "matters because the dissection itself is the commonest cause of secondary lymphedema in "
    "developed countries — sentinel biopsy buys accurate nodal staging at a fraction of the "
    "morbidity. The caveat is skip metastases, which occur when tumour obstructs lymphatics and "
    "diverts flow around the expected node.\n\n"
    "Contrast this with the node's reactive compartments: B cells in the cortical follicles, T cells "
    "in the paracortex, plasma cells in the medullary cords, histiocytes in the sinuses.\n\n"
    "Educational objective: Metastatic carcinoma arrives through afferent lymphatics and is first "
    "seen in the subcapsular sinus, which is why that compartment is examined first in a sentinel "
    "node; a negative sentinel node allows a full nodal dissection — and its lymphedema risk — to be "
    "avoided.",
    "Lymph flows into a node at its outer rim first, so that rim is where escaped cancer cells land "
    "before anywhere else. If the first node on the route is clean, the ones after it almost always "
    "are too.",
    exim="fig_slide_node_architecture",
    excap="The floor plan: afferent lymphatics enter at the capsule, the efferent lymphatic leaves "
          "at the hilum, and each zone holds one population.",
)

# ── 96. Splenic injury with a contrast blush (§55) ─────────────────────────────
q(
    "A 27-year-old man is brought to the emergency department after a motor vehicle collision. He is "
    "alert and reports left-sided abdominal pain and left shoulder pain that worsens when the "
    "stretcher is laid flat. Pulse is 104/min and blood pressure is 118/74 mm Hg, which remains "
    "stable after 1 L of crystalloid. The abdomen is tender in the left upper quadrant without "
    "guarding, and there is tenderness over the left lower ribs. Hemoglobin is 12.4 g/dL. "
    "Contrast-enhanced computed tomography of the abdomen is shown, demonstrating a 4 cm "
    "intraparenchymal splenic laceration with a focus of active contrast extravasation contained "
    "within the capsule. Which of the following is the most appropriate next step in management?",
    {
        "Admission for observation with serial hematocrit measurement":
            "Non-operative management is the default for a stable patient with NO blush and no "
            "peritonitis — it is rung 1, and the contrast extravasation here is precisely what moves "
            "him up a rung.",
        "Emergency laparotomy with splenectomy":
            "Surgery is for hemodynamic instability despite resuscitation, peritonitis, or failure of "
            "the rungs above. He is stable after 1 L of fluid.",
        "Exploratory laparoscopy with splenorrhaphy":
            "Spleen-preserving repair exists, but an operation is not indicated in a stable patient "
            "whose bleeding can be controlled radiologically.",
        "Repeat focused assessment with sonography for trauma":
            "FAST is the test for the UNSTABLE patient, where free fluid means the operating room. He "
            "has already had the definitive study.",
        "Splenic artery angiography with embolization": "",
    },
    "Splenic artery angiography with embolization",
    "Blunt splenic injury with a contrast blush in a hemodynamically stable patient — rung 2 of the "
    "three-rung ladder.\n\n"
    "The diagnostic fork comes first, and it turns on STABILITY, not on the grade:\n"
    "• UNSTABLE → bedside FAST. Free fluid in an unstable patient means the operating room. An "
    "unstable trauma patient does not go to the scanner\n"
    "• STABLE → contrast-enhanced CT, which grades the injury and — critically — detects the BLUSH, "
    "meaning the spleen is bleeding at this moment\n\n"
    "Then the ladder:\n"
    "1. MEDICAL / non-operative management — stable, no blush, no peritonitis: monitored bed, bed "
    "rest, serial hemoglobin and abdominal examination, type and cross held active. It succeeds in "
    "the large majority, and even more often in children\n"
    "2. INTERVENTIONAL — angiography with splenic artery embolization for a blush, a pseudoaneurysm, "
    "an arteriovenous fistula, or a high-grade (IV–V) injury. This is the rung that lets a patient "
    "keep the spleen who would once have lost it. Proximal embolization drops perfusion pressure "
    "while collaterals preserve the organ; distal embolization targets the bleeding vessel\n"
    "3. SURGICAL — instability despite resuscitation, peritonitis, or failure above. The unstable "
    "patient gets a total splenectomy, because the correct operation in a crashing patient is the "
    "fast one\n\n"
    "The left shoulder pain worse when supine is KEHR SIGN: blood irritating the left hemidiaphragm, "
    "which shares the C3–C5 phrenic root with the shoulder dermatome. It names the organ but does not "
    "decide management. Left lower rib fractures should always prompt imaging of the spleen — the "
    "ribs that protect it are the ribs that lacerate it.\n\n"
    "Watch afterwards for DELAYED rupture, classically on day 5–6, and for a pseudoaneurysm that may "
    "be absent on the first scan — which is why non-operative management means inpatient observation "
    "rather than reassurance.\n\n"
    "Educational objective: In blunt splenic injury, hemodynamic stability decides the pathway — "
    "unstable patients go to the operating room after FAST, while stable patients are imaged by CT; a "
    "contrast blush in a stable patient is the indication for splenic artery embolization rather than "
    "observation or surgery.",
    "His spleen is torn and actively leaking dye on the scan, but his blood pressure is holding. "
    "Rather than remove the spleen, a radiologist threads a catheter up and plugs the bleeding "
    "vessel.",
    image="fig_splenic_injury_ct",
    imcap="Contrast-enhanced axial computed tomography of the upper abdomen: the spleen is "
          "heterogeneous with surrounding low-attenuation fluid, and a rounded focus of bright "
          "contrast lies within the parenchyma.",
    exim="fig_splenic_artery",
    excap="The splenic artery off the celiac trunk, running along the superior border of the "
          "pancreas to the hilum — the vessel the interventional radiologist catheterizes.",
)

# ── 97. Unstable splenic injury and post-splenectomy care (§55, §11) ───────────
q(
    "A 34-year-old woman is brought to the emergency department after falling from a horse onto her "
    "left flank. She is pale and diaphoretic. Pulse is 132/min and blood pressure is 78/44 mm Hg; "
    "after 2 L of crystalloid and 2 units of red blood cells, blood pressure is 82/50 mm Hg and "
    "pulse is 128/min. The abdomen is distended and diffusely tender. Focused assessment with "
    "sonography for trauma shows free fluid in the left upper quadrant and pelvis. She undergoes "
    "emergency laparotomy and total splenectomy for a shattered spleen. Which of the following is "
    "most appropriate before her discharge?",
    {
        "Administration of pneumococcal, meningococcal and Haemophilus vaccines": "",
        "Daily lifelong penicillin prophylaxis for all adult patients after splenectomy":
            "Daily antibiotic prophylaxis is the standard of care in CHILDREN, above all in pediatric "
            "sickle cell disease. In adults it is not routine; education about fever is.",
        "Lifelong warfarin anticoagulation for portal vein thrombosis":
            "Splenic and portal vein thrombosis is a recognised complication, favoured by the "
            "post-splenectomy platelet surge — but prophylaxis is aspirin if the platelet count "
            "exceeds about 1 million, not lifelong warfarin.",
        "Repeat computed tomography to exclude an accessory spleen":
            "Accessory spleens matter when an operation was performed for immune thrombocytopenia and "
            "the disease recurs. After trauma splenectomy they are not routinely hunted.",
        "Scheduled transfusion to maintain hemoglobin above 10 g/dL":
            "Transfusion thresholds are restrictive — about 7 g/dL in a stable euvolemic patient. A "
            "scheduled program has no role here.",
    },
    "Administration of pneumococcal, meningococcal and Haemophilus vaccines",
    "Emergency splenectomy for an unstable blunt splenic injury — the correct decision, since she "
    "failed to respond to resuscitation and FAST showed free fluid. An unstable trauma patient does "
    "not go to the CT scanner.\n\n"
    "The management question that follows is prevention of OVERWHELMING POST-SPLENECTOMY INFECTION. "
    "The spleen is the body's principal filter for encapsulated organisms, so without it a "
    "bloodstream infection can progress to fulminant sepsis in HOURS rather than days. The organisms "
    "are Streptococcus pneumoniae (dominant by a wide margin), Neisseria meningitidis and Haemophilus "
    "influenzae type b — and the prevention is three-part:\n"
    "1. VACCINATE against all three. For an ELECTIVE splenectomy, vaccinate about 2 weeks BEFORE "
    "operating. That is impossible in trauma, so vaccinate before discharge — commonly around 14 days "
    "postoperatively, when the immune response is better\n"
    "2. Antibiotic prophylaxis in CHILDREN — daily penicillin\n"
    "3. EDUCATE the patient and family that any fever is an emergency requiring immediate evaluation "
    "and empiric antibiotics without waiting for cultures. This is the intervention that actually "
    "saves lives, because the window is measured in hours\n\n"
    "Other post-splenectomy issues to anticipate: reactive thrombocytosis (start aspirin if the "
    "platelet count exceeds about 1 million) with a risk of splenic and portal vein thrombosis; "
    "subphrenic abscess with a left pleural effusion; pancreatic tail injury from hilar dissection; "
    "gastric wall necrosis if the short gastric vessels were divided carelessly; and Howell-Jolly "
    "bodies appearing on the smear as proof that no functioning splenic tissue remains.\n\n"
    "Educational objective: After splenectomy, patients require vaccination against Streptococcus "
    "pneumoniae, Neisseria meningitidis and Haemophilus influenzae type b — before an elective "
    "operation, or before discharge after an emergency one — together with education that any fever "
    "requires immediate empiric antibiotics.",
    "Without a spleen, a few specific bacteria can go from a sore throat to life-threatening in "
    "hours. Vaccines against those bugs, plus a standing rule to treat any fever immediately, are "
    "what keep her safe.",
    exim="fig_opsi",
    excap="Overwhelming post-splenectomy sepsis — purpura fulminans and peripheral gangrene, the "
          "endpoint the vaccination schedule exists to prevent.",
)

# ── 98. Accuracy versus precision (§23) ───────────────────────────────────────
q(
    "A hematology laboratory reviews quality control data for a new analyzer. Across 40 consecutive "
    "control samples with a known platelet count of 250,000/mm3, the instrument reports values "
    "ranging from 208,000 to 222,000/mm3, with a mean of 214,000/mm3 and a standard deviation of "
    "3,600/mm3. Repeat runs of the same sample agree closely with one another. Which of the "
    "following best describes this instrument's performance, and what should be done?",
    {
        "Decreased accuracy from systematic bias; recalibrate the instrument": "",
        "Decreased accuracy from random bias; replace the reagent lot":
            "Random bias is what degrades PRECISION rather than accuracy, and it scatters results "
            "around the true value rather than shifting them consistently.",
        "Decreased precision from random bias; repeat testing in duplicate":
            "Decreased precision means results scatter widely. This instrument's repeat runs agree "
            "closely — a standard deviation of 3,600 on a count of about 214,000 is tight.",
        "Decreased precision from systematic bias; verify specimen handling":
            "Systematic bias does not affect precision. Handling problems such as a clotted or "
            "under-filled tube produce erratic single results, not a consistent offset across 40 "
            "controls.",
        "Decreased sensitivity of the assay; lower the detection threshold":
            "Sensitivity and specificity describe how well a test identifies disease, not how close "
            "an instrument's measurements are to a known value.",
    },
    "Decreased accuracy from systematic bias; recalibrate the instrument",
    "Accuracy and precision measure different things, and the distinction is the point of this "
    "question.\n\n"
    "• ACCURACY is how close a result is to the true value. SYSTEMATIC bias — every result off in the "
    "same direction by a consistent amount — reduces accuracy. It often reflects an instrument "
    "problem and is fixable by CALIBRATION. Rule of thumb: consistently wrong → suspect the machine\n"
    "• PRECISION is how close repeated measurements are to each other. RANDOM bias — results "
    "scattering around the truth — reduces precision. It may be an intrinsic feature of the assay and "
    "not fixable at all. Rule of thumb: inconsistently wrong → suspect the method\n\n"
    "Here every value is low by roughly 36,000 (about 14%) with a tight spread, which is the textbook "
    "description of systematic bias: accurate no, precise yes.\n\n"
    "One nuance worth carrying: precision is partly a property of the ANALYTE, not just the machine. "
    "Platelets vary by roughly 15%–20% between repeat runs intrinsically, because they activate — so "
    "a repeat count differing by 15% is not an instrument fault. The MCV, by contrast, is very "
    "tightly precise, so a genuinely shifting MCV means something real.\n\n"
    "And a practical note on the laboratory's own numbers: turnaround time is measured across the "
    "whole workflow, from sample arrival to the result reaching the clinician, not just the "
    "instrument's run time.\n\n"
    "Educational objective: Systematic bias shifts every measurement in the same direction and "
    "reduces ACCURACY, and is corrected by calibration; random bias scatters measurements and reduces "
    "PRECISION, and may be intrinsic to the assay.",
    "The machine gives nearly the same answer every time, so it is consistent — but that answer is "
    "always about 14% too low. Consistent and wrong means the machine needs recalibrating.",
    exim="fig_slide_accuracy_precision",
    excap="Accuracy versus precision: systematic bias moves every shot off-centre; random bias "
          "scatters them.",
)

# ── 99. The incomplete prescription (§54) ─────────────────────────────────────
q(
    "A 28-year-old woman is diagnosed with iron deficiency anemia due to menorrhagia. A resident "
    "sends the following prescription to the pharmacy: 'Date 12 Sep 2026. Jane Doe, date of birth 14 "
    "Mar 1998, 14 Elm Street. Ferrous sulfate 325 mg tablets. Sig: Take 1 tablet by mouth three "
    "times daily with vitamin C. Indication: iron deficiency anemia. Refills: 2.' The pharmacist "
    "telephones to say the prescription cannot be filled as written. Which of the following elements "
    "is missing?",
    {
        "The dosage form":
            "'Tablets' is stated. Dosage form matters most where a drug exists as tablet, capsule, "
            "solution, suspension or patch — especially in pediatrics.",
        "The indication for therapy":
            "'Iron deficiency anemia' is stated. The indication lets the pharmacist catch a "
            "drug-indication mismatch and helps the patient understand the medicine, and it matters "
            "most on an as-needed prescription.",
        "The quantity to dispense": "",
        "The route of administration":
            "'By mouth' is stated within the directions, which is where route belongs alongside dose "
            "and frequency.",
        "The strength of the drug":
            "'325 mg' is stated. Omitting strength makes a prescription unfillable too — most drugs "
            "come in several — but it is present here.",
    },
    "The quantity to dispense",
    "The prescription is missing 'Disp: #90'. Without a quantity the pharmacist cannot know whether "
    "to supply one month or three, and cannot fill it at all.\n\n"
    "Run the bare-minimum list and check each element: drug and dose (ferrous sulfate 325 mg) ✓; "
    "indication (iron deficiency anemia) ✓; AMOUNT TO DISPENSE ✗; refills (2) ✓. Date, patient "
    "identifiers including date of birth, dosage form, route and frequency are all present as well.\n\n"
    "Nothing else here is unsafe, and the things to scan for on any prescription question are the "
    "patient-safety conventions:\n"
    "• NO TRAILING ZERO — write 1 mg, never 1.0 mg, because a missed decimal reads as 10 mg\n"
    "• ALWAYS A LEADING ZERO — write 0.5 mg, never .5 mg, for the same reason in reverse\n"
    "• Write 'units' in full — '10 U' is misread as 100, the classic insulin and heparin error\n"
    "• Write the frequency out — daily, every other day, four times daily — because QD, QOD and QID "
    "are readily confused with one another\n"
    "• Spell the drug fully — 'MS' has meant both morphine sulfate and magnesium sulfate\n"
    "• For controlled substances, write the quantity in words as well as numerals\n\n"
    "Two drug-specific points for this particular prescription: specify the iron SALT, because "
    "elemental iron differs (ferrous fumarate 33%, ferrous sulfate 20%, ferrous gluconate about 12%); "
    "and warn the patient that black or green tarry stools are expected, so they are not mistaken for "
    "gastrointestinal bleeding.\n\n"
    "Educational objective: A complete prescription requires drug, strength, dosage form, directions "
    "(dose, route, frequency), indication, QUANTITY TO DISPENSE and refills, plus prescriber "
    "identification; omitting the quantity makes the prescription unfillable.",
    "Everything about how to take the medicine is written down, but not how many pills to hand over. "
    "The pharmacist has no way to guess whether that means one month or three.",
)

# ── 100. Prescribing for the older adult (§54, §53) ───────────────────────────
q(
    "An 84-year-old woman with moderate dementia is brought to the office by her son because she has "
    "become agitated and restless in the evenings and sleeps poorly. She lives with him and has had "
    "no fever, cough, dysuria or change in bowel habit, and examination and basic laboratory studies "
    "including a urinalysis are unremarkable. Her medications are lisinopril, atorvastatin and "
    "acetaminophen. Her son asks for 'something to calm her down at night'. Which of the following "
    "is the most appropriate response?",
    {
        "Prescribe diphenhydramine nightly for sleep":
            "Diphenhydramine is an ANTICHOLINERGIC, one of the four named high-risk classes in older "
            "adults, and it worsens confusion, urinary retention and fall risk. It is on the Beers "
            "list for exactly this reason.",
        "Prescribe lorazepam at bedtime":
            "Benzodiazepines are sedatives — another of the four high-risk classes — and are "
            "conspicuously absent even from the reluctant second-line options for anxiety in older "
            "adults.",
        "Prescribe quetiapine at bedtime":
            "Antipsychotics carry a boxed warning for increased mortality in elderly patients with "
            "dementia-related psychosis. They are reserved for severe distress or danger, not for "
            "evening restlessness.",
        "Prescribe zolpidem at bedtime":
            "A sedative-hypnotic, strongly associated with falls and delirium in older adults, and "
            "not among the options offered even for insomnia in this age group.",
        "Recommend non-drug behavioural management": "",
    },
    "Recommend non-drug behavioural management",
    "There is no safe medication for the neuropsychiatric behaviours of dementia — and unlike "
    "insomnia and anxiety, which each get a reluctant second-line drug option, this one gets no "
    "pharmacologic fallback at all. The stated treatment is compassion and creativity: meet the "
    "person where they are, address unmet needs (pain, hunger, boredom, disrupted routine, "
    "overstimulation in the evening), and support the caregiver.\n\n"
    "Why the bar is so high: in older adults, medications are directly linked to FALLS, DELIRIUM, "
    "DEMENTIA, DISABILITY and DEATH. The four high-risk classes are OPIOIDS, ANTICHOLINERGICS, "
    "SEDATIVES and ANTIDEPRESSANTS — and every tempting option in this question belongs to one of "
    "them.\n\n"
    "The tools that exist for exactly this decision:\n"
    "• BEERS CRITERIA — medications potentially inappropriate in adults 65 and older\n"
    "• ANTICHOLINERGIC BURDEN SCALE — catches the patient on five individually mild drugs whose "
    "combined load is causing the confusion\n"
    "• STOPP — drugs that should be stopped; STAR — drugs that should be started but have not been. "
    "The under-prescribing half is the one people forget\n"
    "• The pharmacist, named explicitly as a resource\n\n"
    "And the maxim, with its correction: 'start low, go slow — BUT get somewhere'. Stopping at a "
    "sub-therapeutic dose because a patient is old is its own harm, which is what the START half of "
    "START/STOPP exists to catch.\n\n"
    "For comparison, the other two 'no safe medication' slides do offer a fallback: insomnia — "
    "cognitive behavioural therapy and sleep restriction first, then possibly doxepin or trazodone; "
    "anxiety — cognitive behavioural therapy first, then possibly a selective serotonin reuptake "
    "inhibitor, and notably never a benzodiazepine.\n\n"
    "Educational objective: There is no safe pharmacologic treatment for the behavioural symptoms of "
    "dementia; management is non-pharmacologic. Opioids, anticholinergics, sedatives and "
    "antidepressants are the high-risk classes in older adults, screened for with the Beers criteria, "
    "the anticholinergic burden scale and START/STOPP.",
    "Every calming pill available makes older people more likely to fall, get confused and end up in "
    "hospital. The real treatment is changing what happens around her in the evening, not adding a "
    "drug.",
)
