# Batch 21 — Antineoplastic pharmacology, lymphatics & thrombosis
# §43 s38-chemo-principles · §45 s40-targeted-immuno · §46 s41-hormonal
# §48 s43-lymphedema · §56 s53-traumatic-edema · §57 s54-lymphatic-spread · §49 s44-vte-duration
# Native LOs: 10, 11, 15, 16, 34, 60, 64
#
# Options are supplied as {option text: wrong-answer explanation}; the helper alphabetises,
# letters, and re-keys. See QUIZ_BUILD_METHOD.md, "The option helper".

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
# §43 — Traditional chemotherapy: principles, resistance, mechanisms (LO 64)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "An oncology team is designing a regimen for an aggressive lymphoma. They have selected an "
    "alkylating agent and are choosing a second drug. Two candidates have equivalent single-agent "
    "activity against the tumor: one acts by a different mechanism but shares the alkylator's "
    "dose-limiting myelosuppression, and the other acts by a different mechanism and has a different "
    "dose-limiting toxicity. Which of the following best explains why the second candidate is "
    "preferred?",
    {
        "Both drugs can be given at full dose": "",
        "It avoids the need for a rescue agent":
            "Rescue agents such as leucovorin, mesna and dexrazoxane are chosen for specific drugs and "
            "specific toxicities. Nothing about non-overlapping toxicity removes the need for one.",
        "It converts the regimen from cell cycle-specific to cell cycle-nonspecific":
            "Cell cycle specificity is a fixed property of each drug and is not changed by what it is "
            "combined with. It is a separate reason to combine agents, not the reason described here.",
        "It eliminates the possibility of acquired resistance":
            "Combination therapy DECREASES the rate at which resistance develops, because the cell must "
            "acquire several independent mechanisms at once. It does not eliminate it — multi-drug "
            "resistance defeats several unrelated drugs through one pump.",
        "It produces a larger log kill from a single dose":
            "Log kill describes the constant FRACTION of cells killed per dose. Adding a second "
            "mechanism does increase total kill, but the specific advantage of non-overlapping "
            "toxicity is a dosing advantage, not a kinetic one.",
    },
    "Both drugs can be given at full dose",
    "The rule has two halves, and this question tests the second one. Combine drugs with differing "
    "MECHANISMS of action AND differing ADVERSE DRUG REACTIONS.\n\n"
    "• Different mechanism buys additive kill and a larger spectrum of activity — a heterogeneous "
    "tumor contains subclones with different vulnerabilities, so more mechanisms reach more of them. "
    "It also decreases the rate of resistance development, because the cell must acquire several "
    "independent resistance mechanisms simultaneously.\n"
    "• Different toxicity is what lets you give each agent at its full effective dose. If two drugs "
    "share a dose-limiting toxicity, you must dose-reduce one or both — and a dose-reduced regimen "
    "kills a smaller fraction of the tumor. That practical cost is exactly why the different-organ-"
    "toxicity rule exists.\n\n"
    "R-CHOP is the worked example: rituximab (anti-CD20 antibody), cyclophosphamide (alkylator), "
    "hydroxydaunorubicin/doxorubicin (anthracycline), Oncovin/vincristine (vinca alkaloid) and "
    "prednisone (corticosteroid) — five different mechanisms and five different dose-limiting "
    "toxicities, which is why all five can be given together at full dose.",
    "If two drugs damage the same organ, you have to lower the dose of both, and a lower dose kills "
    "less cancer. Pick drugs that hurt different organs and each one can be given at full strength.",
    exim="fig_chemo_man",
    excap="The Chemo Man mnemonic from the lecture — each agent mapped onto the organ it damages, "
          "which is how non-overlapping toxicity is chosen in practice.",
)

q(
    "A 52-year-old woman undergoes complete resection of a breast carcinoma. Imaging shows no "
    "residual or metastatic disease. She is nonetheless offered chemotherapy. Which of the following "
    "best explains the rationale for treating her?",
    {
        "Chemotherapy kills a constant fraction of cells, so undetectable disease still requires "
        "treatment": "",
        "Chemotherapy kills a constant number of cells, so a small burden can be eradicated in a "
        "single cycle":
            "This inverts the kinetics. Cytotoxic agents follow first-order kinetics — a constant "
            "FRACTION, not a constant number — which is precisely why no single dose can ever sterilize "
            "a tumor.",
        "Chemotherapy given after resection is intended to shrink the tumor before surgery":
            "That describes NEOADJUVANT chemotherapy, which by definition is given before the local "
            "therapy. Chemotherapy after surgery is adjuvant — the prefix is the whole mnemonic.",
        "Resting cells in G0 are more susceptible to cytotoxic agents than cycling cells":
            "The opposite is true. Cells in G0 are LESS susceptible, and a large G0 fraction is a major "
            "reason slow-growing solid tumors resist cell cycle-specific drugs.",
        "Surgical resection converts the disease from primary to neoadjuvant chemotherapy":
            "These terms describe timing relative to local therapy, not a conversion. Primary "
            "chemotherapy is chemotherapy with no local treatment to be an adjuvant to.",
    },
    "Chemotherapy kills a constant fraction of cells, so undetectable disease still requires "
    "treatment",
    "This is the log-kill hypothesis and its most important clinical consequence.\n\n"
    "Cytotoxic agents follow first-order kinetics: each dose kills a constant FRACTION of the cells "
    "present, not a constant number. A drug taking the burden from 10⁸ to 10⁵ cells has produced a "
    "3-log kill. Because a fixed fraction of whatever remains always survives, no single dose can "
    "sterilize a tumor — repeated cycles are mathematically necessary, not merely conventional.\n\n"
    "The second number is the one that justifies her treatment. About 10⁹ cells — roughly 1 gram, the "
    "size of a small grape — is the smallest physically detectable burden, and roughly where symptoms "
    "begin. Everything below that line is subclinical disease that imaging cannot see. A 'complete' "
    "resection with normal imaging is therefore entirely compatible with 10⁸ residual cells, and "
    "treating those occult micrometastases is the whole point of adjuvant therapy.\n\n"
    "The vocabulary, since it turns on timing alone: NEOADJUVANT is given before the local therapy to "
    "shrink the tumor and make the operation smaller; ADJUVANT is given after it to reduce recurrence; "
    "PRIMARY chemotherapy is used where there is no local treatment for it to supplement.",
    "Each round of chemotherapy kills a set percentage of cancer cells, never a set number — so "
    "there is always a remainder. And a scan cannot see anything smaller than about a gram, so "
    "'all clear' still leaves millions of cells behind.",
    exim="fig_chemo_logkill",
    excap="Log-kill and treatment scheduling — tumor cell number on a logarithmic scale, showing the "
          "fractional fall with each cycle and the threshold of clinical detection.",
)

q(
    "A metastatic tumor initially responds to doxorubicin and then progresses. On re-biopsy and "
    "testing it is found to be resistant not only to doxorubicin but also to vincristine and "
    "etoposide — agents the tumor has never been exposed to and which are structurally unrelated to "
    "doxorubicin and to each other. Which of the following best explains this pattern?",
    {
        "Amplification of dihydrofolate reductase":
            "This would be the answer for resistance to methotrexate specifically. Altering or "
            "amplifying a target enzyme confers resistance to the drug that inhibits that enzyme — it "
            "cannot explain resistance to three drugs with three different targets.",
        "Increased expression of an adenosine triphosphate-dependent efflux pump": "",
        "Increased repair of deoxyribonucleic acid adducts and interstrand cross-links":
            "This is the resistance mechanism of alkylating agents and cisplatin. Vincristine and "
            "etoposide do not act by forming DNA adducts, so faster adduct repair would not protect "
            "against them.",
        "Loss of the enzyme that activates the prodrug":
            "Decreased prodrug activation explains resistance to the purine and pyrimidine "
            "antimetabolites — mercaptopurine, thioguanine, cytarabine, fluorouracil. None of the three "
            "drugs here is a prodrug of that kind.",
        "Sequestration of the tumor behind the blood-brain barrier":
            "This is pharmacologic sanctuary — the tumor sits where the drug cannot reach, classically "
            "the central nervous system or the testis. It is a site problem, and it would not produce "
            "an initial response followed by progression at the same site.",
    },
    "Increased expression of an adenosine triphosphate-dependent efflux pump",
    "This is multi-drug resistance, and every feature of the stem points to it.\n\n"
    "It is ACQUIRED resistance — the tumor responded and then stopped — as opposed to primary "
    "(inherent) resistance, where the tumor never responded at all. And it is CROSS-resistance: "
    "resistance to one agent conferring resistance to others, including structurally unrelated ones.\n\n"
    "The mechanism is increased expression of a normal gene, MDR1, which encodes the cell-surface "
    "P-glycoprotein — an ATP-dependent pump that exports drugs out of the cell. The P stands for "
    "'permeability.' Because the pump recognizes a broad range of hydrophobic substrates, one "
    "up-regulated gene defeats vincristine, vinblastine, doxorubicin, bleomycin and etoposide "
    "together: they all leave through the same door.\n\n"
    "Worth connecting to the anticoagulation block: the same transporter is behind the long list of "
    "interactions described as P-glycoprotein inhibitors and inducers — verapamil, amiodarone, "
    "clarithromycin, ketoconazole, rifampicin. One transporter, one job, many organs.",
    "The cancer cell has turned up a molecular bouncer in its membrane that throws drugs back out. "
    "The bouncer is not fussy about which drug, so beating one drug means beating several at once — "
    "even ones the tumor has never met.",
    exim="fig_chemo_pgp",
    excap="The P-glycoprotein transporter spanning the cell membrane, using adenosine triphosphate to "
          "export a broad range of hydrophobic drugs.",
)

