S48 = "s43-lymphedema"        # LO 34 lists §56 first, so lymphedema items need the pair form
S56 = "s53-traumatic-edema"

LO_TAGS = {
 1:  [64],            # combine on different mechanism AND different toxicity
 2:  [64],            # log kill, the 1-gram threshold, adjuvant rationale
 3:  [64],            # MDR1 / P-glycoprotein cross-resistance
 4:  [64],            # G0 and cell cycle specificity
 5:  [64],            # mesna and acrolein; the three rescue agents
 6:  [64],            # intrathecal vincristine is uniformly fatal
 7:  [64],            # oxaliplatin cold-induced dysesthesia
 8:  [11],            # size decides format — no antibody hits an intracellular target
 9:  [16, 11],        # trastuzumab and HER2 on cardiomyocytes
 10: [16, 11],        # antibody-drug conjugate payloads
 11: [16],            # EGFR rash is on-target, not allergy
 12: [16],            # cytokine release syndrome → tocilizumab
 13: [16],            # ICANS → dexamethasone, not tocilizumab
 14: [16],            # checkpoint colitis → corticosteroids
 15: [16, (31, "s12-immuno")],   # daratumumab and the blood bank
 16: [15],            # aromatase inhibitor in a premenopausal woman
 17: [15],            # SERM vs aromatase inhibitor, read off bone
 18: [15],            # GnRH agonist tumour flare
 19: [(34, S48), 60], # Stemmer sign, iatrogenic secondary lymphedema
 20: [(34, S48)],     # filariasis
 21: [(34, S56)],     # compartment syndrome
 22: [60],            # Virchow's node and the thoracic duct
 23: [60],            # sentinel node — staging without the lymphedema
 24: [10],            # DVT after arthroplasty → duplex ultrasound first
 25: [10],            # CTEPH → V/Q scan, not CT angiography
}
