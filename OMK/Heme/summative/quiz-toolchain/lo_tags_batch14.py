# Jeevs Edition batch 14 = BENIGN WHITE CELL DISORDERS  (Objective Review §26–§28)
# Native objectives:
#   §26 s23-wbc-normal -> LO 76 (normal leukocytes, cell levels, ANC)
#   §27 s24-reactive   -> LO 66 (reactive vs malignant)
#   §28 s25-immunodef  -> LO 4  (primary immunodeficiencies)
S23, S24, S25 = "s23-wbc-normal", "s24-reactive", "s25-immunodef"

LO_TAGS = {
 1:  [76],                       # §26 the absolute neutrophil count
 2:  [76],                       # §26 febrile neutropenia
 3:  [76],                       # §26 Duffy-null
 4:  [76],                       # §26 mechanisms of neutropenia — adults and drugs
 5:  [76],                       # §26 bacteriostatic therapy in a defenceless host
 6:  [76, (1, "s17-sepsis")],    # §26 infection without leukocytosis · sepsis criteria
 7:  [(66, S24)],                       # §27 leukemoid reaction
 8:  [(66, S24)],                       # §27 the inverted blast pyramid
 9:  [(66, S24)],                       # §27 reactive lymphocytosis
 10: [(66, S24)],                       # §27 leukoerythroblastic picture
 11: [(66, S24)],                       # §27 basophilia and BCR-ABL
 12: [(66, S24)],                       # §27 pertussis lymphocytosis
 13: [4],                        # §28 chronic granulomatous disease
 14: [4],                        # §28 the catalase logic
 15: [4],                        # §28 Bruton agammaglobulinemia
 16: [4],                        # §28 severe combined immunodeficiency
 17: [4],                        # §28 DiGeorge and the branchial pouches
 18: [4, (31, "s11-products")],  # §28 irradiated components · blood product modification
 19: [4],                        # §28 live vaccines in T-cell deficiency
 20: [4],                        # §28 ADA deficiency and the limits of transplant
}
