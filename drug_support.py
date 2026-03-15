THERAPEUTIC_AREAS = {
    "Pain / Fever": "pain_fever",
    "Allergic Rhinitis": "allergic_rhinitis",
    "Acid Reflux / Dyspepsia": "acid_reflux",
    "Nausea / Vomiting": "nausea_vomiting",
    "Cough / Cold Symptoms": "cough_cold",
    "Hypertension": "hypertension",
    "Type 2 Diabetes": "type2_diabetes",
    "Anxiety / Insomnia": "anxiety_insomnia",
    "Depression": "depression",
    "Asthma / COPD": "asthma_copd",
    "Constipation": "constipation",
    "Urinary Symptoms / BPH": "urinary_bph",
    "Anticoagulation": "anticoagulation",
}


DRUG_CATALOG = {
    "pain_fever": [
        {
            "name": "Acetaminophen",
            "class": "Analgesic / antipyretic",
            "summary": "Often considered when NSAIDs are undesirable for pain or fever.",
            "avoid_terms": ["liver disease", "cirrhosis", "heavy alcohol", "alcohol use disorder"],
            "caution_terms": ["malnutrition"],
            "practice_note": "Review total daily dose and combination products before recommending.",
        },
        {
            "name": "Topical Diclofenac",
            "class": "Topical NSAID",
            "summary": "Useful for localized musculoskeletal pain when a topical option is reasonable.",
            "avoid_terms": ["nsaid allergy", "aspirin allergy", "third trimester", "pregnant 3rd trimester"],
            "caution_terms": ["gi bleed", "ckd", "kidney disease", "anticoagulant"],
            "practice_note": "Lower systemic exposure than oral NSAIDs, but interaction and bleeding risk still matters.",
        },
        {
            "name": "Celecoxib",
            "class": "COX-2 selective NSAID",
            "summary": "May be discussed when anti-inflammatory benefit is needed and GI risk profile matters.",
            "avoid_terms": ["sulfa allergy", "cabg", "heart failure", "third trimester"],
            "caution_terms": ["hypertension", "ckd", "kidney disease", "anticoagulant"],
            "practice_note": "Assess cardiovascular, renal, and bleeding risk before use.",
        },
    ],
    "allergic_rhinitis": [
        {
            "name": "Cetirizine",
            "class": "Second-generation antihistamine",
            "summary": "Common option for allergic rhinitis with relatively low sedation in many patients.",
            "avoid_terms": [],
            "caution_terms": ["elderly", "older adult", "renal impairment", "ckd"],
            "practice_note": "Dose adjustment may be needed in renal impairment.",
        },
        {
            "name": "Fexofenadine",
            "class": "Second-generation antihistamine",
            "summary": "Often chosen when minimal sedation is preferred.",
            "avoid_terms": [],
            "caution_terms": ["renal impairment", "ckd"],
            "practice_note": "Separate from aluminum or magnesium antacids when relevant.",
        },
        {
            "name": "Fluticasone Nasal Spray",
            "class": "Intranasal corticosteroid",
            "summary": "Helpful when congestion and nasal inflammation are prominent.",
            "avoid_terms": ["recent nasal surgery"],
            "caution_terms": ["glaucoma", "recurrent nosebleeds"],
            "practice_note": "Technique and local adverse effects should be reviewed.",
        },
    ],
    "acid_reflux": [
        {
            "name": "Famotidine",
            "class": "H2 blocker",
            "summary": "May be considered when a simpler acid suppression option is appropriate.",
            "avoid_terms": [],
            "caution_terms": ["renal impairment", "ckd", "older adult"],
            "practice_note": "Renal dosing may be required.",
        },
        {
            "name": "Omeprazole",
            "class": "Proton pump inhibitor",
            "summary": "Reasonable discussion option for stronger acid suppression when symptom pattern fits.",
            "avoid_terms": [],
            "caution_terms": ["osteoporosis", "c diff", "clostridioides difficile", "hypomagnesemia"],
            "practice_note": "Long-term use should be periodically reassessed.",
        },
        {
            "name": "Alginate Antacid",
            "class": "Barrier-forming antacid",
            "summary": "May help post-meal reflux symptoms as a non-PPI option.",
            "avoid_terms": ["bowel obstruction"],
            "caution_terms": ["heart failure", "sodium restriction", "ckd"],
            "practice_note": "Check sodium load and formulation details.",
        },
    ],
    "nausea_vomiting": [
        {
            "name": "Ondansetron",
            "class": "5-HT3 antagonist",
            "summary": "Frequently used option when nausea control is needed.",
            "avoid_terms": ["long qt", "qt prolongation"],
            "caution_terms": ["constipation", "serotonergic drugs", "arrhythmia"],
            "practice_note": "Consider ECG and interaction review in higher-risk patients.",
        },
        {
            "name": "Metoclopramide",
            "class": "Prokinetic / dopamine antagonist",
            "summary": "May be relevant when gastroparesis or migraine-associated nausea is suspected.",
            "avoid_terms": ["parkinson", "bowel obstruction", "seizure disorder"],
            "caution_terms": ["elderly", "older adult", "renal impairment"],
            "practice_note": "Extrapyramidal effects and duration limits matter.",
        },
        {
            "name": "Doxylamine-Pyridoxine",
            "class": "Antihistamine plus vitamin B6",
            "summary": "Common discussion option for pregnancy-associated nausea.",
            "avoid_terms": [],
            "caution_terms": ["glaucoma", "urinary retention", "older adult"],
            "practice_note": "Sedation and anticholinergic burden should be reviewed.",
        },
    ],
    "cough_cold": [
        {
            "name": "Dextromethorphan",
            "class": "Antitussive",
            "summary": "May be considered for dry cough symptom relief.",
            "avoid_terms": ["mao inhibitor"],
            "caution_terms": ["serotonergic drugs", "ssri", "snri"],
            "practice_note": "Interaction review matters because serotonergic combinations can be risky.",
        },
        {
            "name": "Guaifenesin",
            "class": "Expectorant",
            "summary": "Common option when mucus clearance is the main concern.",
            "avoid_terms": [],
            "caution_terms": [],
            "practice_note": "Encourage hydration if clinically appropriate.",
        },
        {
            "name": "Saline Nasal Spray",
            "class": "Non-drug supportive therapy",
            "summary": "Useful low-risk option for congestion and nasal dryness.",
            "avoid_terms": [],
            "caution_terms": [],
            "practice_note": "Helpful supportive option when medication burden should stay low.",
        },
        {
            "name": "Ipratropium Nasal Spray",
            "class": "Anticholinergic nasal spray",
            "summary": "May be considered for rhinorrhoea-predominant cold symptoms.",
            "avoid_terms": [],
            "caution_terms": ["glaucoma", "urinary retention", "bph"],
            "practice_note": "Avoid inadvertent eye contact; review with urological or ophthalmic concerns.",
        },
    ],

    # ─── Hypertension ────────────────────────────────────────────────────────────
    "hypertension": [
        {
            "name": "Amlodipine",
            "class": "Dihydropyridine calcium channel blocker",
            "summary": "Widely used first-line antihypertensive with a broad safety profile.",
            "avoid_terms": ["heart failure with reduced ejection fraction"],
            "caution_terms": ["elderly", "liver disease", "cirrhosis"],
            "practice_note": "Ankle oedema is common; dose reduction may be needed in significant hepatic impairment.",
        },
        {
            "name": "Ramipril",
            "class": "ACE inhibitor",
            "summary": "First-line option in hypertension, especially with co-existing diabetes or proteinuria.",
            "avoid_terms": ["ace inhibitor allergy", "angioedema history", "pregnant", "bilateral renal artery stenosis"],
            "caution_terms": ["ckd", "renal impairment", "anticoagulant"],
            "practice_note": "Monitor potassium and creatinine after initiation and dose changes.",
        },
        {
            "name": "Losartan",
            "class": "Angiotensin II receptor blocker (ARB)",
            "summary": "Alternative to ACE inhibitors; useful when ACE inhibitor cough is problematic.",
            "avoid_terms": ["pregnant", "bilateral renal artery stenosis"],
            "caution_terms": ["ckd", "renal impairment", "liver disease"],
            "practice_note": "Does not typically cause dry cough; monitor renal function and potassium.",
        },
        {
            "name": "Indapamide",
            "class": "Thiazide-like diuretic",
            "summary": "Effective antihypertensive with a more favourable metabolic profile than older thiazides.",
            "avoid_terms": ["sulfa allergy", "gout"],
            "caution_terms": ["elderly", "diabetes", "ckd"],
            "practice_note": "Monitor electrolytes; hyperuricaemia and glucose effects are possible.",
        },
        {
            "name": "Bisoprolol",
            "class": "Cardioselective beta-blocker",
            "summary": "Useful when co-existing heart failure or rate control is also indicated.",
            "avoid_terms": ["asthma", "copd", "severe bradycardia"],
            "caution_terms": ["diabetes", "peripheral vascular disease", "elderly"],
            "practice_note": "Never stop abruptly; titrate down gradually to avoid rebound effects.",
        },
    ],

    # ─── Type 2 Diabetes ─────────────────────────────────────────────────────────
    "type2_diabetes": [
        {
            "name": "Metformin",
            "class": "Biguanide",
            "summary": "First-line oral agent for type 2 diabetes when tolerated.",
            "avoid_terms": ["severe renal impairment", "liver disease", "cirrhosis", "acute heart failure"],
            "caution_terms": ["ckd", "renal impairment", "elderly", "alcohol use disorder"],
            "practice_note": "Check eGFR regularly; use extended-release formulation to reduce GI intolerance.",
        },
        {
            "name": "Empagliflozin",
            "class": "SGLT2 inhibitor",
            "summary": "Glucose lowering with established cardiovascular and renal protective benefits.",
            "avoid_terms": ["type 1 diabetes", "dka history", "recurrent utis"],
            "caution_terms": ["ckd", "elderly", "diuretic use", "foot ulcers"],
            "practice_note": "Hold perioperatively and during acute illness; educate on DKA symptoms.",
        },
        {
            "name": "Sitagliptin",
            "class": "DPP-4 inhibitor",
            "summary": "Well-tolerated option with a low intrinsic hypoglycaemia risk.",
            "avoid_terms": [],
            "caution_terms": ["ckd", "renal impairment", "heart failure", "pancreatitis history"],
            "practice_note": "Dose reduce in renal impairment; monitor for pancreatitis symptoms.",
        },
        {
            "name": "Gliclazide MR",
            "class": "Sulphonylurea",
            "summary": "Effective when cost or access to newer agents is a barrier; lower hypoglycaemia risk than older sulphonylureas.",
            "avoid_terms": ["sulfa allergy", "type 1 diabetes", "liver disease"],
            "caution_terms": ["elderly", "renal impairment"],
            "practice_note": "Hypoglycaemia risk; counsel patient on timing and meal regularity.",
        },
        {
            "name": "Liraglutide",
            "class": "GLP-1 receptor agonist",
            "summary": "Offers weight benefit alongside glucose lowering; cardiovascular outcome data available.",
            "avoid_terms": ["pancreatitis history"],
            "caution_terms": ["heart failure", "renal impairment", "elderly"],
            "practice_note": "Injectable; titrate slowly to minimise GI side effects.",
        },
    ],

    # ─── Anxiety / Insomnia ──────────────────────────────────────────────────────
    "anxiety_insomnia": [
        {
            "name": "Sertraline",
            "class": "SSRI",
            "summary": "Evidence-based first-line treatment for generalised anxiety disorder and panic disorder.",
            "avoid_terms": ["mao inhibitor"],
            "caution_terms": ["elderly", "gi bleed", "anticoagulant", "bipolar disorder"],
            "practice_note": "Anxiety may transiently worsen in early weeks; start low and titrate slowly.",
        },
        {
            "name": "Buspirone",
            "class": "Azapirone anxiolytic",
            "summary": "Non-benzodiazepine option for generalised anxiety without sedation or dependence risk.",
            "avoid_terms": ["mao inhibitor"],
            "caution_terms": ["liver disease", "renal impairment"],
            "practice_note": "Takes 2–4 weeks for full effect; not effective for acute panic episodes.",
        },
        {
            "name": "Hydroxyzine",
            "class": "Antihistamine anxiolytic",
            "summary": "May be considered for short-term or situational anxiety.",
            "avoid_terms": ["long qt", "pregnant"],
            "caution_terms": ["elderly", "glaucoma", "urinary retention", "bph"],
            "practice_note": "Sedation is notable; avoid combining with other CNS depressants or anticholinergics.",
        },
        {
            "name": "Melatonin",
            "class": "Melatonin receptor agonist",
            "summary": "Low-risk option for sleep onset difficulties and circadian disruption.",
            "avoid_terms": [],
            "caution_terms": ["liver disease", "anticoagulant"],
            "practice_note": "Take 30–60 minutes before target sleep time; not a sedative-hypnotic.",
        },
        {
            "name": "Zolpidem",
            "class": "Z-drug (non-benzodiazepine hypnotic)",
            "summary": "Short-term insomnia option when non-pharmacological measures have failed.",
            "avoid_terms": ["respiratory failure", "sleep apnoea"],
            "caution_terms": ["elderly", "liver disease", "depression", "alcohol use disorder"],
            "practice_note": "Use lowest effective dose for shortest duration; dependence and complex sleep behaviour risk.",
        },
    ],

    # ─── Depression ──────────────────────────────────────────────────────────────
    "depression": [
        {
            "name": "Sertraline",
            "class": "SSRI",
            "summary": "Commonly used first-line antidepressant with a broad evidence base.",
            "avoid_terms": ["mao inhibitor"],
            "caution_terms": ["elderly", "gi bleed", "anticoagulant", "bipolar disorder"],
            "practice_note": "Monitor for suicidality in early treatment, especially in younger patients.",
        },
        {
            "name": "Escitalopram",
            "class": "SSRI",
            "summary": "Well-tolerated SSRI with a relatively clean interaction profile.",
            "avoid_terms": ["mao inhibitor", "long qt"],
            "caution_terms": ["elderly", "liver disease"],
            "practice_note": "QTc prolongation risk at higher doses; ECG review relevant in cardiac patients.",
        },
        {
            "name": "Mirtazapine",
            "class": "NaSSA",
            "summary": "Useful when sedation, appetite stimulation, or sleep improvement is also a treatment goal.",
            "avoid_terms": ["mao inhibitor"],
            "caution_terms": ["elderly", "obesity", "diabetes", "liver disease"],
            "practice_note": "Weight gain is significant; monitor metabolic parameters.",
        },
        {
            "name": "Venlafaxine",
            "class": "SNRI",
            "summary": "Effective for depression and anxiety; additional noradrenergic benefit at higher doses.",
            "avoid_terms": ["mao inhibitor", "uncontrolled hypertension"],
            "caution_terms": ["hypertension", "heart disease", "elderly", "gi bleed", "anticoagulant"],
            "practice_note": "Blood pressure monitoring required; discontinue gradually to avoid withdrawal.",
        },
        {
            "name": "Bupropion",
            "class": "NDRI",
            "summary": "Antidepressant with weight-neutral or weight-reducing profile; also used for smoking cessation.",
            "avoid_terms": ["seizure disorder", "eating disorder", "mao inhibitor"],
            "caution_terms": ["bipolar disorder", "hypertension", "elderly"],
            "practice_note": "Absolute contraindication in seizure and eating disorders as it lowers seizure threshold.",
        },
    ],

    # ─── Asthma / COPD ───────────────────────────────────────────────────────────
    "asthma_copd": [
        {
            "name": "Salbutamol Inhaler (SABA)",
            "class": "Short-acting beta-2 agonist",
            "summary": "Reliever inhaler for acute bronchospasm in asthma and COPD.",
            "avoid_terms": [],
            "caution_terms": ["tachycardia", "long qt"],
            "practice_note": "Frequent use signals poorly controlled disease; reassess maintenance therapy.",
        },
        {
            "name": "Beclomethasone Inhaled",
            "class": "Inhaled corticosteroid (ICS)",
            "summary": "Standard preventer for persistent asthma.",
            "avoid_terms": [],
            "caution_terms": ["tuberculosis active", "osteoporosis"],
            "practice_note": "Rinse mouth after use to reduce oral candidiasis risk; review technique regularly.",
        },
        {
            "name": "Tiotropium",
            "class": "Long-acting anticholinergic (LAMA)",
            "summary": "Once-daily bronchodilator preferred in COPD maintenance therapy.",
            "avoid_terms": [],
            "caution_terms": ["glaucoma", "urinary retention", "bph", "renal impairment"],
            "practice_note": "Avoid eye contact with powder; counsel on correct inhalation technique.",
        },
        {
            "name": "Salmeterol / Fluticasone ICS-LABA",
            "class": "Inhaled corticosteroid + long-acting beta-2 agonist combination",
            "summary": "Combination preventer for persistent asthma or moderate-severe COPD not controlled on ICS alone.",
            "avoid_terms": [],
            "caution_terms": ["diabetes", "osteoporosis", "tachycardia"],
            "practice_note": "Not for acute relief; always ensure a reliever inhaler is also available.",
        },
        {
            "name": "Roflumilast",
            "class": "PDE-4 inhibitor",
            "summary": "Add-on option for severe COPD with frequent exacerbations despite ICS/LABA/LAMA triple therapy.",
            "avoid_terms": ["depression", "liver disease", "cirrhosis"],
            "caution_terms": ["underweight", "psychiatric history"],
            "practice_note": "GI side effects usually settle after 4–8 weeks; monitor weight and mood.",
        },
    ],

    # ─── Constipation ────────────────────────────────────────────────────────────
    "constipation": [
        {
            "name": "Macrogol (Polyethylene Glycol)",
            "class": "Osmotic laxative",
            "summary": "First-line osmotic laxative suitable for a wide range of patients including faecal impaction.",
            "avoid_terms": ["bowel obstruction", "bowel perforation"],
            "caution_terms": ["heart failure", "renal impairment", "sodium restriction"],
            "practice_note": "Ensure adequate fluid intake; adjust dose to achieve comfortable stool consistency.",
        },
        {
            "name": "Lactulose",
            "class": "Osmotic laxative",
            "summary": "Osmotic laxative also used in hepatic encephalopathy management.",
            "avoid_terms": ["bowel obstruction", "galactosaemia"],
            "caution_terms": ["diabetes"],
            "practice_note": "Bloating and flatulence are common; onset 24–48 hours.",
        },
        {
            "name": "Senna",
            "class": "Stimulant laxative",
            "summary": "Widely used stimulant laxative, often effective for opioid-induced constipation.",
            "avoid_terms": ["bowel obstruction"],
            "caution_terms": ["elderly"],
            "practice_note": "Abdominal cramping possible; review need regularly to avoid laxative dependence.",
        },
        {
            "name": "Docusate Sodium",
            "class": "Stool softener",
            "summary": "Useful softener when straining must be minimised (e.g. post-surgical, post-cardiac event).",
            "avoid_terms": ["bowel obstruction"],
            "caution_terms": [],
            "practice_note": "Less effective as a sole agent; often combined with stimulant laxatives.",
        },
        {
            "name": "Linaclotide",
            "class": "Guanylate cyclase-C agonist",
            "summary": "Consider when IBS-C or chronic constipation persists despite first-line agents.",
            "avoid_terms": ["bowel obstruction"],
            "caution_terms": [],
            "practice_note": "Diarrhoea is the most common side effect; take 30 min before first meal of the day.",
        },
    ],

    # ─── Urinary Symptoms / BPH ──────────────────────────────────────────────────
    "urinary_bph": [
        {
            "name": "Tamsulosin",
            "class": "Alpha-1 adrenoceptor blocker",
            "summary": "First-line option for lower urinary tract symptoms (LUTS) due to BPH.",
            "avoid_terms": ["hypotension severe"],
            "caution_terms": ["elderly", "hypotension", "cataract surgery planned"],
            "practice_note": "Intraoperative floppy iris syndrome risk with cataract surgery; inform ophthalmologist in advance.",
        },
        {
            "name": "Finasteride",
            "class": "5-alpha reductase inhibitor",
            "summary": "Reduces prostate volume over time; considered when prostate is enlarged and long-term management is planned.",
            "avoid_terms": ["pregnant"],
            "caution_terms": ["liver disease"],
            "practice_note": "Benefits take 6–12 months; discuss sexual side effects. Women must not handle crushed tablets.",
        },
        {
            "name": "Solifenacin",
            "class": "Muscarinic antagonist",
            "summary": "Used for overactive bladder symptoms (urgency, frequency, urge incontinence).",
            "avoid_terms": ["urinary retention", "bph", "glaucoma", "bowel obstruction"],
            "caution_terms": ["elderly", "ckd", "liver disease", "constipation"],
            "practice_note": "Anticholinergic burden matters in older patients; review Beers Criteria.",
        },
        {
            "name": "Mirabegron",
            "class": "Beta-3 adrenergic agonist",
            "summary": "Alternative to antimuscarinics for overactive bladder with lower anticholinergic burden.",
            "avoid_terms": ["severe hypertension uncontrolled"],
            "caution_terms": ["hypertension", "elderly", "renal impairment", "liver disease"],
            "practice_note": "Monitor blood pressure; preferable to anticholinergics in elderly for cognitive safety.",
        },
    ],

    # ─── Anticoagulation ─────────────────────────────────────────────────────────
    "anticoagulation": [
        {
            "name": "Apixaban",
            "class": "Direct factor Xa inhibitor (DOAC)",
            "summary": "Twice-daily DOAC for AF-related stroke prevention and VTE treatment/prevention.",
            "avoid_terms": ["mechanical heart valve", "antiphospholipid syndrome", "dialysis"],
            "caution_terms": ["ckd", "renal impairment", "elderly", "gi bleed", "liver disease"],
            "practice_note": "Does not require routine INR monitoring; check renal function annually.",
        },
        {
            "name": "Rivaroxaban",
            "class": "Direct factor Xa inhibitor (DOAC)",
            "summary": "Once-daily DOAC for AF and VTE prevention and treatment.",
            "avoid_terms": ["mechanical heart valve", "antiphospholipid syndrome", "liver disease", "cirrhosis"],
            "caution_terms": ["ckd", "renal impairment", "elderly", "gi bleed"],
            "practice_note": "Take with evening meal to maximise absorption; avoid in significant hepatic impairment.",
        },
        {
            "name": "Warfarin",
            "class": "Vitamin K antagonist",
            "summary": "Still indicated for mechanical heart valves, antiphospholipid syndrome, and when DOACs are unsuitable.",
            "avoid_terms": ["pregnant"],
            "caution_terms": ["elderly", "liver disease", "frequent falls"],
            "practice_note": "Regular INR monitoring essential; extensive food and drug interactions require management.",
        },
        {
            "name": "Low-Molecular-Weight Heparin (LMWH)",
            "class": "Subcutaneous anticoagulant",
            "summary": "Preferred in pregnancy-associated VTE and cancer-associated thrombosis.",
            "avoid_terms": ["heparin induced thrombocytopaenia"],
            "caution_terms": ["ckd", "renal impairment", "elderly", "obesity"],
            "practice_note": "Anti-Xa monitoring may be required in renal impairment or obesity; subcutaneous injection required.",
        },
        {
            "name": "Dabigatran",
            "class": "Direct thrombin inhibitor (DOAC)",
            "summary": "Twice-daily DOAC reversible with idarucizumab if needed.",
            "avoid_terms": ["mechanical heart valve", "antiphospholipid syndrome", "severe renal failure"],
            "caution_terms": ["renal impairment", "elderly", "gi bleed"],
            "practice_note": "Most renally cleared of the DOACs; higher GI bleed rate than other DOACs.",
        },
    ],
}


