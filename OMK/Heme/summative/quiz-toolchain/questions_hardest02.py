# Hardest Exam — batch H2 of 5 (questions 21–40)
# Sections §15–§28: hemostasis pharmacology, anemia pharmacology, sepsis, HIV, vector-borne
# infection, viral hemorrhagic fever, laboratory foundations, benign white cell disorders.

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


# ── 21. Warfarin-induced skin necrosis (§15) ────────────────────────────────────
q(
    "A 44-year-old woman comes to the emergency department due to a painful, darkening lesion on "
    "her left thigh. Four days ago she was diagnosed with a proximal deep vein thrombosis and "
    "started on warfarin; no parenteral anticoagulant was given. Her brother had an unprovoked "
    "pulmonary embolism at age 30. Her platelet count is 268,000/mm3 and the international "
    "normalized ratio is 3.1. The lesion is shown. Biopsy of the affected skin shows fibrin "
    "thrombi occluding dermal and subcutaneous venules with hemorrhagic necrosis of the overlying "
    "tissue and no vasculitis. Which of the following best explains this patient's lesion?",
    {
        "Antibodies against a heparin-platelet factor 4 complex":
            "This is heparin-induced thrombocytopenia, which also causes thrombosis with skin "
            "necrosis — but it requires heparin exposure, and the platelet count falls by more than "
            "half. She received no heparin and her platelets are normal.",
        "Calcium phosphate deposition in small vessels":
            "This is calciphylaxis, which produces very similar painful necrotic skin lesions — but "
            "in patients with end-stage kidney disease and disordered calcium and phosphate, not "
            "4 days after starting a drug.",
        "Faster decline of protein C than prothrombin": "",
        "Immune complex deposition in venule walls":
            "This is leukocytoclastic vasculitis, which shows fibrinoid necrosis of vessel walls with "
            "a neutrophilic infiltrate and nuclear dust. The biopsy explicitly shows bland thrombi "
            "without vasculitis.",
        "Mutant factor V resisting inactivation by protein C":
            "Factor V Leiden explains why she and her brother clot in the first place, and it "
            "amplifies this complication — but on its own it does not produce skin necrosis in the "
            "first days of a new drug.",
    },
    "Faster decline of protein C than prothrombin",
    "Warfarin-induced skin necrosis, from starting warfarin without bridging.\n\n"
    "Warfarin inhibits vitamin K epoxide reductase → the liver cannot carboxylate factors II, VII, "
    "IX and X, or the natural anticoagulants protein C and protein S. Those proteins do not "
    "disappear at the same rate — each falls at the pace of its own half-life:\n"
    "• Factor VII ~4–6 hours (shortest) — this is what moves the INR first\n"
    "• Protein C ~8 hours — the natural ANTICOAGULANT\n"
    "• Factor IX ~24 hours\n"
    "• Factor X ~48–72 hours\n"
    "• Factor II (prothrombin) ~60 hours (longest)\n\n"
    "So in the first days the body loses protein C before it loses prothrombin → a transient "
    "HYPERcoagulable window → thrombosis of dermal and subcutaneous venules, classically over fatty "
    "areas (thigh, breast, buttock) → hemorrhagic skin necrosis. The risk is greatest in those with "
    "underlying protein C deficiency or another thrombophilia, and after a large loading dose.\n\n"
    "The same arithmetic explains the other trap: an INR of 2.3 on day 2 reflects loss of factor "
    "VII, not true anticoagulation, because prothrombin is still present. Both problems have one "
    "fix — bridge with heparin or enoxaparin for at least 5 days AND until the INR has been "
    "therapeutic for 24 hours.\n\n"
    "Educational objective: Warfarin depletes protein C faster than prothrombin, creating a "
    "transient hypercoagulable state in the first days of therapy that can cause skin necrosis over "
    "fatty areas. Bridging with a heparin until the INR has been therapeutic for 24 hours, for at "
    "least 5 days, prevents both this and inadequate early anticoagulation.",
    "Warfarin switches off both the body's clot-makers and its clot-brakes, and the brakes wear off "
    "first. For a few days she was actually more likely to clot, so tiny vessels in her skin "
    "blocked and the skin died.",
    image="fig_warfarin_necrosis",
    imcap="Photograph of the lateral thigh. There is a well-demarcated area of black, necrotic "
          "tissue with a friable, hyperemic border and surrounding erythema.",
    exim="fig_slide_warf_onset",
    excap="Clotting factor half-lives — protein C falls well before prothrombin, which is the whole "
          "reason bridging exists.",
)

# ── 22. Warfarin drug interaction — CYP2C9 inhibition (§15) ─────────────────────
q(
    "A 71-year-old man comes to the emergency department due to 2 days of painless gross hematuria "
    "and new bruises over both forearms. He has atrial fibrillation and has taken warfarin for 3 "
    "years, with an international normalized ratio consistently between 2.2 and 2.6 at monthly "
    "checks. Five days ago he was prescribed fluconazole for esophageal candidiasis. He takes no "
    "other new medications, has not changed his diet, and does not drink alcohol. Vital signs are "
    "stable.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 11.4 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 34% (N=41%–53%)\n"
    "Platelet count 232,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 52 sec (N=11–15 sec)\n"
    "International normalized ratio 6.9 (N=0.9–1.1)\n\n"
    "Which of the following best explains this patient's laboratory findings?",
    {
        "Additive inhibition of platelet aggregation":
            "This is how aspirin and other nonsteroidal anti-inflammatory drugs raise bleeding risk "
            "with warfarin — a pharmacodynamic interaction that leaves the INR UNCHANGED. His INR "
            "has nearly tripled.",
        "Decreased hepatic metabolism of warfarin": "",
        "Increased hepatic clearance by enzyme induction":
            "Rifampin, carbamazepine, phenytoin and St John's wort induce metabolism, which LOWERS "
            "the INR and risks clotting. That is the opposite direction.",
        "Loss of gut flora that synthesize vitamin K":
            "This is the pharmacodynamic half of the antibiotic interaction and does raise the INR — "
            "but fluconazole is an antifungal and does not eliminate the vitamin K-producing "
            "bacterial flora.",
        "Reduced dietary intake of vitamin K":
            "A sudden fall in leafy green intake raises the INR, and a sudden rise lowers it. His "
            "diet is explicitly unchanged.",
        "Variant VKORC1 conferring target sensitivity":
            "Polymorphisms in VKORC1 and CYP2C9 explain why dose requirements differ so much between "
            "patients — but they are present from the start and would not let him run a stable INR "
            "for 3 years before suddenly changing.",
    },
    "Decreased hepatic metabolism of warfarin",
    "A pharmacokinetic drug-drug interaction. Fluconazole inhibits CYP2C9, the enzyme that clears "
    "warfarin → warfarin accumulates → the vitamin K-dependent factors II, VII, IX and X fall "
    "further → INR rises → bleeding.\n\n"
    "The warfarin interaction list is the highest-yield in hematology, and it sorts by mechanism:\n"
    "• ↑ INR by CYP2C9 INHIBITION — amiodarone, metronidazole, trimethoprim-sulfamethoxazole, "
    "fluconazole, ciprofloxacin, fluvoxamine\n"
    "• ↓ INR by enzyme INDUCTION — rifampin, carbamazepine, phenytoin, St John's wort\n"
    "• ↑ bleeding at an UNCHANGED INR — aspirin, other antiplatelets, nonsteroidal "
    "anti-inflammatory drugs (pharmacodynamic)\n"
    "• ↑ INR from LESS SUBSTRATE — any antibiotic that kills vitamin K-producing gut flora\n"
    "• Food and drink — a sudden increase in leafy greens lowers the INR (consistency matters more "
    "than avoidance); an acute alcohol binge raises it, while chronic use induces and lowers it\n\n"
    "Management here: hold warfarin, give vitamin K, and for serious or life-threatening bleeding "
    "add 4-factor prothrombin complex concentrate — which corrects the INR immediately, while "
    "vitamin K restores his own ability to make factors so the INR does not rebound as the "
    "concentrate clears.\n\n"
    "Educational objective: Azole antifungals, amiodarone, metronidazole and "
    "trimethoprim-sulfamethoxazole inhibit CYP2C9 and raise the INR in patients on warfarin, "
    "whereas rifampin and other inducers lower it. Antiplatelet drugs increase bleeding without "
    "changing the INR.",
    "The new antifungal pill blocks the liver enzyme that normally chews up his blood thinner, so "
    "the thinner piled up and his blood stopped clotting at all.",
    exim="fig_slide_warf_reversal",
    excap="Stepwise reversal of warfarin anticoagulation.",
)

