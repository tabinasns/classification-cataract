import streamlit as st
import time

# ❗ Hanya di sini kita boleh set page config
st.set_page_config(
    page_title="Klasifikasi Katarak",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Styling splash screen
st.markdown("""
    <style>
        .splash-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            margin-top: 2em;
        }
        .splash-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
            margin-bottom: 2em;
        }
        .loader {
            border: 6px solid #f3f3f3;
            border-top: 6px solid #3498db;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
""", unsafe_allow_html=True)

# Splash screen content
st.markdown('<div class="splash-title">Website Deteksi Katarak</div>', unsafe_allow_html=True)
st.markdown('<div class="splash-subtitle">Menggunakan Model CNN & Citra Fundus Retina</div>', unsafe_allow_html=True)
st.markdown('<div class="loader"></div>', unsafe_allow_html=True)

# Delay splash
time.sleep(3)

# ❗ Redirect manual pakai JavaScript (tanpa switch_page)
st.markdown(
    """<meta http-equiv="refresh" content="0;url=./Beranda">""",
    unsafe_allow_html=True
)
