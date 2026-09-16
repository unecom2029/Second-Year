# Batch 22 — Chemotherapy toxicity, lymphatic structure, and the gaps left by batch 21
# §44 s39-chemo-tox · §47 s42-lymphatics · §43 s38-chemo-principles · §45 s40-targeted-immuno
# §46 s41-hormonal · §56 s53-traumatic-edema · §57 s54-lymphatic-spread
# Native LOs: 11, 15, 16, 17, 34, 60, 63, 64

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
# §44 — Toxicities of traditional chemotherapy (LO 17)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 27-year-old man with Hodgkin lymphoma has completed five cycles of doxorubicin, bleomycin, "
    "vinblastine and dacarbazine. He reports 3 weeks of a dry cough and dyspnea on climbing one "
    "flight of stairs. He is afebrile. Examination shows fine bibasilar inspiratory crackles.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 13.9 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 41% (N=41%–53%)\n"
    "Leukocyte count 6,100/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 244,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Pulmonary function testing shows a restrictive pattern with a reduced diffusing capacity. Which "
    "agent is most likely responsible?",
    {
        "Bleomycin": "",
        "Dacarbazine":
            "This triazene alkylating agent is highly emetogenic and myelosuppressive. Its relative "
            "procarbazine carries the monoamine oxidase inhibition; neither is a pulmonary toxin.",
        "Doxorubicin":
            "Its organ toxicity is cardiac — a cumulative, dose-dependent cardiomyopathy. That would "
            "give orthopnea and a fall in ejection fraction rather than a restrictive pattern with a "
            "reduced diffusing capacity.",
        "Vinblastine":
            "Its dose-limiting toxicity is myelosuppression, which the normal blood counts here "
            "exclude. Note the within-class split: vinCRIStine's dose-limiting toxicity is "
            "neurotoxicity instead.",
        "None of these agents causes pulmonary toxicity":
            "One of them is among the six classic dose-limiting toxicity pairings, and pulmonary "
            "fibrosis in a patient on this exact regimen is the textbook presentation.",
    },
    "Bleomycin",
    "Pulmonary fibrosis — 'bleomycin lung' — and the normal blood counts are the buried clue rather "
    "than a reassurance. Bleomycin sits in the MILDEST myelosuppression tier, alongside vincristine "
    "and methotrexate given with leucovorin. A patient five cycles into a cytotoxic regimen with an "
    "entirely normal complete blood count is being pointed at the one agent whose dose-limiting "
    "toxicity is not the marrow.\n\n"
    "Mechanism: the bleomycin-iron complex generates free oxygen radicals that break DNA strands — "
    "which is how it kills tumor cells, in G2. The lung is uniquely vulnerable because it lacks "
    "bleomycin hydrolase, the enzyme that inactivates the drug in other tissues. Monitoring is by "
    "pulmonary function testing, and the diffusing capacity is the parameter that falls first.\n\n"
    "Learn the six classic dose-limiting pairings as one block:\n"
    "• Hemorrhagic cystitis — cyclophosphamide and ifosfamide (acrolein; prevent with mesna)\n"
    "• Pulmonary toxicity — bleomycin\n"
    "• Ototoxicity, nephrotoxicity and vomiting — cisplatin\n"
    "• Cardiotoxicity — doxorubicin, daunorubicin and trastuzumab\n"
    "• Peripheral neuropathy — oxaliplatin, vincristine and the taxanes\n"
    "• Potentially fatal diarrhea — irinotecan\n\n"
    "The general toxicities — stomatitis, myelosuppression, nausea and alopecia, from the four "
    "highest-turnover normal tissues — belong to nearly every agent and therefore discriminate "
    "nothing. The drug-specific ones are what get tested.",
    "One drug in his regimen scars the lungs instead of knocking down the blood counts. The fact that "
    "his blood counts are perfectly normal is the giveaway that it is that drug.",
    exim="fig_chemo_man",
    excap="The Chemo Man mnemonic — each drug mapped onto the organ it damages, with bleomycin and "
          "busulfan on the pulmonary arm.",
)

q(
    "Two patients are treated at the same clinic. The first receives vincristine as part of a "
    "lymphoma regimen and develops numbness of the fingertips, loss of ankle reflexes and "
    "constipation; her blood counts remain normal. The second receives vinblastine and develops "
    "neutropenia and thrombocytopenia requiring a dose delay, with no neurologic symptoms. Both drugs "
    "are vinca alkaloids acting at the same phase of the cell cycle. Which of the following best "
    "describes this difference?",
    {
        "Dose-limiting toxicity differs between agents within one class": "",
        "Only vinblastine is a substrate of P-glycoprotein":
            "Vincristine, vinblastine, doxorubicin, bleomycin and etoposide are all P-glycoprotein "
            "substrates, which is why multi-drug resistance defeats them together. Efflux concerns "
            "resistance, not the pattern of host toxicity.",
        "Vinblastine is cell cycle-nonspecific and vincristine is not":
            "Both are M-phase agents. The cell cycle-nonspecific classes are the alkylators, platinums "
            "and anthracyclines.",
        "Vincristine promotes microtubule assembly and vinblastine blocks it":
            "Both vincas BLOCK assembly of tubulin dimers so that the spindle dissolves. It is the "
            "TAXANES that promote microtubule formation and prevent disassembly, freezing the cell in "
            "metaphase.",
        "Vincristine was given intrathecally and vinblastine intravenously":
            "Intrathecal vincristine causes an ascending myeloencephalopathy and is uniformly fatal — "
            "it would not produce a survivable stocking-glove neuropathy. That absolute rule is why "
            "vincristine is dispensed in a minibag.",
    },
    "Dose-limiting toxicity differs between agents within one class",
    "The vinca split is a classic distractor, and the point generalizes: shared mechanism does not "
    "mean shared toxicity. Vincristine's dose-limiting toxicity is NEUROTOXICITY; vinblastine's and "
    "vinorelbine's is MYELOSUPPRESSION.\n\n"
    "The hook: vinCRIStine → CRIS-py nerves. vinBLAStine → BLASts, meaning the marrow.\n\n"
    "Clinically vincristine's neuropathy is a length-dependent sensorimotor neuropathy with "
    "autonomic involvement — which is why constipation and ileus appear alongside the numbness and "
    "the lost reflexes.\n\n"
    "The myelosuppression ranking is worth holding alongside it:\n"
    "• Strong — cyclophosphamide, cytarabine, doxorubicin, the nitrosoureas, vinblastine\n"
    "• Intermediate — carboplatin, etoposide, 5-fluorouracil, methotrexate, procarbazine\n"
    "• Mild — bleomycin, vincristine, and methotrexate given with leucovorin\n\n"
    "Notice that the two famously non-myelosuppressive drugs are exactly the two whose dose-limiting "
    "toxicity is something else entirely: bleomycin (lung) and vincristine (nerve).",
    "Two closely related drugs, and each picks a different victim: one goes after the nerves, the "
    "other after the bone marrow. Being in the same family does not mean causing the same harm.",
)

