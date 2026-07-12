import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)

st.title("🏠 Real Estate AI Assistant")

st.markdown("### Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login", use_container_width=True):

    if username == "admin" and password == "admin123":

        st.session_state.logged_in = True

        st.success("Login Successful")

        st.switch_page("pages/chat.py")

    else:

        st.error("Invalid Username or Password")