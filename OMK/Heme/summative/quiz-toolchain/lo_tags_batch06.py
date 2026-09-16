# Jeevs Edition batch 6 = TRANSFUSION MEDICINE, part 2  (Objective Review §12 + §13 + §14)
# Native objectives: §12 s11-products -> LO 31, 74 · §13 s12-immuno -> LO 31, 61
#                    §14 s13-reactions -> LO 61
S11, S12, S13 = "s11-products", "s12-immuno", "s13-reactions"

LO_TAGS = {
 1:  [74],                          # §12 the 30% threshold — treating the number
 2:  [74, (31, S11)],               # §12 storage conditions, the platelet exception
 3:  [74],                          # §12 albumin — volume without hemostasis
 4:  [(31, S12)],                   # §13 type and screen versus type and cross
 5:  [(31, S12)],                   # §13 front type / back type discrepancy
 6:  [(61, S12), (31, S12)],        # §13 hemolytic disease of the fetus and newborn
 7:  [(31, S12)],                   # §13 alloimmunization in sickle cell disease
 8:  [61],                          # §14 the reaction algorithm — stop first
 9:  [61],                          # §14 mild allergic reaction, may resume
 10: [61],                          # §14 the transfusion-refusal conversation
}