GLOBAL_ALERTS = {
    "pregnan": "Pregnancy significantly alters drug selection and dosing; verify trimester-specific safety for all agents discussed.",
    "breastfeed": "Breastfeeding status may affect preferred agents; check infant transfer data before recommending.",
    "ckd": "Renal impairment increases risk from renally cleared drugs; dosing review and nephrotoxic avoidance are essential.",
    "kidney disease": "Kidney disease requires dosing review and avoidance of nephrotoxic options.",
    "renal impairment": "Renal impairment requires dosing review and avoidance of nephrotoxic options.",
    "liver disease": "Hepatic impairment can narrow drug choices and lower safe dose ceilings for many agents.",
    "cirrhosis": "Cirrhosis significantly impairs drug metabolism; many agents require dose reduction or avoidance.",
    "gi bleed": "Prior GI bleeding raises concern for NSAIDs, anticoagulants, and other bleeding-risk therapies.",
    "anticoagulant": "Concurrent anticoagulation raises bleeding and interaction risk across many drug classes.",
    "elderly": "Older adults may be more vulnerable to sedation, falls, renal decline, and anticholinergic burden.",
    "older adult": "Older adults may be more vulnerable to sedation, falls, renal decline, and anticholinergic burden.",
    "allergy": "Documented allergies must be verified; cross-reactivity is possible within some drug classes.",
    "heart failure": "Heart failure restricts several drug classes including NSAIDs, certain CCBs, and high-sodium preparations.",
    "diabetes": "Diabetes can affect drug suitability; corticosteroids and thiazide diuretics may worsen glycaemic control.",
    "long qt": "Long QT / arrhythmia limits several classes including antihistamines, antiemetics, and certain antibiotics.",
    "seizure": "Seizure history is a contraindication or caution for multiple classes including bupropion and tramadol.",
    "parkinson": "Parkinson's disease is a contraindication for dopamine-blocking antiemetics and antipsychotics.",
}


