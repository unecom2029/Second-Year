# Jeevs Edition batch 3 = ANEMIA II · HEMOLYSIS  (Objective Review §8 + §9 + §10)
# Native objectives of that block:
#   §8  s7-hemolysis       -> LO 25
#   §9  s8-membrane-enzyme -> LO 28
#   §10 s9-globin          -> LO 7, 28
# Every question leads with a native LO. LO 28 spans two sections, so the pair form
# (LO, anchor) is used for every globin-disorder item — a bare 28 would send the chip
# to the membrane/enzyme section.
S7, S8, S9 = "s7-hemolysis", "s8-membrane-enzyme", "s9-globin"

LO_TAGS = {
 1:  [25],                        # §8 intravascular — hemoglobinemia and hemoglobinuria
 2:  [25],                        # §8 which markers localize destruction
 3:  [25, (19, "s3-anemia-eval")],  # §8 corrected reticulocyte count · §3 classification
 4:  [28],                        # §9 hereditary spherocytosis — Coombs-negative
 5:  [28],                        # §9 osmotic fragility — surface area to volume
 6:  [28],                        # §9 aplastic crisis, parvovirus B19
 7:  [28],                        # §9 spherocytes with a POSITIVE antiglobulin test
 8:  [28],                        # §9 G6PD — bite cells after an oxidant drug
 9:  [28],                        # §9 G6PD — NADPH and glutathione
 10: [28],                        # §9 the falsely normal enzyme assay
 11: [28],                        # §9 enzyme half-life — why class III is self-limited
 12: [(28, S9)],                  # §10 counting alpha genes — hemoglobin H
 13: [(28, S9)],                  # §10 hemoglobin Barts — oxygen affinity
 14: [(28, S9)],                  # §10 the globin switch — onset at 6 months
 15: [(28, S9), (20, "s4-iron")], # §10 thalassemia trait vs iron deficiency
 16: [(28, S9), (9, "s16-anemia-drugs")],  # §10 transfusional iron overload · §17 chelation
 17: [(28, S9)],                  # §10 electrophoresis — trait versus disease
 18: [(7, S9), (51, "s10-spleen")],  # §10 fever in sickle cell disease · §11 asplenia
 19: [(7, S9)],                   # §10 the three crises
 20: [(7, S9)],                   # §10 hydroxyurea — raising hemoglobin F
}
