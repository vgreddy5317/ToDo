import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to the application"""
    st.markdown("""
        <style>
        .stCheckbox {
            padding: 10px;
            border-radius: 5px;
            background-color: #f0f2f6;
            margin: 5px 0;
        }

        .stButton button {
            width: 100%;
        }

        /* Style for Complete button */
        .stButton button[data-testid*="complete"] {
            background-color: #28a745;
            color: white;
        }

        .stProgress > div > div > div {
            background-color: #FF4B4B;
        }

        .task-container {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 5px 0;
        }

        .success-message {
            padding: 10px;
            border-radius: 5px;
            background-color: #90EE90;
            color: white;
        }

        .error-message {
            padding: 10px;
            border-radius: 5px;
            background-color: #FFB6C1;
            color: white;
        }

        .sidebar .element-container {
            margin-bottom: 20px;
        }

        .metric-container {
            background-color: #f0f2f6;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)