import streamlit as st
from utils.test_result import TEST_OPTIONS

def show():
    st.title("檢測項目設定 (Settings)")
    st.markdown("請在此勾選您想要執行的測試項目。設定將會自動儲存。")

    # 初始化 session_state
    if "selected_tests" not in st.session_state:
        st.session_state["selected_tests"] = ["檢查連結 (validLink)"]

    current_selection = []
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 基本檢測")
        # 檢查是否在已選列表中，決定預設勾選狀態
        is_speed_checked = "網速檢測 (pageSpeed)" in st.session_state["selected_tests"]
        if st.checkbox("網速檢測 (pageSpeed)", value=is_speed_checked):
            current_selection.append("網速檢測 (pageSpeed)")

        is_lang_checked = "語系編碼檢測 (lang)" in st.session_state["selected_tests"]
        if st.checkbox("語系編碼檢測 (lang)", value=is_lang_checked):
            current_selection.append("語系編碼檢測 (lang)")

        is_https_checked = "加密連結檢測 (https)" in st.session_state["selected_tests"]
        if st.checkbox("加密連結檢測 (https)", value=is_https_checked):
            current_selection.append("加密連結檢測 (https)")
        
        is_rwd_checked = "響應式設計檢測 (RWD)" in st.session_state["selected_tests"]
        if st.checkbox("響應式設計檢測 (RWD)", value=is_rwd_checked):
            current_selection.append("響應式設計檢測 (RWD)")
        
        is_favicon_checked = "網站圖示檢測 (Favicon)" in st.session_state["selected_tests"]
        if st.checkbox("網站圖示檢測 (Favicon)", value=is_favicon_checked):
            current_selection.append("網站圖示檢測 (Favicon)")

    with col2:
        st.markdown("### W3C 標準檢測")
        is_valid_checked = "檢查連結 (validLink)" in st.session_state["selected_tests"]
        if st.checkbox("檢查連結 (validLink)", value=is_valid_checked):
            current_selection.append("檢查連結 (validLink)")

        is_html_checked = "W3C HTML 檢查 (W3CHtml)" in st.session_state["selected_tests"]
        if st.checkbox("W3C HTML 檢查 (W3CHtml)", value=is_html_checked):
            current_selection.append("W3C HTML 檢查 (W3CHtml)")
            
        is_css_checked = "W3C CSS 檢查 (W3CCss)" in st.session_state["selected_tests"]
        if st.checkbox("W3C CSS 檢查 (W3CCss)", value=is_css_checked):
            current_selection.append("W3C CSS 檢查 (W3CCss)")

    # 更新 session_state
    st.session_state["selected_tests"] = current_selection
    
    st.markdown("---")
    st.info(f"目前已選擇 **{len(current_selection)}** 個項目。設定完成後，請前往「執行檢測」頁面。")
