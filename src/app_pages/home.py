import streamlit as st

def show():
    # 設定頁面樣式 (CSS)
    st.markdown("""
        <style>
        /* 強制設定背景色為深色 (若全域未設定) */
        .stApp {
            background-color: #0e1117;
            color: #fafafa;
        }
        
        /* 標題樣式 */
        .main-title {
            font-family: 'Inter', sans-serif;
            font-size: 3.5rem;
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #00d2ff, #3a7bd5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 100rem;
            text-align: center;
        }
        
        /* 說明文字容器 */
        .description-wrapper {
            display: flex;
            justify-content: center;
            width: 100%;
            margin-top: 2rem;
        }

        /* 說明文字樣式 */
        .description-text {
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            color: #b0b8c4;
            text-align: center;
            max-width: 800px;
            line-height: 1.6;
            margin: 0;
        }
        
        /* 按鈕容器置中 */
        .button-container {
            display: flex;
            justify-content: center;
            margin-bottom: 4rem;
        }
        
        /* 版本資訊樣式 */
        .version-footer {
            text-align: center;
            color: #4b5563;
            font-size: 0.9rem;
            margin-top: 5rem;
            border-top: 1px solid #1f2937;
            padding-top: 2rem;
        }
        
        /* 裝飾性光暈 */
        .glow-effect {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(58, 123, 213, 0.1) 0%, rgba(0, 0, 0, 0) 70%);
            z-index: -1;
            pointer-events: none;
        }
        </style>
    """, unsafe_allow_html=True)

    # 頁面佈局容器
    with st.container():
        # 裝飾背景
        st.markdown('<div class="glow-effect"></div>', unsafe_allow_html=True)
        
        # 空白佔位，讓內容垂直置中一點
        st.markdown('<div style="height: 20vh;"></div>', unsafe_allow_html=True)
        
        # 歡迎標題
        st.markdown('<h1 class="main-title">歡迎使用 Web Diagnostic System</h1>', unsafe_allow_html=True)
        
        # 說明文字
        st.markdown(
            '<div class="description-wrapper"><p class="description-text">本系統協助檢測網站品質，例如 無障礙、W3C 標準等。<br>透過自動化工具，快速掌握網站狀況。</p></div>', 
            unsafe_allow_html=True
        )
        
        # # 開始使用按鈕
        # # 使用 columns 來置中按鈕
        # col1, col2, col3 = st.columns([1, 1, 1])
        # with col2:
        #     if st.button("開始使用 ", use_container_width=True):
        #         st.session_state["current_page"] = "Run"
        #         st.rerun()

        # 版本資訊
        st.markdown('<div class="version-footer">v1.0</div>', unsafe_allow_html=True)
