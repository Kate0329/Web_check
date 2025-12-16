import streamlit as st

# 定義可用的測試項目
TEST_OPTIONS = {
    "檢查連結 (validLink)": "validLink",
    "W3C HTML 檢查 (W3CHtml)": "W3CHtml",
    "W3C CSS 檢查 (W3CCss)": "W3CCss",
    "網速檢測 (pageSpeed)": "pageSpeed",
    "語系編碼檢測 (lang)": "lang",
    "加密連結檢測 (https)": "https",
    "響應式設計檢測 (RWD)": "RWD",
    "網站圖示檢測 (Favicon)": "favicon",
    "流量統計檢測 (WebAnalysis)": "WebAnalysis",
    "網頁動畫 (Animation)": "Animation",
    "無障礙檢測 (accessibility)": "accessibility"
}

def parse_w3c_response(response):
    """解析 W3C 相關的測試結果"""
    # 處理列表包覆的情況
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]

    if isinstance(main_data, dict) and "output" in main_data:
        output = main_data["output"]
        # 檢查 html 或 css
        result_data = output.get("html") or output.get("css")
        
        if result_data and "passed" in result_data:
            passed = result_data["passed"]
            error_count = result_data.get("errorCount", 0)
            return True, passed, error_count
            
    return False, False, 0

def parse_link_response(response):
    """解析連結檢查的測試結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]

    if isinstance(main_data, dict) and "output" in main_data:
        output = main_data["output"]
        result_data = output.get("links")
        
        if result_data and "passed" in result_data:
            passed = result_data["passed"]
            broken_count = result_data.get("broken", 0)
            return True, passed, broken_count
            
    return False, False, 0

def parse_page_speed_response(response):
    """解析網速檢測的測試結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]

    if isinstance(main_data, dict):
        # 檢查是否有 pageSpeed 欄位或是 mobile/desktop 欄位
        if "pageSpeed" in main_data or "mobile" in main_data:
            mobile = main_data.get("mobile", "N/A")
            desktop = main_data.get("desktop", "N/A")
            average = main_data.get("average", "N/A")
            return True, mobile, desktop, average
            
    return False, 0, 0, 0

def parse_lang_response(response):
    """解析語系編碼檢測結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        if "charset" in main_data:
            return True, main_data["charset"]
    return False, None

def parse_https_response(response):
    """解析加密連結檢測結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        if "isEncrypted" in main_data:
            return True, main_data["isEncrypted"], main_data.get("message", "")
    return False, False, ""

def parse_simple_response(response, key):
    """解析簡單的測試結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
        
    if isinstance(main_data, dict):
        if "output" in main_data and key in main_data["output"]:
            data = main_data["output"][key]
            if isinstance(data, dict) and "passed" in data:
                return True, data["passed"]
    return False, False

def parse_rwd_response(response):
    """解析 RWD 測試結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        # 檢查是否有 hasThreeMedias (新格式)
        if "hasThreeMedias" in main_data:
            return True, main_data["hasThreeMedias"]
            
        # 檢查標準格式 
        if "output" in main_data:
            output = main_data["output"]
            rwd_data =  output.get("RWD")
            if rwd_data and "passed" in rwd_data:
                return True, rwd_data["passed"]
                
    return False, False

def parse_favicon_response(response):
    """解析 Favicon 測試結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        # 檢查是否有 favicon 欄位且不為空
        if "favicon" in main_data and main_data["favicon"]:
            return True, True, main_data["favicon"]
            
    return False, False, None

def parse_web_analysis_response(response):
    """解析流量統計檢測結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        if "hasAnalytics" in main_data:
            passed = main_data["hasAnalytics"]
            tools = []
            if "detectedTools" in main_data and isinstance(main_data["detectedTools"], dict):
                for tool_name, is_detected in main_data["detectedTools"].items():
                    if is_detected:
                        tools.append(tool_name)
            return True, passed, tools
            
    return False, False, []

def parse_accessibility_response(response):
    """解析無障礙檢測結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        if "hasAccessibility" in main_data:
            return True, main_data["hasAccessibility"]
            
    return False, False

def parse_animation_response(response):
    """解析網頁動畫檢測結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        if "hasFlashAnimation" in main_data:
            # hasFlashAnimation=True 代表有動畫 -> 未通過
            # hasFlashAnimation=False 代表無動畫 -> 通過
            return True, not main_data["hasFlashAnimation"]
            
    return False, False