q(
    "A 61-year-old woman treated 8 years ago for breast cancer with a doxorubicin-containing regimen "
    "now has a new, unrelated diffuse large B-cell lymphoma. The proposed regimen is R-CHOP, which "
    "contains doxorubicin. Her current echocardiogram shows a left ventricular ejection fraction of "
    "56%. Which of the following is the most important consideration before proceeding?",
    {
        "The cumulative lifetime anthracycline dose she has already received": "",
        "Her prior exposure will have selected for multi-drug resistance":
            "Cross-resistance through P-glycoprotein is a genuine concern after anthracycline exposure, "
            "but this is a NEW and unrelated malignancy — a different clone that has never seen the "
            "drug.",
        "Whether she received mesna with the original regimen":
            "Mesna prevents the hemorrhagic cystitis caused by acrolein from cyclophosphamide and "
            "ifosfamide. It has nothing to do with anthracycline cardiotoxicity, whose protective agent "
            "is dexrazoxane.",
        "Whether her current ejection fraction is above the threshold for treatment":
            "A normal ejection fraction today is necessary but not sufficient, and it is the reassuring "
            "finding the question wants you to look past. Cardiac function can be normal right up to "
            "the point where cumulative dose causes it to fall.",
        "Whether the original tumor was estrogen receptor-positive":
            "Receptor status directs endocrine therapy for the breast primary. It has no bearing on the "
            "safety of re-treating with an anthracycline.",
    },
    "The cumulative lifetime anthracycline dose she has already received",
    "Anthracycline cardiomyopathy is dose-cumulative across a patient's ENTIRE LIFETIME, not per "
    "regimen. Exposure eight years ago still counts, and a normal ejection fraction today does not "
    "reset the clock.\n\n"
    "Mechanism: anthracyclines work by DNA intercalation, topoisomerase II inhibition and free "
    "radical generation. It is the free radical arm — iron-catalyzed redox cycling of the quinone ring "
    "— that injures cardiac muscle, which is poorly equipped to handle oxidative stress.\n\n"
    "What to do: total the lifetime exposure, obtain baseline cardiac function, and then consider "
    "liposomal doxorubicin, dexrazoxane (which chelates intracellular iron so it cannot react with "
    "superoxide and hydrogen peroxide), or an anthracycline-free regimen.\n\n"
    "The cardiotoxicity arm of Chemo Man has three names on it: doxorubicin, daunorubicin and — the "
    "only targeted agent on the list — trastuzumab, because HER2 is expressed on cardiomyocytes. "
    "Sequencing an anthracycline into trastuzumab stacks two mechanisms on one organ.\n\n"
    "Alkylating agents carry the other long-tail hazard: they are mutagens, and secondary malignancy "
    "is their class signature.",
    "The heart damage from this drug family adds up over a whole lifetime and never goes away. A "
    "normal heart scan today does not undo the dose she was given eight years ago.",
)

q(
    "A 59-year-old man receives his first dose of irinotecan for metastatic colorectal cancer. Twenty "
    "minutes into the infusion he develops abdominal cramping, profuse watery diarrhea, sweating, "
    "lacrimation and salivation. His blood pressure is 104/62 mm Hg and pulse 54/min. Which of the "
    "following is the most appropriate treatment?",
    {
        "Atropine": "",
        "Corticosteroids":
            "These are the treatment for immune-mediated colitis from a checkpoint inhibitor, which "
            "develops over weeks and is not accompanied by lacrimation, salivation and bradycardia.",
        "Loperamide":
            "This is the correct treatment for irinotecan's LATE diarrhea, which appears days after the "
            "infusion and is potentially fatal. It does not address a cholinergic syndrome occurring "
            "during the infusion.",
        "Octreotide":
            "This is used for refractory chemotherapy-associated diarrhea and for secretory diarrhea "
            "from neuroendocrine tumors. It is not the agent for an acute cholinergic reaction.",
        "Tocilizumab":
            "This blocks the interleukin-6 receptor and treats cytokine release syndrome after a T-cell "
            "engager or chimeric antigen receptor T-cell infusion — fever, hypotension and hypoxia, not "
            "a muscarinic syndrome.",
    },
    "Atropine",
    "Irinotecan causes diarrhea in two distinct forms with two different treatments, and the timing "
    "separates them completely.\n\n"
    "• EARLY (cholinergic) diarrhea occurs during or within hours of the infusion. Irinotecan inhibits "
    "acetylcholinesterase, producing a muscarinic syndrome — diarrhea with cramping, sweating, "
    "lacrimation, salivation, and bradycardia. Treatment is ATROPINE, an antimuscarinic. The "
    "accompanying secretions and the bradycardia in this stem are what identify it.\n"
    "• LATE diarrhea occurs days afterwards, from direct mucosal injury by the active metabolite. It "
    "is potentially fatal, and is treated with LOPERAMIDE, often in high dose.\n\n"
    "Irinotecan is a camptothecin — a topoisomerase I inhibitor acting in S/G2 by stabilizing the "
    "cleavable complex to produce single-strand breaks. Diarrhea is its dose-limiting toxicity, which "
    "is why it appears on the gut arm of Chemo Man, and the lecture describes it explicitly as "
    "'potentially fatal.'\n\n"
    "Compare the other gastrointestinal signature: 5-fluorouracil and capecitabine give diarrhea "
    "together with hand-foot syndrome (painful palmar-plantar erythrodysesthesia).",
    "The drug briefly floods his system with the 'rest and digest' signal — hence the watering eyes, "
    "sweating, slow pulse and sudden diarrhea. Atropine switches that signal off. The other kind of "
    "diarrhea, days later, needs a completely different drug.",
)

q(
    "A 48-year-old woman is to receive a highly emetogenic cisplatin-based regimen. Her antiemetic "
    "prophylaxis includes dexamethasone, palonosetron and netupitant. Which of the following "
    "correctly identifies the receptor blocked by netupitant?",
    {
        "The dopamine D2 receptor":
            "This is the target of the phenothiazines such as promethazine, the older option in this "
            "list, and of metoclopramide.",
        "The glucocorticoid receptor":
            "Dexamethasone acts here, and it is genuinely part of the regimen described — but it is a "
            "different drug in the same order.",
        "The histamine H1 receptor":
            "Antihistamines are used for motion sickness and as premedication for infusion reactions. "
            "No agent in this regimen targets H1.",
        "The neurokinin-1 receptor": "",
        "The 5-hydroxytryptamine-3 receptor":
            "This is what PALONOSETRON blocks — the -setron suffix. It is also in this regimen, which "
            "is exactly why the two suffixes have to be kept apart.",
    },
    "The neurokinin-1 receptor",
    "The suffixes are the gift here, and the lecture flags them precisely because a question will "
    "give you an unfamiliar generic name and expect you to classify it from the ending alone.\n\n"
    "• -setron → 5-hydroxytryptamine-3 (serotonin) receptor antagonists: ondansetron, granisetron, "
    "dolasetron, palonosetron.\n"
    "• -pitant → neurokinin-1 receptor antagonists: aprepitant, netupitant, rolapitant.\n"
    "• Promethazine — a phenothiazine and dopamine antagonist, the older option.\n"
    "• Synthetic cannabinoids — dronabinol, nabilone.\n\n"
    "This regimen deliberately contains one of each of the first two, plus dexamethasone, because "
    "highly emetogenic chemotherapy has two temporally distinct phases: acute emesis, driven largely "
    "by serotonin released from gut enterochromaffin cells, and delayed emesis, driven largely by "
    "substance P at neurokinin-1 receptors. Blocking one pathway leaves the other intact.\n\n"
    "Cisplatin is the drug that makes this necessary — it is the most emetogenic agent in common use, "
    "and nausea and vomiting sit alongside its ototoxicity and nephrotoxicity on the same arm of "
    "Chemo Man. Carboplatin is far less emetogenic, at the price of more myelosuppression.",
    "The drug name's ending tells you what it blocks. Anything ending in -pitant blocks one nausea "
    "pathway; anything ending in -setron blocks a different one. She is given both because the two "
    "pathways cause sickness at different times.",
)

