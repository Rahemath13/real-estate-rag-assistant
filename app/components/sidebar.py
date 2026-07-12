import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("🏠 Real Estate AI")

        st.markdown("---")

        st.success("✅ Knowledge Base Loaded")

        st.info("📄 Documents : 21")

        st.info("🤖 Model : Llama 3.3 70B")

        st.info("🗂 Vector DB : FAISS")

        st.markdown("---")

        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.messages = []
            st.switch_page("pages/login.py")