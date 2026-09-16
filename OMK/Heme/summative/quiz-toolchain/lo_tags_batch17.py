# Jeevs Edition batch 17 = COAGULATION II · CLOTTING  (Objective Review §32–§34)
# Native objectives:
#   §32 s29-tma            -> LO 33 (compare/contrast the TMAs), LO 44 (causes of TMA)
#   §33 s30-thrombophilia  -> LO 45 (common thrombophilias), LO 46, LO 48
#   §34 s31-vte-management -> LO 43 (anticoagulation strategies), LO 52 (complications), LO 46
S29, S30, S31 = "s29-tma", "s30-thrombophilia", "s31-vte-management"

LO_TAGS = {
 1:  [33, 44],                   # §32 TTP — plasma exchange, not platelets
 2:  [33],                       # §32 ADAMTS13 and ultra-large multimers
 3:  [44, 33],                   # §32 Shiga toxin HUS
 4:  [44, 33],                   # §32 atypical HUS and eculizumab
 5:  [44],                       # §32 aHUS genetics before transplant
 6:  [33],                       # §32 the TMA/DIC coagulation panel split
 7:  [45, 48],                   # §33 factor V Leiden
 8:  [45],                       # §33 prothrombin G20210A
 9:  [45, (48, S30)],            # §33 antithrombin deficiency and heparin resistance
 10: [45, (52, S31)],            # §33 neonatal purpura fulminans
 11: [46, 45],                   # §33 the lupus anticoagulant paradox
 12: [46],                       # §33 antibody is not syndrome
 13: [46],                       # §33 the false-positive non-treponemal test
 14: [43, 52],                   # §34 the 4T score and immediate actions
 15: [43],                       # §34 cross-reactivity — no LMWH after HIT
 16: [52, 43],                   # §34 rapid-onset HIT
 17: [43],                       # §34 anti-Xa monitoring for LMWH
 18: [43, (46, S31)],            # §34 duration set by circumstances; acute-period testing
 19: [(46, S31), 43],            # §34 who to test
 20: [52, 43],                   # §34 warfarin-induced skin necrosis
}