q(
    "A 34-year-old man receives high-dose cytarabine for acute myeloid leukemia. On day 4 he reports "
    "bilateral eye redness, grittiness and watering, and on examination has dysdiadochokinesia and an "
    "unsteady, wide-based gait. He is afebrile, and there is no visual field defect. Which of the "
    "following is the most appropriate management of the ocular finding?",
    {
        "Empiric intravenous acyclovir":
            "This would be the answer for herpetic keratitis or a suspected viral retinitis. Bilateral "
            "chemical conjunctivitis with a simultaneous cerebellar syndrome in a patient on a specific "
            "drug has a simpler explanation.",
        "Prophylactic corticosteroid eye drops": "",
        "Topical antibiotic drops for bacterial conjunctivitis":
            "Bacterial conjunctivitis is usually unilateral at onset and purulent, and it would not "
            "explain the cerebellar signs appearing in the same patient at the same time.",
        "Urgent ophthalmologic examination for cytomegalovirus retinitis":
            "That would be the answer in profound immunosuppression with a CD4 count below 50, and it "
            "presents with visual field loss and characteristic retinal changes rather than with "
            "grittiness and injection.",
        "Withholding all further chemotherapy permanently":
            "The ocular toxicity is prevented, not a reason to abandon a potentially curative drug. The "
            "CEREBELLAR toxicity is the one that can require dose modification or discontinuation, and "
            "it is assessed by neurologic examination before each dose.",
    },
    "Prophylactic corticosteroid eye drops",
    "Cytarabine has two drug-specific toxicities that travel together, and both are on the eye and "
    "brain of Chemo Man: chemical conjunctivitis and cerebellar ataxia.\n\n"
    "The conjunctivitis occurs because cytarabine is secreted in tears and irritates the ocular "
    "surface directly. It is managed PROPHYLACTICALLY with corticosteroid eye drops whenever high-dose "
    "cytarabine is given — that is, it is anticipated rather than treated after the fact.\n\n"
    "The cerebellar toxicity is the more serious of the two and is why a neurologic examination is "
    "performed before each dose. Dysdiadochokinesia, dysmetria, nystagmus and gait ataxia can become "
    "irreversible if dosing continues, so the finding must be sought deliberately rather than waited "
    "for.\n\n"
    "Cytarabine is a pyrimidine antagonist acting in S phase and one of the strongly myelosuppressive "
    "agents — but myelosuppression is shared by almost everything and so discriminates nothing. Its "
    "eye-and-cerebellum pairing is what identifies it. Set it against the other pyrimidine "
    "antagonists: 5-fluorouracil and capecitabine are identified instead by diarrhea with hand-foot "
    "syndrome.",
    "This chemotherapy comes out in the tears and stings the eyes, so steroid drops are started in "
    "advance rather than waited for. The clumsiness is the same drug hitting the balance centre of the "
    "brain, and that one is checked before every dose.",
)

q(
    "A 44-year-old man with Hodgkin lymphoma is receiving a procarbazine-containing regimen. He "
    "attends a family celebration where he eats aged cheese, cured sausage and drinks red wine. Two "
    "hours later he develops a severe occipital headache, palpitations and diaphoresis. His blood "
    "pressure is 224/128 mm Hg. Which of the following best explains this episode?",
    {
        "Direct alkylation of vascular smooth muscle deoxyribonucleic acid":
            "Procarbazine is indeed a triazene alkylating agent, and alkylation is how it kills tumor "
            "cells — but DNA damage in vascular smooth muscle does not produce an acute hypertensive "
            "episode within 2 hours of a meal.",
        "Inhibition of monoamine oxidase": "",
        "Inhibition of vascular endothelial growth factor signaling":
            "VEGF pathway inhibitors — bevacizumab, sunitinib, pazopanib — do cause hypertension, along "
            "with impaired wound healing, thrombosis, bleeding and gastrointestinal perforation. But "
            "that hypertension is sustained, not food-triggered, and procarbazine is not in that class.",
        "Release of catecholamines from an unrecognized pheochromocytoma":
            "This would produce the same picture, and it is the near-miss the vignette is built "
            "against. But the trigger here is a specific, well-described dietary interaction in a "
            "patient on a specific drug.",
        "Tumor lysis with massive potassium release":
            "Tumor lysis syndrome follows treatment of a bulky, rapidly proliferating malignancy and "
            "gives hyperkalemia, hyperphosphatemia, hyperuricemia, hypocalcemia and acute kidney "
            "injury — not a hypertensive crisis after a meal.",
    },
    "Inhibition of monoamine oxidase",
    "Procarbazine is a monoamine oxidase inhibitor, and the tyramine reaction is its named "
    "drug-specific toxicity.\n\n"
    "The mechanism: tyramine in aged, cured and fermented foods is normally degraded by monoamine "
    "oxidase in the gut wall and liver before it reaches the circulation. With that enzyme inhibited, "
    "tyramine is absorbed intact, enters sympathetic nerve terminals, and displaces stored "
    "noradrenaline into the synapse — producing an abrupt hypertensive crisis. Aged cheese, cured "
    "meats, fermented products and red wine are the classic triggers.\n\n"
    "Procarbazine belongs to the TRIAZENE subclass of alkylating agents, with dacarbazine and "
    "temozolomide. It is worth keeping the alkylator subclasses and their distinguishing toxicities "
    "together:\n"
    "• Nitrogen mustards (cyclophosphamide, ifosfamide, chlorambucil, melphalan, bendamustine, "
    "mechlorethamine) — hemorrhagic cystitis from acrolein at high dose; prevent with mesna.\n"
    "• Nitrosoureas (carmustine, lomustine) — nausea and vomiting with delayed myelosuppression; they "
    "cross the blood-brain barrier.\n"
    "• Triazenes (dacarbazine, procarbazine, temozolomide) — procarbazine's monoamine oxidase "
    "inhibition.\n\n"
    "And the class signature they all share: myelosuppression with mucositis, neurotoxicity, and "
    "SECONDARY MALIGNANCIES — because alkylators are mutagens, which is the mechanism behind "
    "therapy-related leukemia.",
    "One of his chemotherapy drugs is secretly also an old-fashioned antidepressant-type enzyme "
    "blocker. That enzyme normally destroys a chemical in aged cheese and cured meat; without it, the "
    "chemical floods his bloodstream and sends his blood pressure through the roof.",
)

