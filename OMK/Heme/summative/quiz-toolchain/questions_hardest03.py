# Hardest Exam — batch H3 of 5 (questions 41–60)
# Sections §29–§35 plus §49 and §50: the cascade and mixing study, inherited and acquired bleeding,
# immune thrombocytopenia, the thrombotic microangiopathies, thrombophilia and antiphospholipid
# syndrome, heparin-induced thrombocytopenia, duration of anticoagulation, and lymph node pathology.

Q = []


def q(stem, opts, correct, explanation, eli5, image=None, imcap=None, exim=None, excap=None):
    assert correct in opts, correct
    assert opts[correct] == "", "keyed option must carry an empty wrong-explanation"
    assert "Educational objective:" in explanation
    bodies = sorted(opts, key=str.lower)
    ci = bodies.index(correct)
    d = {
        "stem": stem,
        "choices": [f"{chr(65 + i)}. {b}" for i, b in enumerate(bodies)],
        "correct": ci,
        "explanation": explanation,
        "wrongExplanations": {str(i): opts[b] for i, b in enumerate(bodies) if i != ci},
        "eli5": eli5,
    }
    if image:
        d["image"] = image
        d["imageCaption"] = imcap
    if exim:
        d["explanationImage"] = exim
        d["explanationImageCaption"] = excap
    Q.append(d)


# ── 41. Reading the bleeding pattern — hemarthrosis (§29, §30) ──────────────────
q(
    "A 6-year-old boy is brought to the emergency department by his mother due to a swollen, painful "
    "right knee that developed overnight after he fell from a swing. He has had two similar episodes "
    "of joint swelling in the past year and a large thigh hematoma after a vaccination in infancy. "
    "He has never had nosebleeds, gum bleeding or petechiae. His maternal uncle has a bleeding "
    "disorder. The right knee is warm, swollen and held in flexion.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 11.8 g/dL (N=11.5–15.5 g/dL)\n"
    "Platelet count 288,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 13 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 74 sec (N=25–40 sec)\n"
    "Fibrinogen 310 mg/dL (N=200–400 mg/dL)\n\n"
    "A 1:1 mix of the patient's plasma with normal pooled plasma corrects the partial "
    "thromboplastin time to 33 seconds. Which of the following is the most likely underlying "
    "abnormality?",
    {
        "Deficiency of factor VIII": "",
        "Deficiency of factor XII":
            "Factor XII deficiency prolongs the aPTT and corrects on mixing, but it causes NO "
            "bleeding at all — the body has a backup contact system even though the tube assay does "
            "not. It is the classic incidental finding on preoperative screening.",
        "Deficiency of factor XIII":
            "Factor XIII cross-links fibrin AFTER the clot has formed, so the PT, aPTT and platelet "
            "count are all normal. It causes delayed bleeding and delayed wound healing — classically "
            "after circumcision.",
        "Deficiency of von Willebrand factor":
            "Von Willebrand disease bleeds mucocutaneously — nosebleeds, gum bleeding, menorrhagia — "
            "because the protein tethers platelets to collagen. The aPTT is usually normal unless "
            "factor VIII falls secondarily.",
        "Deficiency of glycoprotein Ib/IX/V":
            "Bernard-Soulier syndrome is a platelet adhesion defect: mucocutaneous bleeding, a low "
            "count with large platelets on the smear, and normal clotting times.",
        "Deficiency of glycoprotein IIb/IIIa":
            "Glanzmann thrombasthenia prevents fibrinogen from bridging platelets. Again the bleeding "
            "is mucocutaneous and the PT and aPTT are normal, because the plasma assays cannot see "
            "platelets at all.",
    },
    "Deficiency of factor VIII",
    "Hemophilia A. Two readings make the diagnosis before any factor assay is sent.\n\n"
    "1. WHERE he bleeds. Platelets patch SURFACES, so platelet and von Willebrand disorders bleed "
    "from skin and mucosa — epistaxis, gum bleeding, menorrhagia, petechiae. Fibrin fills SPACES, so "
    "coagulation factor deficiencies bleed into joints and muscles — hemarthrosis and deep "
    "hematomas. He has spaces, not surfaces.\n\n"
    "2. WHICH test is long. An isolated prolonged aPTT with a normal PT points to the intrinsic "
    "pathway: factors VIII, IX, XI, XII. Of those, VIII (hemophilia A, 1 in 5,000 males) and IX "
    "(hemophilia B, 1 in 30,000 males) are X-linked and clinically identical — the maternal uncle "
    "fits that inheritance. Factor XI bleeds mildly; factor XII does not bleed at all.\n\n"
    "The mixing study then asks: missing, or blocked? It CORRECTED, so a factor is deficient rather "
    "than inhibited. Factor VIII and IX activity assays separate A from B.\n\n"
    "Severity is defined by the factor level, not the symptoms: under 1% severe (spontaneous "
    "bleeding), 1%–5% moderate (minor trauma), 5%–30% mild (surgery or significant trauma only). "
    "Repeated hemarthrosis scars the joint, which is why prophylaxis exists. Treat with recombinant "
    "factor concentrate — not plasma or cryoprecipitate — or, for patients with inhibitors, "
    "emicizumab, a bispecific antibody that simply holds factor IXa and factor X together the way "
    "factor VIIIa does.\n\n"
    "Educational objective: Bleeding into joints and muscles indicates a coagulation factor "
    "deficiency, whereas mucocutaneous bleeding indicates a platelet or von Willebrand factor "
    "problem. An isolated prolonged aPTT that corrects on mixing points to deficiency of factor "
    "VIII, IX, XI or XII, and only factor XII deficiency does not bleed.",
    "Where you bleed tells you what is broken. Platelets seal leaks on surfaces like the nose and "
    "gums; the clotting proteins fill deeper spaces like joints. His knee bleed means a clotting "
    "protein is missing.",
    exim="fig_slide_bleeding_pattern",
    excap="Platelet defects bleed from surfaces; coagulation defects bleed into spaces. The pattern "
          "points before any assay is sent.",
)

# ── 42. Acquired factor VIII inhibitor — the incubated mix (§29, §31) ───────────
q(
    "A 74-year-old woman comes to the emergency department due to 1 week of large spontaneous "
    "bruises on her arms, flank and thighs. She has never had abnormal bleeding, including after a "
    "hysterectomy at age 46 and two dental extractions. She has rheumatoid arthritis. She takes no "
    "anticoagulant. Examination shows extensive ecchymoses and a tense hematoma of the left "
    "forearm.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 9.1 g/dL (N=12.0–16.0 g/dL)\n"
    "Platelet count 302,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 12 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 66 sec (N=25–40 sec)\n\n"
    "A 1:1 mix with normal pooled plasma immediately after mixing gives a partial thromboplastin "
    "time of 35 seconds; after incubation at 37 C for 60 minutes, the mixed sample measures 61 "
    "seconds. Which of the following best explains these findings?",
    {
        "An antibody that neutralizes factor VIII": "",
        "An antibody directed against phospholipid":
            "A lupus anticoagulant also fails to correct on mixing — but it does so IMMEDIATELY, "
            "not after incubation, and it corrects when excess phospholipid is added. It also causes "
            "thrombosis, not spontaneous soft-tissue bleeding.",
        "Contamination of the sample with heparin":
            "Heparin from a line draw prolongs the aPTT and fails to correct on mixing, but she is "
            "on no anticoagulant and the finding would not be time-dependent.",
        "Inherited deficiency of factor IX":
            "Hemophilia B is X-linked and lifelong. A woman of 74 with uneventful surgery and dental "
            "extractions does not have a congenital factor deficiency declaring itself now.",
        "Underfilling of the sodium citrate tube":
            "A short-draw blue top has proportionally too much citrate, which artificially prolongs "
            "the clotting time — but it is a pre-analytic artefact in a patient with no bleeding, and "
            "it corrects fully on mixing.",
        "Vitamin K deficiency from poor intake":
            "Vitamin K deficiency prolongs the PT FIRST, because factor VII has the shortest "
            "half-life. Her PT is normal.",
    },
    "An antibody that neutralizes factor VIII",
    "Acquired hemophilia A — an autoantibody against factor VIII. The vignette is built from the "
    "three features that define it.\n\n"
    "1. A NEW bleeding diathesis in an older patient with a negative lifetime history. Congenital "
    "factor deficiencies declare themselves in childhood or at a first hemostatic challenge; a "
    "diathesis appearing suddenly at 74 is acquired until proven otherwise. Associations: autoimmune "
    "disease (her rheumatoid arthritis), malignancy, and the postpartum state.\n\n"
    "2. An isolated prolonged aPTT — factor VIII is an intrinsic pathway factor.\n\n"
    "3. The mixing study. Adding normal plasma supplies every factor at about 50%, which is enough "
    "for hemostasis, so a DEFICIENCY corrects. An INHIBITOR does not, because the antibody attacks "
    "the donated factor too. The trap here is that anti-factor VIII antibodies are slow and "
    "temperature-dependent: on an immediate mix they look like a deficiency, and only after "
    "incubation at 37 C for 30–60 minutes does the clotting time drift back out. An immediate mix "
    "that corrects therefore does not exclude an inhibitor.\n\n"
    "Confirm with a factor VIII activity level and a Bethesda titre to quantify the antibody. "
    "Management has two halves: control bleeding with a BYPASSING agent (infused factor VIII would "
    "simply be neutralized), and eradicate the antibody with immunosuppression — which is what "
    "distinguishes acquired from congenital disease, where the deficiency is permanent.\n\n"
    "Educational objective: A new bleeding diathesis in an older adult with an isolated prolonged "
    "aPTT that fails to correct on an INCUBATED mixing study indicates an acquired factor VIII "
    "inhibitor. Treatment is a bypassing agent for bleeding plus immunosuppression to eradicate the "
    "antibody.",
    "Her body has started making an antibody that destroys one of her clotting proteins. Adding "
    "normal plasma looks like it fixes the test at first, but wait an hour and the antibody eats "
    "that too — which is how you catch it.",
    exim="fig_slide_mixing_study",
    excap="The mixing study: corrects means deficiency, fails to correct means inhibitor — and a "
          "slow inhibitor needs the incubated version.",
)

