import streamlit as st
from app_pages import home, url_setting, selection

st.set_page_config(page_title="N8n API Connector", layout="wide")

# Initialize session state for page navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Custom CSS for better button styling
st.markdown("""
<style>
    section[data-testid="stSidebar"] div.stButton > button:first-child {
        width: 100%;
        text-align: left;
        border-radius: 5px;
        margin-bottom: 5px;
        border: none;
    }
    section[data-testid="stSidebar"] div.stButton > button:active {
        border-color: #FF4B4B;
        color: #FF4B4B;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
if st.sidebar.button("首頁", use_container_width=True):
    st.session_state["current_page"] = "Home"

if st.sidebar.button("執行檢測", use_container_width=True):
    st.session_state["current_page"] = "Run"

if st.sidebar.button("項目勾選", use_container_width=True):
    st.session_state["current_page"] = "Settings"

st.sidebar.markdown("---")

# Page Routing
if st.session_state["current_page"] == "Home":
    home.show()
elif st.session_state["current_page"] == "Settings":
    selection.show()
elif st.session_state["current_page"] == "Run":
    url_setting.show()


