S47 = "s42-lymphatics"   # LO 63 lists §35 (node architecture) first, so §47 items need the pair form

LO_TAGS = {
 1:  [17],                 # bleomycin — pulmonary fibrosis, marrow spared
 2:  [17],                 # vincristine vs vinblastine dose-limiting toxicity
 3:  [17],                 # cumulative lifetime anthracycline dose
 4:  [17],                 # irinotecan early cholinergic diarrhea → atropine
 5:  [17],                 # antiemetic suffixes: -pitant = neurokinin-1
 6:  [17],                 # cytarabine — conjunctivitis and cerebellar ataxia
 7:  [17, 64],             # procarbazine is a monoamine oxidase inhibitor
 8:  [17, 2],              # plerixafor + G-CSF for stem cell mobilization
 9:  [(63, S47)],          # thoracic duct injury → chylothorax
 10: [(63, S47), (34, "s43-lymphedema")],   # why lymphatic obstruction swells more
 11: [(63, S47)],          # Peyer's patches, IgA, ileocecal resection
 12: [(63, S47)],          # thymic positive selection
 13: [64],                 # topoisomerase I vs II
 14: [11, 16],             # IgG4 for checkpoint inhibitors; antibody nomenclature
 15: [16],                 # lenalidomide → venous thromboembolism
 16: [15],                 # abiraterone, CYP17 and mineralocorticoid excess
 17: [34],                 # hypoalbuminemia after resuscitation
 18: [34],                 # inflammatory capillary leak — the expected swelling
 19: [60],                 # testis → para-aortic, not inguinal
 20: [60],                 # the dentate line watershed
}
