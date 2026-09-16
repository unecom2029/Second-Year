# Jeevs Edition batch 19 = HEMATOLOGIC MALIGNANCY part 1 (Objective Review §36–§39)
#   §36 s32-malig-core -> LO 6 (grade/stage), LO 58 (myeloid vs lymphoid)
#   §37 s33-aml        -> LO 39, 54, 80 (APL), 82
#   §38 s34-mds-cml    -> LO 37 (MDS), 39
#   §39 s35-mpn        -> LO 38
S32, S33, S34, S35 = "s32-malig-core", "s33-aml", "s34-mds-cml", "s35-mpn"

LO_TAGS = {
 1:  [58, 6],                    # §36 differentiation stage sets tempo
 2:  [58],                       # §36 blasts are non-functional
 3:  [6, 58],                    # §36 tumor lysis syndrome
 4:  [80, 54],                   # §36/§37 APL — start ATRA on suspicion
 5:  [6],                        # §36 the grade paradox
 6:  [80],                       # §37 ATRA releases the maturation block
 7:  [(58, S33), 39],            # §37 flow cytometry assigns lineage
 8:  [39],                       # §37 fitness, not age
 9:  [82, 39],                   # §37 therapy-related myeloid neoplasm
 10: [37, 39],                   # §37/§38 the 20% line
 11: [37],                       # §38 the MDS paradox
 12: [37],                       # §38 what actually kills in MDS
 13: [39, (66, "s24-reactive")], # §38 CML versus a leukemoid reaction
 14: [39],                       # §38 phase criteria
 15: [39],                       # §38 the T315I gatekeeper mutation
 16: [38],                       # §39 polycythemia vera
 17: [38],                       # §39 ruxolitinib in myelofibrosis
 18: [38],                       # §39 essential thrombocythemia risk
 19: [38],                       # §39 the polycythemia split
 20: [38, (52, "s31-vte-management")],  # §39 one pathway, three diseases
}
