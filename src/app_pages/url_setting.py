import streamlit as st
import time # 延遲
# from urllib.parse import urlparse # 鎖網域
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
    if "navigation_url" not in st.session_state:
        st.session_state["navigation_url"] = ""
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
        st.markdown("#### 目標網址 <span style='color:red'>*</span>", unsafe_allow_html=True)
        url_input = st.text_input(
            "目標網址",
            value=st.session_state["target_url"], 
            label_visibility="collapsed", 
            placeholder="請輸入網址 (例如: https://www.google.com)"
        )
        st.session_state["target_url"] = url_input
        
    with col_btn:
        run_btn = st.button("開始檢測 (Start)", type="primary", use_container_width=True)

    # 意見信箱
    st.markdown("### 意見信箱頁連結 <span style='color:red'>*</span>", unsafe_allow_html=True)
    havemail_url_input = st.text_input(
        "意見信箱URL", 
        value=st.session_state["havemail_url"], 
        label_visibility="collapsed", 
        placeholder="請輸入網址"
    )
    st.session_state["havemail_url"] = havemail_url_input

    # 網頁導覽
    st.markdown("### 網頁導覽頁連結 <span style='color:red'>*</span>", unsafe_allow_html=True)
    classification_url_input = st.text_input(
        "內容分類URL (haveClassification)",
        value=st.session_state.get("classification_url", ""),
        label_visibility="collapsed",
        placeholder="請輸入網址"
    )
    st.session_state["classification_url"] = classification_url_input

    # 內容更新
    st.markdown("### 最新消息頁連結 <span style='color:red'>*</span>", unsafe_allow_html=True)
    isupdate_url_input = st.text_input(
        "內容更新URL (isUpdateShow)",
        value=st.session_state["isupdate_url"],
        label_visibility="collapsed",
        placeholder="請輸入網址"
    )
    st.session_state["isupdate_url"] = isupdate_url_input

    # 重大政策
    st.markdown("### 重大政策頁連結 <span style='color:red'>*</span>", unsafe_allow_html=True)
    haveNews_url_input = st.text_input(
        "重大政策URL (haveNews)",
        value=st.session_state["haveNews_url"],
        label_visibility="collapsed",
        placeholder="請輸入網址"
    )
    st.session_state["haveNews_url"] = haveNews_url_input

    # 公開資訊
    st.markdown("### 公開資訊頁連結 <span style='color:red'>*</span>", unsafe_allow_html=True)
    publicdata_url_input = st.text_input(
        "公開資訊URL (havePublicData)",
        value=st.session_state["publicdata_url"],
        label_visibility="collapsed",
        placeholder="請輸入網址"
    )
    st.session_state["publicdata_url"] = publicdata_url_input

    # Sitemap.xml
    st.markdown("### Sitemap.xml頁連結 <span style='color:red'>*</span>", unsafe_allow_html=True)
    sitemap_url_input = st.text_input(
        "提供Sitemap.xml文件URL (Sitemap)",
        value=st.session_state["sitemap_url"],
        label_visibility="collapsed",
        placeholder="請輸入網址"
    )
    st.session_state["sitemap_url"] = sitemap_url_input


    selected_count = len(st.session_state["selected_tests"])
    st.caption(f"目前已選定 **{selected_count}** 個測試項目。")


    if run_btn:
        if not st.session_state["selected_tests"]:
            st.error("未選擇任何測試項目！請先至「項目選擇」頁面勾選。")
        elif not url_input:
            st.error("請輸入目標網址！")
        else:
            #必填檢查
            required_fields = {}
            selected_tests = st.session_state["selected_tests"]

            if "意見信箱(haveMail )" in selected_tests:
                required_fields["havemail_url"] = ("意見信箱頁連結", st.session_state.get("havemail_url", ""))
            
            if "網站導覽功能(navigation )" in selected_tests:
                required_fields["navigation_url"] = ("網頁導覽頁連結", st.session_state.get("navigation_url", ""))

            isupdate_tests = ["內容更新(isUpdateShow )", "更新頻率(updateFreq )", "提供路徑導覽列(breadcrumb )", "內容分類(haveClassification )"]
            if any(test in selected_tests for test in isupdate_tests):
                required_fields["isupdate_url"] = ("最新消息頁連結", st.session_state.get("isupdate_url", ""))

            if "重大政策(haveNews )" in selected_tests:
                required_fields["haveNews_url"] = ("重大政策頁連結", st.session_state.get("haveNews_url", ""))

            if "公開資訊(havePublicData )" in selected_tests:
                required_fields["publicdata_url"] = ("公開資訊頁連結", st.session_state.get("publicdata_url", ""))

            if "提供Sitemap.xml文件(Sitemap )" in selected_tests:
                required_fields["sitemap_url"] = ("Sitemap.xml頁連結", st.session_state.get("sitemap_url", ""))

            missing_labels = [label for _, (label, value) in required_fields.items() if not value.strip()]
            if missing_labels:
                st.error("請輸入以下網址（皆為必填）： " + "、".join(missing_labels))
                return

            # URL 對應：即便網域鎖定暫停，仍需為請求提供對應輸入框 URL
            url_overrides = {
                "haveMail": st.session_state.get("havemail_url", "").strip(),
                "navigation_url": st.session_state.get("navigation_url", "").strip(),
                "isUpdateShow": st.session_state.get("isupdate_url", "").strip(),
                "haveNews": st.session_state.get("haveNews_url", "").strip(),
                "havePublicData": st.session_state.get("publicdata_url", "").strip(),
                "Sitemap": st.session_state.get("sitemap_url", "").strip(),
            }

            # 必須使用對應輸入框的端點（不得退回 target_url）
            strict_override_endpoints = {
                "haveMail",
                "navigation_url",
                "isUpdateShow",
                "haveNews",
                "havePublicData",
                "Sitemap",
            }

            # 網域鎖定與格式檢查（暫時停用）
            # target_parsed = urlparse(url_input.strip())
            # if not target_parsed.scheme or not target_parsed.netloc:
            #     st.error("目標網址格式不正確，請輸入含 http/https 的完整網址。")
            #     return
            #
            # target_domain = target_parsed.netloc.lower()
            #
            # endpoint_labels = {
            #     "haveMail": "意見信箱URL",
            #     "classification_url":"內容分類URL (haveClassification)",
            #     "isUpdateShow": "內容更新URL (isUpdateShow / updateFreq / breadcrumb)",
            #     "haveNews": "重大政策URL (haveNews)",
            #     "havePublicData": "公開資訊URL (havePublicData)",
            #     "Sitemap": "提供Sitemap.xml文件URL (Sitemap)",
            # }
            #
            # domain_errors = []
            # for endpoint, override_url in url_overrides.items():
            #     if not override_url:
            #         continue
            #     # 個別欄位格式檢查與網域比對
            #     parsed = urlparse(override_url)
            #     if not parsed.scheme or not parsed.netloc:
            #         domain_errors.append(f"{endpoint_labels.get(endpoint, endpoint)} 格式不正確，請輸入含 http/https 的完整網址。")
            #         continue
            #
            #     if parsed.netloc.lower() != target_domain:
            #         domain_errors.append(
            #             f"{endpoint_labels.get(endpoint, endpoint)} 的網域必須與目標網址相同（{target_domain}）。"
            #         )
            #
            # if domain_errors:
            #     for msg in domain_errors:
            #         st.error(msg)
            #     return

            client = N8nApiClient(is_test=is_test_mode)
            selected_tests = st.session_state["selected_tests"]

            st.markdown("### 檢測結果報告")

            # 建立進度條
            progress_bar = st.progress(0)
            status_text = st.empty()

            # 緩存響應結果（用於合併相同 endpoint 的請求）
            response_cache = {}
            # 追蹤是否已發送過請求（用於判斷是否需要延遲）
            request_sent = False

            # 按照用戶勾選的順序，一個一個檢測並立即顯示結果
            for i, test_name in enumerate(selected_tests):
                status_text.text(f"正在執行: {test_name} ({i+1}/{selected_count})...")

                # 特殊處理：網站導覽功能(navigation) 不需要呼叫 API，直接判定為通過
                if test_name == "網站導覽功能(navigation )":
                    st.markdown(f"#### {test_name}")
                    st.success("測試結果 : 通過")
                    progress_bar.progress((i + 1) / selected_count)
                    time.sleep(0.1)
                    continue

                # 以安全方式取得 endpoint，避免 KeyError
                endpoint = TEST_OPTIONS.get(test_name)
                if endpoint is None:
                    st.error(f"找不到對應的 endpoint: {test_name}")
                    progress_bar.progress((i + 1) / selected_count)
                    time.sleep(0.1)
                    continue

                cache_key = endpoint

                if cache_key not in response_cache:
                    # 如果不是第一個請求，則等待
                    if request_sent:
                        status_text.text(f"等待中... ({i+1}/{selected_count})")
                        time.sleep(15)
                    
                    # 嚴格端點只能用對應輸入框，其餘才可回退 target_url
                    if endpoint in strict_override_endpoints:
                        url = url_overrides.get(endpoint, "")
                    else:
                        url = url_overrides.get(endpoint, "") or url_input

                    try:
                        with st.spinner(f"正在連線至 {endpoint}..."):
                            payload = {"link": url}
                            response = client.call_endpoint(endpoint, data=payload)
                            # 緩存響應結果
                            response_cache[cache_key] = response
                            # 標記已發送請求
                            request_sent = True
                    except Exception as e:
                        # 如果請求失敗，設置錯誤響應
                        response_cache[cache_key] = {"error": str(e), "status": "failed"}
                        # 標記已發送請求
                        request_sent = True

                # 顯示測試項目標題
                st.markdown(f"#### {test_name}")

                # 從緩存中獲取響應並顯示結果
                if cache_key in response_cache:
                    response = response_cache[cache_key]
                    try:
                        display_test_result(endpoint, response, label=test_name)
                    except Exception as e:
                        st.error(f"發生錯誤: {str(e)}")
                else:
                    st.error("無法找到測試結果")

                progress_bar.progress((i + 1) / selected_count)
                time.sleep(0.1)

            status_text.text("所有測試執行完畢。")
            st.success("檢測完成！")