# ── 43. Type 2 von Willebrand disease (§30) ─────────────────────────────────────
q(
    "A 24-year-old woman comes to the office due to heavy menstrual bleeding. Her periods have "
    "soaked through a pad every 2 hours for 7 days since menarche at age 12, and she has frequent "
    "nosebleeds and bruises on her thighs. She bled for 2 days after a dental extraction at 16. Her "
    "mother and older sister have similar symptoms. She takes no medications and has never been "
    "pregnant. She is blood group A.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 10.4 g/dL (N=12.0–16.0 g/dL)\n"
    "Platelet count 244,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 12 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 33 sec (N=25–40 sec)\n"
    "von Willebrand factor antigen 62% (N=50%–200%)\n"
    "Ristocetin cofactor activity 20% (N=50%–200%)\n"
    "Factor VIII activity 58% (N=50%–150%)\n\n"
    "Which of the following best characterizes this patient's disorder?",
    {
        "A qualitative defect in von Willebrand factor": "",
        "A quantitative deficiency of von Willebrand factor":
            "In type 1 disease, activity and antigen fall TOGETHER — the protein present is normal, "
            "there is simply less of it, and the ratio stays near 1. Her antigen is 62% while her "
            "activity is 20%.",
        "An acquired antibody against von Willebrand factor":
            "Acquired von Willebrand disease occurs with lymphoproliferative disease, and mechanically "
            "in aortic stenosis (Heyde syndrome). Lifelong symptoms from menarche with two affected "
            "relatives make an inherited disorder far more likely.",
        "Deficient hepatic synthesis of factor VIII":
            "Factor VIII is not made by hepatocytes at all — it is largely endothelial in origin and "
            "circulates bound to von Willebrand factor. Her factor VIII is normal.",
        "Loss of the platelet receptor for von Willebrand factor":
            "Bernard-Soulier syndrome is the other side of the same handshake — the GPIb receptor "
            "rather than the ligand. It gives a low platelet count with large platelets, and the "
            "ristocetin cofactor assay uses normal fixed platelets specifically to exclude it.",
    },
    "A qualitative defect in von Willebrand factor",
    "Type 2 von Willebrand disease. The whole algorithm is one comparison: are ACTIVITY and ANTIGEN "
    "similar?\n\n"
    "• Similar → the protein works normally, there is just not enough of it → QUANTITATIVE disease "
    "(type 1, the most common; type 3, essentially absent)\n"
    "• Antigen much higher than activity → the protein is present but broken → QUALITATIVE disease "
    "(type 2)\n\n"
    "Her ratio is 20/62 = 0.32, well below the 0.5–0.7 threshold. Multimer analysis is the next "
    "test and would be expected to show loss of the high molecular weight multimers.\n\n"
    "Why size matters: von Willebrand factor must stretch from collagen at the injury site out into "
    "flowing blood to catch a passing platelet by its GPIb receptor. Hemostatic activity therefore "
    "tracks multimer size, and a patient who makes only short multimers has plenty of antigen and "
    "still bleeds.\n\n"
    "Two further points in this vignette. Her normal aPTT is expected — von Willebrand disease is a "
    "disease of PRIMARY hemostasis, and the plasma clotting assays cannot see platelet function at "
    "all; only severe (type 3) disease prolongs the aPTT, by dragging factor VIII down with it. And "
    "menorrhagia from menarche with an affected mother and sister is the most commonly missed "
    "presentation of the most common inherited bleeding disorder.\n\n"
    "Treatment follows the subtype: desmopressin releases stored von Willebrand factor from "
    "endothelial Weibel-Palade bodies and works in type 1, but it is avoided in type 2B, where it "
    "worsens thrombocytopenia; types 2B and 3 need a plasma-derived or recombinant von Willebrand "
    "factor concentrate. Note also that group O individuals run lower levels at baseline — her group "
    "A makes a spuriously low value less likely.\n\n"
    "Educational objective: Comparing von Willebrand factor activity with antigen separates "
    "quantitative disease (types 1 and 3, both reduced proportionally) from qualitative disease "
    "(type 2, activity disproportionately low with loss of high molecular weight multimers). The "
    "routine coagulation screen is normal in most cases.",
    "Her body makes enough of the protein that glues platelets to a wound, but the protein is the "
    "wrong shape and cannot do its job. That is why the usual clotting tests look perfectly normal.",
    exim="fig_slide_ristocetin",
    excap="The ristocetin cofactor assay — normal fixed platelets are supplied, so the test reads "
          "only the patient's von Willebrand factor.",
)

# ── 44. Immune thrombocytopenia — the marrow finding (§50) ──────────────────────
q(
    "A 5-year-old boy is brought to the office by his father due to 3 days of bruising. Three weeks "
    "ago he had a cold that resolved. He is well and playing in the examination room. Temperature is "
    "36.9 C (98.4 F). There are scattered petechiae over both shins that do not blanch with "
    "pressure, and two blood blisters on the buccal mucosa. There is no lymphadenopathy, "
    "hepatomegaly, splenomegaly or bone tenderness.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 12.6 g/dL (N=11.5–15.5 g/dL)\n"
    "Leukocyte count 7,400/mm3 (N=4,500–13,500/mm3)\n"
    "Platelet count 14,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 12 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 31 sec (N=25–40 sec)\n\n"
    "The peripheral smear shows markedly reduced platelets with occasional large forms, and normal "
    "red cell and leukocyte morphology. If a bone marrow examination were performed, which of the "
    "following would most likely be found?",
    {
        "Absence of megakaryocytes with preserved other lineages":
            "Congenital amegakaryocytic thrombocytopenia and acquired pure megakaryocyte aplasia do "
            "exist, but they are rare and would not follow a viral illness in a previously well "
            "child.",
        "Extensive fibrosis with tear-drop red cells":
            "Marrow fibrosis produces a leukoerythroblastic smear with tear-drop cells, nucleated red "
            "cells and immature granulocytes, plus massive splenomegaly. His smear and examination "
            "are clean.",
        "Increased numbers of megakaryocytes": "",
        "Markedly hypocellular marrow with fat replacement":
            "Aplastic anemia fails every lineage, giving pancytopenia with a low reticulocyte count. "
            "His hemoglobin and white count are normal.",
        "Ringed sideroblasts on iron staining":
            "Ringed sideroblasts mark sideroblastic anemia and some myelodysplastic syndromes — "
            "an anemia with iron trapped in mitochondria, not an isolated thrombocytopenia.",
        "Sheets of lymphoblasts replacing normal elements":
            "Acute lymphoblastic leukemia is the diagnosis you must not miss, but it produces a "
            "sick-appearing child, usually with other cytopenias, organomegaly or bone pain, and "
            "blasts on the smear.",
    },
    "Increased numbers of megakaryocytes",
    "Acute immune thrombocytopenia (ITP) — post-viral, in a well child, with ISOLATED "
    "thrombocytopenia, normal clotting times and an otherwise normal smear.\n\n"
    "Mechanism: IgG autoantibody against platelet surface glycoprotein IIb/IIIa. The antibody is "
    "made in the spleen AND the coated platelets are consumed in the spleen — one organ doing both "
    "jobs, which is why the treatment ladder works the way it does.\n\n"
    "Because the destruction is PERIPHERAL, the marrow is not the problem: it responds by increasing "
    "megakaryocytes. That single finding separates destruction from underproduction, and it is the "
    "reason the other five options — each of which is a marrow-failure or marrow-replacement "
    "picture — are wrong.\n\n"
    "Note the supporting details: petechiae are non-blanching (hemorrhage, not rash); 'wet purpura' "
    "on the oral mucosa marks a higher bleeding risk than skin findings alone; and splenomegaly is "
    "RARE in ITP, so a big spleen should redirect you to hypersplenism, a lymphoproliferative "
    "disorder or portal hypertension.\n\n"
    "A marrow biopsy is not actually required in a typical case. Management in children is usually "
    "observation — about 80% recover spontaneously and intracranial hemorrhage occurs in under 0.1% "
    "— with IVIG or corticosteroids reserved for significant bleeding, and avoidance of aspirin and "
    "contact sports meanwhile.\n\n"
    "Educational objective: Immune thrombocytopenia is peripheral antibody-mediated platelet "
    "destruction, so the marrow shows INCREASED megakaryocytes, and the blood shows isolated "
    "thrombocytopenia with normal clotting times. Childhood disease follows a viral illness and "
    "usually resolves spontaneously.",
    "His body is making antibodies that stick to his platelets, and the spleen eats them. His bone "
    "marrow is fine — in fact it is working overtime making more.",
)

# ── 45. ITP recurrence after splenectomy — accessory spleen (§50, §11) ──────────
q(
    "A 39-year-old woman comes to the office due to recurrent easy bruising and gum bleeding. She "
    "has had immune thrombocytopenia for 6 years, with only transient responses to corticosteroids "
    "and intravenous immunoglobulin. She underwent laparoscopic splenectomy 8 months ago; her "
    "platelet count rose to 186,000/mm3 and remained normal for 5 months. She takes no medications "
    "and has not been ill.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 12.9 g/dL (N=12.0–16.0 g/dL)\n"
    "Leukocyte count 6,800/mm3 (N=4,500–11,000/mm3)\n"
    "Platelet count 16,000/mm3 (N=150,000–400,000/mm3)\n\n"
    "The peripheral smear shows reduced platelets and no Howell-Jolly bodies. Which of the following "
    "best explains this patient's findings?",
    {
        "Development of antibodies against transfused platelets":
            "Platelet alloimmunization causes refractoriness to platelet TRANSFUSION. She has not "
            "been transfused, and it would not explain a 5-month remission followed by relapse.",
        "Functioning accessory splenic tissue": "",
        "Marrow suppression by a myelodysplastic clone":
            "Myelodysplasia can present with thrombocytopenia, but usually with other cytopenias, "
            "dysplastic morphology on the smear, and in an older patient.",
        "Progression to a thrombotic microangiopathy":
            "A microangiopathy would add schistocytes, hemolytic anemia and organ injury. Her "
            "hemoglobin is normal and her smear is clean.",
        "Recurrent infection stimulating antibody production":
            "A viral trigger can precipitate childhood ITP, but she has not been ill, and an "
            "infection would not explain the absent Howell-Jolly bodies.",
    },
    "Functioning accessory splenic tissue",
    "Relapsed immune thrombocytopenia from a missed accessory spleen — and the smear proves it.\n\n"
    "After a complete splenectomy, red cells retain nuclear remnants that a working spleen would pit "
    "out, so HOWELL-JOLLY BODIES appear on the smear and stay there. Their ABSENCE 8 months after "
    "splenectomy means functioning splenic tissue is still present somewhere.\n\n"
    "Why that matters mechanistically: in ITP the spleen is both the factory making the "
    "anti-glycoprotein IIb/IIIa antibody and the site where the antibody-coated platelets are "
    "destroyed. Leave functioning splenic tissue behind and both jobs continue. Accessory spleens "
    "occur in about 20% of people, and more than 80% of them sit immediately adjacent to the spleen "
    "— so they are easy to miss and easy to find once suspected (imaging, or a heat-damaged red cell "
    "scan).\n\n"
    "Splenectomy otherwise gives sustained remission in 75%–85% of refractory patients. When it "
    "genuinely fails and no accessory spleen is found, the next options work at the two ends of the "
    "problem: rituximab removes the B cells making the antibody, and romiplostim (a thrombopoietin "
    "receptor agonist) pushes production instead of protecting the platelets.\n\n"
    "Educational objective: Recurrence of immune thrombocytopenia after an initially successful "
    "splenectomy suggests a retained accessory spleen, present in about 20% of people; the absence of "
    "Howell-Jolly bodies on the peripheral smear indicates that functioning splenic tissue remains.",
    "Her spleen was removed because it was eating her platelets, but people often have a small extra "
    "spleen hiding nearby. The clue is that her blood cells still look 'cleaned', which only a "
    "working spleen does.",
)

# ── 46. Vitamin K deficiency versus liver disease — the factor grid (§31) ───────
q(
    "A 68-year-old man who had a small bowel resection 3 weeks ago is evaluated because of oozing "
    "from his central line site. He has received nothing by mouth since surgery and has been treated "
    "with broad-spectrum antibiotics for an intra-abdominal collection. He does not drink alcohol, "
    "and there is no jaundice, ascites or splenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Platelet count 208,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 26 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 44 sec (N=25–40 sec)\n"
    "Fibrinogen 340 mg/dL (N=200–400 mg/dL)\n"
    "D-dimer 180 ng/mL (N=less than 250 ng/mL)\n"
    "Albumin 3.6 g/dL (N=3.5–5.5 g/dL)\n"
    "Bilirubin, total 0.8 mg/dL (N=0.1–1.0 mg/dL)\n\n"
    "Individual factor levels are sent. Which of the following results is most likely?\n\n"
    "Factor VII | Factor V | Factor VIII",
    {
        "Decreased, decreased, decreased":
            "Everything low, with a falling fibrinogen and a high D-dimer, is disseminated "
            "intravascular coagulation — factor VIII is consumed there along with the rest. His "
            "fibrinogen and D-dimer are normal.",
        "Decreased, decreased, increased":
            "This is hepatic synthetic failure: the liver makes factor V as well, so it falls, while "
            "factor VIII — which hepatocytes do NOT make — is normal or high. He has no stigmata of "
            "liver disease and a normal albumin and bilirubin.",
        "Decreased, normal, normal": "",
        "Normal, decreased, decreased":
            "Combined factor V and factor VIII deficiency is a rare inherited disorder of a shared "
            "intracellular transport protein, presenting with lifelong mild bleeding rather than "
            "after 3 weeks of starvation and antibiotics.",
        "Normal, normal, decreased":
            "An isolated low factor VIII is hemophilia A or an acquired factor VIII inhibitor. Either "
            "would prolong the aPTT alone and leave the PT normal — his PT is markedly prolonged.",
        "Normal, normal, normal":
            "Normal factor levels cannot coexist with a prothrombin time of 26 seconds unless the "
            "sample is artefactual, and there is no indication of that here.",
    },
    "Decreased, normal, normal",
    "Vitamin K deficiency — the predictable consequence of 3 weeks of no oral intake plus "
    "broad-spectrum antibiotics, which eliminate the gut flora that produce vitamin K.\n\n"
    "Vitamin K is required to gamma-carboxylate factors II, VII, IX and X, and the anticoagulants "
    "protein C and protein S. Factor V is NOT vitamin K dependent, which is exactly what makes it "
    "the discriminating assay:\n"
    "• Vitamin K deficiency or warfarin → factors II, VII, IX, X low; factor V NORMAL\n"
    "• Liver disease → all of them low, INCLUDING factor V, because the hepatocyte makes it\n\n"
    "A second check runs the other way. Factor VIII is not made by hepatocytes (it is largely "
    "endothelial and circulates bound to von Willebrand factor), so it is normal or high in liver "
    "disease but LOW in disseminated intravascular coagulation, where it is consumed with everything "
    "else.\n\n"
    "The PT prolongs first in vitamin K deficiency because factor VII has the shortest half-life "
    "(4–6 hours); the aPTT follows as factors IX and X fall. Fibrinogen and D-dimer stay normal, "
    "which excludes DIC.\n\n"
    "Treatment is vitamin K — and in serious bleeding, 4-factor prothrombin complex concentrate for "
    "immediate correction while the vitamin K restores endogenous synthesis. The same physiology "
    "explains neonatal vitamin K prophylaxis: newborns have minimal placental transfer, low stores "
    "and a sterile gut, so without the injection they risk hemorrhagic disease of the newborn.\n\n"
    "Educational objective: Vitamin K deficiency lowers factors II, VII, IX and X while leaving "
    "factor V normal; liver disease lowers factor V as well but spares factor VIII, and DIC consumes "
    "factor VIII along with fibrinogen and raises the D-dimer.",
    "Vitamin K is the tool the liver needs to finish four clotting proteins. Starving plus "
    "antibiotics wiped out his supply — but the proteins that don't need that tool, like factor five, "
    "are still normal, which is how you tell it apart from liver failure.",
    exim="fig_slide_dic_chart",
    excap="The acquired coagulopathies side by side — liver disease, vitamin K deficiency and "
          "disseminated intravascular coagulation.",
)

# ── 47. Thrombotic thrombocytopenic purpura (§32) ───────────────────────────────
q(
    "A 34-year-old woman is brought to the emergency department by her husband due to 2 days of "
    "confusion and slurred speech. She has had fatigue and bruising for a week. She takes no "
    "medications and has had no diarrhea. Temperature is 38.2 C (100.8 F). She is disoriented to "
    "time. There is no splenomegaly.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.9 g/dL (N=12.0–16.0 g/dL)\n"
    "Hematocrit 24% (N=36%–46%)\n"
    "Platelet count 12,000/mm3 (N=150,000–400,000/mm3)\n"
    "Reticulocyte count 7.4% (N=0.5%–1.5%)\n"
    "Lactate dehydrogenase 1,460 U/L (N=45–200 U/L)\n"
    "Haptoglobin less than 10 mg/dL (N=41–165 mg/dL)\n"
    "Creatinine 1.4 mg/dL (N=0.6–1.2 mg/dL)\n"
    "Prothrombin time 13 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 32 sec (N=25–40 sec)\n"
    "Fibrinogen 330 mg/dL (N=200–400 mg/dL)\n\n"
    "Direct antiglobulin test is negative. The peripheral smear is shown. Which of the following is "
    "the most likely mechanism of this patient's illness?",
    {
        "Antibodies against a heparin-platelet factor 4 complex":
            "Heparin-induced thrombocytopenia also drops platelets and causes thrombosis, but it "
            "requires heparin exposure 5–10 days earlier and produces large-vessel clots rather than "
            "a microangiopathic hemolytic anemia.",
        "Antibodies against platelet glycoprotein IIb/IIIa":
            "This is immune thrombocytopenia, which gives an ISOLATED low platelet count with a "
            "normal hemoglobin and no schistocytes.",
        "Autoantibody inhibition of ADAMTS13": "",
        "Complement dysregulation from a factor H defect":
            "Atypical hemolytic uremic syndrome produces the same triad but is kidney-dominant, "
            "often recurrent or familial, and is treated with complement blockade. Her creatinine is "
            "barely raised and her presentation is neurologic.",
        "Endothelial injury by a bacterial exotoxin":
            "Shiga toxin from enterohemorrhagic Escherichia coli causes typical hemolytic uremic "
            "syndrome — after bloody diarrhea, in a child, with renal failure dominating. She has had "
            "no diarrhea.",
        "Systemic activation of the coagulation cascade":
            "Disseminated intravascular coagulation also shreds red cells, but it consumes clotting "
            "factors: the PT and aPTT are prolonged and fibrinogen falls. Hers are all normal.",
    },
    "Autoantibody inhibition of ADAMTS13",
    "Thrombotic thrombocytopenic purpura (TTP). The mechanism is a failure to trim von Willebrand "
    "factor:\n\n"
    "Endothelial cells secrete von Willebrand factor as ULTRA-LARGE multimers → ADAMTS13 normally "
    "cleaves them to a safe size → in TTP the enzyme is absent (congenital Upshaw-Schulman) or, far "
    "more often, blocked by an acquired IgG inhibitor → uncleaved multimers act as adhesive ropes "
    "that seize platelets throughout the microvasculature → platelets are consumed (thrombocytopenia) "
    "and red cells are shredded on the strands (schistocytes, raised LDH, undetectable haptoglobin, "
    "reticulocytosis, negative antiglobulin test).\n\n"
    "The pentad is fever, thrombocytopenia, microangiopathic hemolytic anemia, neurologic change and "
    "renal impairment — but do NOT wait for all five. TTP is systemic and platelet-rich, so the brain "
    "is involved early; HUS is renal and fibrin-rich. The acquired autoimmune form typically presents "
    "in the 20s and 30s.\n\n"
    "The single most useful discriminator is the coagulation panel: in every thrombotic "
    "microangiopathy the PT, aPTT and fibrinogen are NORMAL, because clotting factors are not being "
    "consumed — the lesion is platelets and endothelium. In DIC they are deranged. The smear cannot "
    "make that distinction; the panel makes it in one look.\n\n"
    "Treatment is urgent plasma EXCHANGE, started on clinical suspicion before the ADAMTS13 result "
    "returns — it both replaces the enzyme and removes the antibody, where infusion alone would only "
    "do the first. Untreated mortality exceeds 90%. Do not transfuse platelets unless there is "
    "life-threatening bleeding: the thrombocytopenia is consumptive, and added platelets feed ongoing "
    "microvascular thrombosis.\n\n"
    "Educational objective: TTP results from ADAMTS13 deficiency or inhibition, leaving ultra-large "
    "von Willebrand factor multimers to consume platelets and shear red cells; it presents with "
    "neurologic changes and normal PT, aPTT and fibrinogen, which distinguishes it from DIC. "
    "Treatment is urgent plasma exchange, not platelet transfusion.",
    "An enzyme that normally trims sticky protein ropes in her blood has been switched off by an "
    "antibody. The untrimmed ropes catch platelets everywhere and slice red cells apart as they "
    "squeeze past.",
    image="fig_schistocytes",
    imcap="Peripheral blood smear. Among the intact erythrocytes there are several smaller angular "
          "cells with one straight or concave edge and a sharply pointed contour.",
    exim="fig_slide_adamts13",
    excap="Two routes to the same failure: congenital ADAMTS13 deficiency, or an acquired IgG "
          "inhibitor against the enzyme.",
)