q(
    "A slow-growing solid tumor with a large proportion of cells in the resting phase of the cell "
    "cycle responds poorly to methotrexate but responds to cyclophosphamide. Which of the following "
    "best explains the difference?",
    {
        "Cyclophosphamide alkylates deoxyribonucleic acid regardless of cell cycle phase": "",
        "Cyclophosphamide is a prodrug and methotrexate is not":
            "Cyclophosphamide is indeed activated by hepatic metabolism, but that concerns where it is "
            "activated rather than which cells it can kill. Loss of prodrug activation is a resistance "
            "mechanism of the antimetabolites, not an explanation of cell cycle behavior.",
        "Cyclophosphamide is not a substrate of P-glycoprotein":
            "Efflux is a mechanism of acquired multi-drug resistance in a previously responsive tumor. "
            "The stem describes a tumor whose resting fraction is the problem from the outset.",
        "Methotrexate is inactivated by leucovorin present within the tumor microenvironment":
            "Leucovorin is given deliberately as a rescue agent, supplying reduced folate downstream of "
            "the blocked enzyme. It is not endogenously produced by tumors, and it is an ENHANCER of "
            "5-fluorouracil — the same molecule with the opposite intent.",
        "Methotrexate is rapidly exported from the tumor across the blood-brain barrier":
            "Pharmacologic sanctuary describes a tumor sitting where the drug cannot reach. This tumor "
            "is accessible; the issue is what its cells are doing, not where they are.",
    },
    "Cyclophosphamide alkylates deoxyribonucleic acid regardless of cell cycle phase",
    "Cells in G0 — the resting phase — are less susceptible to cancer therapy, and that single fact "
    "is the reason cure is hard in slow-growing solid tumors.\n\n"
    "Cell cycle-SPECIFIC (CCS) drugs can only kill a cell that is currently cycling. Methotrexate "
    "acts in S phase, inhibiting dihydrofolate reductase and thymidylate synthase, so a cell that is "
    "not synthesizing DNA is simply not exposed to its mechanism. A tumor with a large G0 fraction is "
    "therefore intrinsically less responsive to it.\n\n"
    "Cell cycle-NONSPECIFIC (CCNS) agents have no such limitation. Alkylating agents, platinums and "
    "anthracyclines damage DNA whatever the cell is doing; the resting cell still carries the damage "
    "and dies when it next attempts to divide. That is why these agents remain the backbone of so "
    "many regimens.\n\n"
    "The phase map worth carrying: G1 — asparaginase. S — folate antagonists (methotrexate, "
    "pemetrexed), pyrimidine antagonists (5-fluorouracil, cytarabine, gemcitabine), purine antagonists "
    "(mercaptopurine, thioguanine, fludarabine). S/G2 — topoisomerase I inhibitors (irinotecan, "
    "topotecan). Late S/early G2 — topoisomerase II inhibitors (etoposide). G2 — bleomycin. M — "
    "taxanes and vinca alkaloids. CCNS — anthracyclines, alkylators, platinums.",
    "One drug only works on cells that are actively copying their DNA, so sleeping cells ignore it. "
    "The other damages the DNA of any cell, awake or asleep — the damage is waiting when the cell "
    "finally tries to divide.",
    exim="fig_chemo_cellcycle",
    excap="The cell cycle with the resting G0 compartment marked, and the phase at which each class "
          "of cytotoxic agent acts.",
)

q(
    "A 34-year-old man receives high-dose cyclophosphamide as part of a conditioning regimen. Thirty "
    "hours later he develops suprapubic discomfort and passes grossly bloody urine.\n\n"
    "Laboratory studies show:\n"
    "Creatinine 0.9 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Platelet count 165,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 12 seconds (N=11–15 seconds)\n\n"
    "Urinalysis shows too many erythrocytes to count, no casts and no organisms. Which of the "
    "following agents, given with the chemotherapy, would most likely have prevented this?",
    {
        "Allopurinol":
            "This would be the answer for prevention of tumor lysis syndrome, by reducing uric acid "
            "production. It does nothing for a urotoxic metabolite in the bladder.",
        "Dexrazoxane":
            "This is the rescue agent for ANTHRACYCLINES. It chelates intracellular iron so it cannot "
            "react with superoxide and hydrogen peroxide to generate free radicals, protecting cardiac "
            "muscle.",
        "Filgrastim":
            "Granulocyte colony-stimulating factor shortens the duration of neutropenia. It addresses "
            "the marrow toxicity of chemotherapy, not the bladder toxicity.",
        "Leucovorin":
            "This is the rescue agent for METHOTREXATE, supplying reduced folate downstream of the "
            "blocked dihydrofolate reductase. Note that the same molecule is an ENHANCER for "
            "5-fluorouracil — do not assume leucovorin means antidote.",
        "Mesna": "",
    },
    "Mesna",
    "Hemorrhagic cystitis, caused by acrolein — the urotoxic metabolite of cyclophosphamide and "
    "ifosfamide — concentrating in the bladder. Mesna (mercaptoethanesulfonate) binds acrolein in the "
    "urine and inactivates it; adequate hydration and frequent voiding reduce contact time. The "
    "toxicity and the prevention are identical for ifosfamide.\n\n"
    "Note what the laboratory panel rules out. A normal platelet count and a normal prothrombin time "
    "mean this is not chemotherapy-induced thrombocytopenia or a coagulopathy; the absence of "
    "organisms and casts argues against infection and against a glomerular source. The bleeding is "
    "local bladder mucosal injury.\n\n"
    "The three rescue agents to know as a set — each is an antidote given on purpose:\n"
    "• Leucovorin (folinic acid) rescues from methotrexate, bypassing the blocked dihydrofolate "
    "reductase in normal cells.\n"
    "• Mesna rescues from cyclophosphamide and ifosfamide by binding acrolein in the bladder.\n"
    "• Dexrazoxane rescues from anthracyclines by chelating intracellular iron, preventing free "
    "radical generation in cardiac muscle.",
    "The drug breaks down into a chemical that burns the lining of the bladder on its way out. Mesna "
    "is given alongside it purely to grab that chemical in the urine before it can do damage.",
)

q(
    "A 6-year-old with acute lymphoblastic leukemia is due to receive intrathecal methotrexate and "
    "intravenous vincristine on the same day. The pharmacy dispenses the vincristine in a 50-mL "
    "minibag rather than a syringe. Which of the following best explains this practice?",
    {
        "Intrathecal administration of vincristine is uniformly fatal": "",
        "Vincristine is a vesicant that requires dilution before peripheral infusion":
            "Vincristine is a vesicant and extravasation is a genuine problem, but that hazard is "
            "managed by central access and careful administration. It is not the reason the drug is "
            "kept out of a syringe.",
        "Vincristine is inactivated by contact with cerebrospinal fluid":
            "The opposite is the problem — it is not inactivated, it is devastatingly active in the "
            "central nervous system. Inactivation would make the error harmless.",
        "Vincristine must be given slowly because it causes cytokine release syndrome":
            "Cytokine release syndrome is a toxicity of T-cell engagers and chimeric antigen receptor "
            "T-cell therapy, not of vinca alkaloids. Vincristine's characteristic toxicity is "
            "peripheral neuropathy.",
        "Vincristine precipitates when mixed with methotrexate in the same line":
            "Physical incompatibility between agents is a real pharmaceutical consideration, but it is "
            "managed by flushing lines and separating administrations, not by changing the container "
            "the drug arrives in.",
    },
    "Intrathecal administration of vincristine is uniformly fatal",
    "Intrathecal vincristine causes an ascending myeloencephalopathy and is uniformly fatal. This is "
    "a named, absolute rule with no exceptions, and it is the reason most institutions dispense "
    "vincristine in a minibag: a minibag cannot be connected to a spinal needle, so the error is made "
    "physically impossible rather than merely forbidden.\n\n"
    "The setting in this stem is exactly where the error historically occurs — a patient receiving an "
    "intrathecal agent (methotrexate, which is correctly given that way) and an intravenous vinca on "
    "the same day, with two syringes on one tray.\n\n"
    "While you are here, the mechanism contrast that gets tested alongside it. Taxanes and vincas both "
    "act on microtubules in M phase, and their effects on tubulin are opposite: paclitaxel PROMOTES "
    "microtubule formation and prevents disassembly, freezing the cell in metaphase; vincristine "
    "BLOCKS assembly of tubulin dimers, so the spindle dissolves. Both end in mitotic arrest. "
    "(Ixabepilone behaves like the taxanes, eribulin like the vincas, with less neuropathy.)",
    "Given into a vein this drug treats leukemia; given into the spine it destroys the spinal cord "
    "and always kills. Hospitals therefore put it in a bag that physically cannot attach to a spinal "
    "needle.",
    exim="fig_chemo_microtubule",
    excap="Normal mitosis contrasted with mitotic arrest — the taxanes stabilize microtubules and "
          "prevent disassembly, the vinca alkaloids block tubulin assembly.",
)

