# Jeevs Edition batch 5 = TRANSFUSION MEDICINE  (Objective Review §12 + §13 + §14)
# Native objectives:
#   §12 s11-products  -> LO 31, 74
#   §13 s12-immuno    -> LO 31, 61
#   §14 s13-reactions -> LO 61
# LO 31 spans §12 and §13 and LO 61 spans §13 and §14, so both use the (LO, anchor)
# pair form wherever the question is not in the objective's first-listed section.
S11, S12, S13 = "s11-products", "s12-immuno", "s13-reactions"

LO_TAGS = {
 1:  [74],                                   # §12 restrictive threshold, TRICC
 2:  [74],                                   # §12 platelet threshold before a procedure
 3:  [74, (36, "s45-itp")],                  # §12 consumptive vs hypoproliferative · §50 ITP
 4:  [74],                                   # §12 cryoprecipitate for fibrinogen
 5:  [74, (12, "s14-anticoag")],             # §12 product choice · §15 warfarin reversal
 6:  [74],                                   # §12 specific concentrate, not plasma
 7:  [(31, S11)],                            # §12 what is in the bag — citrate
 8:  [(31, S12)],                            # §13 naturally occurring ABO antibodies
 9:  [(31, S12)],                            # §13 emergency release and RhD rationing
 10: [(31, S12), (61, S12)],                 # §13 alloimmunization → HDFN
 11: [(31, S12)],                            # §13 antibody screen → antigen-negative units
 12: [61, (31, S12)],                        # §14 delayed hemolytic reaction · §13 alloantibody
 13: [(31, S12), (74, S11)],                 # §13 plasma compatibility inversion · §12 product
 14: [61],                                   # §14 acute hemolytic reaction
 15: [61],                                   # §14 TRALI
 16: [61],                                   # §14 TACO — the matched-set contrast
 17: [61],                                   # §14 febrile nonhemolytic → leukoreduction
 18: [61],                                   # §14 anaphylaxis and IgA deficiency
 19: [61],                                   # §14 septic platelet unit
 20: [61],                                   # §14 TA-GVHD → irradiation
}