# ── 48. Atypical hemolytic uremic syndrome (§32) ────────────────────────────────
q(
    "A 5-year-old girl is admitted to the hospital due to 3 days of decreasing urine output and "
    "pallor. She has had no diarrhea. She had a similar episode at age 3 that required dialysis, and "
    "a maternal cousin developed kidney failure in childhood. Blood pressure is 128/84 mm Hg.\n\n"
    "Laboratory studies show:\n"
    "Hemoglobin 7.2 g/dL (N=11.5–15.5 g/dL)\n"
    "Platelet count 46,000/mm3 (N=150,000–400,000/mm3)\n"
    "Creatinine 3.6 mg/dL (N=0.3–0.7 mg/dL)\n"
    "Lactate dehydrogenase 1,880 U/L (N=45–200 U/L)\n"
    "Prothrombin time 12 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 30 sec (N=25–40 sec)\n"
    "Complement C3 58 mg/dL (N=80–170 mg/dL)\n\n"
    "The smear shows numerous schistocytes. Stool culture and Shiga toxin testing are negative, and "
    "ADAMTS13 activity is 68% (N=greater than 50%). Which of the following is the most appropriate "
    "treatment?",
    {
        "Corticosteroids and intravenous immunoglobulin":
            "This is the treatment for immune thrombocytopenia, in which the platelet count is low in "
            "isolation with no hemolysis and no renal failure.",
        "Eculizumab": "",
        "Plasma exchange":
            "Plasma exchange is the emergency treatment of TTP, where ADAMTS13 activity is severely "
            "reduced — usually under 10%. Hers is normal, which excludes that diagnosis.",
        "Platelet transfusion":
            "Platelets are consumed in every thrombotic microangiopathy, so transfusing them feeds "
            "ongoing microvascular thrombosis and is reserved for life-threatening bleeding.",
        "Supportive care with dialysis alone":
            "This is correct management for typical Shiga toxin-associated hemolytic uremic syndrome "
            "after a diarrheal illness. Her stool studies are negative and the disease is recurrent "
            "and familial.",
    },
    "Eculizumab",
    "Atypical hemolytic uremic syndrome (aHUS) — a thrombotic microangiopathy driven by uncontrolled "
    "complement activation.\n\n"
    "Work the recognition algorithm. Schistocytes with thrombocytopenia and a normal PT, aPTT and "
    "fibrinogen puts her in the microangiopathy group rather than DIC. Then:\n"
    "• Bloody diarrheal prodrome with Shiga toxin → typical HUS → supportive care\n"
    "• Severely reduced ADAMTS13 → TTP → plasma exchange\n"
    "• Neither, especially if recurrent or familial with a low C3 → aHUS → complement blockade\n\n"
    "Mechanism: the alternative complement pathway is constitutively ticking over and is held in "
    "check by regulators — complement factor H, factor I, membrane cofactor protein (CD46) and "
    "thrombomodulin. Lose a regulator and the pathway runs unchecked: the membrane attack complex "
    "damages the patient's own endothelium, and injured endothelium exposes collagen and tissue "
    "factor, switching on coagulation. The consumed C3 is the laboratory footprint.\n\n"
    "Eculizumab is a monoclonal antibody against C5 that blocks terminal complement. Note the "
    "consequence of that mechanism: blocking terminal complement removes the exact defence against "
    "encapsulated organisms, so every complement inhibitor carries a boxed warning for "
    "life-threatening meningococcal infection and patients must be vaccinated against Neisseria "
    "meningitidis before starting — the same vulnerability as asplenia, arrived at pharmacologically.\n\n"
    "Genetics must be established before any kidney transplant: if the faulty regulator is a "
    "circulating protein made in the liver (factor H, factor I), a transplanted kidney meets the same "
    "unregulated complement and is attacked, whereas a defect in the membrane-bound renal regulator "
    "(CD46) is largely corrected by the graft itself.\n\n"
    "Educational objective: Atypical hemolytic uremic syndrome is caused by defective regulation of "
    "the alternative complement pathway and presents as a kidney-dominant thrombotic microangiopathy "
    "without diarrhea and with normal ADAMTS13 activity. It is treated with the anti-C5 antibody "
    "eculizumab, which requires meningococcal vaccination.",
    "A brake on part of her immune system is missing, so it keeps attacking the lining of her own "
    "blood vessels, especially in the kidneys. The drug clamps that pathway shut.",
    exim="fig_slide_ahus_complement",
    excap="Atypical HUS: loss of complement suppression leaves the alternative pathway continually "
          "active.",
)

# ── 49. Antithrombin deficiency and heparin resistance (§33) ────────────────────
q(
    "A 46-year-old man is admitted to the hospital due to left leg swelling and pain, and "
    "compression ultrasonography confirms a proximal deep vein thrombosis. He has nephrotic syndrome "
    "from membranous nephropathy, with 9 g of protein in a 24-hour urine collection and peripheral "
    "edema. Intravenous unfractionated heparin is started. Despite three dose increases over 24 "
    "hours, the activated partial thromboplastin time remains at 30–33 seconds (N=25–40 sec) and the "
    "anti-factor Xa level is below target. The infusion pump and line have been checked and the "
    "drug is being delivered. Which of the following best explains this patient's response to "
    "therapy?",
    {
        "Antibodies against heparin-platelet factor 4 complexes":
            "Heparin-induced thrombocytopenia appears 5–10 days after exposure, drops the platelet "
            "count by more than half and causes new thrombosis — it does not make the aPTT resistant "
            "to escalating doses on day one.",
        "A lupus anticoagulant interfering with the assay":
            "An antiphospholipid antibody PROLONGS the baseline aPTT rather than keeping it short, "
            "which is why an alternative assay is needed to monitor heparin in those patients.",
        "Resistance of factor V to activated protein C":
            "Factor V Leiden explains a tendency to clot, not a failure to respond to heparin — "
            "heparin acts through antithrombin, entirely downstream of protein C.",
        "Urinary loss of antithrombin": "",
        "Rapid hepatic clearance of unfractionated heparin":
            "Heparin is cleared by a saturable cellular mechanism and then renally, and clearance is "
            "not accelerated in nephrotic syndrome to a degree that produces this picture.",
    },
    "Urinary loss of antithrombin",
    "Acquired antithrombin deficiency causing heparin resistance.\n\n"
    "The key mechanistic fact is that heparin has essentially NO anticoagulant activity of its own. "
    "It works by binding antithrombin and accelerating it — a slow natural brake becomes a fast one. "
    "With little antithrombin present, more heparin achieves very little.\n\n"
    "Antithrombin is a small protein and is easily lost. Acquired causes: nephrotic syndrome (the "
    "glomerulus leaks it into the urine, as here — the same protein loss that makes nephrotic "
    "patients hypercoagulable in the first place), chest tube drainage, protein-losing enteropathy, "
    "severe heart failure, and consumption by an acute thrombosis itself. Inherited deficiency is "
    "rarer but carries a much higher risk per patient — the anticoagulant-protein deficiencies "
    "(antithrombin, protein C, protein S) run a relative risk of 15–19x, against 3–5x for factor V "
    "Leiden and prothrombin G20210A.\n\n"
    "The answer is not more heparin. Either supplement antithrombin so the heparin can work, or "
    "switch to an agent that does not depend on it — a direct thrombin inhibitor such as argatroban "
    "or bivalirudin.\n\n"
    "Note the testing caveat this also creates: heparin itself lowers antithrombin levels, so a level "
    "drawn during treatment cannot establish an inherited deficiency. Repeat it months later, off "
    "anticoagulation.\n\n"
    "Educational objective: Heparin acts by potentiating antithrombin, so antithrombin deficiency — "
    "commonly acquired through urinary loss in nephrotic syndrome — produces heparin resistance. "
    "Management is antithrombin replacement or a direct thrombin inhibitor, not escalating heparin "
    "doses.",
    "Heparin does not thin blood by itself — it supercharges a natural brake protein. His kidneys are "
    "leaking that brake protein into his urine, so there is almost nothing for the heparin to work "
    "with.",
    exim="fig_slide_anticoag_brakes",
    excap="The natural anticoagulants — antithrombin acting on thrombin and factor Xa, and activated "
          "protein C with protein S on factors Va and VIIIa.",
)

# ── 50. Thrombophilia testing in the acute setting (§34) ────────────────────────
q(
    "A 28-year-old woman is hospitalized due to a first deep vein thrombosis of the left leg, which "
    "developed 2 weeks after she started a combined oral contraceptive. She smokes half a pack of "
    "cigarettes daily. There is no family history of thrombosis. Intravenous heparin is started, "
    "and on hospital day 2 the admitting team sends a full thrombophilia panel. Results show an "
    "antithrombin activity of 52% (N=80%–120%), normal protein C and protein S activity, and "
    "heterozygous factor V Leiden. Which of the following is the most appropriate interpretation of "
    "the antithrombin result?",
    {
        "It confirms an inherited antithrombin deficiency":
            "That conclusion cannot be drawn from a level measured during an acute clot on heparin. "
            "Inherited deficiency is diagnosed on a repeat level months later, off anticoagulation, "
            "ideally with family testing.",
        "It explains the thrombosis better than factor V Leiden":
            "Anticoagulant-protein deficiencies do carry far higher risk than factor V Leiden "
            "(15–19x versus 3–5x) — but only if the level is real. An uninterpretable value explains "
            "nothing, and she already has two acquired triggers.",
        "It indicates consumption by disseminated intravascular coagulation":
            "DIC would lower fibrinogen, prolong the clotting times and raise the D-dimer far beyond "
            "what a single deep vein thrombosis produces. Nothing here suggests it.",
        "It is uninterpretable because of the heparin and the acute clot": "",
        "It is unreliable because she is taking an estrogen contraceptive":
            "Estrogen does alter several hemostatic proteins, but the dominant confounders in this "
            "specific result are the heparin infusion and consumption by the acute thrombosis.",
    },
    "It is uninterpretable because of the heparin and the acute clot",
    "Thrombophilia testing in the acute period is unreliable, and this panel illustrates most of the "
    "reasons.\n\n"
    "What confounds what:\n"
    "• HEPARIN lowers antithrombin levels\n"
    "• The THROMBOSIS itself consumes antithrombin, protein C and protein S\n"
    "• WARFARIN lowers protein C and protein S (both are vitamin K dependent)\n"
    "• ACUTE ILLNESS and inflammation raise factor VIII and fibrinogen\n"
    "• PREGNANCY alters multiple levels\n"
    "• A LUPUS ANTICOAGULANT may be transient, hence the 12-week repeat requirement\n\n"
    "Genetic testing is the exception: factor V Leiden and prothrombin G20210A can be run at any "
    "time, are unaffected by drugs or illness, and never need repeating. Everything else should wait "
    "several months and, if possible, be drawn off anticoagulation.\n\n"
    "The deeper point is whether to test at all. Some thrombophilia is present in roughly a quarter "
    "of the general population, so finding one does not establish causation. Duration of "
    "anticoagulation is set by the CIRCUMSTANCES of the clot — about 3% recurrence in the first year "
    "after a major transient risk factor, 5% after a minor reversible one (an oral contraceptive, a "
    "long flight), and 10% when unprovoked or with a persistent risk factor — not by the genotype. "
    "Here the estrogen contraceptive plus smoking is a reversible, and removable, explanation.\n\n"
    "Before sending any of these assays, finish the sentence: if positive I will do X, if negative I "
    "will do Y. If X and Y are the same, do not send the test.\n\n"
    "Educational objective: Antithrombin, protein C and protein S levels are unreliable during acute "
    "thrombosis and on anticoagulation, and should be repeated months later off therapy; only the "
    "genetic tests for factor V Leiden and prothrombin G20210A can be performed at any time. "
    "Duration of anticoagulation is determined by the circumstances of the clot rather than by a "
    "thrombophilia result.",
    "Testing for an inherited clotting problem in the middle of a clot, while on a blood thinner, "
    "gives numbers you cannot trust. The clot and the drug both use up the very protein being "
    "measured.",
    exim="fig_slide_thrombophilia_summary",
    excap="The thrombophilias on one diagram — lost brakes versus pushed accelerators.",
)