# ── 23. Thrombolysis and intracranial hemorrhage (§16) ──────────────────────────
q(
    "A 68-year-old man is brought to the emergency department due to sudden right-sided weakness "
    "and difficulty speaking that began 90 minutes ago. He takes low-dose aspirin and a statin. "
    "Blood pressure is 168/92 mm Hg. Noncontrast head computed tomography shows no hemorrhage, and "
    "intravenous alteplase is started. Two hours later he develops a severe headache, vomiting, and "
    "a declining level of consciousness, and he dies the following day. A coronal section of the "
    "brain at autopsy is shown. Which of the following drug actions is most directly responsible "
    "for this complication?",
    {
        "Blockade of platelet adenosine diphosphate receptors":
            "This is clopidogrel and the other P2Y12 blockers. They raise bleeding risk modestly but "
            "do not dissolve established fibrin, and he was not taking one.",
        "Conversion of plasminogen to plasmin": "",
        "Inhibition of platelet cyclooxygenase-1":
            "This is his aspirin, which irreversibly acetylates cyclooxygenase-1 and blocks "
            "thromboxane A2 for the platelet's 7–10 day life. It contributes to bleeding risk but "
            "cannot lyse an intracranial clot within 2 hours.",
        "Inhibition of vitamin K epoxide reductase":
            "This is warfarin's mechanism, producing bleeding through a multiple factor deficiency "
            "over days. He is not on warfarin, and the event was immediate.",
        "Potentiation of antithrombin activity":
            "This is how the heparins work. Heparin-associated bleeding is possible, but he received "
            "a plasminogen activator, which is far more likely to cause intracranial hemorrhage.",
    },
    "Conversion of plasminogen to plasmin",
    "Intracranial hemorrhage after thrombolysis — the feared complication of the -plase drugs, and "
    "the reason their contraindication list exists.\n\n"
    "Mechanism: alteplase (recombinant tissue plasminogen activator) converts plasminogen → plasmin "
    "→ plasmin digests the fibrin mesh holding a clot together (fibrin degradation products are "
    "measured as the D-dimer). These agents are only RELATIVELY fibrin-selective, so hemostatic "
    "plugs elsewhere are lysed too — systemic bleeding is the defining risk, and bleeding into the "
    "brain is the one you cannot take back.\n\n"
    "If catastrophic bleeding occurs: stop the infusion, image the head, give CRYOPRECIPITATE to "
    "replace the fibrinogen plasmin has consumed, and give an ANTIFIBRINOLYTIC — tranexamic acid or "
    "aminocaproic acid — which blocks plasminogen from becoming plasmin, the exact mirror image of "
    "the drug.\n\n"
    "The contraindications all follow from 'you are about to dissolve every clot in the body': prior "
    "intracranial hemorrhage, ischemic stroke within 3 months, intracranial neoplasm or vascular "
    "malformation, suspected aortic dissection, active internal bleeding or bleeding diathesis, "
    "significant closed head trauma within 3 months, and severe uncontrolled hypertension.\n\n"
    "Educational objective: Thrombolytics (alteplase, reteplase, tenecteplase) convert plasminogen "
    "to plasmin, which degrades fibrin; intracranial hemorrhage is the feared complication. "
    "Treatment is to stop the drug, replace fibrinogen with cryoprecipitate, and give tranexamic or "
    "aminocaproic acid to block further plasmin generation.",
    "The clot-busting drug switches on the body's demolition crew to chew up a clot in a brain "
    "artery. The crew does not only work where you want it to, so it also tore open a vessel and "
    "the brain bled.",
    image="fig_hx_ich_gross",
    imcap="Coronal section of the brain at autopsy. A large, dark, blood-filled cavity (diamond) "
          "occupies the deep gray matter of one hemisphere, destroying the surrounding tissue and "
          "shifting the midline.",
    exim="fig_slide_fibrinolysis",
    excap="The fibrinolysis diagram — plasminogen activators on one side, tranexamic and "
          "aminocaproic acid blocking the same step on the other.",
)

# ── 24. Anticoagulation in pregnancy (§15) ──────────────────────────────────────
q(
    "A 30-year-old woman, gravida 2 para 1, at 9 weeks' gestation comes to the office due to 3 days "
    "of left calf pain and swelling. She has no chronic medical conditions and takes only a "
    "prenatal vitamin. The left calf is 4 cm larger in circumference than the right and is tender "
    "along the deep venous course. Compression ultrasonography shows a noncompressible left "
    "popliteal vein with thrombus extending into the femoral vein. Serum creatinine is 0.7 mg/dL "
    "(N=0.6–1.2 mg/dL). Which of the following is the most appropriate anticoagulant for this "
    "patient?",
    {
        "Apixaban":
            "Direct oral factor Xa inhibitors are convenient and need no monitoring, but safety in "
            "pregnancy is not established, so they are avoided.",
        "Dabigatran":
            "The same problem as the -xabans: a direct oral anticoagulant with no established "
            "pregnancy safety data. It is also the one reversed by idarucizumab, which is irrelevant "
            "here.",
        "Enoxaparin": "",
        "Fondaparinux":
            "This synthetic pentasaccharide is the agent of choice in heparin-induced "
            "thrombocytopenia, but pregnancy data are limited and it has NO effective reversal agent "
            "— protamine does not work.",
        "Warfarin":
            "Warfarin is teratogenic (fetal warfarin syndrome) and is contraindicated in pregnancy. "
            "It is small enough to cross the placenta, which is precisely the difference from the "
            "heparins.",
    },
    "Enoxaparin",
    "Acute proximal deep vein thrombosis in the first trimester. Pregnancy is a hypercoagulable "
    "state, and the anticoagulant choice is decided by what crosses the placenta.\n\n"
    "Heparins — unfractionated and low-molecular-weight — are large, highly charged molecules that "
    "do NOT cross the placenta, so they are the anticoagulants of pregnancy. Low-molecular-weight "
    "heparin is preferred for an outpatient: predictable dosing, no routine monitoring (check an "
    "anti-factor Xa level in pregnancy, obesity or renal impairment), subcutaneous administration, "
    "and a lower risk of heparin-induced thrombocytopenia than unfractionated heparin.\n\n"
    "Warfarin is small, crosses the placenta, and is teratogenic. Direct oral anticoagulants are "
    "avoided because safety is not established.\n\n"
    "The rest of the agent-selection logic, for contrast: severe renal impairment → unfractionated "
    "heparin (not renally cleared); a need to stop quickly → unfractionated heparin (short half-life "
    "plus full reversal with protamine); heparin-induced thrombocytopenia → argatroban, bivalirudin "
    "or fondaparinux, never a heparin and never warfarin alone; mechanical heart valve → warfarin; "
    "routine outpatient venous thromboembolism or atrial fibrillation → a direct oral "
    "anticoagulant, usually apixaban.\n\n"
    "Educational objective: Heparins do not cross the placenta and are the anticoagulants of choice "
    "in pregnancy, with low-molecular-weight heparin preferred for outpatient therapy. Warfarin is "
    "teratogenic and direct oral anticoagulants lack established pregnancy safety data.",
    "Her blood thinner has to be one that cannot cross into the baby. Heparin shots are too big to "
    "get across; warfarin pills are small enough and can hurt the baby.",
)

# ── 25. Clopidogrel and omeprazole — stent thrombosis (§16) ─────────────────────
q(
    "A 58-year-old man comes to the emergency department due to 40 minutes of crushing substernal "
    "chest pain. Three weeks ago he underwent percutaneous coronary intervention with a "
    "drug-eluting stent to the left anterior descending artery and was discharged on aspirin 81 mg "
    "and clopidogrel daily, which he has taken without missing a dose. Two weeks ago his primary "
    "physician added omeprazole for dyspepsia. ECG shows ST-segment elevation in leads V2 through "
    "V4. Platelet count is 244,000/mm3. Coronary angiography shows a fresh occlusive thrombus "
    "within the previously placed stent. Which of the following best explains this patient's "
    "presentation?",
    {
        "Antibody-mediated activation of platelets":
            "Heparin-induced thrombocytopenia does cause arterial and venous thrombosis, but it "
            "requires heparin exposure within the preceding days to weeks and produces a platelet "
            "count that has fallen by more than half. His count is normal.",
        "Decreased formation of the active metabolite": "",
        "Increased platelet turnover restoring cyclooxygenase":
            "New platelets restore thromboxane production only if aspirin is stopped, because "
            "aspirin inhibits cyclooxygenase-1 irreversibly for each platelet's life. He has taken "
            "his aspirin.",
        "Loss of prostacyclin from a high aspirin dose":
            "This is the aspirin dose paradox: higher doses also inhibit endothelial cyclooxygenase-2 "
            "and the prostacyclin it makes. He is on 81 mg, the antiplatelet dose.",
        "Resistance of factor V to activated protein C":
            "Factor V Leiden is a venous thrombophilia — deep vein thrombosis and pulmonary "
            "embolism. Stent thrombosis is a platelet-rich arterial event.",
    },
    "Decreased formation of the active metabolite",
    "Stent thrombosis from a pharmacokinetic drug interaction.\n\n"
    "Clopidogrel is a PRODRUG. It requires hepatic CYP2C19 to be converted to its active metabolite, "
    "which then irreversibly blocks the platelet P2Y12 adenosine diphosphate receptor. Omeprazole "
    "inhibits CYP2C19 → less active metabolite → inadequate platelet inhibition → thrombosis inside "
    "a stent whose struts are not yet covered by endothelium.\n\n"
    "What to do instead: pantoprazole, which does not meaningfully inhibit CYP2C19, or switch to "
    "ticagrelor, which is not a prodrug (but causes dyspnea and bradyarrhythmias, and requires "
    "maintenance aspirin ≤ 100 mg/day). Genetic CYP2C19 poor metabolizers have the same problem "
    "without any interacting drug.\n\n"
    "The class in one line each: clopidogrel needs activation; prasugrel is more potent and is "
    "contraindicated after stroke or transient ischemic attack; ticagrelor is reversible and not a "
    "prodrug; cangrelor is intravenous with onset and offset in minutes. And the framing rule — "
    "arterial 'white clots' are platelet-rich and treated with antiplatelet drugs, while venous "
    "'red clots' are fibrin-rich and treated with anticoagulants.\n\n"
    "Educational objective: Clopidogrel is a prodrug activated by CYP2C19, so CYP2C19 inhibitors "
    "such as omeprazole blunt its antiplatelet effect and can precipitate stent thrombosis. "
    "Pantoprazole or a non-prodrug P2Y12 inhibitor such as ticagrelor avoids the interaction.",
    "His anti-clot pill only works after the liver switches it on. The heartburn pill blocked that "
    "switch, so his platelets stayed sticky and a clot formed inside the new stent.",
    exim="fig_slide_kp_antiplatelet",
    excap="The antiplatelet summary — mechanism, activation requirement and interactions by agent.",
)