q(
    "A 58-year-old woman begins chemotherapy for metastatic colon cancer. During the first infusion "
    "she notices a metallic taste. Two days later she reports that drinking cold water makes her "
    "throat feel as though it is closing, and that holding a cold drink causes painful tingling in "
    "her fingers. She has no rash, no wheeze and no hypotension. Which of the following agents is "
    "most likely responsible?",
    {
        "Carboplatin":
            "Carboplatin trades cisplatin's organ toxicity for marrow toxicity — less nephrotoxicity, "
            "ototoxicity, neuropathy and vomiting, at the cost of more myelosuppression. Cold-induced "
            "symptoms are not its signature.",
        "Cisplatin":
            "Cisplatin is the highly emetogenic, nephrotoxic and ototoxic platinum, and it does cause a "
            "peripheral neuropathy — but a cumulative, dose-dependent sensory one, not a cold-triggered "
            "pharyngolaryngeal syndrome.",
        "Cyclophosphamide":
            "Its distinguishing toxicity is hemorrhagic cystitis from acrolein, prevented with mesna. "
            "Like all alkylators it also carries myelosuppression, mucositis and a secondary malignancy "
            "risk.",
        "Irinotecan":
            "This topoisomerase I inhibitor is used in colorectal cancer and causes both acute "
            "cholinergic diarrhea and delayed diarrhea. Neither is cold-triggered.",
        "Oxaliplatin": "",
    },
    "Oxaliplatin",
    "Pharyngolaryngeal dysesthesia and cold-induced peripheral neuropathy are specific to oxaliplatin "
    "among the three platinums. Patients describe choking on cold air or cold drinks. The absence of "
    "rash, wheeze and hypotension is the buried clue: this is a NEUROTOXIC phenomenon, not an allergic "
    "one, so patients are counselled to avoid cold food, drinks and air rather than being "
    "desensitized or switched.\n\n"
    "A separate delayed hypersensitivity reaction is shared by all three platinums, along with the "
    "metallic taste during infusion and longer-term taste changes — so the metallic taste in this stem "
    "localizes the class but not the drug.\n\n"
    "The platinum trade-off in one line: carboplatin trades cisplatin's organ toxicity for marrow "
    "toxicity. Everything cisplatin does to the kidney, the ear, the nerve and the vomiting centre, "
    "carboplatin does less of — and pays for it with more myelosuppression. Oxaliplatin is the odd one "
    "out, with cold-induced neuropathy as its signature.",
    "Cold sets off this particular drug's nerve toxicity — a cold drink makes the throat feel like it "
    "is closing. It looks alarming but it is not an allergy, so the advice is simply to avoid cold "
    "things.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §45 — Targeted therapy and immunotherapy (LO 11, 16)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A pharmacology student notices that every agent in the signal transduction inhibitor group — "
    "those targeting BCR-ABL, RAF, MEK, mTOR, Bruton tyrosine kinase, PARP, PI3K and CDK4/6 — is a "
    "small molecule, while the agents targeting HER2, EGFR and VEGFR include both small molecules and "
    "monoclonal antibodies. Which of the following best explains this?",
    {
        "A monoclonal antibody cannot cross the plasma membrane": "",
        "Monoclonal antibodies are cleared too rapidly to inhibit an intracellular enzyme":
            "The opposite is true of their pharmacokinetics — IgG1, IgG2 and IgG4 antibodies have "
            "half-lives of about 21 days, far longer than any small molecule. Duration is not the "
            "limitation.",
        "Monoclonal antibodies cannot be engineered against enzymes, only against receptors":
            "Antibodies are raised against a wide variety of protein targets including enzymes. The "
            "constraint is anatomic access, not the class of protein.",
        "Signal transduction targets are expressed only on normal cells":
            "They are expressed on tumor cells — that is why they are drug targets. Their expression "
            "on normal cells is what generates the toxicity, not what prevents antibody binding.",
        "Small molecules trigger complement-dependent cytotoxicity more effectively":
            "Effector functions such as complement-dependent cytotoxicity and antibody-dependent "
            "cellular cytotoxicity belong to ANTIBODIES, specifically IgG1. Small molecules have no "
            "such mechanism.",
    },
    "A monoclonal antibody cannot cross the plasma membrane",
    "Size decides where a drug can act, and it settles this entire classification in one fact. A "
    "monoclonal antibody is roughly 145,000 daltons; a tyrosine kinase inhibitor is a few hundred.\n\n"
    "• Antibodies can only engage the OUTSIDE of the cell — the extracellular domain of a "
    "transmembrane receptor. That is why HER2, EGFR and VEGFR, all of which have extracellular "
    "domains, can be hit by either format.\n"
    "• Small molecules cross the membrane and reach intracellular kinases.\n"
    "• BCR-ABL, RAF, MEK, mTOR, Bruton tyrosine kinase, PARP, PI3K and CDK4/6 all sit inside the "
    "cell. Therefore every signal transduction inhibitor is a small molecule — there are no antibodies "
    "in that group, and there cannot be.\n\n"
    "The format also predicts the toxicity family, which is worth more than the classification "
    "itself. Small molecule → pharmacokinetic problems (CYP3A4 interactions, food effects, most taken "
    "on an empty stomach) plus off-target kinase effects — QT prolongation, raised liver function "
    "tests and diarrhea appear again and again, and multi-kinase inhibitors have more adverse "
    "reactions because hitting more kinases means hitting more normal tissue. Antibody → immunologic "
    "and on-target problems: infusion reactions, and mechanism-based toxicity in whatever normal "
    "tissue expresses the antigen.",
    "Antibodies are enormous proteins that cannot get through the cell wall, so they can only grab "
    "things sticking out of the surface. Anything inside the cell has to be hit by a drug small "
    "enough to slip in.",
    exim="fig_chemo_size",
    excap="Molecular sizes compared — a small-molecule drug against a monoclonal antibody, drawn to "
          "scale.",
)

q(
    "A 54-year-old woman with HER2-positive breast cancer has completed four cycles of doxorubicin "
    "and cyclophosphamide and is now receiving trastuzumab. She reports 2 weeks of exertional "
    "dyspnea and orthopnea. Examination shows bibasilar crackles and an elevated jugular venous "
    "pressure. Echocardiography shows a left ventricular ejection fraction of 38%, reduced from 62% "
    "at baseline. Which of the following best explains why this agent produces this toxicity?",
    {
        "Its payload is an anti-microtubule agent released in cardiac tissue":
            "Trastuzumab is a naked antibody, not an antibody-drug conjugate. Ado-trastuzumab emtansine "
            "is the conjugate carrying an anti-microtubule payload, and its toxicities are neutropenia "
            "and neuropathy rather than heart failure.",
        "It chelates intracellular iron within cardiac myocytes":
            "That describes dexrazoxane, the rescue agent given to PREVENT anthracycline "
            "cardiotoxicity. Iron-catalyzed free radical generation is the anthracycline mechanism, not "
            "the antibody's.",
        "It generates free radicals through redox cycling of a quinone ring":
            "This is the mechanism of the anthracyclines, which is why doxorubicin also sits on the "
            "cardiotoxicity list. The question asks about the targeted agent.",
        "It inhibits vascular endothelial growth factor signaling, causing hypertension and "
        "cardiomyopathy":
            "VEGF pathway inhibitors do cause hypertension, thrombosis, bleeding, impaired wound "
            "healing and gastrointestinal perforation. Trastuzumab does not target that pathway.",
        "The receptor it blocks is also expressed on cardiomyocytes": "",
    },
    "The receptor it blocks is also expressed on cardiomyocytes",
    "HER2 is expressed on cardiac myocytes, where it participates in survival signaling. Block it and "
    "you damage the heart. Trastuzumab is the only targeted agent on the cardiotoxicity list "
    "alongside doxorubicin and daunorubicin, and the reason is anatomic rather than chemical.\n\n"
    "This is the cleanest illustration of the governing principle of the whole block: "
    "targeted-therapy toxicity follows the target's NORMAL TISSUE DISTRIBUTION, not the mitotic rate. "
    "Traditional cytotoxic chemotherapy damages whatever divides fastest — marrow, gut lining, hair "
    "follicles. A targeted agent damages wherever its target normally lives.\n\n"
    "The same logic explains the rest of the table. EGFR inhibitors cause an acne-like rash because "
    "EGFR is highly expressed in normal skin. PI3K inhibitors cause autoimmune dysfunction and "
    "opportunistic infections because PI3Kδ is a lymphocyte signaling node. mTOR inhibitors cause "
    "glucose and lipid dysregulation because mTOR is the cell's nutrient sensor.\n\n"
    "Note the sequence in this stem: an anthracycline followed by trastuzumab stacks two "
    "cardiotoxicities, which is why ejection fraction is monitored through HER2-directed therapy.",
    "The drug targets a receptor that breast cancer cells overuse — but heart muscle cells use the "
    "same receptor to stay healthy. Blocking it everywhere weakens the heart as well as the tumor.",
)