# ── 51. The lupus anticoagulant paradox (§33) ───────────────────────────────────
q(
    "A 31-year-old woman comes to the office for preconception counseling. She has had three "
    "consecutive spontaneous abortions at 7, 8 and 9 weeks' gestation, all with normal fetal "
    "karyotypes. Last year she had a left calf deep vein thrombosis with no identifiable trigger. "
    "She has never bled abnormally, including after a tonsillectomy. A rapid plasma reagin test "
    "performed during her first pregnancy was positive, but treponemal-specific testing was "
    "negative.\n\n"
    "Laboratory studies show:\n"
    "Platelet count 118,000/mm3 (N=150,000–400,000/mm3)\n"
    "Prothrombin time 13 sec (N=11–15 sec)\n"
    "Partial thromboplastin time 58 sec (N=25–40 sec)\n\n"
    "A 1:1 mix with normal plasma does not correct the partial thromboplastin time, but adding "
    "excess phospholipid does. Which of the following best explains the prolonged partial "
    "thromboplastin time?",
    {
        "An antibody bound to a clotting factor":
            "A specific factor inhibitor, such as an acquired anti-factor VIII antibody, also fails "
            "to correct on mixing — but it causes BLEEDING, and extra phospholipid does not correct "
            "it.",
        "An antibody competing for the assay's phospholipid": "",
        "Consumption of clotting factors by microthrombi":
            "Consumption would prolong the PT as well and lower fibrinogen. Her PT is normal.",
        "Deficiency of an intrinsic pathway factor":
            "A deficiency corrects on mixing, because normal plasma supplies the missing factor at "
            "about 50% — enough for hemostasis. Hers did not correct.",
        "Residual heparin in the collected sample":
            "Heparin contamination from a line draw is a real cause of an unexpected long aPTT that "
            "fails to correct, but it is excluded by the phospholipid correction and does not explain "
            "the obstetric history or the false-positive syphilis test.",
    },
    "An antibody competing for the assay's phospholipid",
    "Antiphospholipid syndrome — and the name is wrong on both counts. It is not lupus (most patients "
    "do not have it), and it is not an anticoagulant.\n\n"
    "The paradox and its resolution: clotting assays are run on a phospholipid surface. The antibody "
    "binds phospholipid, so IN THE TUBE it competes with the clotting complexes for a limited amount "
    "of surface and the reaction is slowed — a long aPTT. IN THE PATIENT phospholipid is not "
    "limiting; the antibodies instead activate endothelium and platelets and interfere with natural "
    "anticoagulant pathways, so the patient CLOTS.\n\n"
    "That mechanism hands you the diagnostic algorithm:\n"
    "1. Mixing study — does not correct, so this is an inhibitor rather than a deficiency\n"
    "2. A phospholipid-dependent assay — aPTT and/or the dilute Russell viper venom test, which is "
    "more specific\n"
    "3. Confirm with EXCESS PHOSPHOLIPID, which corrects the prolongation and proves the target is "
    "phospholipid rather than a factor\n"
    "4. Immunoassays — anti-cardiolipin and anti-beta-2-glycoprotein-1 IgG and IgM\n\n"
    "Her positive rapid plasma reagin with negative treponemal testing is the same mechanism in "
    "another guise: the non-treponemal syphilis tests use a cardiolipin antigen, so anti-cardiolipin "
    "antibodies produce a biological false positive.\n\n"
    "Diagnosis requires one clinical plus one laboratory criterion, and the laboratory finding must "
    "be PERSISTENT on repeat testing at least 12 weeks apart — transient antiphospholipid antibodies "
    "appear after infections and acute illness. She meets the clinical criterion twice over: vascular "
    "thrombosis, and three or more consecutive losses before the 10th week. Having the antibody "
    "without a clinical criterion is not the syndrome and is generally not anticoagulated.\n\n"
    "Educational objective: A lupus anticoagulant prolongs phospholipid-dependent clotting assays in "
    "vitro yet causes thrombosis in vivo; it fails to correct with normal plasma but corrects with "
    "excess phospholipid. Diagnosis of antiphospholipid syndrome requires a clinical event plus a "
    "persistent antibody 12 weeks apart.",
    "Her antibody sticks to the fatty surface the lab test needs to work, so the test runs slow and "
    "looks like she should bleed. Inside her body that same antibody makes her clot instead.",
    exim="fig_slide_aps_mixing",
    excap="The mixing study again: a factor deficiency corrects with normal plasma; antiphospholipid "
          "antibodies do not.",
)

# ── 52. Anticoagulant choice in antiphospholipid syndrome (§49) ─────────────────
q(
    "A 37-year-old man comes to the office to discuss long-term treatment after a segmental "
    "pulmonary embolism diagnosed 4 weeks ago. He was previously well, with no surgery, immobility "
    "or travel before the event, and he has a history of an unprovoked deep vein thrombosis at age "
    "33. Lupus anticoagulant testing and anti-beta-2-glycoprotein-1 antibodies were positive at the "
    "time of the embolism and again today, 12 weeks apart. Renal and hepatic function are normal. "
    "He asks to take a once-daily tablet that does not require monitoring. Which of the following is "
    "the most appropriate long-term anticoagulant for this patient?",
    {
        "Apixaban":
            "Apixaban is the usual first choice for most venous thromboembolism — twice daily, "
            "no monitoring, the least renal clearance and the lowest bleeding rates of the class. "
            "Antiphospholipid syndrome is the specific carve-out.",
        "Aspirin":
            "Aspirin blocks platelet thromboxane and is for arterial, platelet-rich 'white clots'. "
            "For extended prevention after venous thromboembolism it is markedly inferior to a "
            "low-dose direct oral anticoagulant and no safer.",
        "Dabigatran":
            "A direct thrombin inhibitor, and a direct oral anticoagulant — subject to the same "
            "evidence of harm in this syndrome. It also requires a parenteral lead-in when starting "
            "treatment for venous thromboembolism.",
        "Rivaroxaban":
            "Once-daily dosing is exactly what he is asking for, which makes this the surface read — "
            "but it is a factor Xa inhibitor, and the randomized evidence of harm applies to the "
            "class.",
        "Warfarin": "",
    },
    "Warfarin",
    "Antiphospholipid syndrome with recurrent unprovoked venous thromboembolism. He meets both "
    "criteria — a clinical thrombotic event, and a persistently positive antibody at least 12 weeks "
    "apart.\n\n"
    "The general rule since the 2021 CHEST guideline is to prefer a direct oral anticoagulant over "
    "warfarin: efficacy is equal, bleeding (especially intracranial) is lower, and no monitoring is "
    "needed. Antiphospholipid syndrome is the most important exception, because randomized trials "
    "showed HARM — more arterial thrombotic events — with direct oral anticoagulants compared with "
    "warfarin. Use warfarin, target INR 2.0–3.0, and since this is a second unprovoked event, "
    "treatment is long term.\n\n"
    "The other situations where a direct oral anticoagulant should not be used: pregnancy or "
    "breastfeeding (use a heparin); massive pulmonary embolism, phlegmasia cerulea dolens or "
    "iliofemoral thrombosis needing titration or thrombolysis; extremes of body weight; altered "
    "gastrointestinal anatomy such as gastric bypass; creatinine clearance below 30 mL/min (apixaban "
    "or warfarin instead); heparin-induced thrombocytopenia; splanchnic vein thrombosis; and major "
    "enzyme-inducing interactions.\n\n"
    "A monitoring note specific to this patient: the lupus anticoagulant can prolong the baseline "
    "clotting times and make the INR unreliable, so some patients require a chromogenic factor X "
    "assay to confirm the intensity of warfarin therapy.\n\n"
    "Educational objective: Direct oral anticoagulants are preferred over warfarin for most venous "
    "thromboembolism, but antiphospholipid syndrome is a carve-out with randomized evidence of harm; "
    "those patients require warfarin with a target INR of 2.0–3.0.",
    "Newer once-a-day blood thinners are usually the easy choice, but in this particular antibody "
    "disease studies showed more clots on them. He needs the older drug with regular blood tests.",
)

