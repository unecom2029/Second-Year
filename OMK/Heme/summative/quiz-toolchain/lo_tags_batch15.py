# Jeevs Edition batch 15 = COAGULATION I · BLEEDING  (Objective Review §29–§31)
# Native objectives:
#   §29 s26-cascade            -> LO 50 (mechanisms of common bleeding disorders), LO 32
#   §30 s27-bleeding-inherited -> LO 32 (compare/contrast bleeding disorders), LO 36 (platelet
#                                 disorders), LO 68 (hereditary historical features), LO 79
#   §31 s28-bleeding-acquired  -> LO 32, LO 36 (both anchored to the acquired section)
S26, S27, S28 = "s26-cascade", "s27-bleeding-inherited", "s28-bleeding-acquired"

LO_TAGS = {
 1:  [50],                       # §29 factor XII — long aPTT, no bleeding
 2:  [50],                       # §29 the short-draw citrate tube
 3:  [50],                       # §29 the incubated mixing study
 4:  [50, (32, S27)],            # §29 normal screen does not exclude VWD
 5:  [50],                       # §29 factor XIII and delayed bleeding
 6:  [50, (32, S28)],            # §29 isolated long PT — vitamin K, factor VII
 7:  [50],                       # §29 what a D-dimer means
 8:  [50],                       # §29 both times long, mix fails — heparin contamination
 9:  [32, 79],                   # §30 hemarthrosis and the expected screen
 10: [32],                       # §30 hemophilia A vs B
 11: [32, 79],                   # §30 severity tracks the factor level
 12: [32],                       # §30 the inhibitor and the bypassing agent
 13: [32],                       # §30 emicizumab and the falsely short aPTT
 14: [32, 79],                   # §30 activity-to-antigen ratio — type 2
 15: [32],                       # §30 desmopressin mechanism
 16: [32, 36],                   # §30 type 2B — concentrate, not desmopressin
 17: [36, 32],                   # §30 Bernard-Soulier
 18: [36, 32],                   # §30 Glanzmann versus aspirin
 19: [32, 68],                   # §30 the grey zone and blood group O
 20: [68, 32],                   # §30 reading the pedigree
 21: [(32, S28), (36, S28)],     # §31 disseminated intravascular coagulation
 22: [(32, S28)],                # §31 factor V separates vitamin K from liver
 23: [(32, S28)],                # §31 the INR in cirrhosis
 24: [(32, S28)],                # §31 hemorrhagic disease of the newborn
 25: [(32, S28)],                # §31 Heyde syndrome
}
