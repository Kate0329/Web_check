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
    "無障礙檢測 (accessibility)": "accessibility",
    "網站名稱或標誌(logo)": "Screenshot",
    "網站資料開放宣告(dataUsagePolicy)": "Screenshot",
    "隱私權及資訊安全宣告(privacyPolicy)": "Screenshot",
    "完整通訊地址(address)": "address",
    "聯絡電話(phone)": "Screenshot",
    "網站具備多語言版本(lang)": "Screenshot",
    "頁尾設計(footer)": "Screenshot",
    "網站導覽功能(navigation )": "Screenshot",
    "提供Sitemap.xml文件(Sitemap )": "Sitemap",
    "提供路徑導覽列(breadcrumb )": "isUpdateShow",
    "重大政策(haveNews )": "haveNews",
    "資訊圖像化(haveGraphic )": "Screenshot",
    "公開資訊(havePublicData )": "havePublicData",
    "內容分類(haveClassification )": "haveClassification",
    "相關連結(haveRelatedLink )": "haveClassification",
    "內容更新(isUpdateShow )": "isUpdateShow",
    "更新頻率(updateFreq )": "isUpdateShow",
    "搜尋服務(haveSearch )": "Screenshot",
    "熱門關鍵字(searchKey )": "GA",
    "搜尋建議(searchSug )": "GA",
    "意見信箱(haveMail )": "haveMail",
    "社群分享(haveShare )": "Screenshot",
    "社群互動(comunity )": "Screenshot"
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
            elif isinstance(data, bool):
                return True, data
        elif key in main_data:
            data = main_data[key]
            if isinstance(data, bool):
                return True, data
            elif isinstance(data, dict) and "passed" in data:
                return True, data["passed"]
    return False, False

def parse_boolean_response(response, key):
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    else:
        main_data = response
    
    if not isinstance(main_data, dict):
        return None
    
    if key in main_data:
        data = main_data[key]
        if isinstance(data, bool):
            return data
        elif isinstance(data, dict) and "passed" in data:
            return data["passed"]
    
    # 嘗試忽略大小寫和空格的匹配
    key_lower = key.lower().strip()
    for k, v in main_data.items():
        if k.lower().strip() == key_lower:
            if isinstance(v, bool):
                return v
            elif isinstance(v, dict) and "passed" in v:
                return v["passed"]
    
    # 然後檢查 output[key]
    if "output" in main_data and isinstance(main_data["output"], dict):
        if key in main_data["output"]:
            data = main_data["output"][key]
            if isinstance(data, bool):
                return data
            elif isinstance(data, dict) and "passed" in data:
                return data["passed"]
        
        # 嘗試忽略大小寫和空格的匹配
        for k, v in main_data["output"].items():
            if k.lower().strip() == key_lower:
                if isinstance(v, bool):
                    return v
                elif isinstance(v, dict) and "passed" in v:
                    return v["passed"]
    
    # 如果 response 是列表，遍歷所有元素查找
    if isinstance(response, list):
        for item in response:
            if isinstance(item, dict):
                # 優先檢查根層級
                if key in item:
                    data = item[key]
                    if isinstance(data, bool):
                        return data
                    elif isinstance(data, dict) and "passed" in data:
                        return data["passed"]
                
                # 嘗試忽略大小寫和空格的匹配
                key_lower = key.lower().strip()
                for k, v in item.items():
                    if k.lower().strip() == key_lower:
                        if isinstance(v, bool):
                            return v
                        elif isinstance(v, dict) and "passed" in v:
                            return v["passed"]
                
                # 然後檢查 output
                if "output" in item and isinstance(item["output"], dict):
                    if key in item["output"]:
                        data = item["output"][key]
                        if isinstance(data, bool):
                            return data
                        elif isinstance(data, dict) and "passed" in data:
                            return data["passed"]
                    
                    # 嘗試忽略大小寫和空格的匹配
                    for k, v in item["output"].items():
                        if k.lower().strip() == key_lower:
                            if isinstance(v, bool):
                                return v
                            elif isinstance(v, dict) and "passed" in v:
                                return v["passed"]
    
    return None

def _extract_key_from_label(lbl: str):
    if not lbl or "(" not in lbl:
        return None
    try:
        start = lbl.index("(") + 1
        end = lbl.index(")", start)
        return lbl[start:end].strip()
    except Exception:
        return None