# ── 53. Heparin-induced thrombocytopenia (§34) ──────────────────────────────────
q(
    "A 64-year-old man is in the hospital on day 8 after elective hip arthroplasty. He has received "
    "subcutaneous unfractionated heparin for prophylaxis since surgery. He now reports a cold, "
    "painful right foot. His platelet count was 265,000/mm3 on admission and is 78,000/mm3 today. "
    "The right dorsalis pedis and posterior tibial pulses are absent, and the foot is mottled and "
    "cool. There is no bleeding at the surgical site and no petechiae. Prothrombin time, partial "
    "thromboplastin time and fibrinogen are normal, and the peripheral smear shows no schistocytes. "
    "Which of the following best explains this patient's findings?",
    {
        "Antibodies to heparin-platelet factor 4 complexes": "",
        "Autoantibody against platelet glycoprotein IIb/IIIa":
            "Immune thrombocytopenia causes bleeding, not arterial occlusion, and is not tied to day "
            "5–10 of a drug.",
        "Consumption of platelets and factors in systemic coagulation":
            "Disseminated intravascular coagulation prolongs the PT and aPTT, lowers fibrinogen and "
            "produces schistocytes. All are normal or absent here.",
        "Dilution of platelets by intravenous fluid administration":
            "Dilutional thrombocytopenia follows massive fluid or blood replacement and does not "
            "cause limb ischemia.",
        "Inhibition of ADAMTS13 by an acquired antibody":
            "TTP gives a microangiopathic hemolytic anemia with schistocytes and neurologic "
            "involvement, not an isolated cold pulseless foot.",
        "Splenic sequestration of circulating platelets":
            "Hypersplenism requires an enlarged spleen and usually affects more than one cell line; "
            "it does not cause thrombosis.",
    },
    "Antibodies to heparin-platelet factor 4 complexes",
    "Heparin-induced thrombocytopenia (HIT) with arterial thrombosis — and the counterintuitive core "
    "of the disease is that it is a CLOTTING emergency, not a bleeding one.\n\n"
    "Mechanism: heparin binds platelet factor 4 → the immune system takes 5–14 days to recognise "
    "that complex and make antibodies against it → the antibody binds and ACTIVATES platelets → "
    "platelets are consumed into new clots, so the count falls while the patient thromboses, venous "
    "to arterial roughly 4:1.\n\n"
    "Score it with the 4Ts: Thrombocytopenia (a fall of more than 50% with a nadir of 20–100 × 10⁹/L "
    "= 2), Timing (clear onset on days 5–10 = 2), Thrombosis (new thrombosis = 2), and oTher cause "
    "(none evident = 2) — a score of 8, high probability. At high probability you treat without "
    "waiting for the assay; at low probability you should not send it at all, because anti-PF4 "
    "antibodies are common in hospitalized patients and a false positive forces you to abandon "
    "heparin in someone who never had HIT.\n\n"
    "Management, and the three classic errors:\n"
    "• STOP all heparin, including flushes and heparin-bonded catheters, and START a non-heparin "
    "anticoagulant — argatroban (hepatically cleared, so usable in renal failure), bivalirudin or "
    "fondaparinux\n"
    "• Do NOT switch to low-molecular-weight heparin — the antibody cross-reacts\n"
    "• Do NOT start warfarin alone — it drops protein C first and can cause venous limb gangrene\n"
    "• Do NOT simply stop anticoagulation because the platelet count is low\n\n"
    "Educational objective: Heparin-induced thrombocytopenia is caused by antibodies against "
    "heparin-platelet factor 4 complexes that activate platelets, producing thrombosis 5–10 days "
    "after exposure despite a falling platelet count. Treatment is to stop all heparin and start a "
    "non-heparin anticoagulant such as argatroban; low-molecular-weight heparin and warfarin "
    "monotherapy are contraindicated.",
    "His immune system made antibodies against the heparin stuck to a platelet protein, and those "
    "antibodies switch platelets ON. The platelets get used up making clots, so the count drops even "
    "though the danger is clotting.",
    exim="fig_slide_hit",
    excap="Heparin-induced thrombocytopenia: heparin-platelet factor 4 complexes, antibody "
          "formation, and platelet activation.",
)

# ── 54. Duration of anticoagulation after a provoked clot (§34, §49) ────────────
q(
    "A 58-year-old woman comes to the office 11 weeks after a right leg deep vein thrombosis that "
    "occurred 6 days after an open hysterectomy, during which she was on bedrest for 4 days. She has "
    "taken apixaban since and has had no bleeding and no further symptoms. She has no personal or "
    "family history of thrombosis, no known malignancy, and takes no hormonal therapy. Age-"
    "appropriate cancer screening is up to date. She asks how long she needs to keep taking the "
    "medication. Which of the following is the most appropriate recommendation?",
    {
        "Complete 3 months of therapy and then stop": "",
        "Continue anticoagulation indefinitely":
            "Indefinite therapy is considered for a SECOND unprovoked event, or after an unprovoked "
            "event when recurrence risk and patient preference favour it. Her clot had a clear "
            "surgical trigger.",
        "Continue until thrombophilia testing is complete":
            "Testing is not indicated here — her clot is fully explained — and a positive result "
            "would not change the duration, which is set by the circumstances of the event.",
        "Stop anticoagulation and begin daily aspirin":
            "For extended prevention aspirin is markedly inferior to a low-dose direct oral "
            "anticoagulant and is not meaningfully safer. It is an option only when anticoagulation "
            "is unacceptable — and she needs no extended therapy at all.",
        "Stop now and place a retrievable vena cava filter":
            "The only confident indication for a filter is acute venous thromboembolism with an "
            "absolute contraindication to anticoagulation. Filters add thrombosis, migration and "
            "fracture risks and increase recurrent deep vein thrombosis.",
        "Switch to low-molecular-weight heparin for 3 more months":
            "Low-molecular-weight heparin for at least 3 months is the answer for cancer-associated "
            "thrombosis. She has no malignancy, and she has already completed her indicated course.",
    },
    "Complete 3 months of therapy and then stop",
    "A provoked venous thromboembolism. The duration decision is driven by the CIRCUMSTANCES of the "
    "clot, because that is what predicts recurrence:\n"
    "• Major transient risk factor (surgery, prolonged hospital bedrest) → about 3% recurrence in the "
    "first year\n"
    "• Minor reversible risk factor (oral contraceptive, a long flight) → about 5%\n"
    "• Unprovoked, or a persistent risk factor such as active cancer → about 10%\n\n"
    "Guideline durations: proximal deep vein thrombosis or pulmonary embolism from a transient risk "
    "factor, 3 months; a first unprovoked event, at least 3 months and then a decision to stop or "
    "continue long term; a second unprovoked event, long term; cancer-associated thrombosis, "
    "low-molecular-weight heparin for at least 3 months. Choosing Wisely states the provoked case "
    "plainly: do not treat beyond 3 months.\n\n"
    "Why the unprovoked case is genuinely close, by contrast: recurrence if you stop runs 5%–8% per "
    "year with a 4%–12% case fatality, while major bleeding if you continue runs 2%–6% per year. "
    "Fatal events per year are 0.3%–1% against 0.2%–0.6% — overlapping ranges, which is why the "
    "guidelines say 'suggest' rather than 'recommend' and why patient preference is decisive. And "
    "there is a middle option: AMPLIFY-EXTEND showed apixaban 2.5 mg twice daily gave the same "
    "reduction in recurrence as the full dose with bleeding indistinguishable from placebo.\n\n"
    "Educational objective: Venous thromboembolism provoked by a major transient risk factor such as "
    "surgery is treated for 3 months and then stopped, whereas unprovoked events require an "
    "individualized decision about extended therapy. Thrombophilia testing does not alter the "
    "duration.",
    "Her clot had an obvious cause — surgery and lying still — and that cause is gone. Three months "
    "of treatment is enough, and staying on a blood thinner longer would add bleeding risk for "
    "almost no benefit.",
    exim="fig_slide_risk_strat",
    excap="Risk stratification — recurrence risk tracks the circumstances of the clot far more than "
          "any inherited defect.",
)

# ── 55. Chronic thromboembolic pulmonary hypertension (§49) ─────────────────────
q(
    "A 52-year-old man comes to the office due to 5 months of progressive shortness of breath on "
    "exertion and two episodes of light-headedness while climbing stairs. Fourteen months ago he had "
    "a large bilateral pulmonary embolism with right ventricular strain on echocardiography; he "
    "completed 6 months of anticoagulation and stopped. He has never smoked. Blood pressure is "
    "124/78 mm Hg, pulse is 92/min, and oxygen saturation is 93% at rest, falling to 86% on walking. "
    "There is a loud pulmonary component of the second heart sound and mild pedal edema. Chest "
    "radiography shows clear lung fields, spirometry is normal, and brain natriuretic peptide is "
    "elevated. Echocardiography shows an estimated pulmonary artery systolic pressure of 62 mm Hg "
    "with a dilated right ventricle. Which of the following is the most appropriate next diagnostic "
    "test?",
    {
        "Bronchoscopy with bronchoalveolar lavage":
            "Useful for infection or diffuse parenchymal disease, neither of which fits clear lung "
            "fields with normal spirometry and isolated right heart failure.",
        "Coronary angiography":
            "Exertional dyspnea can be an anginal equivalent, but this patient has objective "
            "pulmonary hypertension with right ventricular dilation after a large embolism.",
        "High-resolution chest computed tomography":
            "This is the test for interstitial lung disease. His lung fields are clear and his "
            "spirometry is normal.",
        "Repeat D-dimer measurement":
            "A persistently elevated D-dimer after stopping anticoagulation predicts recurrence and "
            "feeds the duration decision, but it cannot diagnose chronic thromboembolic disease.",
        "Ventilation-perfusion scanning": "",
    },
    "Ventilation-perfusion scanning",
    "Chronic thromboembolic pulmonary hypertension (CTEPH) — unresolved organized thrombus in the "
    "pulmonary arteries causing progressive pulmonary hypertension and right heart failure.\n\n"
    "The setup is textbook: a large pulmonary embolism with right ventricular strain at presentation "
    "(the highest-risk group), then a symptom-free interval, then exertional dyspnea, exertional "
    "desaturation, a loud P2 and right-sided failure months later.\n\n"
    "The test to know is the VENTILATION-PERFUSION SCAN, not computed tomography angiography. "
    "V/Q scanning is the screening test of choice because chronic, organized, endothelialized "
    "thrombus can be missed on CT angiography while still producing unmatched perfusion defects. "
    "The workup triad is brain natriuretic peptide, echocardiography and a V/Q scan.\n\n"
    "If confirmed: indefinite anticoagulation, and referral for pulmonary thromboendarterectomy — "
    "which is potentially curative — with lung transplantation for refractory disease. Untreated, it "
    "progresses to cor pulmonale and death.\n\n"
    "The other long-term complication of venous thromboembolism, for contrast, is post-thrombotic "
    "syndrome: chronic limb swelling, pain, skin changes and ulceration from valve damage after a "
    "proximal deep vein thrombosis.\n\n"
    "Educational objective: New exertional dyspnea months after a pulmonary embolism suggests chronic "
    "thromboembolic pulmonary hypertension, evaluated with brain natriuretic peptide, "
    "echocardiography and a ventilation-perfusion scan — the screening test of choice, rather than "
    "computed tomography angiography. Treatment is indefinite anticoagulation plus referral for "
    "pulmonary thromboendarterectomy.",
    "Old clots in his lung arteries never fully dissolved and turned into scar, so his heart has to "
    "push much harder to get blood through. A lung scan that compares air flow with blood flow is "
    "the best way to see it.",
)

