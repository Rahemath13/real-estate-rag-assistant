import streamlit as st


def render_chat(role, message):

    with st.chat_message(role):

        st.markdown(message)