def display_simple_boolean_result(response, key, label=None):
    if not key and label:
        extracted = _extract_key_from_label(label)
        if extracted:
            key = extracted
    
    if not key:
        return False
    
    result = parse_boolean_response(response, key)
    
    if result is None:
        def search_recursive(obj, search_key):
            if isinstance(obj, dict):
                if search_key in obj:
                    val = obj[search_key]
                    if isinstance(val, bool):
                        return val
                for v in obj.values():
                    found = search_recursive(v, search_key)
                    if found is not None:
                        return found
            elif isinstance(obj, list):
                for item in obj:
                    found = search_recursive(item, search_key)
                    if found is not None:
                        return found
            return None
        
        result = search_recursive(response, key)

    if result is None:
        def extract_all_booleans(obj):
            booleans = {}
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, bool):
                        booleans[k] = v
                    elif isinstance(v, (dict, list)):
                        nested = extract_all_booleans(v)
                        booleans.update(nested)
            elif isinstance(obj, list):
                for item in obj:
                    if isinstance(item, dict):
                        nested = extract_all_booleans(item)
                        booleans.update(nested)
            return booleans
        
        all_booleans = extract_all_booleans(response)
        key_lower = key.lower().strip()
        for k, v in all_booleans.items():
            if k.lower().strip() == key_lower:
                result = v
                key = k  # 使用實際找到的 key
                break
    
    # 如果還是找不到，顯示調試信息（臨時用於找出問題）
    if result is None:
        # 臨時調試：顯示實際的 JSON 結構
        st.warning(f"⚠️ 找不到欄位 '{key}'，請檢查 JSON 結構")
        with st.expander("🔍 調試：查看實際 JSON 回應", expanded=False):
            st.json(response)
        return False
    
    # 顯示測試結果
    if result:
        st.success("測試結果 : 通過")
    else:
        st.error("測試結果 : 未通過")
    
    # 顯示簡化的 JSON
    with st.expander("查看詳細 JSON 結果", expanded=False):
        st.json({key: result})
    
    return True

def parse_rwd_response(response):
    """解析 RWD 測試結果"""
    main_data = response
    if isinstance(response, list) and len(response) > 0:
        main_data = response[0]
    
    if isinstance(main_data, dict):
        # 優先檢查是否有 hasRWD (對應截圖格式)
        if "hasRWD" in main_data:
            return True, main_data["hasRWD"], main_data.get("totalMediaQueries", 0)

        # 檢查是否有 hasThreeMedias (新格式)
        if "hasThreeMedias" in main_data:
            return True, main_data["hasThreeMedias"], 0
            
        # 檢查標準格式 
        if "output" in main_data:
            output = main_data["output"]
            rwd_data =  output.get("RWD")
            if rwd_data and "passed" in rwd_data:
                return True, rwd_data["passed"], 0
                
    return False, False, 0

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

def display_test_result(endpoint, response, label=None):
    
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
        is_parsed, passed, total_media = parse_rwd_response(response)
            
        if is_parsed:
            if passed:
                st.success("測試結果 : 通過")
            else:
                st.error("測試結果 : 未通過")
            
            st.markdown(f"**Totalmedia :** {total_media}")
            
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

    # 11. 錯誤處理
    if isinstance(response, dict):
        if "error" in response and response.get("status") == "failed":
            st.error(f"請求失敗: {response['error']}")
            return

    # 12. 多項共用 Screenshot 的輸出
    screenshot_like_keys = {
        "logo",
        "dataUsagePolicy",
        "privacyPolicy",
        "phone",
        "lang",
        "footer",
        "navigation",
        "haveGraphic",
        "haveSearch",
        "haveShare",
        "comunity"
    }

    # endpoint == "Screenshot" 或 screenshot_like_keys
    target_key = None
    if endpoint in screenshot_like_keys:
        target_key = endpoint
    elif endpoint == "Screenshot":
        target_key = _extract_key_from_label(label)

    if target_key:
        if display_simple_boolean_result(response, target_key):
            return

    # 13. 完整通訊地址 (address) 
    if endpoint == "address":
        if display_simple_boolean_result(response, "zipcodeMatch"):
            return


    # 14. 提供Sitemap.xml文件 (Sitemap) 
    if endpoint == "Sitemap":
        if display_simple_boolean_result(response, "sitemap"):
            return

    # 15. 提供路徑導覽列/內容更新/更新頻率 (isUpdateShow)
    if endpoint == "isUpdateShow":
        target_key = None
        if label and "(" in label and ")" in label:
            target_key = _extract_key_from_label(label)
        
        if not target_key:
            target_key = "isUpdateShow"
        
        if display_simple_boolean_result(response, target_key):
            return

    # 16. 重大政策 (haveNews) 
    if endpoint == "haveNews":
        if display_simple_boolean_result(response, "haveNews"):
            return

    # 17. 公開資訊 (havePublicData) 
    if endpoint == "havePublicData":
        if display_simple_boolean_result(response, "havePublicData"):
            return

    # 18. 內容分類 (haveClassification) 
    if endpoint == "haveClassification":
        field_name = "haveRelatedLink" if (label and "相關連結" in label) else "haveClassification"
        if display_simple_boolean_result(response, field_name):
            return

    # 19. 熱門關鍵字 & 搜尋建議 (GA endpoint)
    if endpoint == "GA":
        field_name = "searchKey" if (label and "熱門關鍵字" in label) else "searchSug"
        if display_simple_boolean_result(response, field_name):
            return

    # 20. 意見信箱 (haveMail) 
    if endpoint == "haveMail":
        if display_simple_boolean_result(response, "haveMail"):
            return