# ── 56. Normal lymph node architecture (§35) ────────────────────────────────────
q(
    "A 58-year-old man with a 4-year history of severe atopic dermatitis comes to the office due to "
    "enlarged axillary lymph nodes. He has no fever, night sweats or weight loss. Examination shows "
    "widespread excoriated, lichenified plaques and two mobile, nontender 2 cm axillary nodes. An "
    "excisional biopsy shows a node with an intact capsule and preserved follicles, in which the "
    "zone between the follicles is markedly expanded by small lymphocytes admixed with numerous pale "
    "cells having abundant cytoplasm and irregular nuclear contours, together with melanin-laden "
    "macrophages. The expanded compartment is normally populated predominantly by which of the "
    "following?",
    {
        "B lymphocytes":
            "B cells occupy the CORTEX, forming the primary and secondary follicles. Those follicles "
            "are described as preserved, which is exactly what tells you the expansion is elsewhere.",
        "Follicular dendritic cells":
            "These form the meshwork inside the germinal center light zone, supporting affinity "
            "selection of B cells. In Castleman disease they become the dominant follicular "
            "population, producing small atretic follicles.",
        "Histiocytes":
            "Histiocytes fill the subcapsular and medullary SINUSES. Massive expansion of that "
            "compartment is sinus histiocytosis or, in its neoplastic form, Rosai-Dorfman disease.",
        "Plasma cells":
            "Plasma cells populate the medullary cords near the hilum, and return to the bone marrow. "
            "Sheets of them between follicles characterize the plasma cell variant of Castleman "
            "disease.",
        "T lymphocytes": "",
    },
    "T lymphocytes",
    "Dermatopathic lymphadenopathy — the reactive node draining chronically inflamed skin — expanding "
    "the PARACORTEX, which is the T-cell zone.\n\n"
    "The lymph node floor plan, and the neoplasm that arises from each zone:\n"
    "• CORTEX — B cells in follicles. Primary follicles have no germinal center; secondary follicles "
    "do. Neoplasms: follicular lymphoma, Burkitt, many diffuse large B-cell lymphomas\n"
    "• PARACORTEX (interfollicular, deep cortex) — small T cells, plus histiocytes, dendritic cells "
    "and scattered immunoblasts, with the high endothelial venules through which lymphocytes enter. "
    "Neoplasms: peripheral T-cell lymphomas, mycosis fungoides\n"
    "• MEDULLA — medullary cords of plasma cells and lymphocytes alternating with sinuses\n"
    "• SINUSES — subcapsular and medullary, lined by histiocytes; the first place metastatic tumour "
    "lands, because lymph empties there first\n\n"
    "In dermatopathic change the paracortex fills with interdigitating dendritic cells (the pale "
    "cells with abundant cytoplasm) and melanin-laden macrophages carried from the inflamed skin. "
    "The clinical stake is real: in mycosis fungoides a dermatopathic node must be distinguished from "
    "true nodal involvement, because that distinction changes the stage.\n\n"
    "Development explains the map. Antigen-INDEPENDENT maturation happens in the marrow (B cells) and "
    "thymus (T cells) and gives rise to the precursor lymphoblastic neoplasms; antigen-DEPENDENT "
    "maturation happens here in the node after the naive cell meets antigen, and gives rise to the "
    "mature peripheral lymphomas.\n\n"
    "Educational objective: The lymph node cortex holds B cells in follicles, the paracortex holds T "
    "cells with dendritic cells and high endothelial venules, the medullary cords hold plasma cells, "
    "and the sinuses hold histiocytes. Paracortical expansion with dendritic cells and melanin-laden "
    "macrophages draining inflamed skin is dermatopathic lymphadenopathy.",
    "A lymph node has neighbourhoods: B cells in round balls near the edge, T cells in the zone "
    "between them. His swollen node is the T-cell zone reacting to years of angry skin.",
    exim="fig_slide_node_architecture",
    excap="The floor plan: afferent lymphatics enter at the capsule, the efferent lymphatic leaves "
          "at the hilum, and each zone holds one population.",
)

# ── 57. Follicular lymphoma versus reactive hyperplasia (§35) ───────────────────
q(
    "A 64-year-old man comes to the office due to 6 months of painless, progressive swelling of "
    "nodes in both sides of the neck, both axillae and both groins. He has no fever, night sweats or "
    "weight loss and feels well. Examination shows multiple rubbery, nontender nodes up to 3 cm and "
    "a spleen tip palpable below the costal margin. An excisional cervical node biopsy is shown; the "
    "follicles are closely apposed and of similar size, tingible body macrophages are absent, and "
    "mantle zones are attenuated. Which of the following immunohistochemical results is most likely "
    "in the follicle centers of this biopsy?",
    {
        "Cytokeratin-positive cohesive clusters":
            "Cytokeratin-positive cells in the subcapsular sinus indicate metastatic carcinoma, which "
            "arrives through the afferent lymphatics and lands there first.",
        "CD15 and CD30 positive large binucleate cells":
            "This is the Reed-Sternberg profile of classic Hodgkin lymphoma, which effaces the node "
            "with scattered large cells in a mixed inflammatory background rather than producing "
            "monotonous follicles.",
        "BCL2 positive follicle center cells": "",
        "Myeloperoxidase-positive crescentic histiocytes":
            "This is Kikuchi-Fujimoto disease, a necrotizing lymphadenitis without neutrophils, "
            "typically in a young woman with a tender cervical node.",
        "S100 positive histiocytes with emperipolesis":
            "Rosai-Dorfman disease expands the SINUSES with histiocytes containing intact "
            "lymphocytes, not the follicles.",
    },
    "BCL2 positive follicle center cells",
    "Follicular lymphoma. The architecture already gives it away, and BCL2 confirms it.\n\n"
    "Reactive follicular hyperplasia versus follicular lymphoma:\n"
    "• Follicle size and spacing — varied, separated by paracortex, versus MONOTONOUS and back-to-back\n"
    "• Tingible body macrophages — numerous, versus ABSENT\n"
    "• Polarization into dark and light zones — present, versus lost\n"
    "• Mantle zones — well defined, versus attenuated or absent\n"
    "• BCL2 in the germinal center — NEGATIVE, versus POSITIVE\n\n"
    "Why BCL2 is the discriminating stain, mechanistically rather than by rote: BCL2 is "
    "anti-apoptotic, and the entire purpose of a germinal center is somatic hypermutation followed by "
    "ruthless selection — B cells whose receptors got worse must die. Normal germinal center B cells "
    "therefore switch BCL2 OFF, which is precisely why tingible body macrophages have so much "
    "apoptotic debris to eat. Follicular lymphoma carries t(14;18), which places BCL2 under the "
    "immunoglobulin heavy chain promoter and forces it back on: the cells become unkillable and "
    "accumulate, and the tingible body macrophages disappear because nothing is dying.\n\n"
    "The clinical frame fits too — painless, widespread, slowly progressive lymphadenopathy in an "
    "older adult who feels well is the indolent lymphoma presentation, while the same histologic "
    "picture in a child with a sore throat would be reactive.\n\n"
    "Educational objective: Follicular lymphoma shows monotonous back-to-back follicles with absent "
    "tingible body macrophages, lost polarization and attenuated mantle zones, and its follicle "
    "center cells are BCL2 POSITIVE because of t(14;18); normal germinal center B cells are BCL2 "
    "negative so that failed clones can undergo apoptosis.",
    "Normal training centers inside a lymph node deliberately let failing cells die, and you can see "
    "the cleanup cells eating them. In this lymphoma a survival switch is jammed on, so nothing dies "
    "and the follicles crowd together.",
    image="fig_lpd_follicular_lymphoma_back_to_back",
    imcap="Lymph node at low power, hematoxylin and eosin: crowded, closely apposed follicles of "
          "similar size fill the section, with little intervening tissue and poorly defined "
          "surrounding cuffs.",
    exim="fig_reactive_gc",
    excap="A reactive germinal center for comparison — large centroblasts with pale tingible body "
          "macrophages scattered through it, and a well-defined mantle cuff.",
)

# ── 58. Infectious mononucleosis mimicking Hodgkin lymphoma (§35) ───────────────
q(
    "A 17-year-old boy comes to the office due to 10 days of sore throat, fever and profound "
    "fatigue. Examination shows a temperature of 38.6 C (101.5 F), tonsillar exudate, petechiae on "
    "the soft palate, tender posterior cervical and axillary lymphadenopathy, and a spleen tip "
    "palpable 2 cm below the left costal margin. Rapid streptococcal testing is negative. Leukocyte "
    "count is 14,200/mm3 with 58% lymphocytes, and more than 10% are large with abundant basophilic "
    "cytoplasm. A node is biopsied because of concern about lymphoma. The paracortex is shown; it is "
    "expanded and mottled, the underlying architecture is only partially effaced, and there are "
    "scattered very large cells with prominent nucleoli that stain strongly for CD30. Which of the "
    "following additional findings would most strongly argue against classic Hodgkin lymphoma?",
    {
        "CD15 expression by the large cells":
            "CD15 is positive in about 75% of classic Hodgkin lymphoma and co-expression with CD30 "
            "supports that diagnosis — the opposite of what the question asks.",
        "CD20 expression by the large cells": "",
        "Detection of Epstein-Barr virus in the node":
            "Epstein-Barr virus is the CAUSE of mononucleosis and is also found in a substantial "
            "proportion of classic Hodgkin lymphoma, so its presence cannot separate them.",
        "Numerous eosinophils in the background":
            "A mixed background of eosinophils, plasma cells and histiocytes is characteristic of "
            "classic Hodgkin lymphoma, particularly the mixed cellularity subtype.",
        "Prominent sclerotic bands within the node":
            "Collagen bands dividing the node into nodules define nodular sclerosis classic Hodgkin "
            "lymphoma.",
        "Weak PAX5 staining relative to background B cells":
            "Reed-Sternberg cells characteristically show WEAK PAX5 compared with surrounding normal "
            "B cells — a feature of Hodgkin lymphoma, not against it.",
    },
    "CD20 expression by the large cells",
    "Infectious mononucleosis — the most dangerous benign mimic of classic Hodgkin lymphoma. "
    "Epstein-Barr virus infects B cells and provokes a massive reactive T-cell response, generating "
    "large atypical immunoblasts that can be CD30 positive: exactly the Hodgkin profile.\n\n"
    "The resolving sentence: the Reed-Sternberg-LIKE cells of mononucleosis RETAIN their B-cell "
    "program; the Reed-Sternberg cells of classic Hodgkin lymphoma have LOST theirs. So CD20 and "
    "OCT2 are positive in mononucleosis and negative (or inconsistent) in Hodgkin lymphoma, while "
    "PAX5 stays at normal intensity here but is weak there.\n\n"
    "Everything else is shared and therefore cannot decide the case — large cells in a mixed "
    "background, CD30 expression (an activation marker, not a lymphoma marker) and Epstein-Barr "
    "virus positivity. Using CD30 alone to call Hodgkin lymphoma in a mononucleosis node is one of "
    "the classic catastrophic errors in hematopathology.\n\n"
    "The architecture supports the benign reading as well: mononucleosis leaves the node intact or "
    "only partially effaced, with paracortical hyperplasia (the mottled low-power look from pale "
    "immunoblasts and dendritic cells), follicular hyperplasia and sinus histiocytosis together. "
    "Clinically, fever, pharyngitis and cervical lymphadenopathy occur in more than half, with "
    "splenomegaly, profound fatigue, and a lymphocytosis containing more than 10% atypical "
    "lymphocytes.\n\n"
    "Educational objective: The large atypical cells of infectious mononucleosis can be CD30 positive "
    "and Epstein-Barr virus positive like Reed-Sternberg cells, but they retain the B-cell program — "
    "CD20 and OCT2 positive with normal PAX5 intensity — which distinguishes reactive "
    "mononucleosis from classic Hodgkin lymphoma.",
    "A common teenage virus can make lymph node cells look scarily like cancer. The giveaway is that "
    "these cells still carry their normal B-cell badges; the cancer cells have thrown theirs away.",
    image="fig_mono_mottling",
    imcap="Lymph node paracortex at medium power, hematoxylin and eosin. A dense population of small "
          "dark lymphocytes is interrupted by irregular paler patches containing larger cells with "
          "more abundant cytoplasm, giving a mottled appearance; a residual follicle is present at "
          "the left edge.",
    exim="fig_slide_im_vs_hodgkin",
    excap="Infectious mononucleosis versus classic Hodgkin lymphoma versus large B-cell lymphoma, "
          "side by side.",
)