q(
    "Two antibody-drug conjugates directed at HER2 are used in metastatic breast cancer. Patients "
    "receiving the first develop prominent peripheral sensory neuropathy and thrombocytopenia; "
    "patients receiving the second develop prominent neutropenia, anemia, nausea and diarrhea. Both "
    "antibodies bind the same receptor with similar affinity. Which of the following best explains "
    "the difference in toxicity?",
    {
        "One antibody is humanized and the other is fully human":
            "The nomenclature suffix does describe antibody origin — -omab murine, -ximab chimeric, "
            "-zumab humanized, -umab fully human — and it predicts immunogenicity. It does not predict "
            "neuropathy versus myelosuppression.",
        "One antibody is IgG1 and the other is IgG4":
            "Subclass matters for effector function: IgG1 triggers potent complement-dependent and "
            "antibody-dependent cellular cytotoxicity, while IgG4 cannot activate classical complement "
            "at all — which is why IgG4 is chosen for checkpoint inhibitors. It does not generate these "
            "toxicity profiles.",
        "One conjugate is internalized and the other acts at the cell surface":
            "Antibody-drug conjugates must be internalized to release their payload; that is how the "
            "class works. Differing internalization would change potency, not the pattern of organ "
            "toxicity.",
        "The conjugates carry payloads from different drug classes": "",
        "The two tumors express different levels of HER2":
            "Receptor density affects how much drug is delivered and therefore how well the drug works. "
            "It would scale toxicity up or down rather than changing its character from neurologic to "
            "hematologic.",
    },
    "The conjugates carry payloads from different drug classes",
    "The antibody determines where the drug goes; the PAYLOAD determines what the toxicity looks "
    "like. Two conjugates can share a target and still behave like two different chemotherapies.\n\n"
    "• Trastuzumab emtansine carries emtansine, an anti-microtubule agent — hence peripheral "
    "neuropathy, with thrombocytopenia and raised transaminases.\n"
    "• Trastuzumab deruxtecan carries deruxtecan, a topoisomerase inhibitor — hence neutropenia, "
    "anemia, thrombocytopenia, nausea, diarrhea, fatigue and alopecia.\n\n"
    "You can read the payload straight out of the generic name, which is the practical exam skill "
    "here. The second word names the payload: -emtansine and -vedotin are anti-microtubule agents, so "
    "expect peripheral neuropathy; -deruxtecan and -govitecan are topoisomerase inhibitors, so expect "
    "myelosuppression and gastrointestinal toxicity.\n\n"
    "Applied to the rest of the list: polatuzumab VEDOTIN (CD79b) and enfortumab VEDOTIN (nectin-4) "
    "both cause neuropathy; sacituzumab GOVITECAN (TROP2) causes neutropenia, anemia, nausea and "
    "diarrhea.",
    "These drugs are a guided missile: the antibody is the guidance, the chemotherapy strapped to it "
    "is the warhead. Same guidance, different warhead — so the collateral damage looks completely "
    "different.",
    exim="fig_chemo_adc",
    excap="Structure of an antibody-drug conjugate — the targeting antibody, the linker, and the "
          "cytotoxic payload.",
)

q(
    "A 63-year-old man with metastatic colorectal cancer begins cetuximab. Three weeks later he has a "
    "florid papulopustular eruption over the face, scalp and upper trunk. He is afebrile, has no "
    "mucosal involvement, no wheeze and no hypotension, and the rash began between infusions rather "
    "than during one. Which of the following is the most accurate characterization of this finding?",
    {
        "A delayed type IV hypersensitivity reaction to the murine portion of the antibody":
            "Cetuximab is chimeric (-ximab), so it does carry a murine variable region and can cause "
            "hypersensitivity — but that presents as an INFUSION reaction, during or shortly after "
            "administration, not as a papulopustular eruption appearing between cycles.",
        "An infusion-related reaction requiring premedication before the next dose":
            "Infusion reactions occur during or within hours of administration and involve fever, "
            "rigors, bronchospasm or hypotension. This rash began between infusions and has none of "
            "those features.",
        "An on-target effect on a receptor normally expressed in skin": "",
        "An opportunistic infection resulting from antibody-induced immunosuppression":
            "The rare devastating infectious complication associated with a few monoclonal antibodies "
            "is progressive multifocal leukoencephalopathy from JC virus reactivation — a neurologic, "
            "not a cutaneous, problem.",
        "A paradoxical activation of mitogen-activated protein kinase signaling in keratinocytes":
            "This is the mechanism of the squamous skin cancers seen with RAF and MEK inhibitors, in "
            "RAS-mutant keratinocytes. It produces keratoacanthomas and squamous carcinomas, not an "
            "acneiform rash.",
    },
    "An on-target effect on a receptor normally expressed in skin",
    "The epidermal growth factor receptor is highly expressed in normal skin, so blocking it produces "
    "the characteristic acne-like rash. This is mechanism-based, on-target toxicity — not an allergy — "
    "and it occurs with both formats: the small molecules (erlotinib, gefitinib, afatinib, "
    "osimertinib) and the antibodies (cetuximab, panitumumab, necitumumab).\n\n"
    "The timing and the negatives in the stem are what separate the two answers a hurried reader "
    "chooses between. An infusion reaction is the ANTIBODY-specific toxicity and happens during or "
    "just after the infusion, with systemic features. An on-target rash appears over weeks and carries "
    "none of them.\n\n"
    "The clinical consequence is that the rash is managed rather than avoided — it is not a reason to "
    "stop a working drug, and across EGFR-targeted therapy its appearance has been associated with "
    "response. The shared EGFR toxicity set also includes diarrhea and pneumonitis, in both "
    "formats.\n\n"
    "This generalizes: when an antibody produces a rash, ask where its target normally lives before "
    "calling it an allergy.",
    "The drug blocks a signal that skin cells need just as much as the tumor does, so the skin "
    "reacts. It looks like an allergic rash but it is the drug working exactly as designed, in the "
    "wrong place.",
)

q(
    "A 47-year-old man with relapsed B-cell lymphoma receives the second step-up dose of a bispecific "
    "T-cell engager. Nine hours later he develops a temperature of 39.4°C, blood pressure 82/50 mm "
    "Hg, and oxygen saturation 88% on room air. He is alert and fully oriented. Which of the "
    "following is the most appropriate specific treatment?",
    {
        "Diphenhydramine and acetaminophen":
            "These are premedications for an infusion-related reaction, which occurs within the first 6 "
            "hours and is generally AFEBRILE. They will not treat an interleukin-6-driven syndrome with "
            "hypotension and hypoxia.",
        "Loperamide":
            "This is the wrong organ and the wrong mechanism. Note also that checkpoint inhibitor "
            "colitis is autoimmune inflammation needing corticosteroids rather than an antimotility "
            "agent.",
        "Tocilizumab": "",
        "Broad-spectrum antibiotics alone":
            "Empiric antibiotics are entirely reasonable while sepsis is excluded in a febrile "
            "immunosuppressed patient, but they are not the specific treatment for this syndrome and "
            "would leave the driving mechanism untreated.",
        "Dexamethasone with a non-sedating anticonvulsant":
            "This is the treatment for ICANS — immune effector cell-associated neurotoxicity syndrome — "
            "which appears 3–9 days after infusion with confusion, speech difficulty, behavior change "
            "or seizure. He is alert and fully oriented.",
    },
    "Tocilizumab",
    "Cytokine release syndrome — the most common reaction to a T-cell engager or chimeric antigen "
    "receptor T-cell therapy. The syndrome is fever, hypotension and hypoxia, and it is driven by "
    "interleukin-6, so the specific treatment is tocilizumab, an anti-interleukin-6 receptor antibody, "
    "with corticosteroids and vasopressors in severe cases.\n\n"
    "Two features of the stem separate it from an infusion reaction. Timing: cytokine release syndrome "
    "typically appears 4–16 hours after a dose, whereas an infusion reaction occurs within the first 6 "
    "hours. Fever: an infusion reaction is generally afebrile. The step-up dosing period is also "
    "exactly when cytokine release syndrome is expected, because these toxicities are largely confined "
    "to the first administrations.\n\n"
    "T-cell engager toxicity behaves quite differently from checkpoint inhibitor toxicity, and the "
    "contrast is worth holding: engager reactions are highly dose-related, follow a constant profile, "
    "are confined mainly to cytokine release syndrome and neurologic events, occur during or just "
    "after step-up dosing, and are quite predictable. Checkpoint toxicities are unrelated to dose "
    "intensity, highly variable, can affect any organ, appear at any time — even after therapy ends — "
    "and are largely unpredictable.",
    "His immune system has been switched on so hard that the resulting chemical storm drops his blood "
    "pressure and oxygen. One chemical, interleukin-6, drives it, and there is an antibody that blocks "
    "exactly that.",
    exim="fig_chemo_irae_tce",
    excap="Adverse-event profiles compared — immune checkpoint inhibitors against T-cell engagers, by "
          "dose relationship, variability, organs affected, time course and predictability.",
)

q(
    "A 39-year-old woman received a chimeric antigen receptor T-cell infusion 6 days ago. She had "
    "fever and hypotension on day 1 that resolved with treatment. She is now afebrile and "
    "normotensive, but over 12 hours has become confused, cannot name common objects, and has had a "
    "witnessed generalized seizure. Which of the following is the most appropriate treatment?",
    {
        "Dexamethasone and levetiracetam": "",
        "Intravenous immunoglobulin":
            "This is used for hypogammaglobulinemia after B-cell-directed therapy, to reduce infection "
            "risk. It has no role in acute neurotoxicity.",
        "Lorazepam infusion and intubation for airway protection":
            "Sedation is specifically avoided where possible, because it obscures the serial "
            "neurologic assessment on which grading and management depend. A non-sedating anticonvulsant "
            "is preferred.",
        "Mannitol and hypertonic saline":
            "These treat raised intracranial pressure from a mass lesion or cerebral edema of another "
            "cause. The mechanism here is blood-brain barrier and endothelial disturbance, treated with "
            "a corticosteroid that penetrates the central nervous system.",
        "Tocilizumab":
            "This is the specific treatment for cytokine release syndrome, which she had on day 1 and "
            "which has resolved. Neurotoxicity is not an interleukin-6 storm, so tocilizumab is not the "
            "answer here.",
    },
    "Dexamethasone and levetiracetam",
    "ICANS — immune effector cell-associated neurotoxicity syndrome — occurring 3 to 9 days after "
    "infusion, which is the classic window. The features are speech difficulty (often the earliest, "
    "as here), confusion, behavior change, headache and seizure.\n\n"
    "The key mechanistic point is that ICANS is NOT an interleukin-6 storm. The pathophysiology is "
    "endothelial activation and blood-brain barrier disturbance, so tocilizumab — which is the right "
    "answer for cytokine release syndrome — is the wrong answer here. Two syndromes, same therapy, "
    "different mechanisms, different drugs.\n\n"
    "Two deliberate choices in the treatment. Dexamethasone is chosen among corticosteroids because it "
    "penetrates the central nervous system. And the anticonvulsant must be NON-SEDATING, because "
    "sedation would obscure the neurologic assessment that grading and escalation depend on.\n\n"
    "The sequence in this patient is typical: cytokine release syndrome first, in the first day or "
    "two, then neurotoxicity later in the first week, often after the fever has settled. Do not let "
    "the resolution of the first syndrome reassure you about the second.",
    "A week after the treated cells were infused, the barrier protecting her brain has become leaky "
    "and she is confused and seizing. The antibody used for the earlier fever does not reach this "
    "problem — a steroid that gets into the brain does.",
)

