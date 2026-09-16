S40, S41, S42 = "s36-all-lymphoma", "s36b-lpd", "s37-plasma-cell"

# LO 21, 30, 41, 56 all list §41 first, so §40 items must use the pair form.
# LO 67 lists §51 (pediatric prognosis) first — pair it to §40 as well.
LO_TAGS = {
 1:  [40],                       # ALL leaves the marrow → CNS prophylaxis
 2:  [(67, S40)],                # favorable/unfavorable factors in childhood leukemia
 3:  [40, (67, S40)],            # BCR::ABL1 B-ALL → tyrosine kinase inhibitor
 4:  [40],                       # T-lymphoblastic lymphoma, thymic mass
 5:  [(30, S40)],                # double hit outranks the International Prognostic Index
 6:  [(30, S40)],                # CLL — a high lymphocyte count is not a treatment indication
 7:  [(30, S40)],                # CLL — autoimmune hemolysis, not marrow infiltration
 8:  [(21, S40)],                # Hodgkin → excisional biopsy
 9:  [(30, S40), (3, S42)],      # Waldenström hyperviscosity → plasmapheresis
 10: [(41, S40)],                # gastric MALT → eradication
 11: [(41, S40)],                # nodal marginal zone + hepatitis C → antiviral
 12: [(41, S40)],                # CD5+/CD23− → mantle cell, cyclin D1
 13: [(21, S41)],                # nodular sclerosis vs mixed cellularity = fibrosis
 14: [(21, S41)],                # PAX5 and the built-in internal control
 15: [(21, S41)],                # NLPHL retains CD20 → rituximab
 16: [(21, S41), (30, S41)],     # contiguous vs noncontiguous spread
 17: [(56, S41)],                # Burkitt — MYC, BCL2 negative
 18: [(56, S41)],                # follicular — BCL2 positive inside the follicle
 19: [57],                       # hairy cell — dry tap and monocytopenia
 20: [57],                       # mycosis fungoides → Sézary, clonality
 21: [57],                       # dermatopathic lymphadenopathy, the staging trap
 22: [57],                       # ALCL vs classic Hodgkin — ALK
 23: [57],                       # ATLL — HTLV-1, flower cells
 24: [3],                        # MGUS vs smoldering — 10 and 3
 25: [3],                        # free light chains and cast nephropathy
 26: [3],                        # myeloma vs Waldenström
}
