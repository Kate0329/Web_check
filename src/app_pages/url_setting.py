import streamlit as st
from services.api_client import N8nApiClient
from utils.test_result import TEST_OPTIONS, display_test_result

def show():
    st.title("執行檢測 (Run Check)")
    
    # 初始化 session_state
    if "target_url" not in st.session_state:
        st.session_state["target_url"] = ""
    if "selected_tests" not in st.session_state:
        st.session_state["selected_tests"] = ["檢查連結 (validLink)"]

    # 測試模式設定
    is_test_mode = st.checkbox("使用測試模式 (-test)", value=True, help="Append -test to the base URL")

    st.markdown("### 輸入目標網址")
    
    # 使用 Columns 排版：輸入框 + 按鈕
    col_input, col_btn = st.columns([3, 1])
    
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
        # 增加一點上邊距讓按鈕對齊輸入框
        st.markdown('<div style="margin-top: 0px;"></div>', unsafe_allow_html=True) 
        run_btn = st.button("開始檢測", type="primary", use_container_width=True)

    # 顯示目前設定狀態
    selected_count = len(st.session_state["selected_tests"])
    st.caption(f"目前將執行 **{selected_count}** 個測試項目 (可至「檢測項目設定」修改)")

    st.markdown("---")

    if run_btn:
        if not st.session_state["selected_tests"]:
            st.error("未選擇任何測試項目！請先至「檢測項目設定」頁面勾選。")
        elif not url_input:
            st.error("請輸入目標網址！")
        else:
            client = N8nApiClient(is_test=is_test_mode)
            payload = {"link": url_input}
            selected_tests = st.session_state["selected_tests"]
            
            st.subheader("測試結果")
            
            # 建立進度條
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, test_name in enumerate(selected_tests):
                endpoint = TEST_OPTIONS[test_name]
                status_text.text(f"正在執行: {test_name} ({i+1}/{selected_count})...")
                
                st.markdown(f"#### 執行中: {test_name}")
                
                try:
                    with st.spinner(f"呼叫 {endpoint}..."):
                        response = client.call_endpoint(endpoint, data=payload)
                    
                    display_test_result(endpoint, response)
                except Exception as e:
                    st.error(f"發生錯誤: {str(e)}")
                
                st.markdown("---")
                progress_bar.progress((i + 1) / selected_count)
                
            status_text.text("所有測試執行完畢！")
            st.success("完成！")