# ── 26. Acute iron poisoning in a toddler (§17) ─────────────────────────────────
q(
    "A 2-year-old girl is brought to the emergency department 3 hours after being found with an "
    "open bottle of her mother's ferrous sulfate tablets. She has vomited five times, twice with "
    "blood, and has had two episodes of bloody diarrhea. She is lethargic. Blood pressure is 74/40 "
    "mm Hg and pulse is 168/min.\n\n"
    "Laboratory studies show:\n"
    "Sodium 138 mEq/L (N=136–146 mEq/L)\n"
    "Bicarbonate 11 mEq/L (N=22–28 mEq/L)\n"
    "Glucose 186 mg/dL (N=70–100 mg/dL)\n"
    "Anion gap 24 mEq/L (N=8–12 mEq/L)\n\n"
    "Abdominal radiography shows multiple radiopaque tablets in the stomach. Which of the following "
    "is the most appropriate pharmacotherapy?",
    {
        "Activated charcoal":
            "Charcoal adsorbs many ingested drugs but binds iron poorly, so it does not help here. "
            "Whole bowel irrigation is the decontamination option in a massive ingestion.",
        "Deferasirox":
            "An ORAL chelator for chronic transfusional iron overload, dosed once daily and carrying "
            "boxed warnings for renal failure, hepatic failure and gastrointestinal hemorrhage. It "
            "is not the acute antidote, and this child cannot keep anything down.",
        "Deferiprone":
            "Also an oral chelator for chronic overload, given three times daily, with a boxed "
            "warning for agranulocytosis requiring weekly white cell counts.",
        "Deferoxamine": "",
        "Dimercaprol":
            "A chelator for arsenic, gold and severe lead poisoning. Lead would give a microcytic "
            "anemia with basophilic stippling, not radiopaque tablets and hemorrhagic gastritis.",
        "Succimer":
            "The oral chelator used for childhood lead poisoning. Wrong metal — and there is no "
            "history of exposure to lead paint or pica here.",
    },
    "Deferoxamine",
    "Acute iron poisoning — one of the leading causes of poisoning death in young children, and "
    "classically an accidental ingestion of an adult's iron tablets.\n\n"
    "Mechanism and staging: free iron is directly corrosive to gastrointestinal mucosa → vomiting, "
    "hematemesis and bloody diarrhea from hemorrhagic gastritis, with hypovolemia from fluid loss. "
    "Absorbed iron then uncouples oxidative phosphorylation and impairs mitochondrial function → "
    "anion-gap metabolic acidosis, shock, and later hepatic necrosis.\n\n"
    "The antidote is DEFEROXAMINE, given parenterally: it chelates free iron and is excreted in the "
    "urine, classically turning it a reddish 'vin rosé' colour. Supportive care and, in massive "
    "ingestion, whole bowel irrigation accompany it. Radiopaque tablets on an abdominal film "
    "confirm a substantial ingestion and identify tablets still available for removal.\n\n"
    "Keep the three chelators straight: deferasirox (oral, once daily; renal, hepatic and "
    "gastrointestinal bleeding warnings), deferiprone (oral, three times daily; agranulocytosis), "
    "and deferoxamine (parenteral, 8–12 hour infusions, ocular and auditory toxicity) — which is "
    "also the acute antidote.\n\n"
    "Educational objective: Acute iron overdose causes hemorrhagic gastroenteritis, shock and an "
    "anion-gap metabolic acidosis, and is treated with parenteral deferoxamine. The oral chelators "
    "deferasirox and deferiprone are for chronic transfusional iron overload.",
    "The iron pills burned the inside of her stomach and then poisoned her cells. The medicine given "
    "grabs onto the loose iron and carries it out in her pee.",
    exim="fig_slide_iron_toxicity",
    excap="Reversal of acute iron toxicity and chronic iron overload — the three chelators side by "
          "side.",
)

# ── 27. Erythropoiesis-stimulating agent — rate and ceiling (§17) ───────────────
q(
    "A 66-year-old man comes to the office for follow-up of anemia of chronic kidney disease. He "
    "has received hemodialysis for 3 years and epoetin alfa for the past 6 weeks. He reports a "
    "dull headache for several days. His hemoglobin was 9.2 g/dL two weeks ago and is 10.9 g/dL "
    "today. Ferritin is 420 ng/mL (N=20–250 ng/mL) and transferrin saturation is 32% (N=20%–50%). "
    "Blood pressure is 176/102 mm Hg, compared with 138/84 mm Hg before treatment was started. "
    "Which of the following is the most appropriate next step in management?",
    {
        "Add intravenous iron sucrose":
            "Functional iron deficiency is the commonest reason an erythropoiesis-stimulating agent "
            "appears not to work — but his ferritin and transferrin saturation show replete stores, "
            "and his hemoglobin is rising too fast, not too slowly.",
        "Continue the current dose unchanged":
            "This ignores both boxed-warning rules at once: the rate of rise and the developing "
            "hypertension, which is the most common adverse effect of the class and has progressed "
            "to symptoms.",
        "Decrease the epoetin alfa dose": "",
        "Increase the dose to target 12 g/dL":
            "Targeting hemoglobin above 11 g/dL increases death, serious cardiovascular events and "
            "stroke in chronic kidney disease, with no additional benefit. The goal is the lowest "
            "dose that avoids transfusion.",
        "Switch to oral vadadustat":
            "The hypoxia-inducible factor prolyl hydroxylase inhibitor is an oral alternative for "
            "dialysis patients, but it carries its own boxed warning for thrombotic events and is "
            "contraindicated in uncontrolled hypertension — exactly what he now has.",
        "Transfuse one unit of red blood cells":
            "Transfusion is for symptomatic anemia, usually below a hemoglobin of 7 g/dL. His "
            "hemoglobin is 10.9 and climbing.",
    },
    "Decrease the epoetin alfa dose",
    "Two numbers govern erythropoiesis-stimulating agent dosing, and this patient has broken both.\n\n"
    "• The CEILING — every boxed warning turns on the same threshold: targeting a hemoglobin above "
    "11 g/dL causes harm with no benefit (increased death, myocardial infarction, stroke, venous "
    "thromboembolism and vascular access thrombosis).\n"
    "• The RATE — if the hemoglobin rises more than 1 g/dL in any 2-week period, decrease the dose. "
    "His rose 1.7 g/dL.\n\n"
    "Why the rate matters: hypertension is the most common adverse effect, occurring in up to a "
    "third of treated patients, and a rapid rise in red cell mass drives it. Hypertensive "
    "encephalopathy has been reported, and seizures are a recognised risk in chronic kidney "
    "disease. Control blood pressure before starting, and note that subcutaneous dosing raises blood "
    "pressure less and reaches target at 15%–30% lower doses than intravenous.\n\n"
    "Mechanism for context: these agents stimulate division and differentiation of committed "
    "erythroid progenitors and push reticulocytes into the blood — reticulocytes rise first, then "
    "hematocrit and hemoglobin. They are approved for anemia of chronic kidney disease and "
    "chemotherapy-induced anemia, only when the goal is avoiding transfusion, and only after iron "
    "stores are checked and repleted.\n\n"
    "Educational objective: Erythropoiesis-stimulating agents should be dosed to the lowest level "
    "that avoids transfusion; targeting a hemoglobin above 11 g/dL increases cardiovascular events "
    "and death, and a rise of more than 1 g/dL in 2 weeks requires a dose reduction. Hypertension "
    "is the most common adverse effect.",
    "The medicine tells his marrow to build red cells, and it worked too fast. Thicker blood pushed "
    "his blood pressure up, so the dose comes down rather than up.",
    exim="fig_slide_esa_ae",
    excap="Adverse effects of erythropoiesis-stimulating agents.",
)

# ── 28. Methotrexate toxicity — leucovorin rescue (§17) ─────────────────────────
q(
    "A 62-year-old woman comes to the emergency department due to 4 days of mouth pain and "
    "inability to eat. She has rheumatoid arthritis treated with methotrexate 15 mg once weekly. "
    "Two weeks ago she misread a new prescription label and has been taking 15 mg daily since. "
    "Examination shows confluent oral ulceration.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.9 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 27% (N=36%–46%)\n"
    "Mean corpuscular volume 109 µm3 (N=80–100 µm3)\n"
    "Leukocyte count 1,300/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 48,000/mm3 (N=150,000–400,000/mm3)\n"
    "Creatinine 1.1 mg/dL (N=0.6–1.2 mg/dL)\n\n"
    "The peripheral smear shows macro-ovalocytes and hypersegmented neutrophils. In addition to "
    "stopping the drug and providing supportive care, which of the following is the most "
    "appropriate pharmacotherapy?",
    {
        "Cyanocobalamin":
            "Vitamin B12 replacement treats deficiency from pernicious anemia, ileal disease, "
            "metformin or proton pump inhibitors. Her folate pathway is blocked by a drug; her B12 "
            "supply is not the problem.",
        "Epoetin alfa":
            "An erythropoiesis-stimulating agent shouts a build order at a marrow that cannot "
            "synthesize DNA. It also takes weeks to work and does nothing for her mucositis or her "
            "low platelets and neutrophils.",
        "Filgrastim":
            "Granulocyte colony-stimulating factor can shorten neutropenia and may be used "
            "adjunctively, but it addresses one lineage only and does not restore the blocked folate "
            "pathway causing all three cytopenias and the mucositis.",
        "Folic acid":
            "This is the trap. Folic acid still requires dihydrofolate reductase to be converted to "
            "its active form — and that is precisely the enzyme methotrexate has blocked. You are "
            "handing the cell a substrate it cannot activate.",
        "Leucovorin": "",
    },
    "Leucovorin",
    "Methotrexate toxicity from a dosing error — weekly therapy taken daily. Methotrexate inhibits "
    "DIHYDROFOLATE REDUCTASE → no tetrahydrofolate → thymidine synthesis fails → DNA synthesis "
    "stops in the fastest-dividing tissues.\n\n"
    "That single mechanism produces the whole picture: the marrow empties (pancytopenia with a "
    "MACROCYTIC anemia, macro-ovalocytes and hypersegmented neutrophils — the same megaloblastic "
    "morphology as B12 or folate deficiency, because the biochemical lesion is the same), the gut "
    "mucosa ulcerates (her stomatitis), and hair is lost.\n\n"
    "Leucovorin (folinic acid) is already PAST the blocked step: it is converted directly to active "
    "folate forms without needing dihydrofolate reductase, restoring the folate pool. That is what "
    "'leucovorin rescue' means — you are not reversing methotrexate, you are handing the cell an "
    "activated folate it can still use. Giving plain folic acid instead is useless.\n\n"
    "Supportive measures matter too: hydration and urinary alkalinization promote methotrexate "
    "excretion (it is renally cleared, so kidney impairment prolongs exposure), and glucarpidase is "
    "available for severe toxicity with renal failure.\n\n"
    "Educational objective: Methotrexate inhibits dihydrofolate reductase, producing megaloblastic "
    "pancytopenia and mucositis. The antidote is leucovorin (folinic acid), which bypasses the "
    "blocked enzyme; folic acid is ineffective because it requires that same enzyme for activation.",
    "Her arthritis drug blocks the machine that turns the vitamin folate into its usable form. "
    "Giving more raw vitamin does nothing, so doctors give the already-usable form instead.",
    exim="fig_slide_folate",
    excap="The folate pathway — methotrexate blocks dihydrofolate reductase; folinic acid enters "
          "beyond that step.",
)

