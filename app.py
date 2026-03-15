import os
import time

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from drug_support import get_area_options, evaluate_alternatives

# =============================
# 🚀 APP SETUP
# =============================
st.set_page_config(
    page_title="MedIQ Clinical Assistant",
    page_icon="🩺",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* ===== MedIQ Global Theme ===== */
    html, body { background: #e9f1ee !important; }

    .stApp {
        background: linear-gradient(150deg, #f0ebe0 0%, #dff1ed 55%, #e8f5f0 100%) !important;
    }

    /* Force all main-area text dark so nothing disappears on light bg */
    .main, .main p, .main span, .main div, .main li,
    .main h1, .main h2, .main h3, .main h4, .main h5,
    [data-testid="stMarkdown"], [data-testid="stMarkdown"] *,
    [data-testid="stText"], [data-testid="stText"] * { color: #183b36 !important; }

    .main .block-container {
        background: transparent !important;
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* ===== Sidebar ===== */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div,
    [data-testid="stSidebar"] > div > div {
        background: linear-gradient(180deg, #0a3530 0%, #0f4940 50%, #124f45 100%) !important;
    }
    [data-testid="stSidebar"] *:not(input):not(textarea) { color: #ddf0eb !important; }
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p { color: #9fd4c8 !important; font-weight: 600 !important; }
    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] textarea {
        background: rgba(255,255,255,0.1) !important;
        color: #ddf0eb !important;
        border: 1px solid rgba(255,255,255,0.18) !important;
    }

    /* ===== Tabs ===== */
    [data-baseweb="tab-list"] {
        background: transparent !important;
        border-bottom: 2px solid rgba(14,116,105,0.22) !important;
        gap: 0.3rem;
    }
    [data-baseweb="tab"] {
        background: transparent !important;
        color: #50635f !important;
        font-weight: 600 !important;
        font-size: 0.97rem !important;
        padding: 0.5rem 1.3rem !important;
        border-radius: 10px 10px 0 0 !important;
        border: none !important;
    }
    [data-baseweb="tab"][aria-selected="true"] {
        background: rgba(14,116,105,0.09) !important;
        color: #0e7469 !important;
        border-bottom: 3px solid #0e7469 !important;
    }
    [data-baseweb="tab-panel"] { background: transparent !important; padding-top: 1.4rem !important; }

    /* ===== Text inputs & textareas ===== */
    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stPasswordInput"] input {
        background: #ffffff !important;
        color: #183b36 !important;
        border: 1.5px solid rgba(14,116,105,0.3) !important;
        border-radius: 10px !important;
        caret-color: #0e7469 !important;
    }
    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus,
    [data-testid="stPasswordInput"] input:focus {
        border-color: #0e7469 !important;
        box-shadow: 0 0 0 3px rgba(14,116,105,0.14) !important;
    }
    [data-testid="stTextInput"] input::placeholder,
    [data-testid="stTextArea"] textarea::placeholder { color: #8aada8 !important; }

    /* ===== Widget labels in main area ===== */
    label, [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] span { color: #183b36 !important; font-weight: 600 !important; }

    /* ===== Selectbox ===== */
    [data-baseweb="select"] > div:first-child {
        background: #ffffff !important;
        border: 1.5px solid rgba(14,116,105,0.3) !important;
        border-radius: 10px !important;
    }
    [data-baseweb="select"] span, [data-baseweb="select"] div { background: transparent !important; color: #183b36 !important; }
    [data-baseweb="popover"] [role="listbox"], [data-baseweb="menu"] {
        background: #ffffff !important;
        border: 1px solid rgba(14,116,105,0.2) !important;
    }
    [data-baseweb="menu"] [role="option"], [data-baseweb="menu"] li { color: #183b36 !important; }
    [data-baseweb="menu"] [role="option"]:hover { background: #d5eee8 !important; }

    /* ===== Multiselect tags ===== */
    [data-baseweb="tag"] { background: #d5eee8 !important; color: #0a5c53 !important; border-radius: 6px !important; }
    [data-baseweb="tag"] span { color: #0a5c53 !important; }

    /* ===== Slider ===== */
    [data-testid="stSlider"] [role="progressbar"] { background: #0e7469 !important; }
    [data-testid="stSlider"] [role="slider"] {
        background: #0e7469 !important;
        border-color: #0e7469 !important;
        box-shadow: 0 2px 8px rgba(14,116,105,0.4) !important;
    }
    [data-testid="stSlider"] p { color: #183b36 !important; }

    /* ===== Chat messages ===== */
    [data-testid="stChatMessage"] {
        background: rgba(255,253,248,0.94) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(14,116,105,0.1) !important;
        margin-bottom: 0.4rem !important;
    }
    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] span,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] strong { color: #183b36 !important; }

    /* ===== Chat input ===== */
    [data-testid="stChatInput"],
    [data-testid="stChatInput"] > div {
        background: #ffffff !important;
        border-radius: 14px !important;
        border: 1.5px solid rgba(14,116,105,0.28) !important;
    }
    [data-testid="stChatInput"] textarea { background: #ffffff !important; color: #183b36 !important; }

    /* ===== Buttons ===== */
    [data-testid="stButton"] > button,
    [data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #0e7469, #18a091) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        font-weight: 700 !important;
        padding: 0.45rem 1.4rem !important;
        box-shadow: 0 4px 14px rgba(14,116,105,0.28) !important;
    }
    [data-testid="stButton"] > button:hover,
    [data-testid="stDownloadButton"] > button:hover {
        background: linear-gradient(135deg, #0b5e54, #0e7469) !important;
        box-shadow: 0 6px 20px rgba(14,116,105,0.42) !important;
        transform: translateY(-1px) !important;
    }

    /* ===== Alert / warning / info boxes ===== */
    [data-testid="stAlert"] { border-radius: 12px !important; }
    [data-testid="stAlert"] p, [data-testid="stAlert"] span { color: inherit !important; }

    /* ===== Headers & caption ===== */
    h1, h2, h3 { color: #183b36 !important; }
    [data-testid="stCaptionContainer"] p { color: #50635f !important; }

    /* ===== Checkbox ===== */
    [data-testid="stCheckbox"] label span,
    [data-testid="stCheckbox"] p { color: #183b36 !important; }

    /* ===== Horizontal rule ===== */
    hr { border-color: rgba(14,116,105,0.2) !important; }

    /* ===== Scrollbar ===== */
    ::-webkit-scrollbar { width: 7px; height: 7px; }
    ::-webkit-scrollbar-track { background: #dff1ed; }
    ::-webkit-scrollbar-thumb { background: #0e7469; border-radius: 6px; }

    /* ===== Custom component styles ===== */
    .hero-card {
        padding: 1.4rem 1.5rem;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(255,252,246,0.97), rgba(230,247,242,0.93));
        border: 1px solid rgba(14,116,105,0.14);
        box-shadow: 0 18px 40px rgba(14,116,105,0.08);
        margin-bottom: 1rem;
    }
    .hero-title { font-size: 2.3rem; font-weight: 700; color: #183b36; margin-bottom: 0.35rem; }
    .hero-subtitle { color: #50635f; font-size: 1rem; margin: 0; }

    .tool-card {
        background: rgba(255,252,246,0.9);
        border: 1px solid rgba(14,116,105,0.14);
        border-radius: 18px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.9rem;
        box-shadow: 0 8px 24px rgba(14,116,105,0.07);
    }
    .tool-card h4 { margin: 0 0 0.35rem 0; color: #183b36; font-size: 1.07rem; }
    .tool-card p { margin: 0.2rem 0; color: #3a5652; font-size: 0.93rem; }

    .fit-chip {
        display: inline-block;
        padding: 0.26rem 0.7rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 700;
        margin-bottom: 0.55rem;
    }

    /* ===== Responsive ===== */
    @media (max-width: 768px) {
        .hero-title { font-size: 1.55rem !important; }
        .main .block-container { padding-left: 0.7rem !important; padding-right: 0.7rem !important; }
        .tool-card { padding: 0.75rem !important; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">MedIQ Clinical Assistant</div>
        <p class="hero-subtitle">General health guidance for patients, with a clinician support panel for medication alternative screening.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("General medical information only. This app does not replace a licensed clinician, urgent care, or emergency services.")


# =============================
# 🧰 SIDEBAR — SETTINGS
# =============================
st.sidebar.title("⚙️ Settings")
api_key = st.sidebar.text_input("Groq API Key", type="password", help="Get it from console.groq.com")

MODEL_OPTIONS = [
    "llama-3.1-8b-instant"
]
model_name = st.sidebar.selectbox("Groq Model", MODEL_OPTIONS, index=0)

temperature = st.sidebar.slider("Temperature (creativity)", 0.1,1.0,0.3,
                                help="Lower = factual, Higher = creative")
max_tokens = st.sidebar.slider("Max Tokens", 200,600,400)

# 🔥 Editable System Prompt
default_prompt = """You are a careful, friendly medical assistant.  
Rules:  
- Always answer in exactly 6 numbered sections with these headings:  
    1. Summary
    2. Common Causes
    3. Safe Home Remedies
    4. Prevention Tips
    5. Medication Advice
    6. Doctor Visit Advice
- Write in English only.
- Adjust detail by max_tokens: under 100 = 1-2 lines per section, 100-250 = 2-3 lines per section, above 250 = 4-5 lines per section.
- Provide only general health information, not diagnosis, prescriptions, or personal medical treatment.
- When medication is discussed, keep advice high level and remind the user to check allergies, pregnancy status, kidney/liver disease, and drug interactions with a licensed clinician.
"""



custom_system_prompt = st.sidebar.text_area("System prompt (rules)", default_prompt, height=200)

col_a, col_b = st.sidebar.columns(2)
with col_a:
    clear_chat = st.button("🧹ClearChat")
with col_b:
    pass

# =============================
# 🧠 SESSION STATE
# =============================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Share your symptoms or question, and I’ll guide you step by step."}
    ]

if clear_chat:
    st.session_state.messages = [{"role": "assistant", "content": "Chat cleared. Fresh start!"}]


# =============================
# 🧩 PROMPT — SYSTEM GUARDRAILS
# =============================
SYSTEM_PROMPT = custom_system_prompt

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content=SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    HumanMessage(content="{input}"),
])

# =============================
# 🔗 LLM FACTORY
# =============================
def make_llm():
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar to start.")
        return None
    os.environ["GROQ_API_KEY"] = api_key
    try:
        llm = ChatGroq(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return llm
    except Exception as e:
        st.error(f"LLM init error: {e}")
        return None

def _lc_history_from_session():
    lc_msgs = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            lc_msgs.append(HumanMessage(content=m["content"]))
        elif m["role"] == "assistant":
            lc_msgs.append(AIMessage(content=m["content"]))
    return lc_msgs

assistant_tab, clinician_tab = st.tabs(["Patient Assistant", "Doctor Support"])

with assistant_tab:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Describe your symptoms or ask a health question...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        llm = make_llm()
        if llm is not None:
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_reply = ""
                try:
                    chain = prompt | llm
                    result = chain.invoke({
                        "history": _lc_history_from_session(),
                        "input": user_input,
                    })
                    full_reply = result.content if hasattr(result, "content") else str(result)
                    placeholder.markdown(full_reply)
                except Exception as e:
                    full_reply = f"Sorry, response error: {e}"
                    placeholder.error(full_reply)

            st.session_state.messages.append({"role": "assistant", "content": full_reply})

    chat_txt_lines = []
    for message in st.session_state.messages:
        role = "User" if message["role"] == "user" else "Assistant"
        chat_txt_lines.append(f"[{role}] {message['content']}")
    chat_txt = "\n\n".join(chat_txt_lines)

    st.download_button(
        label="Download Chat",
        data=chat_txt,
        file_name=f"medical_assistant_chat_{int(time.time())}.txt",
        mime="text/plain",
    )

with clinician_tab:
    st.subheader("Alternative Drug Finder")
    st.write(
        "Screen common alternative medication options against the patient profile below. "
        "This is a quick discussion aid — not a prescribing engine. Always verify against full prescribing information and local formulary."
    )

    therapeutic_area = st.selectbox("Therapeutic area / symptom category", get_area_options())

    st.markdown("**Patient profile**")
    col1, col2 = st.columns(2)
    with col1:
        age_group = st.selectbox(
            "Age group",
            ["18–64 years", "Under 18 years", "65 years or older"],
        )
        sex = st.selectbox("Sex", ["Not specified", "Male", "Female"])
        pregnancy_status = st.selectbox(
            "Pregnancy / feeding status",
            [
                "Not pregnant / not applicable",
                "Pregnant — 1st trimester",
                "Pregnant — 2nd trimester",
                "Pregnant — 3rd trimester",
                "Breastfeeding",
            ],
        )
    with col2:
        known_allergies = st.multiselect(
            "Known drug allergies",
            [
                "NSAIDs / Aspirin",
                "Sulfa drugs",
                "Penicillin",
                "Cephalosporins",
                "Fluoroquinolones",
                "ACE inhibitors",
                "Statins",
            ],
        )
        other_allergy = st.text_input("Other allergy (free text)", placeholder="e.g. codeine, metronidazole")

    st.markdown("**Active conditions & organ function**")
    col3, col4 = st.columns(2)
    with col3:
        conditions_a = st.multiselect(
            "Conditions (A – L)",
            [
                "Asthma / COPD",
                "Cardiac arrhythmia / Long QT",
                "Cirrhosis / Liver disease",
                "CKD / Renal impairment",
                "Diabetes (Type 2)",
                "GI bleed history",
                "Glaucoma",
                "Heart failure",
                "Hypertension",
            ],
        )
    with col4:
        conditions_b = st.multiselect(
            "Conditions (M – Z)",
            [
                "Malnutrition",
                "On anticoagulant (warfarin / DOAC)",
                "Osteoporosis",
                "Parkinson's disease",
                "Peptic ulcer disease",
                "Seizure disorder",
                "Urinary retention / BPH",
            ],
        )

    current_medications = st.text_area(
        "Current medications",
        placeholder="Examples: ibuprofen, apixaban, sertraline, metformin",
        height=100,
    )

    if st.button("Find alternatives"):
        history_parts = []

        if age_group == "65 years or older":
            history_parts.append("elderly older adult")
        elif age_group == "Under 18 years":
            history_parts.append("pediatric under 18")

        preg_map = {
            "Pregnant — 1st trimester": "pregnant first trimester",
            "Pregnant — 2nd trimester": "pregnant second trimester",
            "Pregnant — 3rd trimester": "pregnant third trimester",
            "Breastfeeding": "breastfeeding",
        }
        if pregnancy_status in preg_map:
            history_parts.append(preg_map[pregnancy_status])

        allergy_map = {
            "NSAIDs / Aspirin": "nsaid allergy aspirin allergy",
            "Sulfa drugs": "sulfa allergy",
            "Penicillin": "penicillin allergy",
            "Cephalosporins": "cephalosporin allergy",
            "Fluoroquinolones": "fluoroquinolone allergy",
            "ACE inhibitors": "ace inhibitor allergy",
            "Statins": "statin allergy",
        }
        for a in known_allergies:
            history_parts.append(allergy_map.get(a, a.lower()))
        if other_allergy.strip():
            history_parts.append(other_allergy.lower())

        condition_map = {
            "Asthma / COPD": "asthma copd",
            "Cardiac arrhythmia / Long QT": "long qt arrhythmia",
            "Cirrhosis / Liver disease": "liver disease cirrhosis",
            "CKD / Renal impairment": "ckd renal impairment kidney disease",
            "Diabetes (Type 2)": "diabetes type 2 diabetes",
            "GI bleed history": "gi bleed gastrointestinal bleed",
            "Glaucoma": "glaucoma",
            "Heart failure": "heart failure",
            "Hypertension": "hypertension",
            "Malnutrition": "malnutrition",
            "On anticoagulant (warfarin / DOAC)": "anticoagulant warfarin doac",
            "Osteoporosis": "osteoporosis",
            "Parkinson's disease": "parkinson",
            "Peptic ulcer disease": "peptic ulcer",
            "Seizure disorder": "seizure disorder",
            "Urinary retention / BPH": "urinary retention bph",
        }
        for c in conditions_a + conditions_b:
            history_parts.append(condition_map.get(c, c.lower()))

        structured_history = " ".join(history_parts)

        recommendations, alerts = evaluate_alternatives(
            therapeutic_area,
            structured_history,
            current_medications,
        )

        if alerts:
            for alert in alerts:
                st.warning(alert)

        if not recommendations:
            st.info("No suggestions generated. Fill in more patient details or try another therapeutic area.")
        else:
            chip_style = {
                "Reasonable discussion option": ("#d5eee8", "#0a5c53"),
                "Use caution": ("#fff3cd", "#7a5400"),
                "Avoid / poor fit": ("#fde8e8", "#9a0000"),
            }
            for rec in recommendations:
                avoid_text = ", ".join(rec["avoid_matches"]) or "None detected"
                caution_text = ", ".join(rec["caution_matches"]) or "None detected"
                chip_bg, chip_color = chip_style.get(rec["fit_label"], ("#ebebeb", "#333"))
                st.markdown(
                    f"""
                    <div class="tool-card">
                        <div class="fit-chip" style="background:{chip_bg};color:{chip_color};">{rec['fit_label']}</div>
                        <h4>{rec['name']}</h4>
                        <p><strong>Class:</strong> {rec['drug_class']}</p>
                        <p><strong>Why it may fit:</strong> {rec['summary']}</p>
                        <p><strong>Avoid signals found:</strong> {avoid_text}</p>
                        <p><strong>Caution signals found:</strong> {caution_text}</p>
                        <p><strong>Clinician note:</strong> {rec['practice_note']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.caption("Suggestions draw from a curated reference set. Always verify against full prescribing information, current guidelines, allergy records, organ function, and local formulary before acting.")


st.sidebar.markdown("---")
st.sidebar.markdown("🩺 **MedIQ Clinical Assistant**")




