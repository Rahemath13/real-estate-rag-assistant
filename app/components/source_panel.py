import streamlit as st


def render_sources(sources):

    with st.expander("📄 Source Documents"):

        for source in sources:
            st.success(source)