# ── 29. Sepsis — the acid-base signature (§18) ──────────────────────────────────
q(
    "A 78-year-old woman is brought to the emergency department from a nursing home due to 1 day of "
    "confusion. She has a productive cough that began 3 days ago. Temperature is 35.6 C (96.1 F), "
    "blood pressure is 94/52 mm Hg, pulse is 118/min, and respirations are 26/min. She is "
    "disoriented to place and time. Crackles are heard at the right lung base. Chest radiography "
    "shows a right lower lobe infiltrate. Her leukocyte count is 3,200/mm3 with 14% band forms, "
    "platelet count is 88,000/mm3, creatinine is 1.9 mg/dL (baseline 1.0 mg/dL), and serum lactate "
    "is 4.6 mmol/L (N=0.5–2.2 mmol/L). Arterial blood gas analysis in this patient would most "
    "likely show which of the following?",
    {
        "Metabolic acidosis with respiratory acidosis":
            "This combination appears when a patient can no longer sustain the compensatory "
            "hyperventilation — exhaustion, an obstructive lung disease with carbon dioxide "
            "retention, or opioid sedation. She is breathing 26 times a minute.",
        "Metabolic acidosis with respiratory alkalosis": "",
        "Metabolic alkalosis with respiratory acidosis":
            "This is chronic carbon dioxide retention with renal compensation, or vomiting in a "
            "hypoventilating patient. It does not fit a lactate of 4.6.",
        "Metabolic alkalosis with respiratory alkalosis":
            "Seen with protracted vomiting in a hyperventilating patient — for example pregnancy or "
            "liver failure. Lactic acid production makes an alkalosis impossible here.",
        "Normal acid-base status with hypoxemia":
            "Hypoxemia alone occurs in an uncomplicated pneumonia, but tissue hypoperfusion with a "
            "lactate of 4.6 mmol/L has already moved her beyond that.",
        "Pure respiratory alkalosis":
            "Early sepsis, anxiety and pulmonary embolism can all give an isolated respiratory "
            "alkalosis. Once lactate accumulates from hypoperfusion, a metabolic acidosis is present "
            "as well.",
    },
    "Metabolic acidosis with respiratory alkalosis",
    "Sepsis from community-acquired pneumonia — life-threatening organ dysfunction from a "
    "dysregulated host response to infection. Her qSOFA is 3 of 3 (respiratory rate ≥ 22, systolic "
    "blood pressure ≤ 100 mm Hg, altered mentation), and organ dysfunction is documented in several "
    "systems.\n\n"
    "The acid-base pattern is the classic simultaneous pairing:\n"
    "• METABOLIC ACIDOSIS — hypoperfusion → anaerobic metabolism → lactate\n"
    "• RESPIRATORY ALKALOSIS — tachypnea, which is both an early direct effect of inflammatory "
    "mediators and the compensation for the acidosis\n\n"
    "Two traps in the laboratory data are deliberate. Her temperature is LOW and her white count is "
    "LOW: the criteria are bidirectional — hypothermia counts as much as fever, and leukopenia "
    "(< 4,000/µL) or a normal count with more than 10% immature forms counts as much as leukocytosis "
    "(> 12,000/µL). A 'normal-looking' number can still be an abnormal response.\n\n"
    "The rest of the panel maps organ by organ: thrombocytopenia (consumption), rising creatinine "
    "and oliguria (renal), bilirubin > 4 mg/dL (hepatic), PaO2/FiO2 < 300 (pulmonary), hyperglycemia "
    "(stress response). Procalcitonin is the one marker that points at a bacterial cause; cultures "
    "are negative in 30%–50% of cases. Management is bundled because the dysfunction is "
    "time-dependent: bactericidal antibiotics, intravenous fluids, lactate measurement, perfusion "
    "reassessment, vasopressors if needed, plus oxygen and source control.\n\n"
    "Educational objective: Sepsis classically produces a metabolic acidosis from lactate "
    "accumulation together with a respiratory alkalosis from tachypnea. Hypothermia and leukopenia "
    "satisfy the systemic inflammatory criteria as fully as fever and leukocytosis.",
    "Her body is not getting enough oxygen to its tissues, so they make acid. She breathes fast to "
    "blow off carbon dioxide, which pushes the blood the other way at the same time.",
    exim="fig_slide_sepsis_labs",
    excap="The laboratory features of sepsis — most rows measure severity; only procalcitonin points "
          "at a cause.",
)

# ── 30. The viral trigger of sepsis — DAMPs (§18) ───────────────────────────────
q(
    "A 63-year-old man is admitted to the intensive care unit due to 2 days of fever, myalgia and "
    "worsening dyspnea during a winter influenza outbreak. Temperature is 39.1 C (102.4 F), blood "
    "pressure is 82/48 mm Hg despite 3 L of intravenous fluid, and oxygen saturation is 88% on "
    "high-flow oxygen. Chest radiography shows bilateral infiltrates. Serum lactate is 5.2 mmol/L "
    "(N=0.5–2.2 mmol/L) and creatinine is 2.4 mg/dL (N=0.6–1.2 mg/dL). A nasopharyngeal swab is "
    "positive for influenza A by polymerase chain reaction. Blood, urine and sputum cultures show "
    "no growth at 48 hours, procalcitonin is within normal limits, and serum beta-D-glucan is "
    "negative. Which of the following most likely initiated this patient's dysregulated host "
    "response?",
    {
        "Beta-glucans within a fungal cell wall":
            "Beta-glucans, mannans and chitin are the fungal pathogen-associated molecular patterns, "
            "and Candida is the usual organism. His beta-D-glucan is negative.",
        "Lipopolysaccharide on a bacterial outer membrane":
            "Endotoxin is the most prominent trigger overall — but it belongs to GRAM-NEGATIVE "
            "bacteria such as Escherichia coli, Klebsiella and Pseudomonas. Cultures are sterile and "
            "procalcitonin, the bacterial marker, is normal.",
        "Lipoteichoic acid in a bacterial cell wall":
            "Lipoteichoic acid and peptidoglycan are the GRAM-POSITIVE patterns — Staphylococcus "
            "aureus, streptococci, enterococci. Again, the cultures are negative.",
        "Molecules released from damaged host cells": "",
        "Superantigen cross-linking of T-cell receptors":
            "Toxic shock syndrome toxins and streptococcal pyrogenic exotoxin bypass normal antigen "
            "presentation to activate T cells en masse. They are bacterial products, and nothing here "
            "suggests a staphylococcal or streptococcal source.",
    },
    "Molecules released from damaged host cells",
    "Viral sepsis — influenza A causing organ dysfunction with sterile cultures and a normal "
    "procalcitonin.\n\n"
    "Sepsis is triggered through two families of molecules:\n"
    "• PAMPs — pathogen-associated molecular patterns, carried by the ORGANISM. Gram-negative: "
    "lipopolysaccharide (the most prominent trigger overall). Gram-positive: lipoteichoic acid and "
    "peptidoglycan. Fungal: beta-glucans, mannans, chitin (all polysaccharides). Also "
    "superantigens, bacterial DNA and RNA.\n"
    "• DAMPs — damage-associated molecular patterns, released from the HOST'S OWN damaged tissue. "
    "This is how a virus triggers sepsis: virus-damaged cells spill intracellular contents, which "
    "set off a cascade of pro-inflammatory cytokines (interleukin-1, interleukin-6).\n\n"
    "Viruses are the exception in the table and therefore the likely question. The damage in sepsis "
    "comes from the host response rather than the pathogen directly, which is why no single organism "
    "defines sepsis, why cultures are negative in 30%–50% of cases, and why a negative culture never "
    "excludes it. Persistent inflammation → endothelial dysfunction and ischemic tissue injury → "
    "sequential organ failure → necrosis, necroptosis, pyroptosis and autophagy.\n\n"
    "Educational objective: Bacteria and fungi trigger sepsis through pathogen-associated molecular "
    "patterns (lipopolysaccharide, lipoteichoic acid, beta-glucans), whereas viruses trigger it "
    "through damage-associated molecular patterns released from injured host cells. Sterile cultures "
    "and a normal procalcitonin do not exclude sepsis.",
    "The flu virus wrecked his lung cells, and the broken pieces of his own cells are what set the "
    "alarm off. His immune system then attacked everything at once, including his own organs.",
    exim="fig_slide_sepsis_cascade",
    excap="The sepsis cascade — every arm converges on endothelial damage, tissue injury and organ "
          "dysfunction.",
)

# ── 31. HIV — enfuvirtide and the env gene (§19) ────────────────────────────────
q(
    "A 41-year-old man with HIV infection comes to the office for follow-up. He has taken several "
    "antiretroviral regimens over 15 years with poor adherence, and resistance testing shows "
    "mutations affecting reverse transcriptase, integrase and protease. A salvage regimen including "
    "subcutaneous enfuvirtide is started, and his HIV RNA falls from 180,000 to fewer than 50 "
    "copies/mL. Six months later the viral load rises to 24,000 copies/mL, and sequencing shows a "
    "new amino acid substitution in the viral fusion protein, which no longer binds the drug. The "
    "altered protein is a product of which of the following viral genes?",
    {
        "env": "",
        "gag":
            "The gag precursor is cleaved by VIRAL protease into p24 (the capsid antigen detected in "
            "fourth-generation testing), p17 (matrix) and the nucleocapsid proteins. None of them is "
            "on the virion surface fusing with the host membrane.",
        "nef":
            "An accessory gene whose product protects infected cells from killing by T lymphocytes. "
            "It is of interest for drug development but is not a structural gene.",
        "pol":
            "The pol gene encodes reverse transcriptase, integrase and protease — the targets of the "
            "three classes he has ALREADY failed. Enfuvirtide acts before any of them.",
        "tat":
            "A regulatory gene: the transactivator of transcription, which also inhibits T-cell "
            "proliferation. It has no surface product.",
        "vpu":
            "An accessory gene that enhances viral release and downregulates surface CD4 expression. "
            "Not a structural surface protein.",
    },
    "env",
    "Enfuvirtide is a FUSION inhibitor that binds gp41, and gp41 is a product of the env gene.\n\n"
    "Entry is a two-step event: gp120 binds CD4 plus a chemokine co-receptor (CCR5 or CXCR4) → a "
    "conformational change exposes gp41 → gp41's fusogenic domain fuses the viral envelope with the "
    "cell membrane. Both glycoproteins are cleaved from a single 160 kDa env precursor — and note "
    "that env is cleaved by HOST protease, which is exactly why protease inhibitors do not touch it, "
    "while the gag and pol precursors are cleaved by VIRAL protease, which is why they do.\n\n"
    "Map the drugs onto the genes:\n"
    "• env → fostemsavir (attachment, gp120), maraviroc (CCR5 antagonist), enfuvirtide (fusion, "
    "gp41); ibalizumab is a post-attachment inhibitor that blocks CD4 on the host side\n"
    "• pol → nucleoside and non-nucleoside reverse transcriptase inhibitors, integrase strand "
    "transfer inhibitors, protease inhibitors\n"
    "• gag → p24, the antigen that makes fourth-generation testing detect acute infection\n\n"
    "Resistance follows the same map: a single substitution in gp41 abolishes enfuvirtide binding, "
    "while a single point mutation in a conserved reverse transcriptase domain can knock out the "
    "entire non-nucleoside class (a low genetic barrier). Protease inhibitors have a high barrier, "
    "and the capsid inhibitor lenacapavir is the extreme case — one mutation confers more than "
    "80,000-fold resistance. The upstream cause is always the same: reverse transcriptase's high "
    "error rate generates the variant pool selection acts on.\n\n"
    "Educational objective: The env gene encodes gp120 and gp41, the surface proteins targeted by "
    "attachment and fusion inhibitors; pol encodes reverse transcriptase, integrase and protease; "
    "and gag encodes p24, the capsid antigen used in fourth-generation testing.",
    "The virus uses a grappling hook and a harpoon on its surface to get into cells. This drug jams "
    "the harpoon, so the virus changed the harpoon's shape — and the instructions for that part come "
    "from the env gene.",
    exim="fig_slide_hiv_cycle_drugs",
    excap="The HIV replication cycle with each drug class mapped to the step it blocks.",
)

