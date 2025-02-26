import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if 'tasks' not in st.session_state:
        st.session_state.tasks = []
    
    if 'filter_category' not in st.session_state:
        st.session_state.filter_category = "All"
        
    if 'filter_priority' not in st.session_state:
        st.session_state.filter_priority = "All"
        
    if 'sort_by' not in st.session_state:
        st.session_state.sort_by = "Due Date"