q(
    "A 66-year-old woman with lymphoma has a platelet count of 12,000/mm3 and a neutrophil count of "
    "400/mm3 eleven days after chemotherapy. Separately, a 58-year-old man with myeloma is due for "
    "autologous transplantation, and despite granulocyte colony-stimulating factor his peripheral "
    "blood CD34-positive cell yield has been insufficient for collection on two attempts. Which agent "
    "is most appropriate for the second patient?",
    {
        "Epoetin alfa":
            "This is an erythropoiesis-stimulating agent for a low red cell count. It does not mobilize "
            "stem cells, and its boxed warnings limit its use in malignancy.",
        "Filgrastim":
            "Granulocyte colony-stimulating factor is the right agent for the FIRST patient's "
            "neutropenia, and it is also the backbone of mobilization — but it has already failed on "
            "its own here, which is the premise of the question.",
        "Plerixafor": "",
        "Romiplostim":
            "This thrombopoietin receptor agonist stimulates platelet production and would be "
            "considered for the first patient's thrombocytopenia, alongside eltrombopag and "
            "avatrombopag.",
        "Sargramostim":
            "Granulocyte-macrophage colony-stimulating factor stimulates granulocytes and macrophages. "
            "It broadens myeloid recovery but is not the agent that releases stem cells from the "
            "marrow niche.",
    },
    "Plerixafor",
    "Plerixafor is a CXCR4 antagonist, and it is given WITH granulocyte colony-stimulating factor to "
    "mobilize peripheral blood stem cells for collection before transplantation.\n\n"
    "The mechanism connects back to the very first block of this course. Hematopoietic stem cells are "
    "tethered in the marrow niche by the CXCR4 receptor binding its ligand CXCL12 (stromal cell-"
    "derived factor 1) on stromal cells. Blocking CXCR4 releases that tether, and the stem cells spill "
    "into the circulation where they can be harvested by apheresis. It is a chemical eviction notice, "
    "which is exactly what is needed when growth factor alone has failed to produce an adequate "
    "CD34-positive yield.\n\n"
    "Map each supportive agent onto the cytopenia it fixes:\n"
    "• Red cells → epoetin alfa (an erythropoiesis-stimulating agent; its boxed warnings are worked in "
    "the anemia pharmacology block)\n"
    "• Neutrophils → filgrastim (granulocyte colony-stimulating factor)\n"
    "• Granulocytes and macrophages → sargramostim (granulocyte-macrophage colony-stimulating factor)\n"
    "• Platelets → the thrombopoietin agents: eltrombopag, romiplostim, avatrombopag\n"
    "• Stem cell mobilization → plerixafor plus granulocyte colony-stimulating factor",
    "Stem cells are anchored inside the bone marrow by a molecular hook. This drug unhooks them so "
    "they float out into the blood, where they can be collected for his transplant.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §47 — Lymphatic structure, the thoracic duct, mucosal immunity (LO 63)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A resident places a central venous catheter in the left internal jugular vein. The first wire "
    "would not thread, so the needle and wire were withdrawn after the dilator had been passed, and "
    "the line was placed successfully on a second attempt. The immediate chest radiograph shows "
    "correct catheter position and no pneumothorax. The next morning the patient is dyspneic and the "
    "left hemithorax is opacified; thoracentesis yields milky, triglyceride-rich fluid. Which "
    "structure was injured?",
    {
        "The left brachiocephalic vein":
            "Injury here causes bleeding into the mediastinum or a hemothorax, which would be "
            "immediate and would not yield milky fluid.",
        "The left phrenic nerve":
            "Phrenic injury produces an elevated hemidiaphragm on the chest radiograph, not an "
            "opacified hemithorax, and no effusion.",
        "The left subclavian artery":
            "Arterial puncture causes immediate bleeding, a pulsatile hematoma or a hemothorax. The "
            "fluid would be blood, not chyle.",
        "The right lymphatic duct":
            "This drains only the right upper body, is smaller and more superficial, and terminates on "
            "the RIGHT. Injury to it is far less significant because the volume it carries is small.",
        "The thoracic duct": "",
    },
    "The thoracic duct",
    "Thoracic duct injury with chylothorax — and it is the reason the lecture says never to place a "
    "left internal jugular central line.\n\n"
    "The anatomy: the thoracic duct enters at the POSTERIOR wall of the vein at the confluence of the "
    "left subclavian and left internal jugular veins — directly in the path of a left internal jugular "
    "needle. It is only 2–3 mm across. The mechanism of injury is exactly as described in this stem: "
    "you believe you are in the vein, the DILATOR does the damage, the line will not thread, you "
    "withdraw and succeed on a second pass, and the immediate film looks perfect.\n\n"
    "Why the first film is normal: chyle accumulates over hours. Lymphatic flow is slow and "
    "low-pressure, and it increases substantially only once the patient is fed — which is why the "
    "hemithorax is white the following morning.\n\n"
    "Why it is so hard to repair: the duct carries everything except the right upper body — the entire "
    "lower body, abdomen, left thorax, left arm and left head and neck. Repair means entering the left "
    "chest and working at the lung apex, and roughly 90% of the time nothing can be done. Peripheral "
    "lymphatics are the width of pencil lead, and you cannot sew pencil lead. The maneuver of last "
    "resort is high-fat feeding to increase chyle flow and make the leak visible enough to place a "
    "stitch; usually the duct is simply ligated, relying on the right-sided duct to compensate.\n\n"
    "Use the RIGHT internal jugular, a subclavian, or a femoral vein instead.",
    "The body's main lymph drain empties into a vein at the base of the left side of the neck — "
    "exactly where the needle went. It was torn, and overnight the milky lymph filled his chest "
    "instead of returning to the bloodstream.",
    exim="fig_lymph_system",
    excap="The lymphatic system as a whole — the thoracic duct draining everything except the right "
          "upper body and emptying at the left venous angle.",
)

q(
    "A 58-year-old man has a swollen right leg. Which of the following best explains why obstruction "
    "of lymphatic drainage produces more severe and more persistent swelling than obstruction of "
    "venous outflow at the same anatomic level?",
    {
        "Lymphatic vessels lack valves, so flow reverses immediately on obstruction":
            "Lymphatic vessels DO have valves and behave much like veins; valve damage or inflammation "
            "is one way flow fails. Absence of valves is not the distinguishing property.",
        "Lymphatic vessels carry blood at higher pressure than veins":
            "Pressure within lymphatic vessel walls is LOWER than in blood vessels, and lymph flows "
            "more slowly. They carry lymph, not blood.",
        "Lymphatic obstruction raises capillary hydrostatic pressure more steeply":
            "Raised capillary hydrostatic pressure is the mechanism of VENOUS obstruction, which "
            "produces a low-protein transudate. It is precisely the mechanism the question is asking "
            "you to contrast against.",
        "Proteins trapped in the interstitium hold water osmotically": "",
        "The lymphatic system's primary function is immunologic surveillance":
            "The immune function is real but secondary in this framing. The PRIMARY function of the "
            "lymphatic system is to return proteins and fluids to the blood — which is the fact the "
            "answer turns on.",
    },
    "Proteins trapped in the interstitium hold water osmotically",
    "The primary function of the lymphatic system is to return PROTEINS and fluids to the blood. The "
    "immune role is real but secondary in this framing, and the protein role is what explains every "
    "clinical consequence.\n\n"
    "The structural property that makes it work: lymphatic vessel walls are MORE PERMEABLE than blood "
    "capillary walls, so they admit large proteins that cannot re-enter the venous capillaries at "
    "all. Lymph is therefore very heavy in protein.\n\n"
    "Now the contrast. Venous obstruction raises capillary hydrostatic pressure — fluid is pushed out, "
    "but the protein-clearing route remains intact, so the result is a low-protein transudate that "
    "responds to elevation. Lymphatic obstruction removes the ONLY route those proteins have. They "
    "accumulate in the interstitium, raise interstitial oncotic pressure, and draw water after them. "
    "Over time the retained protein and cellular metabolites also drive collagen deposition, which is "
    "why chronic lymphedema becomes firm and fibrotic and stops pitting.\n\n"
    "Two further consequences follow from the same anatomy. The vessels are tiny — the thoracic duct "
    "is 2–3 mm and peripheral lymphatics are the width of pencil lead — so there is no good surgical "
    "repair. And nodes enlarge because bacteria, allergens and tumor cells collected there stimulate "
    "lymphocyte proliferation.",
    "Lymph vessels are the only route big protein molecules have out of the tissues. Block them and "
    "the proteins are stranded, and protein drags water along with it — so the swelling is worse and "
    "does not drain away with elevation.",
    exim="fig_lymph_capillary",
    excap="Lymphatic capillaries picking up protein that the blood capillaries cannot reabsorb, and "
          "returning it via the node to the circulation.",
)