# ── 32. Unmasking IRIS (§20) ────────────────────────────────────────────────────
q(
    "A 34-year-old woman with newly diagnosed HIV infection comes to the office due to 2 weeks of "
    "progressive right-sided weakness and difficulty finding words. At diagnosis 6 weeks ago her "
    "CD4 count was 38/mm3 and her HIV RNA was 420,000 copies/mL, and antiretroviral therapy was "
    "started the same week; she had no opportunistic infection at that time and takes no "
    "prophylaxis other than trimethoprim-sulfamethoxazole. Today her CD4 count is 165/mm3 and her "
    "HIV RNA is 780 copies/mL. Magnetic resonance imaging shows multifocal, nonenhancing white "
    "matter lesions with several new areas of faint peripheral enhancement and surrounding edema. "
    "A brain biopsy specimen is shown. Which of the following best explains this patient's current "
    "illness?",
    {
        "Direct neurotoxicity of antiretroviral drugs":
            "Some agents cause neuropsychiatric effects — vivid dreams and mood change with "
            "efavirenz, for example — but they do not produce focal deficits with demyelinating "
            "white matter lesions and viral inclusions on biopsy.",
        "Emergence of antiretroviral drug resistance":
            "Resistance announces itself as a RISING viral load. Hers has fallen from 420,000 to "
            "780 copies/mL, which is treatment success.",
        "Paradoxical immune reconstitution syndrome":
            "Paradoxical IRIS requires an opportunistic infection that was ALREADY diagnosed and "
            "being treated when antiretroviral therapy began, which then worsens. She had no known "
            "opportunistic infection.",
        "Progressive decline in immune function":
            "An ordinary opportunistic infection occurs as CD4 falls, late in the untreated course. "
            "Her CD4 has more than quadrupled.",
        "Unmasking immune reconstitution syndrome": "",
    },
    "Unmasking immune reconstitution syndrome",
    "Unmasking immune reconstitution inflammatory syndrome (IRIS), revealing progressive multifocal "
    "leukoencephalopathy caused by JC virus (a polyomavirus).\n\n"
    "IRIS is an exaggerated immune response to pathogens that occurs as antiretroviral therapy "
    "restores immune function. It takes two forms:\n"
    "• PARADOXICAL — the opportunistic infection is already known and being treated, and symptoms "
    "worsen after antiretroviral therapy starts\n"
    "• UNMASKING — no opportunistic infection was diagnosed; the recovering immune system generates "
    "inflammation that reveals a subclinical one. That is this patient\n\n"
    "The supporting pattern: advanced disease with a very low pre-treatment CD4 count and a high "
    "viral load, a robust virologic and immunologic response, and symptom onset within the first "
    "months of therapy (median 48 days, here 6 weeks). IRIS occurs in 10%–20% of patients, and the "
    "specific regimen chosen does not change the risk.\n\n"
    "The biopsy shows the JC virus lesion: demyelination with vacuolated white matter, enlarged "
    "oligodendroglial nuclei containing viral inclusions, and reactive astrocytes. Untreated PML has "
    "no specific antiviral — immune reconstitution IS the treatment, which is the paradox.\n\n"
    "The answer is not to delay antiretroviral therapy: delaying costs more than it saves. "
    "Anticipate IRIS, counsel the patient that worsening can occur, and keep it on the differential "
    "when a patient deteriorates while the numbers improve.\n\n"
    "Educational objective: Immune reconstitution inflammatory syndrome occurs within the first "
    "months of antiretroviral therapy in patients with a low pre-treatment CD4 count and a brisk "
    "virologic response; the unmasking form reveals a previously undiagnosed opportunistic "
    "infection. Improving CD4 count and falling viral load distinguish it from treatment failure.",
    "Her immune system was too weak to notice a slow brain virus. When the HIV medicines let it "
    "recover, it charged in and the swelling from that fight is what made her sick.",
    image="fig_hx_pml_histo",
    imcap="Brain biopsy, hematoxylin and eosin. The white matter is vacuolated and loosely textured, "
          "with scattered small lymphocytes and reactive astrocytes. Several glial cells have "
          "markedly enlarged, densely staining nuclei filled by a homogeneous inclusion (arrowhead).",
    exim="fig_slide_cd4_oi",
    excap="Opportunistic organisms by CD4 threshold, with the clinical clue for each.",
)

# ── 33. Cerebral malaria and hemozoin (§21) ─────────────────────────────────────
q(
    "A 29-year-old man is brought to the emergency department due to 4 days of fever with rigors "
    "and sweats occurring at no discernible interval, followed today by confusion and a generalized "
    "seizure. He returned 2 weeks ago from a 3-month stay in Nigeria and took no chemoprophylaxis. "
    "Temperature is 39.4 C (102.9 F). He is jaundiced. Hemoglobin is 7.6 g/dL (N=13.5–17.5 g/dL), "
    "platelet count is 42,000/mm3 (N=150,000–400,000/mm3), and creatinine is 2.8 mg/dL (N=0.6–1.2 "
    "mg/dL). He dies 12 hours after admission. A section of cerebral cortex is shown; the "
    "capillary contains erythrocytes packed with organisms and dark brown-black granular pigment. "
    "That pigment is produced by which of the following processes?",
    {
        "Aggregation of residual ribosomal RNA":
            "Aggregated ribosomes produce the coarse basophilic stippling of lead poisoning and "
            "thalassemia. That inclusion is blue and diffuse, not a brown-black pigment inside a "
            "parasite.",
        "Deposition of iron within mitochondria":
            "This is the ringed sideroblast of sideroblastic anemia, demonstrated with a Prussian "
            "blue stain of the marrow — iron the cell cannot insert into protoporphyrin.",
        "Oxidative denaturation of hemoglobin":
            "Oxidized, precipitated hemoglobin forms Heinz bodies in G6PD deficiency, visible only "
            "with a supravital stain and bitten out by splenic macrophages to leave bite cells.",
        "Polymerization of heme into hemozoin": "",
        "Precipitation of unpaired globin chains":
            "Unpartnered chains aggregate in thalassemia, killing precursors in the marrow and "
            "shortening red cell survival — a disorder of globin quantity, not a parasite product.",
        "Retention of nuclear DNA remnants":
            "Howell-Jolly bodies are retained nuclear fragments that a working spleen would remove; "
            "they signal asplenia or functional hyposplenism.",
    },
    "Polymerization of heme into hemozoin",
    "Severe falciparum malaria with cerebral involvement — sub-Saharan travel with no prophylaxis, "
    "IRREGULAR fever (falciparum's erythrocytic cycles are not synchronized, unlike the 48-hour "
    "cycle of vivax and ovale or the 72-hour cycle of malariae), hemolytic anemia, thrombocytopenia, "
    "acute kidney injury and encephalopathy.\n\n"
    "Where the pigment comes from — and why it is also the drug target:\n"
    "• The parasite digests hemoglobin inside the red cell and uses globin as an amino acid source\n"
    "• That liberates free HEME, which is toxic to the parasite itself\n"
    "• HEME POLYMERASE converts toxic heme into inert, crystalline HEMOZOIN — the brown-black "
    "pigment seen here\n"
    "• Chloroquine, quinine and mefloquine BLOCK that conversion, so heme accumulates and the "
    "parasite poisons itself with its own waste\n\n"
    "The neurologic disease is mechanical as well as inflammatory: parasitized erythrocytes adhere "
    "in and obstruct cerebral capillaries (exactly what this section shows), producing infarcts, "
    "capillary leak and neuronal injury. Patients can die within 24 hours.\n\n"
    "Diagnosis: a THICK smear is the screen (red cells pre-lysed, so it answers 'is it there?') and "
    "a THIN smear identifies the species and quantifies parasitemia; rapid antigen tests give an "
    "answer in about 10 minutes. Nigeria is chloroquine-resistant territory, so treatment is "
    "artemisinin-based combination therapy.\n\n"
    "Educational objective: Plasmodium digests hemoglobin and detoxifies the liberated heme by "
    "polymerizing it into hemozoin pigment; chloroquine and quinine block that step so heme "
    "accumulates and kills the parasite. Falciparum malaria causes irregular fever and can sequester "
    "in cerebral capillaries, producing cerebral malaria.",
    "The parasite eats the red stuff inside blood cells, and the leftovers are poisonous to it, so "
    "it packs them into harmless dark crystals. Some malaria drugs stop it doing that, so it is "
    "killed by its own garbage.",
    image="fig_hx_cerebral_malaria",
    imcap="Section of cerebral cortex, hematoxylin and eosin. A small capillary running through the "
          "vacuolated neuropil (arrowhead) is distended and packed with erythrocytes containing "
          "coarse dark brown-black granular pigment. Adjacent tissue shows small hemorrhages.",
    exim="fig_slide_chloroquine",
    excap="How chloroquine kills the parasite: it blocks the detoxification of heme into hemozoin.",
)