q(
    "A 61-year-old man with metastatic melanoma has received three cycles of nivolumab. He reports 10 "
    "days of watery diarrhea, now six to eight stools daily with intermittent blood and abdominal "
    "cramping. He is afebrile. Stool studies including Clostridioides difficile testing are negative. "
    "Colonoscopy shows diffuse erythema, loss of vascular pattern and superficial ulceration. Which "
    "of the following is the most appropriate treatment?",
    {
        "Corticosteroids": "",
        "Infliximab as first-line therapy":
            "Anti-tumor necrosis factor therapy is reserved for immune-mediated colitis that is "
            "refractory to corticosteroids. It is an escalation, not a starting point.",
        "Loperamide":
            "This is the intuitive answer and it is the named trap. Checkpoint colitis is autoimmune "
            "inflammation, not a motility problem, and an antimotility agent treats none of the "
            "underlying process while risking toxic megacolon.",
        "Oral vancomycin":
            "This would be the answer for Clostridioides difficile colitis, which the stem has "
            "explicitly excluded.",
        "Tocilizumab":
            "This is the specific treatment for cytokine release syndrome after a T-cell engager or "
            "chimeric antigen receptor T-cell infusion — an interleukin-6-driven syndrome of fever, "
            "hypotension and hypoxia.",
    },
    "Corticosteroids",
    "Immune-mediated colitis, and the treatment follows directly from the mechanism. Checkpoint "
    "inhibitors work by removing the brakes that maintain self-tolerance, so the predictable cost is "
    "autoimmunity. The treatment for a serious immune-related adverse event is therefore to put a "
    "brake back on — corticosteroids.\n\n"
    "The trap named in the lecture is loperamide: checkpoint colitis is autoimmune inflammation "
    "needing steroids, not a motility problem. The colonoscopic findings here — diffuse erythema, loss "
    "of vascular pattern, superficial ulceration — are inflammatory bowel disease in appearance, which "
    "is the point.\n\n"
    "The shorthand for the whole toxicity family is 'any organ ending in -itis,' across eight "
    "systems: colitis, rash, pneumonitis, hepatitis, musculoskeletal (arthritis, myositis), "
    "endocrinopathies (thyroiditis, hypophysitis, adrenal insufficiency, new diabetes — often "
    "permanent), ophthalmologic (uveitis) and neurologic.\n\n"
    "The checkpoints themselves: CTLA-4 downregulates T-cell function and is blocked by ipilimumab "
    "and tremelimumab; PD-1 limits autoimmunity in peripheral tissues and is the major immune "
    "resistance mechanism in tumors, blocked by pembrolizumab, nivolumab, cemiplimab and dostarlimab; "
    "PD-L1 is the tumor-side ligand, blocked by atezolizumab, avelumab and durvalumab; LAG-3 is "
    "blocked by relatlimab, given with nivolumab in a single infusion.",
    "The drug works by taking the safety catch off his immune system so it will attack the melanoma. "
    "The price is that it also attacks his bowel — so the fix is to put a safety catch back on with "
    "steroids.",
    exim="fig_chemo_checkpoint",
    excap="Mechanism of immune checkpoint inhibition — an antigen-presenting cell engaging a T cell, "
          "with the inhibitory checkpoints that the antibodies block.",
)

q(
    "A 68-year-old man with newly diagnosed multiple myeloma is scheduled to begin daratumumab. The "
    "blood bank reports that his antibody screen, previously negative, is now positive against every "
    "panel cell tested, while his direct antiglobulin test is positive for IgG. He has no evidence of "
    "hemolysis. Which of the following best explains this finding?",
    {
        "An anamnestic response to a previously encountered red blood cell alloantigen":
            "A delayed serologic or hemolytic transfusion reaction from anti-Jka or a similar "
            "alloantibody gives a positive screen against SOME panel cells — the ones bearing that "
            "antigen. A panreactive result against every cell is a different pattern.",
        "Development of warm autoimmune hemolytic anemia":
            "This would give a positive direct antiglobulin test with a panreactive screen — but also "
            "hemolysis: a raised reticulocyte count, raised lactate dehydrogenase, low haptoglobin and "
            "an unconjugated hyperbilirubinemia. He has none.",
        "Paraprotein interference causing rouleaux formation":
            "A high paraprotein does cause rouleaux on the smear and can raise the erythrocyte "
            "sedimentation rate, and it may interfere with some assays. It does not produce a positive "
            "direct antiglobulin test against panel cells.",
        "The antibody binds an antigen expressed on the patient's red blood cells": "",
        "The antibody has caused a cold agglutinin to develop":
            "Cold agglutinin disease is a feature of lymphoplasmacytic lymphoma with its pentameric "
            "IgM paraprotein, and it produces IgM-mediated, complement-fixing agglutination at low "
            "temperatures — a different serologic pattern.",
    },
    "The antibody binds an antigen expressed on the patient's red blood cells",
    "CD38 is not confined to plasma cells — it is also expressed on red blood cells. Daratumumab, an "
    "anti-CD38 antibody, therefore coats the patient's erythrocytes and every reagent red cell in the "
    "panel, producing a panreactive indirect antiglobulin test and a positive direct antiglobulin "
    "test without any hemolysis.\n\n"
    "Why this matters clinically: the panreactivity can MASK a genuine alloantibody. A real anti-Jka "
    "or anti-E sitting underneath a daratumumab-driven pan-positive screen is invisible, and the "
    "patient could be transfused with incompatible units.\n\n"
    "The practical rule: tell the blood bank before the first dose, and obtain a baseline type and "
    "screen plus an extended red cell phenotype or genotype while the serology is still "
    "interpretable. Laboratories also treat panel cells with dithiothreitol, which denatures CD38 and "
    "removes the interference — at the cost of destroying the Kell antigens, so Kell-negative units "
    "are then given.\n\n"
    "This is the same principle as every other targeted-therapy toxicity in this section: the effect "
    "follows the target's normal tissue distribution. Here the affected tissue is the red cell, and "
    "the 'toxicity' shows up in the transfusion laboratory rather than in the patient.",
    "The myeloma drug sticks to a marker that is also on normal red cells, so every compatibility "
    "test comes back positive. The danger is not the drug — it is that a real incompatibility could "
    "now be hiding behind the false one.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §46 — Hormonal therapy (LO 15)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 44-year-old premenopausal woman with estrogen receptor-positive breast cancer is started on "
    "anastrozole alone as adjuvant endocrine therapy. Which of the following best explains why this "
    "plan is inappropriate?",
    {
        "Aromatase inhibitors are agonists at the endometrial estrogen receptor":
            "That describes tamoxifen, a selective estrogen receptor modulator — antagonist in breast "
            "but agonist in endometrium, which is why it raises endometrial cancer risk. Aromatase "
            "inhibitors have no agonist activity anywhere.",
        "Aromatase inhibitors cause tumor flare during the first weeks of therapy":
            "Tumor flare is the toxicity of a GnRH agonist such as leuprolide, caused by the initial "
            "surge in luteinizing hormone and follicle-stimulating hormone before the axis is "
            "downregulated.",
        "Aromatase inhibitors protect bone, which is undesirable in a premenopausal woman":
            "Both halves are wrong. Aromatase inhibitors cause osteoporosis; it is the SERMs that "
            "protect bone, through estrogen agonism in that tissue.",
        "Her ovaries still produce estrogen directly": "",
        "Her tumor must be HER2-positive before endocrine therapy can be used":
            "HER2 status directs HER2-targeted therapy such as trastuzumab. It is estrogen receptor "
            "positivity that makes endocrine therapy appropriate, and hers is positive.",
    },
    "Her ovaries still produce estrogen directly",
    "Aromatase inhibitors are for POSTMENOPAUSAL women. They work by blocking the peripheral "
    "conversion of androgenic precursors to estrogens — the route that dominates after menopause.\n\n"
    "In a premenopausal woman the ovary makes estrogen directly, and there is far more of it than "
    "peripheral aromatization accounts for. Blocking aromatase therefore cannot suppress estrogen "
    "adequately, and may even trigger a compensatory rise in gonadotropins that drives the ovary "
    "harder.\n\n"
    "The appropriate options are tamoxifen, which is effective regardless of menopausal status, or "
    "ovarian suppression with a GnRH agonist — leuprolide, goserelin or triptorelin — with an "
    "aromatase inhibitor added afterwards, once the ovarian source has been shut down.\n\n"
    "The pathway is worth drawing once: adrenal cortex → androgens → [AROMATASE: blocked by "
    "anastrozole, letrozole, exemestane] → estrogens → [RECEPTOR: blocked by tamoxifen, fulvestrant] "
    "→ tumor growth. Aromatase inhibitors deplete the hormone upstream; SERMs and fulvestrant block "
    "the receptor downstream.",
    "This drug only shuts off the small side-route that makes estrogen after menopause. Her ovaries "
    "are still running the main factory, so blocking the side-route achieves almost nothing.",
    exim="fig_chemo_antiestrogen",
    excap="Anti-estrogen mechanisms — the aromatase step upstream and the estrogen receptor "
          "downstream, with the drug class acting at each.",
)