def display_test_result(endpoint, response):
    """根據 Endpoint 顯示不同的測試結果"""
    
    # 1. W3C 檢查 (HTML & CSS)
    if endpoint in ["W3CHtml", "W3CCss"]:
        is_w3c, passed, error_count = parse_w3c_response(response)
        if is_w3c:
            if passed:
                st.success("測試結果 : 通過")
            else:
                st.error("測試結果 : 未通過")
                st.markdown(f"**不合格 :** {error_count}")
            
            # 顯示詳細資料 (預設摺疊)
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 2. 連結檢查 (validLink)
    if endpoint == "validLink":
        is_valid, passed, broken_count = parse_link_response(response)
        if is_valid:
            if passed:
                st.success("測試結果 : 通過")
            else:
                st.error("測試結果 : 未通過")
                st.markdown(f"**不合格 :** {broken_count}")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 3. 網速檢測 (pageSpeed)
    if endpoint == "pageSpeed":
        is_speed, mobile, desktop, average = parse_page_speed_response(response)
        if is_speed:
            st.success("測試結果 : 通過")
            st.markdown(f"**行動版 :** {mobile}")
            st.markdown(f"**電腦版 :** {desktop}")
            st.markdown(f"**平均 :** {average}")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 4. 語系編碼檢測 (lang)
    if endpoint == "lang":
        is_parsed, charset = parse_lang_response(response)
        if is_parsed:
            st.success("測試結果 : 通過")
            st.markdown(f"**語系編碼 :** {charset}")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 5. 加密連結檢測 (https)
    if endpoint == "https":
        is_parsed, is_encrypted, message = parse_https_response(response)
        if is_parsed:
            if is_encrypted:
                st.success("測試結果 : 通過")
                st.markdown(f"**加密說明 :** {message}")
            else:
                st.error("測試結果 : 未通過")
                if message:
                    st.markdown(f"**加密說明 :** {message}")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 6. 響應式設計檢測 (RWD)
    if endpoint == "RWD":
        is_parsed, passed = parse_rwd_response(response)
            
        if is_parsed:
            if passed:
                st.success("測試結果 : 通過")
            else:
                st.error("測試結果 : 未通過")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return
        
    # 7. 網站圖示檢測 (Favicon)
    if endpoint == "favicon":
        is_parsed, passed, favicon_url = parse_favicon_response(response)

        if is_parsed:
            if passed:
                st.success("測試結果 : 通過")
                st.markdown(f"**favicon :** {favicon_url}")
            else:
                st.error("測試結果 : 未通過")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return
    
    # 8. 流量統計(WebAnalysis)
    if endpoint == "WebAnalysis":
        is_parsed, passed, tools = parse_web_analysis_response(response)
        
        if is_parsed:
            if passed:
                st.success("測試結果 : 通過")
                tools_str = "、".join(tools) if tools else "無"
                st.markdown(f"**流量統計工具 :** {tools_str}")
            else:
                st.error("測試結果 : 未通過")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 9. 網頁動畫 (Animation)
    if endpoint == "Animation":
        is_parsed, passed = parse_animation_response(response)
        
        if is_parsed:
            if passed:
                st.success("測試結果 : 通過")
            else:
                st.error("測試結果 : 未通過")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 10. 無障礙檢測 (accessibility)
    if endpoint == "accessibility":
        is_parsed, passed = parse_accessibility_response(response)
        
        if is_parsed:
            if passed:
                st.success("測試結果 : 通過")
            else:
                st.error("測試結果 : 未通過")
            
            with st.expander("查看詳細 JSON 結果", expanded=False):
                st.json(response)
            return

    # 11. 其他測試 (預設顯示方式)
    if isinstance(response, list):
        st.success("請求成功! (收到列表資料)")
        with st.expander("查看詳細 JSON 結果", expanded=True):
            st.json(response)
    elif isinstance(response, dict):
        if "error" in response and response.get("status") == "failed":
            st.error(f"請求失敗: {response['error']}")
        elif "raw_text" in response and response.get("status") == "success_non_json":
            st.success("請求成功 (非 JSON 回應)!")
            with st.expander("查看原始回應"):
                st.code(response["raw_text"])
        else:
            st.success("請求成功!")
            with st.expander("查看詳細 JSON 結果", expanded=True):
                st.json(response)
    else:
        st.warning(f"收到未預期的資料型別: {type(response)}")
        st.write(response)