# ── 34. Bacillary angiomatosis versus Kaposi sarcoma (§21) ──────────────────────
q(
    "A 38-year-old man with AIDS comes to the office due to 6 weeks of enlarging red skin lesions. "
    "He stopped antiretroviral therapy 2 years ago. His CD4 count is 44/mm3. He has several cats "
    "at home, one of them a kitten. Examination shows numerous friable, cherry-red papules and "
    "nodules on the face and trunk, some with a collarette of scale, and a violaceous plaque on the "
    "forearm. His lesions are shown. Bartonella serology is negative. Biopsy of a papule shows a "
    "lobular proliferation of small capillaries lined by plump endothelial cells, with neutrophils "
    "and clumps of granular purple material that stain black on Warthin-Starry silver stain. In "
    "addition to restarting antiretroviral therapy, which of the following is the most appropriate "
    "treatment?",
    {
        "Doxycycline": "",
        "Itraconazole":
            "An antifungal for histoplasmosis and other endemic mycoses, which can also cause skin "
            "lesions in advanced HIV — but fungal elements, not silver-staining bacilli, would be "
            "seen on biopsy.",
        "Liposomal doxorubicin":
            "This treats Kaposi sarcoma, the critical look-alike: also violaceous lesions in AIDS, "
            "but driven by human herpesvirus 8, and showing spindle cells with slit-like vascular "
            "spaces and hemosiderin rather than bacilli.",
        "Trimethoprim-sulfamethoxazole":
            "The treatment and prophylaxis for Pneumocystis jirovecii pneumonia and toxoplasmosis, "
            "which he should already be receiving at this CD4 count. It does not treat this "
            "infection.",
        "Valganciclovir":
            "Used for cytomegalovirus disease — retinitis, esophagitis, colitis — at CD4 counts "
            "below 50. Cytomegalovirus does not produce vascular skin nodules.",
    },
    "Doxycycline",
    "Bacillary angiomatosis caused by Bartonella henselae — the SAME organism as cat scratch "
    "disease, producing a completely different disease because the host is different.\n\n"
    "One fork organizes the topic: immunoCOMPETENT host (typically a child under 10) → cat scratch "
    "disease, a lymphocutaneous illness with an inoculation papule and tender regional "
    "lymphadenopathy, self-limiting over 5–6 weeks, treated with azithromycin. ImmunoCOMPROMISED "
    "host (AIDS, chemotherapy, transplant) → bacillary angiomatosis, a proliferation of small "
    "vessels in skin and viscera, progressive and fatal if untreated, treated with erythromycin "
    "and/or doxycycline plus restoration of immune function.\n\n"
    "Two exam points are built into this vignette:\n"
    "• The negative serology means nothing. Serology detects the HOST's antibody response, and this "
    "host cannot mount one — the test underperforms in exactly the population that gets the "
    "disease. Diagnose by lesion biopsy with histopathology and PCR.\n"
    "• The look-alike is Kaposi sarcoma. Both occur in AIDS and look similar, but one is a curable "
    "bacterial infection and the other an HHV-8-driven vascular malignancy. You cannot tell them "
    "apart by looking, which is why the biopsy is mandatory.\n\n"
    "The Warthin-Starry stain identifies argyrophilic ('silver-loving') organisms: Bartonella, "
    "spirochetes, Legionella and Helicobacter pylori. The clinical context picks the winner. Note "
    "also that the infectious material in a cat scratch is FLEA FECES on the fur and claws — the "
    "claw is the needle, not the source.\n\n"
    "Educational objective: Bartonella henselae causes cat scratch disease in immunocompetent hosts "
    "and bacillary angiomatosis in immunocompromised ones; the latter is diagnosed by biopsy with a "
    "Warthin-Starry stain (serology is unreliable) and treated with erythromycin or doxycycline plus "
    "immune restoration. Kaposi sarcoma is the clinical mimic.",
    "A germ from a cat's fleas is making tiny blood vessels grow into red bumps on his skin because "
    "his immune system cannot stop it. The right antibiotic clears it, but only if his immune system "
    "is also rebuilt.",
    image="fig_bacillary_angiomatosis",
    imcap="Face of a patient with advanced HIV infection. Numerous smooth, dome-shaped, deep red "
          "papules and nodules of varying size are scattered over the cheek, eyelid and nose; "
          "several are eroded and crusted.",
    exim="fig_hx_kaposi_histo",
    excap="The look-alike under the microscope: Kaposi sarcoma, with fascicles of spindle cells, "
          "slit-like vascular spaces containing red cells, and hemosiderin.",
)

# ── 35. Bubonic plague (§21) ────────────────────────────────────────────────────
q(
    "A 32-year-old man comes to the emergency department due to 1 day of fever, chills and profound "
    "weakness, with a painful lump in the right groin. He has been camping in rural New Mexico and "
    "handled several dead prairie dogs near his campsite 4 days ago. Temperature is 39.7 C (103.5 "
    "F), blood pressure is 96/56 mm Hg, and pulse is 124/min. Examination shows an exquisitely "
    "tender, boggy 5 cm mass in the right inguinal region with overlying erythema, and a small "
    "crusted papule on the right calf. There is no pharyngitis and no genital ulcer. Aspiration of "
    "the mass is performed. Which of the following is most likely to be seen on stained smears of "
    "the aspirate?",
    {
        "Acid-fast beaded bacilli":
            "Mycobacterial lymphadenitis (scrofula) produces a chronic, often nontender node over "
            "weeks to months, not a 1-day febrile illness with hypotension.",
        "Gram-negative rods with bipolar staining": "",
        "Gram-positive lancet-shaped diplococci":
            "Streptococcus pneumoniae causes fulminant sepsis in asplenic patients and pneumonia in "
            "the community, but it does not produce a bubo after rodent exposure.",
        "Intraerythrocytic ring forms":
            "Rings inside red cells are Babesia or Plasmodium — and they are sought on a Giemsa "
            "smear of BLOOD, not a node aspirate. Babesia would also mean a New England tick, not a "
            "western rodent.",
        "Pleomorphic coccobacilli on silver stain":
            "Bartonella henselae is argyrophilic and causes tender regional lymphadenopathy after a "
            "cat scratch — but the illness is indolent and self-limiting rather than an abrupt "
            "septic presentation with rodent exposure.",
    },
    "Gram-negative rods with bipolar staining",
    "Bubonic plague — Yersinia pestis. Every element of the stem is a deliberate pointer: the "
    "western United States (endemic in at least 17 states, chiefly Pacific Coast and western states "
    "— New Mexico, Colorado, California, Texas, Arizona, Oregon, Nevada), a named epizootic host "
    "(squirrels, prairie dogs, chipmunks), abrupt high fever with weakness, and a BUBO in the node "
    "draining a flea bite on the leg.\n\n"
    "The organism is a gram-negative rod with BIPOLAR 'safety pin' staining on Gram or Giemsa — dark "
    "at both ends, pale in the middle. A rapid antigen test is 100% sensitive and 100% specific; "
    "culture on blood agar gives sensitivities, and PCR confirms. Treat with gentamicin or a "
    "fluoroquinolone. Untreated bubonic plague kills about half of those infected; treated mortality "
    "is 1%–15%.\n\n"
    "Why a flea transmits it at all: Y. pestis multiplies in the flea's proventriculus until a hard "
    "mass BLOCKS it, so the flea can bite but cannot swallow. Starving, it bites frantically and "
    "indiscriminately, regurgitating bacteria into each wound — which is how humans, a DEAD-END host "
    "that offers the organism nothing, are bitten at all.\n\n"
    "The complication to watch is progression to secondary plague pneumonia, after which the patient "
    "transmits by aerosol and can seed primary plague pneumonia in contacts — 100% fatal untreated. "
    "And a plague isolate with marked antibiotic resistance should raise the possibility of "
    "deliberate engineering, since naturally occurring plague is almost uniformly susceptible.\n\n"
    "Educational objective: Yersinia pestis causes bubonic plague after a rodent-flea exposure in "
    "the western United States and appears as a bipolar-staining ('safety pin') gram-negative rod on "
    "node aspirate. Treat with gentamicin or a fluoroquinolone, and watch for secondary plague "
    "pneumonia, which spreads by aerosol.",
    "A flea that fed on infected prairie dogs bit him, and the germs travelled to the nearest "
    "lymph node and made it swell into a painful lump. Under the microscope those germs look like "
    "tiny safety pins.",
    image="fig_bubo",
    imcap="Photograph of the groin. A large, smooth, dome-shaped swelling distorts the inguinal "
          "region beneath intact skin.",
    exim="fig_flea_proventriculus",
    excap="The blocked flea proventriculus — a starving flea bites repeatedly and regurgitates "
          "bacteria into each wound.",
)