q(
    "Two postmenopausal women with estrogen receptor-positive breast cancer are seen in follow-up. "
    "One, taking tamoxifen for 4 years, reports vaginal bleeding; her bone density is unchanged from "
    "baseline. The other, taking anastrozole for 4 years, reports hot flashes and diffuse joint "
    "aches; dual-energy radiographic absorptiometry now shows osteoporosis. Which of the following "
    "best explains this divergence?",
    {
        "Anastrozole promotes degradation of the estrogen receptor in bone":
            "That is the mechanism of FULVESTRANT, a pure antiestrogen that inhibits receptor "
            "dimerization and promotes receptor degradation. Aromatase inhibitors act on the enzyme, "
            "not the receptor.",
        "Anastrozole is a partial agonist at the endometrial receptor and an antagonist in bone":
            "This assigns tamoxifen's mixed agonist-antagonist behavior to the wrong drug, and reverses "
            "the tissues. Aromatase inhibitors have no agonist activity in any tissue.",
        "Tamoxifen acts as an estrogen agonist in bone and endometrium": "",
        "Tamoxifen increases circulating estrogen by blocking aromatase":
            "Tamoxifen does not touch aromatase; it competes at the receptor. The aromatase inhibitors "
            "are anastrozole, letrozole and exemestane.",
        "Tamoxifen is metabolized to an aromatase inhibitor in postmenopausal women":
            "Tamoxifen requires CYP2D6 activation to endoxifen, but endoxifen is a more potent receptor "
            "antagonist, not an aromatase inhibitor. The two classes act at different points on one "
            "pathway.",
    },
    "Tamoxifen acts as an estrogen agonist in bone and endometrium",
    "Bone is the giveaway, and it lets you name the class from a single finding.\n\n"
    "A selective estrogen receptor modulator does exactly what its name says — it modulates rather "
    "than simply blocks, with agonist and antagonist effects in different tissues. Tamoxifen is an "
    "ANTAGONIST in breast (the therapeutic effect), and an AGONIST in bone and endometrium. Agonism in "
    "bone preserves bone mineral density; agonism in endometrium drives proliferation and raises "
    "endometrial cancer risk, which is what postmenopausal bleeding on tamoxifen must be investigated "
    "for. Tamoxifen additionally carries thromboembolic risk, plus vaginal dryness and discharge.\n\n"
    "An aromatase inhibitor removes estrogen from EVERY tissue. There is therefore no endometrial "
    "agonist effect — and, for exactly the same reason, no bone protection. Its toxicity set is "
    "osteoporosis, hot flashes and arthralgias.\n\n"
    "SERMs protect bone; aromatase inhibitors destroy it. Give the bone finding and you can name the "
    "class.",
    "One drug pretends to be estrogen in some tissues and blocks it in others — good for bones, bad "
    "for the womb lining. The other simply removes estrogen everywhere — so the womb is safe and the "
    "bones crumble.",
)

q(
    "A 72-year-old man with metastatic prostate cancer and known vertebral metastases is started on "
    "leuprolide as a single agent. Twelve days later he develops severe mid-back pain, bilateral leg "
    "weakness and urinary retention. Which of the following best explains this deterioration?",
    {
        "An initial rise in luteinizing hormone and testosterone": "",
        "A hypersensitivity reaction to the depot vehicle":
            "Injection-site reactions occur with depot formulations, but they are local. They do not "
            "produce cord compression at a site of known metastatic disease.",
        "Inhibition of CYP17 causing mineralocorticoid excess":
            "That is abiraterone, whose blockade of androgen biosynthesis shunts precursors down the "
            "mineralocorticoid pathway, giving hypokalemia, fluid retention and hypertension — and why "
            "it is co-prescribed with prednisone.",
        "Osteoporotic vertebral collapse from androgen deprivation":
            "Decreased bone mineral density is a genuine long-term toxicity of GnRH agonists, together "
            "with hot flashes and sexual dysfunction. It develops over months to years, not within two "
            "weeks.",
        "Rapid tumor lysis with deposition of urate in the spinal canal":
            "Tumor lysis syndrome follows treatment of a rapidly proliferating hematologic malignancy "
            "and causes hyperkalemia, hyperphosphatemia, hyperuricemia, hypocalcemia and acute kidney "
            "injury — not a compressive myelopathy.",
    },
    "An initial rise in luteinizing hormone and testosterone",
    "Tumor flare. A GnRH (LHRH) agonist binds the LHRH receptors on pituitary gonadotropes and — "
    "counterintuitively for a drug whose purpose is androgen deprivation — INITIALLY stimulates them. "
    "Luteinizing hormone and follicle-stimulating hormone surge, testosterone rises, and only with "
    "continuous stimulation does receptor downregulation shut the axis down.\n\n"
    "In a man with bony metastatic prostate cancer, that transient testosterone surge feeds the "
    "tumor. The consequences are worsening bone pain, urinary obstruction, and — as here — spinal "
    "cord compression.\n\n"
    "The mandated fix is concurrent ANTI-ANDROGEN therapy to cover the flare window: bicalutamide, "
    "flutamide or nilutamide, started with or shortly before the agonist. Their own characteristic "
    "toxicity is gynecomastia, with rare hepatotoxicity.\n\n"
    "The longer-term toxicities of the GnRH agonists themselves (leuprolide, goserelin, triptorelin) "
    "are hot flashes, sexual dysfunction and decreased bone mineral density — the toxicity of "
    "inducing andropause on purpose. In premenopausal breast cancer the same drugs are used to induce "
    "menopause deliberately.",
    "The drug that eventually shuts down testosterone production first switches it sharply UP for a "
    "couple of weeks. In a man whose cancer is already in his spine, that surge can feed the tumor "
    "enough to crush the spinal cord.",
    exim="fig_chemo_gnrh",
    excap="The hypothalamic-pituitary-gonadal axis with the sites of action of the anti-androgens and "
          "the GnRH/LHRH agonists.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §48 / §56 — Lymphedema and post-traumatic edema (LO 34)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 54-year-old woman has a 3-week history of a heavy, aching, swollen right leg. The swelling "
    "began gradually about 6 weeks after an open inguinal hernia repair and has slowly worsened. The "
    "left leg is normal. The right leg is mildly warm with faint erythema; pain is described as "
    "heaviness rather than as severe. Duplex ultrasonography of the right leg shows no deep vein "
    "thrombosis. On examination the skin of the second interdigital web space of the right foot "
    "cannot be tented between the examiner's fingers. Which of the following is the most likely "
    "diagnosis?",
    {
        "Cellulitis":
            "The warmth and faint erythema invite this, and lymphedema is commonly mistaken for it. But "
            "cellulitis is acute, painful and usually febrile with a leukocytosis, and it does not "
            "produce loss of cutaneous elasticity in the web space.",
        "Chronic venous insufficiency":
            "This produces a heavy, swollen leg with skin changes, but the changes are "
            "hemosiderin-driven — medial ankle hyperpigmentation, lipodermatosclerosis and venous "
            "ulceration — and the web space skin remains pinchable.",
        "Decompensated heart failure":
            "Heart failure causes BILATERAL dependent edema. A unilateral heavy leg is not heart "
            "failure, and the unilateral detail in the stem is doing that rule-out deliberately.",
        "Recurrent deep vein thrombosis":
            "This is the first thought and it must be excluded first, because a clot can kill and "
            "lymphedema cannot — which is why the ultrasound was ordered. It is negative, and the onset "
            "over weeks rather than hours is also wrong for a clot.",
        "Secondary lymphedema": "",
    },
    "Secondary lymphedema",
    "The inability to tent the skin of the interdigital web space is a positive STEMMER SIGN — the "
    "'square toes' of lymphedema. It is the single physical sign the diagnosis hinges on: with "
    "ordinary edema you can usually pinch the skin, whereas in lymphedema it is firm and tough and "
    "cannot be pinched despite obvious swelling.\n\n"
    "The discriminating triad in this stem: UNILATERAL (so not heart failure) + NEGATIVE ULTRASOUND "
    "(so not a clot) + SQUARE TOES with a positive Stemmer sign (so lymphedema). Add a groin operation "
    "6–8 weeks ago in a developed country and you have the cause as well as the diagnosis — iatrogenic "
    "injury to the groin lymphatics. Hernia repair and kidney transplantation are both approached "
    "through the groin, where the lymphatics run.\n\n"
    "Order of testing matters and is examinable: ultrasound FIRST, always, because a deep vein "
    "thrombosis can kill and lymphedema cannot. Lymphedema is the diagnosis you reach after the "
    "ultrasound is negative and you look at the toes. Lymphoscintigraphy — a radiolabeled "
    "macromolecular tracer injected in an interdigital space and its transit imaged — is the "
    "confirmatory study.\n\n"
    "The pathophysiology in one sentence: lymphedema ensues when lymph production exceeds the maximal "
    "transport capacity of the lymphatic conduits. Protein and cellular metabolites accumulate in the "
    "extracellular space, drawing in water and provoking collagen deposition — which is why chronic "
    "lymphedema becomes firm and fibrotic rather than staying soft and pitting. Management is "
    "conservative and lifelong: elevation, therapeutic exercise, manual massage and compression. "
    "Surgical injury is probably not reversible.",
    "Her leg swelled slowly, weeks after an operation in the groin where the drainage channels run. "
    "The tell is the skin between her toes: it has gone so tough you cannot pinch it, which ordinary "
    "swelling never does.",
    exim="fig_stemmer",
    excap="Normal versus lymphedematous limb — the Stemmer sign, in which the skin of the web space "
          "cannot be lifted away from the underlying tissue.",
)

