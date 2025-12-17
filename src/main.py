import streamlit as st
from app_pages import home, url_setting, selection

st.set_page_config(page_title="Web Diagnostic System", layout="wide")

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Sidebar Button Styling */
    section[data-testid="stSidebar"] div.stButton > button:first-child {
        width: 100%;
        text-align: left;
        border-radius: 4px;
        margin-bottom: 8px;
        border: 1px solid transparent;
        background-color: transparent;
        color: #ffffff;
        font-weight: 500;
        padding: 10px 15px;
        transition: all 0.2s ease;
    }
    section[data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #f0f2f6;
        color: #2c3e50;
        border-color: #d1d5db;
    }
    section[data-testid="stSidebar"] div.stButton > button:active,
    section[data-testid="stSidebar"] div.stButton > button:focus {
        background-color: #e8f0fe;
        color: #1a73e8;
        border-color: #1a73e8;
        box-shadow: none;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Global Card Styling */
    .stCard {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("導覽選單")
st.sidebar.markdown("---")

if st.sidebar.button("首頁", use_container_width=True):
    st.session_state["current_page"] = "Home"

if st.sidebar.button("網頁檢核", use_container_width=True):
    st.session_state["current_page"] = "Run"

if st.sidebar.button("項目選擇", use_container_width=True):
    st.session_state["current_page"] = "Settings"

st.sidebar.markdown("---")
st.sidebar.caption("Web Diagnostic System v1.0")

# Page Routing
if st.session_state["current_page"] == "Home":
    home.show()
elif st.session_state["current_page"] == "Settings":
    selection.show()
elif st.session_state["current_page"] == "Run":
    url_setting.show()