# ── 36. Hantavirus hemorrhagic fever with renal syndrome (§22) ──────────────────
q(
    "A 38-year-old man comes to the emergency department due to 5 days of fever, severe headache "
    "and vomiting, followed by decreasing urine output. Five weeks ago he returned from rural South "
    "Korea, where he spent a month renovating a long-disused grain barn heavily soiled with rodent "
    "droppings. He recalls no insect or tick bites and no animal bites. Temperature is 38.9 C "
    "(102.0 F) and blood pressure is 88/52 mm Hg. There are petechiae over the trunk and "
    "conjunctival hemorrhages. Platelet count is 38,000/mm3 (N=150,000–400,000/mm3), creatinine is "
    "5.1 mg/dL (N=0.6–1.2 mg/dL), and urinalysis shows marked proteinuria. Renal biopsy shows "
    "interstitial hemorrhage with a dense mononuclear infiltrate and tubular injury, most severe in "
    "the medulla. Which of the following was the most likely route of transmission?",
    {
        "Bite of a female Anopheles mosquito":
            "This transmits malaria, whose reservoir is humans themselves, in the tropics and "
            "subtropics — with cyclic fever and ring forms inside red cells rather than renal "
            "failure with hemorrhage.",
        "Bite of a Hyalomma tick":
            "This is Crimean-Congo hemorrhagic fever, acquired from livestock and birds that stay "
            "well, in Africa, the Middle East, Asia and southeastern Europe — not the Far East, and "
            "not with kidney failure as the dominant organ injury.",
        "Bite of an Ixodes scapularis nymph":
            "This vector transmits babesiosis, Lyme disease and anaplasmosis in the northeastern "
            "United States. Babesia causes hemolysis and thrombocytopenia, not an interstitial "
            "nephritis.",
        "Bite of an infected rat flea":
            "The rat flea transmits Yersinia pestis, which produces a bubo and acral gangrene, and "
            "is a disease of the western United States rather than the Far East.",
        "Contact with infected fruit bat fluids":
            "This is how filoviruses (Ebola and Marburg) are acquired, in Central and West Africa, "
            "with generalized multi-organ failure rather than a kidney-dominant illness.",
        "Inhalation of aerosolized rodent excreta": "",
    },
    "Inhalation of aerosolized rodent excreta",
    "Hantavirus hemorrhagic fever with renal syndrome (HFRS), most likely Hantaan or Seoul virus "
    "given Korea.\n\n"
    "Transmission: the virus is shed in rodent urine, feces and saliva and is acquired by AEROSOL, "
    "classically while generating dust in a rodent-infested building. There is NO vector — hantavirus "
    "and Lassa are the two agents in this block with no arthropod at all, which is why the stem "
    "pointedly denies bites.\n\n"
    "The incubation period is the other clue: 3 to 9 WEEKS, far longer than dengue's 4–7 days. An "
    "exposure more than a month ago is still within the window and must not be dismissed as too "
    "remote.\n\n"
    "Why the kidney fails out of proportion: this is an IMMUNOPATHOLOGIC lesion. Infected dendritic "
    "cells and macrophages release a cytokine storm; cytotoxic T cells are recruited; infected "
    "endothelial cells upregulate HLA and adhesion molecules, marking themselves for "
    "antibody-dependent cytotoxicity and complement, and secrete vascular endothelial growth factor, "
    "which increases permeability; and the kallikrein-kinin system raises bradykinin. The result is "
    "an acute tubulointerstitial nephritis with interstitial hemorrhage — and acute kidney injury is "
    "the usual cause of death. Every other viral hemorrhagic fever here fails as a set of organs.\n\n"
    "Old World hantaviruses → kidneys (HFRS). New World hantaviruses → heart and lungs (the "
    "cardiopulmonary syndrome). There is no antiviral and no vaccine available in the United States; "
    "care is supportive with volume and electrolyte management and renal replacement therapy.\n\n"
    "Educational objective: Old World hantaviruses are acquired by inhaling aerosolized rodent "
    "urine, feces or saliva with no arthropod vector, have a 3–9 week incubation, and cause "
    "hemorrhagic fever with renal syndrome in which immunopathologic acute kidney injury is the "
    "usual cause of death.",
    "He breathed in dried mouse droppings while cleaning an old barn, and the virus in them attacked "
    "the lining of his blood vessels. His kidneys took the worst of it, which is what makes this "
    "particular virus stand out.",
    exim="fig_slide_hanta_kidney",
    excap="The hantavirus renal lesion — cytokines, cytotoxic T cells and complement acting on an "
          "infected endothelium.",
)

# ── 37. Cold agglutinins — the impossible MCHC (§25) ────────────────────────────
q(
    "A 72-year-old woman comes to the office due to 3 weeks of fatigue and a dusky blue "
    "discoloration of her fingertips that appears when she goes outdoors and resolves indoors. She "
    "had an atypical pneumonia treated with azithromycin 6 weeks ago. She takes no other "
    "medications. The sample is drawn in the office and sent to the laboratory.\n\n"
    "Laboratory studies show:\n"
    "Erythrocyte count 2.1 million/mm3 (N=3.5–5.5 million/mm3)\n"
    "Hemoglobin 11.6 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 26% (N=36%–46%)\n"
    "Mean corpuscular volume 124 µm3 (N=80–100 µm3)\n"
    "Mean corpuscular hemoglobin concentration 44.6% (N=31%–36%)\n"
    "Platelet count 244,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "The analyzer flags the specimen. A smear made from the same tube is shown. Which of the "
    "following is the most appropriate next step?",
    {
        "Begin vitamin B12 replacement":
            "The macrocytosis here is an artefact of clumped cells being sized as one large cell. "
            "True megaloblastic anemia gives hypersegmented neutrophils and a raised methylmalonic "
            "acid, and would not produce an impossible MCHC.",
        "Correct the hemoglobin with a plasma blank":
            "Blank correction is the fix when LIPEMIA, marked leukocytosis or hyperbilirubinemia add "
            "absorbance and falsely raise the measured hemoglobin. Here the hemoglobin is measured on "
            "lysed cells and is accurate — the hematocrit is the corrupted value.",
        "Perform a bone marrow biopsy":
            "A marrow biopsy investigates unexplained pancytopenia or suspected primary marrow "
            "disease. Acting on an artefactual result with an invasive test is the specific harm "
            "this flag exists to prevent.",
        "Redraw the specimen in a citrate tube":
            "Citrate is the workaround for EDTA-dependent PLATELET clumping, which falsely lowers "
            "the platelet count. Her platelet count is normal and the abnormality is in the red cell "
            "indices.",
        "Transfuse one unit of red blood cells":
            "Her true hemoglobin is 11.6 g/dL, which is measured correctly and nowhere near a "
            "transfusion threshold.",
        "Warm the specimen to 37 C and re-run": "",
    },
    "Warm the specimen to 37 C and re-run",
    "Cold agglutinins causing red cell agglutination in the tube — here following Mycoplasma "
    "pneumoniae infection, with acrocyanosis on cold exposure as the clinical counterpart.\n\n"
    "The giveaway is an MCHC of 44.6%. MCHC is a CONCENTRATION, so it is bounded by physics: a red "
    "cell can only hold so much hemoglobin per unit volume, and the normal range tops out near "
    "36%–37%. A value well above that is almost never biological.\n\n"
    "Trace the error through the arithmetic, remembering that only three values are MEASURED (red "
    "cell count and MCV by impedance, hemoglobin photometrically) and the rest are calculated:\n"
    "• Clumped cells cross the aperture together → counted as ONE very large cell → red cell count "
    "falls, MCV rises\n"
    "• Hematocrit = (RBC × MCV)/10 → the count fell further than the volume rose → hematocrit is "
    "falsely LOW (note it is also only 2.2 times the hemoglobin, breaking the rule of three)\n"
    "• MCHC = (Hgb/Hct) × 100 → an impossibly HIGH value\n"
    "• The hemoglobin itself is measured on lysed cells and remains accurate\n\n"
    "The fix is to warm the sample to 37 C and re-run, which disperses the agglutinates. Clinically, "
    "follow with a cold agglutinin titre and a direct antiglobulin test, which is positive for "
    "complement C3 in cold agglutinin disease.\n\n"
    "The one setting where a genuinely high MCHC is a disease and not an artefact is hereditary "
    "spherocytosis, where the cells really are hyperdense.\n\n"
    "Educational objective: An MCHC above about 37% is nearly always a specimen artefact — either "
    "falsely raised hemoglobin (lipemia, marked leukocytosis, hyperbilirubinemia) or a falsely low "
    "calculated hematocrit from cold agglutinin-induced red cell clumping, which is resolved by "
    "warming the sample to 37 C and re-running it.",
    "Her blood cells stuck together into clumps in the cold tube, and the machine counted each clump "
    "as one giant cell. Warming the tube unsticks them so the numbers come out right.",
    image="fig_agglutination",
    imcap="Peripheral blood smear. Erythrocytes are gathered into irregular three-dimensional clumps "
          "with clear spaces between them, rather than lying separately; a neutrophil is present at "
          "left.",
    exim="fig_slide_coulter",
    excap="The Coulter principle — each cell crossing the aperture makes one pulse, and pulse height "
          "is read as that cell's volume.",
)

# ── 38. The absolute neutrophil count and absent inflammation (§26) ─────────────
q(
    "A 47-year-old woman is hospitalized on day 12 after induction chemotherapy for acute myeloid "
    "leukemia due to fever. She reports 2 days of deep perianal pain. Temperature is 38.9 C (102.0 "
    "F). Examination shows tenderness lateral to the anus with minimal erythema and no fluctuance, "
    "induration or drainage. Chest examination is normal and chest radiography shows no infiltrate, "
    "although she reports a cough.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 8.4 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 25% (N=36%–46%)\n"
    "Leukocyte count 600/mm3 (N=4,500–11,000/mm3)\n"
    "Segmented neutrophils 12% (N=54%–62%)\n"
    "Platelet count 24,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "Which of the following best explains the paucity of local findings in this patient?",
    {
        "Absent antibody production by B lymphocytes":
            "An antibody deficiency such as Bruton agammaglobulinemia causes recurrent pyogenic "
            "infections — but those patients still form pus, because their neutrophils are present "
            "and functional.",
        "Defective oxidative burst within phagocytes":
            "In chronic granulomatous disease the neutrophil COUNT is normal and the cells are "
            "recruited normally; they simply cannot kill catalase-positive organisms, so patients "
            "form abscesses and granulomas — the opposite of no inflammation.",
        "Loss of T-cell help for macrophage activation in tissue":
            "This is the defect in advanced HIV infection and DiGeorge syndrome, producing viral, "
            "fungal and opportunistic infections. It does not abolish the neutrophilic exudate.",
        "Margination of neutrophils along vessel walls":
            "Excessive peripheral pooling makes the measured count understate the total neutrophil "
            "pool — but those cells are still available to enter tissue, and this patient's marrow "
            "has been ablated by chemotherapy.",
        "Too few neutrophils to form an inflammatory exudate": "",
    },
    "Too few neutrophils to form an inflammatory exudate",
    "Febrile neutropenia after induction chemotherapy, with a perianal infection.\n\n"
    "Compute the number, because a percentage always misleads: ANC = white cell count × % "
    "neutrophils = 600 × 0.12 = 72/µL.\n\n"
    "The three thresholds:\n"
    "• < 1,000/µL — sharply increased risk of infection\n"
    "• < 500/µL — control of endogenous skin and gut flora is impaired; this is absolute neutropenia\n"
    "• < 200/µL — NO inflammatory process can be mounted in response to immune challenge\n\n"
    "She is at 72/µL, and the classic signs of infection ARE the inflammatory response. Pus is dead "
    "neutrophils. Consolidation on a chest film is largely neutrophilic exudate. Erythema, swelling, "
    "induration and fluctuance all depend on neutrophil recruitment. With too few cells to produce "
    "any of it, a serious infection — here a perianal infection that could be a deep abscess — can "
    "be present with almost no localizing signs, and the chest film can stay clear in a patient with "
    "pneumonia.\n\n"
    "Hence fever alone is the emergency: obtain cultures and start empiric broad-spectrum "
    "intravenous antibiotics immediately rather than waiting for a source to declare itself, because "
    "the progression is fever and chills → sepsis → multi-organ failure. Note also that "
    "bacteriostatic agents rely on a functioning immune system to clear the organisms already "
    "present, which is why bactericidal therapy is preferred here.\n\n"
    "Educational objective: The absolute neutrophil count is the white cell count times the "
    "neutrophil percentage; below 500/µL endogenous flora become pathogens, and below 200/µL no "
    "inflammatory response can be generated, so infections present with fever and few localizing "
    "signs. Febrile neutropenia requires immediate empiric broad-spectrum antibiotics.",
    "The redness, swelling and pus you normally see with an infection are made OF white blood cells, "
    "and chemotherapy has wiped hers out. So a dangerous infection can be there with almost nothing "
    "to see — a fever is the only warning.",
    exim="fig_slide_five_wbc",
    excap="The five normal circulating leukocytes — the neutrophil is the cell that builds the "
          "inflammatory exudate.",
)

