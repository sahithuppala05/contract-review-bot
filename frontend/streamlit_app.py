import streamlit as st
import requests

BACKEND_URL ="http://127.0.0.1:10000/analyze"

st.set_page_config(page_title="AI Contract Review Bot")
st.title(" AI Contract Review Bot ")

uploaded_file = st.file_uploader("Upload Contract (PDF)", type=["pdf"])
pasted_text = st.text_area("Or Paste Contract Text")

if st.button("Analyze"):

    with st.spinner("Analyzing contract..."):

        if uploaded_file:
            response = requests.post(BACKEND_URL, files={"file": uploaded_file})
        else:
            response = requests.post(
                BACKEND_URL,
                json={"text": pasted_text}
            )

    data = response.json()

    if response.status_code != 200:
        st.error("Backend Error")
        st.write(data)
        st.stop()
    else:
        st.header("📌 Key Information")
        st.write("**Parties:**", data["parties"])
        st.write("**Duration:**", data["contract_duration"])
        st.write("**Payment Terms:**", data["payment_terms"])
        st.write("**Termination:**", data["termination_clauses"])
        st.write("**Renewal:**", data["renewal_terms"])

        st.header("⚠ Risk Flags")
        st.error("🔴 Auto Renewal: " + data["risk_flags"]["auto_renewal_trap"])
        st.warning("🟡 Liability: " + data["risk_flags"]["liability_risk"])
        st.info("🔵 Missing Exit: " + data["risk_flags"]["missing_exit_clause"])

        st.header("📝 Summary")
        st.success(data["plain_english_summary"])