q(
    "A 6-week-old infant born at 28 weeks' gestation undergoes ileocecal resection for necrotizing "
    "enterocolitis. Over the following months she has repeated episodes of Gram-negative bacteremia "
    "without an identifiable focus. Which of the following best explains her susceptibility?",
    {
        "Asplenia from vascular compromise during the resection":
            "Loss of splenic function predisposes to overwhelming infection by ENCAPSULATED organisms "
            "— pneumococcus, meningococcus, Haemophilus influenzae type b — and would be accompanied by "
            "Howell-Jolly bodies on the blood smear.",
        "Inherited selective immunoglobulin A deficiency":
            "This is the most common primary immunodeficiency and produces a genuinely similar final "
            "picture of a less-protected mucosal barrier, which is why the two are confused. Hers is an "
            "ACQUIRED, LOCAL deficit caused by removing the tissue, not an inherited failure of "
            "production.",
        "Loss of the major site of immunoglobulin A production": "",
        "Loss of thymic tissue with failure of positive selection":
            "Positive selection occurs in the thymic cortex, in the mediastinum, and its failure would "
            "produce a T-cell deficiency with opportunistic and viral infection. The thymus was not "
            "operated on.",
        "Reduced hepatic synthesis of complement proteins":
            "Complement deficiency predisposes particularly to neisserial infection and is not a "
            "consequence of bowel resection.",
    },
    "Loss of the major site of immunoglobulin A production",
    "Peyer's patches are gut-associated lymphoid tissue, concentrated in the ILEUM and ileocecal "
    "region. They are the major site of immunoglobulin A production — the lecture's 'mucosal "
    "antiseptic paint.'\n\n"
    "The chain to memorize: Peyer's patches → ileum and ileocecal region → IgA → mucosal antiseptic "
    "paint → coats the bowel → prevents bacterial invasion of the mucosa. Remove that tissue and the "
    "intestinal mucosa is left unprotected, allowing bacterial translocation across it and "
    "gastrointestinal sepsis.\n\n"
    "The structural details that distinguish these tissues from lymph nodes: Peyer's patches are NOT "
    "encapsulated, and antigen arrives not through afferent lymphatics or the bloodstream but through "
    "M (microfold) cells, which face the lumen and sample antigen by endocytosis. Tonsils "
    "(bronchus-associated lymphoid tissue) are likewise non-encapsulated and are exposed directly and "
    "continuously at their crypts; their predominant antibody is IgG, with some IgE.\n\n"
    "Why age matters so much here: in young children the gut and mucosal lymphoid tissue — Peyer's "
    "patches, tonsils, appendix — and the thymus carry enormous immunological weight, and that "
    "responsibility shifts toward the bone marrow with age. The same operation therefore carries "
    "different risk at different ages, which is also why splenectomy is deferred past early childhood "
    "and tonsillectomy is generally deferred to about age 12.",
    "The last part of the small bowel is the factory for the antibody that paints the gut lining and "
    "keeps bacteria out. She had that section removed as a newborn, so bacteria now slip through the "
    "unprotected lining into her blood.",
    exim="fig_peyers_patch",
    excap="A Peyer's patch — M cells facing the lumen sampling antigen, with the lymphoid follicle "
          "beneath producing the plasma cells that secrete immunoglobulin A.",
)

q(
    "During normal development, immature T cells arrive in the thymus from the bone marrow. Which of "
    "the following correctly describes what happens to a thymocyte that fails to recognize antigen "
    "presented by thymic epithelial cells?",
    {
        "It is exported to the paracortex of peripheral lymph nodes as a naive T cell":
            "The paracortex is indeed the T-cell zone of the node and is where naive T cells go — but "
            "only the cells that PASSED selection. Exporting non-responders would defeat the purpose of "
            "the process.",
        "It matures into a regulatory T cell that enforces peripheral tolerance":
            "Regulatory T cells are a real lineage, but failure of positive selection is not how they "
            "are generated. The slide describes only survival or death at this step.",
        "It migrates to the thymic medulla and completes maturation":
            "This is what happens to cells that DO respond — they are selected to survive, mature, and "
            "migrate from cortex to medulla. It is the exact inversion of the answer.",
        "It undergoes apoptosis and is cleared by macrophages": "",
        "It undergoes receptor gene rearrangement a second time in the marrow":
            "Antigen receptor gene rearrangement occurs once, in the primary lymphoid organ, before "
            "selection. There is no return to the marrow for a second attempt.",
    },
    "It undergoes apoptosis and is cleared by macrophages",
    "This is POSITIVE SELECTION, and the lecture describes it in exactly three steps:\n\n"
    "1. Immature T cells first reside in the thymic CORTEX, where they contact antigen-presenting "
    "epithelial cells.\n"
    "2. Those that respond appropriately are selected to survive, mature, and migrate to the MEDULLA.\n"
    "3. Non-responders die by apoptosis and are cleared by macrophages.\n\n"
    "This is antigen-INDEPENDENT maturation — it happens in a primary (generative) lymphoid organ, "
    "where the cell rearranges its receptor genes and is selected for functionality and self-tolerance "
    "without ever meeting its actual antigen. The product is a naive lymphocyte. Contrast "
    "antigen-DEPENDENT maturation, which happens in the secondary (peripheral) organs — lymph nodes, "
    "spleen and mucosa — where the naive cell meets its antigen and undergoes clonal expansion, class "
    "switching, somatic hypermutation and affinity maturation in the germinal center.\n\n"
    "The overall architecture: marrow → thymus for T cells → nodes, spleen and mucosa, with continuous "
    "recirculation. Generative organs feed the peripheral organs.\n\n"
    "The thymus itself is a soft, triangular organ in the mediastinum, anterior and superior to the "
    "heart and posterior to the sternum. It secretes thymulin, thymopoietin and thymosins, and "
    "involutes from the onset of puberty, being replaced by adipose tissue — because most T cells are "
    "produced during childhood and few new ones are needed afterwards.",
    "The thymus is a school with a brutal exam. Young T cells that can recognize what is shown to them "
    "graduate and move deeper in; the ones that cannot are killed on the spot and cleared away.",
    exim="fig_thymic_selection",
    excap="T-cell training — a bone marrow precursor entering the thymic cortex, positive selection "
          "there, then passage to the medulla and out as a mature CD4 or CD8 cell.",
)

# ─────────────────────────────────────────────────────────────────────────────
# Top-ups — §43 (LO 64), §45 (LO 11, 16), §46 (LO 15)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "Two antineoplastic agents both act by stabilizing the complex formed between deoxyribonucleic "
    "acid and a topoisomerase enzyme, preventing religation of the cut strands. One produces "
    "single-strand breaks and acts in S and G2 phase; the other produces double-strand breaks and "
    "acts in late S and early G2. Which of the following correctly pairs the drugs with these "
    "descriptions?",
    {
        "Bleomycin produces the single-strand breaks; cisplatin the double-strand breaks":
            "Bleomycin acts in G2 but is an antitumor antibiotic whose bleomycin-iron complex generates "
            "free oxygen radicals. Cisplatin is cell cycle-nonspecific and forms intrastrand adducts, "
            "cross-linking DNA to DNA or to protein.",
        "Cytarabine produces the single-strand breaks; gemcitabine the double-strand breaks":
            "Both are pyrimidine antagonists acting in S phase by interfering with nucleotide "
            "metabolism. Neither acts on a topoisomerase.",
        "Etoposide produces the single-strand breaks; irinotecan the double-strand breaks":
            "This is the correct pair of drugs with the two roles reversed — the most likely error. "
            "Topoisomerase I is the single-strand enzyme and topoisomerase II the double-strand one.",
        "Irinotecan produces the single-strand breaks; etoposide the double-strand breaks": "",
        "Methotrexate produces the single-strand breaks; 5-fluorouracil the double-strand breaks":
            "Methotrexate is a folate antagonist inhibiting dihydrofolate reductase and thymidylate "
            "synthase; 5-fluorouracil is converted to 5-FdUMP and inhibits thymidylate synthase, "
            "causing thymidine-less death. Both act in S phase without touching a topoisomerase.",
    },
    "Irinotecan produces the single-strand breaks; etoposide the double-strand breaks",
    "The enzyme number tells you the number of strands, which is the whole memory device:\n\n"
    "• Topoisomerase I — the camptothecins, irinotecan and topotecan. They stabilize the cleavable "
    "complex, producing SINGLE-strand breaks, in S/G2.\n"
    "• Topoisomerase II — the podophyllotoxins, etoposide and teniposide. A persistent cleavable "
    "complex produces DOUBLE-strand breaks, in late S/early G2.\n\n"
    "Their dose-limiting toxicities differ accordingly: irinotecan and topotecan give diarrhea "
    "(irinotecan's is potentially fatal) with marrow suppression; etoposide gives dose-limiting "
    "myelosuppression with infusion-related hypotension.\n\n"
    "Note that a third class also inhibits topoisomerase II — the anthracyclines, which combine "
    "intercalation, topoisomerase II inhibition and free radical generation, and are cell "
    "cycle-nonspecific rather than phase-specific.\n\n"
    "The broader phase map: G1 asparaginase; S folate, pyrimidine and purine antagonists; S/G2 "
    "topoisomerase I; late S/early G2 topoisomerase II; G2 bleomycin; M taxanes and vincas; and cell "
    "cycle-nonspecific for the anthracyclines, alkylators and platinums.",
    "Both drugs jam the enzyme that untangles DNA, but there are two such enzymes. The one numbered "
    "I cuts a single strand, the one numbered II cuts both — so the number is the answer.",
    exim="fig_chemo_pathways",
    excap="Master pathway diagram — where each class of antineoplastic agent acts on nucleotide "
          "synthesis, DNA and the topoisomerases.",
)