# ── 39. Leukemoid reaction versus malignancy (§27) ──────────────────────────────
q(
    "A 70-year-old man is admitted to the hospital due to 3 days of fever and left lower quadrant "
    "pain. Computed tomography shows perforated sigmoid diverticulitis with a 7 cm pelvic abscess, "
    "which is drained percutaneously. He has no lymphadenopathy, splenomegaly, night sweats or "
    "weight loss.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 13.1 g/dL (N=13.5–17.5 g/dL)\n"
    "Hematocrit 39% (N=41%–53%)\n"
    "Leukocyte count 58,000/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 388,000/mm3 (N=150,000–400,000/mm3)\n"
    "Basophils 0% (N=0%–0.75%)\n\n"
    "The peripheral smear shows abundant neutrophils with coarse dark cytoplasmic granules, pale "
    "blue cytoplasmic inclusions and vacuoles, along with occasional myelocytes and metamyelocytes; "
    "blasts account for less than 1% of cells. Which of the following is most likely to occur in "
    "this patient?",
    {
        "Appearance of myeloblasts containing Auer rods":
            "Needle-shaped granule inclusions mark a malignant myeloid cell and would indicate acute "
            "myeloid leukemia. His blasts are under 1% and his other cell lines are intact.",
        "Detection of a BCR-ABL1 fusion transcript":
            "This defines chronic myeloid leukemia, which also produces a very high white count with "
            "circulating immature cells — but characteristically with ABSOLUTE BASOPHILIA, which he "
            "does not have, and it does not resolve when an abscess is drained.",
        "Development of a leukoerythroblastic smear":
            "Immature white cells plus nucleated red cells plus tear-drop cells together indicate "
            "disturbed marrow architecture — myelofibrosis or marrow infiltration by tumour. His red "
            "cell morphology is unremarkable.",
        "Identification of a monoclonal population by flow cytometry":
            "Flow cytometry demonstrates clonality directly and is the test to send when you are "
            "unsure. Here the response is polyclonal and reactive: heterogeneous cells with toxic "
            "changes, and normal other lineages.",
        "Persistent absolute basophilia on repeat counts":
            "Unexplained persistent basophilia is one of the few findings that points directly at a "
            "myeloproliferative neoplasm. His basophil count is zero.",
        "Return of the leukocyte count to normal after drainage": "",
    },
    "Return of the leukocyte count to normal after drainage",
    "A leukemoid reaction — severe leukocytosis with immature cells in the blood that mimics a "
    "neoplastic proliferation. The discrimination decides whether this patient gets antibiotics or a "
    "bone marrow biopsy.\n\n"
    "Everything here favours REACTIVE:\n"
    "• Toxic granulation, Döhle bodies (the pale blue inclusions) and vacuolization — the three "
    "changes of a neutrophil working hard, never of a malignant clone\n"
    "• The blast pyramid is the right way up: a few blasts, more myelocytes and metamyelocytes, and "
    "mostly mature cells. Inverting that pyramid is the concerning pattern\n"
    "• Other cell lines are preserved — a marrow crowded out by a clone cannot keep making red cells "
    "and platelets\n"
    "• No basophilia, no B symptoms, and a named precipitant that has been treated\n\n"
    "The six morphologic criteria, reactive versus malignant: nuclear-to-cytoplasmic ratio "
    "(decreased vs increased), cytoplasm (abundant, moulding around neighbouring red cells vs "
    "scant), population uniformity (heterogeneous and polyclonal vs monoclonal), chromatin (coarse "
    "and clumped vs open and powdery), nucleoli (occasional and small vs prominent) and other cell "
    "lines (normal vs decreased). A nucleolus alone is not abnormal — any hard-working cell has one; "
    "many or very large nucleoli are the problem, and Auer rods are unambiguous.\n\n"
    "Duration settles most cases: reactive morphology resolves as the source is controlled, whereas "
    "a leukemia persists after the patient recovers. When in doubt, have a low threshold for flow "
    "cytometry, which demonstrates clonality directly.\n\n"
    "Educational objective: A leukemoid reaction is a severe reactive leukocytosis with toxic "
    "granulation, Döhle bodies and a left shift that preserves the normal maturation pyramid and "
    "other cell lines, and it resolves once the underlying stimulus is treated. Basophilia, an "
    "excess of blasts, Auer rods, cytopenias or a monoclonal population point to malignancy.",
    "His body is pumping out huge numbers of infection-fighting cells because of the abscess, which "
    "can look like leukemia on a count. Once the abscess is drained, the number comes back down — "
    "leukemia would not.",
    exim="fig_toxic_granulation",
    excap="Toxic granulation — coarse dark granules in a neutrophil responding hard to a stimulus, "
          "not a malignant change.",
)

# ── 40. Chronic granulomatous disease — the catalase rule (§28) ─────────────────
q(
    "A 4-year-old boy is brought to the office due to 3 weeks of fever and cough. He has had two "
    "episodes of cervical lymphadenitis requiring surgical drainage, both growing Staphylococcus "
    "aureus, and a liver abscess at age 2 that grew Serratia marcescens. He is at the 10th "
    "percentile for weight. Chest computed tomography shows a cavitating right upper lobe "
    "consolidation, and lung biopsy grows Aspergillus fumigatus; histologic sections show "
    "granulomas with multinucleated giant cells. Leukocyte count is 9,400/mm3 with 58% segmented "
    "neutrophils, and serum IgG, IgA and IgM concentrations are normal. The organisms that have "
    "infected this patient share which of the following properties?",
    {
        "Production of a polysaccharide capsule":
            "Encapsulated organisms — Streptococcus pneumoniae, Neisseria meningitidis, Haemophilus "
            "influenzae type b — overwhelm patients without a functioning SPLEEN or without "
            "antibody. Serratia and Aspergillus are not in that group.",
        "Production of catalase": "",
        "Production of coagulase":
            "Coagulase distinguishes Staphylococcus aureus from other staphylococci. It says nothing "
            "about Serratia or Aspergillus, so it cannot be the shared property.",
        "Production of IgA protease":
            "IgA protease helps organisms colonize mucosal surfaces and is made by pneumococcus, "
            "meningococcus and Haemophilus — a different group entirely.",
        "Survival within resting macrophages":
            "Intracellular survival characterizes mycobacteria, Listeria and Salmonella, and those "
            "infections dominate when interferon-gamma signalling or T cells fail — not this pattern "
            "of abscesses and fungal pneumonia.",
    },
    "Production of catalase",
    "Chronic granulomatous disease — a QUALITATIVE phagocyte defect. Note the normal neutrophil "
    "count and normal immunoglobulins: the cells are present in normal numbers and simply do not "
    "work.\n\n"
    "The respiratory burst, and where it breaks:\n"
    "• O2 → superoxide, by NADPH OXIDASE — the step that fails (mutations in cytochrome b558; 70% "
    "X-linked recessive, and 86% of patients are male)\n"
    "• Superoxide → hydrogen peroxide, by superoxide dismutase\n"
    "• Hydrogen peroxide → hypochlorous acid, by myeloperoxidase — the neutrophil is making bleach "
    "inside a vacuole\n\n"
    "The catalase logic: phagocytosis is intact, so organisms are ingested normally. A phagocyte "
    "with no NADPH oxidase makes no hydrogen peroxide of its own — but many bacteria generate "
    "hydrogen peroxide as a metabolic by-product, and the defective phagocyte simply borrows theirs. "
    "CATALASE-POSITIVE organisms destroy their own hydrogen peroxide, leaving nothing to borrow, so "
    "they survive inside the cell. The offenders to name: Staphylococcus aureus, Aspergillus, "
    "Serratia, Nocardia and Burkholderia. Catalase-negative organisms are still killed.\n\n"
    "The standoff that follows is the granuloma: a necrotic centre with living organisms, walled off "
    "by macrophages and multinucleated giant cells, with T and B cells outside holding the line.\n\n"
    "Diagnosis: the nitroblue tetrazolium test (normal neutrophils reduce a yellow dye to a "
    "blue-black precipitate; these cannot) or the modern neutrophil oxidative index by flow "
    "cytometry. Management: prophylactic antibiotics and antifungals, recombinant interferon gamma "
    "(reduces infection rate by up to 70%), and corticosteroids when granulomas obstruct a viscus.\n\n"
    "Educational objective: Chronic granulomatous disease is a defect of NADPH oxidase that leaves "
    "phagocytes unable to generate reactive oxygen species, so catalase-positive organisms — "
    "Staphylococcus aureus, Serratia, Nocardia, Burkholderia and Aspergillus — survive ingestion and "
    "produce recurrent abscesses and granulomas. The neutrophil count is normal.",
    "His infection-fighting cells can swallow germs but cannot make the bleach that kills them. Germs "
    "that clean up their own bleach survive inside, and the body walls them off into little lumps.",
    exim="fig_slide_granuloma",
    excap="The granuloma — a necrotic centre with living organisms, walled off by macrophages and "
          "lymphocytes. A siege, not a cure.",
)
