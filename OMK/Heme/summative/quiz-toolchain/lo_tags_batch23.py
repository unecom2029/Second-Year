S51 = "s46-pediatric"
S52 = "s47-hypersplenism"
S11 = "s10-spleen"
S55 = "s52-splenic-trauma"
S58 = "s55-geriatric-assessment"

# LO 65 lists §51 first — bare 65 is fine.
# LO 67 lists §51 first — bare 67 is fine.
# LO 73 lists §55 first, so hypersplenism items need the pair form.
# LO 51 lists §11 first — bare 51 lands on s10-spleen.
# LO 77 lists §53 (s48-aging) first; the functional-assessment items pair to §58.

LO_TAGS = {
 # Group 1 — pediatrics, spleen & prescribing
 1:  [65],                       # well vs sick pancytopenic child
 2:  [65],                       # Fanconi vs TAR — the thumbs
 3:  [65],                       # Wiskott-Aldrich, small platelets
 4:  [67],                       # ploidy and translocation in childhood ALL
 5:  [(73, S52)],                # congestive hypersplenism from portal hypertension
 6:  [(73, S52)],                # splenic vein thrombosis → gastric varices
 7:  [51, (73, S52)],            # OPSI prevention and vaccine timing
 8:  [51, 7],                    # Howell-Jolly bodies, fever in functional asplenia
 9:  [78],                       # the missing element — quantity to dispense
 10: [78],                       # patient-safety writing conventions

 # Group 2 — trauma, edema & metastasis
 11: [47, 73],                   # unstable + positive FAST → laparotomy
 12: [47],                       # stable + blush → embolization
 13: [47, 73],                   # delayed rupture on day 5–6
 14: [73],                       # spontaneous rupture in mononucleosis
 15: [47],                       # post-splenectomy thrombocytosis → aspirin
 16: [47, (73, S55)],            # pancreatic tail injury at the hilum
 17: [34],                       # hematoma — immediate, focal, expanding
 18: [60],                       # the subcapsular sinus
 19: [60],                       # why carcinoma prefers lymphatics
 20: [60],                       # medial breast → internal mammary

 # Group 3 — geriatrics
 21: [77],                       # marrow cellularity = 100 − age
 22: [77, 49],                   # anemia is never "just age"; iron deficiency → endoscopy
 23: [77],                       # inflammaging in treated HIV
 24: [(77, S58)],                # ADL vs IADL, and the anticoagulation crossover
 25: [(77, S58), 78],            # no safe medication for dementia behaviours
}
