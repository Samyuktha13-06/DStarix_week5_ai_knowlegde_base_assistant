import requests
# pyrefly: ignore [missing-import]
import streamlit as st


st.set_page_config(
    page_title="AI Knowledge Base Assistant",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📚 AI Knowledge Base Assistant")

st.markdown(
    """
    Ask questions about the **DStarix Internship Guide**
    and receive answers grounded in the knowledge base.
    """
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("💡 Suggested Questions")

    suggestions = [
        "How long is the internship?",
        "What are the working days?",
        "Can interns use ChatGPT?",
        "How will interns be evaluated?",
        "Who should I contact for technical questions?"
    ]

    for suggestion in suggestions:

        st.write(f"• {suggestion}")

    st.divider()

    st.caption(
        "Powered by Advanced RAG • FAISS • BM25 • "
        "Reranking • Groq"
    )


# --------------------------------------------------
# Question Input
# --------------------------------------------------

question = st.text_input(
    "Ask your question",
    placeholder="e.g. How long is the internship?"
)


# --------------------------------------------------
# Ask Button
# --------------------------------------------------

if st.button("🔍 Ask Assistant", use_container_width=False):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching the knowledge base..."
        ):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={
                        "question": question
                    },
                    timeout=120
                )

                if response.status_code == 200:

                    data = response.json()

                    st.subheader("🤖 Answer")

                    st.write(
                        data["answer"]
                    )

                    st.divider()

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Confidence",
                            data["confidence"].upper()
                        )

                    with col2:

                        status = (
                            "Yes"
                            if data["found_in_documents"]
                            else "No"
                        )

                        st.metric(
                            "Found in Documents",
                            status
                        )

                else:

                    try:

                        error_message = (
                            response.json()
                            .get(
                                "detail",
                                "Unable to process the request."
                            )
                        )

                    except Exception:

                        error_message = (
                            "Unable to process the request."
                        )

                    st.error(
                        error_message
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Unable to connect to the FastAPI backend. "
                    "Please make sure the API server is running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request timed out. "
                    "Please try again."
                )

            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )