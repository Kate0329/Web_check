import requests
import json
from typing import Optional, Dict, Any

class N8nApiClient:
    def __init__(self, base_url: str = "http://youth.econcord.com.tw:8080/webhook", is_test: bool = False):
        self.base_url = base_url.rstrip('/')
        if is_test:
            self.base_url += "-test"

    def _make_request(self, endpoint: str, method: str = "POST", data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        處理實際請求邏輯的內部方法。
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, params=data)
            else:
                response = requests.post(url, json=data)
            
            response.raise_for_status()
            
            try:
                return response.json()
            except (ValueError, json.JSONDecodeError):
                # 如果回應不是 JSON 格式，回傳原始文字
                return {"raw_text": response.text, "status": "success_non_json"}
                
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status": "failed"}

    def call_endpoint(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        呼叫 n8n webhook 任何端點的通用方法。
        """
        print(endpoint)
        return self._make_request(endpoint, method="POST", data=data)

    # W3C_Html
    def check_w3c_html(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("W3CHtml", {"link": link})
    
    # W3C_Css
    def check_w3c_css(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("W3CCss", {"link": link})

    # 有效連結
    def check_valid_link(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("validLink", {"link": link})
    
    # 網速檢測
    def check_pageSpeed(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("pageSpeed", {"link": link})

    # 語系編碼檢測
    def check_lang(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("lang", {"link": link})

    # 加密連結檢測
    def check_https(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("https", {"link": link})
    
    # 響應式設計檢測
    def check_rwd(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("RWD", {"link": link})
    
    # 網站圖示檢測
    def check_favicon(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("favicon", {"link": link})

    # 流量統計檢測
    def check_web_analysis(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("WebAnalysis", {"link": link})

    # 網頁動畫檢測
    def check_Animation(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("Animation", {"link": link})

    # 無障礙檢測
    def check_accessibility(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("accessibility", {"link": link})

    # 網站名稱或標誌
    def check_Screenshot(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("Screenshot", {"link": link})

    # 網站無障礙標章
    def check_Screenshot(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("Screenshot", {"link": link})

    # 網站資料開放宣告
    def check_Screenshot(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("Screenshot", {"link": link})

    # 隱私權及資訊安全宣告
    def check_Screenshot(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("Screenshot", {"link": link})

    # 完整通訊地址
    def check_address(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("address", {"link": link})

    # 聯絡電話
    def check_Screenshot(self, link: str) -> Dict[str, Any]:
        return self.call_endpoint("Screenshot", {"link": link})

    # 網站具備多語言版本
    def check_Screenshot(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("Screenshot", {"link": link})

    # 頁尾設計
    def check_footer(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("footer", {"link": link})

    # 網站導覽功能
    def check_Screenshot(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("Screenshot", {"link": link})

    # 提供Sitemap.xml文件
    def check_Sitemap(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("Sitemap", {"link": link})

    # 提供路徑導覽列
    def check_breadcrumb(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("isUpdateShow", {"link": link})

    # 重大政策
    def check_haveNews(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("haveNews", {"link": link})

    # 資訊圖像化
    def check_Screenshot(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("Screenshot", {"link": link})

    # 公開資訊
    def check_havePublicData(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("havePublicData", {"link": link})

    # 內容分類
    def check_haveClassification(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("haveClassification", {"link": link})

    # 相關連結
    def check_haveRelatedLink(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("haveClassification", {"link": link})

    # 內容更新
    def check_isUpdateShow(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("isUpdateShow", {"link": link})

    # 更新頻率
    def check_updateFreq(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("isUpdateShow", {"link": link})

    # 搜尋服務
    def check_haveSearch(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("Screenshot", {"link": link})

    # 熱門關鍵字
    def check_searchKey(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("GA", {"link": link})

    # 搜尋建議
    def check_searchSug(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("GA", {"link": link})

    # 意見信箱
    def check_haveMail(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("haveMail", {"link": link})

    # 社群分享
    def check_Screenshot(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("Screenshot", {"link": link})

    # 社群互動
    def check_Screenshot(self, link: str) -> Dict[str, Any]:  
        return self.call_endpoint("Screenshot", {"link": link})