q(
    "Most approved therapeutic monoclonal antibodies used against tumor antigens are of the IgG1 "
    "subclass, which triggers potent complement-dependent cytotoxicity and antibody-dependent "
    "cellular cytotoxicity. The immune checkpoint inhibitors, by contrast, are engineered as IgG4. "
    "Which of the following best explains this choice?",
    {
        "IgG4 antibodies are fully human, whereas IgG1 antibodies are invariably chimeric":
            "Species origin and subclass are independent properties. Origin is read from the suffix — "
            "-omab murine, -ximab chimeric, -zumab humanized, -umab fully human — and does not "
            "determine effector function.",
        "IgG4 cannot activate classical complement, sparing the cell being activated": "",
        "IgG4 crosses the cell membrane and can reach intracellular checkpoints":
            "No antibody crosses the plasma membrane; at roughly 145,000 daltons they are far too "
            "large. That limitation is why every signal transduction inhibitor is a small molecule. "
            "PD-1, PD-L1 and CTLA-4 are all cell-surface molecules.",
        "IgG4 has a substantially longer half-life than IgG1":
            "IgG1, IgG2 and IgG4 all have half-lives of about 21 days. It is IgG3 that is the short one "
            "at about 7 days.",
        "IgG4 binds its target with higher affinity than other subclasses":
            "Affinity is a property of the variable region, which is engineered independently of the "
            "constant region that defines the subclass.",
    },
    "IgG4 cannot activate classical complement, sparing the cell being activated",
    "The logic is entirely about what you are aiming at. A tumor-directed antibody such as rituximab "
    "or trastuzumab binds a cell you want DESTROYED, so IgG1 is ideal — it recruits complement-"
    "dependent cytotoxicity and antibody-dependent cellular cytotoxicity to finish the job.\n\n"
    "A checkpoint inhibitor binds PD-1 on a T cell you are trying to ACTIVATE. Recruiting killing "
    "machinery to that cell would destroy the very lymphocyte the therapy depends on. IgG4 cannot "
    "activate the classical complement pathway at all, which makes it the right chassis for a "
    "blocking antibody whose only job is to occupy a receptor.\n\n"
    "The subclass facts to carry: IgG1, IgG2 and IgG4 have half-lives of about 21 days; IgG3 about 7 "
    "days. Most approved monoclonals are IgG1.\n\n"
    "And the nomenclature, which is a separate axis and a reliable source of easy points: -omab is "
    "murine (fully mouse-derived); -ximab is chimeric, a mouse variable region on a human constant "
    "region (cetuximab, rituximab); -zumab is humanized, human except the complementarity-determining "
    "regions (trastuzumab, bevacizumab, alemtuzumab); -umab is fully human (panitumumab). The more "
    "murine the sequence, the greater the immunogenicity and the risk of infusion reactions.",
    "Normally these antibodies are built to call in a demolition crew on whatever they stick to. "
    "Checkpoint drugs stick to your own T cells, which you want alive — so they are built from the one "
    "version that cannot call the crew.",
    exim="fig_antibody_types",
    excap="Endogenous and engineered antibody structures — the constant region determines subclass and "
          "effector function, the variable region determines the target.",
)

q(
    "A 69-year-old man with newly diagnosed multiple myeloma begins lenalidomide with dexamethasone. "
    "He has no personal or family history of thrombosis and is ambulatory. Which of the following "
    "adverse effects of this agent most requires specific prophylaxis?",
    {
        "Capillary leak syndrome":
            "This is the signature toxicity of aldesleukin (interleukin-2), which makes the endothelium "
            "leak so that the patient becomes hypotensive and third-spaces fluid.",
        "Herpes zoster reactivation":
            "This is a toxicity of the PROTEASOME INHIBITORS — bortezomib, ixazomib, carfilzomib — "
            "which also cause neuropathy, less with subcutaneous than intravenous dosing. Antiviral "
            "prophylaxis is given with those agents.",
        "Hypokalemia from mineralocorticoid excess":
            "This is abiraterone, whose blockade of CYP17 shunts adrenal precursors down the "
            "mineralocorticoid pathway — which is why it is co-prescribed with prednisone.",
        "QT interval prolongation":
            "This is a class effect of the SMALL-MOLECULE targeted agents, appearing in five of the ten "
            "signal transduction rows, along with diarrhea and raised liver function tests. "
            "Lenalidomide is not a kinase inhibitor.",
        "Venous thromboembolism": "",
    },
    "Venous thromboembolism",
    "The thalidomide derivatives — thalidomide, lenalidomide and pomalidomide — carry two named "
    "hazards: THROMBOEMBOLISM, and contraindication in pregnancy.\n\n"
    "The thrombotic risk is high enough that antithrombotic prophylaxis is standard with these agents, "
    "and the risk is amplified by the dexamethasone he is also receiving and by the underlying "
    "myeloma, which is itself a prothrombotic state. Lower-risk patients receive aspirin; "
    "higher-risk patients receive a prophylactic anticoagulant.\n\n"
    "The teratogenicity is the historical reason these drugs are dispensed only under strict "
    "pregnancy-prevention programs — thalidomide's phocomelia disaster is the origin of modern drug "
    "regulation.\n\n"
    "Keep the myeloma treatment classes and their signature toxicities apart, because a single patient "
    "may receive all of them:\n"
    "• Thalidomide derivatives (the '-amides') → thromboembolism, teratogenicity\n"
    "• Proteasome inhibitors (bortezomib, ixazomib, carfilzomib) → peripheral neuropathy and herpes "
    "zoster reactivation\n"
    "• Anti-CD38 antibodies (daratumumab) → interference with blood bank cross-matching, because CD38 "
    "is expressed on red cells\n"
    "• Corticosteroids → hyperglycemia, insomnia, infection risk",
    "This myeloma drug makes the blood far more likely to clot, and the steroid given with it makes "
    "that worse. So a blood thinner is started at the same time, before anything happens.",
)

