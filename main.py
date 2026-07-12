import streamlit as st

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Redirect based on login state
if st.session_state.logged_in:
    st.switch_page("pages/chat.py")
else:
    st.switch_page("pages/login.py")