import streamlit as st
import time
import importlib
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Klasifikasi Katarak",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------- SPLASH SCREEN -------- #
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
            /* Sembunyikan tombol expander sidebar */
        [data-testid="collapsedControl"] {
            display: none;
        }
        .splash-title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            font-family: 'Segoe UI';
            margin-top: 2em;
        }
        .splash-subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
            font-family: 'Segoe UI';
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
        [data-testid="stSidebarNav"]::before {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }   
        [data-testid="stSidebar"] {
            background-color: #33D621;
            border-right: 2px solid #ccc;
        }
        
        [data-testid="stSidebar"] {
            background-color: transparent;
            box-shadow: none;
        }
        [data-testid="stSidebar"] header {
            display: none;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <h3 style='text-align:center;'>🧠 Deteksi Katarak AI</h3>
    <hr style='margin-top: 0.5em; margin-bottom: 1em;'>
    """, unsafe_allow_html=True
)

st.markdown('<div class="splash-title">Website Deteksi Katarak</div>', unsafe_allow_html=True)
st.markdown('<div class="splash-subtitle">Menggunakan Model CNN & Citra Fundus Retina</div>', unsafe_allow_html=True)
st.markdown('<div class="loader"></div>', unsafe_allow_html=True)

# Delay 3 detik (waktu splash screen)
time.sleep(3)

# Redirect ke halaman beranda
switch_page("1_beranda")