q(
    "A 74-year-old man with metastatic castration-resistant prostate cancer is started on abiraterone. "
    "Three weeks later he reports leg swelling and muscle cramps.\n\n"
    "Laboratory studies show:\n"
    "Potassium 2.9 mEq/L (N=3.5–5.0 mEq/L)\n"
    "Sodium 144 mEq/L (N=136–146 mEq/L)\n"
    "Bicarbonate 31 mEq/L (N=22–28 mEq/L)\n"
    "Creatinine 1.1 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "His blood pressure is 164/96 mm Hg, up from 128/78 mm Hg. Which of the following best explains "
    "these findings, and what should be co-prescribed?",
    {
        "Androgen receptor blockade with a compensatory rise in aldosterone; add spironolactone":
            "Abiraterone is not a receptor antagonist — that is the first- and second-generation "
            "anti-androgens (bicalutamide, enzalutamide), whose own toxicity is gynecomastia. "
            "Spironolactone is also avoided in prostate cancer because it has androgenic receptor "
            "activity.",
        "An initial surge in luteinizing hormone; add an anti-androgen":
            "That is tumor flare from a GnRH agonist such as leuprolide, which causes worsening bone "
            "pain, obstruction or cord compression — not hypokalemia and hypertension.",
        "CYP17 blockade shunts precursors into the mineralocorticoid pathway; add prednisone": "",
        "Hepatotoxicity causing secondary hyperaldosteronism; add ursodeoxycholic acid":
            "Abiraterone does cause hepatotoxicity, and liver function is monitored on treatment — but "
            "that presents as a transaminitis, and it is not the mechanism of this electrolyte "
            "picture.",
        "Inhibition of aromatase reducing estrogen feedback; add tamoxifen":
            "Aromatase inhibition is the anti-estrogen strategy in postmenopausal breast cancer. Its "
            "toxicities are osteoporosis, hot flashes and arthralgias.",
    },
    "CYP17 blockade shunts precursors into the mineralocorticoid pathway; add prednisone",
    "Abiraterone is the testosterone DEPLETER among the anti-androgens, in contrast to the receptor "
    "antagonists. It inhibits CYP17 (17α-hydroxylase / C17,20-lyase), the enzyme required for androgen "
    "biosynthesis from the precursors dehydroepiandrosterone and androstenedione — and CYP17 is "
    "expressed in testicular, adrenal and prostatic tumor tissue alike, which is why the drug works "
    "even after castration.\n\n"
    "The toxicity follows directly from where the block sits. Adrenal steroid precursors that can no "
    "longer travel down the androgen route are shunted into the MINERALOCORTICOID pathway instead, "
    "producing a state of mineralocorticoid excess: hypokalemia, fluid retention and hypertension — "
    "exactly this patient's picture, with the metabolic alkalosis that accompanies renal potassium "
    "wasting.\n\n"
    "Prednisone is co-prescribed for a mechanistic reason rather than an anti-inflammatory one: the "
    "corticosteroid suppresses the adrenocorticotropic hormone drive that is generating the excess "
    "precursors in the first place. Turn off the drive and you turn off the shunt.\n\n"
    "Abiraterone's other named toxicity is hepatotoxicity. The receptor antagonists — flutamide, "
    "bicalutamide and nilutamide, and the second-generation enzalutamide and apalutamide — instead "
    "cause gynecomastia with rare hepatotoxicity.",
    "The drug blocks one exit from the adrenal gland's assembly line, so the raw material piles up and "
    "takes the other exit — the salt-retaining hormone. A steroid tablet switches off the signal "
    "driving the whole line.",
)

# ─────────────────────────────────────────────────────────────────────────────
# §56 / §57 — Post-traumatic edema and the drainage map (LO 34, LO 60)
# ─────────────────────────────────────────────────────────────────────────────

q(
    "A 29-year-old man is admitted after a motor vehicle collision with a femoral fracture, splenic "
    "laceration and pulmonary contusions. He receives 6 L of crystalloid and 4 units of packed red "
    "cells over the first 12 hours. On day 4 he has periorbital puffiness, deeply pitting edema of "
    "both legs and the sacrum, and a 7 kg weight gain.\n\n"
    "Laboratory studies show:\n"
    "Albumin 1.9 g/dL (N=3.5–5.5 g/dL)\n"
    "Creatinine 0.8 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Hemoglobin 9.8 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 29% (N=41%–53%)\n\n"
    "Which Starling variable best accounts for this pattern of edema?",
    {
        "Decreased lymphatic drainage":
            "Lymphatic failure gives protein-rich swelling confined to the drainage territory of the "
            "injured lymphatics. It appears over weeks to months, becomes non-pitting and fibrotic, and "
            "would not involve the periorbital tissues.",
        "Decreased plasma oncotic pressure": "",
        "Increased capillary hydrostatic pressure":
            "This is venous obstruction or deep vein thrombosis, and it would give a unilateral, "
            "whole-limb, warm and tender leg — not symmetrical dependent edema with periorbital "
            "puffiness.",
        "Increased capillary permeability":
            "Inflammatory capillary leak is real in this patient and contributes — but it produces a "
            "LOCAL, warm, tender protein-rich exudate at the injured sites, peaking at 24–72 hours, "
            "not generalized edema on day 4.",
        "Increased interstitial hydrostatic pressure within a fascial compartment":
            "That is compartment syndrome, which presents within hours as a tense, wood-hard "
            "compartment with pain out of proportion and pain on passive stretch — a surgical "
            "emergency, and confined to the compartment.",
    },
    "Decreased plasma oncotic pressure",
    "Every cause of edema is a failure of one of four Starling variables, and trauma is unusual in "
    "being able to break all four, at different times, in the same patient. The skill is reading WHEN "
    "the swelling started and WHAT IT FEELS LIKE.\n\n"
    "Here albumin has fallen three ways at once, which is why the effect is so marked: capillary leak "
    "of albumin into the interstitium, the acute-phase fall in hepatic albumin synthesis, and dilution "
    "by large-volume crystalloid resuscitation. The result is generalized and DEPENDENT — sacrum, "
    "flanks, both legs, periorbital — and deeply pitting. Crucially, it is not limited to the injured "
    "part, which is what separates it from every other mechanism on this list.\n\n"
    "The four-variable frame, with the six post-traumatic mechanisms as instances:\n"
    "• ↑ Capillary hydrostatic pressure → venous obstruction, deep vein thrombosis, dependency. "
    "Transudate.\n"
    "• ↓ Plasma oncotic pressure → hypoalbuminemia, resuscitation dilution. Transudate, generalized.\n"
    "• ↑ Capillary permeability → inflammation, burns, crush. Exudate.\n"
    "• ↓ Lymphatic drainage → transection, nodal dissection, scarring. Protein-rich, eventually "
    "non-pitting.\n\n"
    "Read the clock, then read the feel. HOURS → inflammation, hematoma, compartment syndrome. DAYS → "
    "deep vein thrombosis, hypoalbuminemia. WEEKS → lymphedema.",
    "Massive fluid resuscitation plus injury has stripped the protein out of his blood, and protein is "
    "what holds water inside vessels. Without it, water leaks out everywhere — which is why he is "
    "puffy around the eyes and not just at the injury.",
)

