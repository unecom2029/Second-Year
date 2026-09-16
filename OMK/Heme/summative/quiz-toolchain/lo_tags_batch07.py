# Jeevs Edition batch 7 = HEMOSTASIS PHARMACOLOGY  (Objective Review §15 + §16)
# Native objectives:
#   §15 s14-anticoag     -> LO 8 (warfarin interactions), 12 (reversal), 26 (slow onset,
#                           bridging), 48 (mechanisms), 69 (uses/contraindications/pregnancy)
#   §16 s15-antiplatelet -> LO 62 (fibrinolytics), 71 (antiplatelets), 12, 69
# LO 12 and LO 69 span both sections, so the (LO, anchor) pair form is used whenever the
# question sits in the objective's second section.
S14, S15 = "s14-anticoag", "s15-antiplatelet"

LO_TAGS = {
 1:  [(48, S14)],                    # §15 heparin chain length and target
 2:  [69, (48, S14)],                # §15 HIT — recognition and management
 3:  [69, 26],                       # §15 why warfarin alone is hazardous in HIT
 4:  [26],                           # §15 factor half-lives and the bridge
 5:  [26, (48, S14)],                # §15 warfarin-induced skin necrosis
 6:  [8],                            # §15 CYP2C9 inhibition raises the INR
 7:  [8, 69],                        # §15 vitamin K in the diet — consistency
 8:  [69],                           # §15 pregnancy — warfarin is teratogenic
 9:  [12],                           # §15 idarucizumab for dabigatran
 10: [12],                           # §15 4F-PCC for a factor Xa inhibitor
 11: [69],                           # §15 renal impairment and reversibility
 12: [69, 8],                        # §15 rivaroxaban must be taken with food
 13: [69],                           # §15 choosing a DOAC in kidney disease
 14: [69],                           # §15 mechanical valve — warfarin only
 15: [(48, S14)],                    # §15 antithrombin deficiency → heparin resistance
 16: [71],                           # §16 aspirin, irreversible COX-1 inhibition
 17: [71],                           # §16 clopidogrel, CYP2C19 and omeprazole
 18: [(69, S15), 71],                # §16 prasugrel after stroke or TIA
 19: [71],                           # §16 ticagrelor and dyspnea
 20: [71],                           # §16 glycoprotein IIb/IIIa thrombocytopenia
 21: [71, (69, S15)],                # §16 cilostazol boxed warning in heart failure
 22: [71, 69],                       # §16 white clot versus red clot
 23: [62],                           # §16 plasminogen → plasmin
 24: [62, (12, S15)],                # §16 reversing thrombolysis
 25: [62, (69, S15)],                # §16 thrombolysis contraindications
}
