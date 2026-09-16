# Jeevs Edition batch 18 = COAGULATION II top-up + LYMPH NODE PATHOLOGY
#   §32–§34 gaps  -> LO 33, 43, 44, 45, 46, 52
#   §35 s31b-node-architecture -> LO 63 (normal architecture), LO 66 (reactive vs malignant)
S29, S30, S31, S31B = "s29-tma", "s30-thrombophilia", "s31-vte-management", "s31b-node-architecture"

LO_TAGS = {
 1:  [43, 52],                   # §34 Virchow's triad
 2:  [(46, S31), 43],            # §34 pregnancy and the postpartum peak
 3:  [46, 43],                   # §33 oral contraceptive plus smoking — reversible
 4:  [45, (52, S31)],            # §33 essential thrombocythemia vs reactive thrombocytosis
 5:  [45],                       # §33 hyperhomocysteinemia inhibits protein C
 6:  [44, 33],                   # §32 pneumococcal HUS — neuraminidase and T antigen
 7:  [44, 33],                   # §32 drug/transplant-associated TMA
 8:  [43],                       # §34 the 4T score says do not test
 9:  [63, 66],                   # §35 the floor plan — paracortex
 10: [66, 63],                   # §35 BCL2 negative in a reactive germinal center
 11: [66],                       # §35 mononucleosis versus Hodgkin lymphoma
 12: [66],                       # §35 Kikuchi-Fujimoto disease
 13: [66],                       # §35 Rosai-Dorfman and emperipolesis
 14: [66, 63],                   # §35 hyaline vascular Castleman disease
 15: [63],                       # §35 formalin is a one-way door
 16: [66],                       # §35 hemophagocytosis is one criterion of eight
}
