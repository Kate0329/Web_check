# N8n API Frontend

這是一個使用 Streamlit 建立的前端應用程式，用於連接 n8n Webhook API 進行網站檢測。

## 專案結構

- `src/main.py`: Streamlit 主程式入口，處理導航與頁面路由。
- `src/app_pages/`: 包含各個頁面的邏輯。
    - `home.py`: 首頁。
    - `url_setting.py`: 執行檢測頁面 (輸入網址與顯示結果)。
    - `test_selection.py`: 檢測項目設定頁面。
- `src/services/api_client.py`: 封裝 n8n API 呼叫邏輯的類別。
- `src/utils/test_result.py`: 處理測試結果的解析與顯示邏輯。
- `requirements.txt`: 專案依賴套件列表。

## 功能特色

目前支援以下檢測項目：
1.  **基本檢測**: 檢查連結有效性 (validLink)。
2.  **W3C 標準檢測**: HTML 檢查 (W3CHtml)、CSS 檢查 (W3CCss)。
3.  **效能檢測**: 網速檢測 (pageSpeed)，包含行動版與電腦版評分。

## 安裝與執行

本專案使用 `uv` 進行套件管理。

1.  **安裝依賴套件**

    確保你已經在虛擬環境中 (或是讓 uv 自動管理)，執行以下指令：

    ```bash
    uv pip install -r requirements.txt
    ```

2.  **執行應用程式**

    ```bash
    streamlit run src/main.py
    ```
    或
    ```bash
    python -m streamlit run src/main.py
    ```

## 使用方式

1.  **項目勾選**: 進入「項目勾選」頁面，選擇想要執行的測試項目 (設定會自動儲存)。
2.  **執行檢測**: 進入「執行檢測」頁面，輸入目標網址，點擊「開始檢測」。
3.  **查看結果**: 測試結果會依序顯示在下方，包含通過狀態與詳細數據。

## API 設定

預設的 API Base URL 設定於 `src/services/api_client.py`。
程式支援測試模式 (Test Mode)，會自動在 URL 後方加上 `-test`。

## 如何新增檢測項目

若要新增新的檢測功能，請依照以下步驟進行：

1.  **定義測試選項 (`src/utils/test_result.py`)**
    在 `TEST_OPTIONS` 字典中加入新的測試項目名稱與對應的 Endpoint 代碼 (Key)。
    ```python
    TEST_OPTIONS = {
        # ...
        "新測試項目名稱 (NewTest)": "newTestEndpoint"
    }
    ```

2.  **實作結果解析與顯示 (`src/utils/test_result.py`)**
    *   若回傳格式特殊，請新增解析函式 (例如 `parse_new_test_response`)。
    *   在 `display_test_result` 函式中加入對應的 `if endpoint == "newTestEndpoint":` 判斷區塊。
    *   定義如何顯示成功/失敗訊息 (使用 `st.success`, `st.error`) 及詳細數據。

3.  **加入選單勾選 (`src/app_pages/selection.py`)**
    在 `show()` 函式中新增 `st.checkbox`，讓使用者可以勾選此項目。
    ```python
    # 範例
    is_checked = "新測試項目名稱 (NewTest)" in st.session_state["selected_tests"]
    if st.checkbox("新測試項目名稱 (NewTest)", value=is_checked):
        current_selection.append("新測試項目名稱 (NewTest)")
    ```

4.  **API 呼叫設定**
    *   **`src/app_pages/url_setting.py`**: 程式會自動根據 `TEST_OPTIONS` 的 Endpoint 呼叫 API，通常**無需修改**此檔案。
    *   **`src/services/api_client.py` (選用)**: 建議在此檔案中新增對應的 `check_...` 方法，以保持程式碼結構完整。
        ```python
        def check_new_test(self, link: str) -> Dict[str, Any]:
            return self.call_endpoint("newTestEndpoint", {"link": link})
        ```
