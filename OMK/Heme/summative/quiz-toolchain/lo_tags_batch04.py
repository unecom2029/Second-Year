# Jeevs Edition batch 4 = ANEMIA II · HEMOLYSIS, part 2  (Objective Review §8 + §9 + §10)
# Native objectives: §8 -> LO 25 · §9 -> LO 28 · §10 -> LO 7, 28
# LO 28 spans §9 and §10, so globin items use the (LO, anchor) pair form.
S7, S8, S9 = "s7-hemolysis", "s8-membrane-enzyme", "s9-globin"

LO_TAGS = {
 1:  [25],                                   # §8 pigment gallstones from bilirubin load
 2:  [25],                                   # §8 filtered free heme → acute kidney injury
 3:  [25],                                   # §8 acholuric jaundice — unconjugated, albumin-bound
 4:  [28, (51, "s10-spleen")],               # §9 splenectomy · §11 vaccinate first
 5:  [28],                                   # §9 pyruvate kinase — ATP depletion
 6:  [28],                                   # §9 infection is the commonest G6PD trigger
 7:  [28],                                   # §9 autosomal dominant inheritance, independence
 8:  [(28, S9)],                             # §10 marrow expansion, ineffective erythropoiesis
 9:  [(28, S9)],                             # §10 raised hemoglobin A2 in beta-thalassemia trait
 10: [(28, S9)],                             # §10 cis vs trans alpha deletions — hydrops risk
 11: [(7, S9)],                              # §10 acute chest syndrome
 12: [(7, S9)],                              # §10 the three variables controlling sickling
 13: [(7, S9)],                              # §10 transcranial Doppler → chronic transfusion
 14: [(7, S9), (51, "s10-spleen")],          # §10 autosplenectomy · §11 encapsulated organisms
 15: [(7, S9), (25, S7)],                    # §10 hemolysis arm · §8 free plasma hemoglobin
}
