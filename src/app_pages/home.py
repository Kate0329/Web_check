import streamlit as st

def show():
    # 1. 注入自定義 CSS (專業版樣式)
    st.markdown("""
        <style>
        /* 全局字體設定 */
        .stApp {
            background-color: #f4f6f9; /* 企業級淺灰背景 */
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        
        /* 標題樣式 */
        .dashboard-header {
            font-size: 2rem;
            color: #2c3e50;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
        .dashboard-subheader {
            font-size: 1rem;
            color: #7f8c8d;
            margin-bottom: 2rem;
        }

        /* 專業卡片樣式 */
        .pro-card {
            background-color: white;
            padding: 24px;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
            border-left: 5px solid #3498db; /* 左側藍色強調線 */
            margin-bottom: 20px;
            transition: all 0.3s cubic-bezier(.25,.8,.25,1);
        }
        .pro-card:hover {
            box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
        }
        
        /* 卡片標題與內容 */
        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 12px;
            letter-spacing: 0.5px;
        }
        .card-desc {
            font-size: 0.95rem;
            color: #57606f;
            line-height: 1.6;
        }
        
        /* 輔助卡片 (灰色樣式) */
        .pro-card-secondary {
            border-left-color: #bdc3c7;
            background-color: #ffffff;
            opacity: 0.8;
        }

        /* 狀態指標區塊 */
        .metric-box {
            background: white;
            padding: 15px;
            border-radius: 6px;
            text-align: center;
            border: 1px solid #dfe6e9;
        }
        .metric-value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #2c3e50;
        }
        .metric-label {
            font-size: 0.8rem;
            color: #95a5a6;
            text-transform: uppercase;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. 頁面標題區
    st.markdown('<div class="dashboard-header">Web Diagnostic System</div>', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-subheader">網站健康度自動化診斷系統</div>', unsafe_allow_html=True)

    # 3. 系統狀態指標
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="metric-box"><div class="metric-value">Online</div><div class="metric-label">System Status</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-box"><div class="metric-value">Secure</div><div class="metric-label">Connection</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-box"><div class="metric-value">v1.0</div><div class="metric-label">Version</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="metric-box"><div class="metric-value">Ready</div><div class="metric-label">Scanner</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 4. 功能區塊
    st.markdown("#### 系統模組 System Modules")

    # 主要功能卡片
    col_main, col_placeholder = st.columns([0.6, 0.4])

    with col_main:
        st.markdown("""
        <div class="pro-card">
            <div class="card-title">全面檢測 (Full Inspection)</div>
            <div class="card-desc">
                執行完整的 N8n 節點連線測試。支援批次勾選項目，針對 Credential 與 Workflow 進行深度驗證，並生成詳細的狀態報告。
                <br><br>
                <strong>適用情境：</strong> 定期巡檢、部署前驗證、故障排除。
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_placeholder:
        # 佔位功能 (顯示系統未來的擴充性，同時填補版面)
        st.markdown("""
        <div class="pro-card pro-card-secondary">
            <div class="card-title">自動排程 (Coming Soon)</div>
            <div class="card-desc">
                定時自動執行檢測任務，並透過 Email 或 Slack 發送異常通知。<br>
                <i>此功能目前正在開發中。</i>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 5. 底部資訊
    st.markdown(
        """
        <div style='margin-top: 50px; padding-top: 20px; border-top: 1px solid #dfe6e9; text-align: center; color: #b2bec3; font-size: 0.8rem;'>
        &copy; 2024 N8n Monitoring System. Internal Use Only.
        </div>
        """, 
        unsafe_allow_html=True
    )
