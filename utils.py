import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chat' not in st.session_state:
        st.session_state.chat = None
    if 'error' not in st.session_state:
        st.session_state.error = None
    if 'input_key' not in st.session_state:
        st.session_state.input_key = 0