q(
    "A 40-year-old woman who emigrated from the Philippines 6 years ago has an 18-month history of "
    "progressive swelling of the left arm and breast. The right side is normal. The skin of the left "
    "arm is thickened with a dimpled, orange-peel texture and there are hyperkeratotic plaques over "
    "the forearm. She has no fever. Mammography and ultrasonography of the left breast show no "
    "malignancy. Photographs of comparable limbs are shown. Which of the following is the most likely "
    "cause?",
    {
        "Filarial infection": "",
        "Inflammatory breast carcinoma":
            "Peau d'orange makes everyone think of this, and it must be excluded — which the stem has "
            "done with imaging. Inflammatory carcinoma progresses over weeks to months, not 18 months, "
            "and would not produce hyperkeratotic plaques down the forearm.",
        "Lymphedema praecox":
            "This is PRIMARY lymphedema with onset between ages 1 and 35. It is a diagnosis of "
            "exclusion, and in a patient from an endemic region with no other explanation the "
            "acquired cause is far more likely.",
        "Prior axillary lymph node dissection":
            "Iatrogenic lymphatic injury is the commonest cause of secondary lymphedema in developed "
            "countries, and axillary dissection is its classic form. She has had no such surgery.",
        "Subclavian vein thrombosis":
            "Venous obstruction of the arm produces swelling, but it is acute or subacute, the skin "
            "texture stays normal, and prominent superficial collateral veins develop over the "
            "shoulder and chest wall.",
    },
    "Filarial infection",
    "Filariasis is the most frequent cause of secondary lymphedema WORLDWIDE, and the organism is "
    "Wuchereria bancrofti. It enters through skin invasion or injury and destroys the lymphatic "
    "system, producing elephantiasis.\n\n"
    "The diagnosis depends on a history question — where has the patient lived? — which is why this "
    "case and the post-hernia-repair case are taught as a pair. Same physical findings, two "
    "geographies, two causes. In developed countries the leading cause of secondary lymphedema is "
    "iatrogenic: lymphatic trauma or dissection, cancer or radiotherapy, and also large burns, "
    "pregnancy, and bacterial or fungal infection.\n\n"
    "The prognostic difference is the reason it matters. The parasitic form is treatable with "
    "medication and may be reversible; surgical lymphatic damage probably is not.\n\n"
    "The skin findings in this stem are the chronic ones: thickened skin with hyperkeratosis, "
    "lichenification and peau d'orange, reflecting progressive collagen deposition and fibrosis. "
    "Acutely, lymphedema gives pink or red skin with a mildly elevated temperature — easily mistaken "
    "for cellulitis or deep vein thrombosis. In both phases the pain is aching or heaviness; severe "
    "pain is rare, and that is a useful discriminator against infection and ischemia.\n\n"
    "Classification: primary lymphedema (females affected 2- to 10-fold more often) is congenital "
    "when onset is before age 1, praecox between 1 and 35, and tarda after 35. Secondary lymphedema is "
    "far more common than primary. The malignant complication of chronic lymphedema is "
    "lymphangiosarcoma.",
    "A parasite caught years ago in the tropics has destroyed the drainage channels of her arm, so "
    "fluid has nowhere to go and the skin has thickened over time. Unlike surgical damage, this kind "
    "can often be treated with medication.",
    image="fig_lymphedema_chronic",
    imcap="Clinical photographs of an arm and both legs with gross, disfiguring swelling; the skin is "
          "thickened and irregular with a dimpled surface and deep creases at the wrist and ankle.",
)

q(
    "A 24-year-old woman sustains a closed tibial shaft fracture and is placed in a long-leg cast. Six "
    "hours later she reports deep calf pain that she rates 9 out of 10 despite intravenous opioids. "
    "Passive dorsiflexion of the toes reproduces the pain intensely. The dorsalis pedis and posterior "
    "tibial pulses are palpable and the foot is warm and pink. The leg is swollen and the anterior "
    "compartment feels firm. Which of the following is the most appropriate next step?",
    {
        "Elevation of the limb above the level of the heart":
            "Elevation is standard for ordinary post-injury swelling and is harmless there. In "
            "compartment syndrome it reduces the arterial-to-compartment pressure gradient and can "
            "worsen perfusion.",
        "Emergency fasciotomy": "",
        "Measurement of serum creatine kinase and urine myoglobin":
            "Rhabdomyolysis with raised creatine kinase, myoglobinuria, hyperkalemia and acute kidney "
            "injury is the downstream consequence to watch for AFTER the compartment is released. "
            "Waiting for it means waiting for dead muscle.",
        "Compression ultrasonography of the leg":
            "This is the right test for a deep vein thrombosis, which typically appears DAYS after "
            "injury as swelling that had plateaued begins to worsen again. At 6 hours, with pain on "
            "passive stretch, the diagnosis is a compartment problem.",
        "Univalving the cast and reassessing in 2 hours":
            "Splitting or removing the cast is a reasonable holding manoeuvre while the operating room "
            "is prepared, but it is not the treatment, and a planned 2-hour delay in a limb that is "
            "already ischemic is the error the question is built around.",
    },
    "Emergency fasciotomy",
    "Acute compartment syndrome. The two early reliable signs are both present: pain out of "
    "proportion to the injury, and pain on PASSIVE STRETCH of the compartment.\n\n"
    "The palpable pulses are the trap, and they are irrelevant. Compartment syndrome is a "
    "CAPILLARY-perfusion problem, not a major-artery problem: compartment pressure only needs to "
    "exceed capillary perfusion pressure to make muscle ischemic, and that threshold is far below the "
    "pressure needed to obliterate flow in a named artery. The classic six Ps mislead for the same "
    "reason — pulselessness, pallor and paralysis are LATE, and by the time they appear the muscle is "
    "infarcting. Diagnosis is clinical; where pressures are measured, a ΔP (diastolic minus "
    "compartment pressure) below 30 mm Hg is the usual operative threshold.\n\n"
    "The mechanism to be able to state: edema inside a non-compliant fascial envelope raises "
    "interstitial pressure, which collapses capillaries and thin-walled veins; the resulting ischemia "
    "increases capillary permeability, which adds more edema — a self-amplifying cycle that does not "
    "break on its own.\n\n"
    "Read the clock, then read the feel. HOURS → inflammation, hematoma, compartment syndrome. DAYS → "
    "deep vein thrombosis, hypoalbuminemia. WEEKS → lymphedema. Then texture decides: hard and "
    "exquisitely painful = compartment; soft, pitting, one leg = deep vein thrombosis; soft, pitting, "
    "both legs and the sacrum = oncotic; firm, non-pitting, square toes = lymphatic.",
    "The swelling is trapped inside a tough sleeve of tissue that cannot stretch, so the pressure is "
    "squeezing her muscle's blood supply shut. Feeling a pulse means nothing here — the surgeon has to "
    "cut the sleeve open now.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §57 — Lymphatic dissemination of carcinoma (LO 60)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 61-year-old man has 3 months of epigastric discomfort, early satiety and 8 kg of weight loss. "
    "Examination shows a firm, non-tender, fixed 2-cm node in the left supraclavicular fossa. Which "
    "of the following best explains why this particular node is enlarged?",
    {
        "Metastatic cells entered the right lymphatic duct and refluxed across the midline":
            "The right lymphatic duct drains only the right side of the head and neck, the right arm "
            "and the right hemithorax, and it terminates on the right. Retrograde flow across the "
            "midline is not the mechanism.",
        "The gastric tumor invaded the thoracic aorta and seeded the neck haematogenously":
            "This describes blood-borne spread. Carcinomas disseminate preferentially by lymphatics; "
            "sarcomas preferentially by blood — and even lymphatic spread ultimately becomes "
            "haematogenous, but through the thoracic duct rather than by arterial invasion.",
        "The node drains the left arm, which shares lymphatics with the upper abdomen":
            "The left arm drains to axillary nodes. It does not share a drainage territory with the "
            "stomach; what links the abdomen to the left neck is the thoracic duct's termination "
            "point.",
        "The thoracic duct drains abdominal lymph and terminates on the left": "",
        "Tumor obstructed the cisterna chyli, forcing lymph into the cervical chain":
            "Obstruction does cause skip metastases by diverting flow around an expected node, but the "
            "left supraclavicular node is not a diversion — it is the normal, expected last station on "
            "this route.",
    },
    "The thoracic duct drains abdominal lymph and terminates on the left",
    "Virchow's node — an enlarged LEFT supraclavicular node from an abdominal malignancy, classically "
    "gastric. The palpable finding carries its own eponym, Troisier sign.\n\n"
    "The anatomy: lymph from the stomach passes through celiac and para-aortic nodes into the cisterna "
    "chyli, then up the thoracic duct, which drains essentially the whole body below the diaphragm "
    "plus the left side above it. The duct terminates at the junction of the left subclavian and left "
    "internal jugular veins — so the last nodal station before tumor cells enter the systemic venous "
    "circulation sits in the left supraclavicular fossa. Lymphatic spread becomes haematogenous spread "
    "at exactly that point; the two routes are sequential, not alternative.\n\n"
    "A RIGHT supraclavicular node would mean something different — the right lymphatic duct drains "
    "only the right side of the head and neck, the right arm and the right hemithorax, so it points to "
    "a lung, esophageal, mediastinal or head-and-neck primary.\n\n"
    "Read the node itself too: hard, painless, FIXED and progressively enlarging in an older patient "
    "is metastatic. Fixation is the ominous feature, because it means tumor has breached the capsule "
    "— extranodal extension, which independently worsens prognosis. A reactive node is soft or "
    "rubbery, mobile and tender, follows a local infection, and regresses.",
    "Almost all the lymph from below the diaphragm travels up one big duct that empties into a vein "
    "at the base of the left side of the neck. A stomach cancer's cells ride that duct and get stuck "
    "at the last stop.",
)

