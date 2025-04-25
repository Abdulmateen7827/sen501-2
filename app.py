import streamlit as st

# Knowledge base of illnesses and their symptoms
knowledge_base = [
    {"illness": "Flu", "symptoms": ["fever", "cough", "fatigue"]},
    {"illness": "Common Cold", "symptoms": ["runny nose", "sore throat", "cough"]},
    {"illness": "Allergies", "symptoms": ["sneezing", "itchy eyes", "runny nose"]}
]

# Extract all unique symptoms
def get_all_symptoms(knowledge_base):
    symptoms = set()
    for item in knowledge_base:
        for symptom in item["symptoms"]:
            symptoms.add(symptom.lower())
    return sorted(list(symptoms))

# Inference logic using set comparison
def forward_chaining(user_symptoms, knowledge_base):
    user_symptoms_set = set(symptom.lower() for symptom in user_symptoms)
    for item in knowledge_base:
        rule_symptoms_set = set(symptom.lower() for symptom in item["symptoms"])
        if rule_symptoms_set.issubset(user_symptoms_set):  # Match only if all required symptoms are selected
            return item["illness"]
    return "Unknown illness"

def main():
    st.set_page_config(page_title="🧠 Symptom Diagnosis App", page_icon="🩺")
    st.title("🧠 Intelligent Health Diagnosis Assistant")
    st.markdown(
        "<p style='font-size:16px; color:gray;'>"
        "Select the symptoms you're experiencing to receive a diagnosis from our rule-based expert system."
        "</p>",
        unsafe_allow_html=True
    )

    # Display contributor info
    with st.expander("ℹ️ Project Contributors"):
        st.markdown("""
        **Group 6 Contributors:**
        - ADEBOWALE ANU VICTOR – `SEN/19/0689`  
        - ASHIFA ABDULMATEEN ADENIYI – `SEN/19/0702`  
        - BALOGUN EMMANUEL AYOMIDE – `SEN/19/0708`  
        - OGUNKENU KAYODE AYOMIDE – `SEN/19/0724`  
        - MAFO MOYOSOREOLUWA AYOMIDE – `SEN/19/0721`  
        - SARAFADEEN IBRAHIM OYINKOLADE – `SEN/19/0742`
        - AKINTAN DAVID OLUWAYEMI – `SEN/19/0698`
        - ADEWUYI EUNICE TOSINMILE – `SEN/19/0695`
        """)

    all_symptoms = get_all_symptoms(knowledge_base)
    capitalized_symptoms = [symptom.capitalize() for symptom in all_symptoms]

    selected_symptoms = st.multiselect("🤒 Select your symptoms:", capitalized_symptoms)

    if st.button("🔍 Diagnose"):
        if not selected_symptoms:
            st.warning("Please select at least one symptom.")
        else:
            normalized_input = [sym.lower() for sym in selected_symptoms]
            diagnosis = forward_chaining(normalized_input, knowledge_base)
            if diagnosis == "Unknown illness":
                st.error("We couldn't identify your illness based on the selected symptoms.")
            else:
                st.success(f"🩺 Based on your symptoms, the diagnosis is: **{diagnosis}**")

    with st.expander("📜 Rule Summary"):
        for item in knowledge_base:
            st.markdown(f"- **IF** {' AND '.join(item['symptoms']).capitalize()} **THEN** {item['illness']}")

if __name__ == "__main__":
    main()
