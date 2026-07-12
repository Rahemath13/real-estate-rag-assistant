import streamlit as st
from rag.chain import RealEstateRAG

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide"
)

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("pages/login.py")

if "rag" not in st.session_state:
    st.session_state.rag = RealEstateRAG()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🏠 Real Estate AI Assistant")

with st.sidebar:

    st.header("Menu")

    if st.button("🗑 Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.messages = []
        st.switch_page("pages/login.py")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about any property...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Searching documents..."):

        answer, sources = st.session_state.rag.ask(question)

    with st.chat_message("assistant"):

        st.markdown(answer)

        st.markdown("### 📄 Sources")

        for source in sources:
            st.write(f"✅ {source}")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )