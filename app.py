import requests
# pyrefly: ignore [missing-import]
import streamlit as st

st.set_page_config(
    page_title="AI Knowledge Base Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Knowledge Base Assistant")

st.write(
    "Ask questions about the DStarix Internship Guide."
)

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching knowledge base..."):

            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={
                    "question": question
                }
            )

        if response.status_code == 200:

            data = response.json()

            st.success(data["answer"])

            st.write(
                f"**Confidence:** {data['confidence']}"
            )

        else:

            st.error(
                response.json()["detail"]
            )

    else:

        st.warning(
            "Please enter a question."
        )