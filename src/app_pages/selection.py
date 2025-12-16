import streamlit as st
from utils.test_result import TEST_OPTIONS

def show():
    st.title("檢測參數配置 (Configuration)")
    st.markdown("請選擇欲執行的診斷項目，系統將自動儲存您的設定。")

    # 初始化 session_state
    if "selected_tests" not in st.session_state:
        st.session_state["selected_tests"] = ["檢查連結 (validLink)"]

    current_selection = []
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("基礎檢測項目")
        # 檢查是否在已選列表中，決定預設勾選狀態
        is_speed_checked = "網速檢測 (pageSpeed)" in st.session_state["selected_tests"]
        if st.checkbox("網速檢測 (PageSpeed)", value=is_speed_checked):
            current_selection.append("網速檢測 (pageSpeed)")

        is_lang_checked = "語系編碼檢測 (lang)" in st.session_state["selected_tests"]
        if st.checkbox("語系編碼檢測 (Lang)", value=is_lang_checked):
            current_selection.append("語系編碼檢測 (lang)")

        is_https_checked = "加密連結檢測 (https)" in st.session_state["selected_tests"]
        if st.checkbox("加密連結檢測 (Https)", value=is_https_checked):
            current_selection.append("加密連結檢測 (https)")
        
        is_rwd_checked = "響應式設計檢測 (RWD)" in st.session_state["selected_tests"]
        if st.checkbox("響應式設計檢測 (RWD)", value=is_rwd_checked):
            current_selection.append("響應式設計檢測 (RWD)")
        
        is_favicon_checked = "網站圖示檢測 (Favicon)" in st.session_state["selected_tests"]
        if st.checkbox("網站圖示檢測 (Favicon)", value=is_favicon_checked):
            current_selection.append("網站圖示檢測 (Favicon)")

        is_isAnalytics_checked = "流量統計檢測 (WebAnalysis)" in st.session_state["selected_tests"]
        if st.checkbox("流量統計檢測 (WebAnalysis)", value= is_isAnalytics_checked):
            current_selection.append("流量統計檢測 (WebAnalysis)")
        
        is_Animation_checked = "網頁動畫 (Animation)" in st.session_state["selected_tests"]
        if st.checkbox("網頁動畫 (Animation)", value= is_Animation_checked):
            current_selection.append("網頁動畫 (Animation)")

        is_accessibility_checked = "無障礙檢測 (accessibility)" in st.session_state["selected_tests"]
        if st.checkbox("無障礙檢測 (Accessibility)", value= is_accessibility_checked):
            current_selection.append("無障礙檢測 (accessibility)")

    with col2:
        st.subheader("W3C 標準檢測")
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
    st.info(f"目前已啟用 **{len(current_selection)}** 個診斷項目。")