# ── 59. Kikuchi-Fujimoto disease (§35) ──────────────────────────────────────────
q(
    "A 26-year-old woman comes to the office due to 3 weeks of fever to 38.9 C (102.0 F), night "
    "sweats, fatigue and a tender lump on the left side of her neck. She has lost 2.3 kg (5 lb). Ten "
    "days of doxycycline produced no improvement. She has no pets, no recent travel and no sick "
    "contacts. Examination shows a tender, mobile 3 cm left posterior cervical node. Leukocyte count "
    "is 2,800/mm3 with neutropenia and lymphopenia, hemoglobin is 10.5 g/dL (N=12.0–16.0 g/dL), "
    "platelet count is normal, and erythrocyte sedimentation rate is elevated. Antinuclear antibody "
    "is negative and infectious serologies are negative. Excisional biopsy is shown: patchy "
    "eosinophilic necrosis with abundant karyorrhectic debris, surrounded by histiocytes with "
    "crescent-shaped nuclei that stain for CD68 and myeloperoxidase. Neutrophils are absent, and "
    "there is no monoclonal population. Which of the following is the most likely diagnosis?",
    {
        "Cat scratch disease":
            "Bartonella lymphadenitis produces STELLATE suppurative granulomas packed with "
            "neutrophils, follows a cat or kitten exposure, and is confirmed by serology, PCR or a "
            "Warthin-Starry silver stain.",
        "Classic Hodgkin lymphoma":
            "Hodgkin nodes can necrose, so Reed-Sternberg cells must always be hunted at the edge of "
            "a necrotic zone — but they are absent here, and the atypical cells are histiocytes "
            "(CD68 and myeloperoxidase positive) rather than lymphoid.",
        "Kikuchi-Fujimoto disease": "",
        "Lupus lymphadenitis":
            "The closest mimic — also necrotizing and also neutrophil-poor — but it classically shows "
            "hematoxylin bodies and abundant plasma cells, and her antinuclear antibody is negative.",
        "Mycobacterial lymphadenitis":
            "Tuberculous nodes show NECROTIZING GRANULOMAS with epithelioid histiocytes and giant "
            "cells, and acid-fast organisms stain red on the appropriate stain. There are no "
            "granulomas here.",
    },
    "Kikuchi-Fujimoto disease",
    "Kikuchi-Fujimoto disease — a benign, self-limited necrotizing lymphadenitis that at high power "
    "can be mistaken for a high-grade lymphoma.\n\n"
    "The clinical profile is the stem: a young woman, more common in Asian populations, with a "
    "tender unilateral cervical node (often posterior), fever, night sweats and weight loss that read "
    "like B symptoms, cytopenias, and no response to antibiotics. That combination makes lymphoma the "
    "clinical worry, which is exactly why the diagnosis matters — the alternative diagnoses lead to "
    "chemotherapy, while this resolves on its own.\n\n"
    "The pathology has two features that save you:\n"
    "• ABSENCE OF NEUTROPHILS (and of eosinophils), which separates it from suppurative infectious "
    "causes such as cat scratch disease\n"
    "• Crescent-shaped (C-shaped) histiocyte nuclei that are CD68 and MYELOPEROXIDASE positive — and "
    "non-phagocytic\n\n"
    "Add partially preserved architecture, eosinophilic necrosis with abundant apoptotic debris, CD8 "
    "T-cell predominance, very few B cells and no monoclonality. Three phases are described: "
    "proliferative, necrotizing (the one to recognise), and xanthomatous.\n\n"
    "A departmental habit worth carrying: when a node shows necrosis, order acid-fast and Grocott "
    "methenamine silver stains for mycobacteria and fungi — and look for Reed-Sternberg cells at the "
    "edge of the necrosis before settling on an infectious or reactive cause. Also check lupus "
    "serology, because lupus lymphadenitis is the closest mimic.\n\n"
    "Educational objective: Kikuchi-Fujimoto disease is a self-limited necrotizing lymphadenitis of "
    "young adults showing patchy necrosis with abundant karyorrhectic debris, crescentic CD68 and "
    "myeloperoxidase-positive histiocytes, and a conspicuous ABSENCE of neutrophils. Its mimics are "
    "lupus lymphadenitis, suppurative lymphadenitis and lymphoma.",
    "Her lymph node has patches of dead tissue full of cell debris, but with none of the pus cells "
    "you would expect from an infection. It looks frightening under the microscope and gets better "
    "on its own.",
    image="fig_kikuchi_highpower",
    imcap="Excised lymph node. At low power (left) irregular pale pink zones replace much of the "
          "darker lymphoid tissue. At high power (right) those zones contain granular eosinophilic "
          "material studded with abundant dark nuclear fragments, with scattered histiocytes whose "
          "nuclei are indented into crescents; no neutrophils are present.",
    exim="fig_slide_kikuchi",
    excap="The Kikuchi-Fujimoto checklist — clinical profile, morphology and immunophenotype.",
)

# ── 60. Rosai-Dorfman disease and emperipolesis (§35) ───────────────────────────
q(
    "A 22-year-old man comes to the office due to 4 months of painless, massive enlargement of the "
    "lymph nodes on both sides of his neck. He has intermittent low-grade fever. Examination shows "
    "bilateral matted cervical nodes measuring up to 8 cm. Studies show a normocytic "
    "anemia, an elevated erythrocyte sedimentation rate and polyclonal hypergammaglobulinemia. An "
    "excisional biopsy shows markedly expanded lymph node sinuses filled with large histiocytes "
    "having abundant pale cytoplasm, many containing intact lymphocytes and plasma cells within "
    "clear spaces in their cytoplasm, together with numerous background plasma cells. The "
    "histiocytes are shown. They stain strongly for S100 and CD68. Which of the following additional "
    "findings would best exclude Langerhans cell histiocytosis?",
    {
        "Absent CD1a and CD207 staining": "",
        "Absent cytokeratin staining":
            "Cytokeratin negativity excludes metastatic carcinoma, the other lesion that fills "
            "sinuses with large cohesive cells — but Langerhans cells are not epithelial either, so "
            "this does not separate them.",
        "Positive CD68 staining":
            "CD68 marks histiocytes generally and is expressed by both entities, so it cannot "
            "distinguish them.",
        "Positive S100 staining":
            "This is the trap: Langerhans cell histiocytosis is ALSO S100 positive, which is exactly "
            "why S100 alone cannot resolve the differential.",
        "Positive SOX10 staining":
            "SOX10 positivity would point toward melanoma, another S100-positive lesion that can fill "
            "a sinus — its presence would argue for melanoma rather than against Langerhans cell "
            "histiocytosis.",
    },
    "Absent CD1a and CD207 staining",
    "Rosai-Dorfman disease — sinus histiocytosis with massive lymphadenopathy, now recognised as a "
    "histiocytic neoplasm.\n\n"
    "The defining morphology is EMPERIPOLESIS: intact, viable lymphocytes and plasma cells passing "
    "THROUGH the histiocyte cytoplasm without being digested, seen as cells sitting in clear halos. "
    "Contrast hemophagocytosis, where the histiocyte contains debris, apoptotic bodies and "
    "degenerated cells that ARE being destroyed — the finding that supplies one of the eight criteria "
    "for hemophagocytic lymphohistiocytosis.\n\n"
    "S100 in this disease is elegant: it stains the neoplastic histiocyte but NOT the engulfed "
    "lymphocytes, so the engulfed cells appear as clear unstained holes inside a brown cell — the "
    "stain highlights emperipolesis and supplies its own internal negative control.\n\n"
    "Because Langerhans cell histiocytosis is also S100 positive, the discriminating markers are "
    "CD1a and CD207 (langerin): POSITIVE in Langerhans cell histiocytosis, NEGATIVE in "
    "Rosai-Dorfman disease. Langerhans cell histiocytosis also shows grooved 'coffee-bean' nuclei "
    "and background eosinophils rather than emperipolesis. Melanoma is the third S100-positive sinus "
    "mimic and is SOX10 positive with CD68 negative.\n\n"
    "Full phenotype: S100+, CD68+, CD163+, cyclin D1+, OCT2+, CD1a−, CD207−. Nodal disease occurs in "
    "50%–60% and extranodal sites in 30%–40%, including skin and central nervous system. MAP kinase "
    "pathway mutations are found in about a third, which makes MEK inhibition a targeted option; "
    "spontaneous regression occurs, so observation is often appropriate.\n\n"
    "Educational objective: Rosai-Dorfman disease expands lymph node sinuses with S100-positive "
    "histiocytes showing emperipolesis — intact lymphocytes passing through the cytoplasm. Langerhans "
    "cell histiocytosis is also S100 positive, so CD1a and CD207 negativity is what excludes it.",
    "Big scavenger cells in his lymph nodes have swallowed whole living lymphocytes that are simply "
    "passing through unharmed. A different disease with similar-looking cells carries two extra "
    "markers, and his cells do not have them.",
    image="fig_rosai_emperipolesis",
    imcap="Lymph node sinus at high power, hematoxylin and eosin. Large cells with abundant pale "
          "cytoplasm and round vesicular nuclei fill the field; several contain clusters of intact "
          "small dark lymphocytes sitting within clear spaces inside the cytoplasm, and occasional "
          "red cells are present within them.",
    exim="fig_slide_sinus_pattern",
    excap="The sinus pattern and its differential — reactive histiocytosis, Rosai-Dorfman disease, "
          "metastasis and anaplastic large cell lymphoma.",
)