def _normalize(text):
    return " ".join((text or "").lower().replace("/", " ").replace(",", " ").split())


def get_area_options():
    return list(THERAPEUTIC_AREAS.keys())


def evaluate_alternatives(area_label, patient_history, current_medications):
    area_key = THERAPEUTIC_AREAS[area_label]
    history_text = _normalize(patient_history)
    medication_text = _normalize(current_medications)
    combined_text = f"{history_text} {medication_text}".strip()

    recommendations = []
    for option in DRUG_CATALOG[area_key]:
        option_name = option["name"].lower()
        if option_name in medication_text:
            continue

        avoid_matches = [term for term in option["avoid_terms"] if term in combined_text]
        caution_matches = [term for term in option["caution_terms"] if term in combined_text]

        score = 100
        score -= len(avoid_matches) * 35
        score -= len(caution_matches) * 15

        if avoid_matches:
            fit_label = "Avoid / poor fit"
        elif caution_matches:
            fit_label = "Use caution"
        else:
            fit_label = "Reasonable discussion option"

        recommendations.append(
            {
                "name": option["name"],
                "drug_class": option["class"],
                "summary": option["summary"],
                "fit_label": fit_label,
                "score": score,
                "avoid_matches": avoid_matches,
                "caution_matches": caution_matches,
                "practice_note": option["practice_note"],
            }
        )

    recommendations.sort(key=lambda item: item["score"], reverse=True)

    alerts = []
    seen_messages = set()
    for keyword, message in GLOBAL_ALERTS.items():
        if keyword in combined_text and message not in seen_messages:
            alerts.append(message)
            seen_messages.add(message)

    return recommendations[:5], alerts