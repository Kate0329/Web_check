import streamlit as st
from utils.test_result import TEST_OPTIONS

def show():
    st.title("檢測參數配置 (Configuration)")
    st.markdown("請選擇欲執行的診斷項目，系統將自動儲存您的設定。")

    # 初始化 session_state
    if "selected_tests" not in st.session_state:
        st.session_state["selected_tests"] = []

    # 全選/全不選功能
    def toggle_all():
        if st.session_state.select_all_toggle:
            st.session_state["selected_tests"] = list(TEST_OPTIONS.keys())
        else:
            st.session_state["selected_tests"] = []

    # 檢查是否全選
    is_all_selected = len(st.session_state.get("selected_tests", [])) == len(TEST_OPTIONS)
    
    st.checkbox("全選", value=is_all_selected, key="select_all_toggle", on_change=toggle_all)

    current_selection = []
    
    col1, col2, col3 = st.columns(3)
    
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

    with col3:
        st.markdown("### AI Agent檢測")
        is_logo_checked = "網站名稱或標誌(logo)" in st.session_state["selected_tests"]
        if st.checkbox("網站名稱或標誌(logo)", value=is_logo_checked):
            current_selection.append("網站名稱或標誌(logo)")

        is_datausage_checked = "網站資料開放宣告(dataUsagePolicy)" in st.session_state["selected_tests"]
        if st.checkbox("網站資料開放宣告(dataUsagePolicy)", value=is_datausage_checked):
            current_selection.append("網站資料開放宣告(dataUsagePolicy)")

        is_privacy_checked = "隱私權及資訊安全宣告(privacyPolicy)" in st.session_state["selected_tests"]
        if st.checkbox("隱私權及資訊安全宣告(privacyPolicy)", value=is_privacy_checked):
            current_selection.append("隱私權及資訊安全宣告(privacyPolicy)")

        is_address_checked = "完整通訊地址(address)" in st.session_state["selected_tests"]
        if st.checkbox("完整通訊地址(address)", value=is_address_checked):
            current_selection.append("完整通訊地址(address)")

        is_phone_checked = "聯絡電話(phone)" in st.session_state["selected_tests"]
        if st.checkbox("聯絡電話(phone)", value=is_phone_checked):
            current_selection.append("聯絡電話(phone)")

        is_multilang_checked = "網站具備多語言版本(lang)" in st.session_state["selected_tests"]
        if st.checkbox("網站具備多語言版本(lang)", value=is_multilang_checked):
            current_selection.append("網站具備多語言版本(lang)")

        is_footer_checked = "頁尾設計(footer)" in st.session_state["selected_tests"]
        if st.checkbox("頁尾設計(footer)", value=is_footer_checked):
            current_selection.append("頁尾設計(footer)")

        is_navigation_checked = "網站導覽功能(navigation )" in st.session_state["selected_tests"]
        if st.checkbox("網站導覽功能(navigation )", value=is_navigation_checked):
            current_selection.append("網站導覽功能(navigation )")

        is_searchkey_checked = "提供Sitemap.xml文件(Sitemap )" in st.session_state["selected_tests"]
        if st.checkbox("提供Sitemap.xml文件(Sitemap )", value=is_searchkey_checked):
            current_selection.append("提供Sitemap.xml文件(Sitemap )")

        is_searchkey_checked = "提供路徑導覽列(breadcrumb )" in st.session_state["selected_tests"]
        if st.checkbox("提供路徑導覽列(breadcrumb )", value=is_searchkey_checked):
            current_selection.append("提供路徑導覽列(breadcrumb )")

        is_searchkey_checked = "重大政策(haveNews )" in st.session_state["selected_tests"]
        if st.checkbox("重大政策(haveNews )", value=is_searchkey_checked):
            current_selection.append("重大政策(haveNews )")

        is_searchkey_checked = "資訊圖像化(haveGraphic )" in st.session_state["selected_tests"]
        if st.checkbox("資訊圖像化(haveGraphic )", value=is_searchkey_checked):
            current_selection.append("資訊圖像化(haveGraphic )")

        is_searchkey_checked = "公開資訊(havePublicData )" in st.session_state["selected_tests"]
        if st.checkbox("公開資訊(havePublicData )", value=is_searchkey_checked):
            current_selection.append("公開資訊(havePublicData )")

        is_searchkey_checked = "內容分類(haveClassification )" in st.session_state["selected_tests"]
        if st.checkbox("內容分類(haveClassification )", value=is_searchkey_checked):
            current_selection.append("內容分類(haveClassification )")

        is_searchkey_checked = "相關連結(haveRelatedLink )" in st.session_state["selected_tests"]
        if st.checkbox("相關連結(haveRelatedLink )", value=is_searchkey_checked):
            current_selection.append("相關連結(haveRelatedLink )")

        is_searchkey_checked = "內容更新(isUpdateShow )" in st.session_state["selected_tests"]
        if st.checkbox("內容更新(isUpdateShow )", value=is_searchkey_checked):
            current_selection.append("內容更新(isUpdateShow )")

        is_searchkey_checked = "更新頻率(updateFreq )" in st.session_state["selected_tests"]
        if st.checkbox("更新頻率(updateFreq )", value=is_searchkey_checked):
            current_selection.append("更新頻率(updateFreq )")

        is_searchkey_checked = "搜尋服務(haveSearch )" in st.session_state["selected_tests"]
        if st.checkbox("搜尋服務(haveSearch )", value=is_searchkey_checked):
            current_selection.append("搜尋服務(haveSearch )")

        is_searchkey_checked = "熱門關鍵字(searchKey )" in st.session_state["selected_tests"]
        if st.checkbox("熱門關鍵字(searchKey )", value=is_searchkey_checked):
            current_selection.append("熱門關鍵字(searchKey )")

        is_searchsug_checked = "搜尋建議(searchSug )" in st.session_state["selected_tests"]
        if st.checkbox("搜尋建議(searchSug )", value=is_searchsug_checked):
            current_selection.append("搜尋建議(searchSug )")

        is_searchsug_checked = "意見信箱(haveMail )" in st.session_state["selected_tests"]
        if st.checkbox("意見信箱(haveMail )", value=is_searchsug_checked):
            current_selection.append("意見信箱(haveMail )")

        is_searchsug_checked = "社群分享(haveShare )" in st.session_state["selected_tests"]
        if st.checkbox("社群分享(haveShare )", value=is_searchsug_checked):
            current_selection.append("社群分享(haveShare )")

        is_searchsug_checked = "社群互動(comunity )" in st.session_state["selected_tests"]
        if st.checkbox("社群互動(comunity )", value=is_searchsug_checked):
            current_selection.append("社群互動(comunity )")

    # 更新 session_state
    st.session_state["selected_tests"] = current_selection
    
    st.markdown("---")
    st.info(f"目前已啟用 **{len(current_selection)}** 個診斷項目。")