q(
    "A 58-year-old woman undergoes wide local excision of a breast carcinoma. Before the operation, "
    "blue dye and radiolabeled colloid are injected around the tumor, and two nodes that take up the "
    "tracer are removed and examined. Both are free of tumor, and no further nodal surgery is "
    "performed. Which of the following is the principal advantage of this approach over complete "
    "axillary dissection?",
    {
        "It allows the pathologist to examine the paracortex rather than the subcapsular sinus":
            "The subcapsular sinus is precisely where metastatic deposits are first seen, and it is the "
            "first compartment the pathologist examines. The paracortex is the node's T-cell zone, a "
            "reactive compartment.",
        "It avoids the leading cause of lymphedema in developed countries": "",
        "It eliminates the possibility of skip metastases":
            "Skip metastases are exactly what this approach cannot exclude. They occur when lymphatics "
            "are obstructed by tumor and flow is diverted around the expected node — the acknowledged "
            "caveat of the technique.",
        "It identifies haematogenous metastases earlier than imaging can":
            "The technique maps lymphatic drainage. Carcinomas spread preferentially by lymphatics and "
            "sarcomas by blood, and nothing about tracer uptake in a node informs you about "
            "blood-borne spread.",
        "It removes the need for nodal staging in the TNM system":
            "It does the opposite — it provides accurate N staging, which sets prognosis and the "
            "adjuvant therapy decision. The point is to obtain that staging at lower cost, not to skip "
            "it.",
    },
    "It avoids the leading cause of lymphedema in developed countries",
    "The sentinel node is the first node receiving drainage from the tumor bed, located by injecting "
    "blue dye and/or radiolabeled colloid around the tumor and following it.\n\n"
    "The logic is a conditional: if the sentinel node is free of tumor, the nodes downstream of it are "
    "almost certainly free too, so a full nodal dissection can be avoided. What makes that worth "
    "doing is that the DISSECTION ITSELF is the single commonest cause of secondary lymphedema in the "
    "developed world. Sentinel biopsy buys accurate N staging at a fraction of the morbidity.\n\n"
    "The caveat: spread is usually orderly, echelon by echelon, but skip metastases occur when "
    "lymphatics are obstructed by tumor and flow is diverted around the expected node.\n\n"
    "The route the technique exploits, step by step: carcinoma cells lose E-cadherin-mediated "
    "adhesion and degrade the basement membrane; they enter a lymphatic capillary — easier to "
    "penetrate than a blood capillary, because lymphatics have no basement membrane and have loose, "
    "overlapping endothelial junctions, which is the structural reason carcinoma prefers this route; "
    "they travel along afferent lymphatics that pierce the capsule on the convex surface of the node; "
    "and they arrive in the SUBCAPSULAR (marginal) SINUS, which is where deposits are first seen and "
    "therefore the first compartment the pathologist examines.\n\n"
    "For the breast specifically: about 75% of lymph drains to the axilla (levels I–III, defined by "
    "their relation to pectoralis minor), while medial quadrants drain to internal mammary nodes — so "
    "a medial tumor with negative axillary nodes may still have internal mammary disease.",
    "Instead of removing the whole cluster of lymph nodes, surgeons trace the dye to the one or two "
    "nodes the tumor drains into first. If those are clean, the rest almost certainly are — and the "
    "patient is spared the arm swelling that the bigger operation causes.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §49 — Diagnostic approach to DVT and PE (LO 10)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 63-year-old man is seen 9 days after a knee arthroplasty because of a swollen, painful right "
    "calf. The swelling began yesterday, having been stable and improving for several days "
    "beforehand. The right calf is 4 cm larger in circumference than the left, is warm and tender, "
    "and pits on pressure. The skin of the interdigital web spaces can be tented normally. Which of "
    "the following is the most appropriate next diagnostic step?",
    {
        "Compression duplex ultrasonography of the right leg": "",
        "Computed tomographic pulmonary angiography of the chest":
            "This images the pulmonary arteries and is the test for suspected pulmonary embolism. He "
            "has no dyspnea, chest pain, hypoxemia or tachycardia; the question is what is in the leg.",
        "Contrast venography of the right leg":
            "Once the reference standard, it is invasive, uses iodinated contrast and is now reserved "
            "for equivocal cases. It is not the first-line imaging test.",
        "Lymphoscintigraphy of the right lower limb":
            "This is the confirmatory study for LYMPHEDEMA, and it comes after a negative ultrasound. "
            "The normal web-space skin here is a negative Stemmer sign, which argues against "
            "lymphedema anyway.",
        "Serum D-dimer measurement":
            "D-dimer is a fibrin degradation product useful for EXCLUDING venous thromboembolism where "
            "pretest probability is low. Nine days after arthroplasty in a swollen, tender limb the "
            "pretest probability is high and the D-dimer will be raised by the surgery regardless, so "
            "a positive result changes nothing.",
    },
    "Compression duplex ultrasonography of the right leg",
    "Doppler (duplex) ultrasound is the standard imaging test for a suspected deep vein thrombosis, "
    "and it is the first move in any unilateral swollen limb — because a deep vein thrombosis can "
    "kill and the alternatives on the differential cannot.\n\n"
    "The buried clue is the tempo. Swelling that had plateaued or was improving and then begins to "
    "worsen again several days after an injury or operation is the classic announcement of a "
    "post-traumatic deep vein thrombosis, particularly where the limb has been immobilized. Injury "
    "plus immobilization supplies all three arms of Virchow's triad at once: stasis, endothelial "
    "injury and a post-traumatic hypercoagulable state.\n\n"
    "The negative Stemmer sign is the deliberate contrast with the lymphedema items. Ultrasound "
    "FIRST, always; lymphedema is the diagnosis you reach after the ultrasound is negative and you "
    "look at the toes.\n\n"
    "Two related points on D-dimer. Beyond its role in initial exclusion, a persistently elevated "
    "D-dimer AFTER anticoagulation is stopped predicts recurrence, which is why it feeds into the "
    "decision about duration. And the site-specific rule to carry alongside this one: for suspected "
    "CHRONIC THROMBOEMBOLIC PULMONARY HYPERTENSION the screening test of choice is a "
    "ventilation-perfusion scan, NOT computed tomographic angiography.\n\n"
    "Do not talk yourself out of imaging on the grounds that the leg is swollen because it was "
    "operated on.",
    "His leg was getting better and then suddenly got worse — that pattern, days after an operation "
    "with a limb held still, means a clot until proven otherwise. An ultrasound is quick, harmless "
    "and answers it.",
)

q(
    "A 58-year-old woman had a submassive pulmonary embolism 14 months ago with right ventricular "
    "strain on the presenting echocardiogram. She completed 6 months of anticoagulation. She now "
    "reports 4 months of progressive exertional dyspnea. Examination shows a loud pulmonic component "
    "of the second heart sound and elevated jugular venous pressure. Which of the following is the "
    "most appropriate screening investigation?",
    {
        "Computed tomographic pulmonary angiography":
            "This is the intuitive choice and it is the named trap. It is the test for an acute "
            "embolus; for chronic thromboembolic disease it is less sensitive than the "
            "ventilation-perfusion scan, because organized fibrotic material does not produce the "
            "filling defects of fresh thrombus.",
        "Compression duplex ultrasonography of both legs":
            "This looks for a residual or recurrent deep vein thrombosis. It cannot establish whether "
            "her pulmonary vasculature is chronically obstructed, which is what her symptoms are "
            "asking about.",
        "Repeat serum D-dimer measurement":
            "A persistently raised D-dimer after stopping anticoagulation predicts recurrence and feeds "
            "into decisions about duration, but it cannot diagnose chronic thromboembolic pulmonary "
            "hypertension.",
        "Right heart catheterization":
            "This is the confirmatory haemodynamic study once the diagnosis is suspected and screening "
            "is abnormal. It is invasive and is not the screening test.",
        "Ventilation-perfusion scanning": "",
    },
    "Ventilation-perfusion scanning",
    "Chronic thromboembolic pulmonary hypertension, and the examinable point is that the "
    "ventilation-perfusion scan is the screening test of CHOICE — not computed tomographic "
    "angiography. Work the patient up with brain natriuretic peptide, echocardiography and a "
    "ventilation-perfusion scan.\n\n"
    "Her risk profile is the one the lecture describes: risk is highest after a submassive or massive "
    "pulmonary embolism, and where there was right ventricular strain at presentation. New or "
    "progressive dyspnea in such a patient is the trigger to investigate.\n\n"
    "If confirmed, the management is indefinite anticoagulation, referral for pulmonary "
    "thromboendarterectomy, and lung transplantation for refractory disease. Untreated it progresses "
    "to cor pulmonale and death.\n\n"
    "The other long-term complication of venous thromboembolism to hold alongside it is "
    "post-thrombotic syndrome — chronic limb swelling, pain, skin changes and ulceration from valve "
    "damage after a proximal deep vein thrombosis.",
    "Months after a big clot in her lungs, scar tissue can leave the lung arteries permanently "
    "narrowed, and the heart strains against it. The scan that maps airflow against blood flow "
    "catches this better than the usual clot scan does.",
)