q(
    "A 31-year-old woman sustains a deep soft tissue contusion of the left thigh in a fall. Over the "
    "next 36 hours the thigh becomes swollen, warm, tender and erythematous, and the swelling pits on "
    "pressure. She is afebrile, the compartment is soft, passive knee movement does not reproduce "
    "disproportionate pain, and the swelling begins to settle by day 5. Which of the following best "
    "describes the mechanism?",
    {
        "Blood dissecting into soft tissue with a subsequent osmotic load":
            "A hematoma is focal, firm and often fluctuant, with discoloration, and it appears "
            "immediately rather than building over 36 hours. Expanding size is its alarm feature.",
        "Increased capillary permeability from inflammatory mediators": "",
        "Lymphatic transection with accumulation of interstitial protein":
            "Lymphatic disruption develops over weeks to months, does not resolve with elevation, and "
            "becomes non-pitting and fibrotic with square toes and a positive Stemmer sign. Hers is "
            "settling by day 5.",
        "Thrombosis of the femoral vein raising upstream hydrostatic pressure":
            "A deep vein thrombosis characteristically announces itself DAYS later, as swelling that "
            "had plateaued or improved begins to worsen again — the opposite of this trajectory — and "
            "typically involves the whole limb with calf tenderness.",
        "Rising pressure within a non-compliant fascial compartment":
            "Compartment syndrome gives a tense, wood-hard compartment with pain out of proportion to "
            "the injury and pain on passive stretch, within hours. The stem explicitly excludes all "
            "three.",
    },
    "Increased capillary permeability from inflammatory mediators",
    "This is the EXPECTED swelling after an injury, and recognizing it as expected is the clinical "
    "point — every other mechanism on the list is something you must not miss.\n\n"
    "Tissue injury releases histamine, bradykinin, complement fragments, interleukin-1 and tumor "
    "necrosis factor, which open interendothelial gaps. Protein-rich fluid — an EXUDATE, as distinct "
    "from the low-protein transudate of a pressure problem — enters the interstitium. It begins within "
    "minutes to hours, peaks at 24–72 hours, and then settles.\n\n"
    "The character matches: local, warm, tender, pitting, accompanied by the other cardinal signs of "
    "inflammation. The negatives in the stem are doing the work — a soft compartment and no "
    "disproportionate pain on passive stretch exclude compartment syndrome, and the improving "
    "trajectory excludes a developing deep vein thrombosis.\n\n"
    "The two emergencies on this differential and how each announces itself:\n"
    "• ACUTE COMPARTMENT SYNDROME — pain out of proportion and pain on passive stretch, within hours. "
    "The six Ps are a trap: pulselessness, pallor and paralysis are late. Treatment is emergency "
    "fasciotomy.\n"
    "• DEEP VEIN THROMBOSIS — suspect it whenever swelling that had plateaued or improved starts "
    "worsening again several days after injury, particularly in an immobilized limb. Confirm with "
    "compression ultrasonography; do not talk yourself out of imaging because the leg is swollen "
    "from the injury.",
    "Injured tissue leaks fluid on purpose — the blood vessels open their seams to let in healing "
    "cells. It swells for a day or two and then settles. The job is to be sure it is this and not one "
    "of the two dangerous causes.",
)

q(
    "A 23-year-old man has a firm, painless right testicular mass. Ultrasonography shows an "
    "intratesticular tumor. He has no palpable inguinal lymphadenopathy. Which nodal group should be "
    "assessed first for metastatic disease?",
    {
        "Deep cervical nodes":
            "These drain the head and neck mucosa. They would matter for a supraclavicular node "
            "signalling distant spread, but they are not the first echelon for any testicular tumor.",
        "External iliac nodes":
            "These lie along the drainage from the lower limb and pelvic wall and are downstream on "
            "several pelvic routes, but they are not the first echelon for the testis.",
        "Obturator and internal iliac nodes of the pelvis":
            "These are the first-echelon nodes for the PROSTATE, which is the other male genitourinary "
            "primary — and prostatic nodal disease precedes the classic osteoblastic bone metastases.",
        "Para-aortic (retroperitoneal) nodes": "",
        "Superficial inguinal nodes":
            "These drain the SCROTAL SKIN, the lower limb, the vulva and the penis. The distinction "
            "between the scrotal skin and the testis inside it is precisely what is being tested, and "
            "it is why the absent inguinal nodes in this stem are reassuring about nothing.",
    },
    "Para-aortic (retroperitoneal) nodes",
    "The testis descended from the posterior abdominal wall and took its lymphatic drainage with it. "
    "Its first-echelon nodes are therefore para-aortic and retroperitoneal, NOT inguinal — despite the "
    "organ now sitting in the scrotum. The ovary follows the same embryologic logic.\n\n"
    "The distinction being tested is between the testis and the SCROTAL SKIN covering it, which drains "
    "to the superficial inguinal nodes like the rest of the lower body surface. A normal inguinal "
    "examination is therefore entirely compatible with bulky retroperitoneal disease, and staging "
    "requires abdominal imaging.\n\n"
    "The rest of the drainage map worth memorizing:\n"
    "• Breast — axillary (levels I–III, defined by their relation to pectoralis minor) for lateral and "
    "upper quadrants, about 75% of the total; internal mammary for medial quadrants\n"
    "• Stomach, pancreas and other abdominal viscera — celiac and para-aortic → thoracic duct → LEFT "
    "supraclavicular node (Virchow's node, Troisier sign)\n"
    "• Anal canal — above the dentate line to internal iliac and inferior mesenteric; below it to "
    "superficial inguinal\n"
    "• Lung — hilar → mediastinal → supraclavicular, with mediastinal status the pivot of resectability\n"
    "• Prostate — obturator and internal iliac\n"
    "• Head and neck mucosa — cervical chains (levels I–VI)\n\n"
    "The governing rule for the whole objective: carcinomas spread preferentially by lymphatics, "
    "sarcomas preferentially by blood.",
    "The testicle started life high in the abdomen and only later dropped into the scrotum — but it "
    "kept its original plumbing. So its cancer drains to nodes beside the aorta, not to the groin.",
)

q(
    "A 58-year-old woman has a squamous cell carcinoma of the anal canal. The tumor is centered 2 cm "
    "BELOW the dentate line. Which nodal group is the first echelon of drainage for this tumor?",
    {
        "Celiac nodes":
            "These drain the foregut — stomach, duodenum, pancreas, liver and spleen — and feed onward "
            "to the cisterna chyli and thoracic duct.",
        "Inferior mesenteric nodes of the hindgut":
            "These, with the internal iliac nodes, drain the anal canal ABOVE the dentate line. Naming "
            "them here is the error the question is built around.",
        "Para-aortic nodes":
            "These are the first echelon for the testis and ovary, and a downstream station for much "
            "of the abdomen. They are not the first-echelon nodes for the distal anal canal.",
        "Superficial inguinal nodes": "",
        "Superior mesenteric nodes":
            "These drain the midgut, from the distal duodenum to the proximal two-thirds of the "
            "transverse colon — proximal to the region in question.",
    },
    "Superficial inguinal nodes",
    "The dentate line is a watershed for LYMPHATIC drainage as well as for blood supply and "
    "innervation — that is the single fact this question tests, and it is one of the three drainage "
    "points with the strongest examination history.\n\n"
    "• ABOVE the dentate line → internal iliac and inferior mesenteric nodes (the hindgut/visceral "
    "route)\n"
    "• BELOW the dentate line → superficial inguinal nodes (the somatic, body-surface route)\n\n"
    "The embryology behind it is the same principle that explains the testis: above the line is "
    "endodermal hindgut, below it is ectodermal, and each keeps the drainage of its origin. It also "
    "explains why sensation, epithelium and venous drainage all change at the same point.\n\n"
    "Clinically this determines the radiation field and where you examine. A tumor below the line "
    "requires the inguinal nodes to be assessed and usually included in treatment; one above it does "
    "not.\n\n"
    "Read a suspicious node the way the lecture describes: metastatic nodes are hard, painless, FIXED "
    "to underlying tissue, often matted, and progressively enlarging. Fixation is the ominous feature, "
    "because it means tumor has breached the capsule — extranodal extension, which independently "
    "worsens prognosis. Reactive nodes are soft or rubbery, mobile and tender, follow a local "
    "infection, and regress.",
    "A line inside the anal canal marks where the gut's original tissue meets skin-type tissue. Above "
    "it, drainage goes deep into the abdomen; below it, straight to the groin — so where the tumor "
    "sits decides where to look for spread.",
)
