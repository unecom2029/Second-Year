# Jeevs Edition batch 11 = INFECTION  (Objective Review §18–§22)
# Native objectives:
#   §18 s17-sepsis            -> LO 1 (screens + labs), LO 75 (microbial triggers)
#   §19 s18-hiv-micro         -> LO 14 (drug classes + resistance), LO 24 (structural genes)
#   §20 s19-hiv-clinical      -> LO 77 (the section's own objective; anchor form, since
#                                LO 77 is first listed under §53 aging)
#   §21 s19b-vector-infections-> LO 5 (Babesia/Plasmodium), LO 22 (Bartonella), LO 23 (plague)
#   §22 s19c-vhf              -> LO 13 (the hemorrhagic fevers)
S17, S18, S19, S19B, S19C = "s17-sepsis", "s18-hiv-micro", "s19-hiv-clinical", "s19b-vector-infections", "s19c-vhf"

LO_TAGS = {
 1:  [1],                        # §18 bidirectional criteria, qSOFA, the bundle
 2:  [1],                        # §18 procalcitonin — the one cause-specific marker
 3:  [75],                       # §18 viral sepsis via DAMPs
 4:  [75],                       # §18 source predicts organism — abdominal anaerobe
 5:  [24],                       # §19 p24 and the gag gene
 6:  [14],                       # §19 NNRTI genetic barrier
 7:  [14],                       # §19 tropism and maraviroc
 8:  [(77, S19), (24, S18)],     # §20 the testing algorithm · §19 p24 timing
 9:  [(77, S19)],                # §20 PJP and the steroid threshold
 10: [(77, S19)],                # §20 paradoxical IRIS
 11: [(77, S19)],                # §20 the CD4 thresholds
 12: [23],                       # §21 bubonic plague
 13: [23],                       # §21 the blocked proventriculus
 14: [22],                       # §21 bacillary angiomatosis vs Kaposi
 15: [5],                        # §21 babesiosis
 16: [5],                        # §21 chloroquine and heme polymerase
 17: [13],                       # §22 dengue and the NSAID rule
 18: [13],                       # §22 hantavirus HFRS
 19: [13],                       # §22 Lassa fever
 20: [13],                       # §22 Crimean-Congo hemorrhagic fever
}
