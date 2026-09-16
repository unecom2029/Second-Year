# Jeevs Edition batch 13 = LABORATORY FOUNDATIONS  (Objective Review §23–§25)
# Native objectives:
#   §23 s20-cbc-method       -> LO 27 (CBC components, methodology, interferences), LO 59 (accuracy/precision)
#   §24 s21-smear            -> LO 27, LO 5 (Babesia/Plasmodium on the smear)
#   §25 s22-cbc-interference -> LO 27
S20, S21, S22 = "s20-cbc-method", "s21-smear", "s22-cbc-interference"

LO_TAGS = {
 1:  [27],                          # §23 measured vs calculated
 2:  [27, (20, "s4-iron")],         # §23 thalassemia vs iron deficiency by RBC count
 3:  [27, (19, "s3-anemia-eval")],     # §23 the reticulocyte branch point
 4:  [59, 27],                      # §23 accuracy vs precision
 5:  [27],                          # §23 the scattergram
 6:  [27],                          # §23 immature platelet fraction
 7:  [27],                          # §23 the averaging trap
 8:  [(27, S21)],                   # §24 feather edge artefact
 9:  [(27, S21)],                   # §24 echinocyte vs acanthocyte
 10: [(27, S21), (28, "s9-globin")],# §24 target cells -> electrophoresis
 11: [(27, S21), (33, "s29-tma")],  # §24 schistocytes and the coagulation screen
 12: [(5, S21)],                    # §24 malaria species and hypnozoites
 13: [(27, S21), (20, "s4-iron")],  # §24 the toddler, the smear and the milk
 14: [(27, S21)],                   # §24 transfusing a chronic anemia
 15: [(27, S22)],                   # §25 cold agglutinins
 16: [(27, S22)],                   # §25 pseudothrombocytopenia
 17: [(27, S22)],                   # §25 microcytes counted as platelets
 18: [(27, S22)],                   # §25 nucleated red cells in the white count
 19: [(27, S22)],                   # §25 lipemia and the hemoglobin reading
 20: [(27, S22)],                   # §25 the uninverted tube
}
