import streamlit as st
from services.api_client import N8nApiClient
from utils.test_result import TEST_OPTIONS, display_test_result

def show():
    st.title("網頁檢核")
    
    # 初始化 session_state
    if "target_url" not in st.session_state:
        st.session_state["target_url"] = ""
    if "selected_tests" not in st.session_state:
        st.session_state["selected_tests"] = ["檢查連結 (validLink)"]
    if "havemail_url" not in st.session_state:
        st.session_state["havemail_url"] = ""
    if "classification_url" not in st.session_state:
        st.session_state["classification_url"] = ""
    if "isupdate_url" not in st.session_state:
        st.session_state["isupdate_url"] = ""
    if "haveNews_url" not in st.session_state:
        st.session_state["haveNews_url"] = ""
    if "publicdata_url" not in st.session_state:
        st.session_state["publicdata_url"] = ""
    if "sitemap_url" not in st.session_state:
        st.session_state["sitemap_url"] = ""
    
    # 測試模式設定
    is_test_mode = st.checkbox("啟用測試模式 (Test Mode)", value=False, help="Append -test to the base URL")
    #is_test_mode = False

    # 使用 Columns 排版：輸入框 + 按鈕
    col_input, col_btn = st.columns([3, 1], vertical_alignment="bottom")
    
    with col_input:
        url_input = st.text_input(
            "目標網址", 
            value=st.session_state["target_url"], 
            label_visibility="collapsed", 
            placeholder="請輸入網址 (例如: https://www.google.com)"
        )
        # 更新 session state
        st.session_state["target_url"] = url_input
        
    with col_btn:
        run_btn = st.button("開始檢測 (Start)", type="primary", use_container_width=True)

    # 意見信箱
    st.markdown("### 意見信箱")
    havemail_url_input = st.text_input(
        "意見信箱URL", 
        value=st.session_state["havemail_url"], 
        label_visibility="collapsed", 
        placeholder="非必填 - 若需要測試請輸入相關信息"
    )
    st.session_state["havemail_url"] = havemail_url_input

    # 內容分類
    st.markdown("### 內容分類")
    classification_url_input = st.text_input(
        "內容分類URL (haveClassification)",
        value=st.session_state["classification_url"],
        label_visibility="collapsed",
        placeholder="非必填 - 若需要測試請輸入相關信息"
    )
    st.session_state["classification_url"] = classification_url_input

    # 內容更新
    st.markdown("### 內容更新")
    isupdate_url_input = st.text_input(
        "內容更新URL (isUpdateShow)",
        value=st.session_state["isupdate_url"],
        label_visibility="collapsed",
        placeholder="非必填 - 若需要測試請輸入相關信息"
    )
    st.session_state["isupdate_url"] = isupdate_url_input

    # 重大政策
    st.markdown("### 重大政策")
    haveNews_url_input = st.text_input(
        "重大政策URL (haveNews)",
        value=st.session_state["haveNews_url"],
        label_visibility="collapsed",
        placeholder="非必填 - 若需要測試請輸入相關信息"
    )
    st.session_state["haveNews_url"] = haveNews_url_input

    # 公開資訊
    st.markdown("### 公開資訊")
    publicdata_url_input = st.text_input(
        "公開資訊URL (havePublicData)",
        value=st.session_state["publicdata_url"],
        label_visibility="collapsed",
        placeholder="非必填 - 若需要測試請輸入相關信息"
    )
    st.session_state["publicdata_url"] = publicdata_url_input

    # 提供Sitemap.xml文件
    st.markdown("### 提供Sitemap.xml文件")
    sitemap_url_input = st.text_input(
        "提供Sitemap.xml文件URL (Sitemap)",
        value=st.session_state["sitemap_url"],
        label_visibility="collapsed",
        placeholder="非必填 - 若需要測試請輸入相關信息"
    )
    st.session_state["sitemap_url"] = sitemap_url_input

    # 顯示目前設定狀態
    selected_count = len(st.session_state["selected_tests"])
    st.caption(f"目前已選定 **{selected_count}** 個測試項目。")
    # st.markdown('</div>', unsafe_allow_html=True)

    if run_btn:
        if not st.session_state["selected_tests"]:
            st.error("未選擇任何測試項目！請先至「項目選擇」頁面勾選。")
        elif not url_input:
            st.error("請輸入目標網址！")
        else:
            client = N8nApiClient(is_test=is_test_mode)
            payload = {"link": url_input}
            selected_tests = st.session_state["selected_tests"]
            
            st.markdown("### 檢測結果報告")
            
            # 建立進度條
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            results_container = st.container()
            
            with results_container:
                for i, test_name in enumerate(selected_tests):
                    endpoint = TEST_OPTIONS[test_name]
                    status_text.text(f"正在執行: {test_name} ({i+1}/{selected_count})...")
                    
                    # 每個測試結果包在一個 Card 中
                    # st.markdown(f'<div class="stCard">', unsafe_allow_html=True)
                    st.markdown(f"#### {test_name}")
                    
                    try:
                        with st.spinner(f"正在連線至 {endpoint}..."):
                            response = client.call_endpoint(endpoint, data=payload)
                        
                        display_test_result(endpoint, response, label=test_name)
                    except Exception as e:
                        st.error(f"發生錯誤: {str(e)}")
                    
                    # st.markdown('</div>', unsafe_allow_html=True)
                    progress_bar.progress((i + 1) / selected_count)
                
            status_text.text("所有測試執行完畢。")
            st.success("檢測完成！")
