import requests
import json
from typing import Optional, Dict, Any

class N8nApiClient:
    def __init__(self, base_url: str = "http://youth.econcord.com.tw:8080/webhook", is_test: bool = True):
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
