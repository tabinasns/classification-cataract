import streamlit as st

st.set_page_config(page_title="Beranda", initial_sidebar_state="collapsed", layout="wide")

from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page

# --------- CSS -------------- #
st.markdown("""
    <style>
        .p {
            font-size: 16px
            color: #4a4a4a;
            line-height: 1.6;
            }
        .hover-pop {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .hover-pop:hover {
            transform: scale(1.0);
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
        }
        .gradient-card {
            border-radius: 16px;
            padding: 1.5em 1em 1em 1em;
            color: #333333;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1.2em;
            background: linear-gradient(100deg, #FFFFFF 0%, #E7F4FF 100%);
            box-shadow: 0 2px 12px rgba(140,140,140,0.07);
        }
        .gradient-card2 {
            border-radius: 16px;
            padding: 1.5em 1em 1em 1em;
            color: #333333;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1.2em;
            background: linear-gradient(100deg, #FFFFFF 10%, #FFDBDF 100%);
            box-shadow: 0 2px 12px rgba(140,140,140,0.07);
        }
        .gradient-card3 {
            border-radius: 16px;
            padding: 1.5em 1em 1em 1em;
            color: #333333;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1.2em;
            background: linear-gradient(100deg, #FFFFFF 10%, #FFE3C1 100%);
            box-shadow: 0 2px 12px rgba(140,140,140,0.07);
        }
        .info-wrapper {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: flex-start;
            gap: 20px;
            margin-bottom: 40px;
        }

        .info-text, .info-image {
            flex: 1 1 300px;
            max-width: 48%;
        }

        .info-image img {
            width: 100%;
            max-width: 420px;
            border-radius: 10px;
            display: block;
            margin: 0 auto;
        }
        .card-wrapper {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            margin-top: 1.5em;
        }
        .card-item {
            flex: 1 1 280px;
        }
        div.stButton > button {
            background: linear-gradient(100deg, #FFFFFF 0%, #E7F4FF 100%);
            color: #3b6cb7;
            border: 2px solid #dbe9ff;
            border-radius: 12px;
            padding: 0.6em 1.5em;
            font-size: 1.05rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }

        div.stButton > button:hover {
            background: linear-gradient(100deg, #d0e9ff 0%, #b8dfff 100%);
            color: #2a4f99;
            transform: scale(1.03);
            box-shadow: 0 6px 16px rgba(0,0,0,0.12);
        }
        /* Responsif untuk layout dua kolom */
        @media (max-width: 768px) {
            .st-emotion-cache-1k0cxxh, .st-emotion-cache-13ln4jf {
                flex-direction: column !important;
            }
            .st-emotion-cache-1k0cxxh > div, .st-emotion-cache-13ln4jf > div {
                width: 100% !important;
                margin-bottom: 1rem;
            }
            .info-text, .info-image {
                max-width: 100%;
            }
            .info-wrapper {
                flex-direction: column;
            }
            .card-wrapper {
                flex-direction: column;
                align-items: center;
            }
        }

        /* Atur padding dan ukuran teks agar lebih nyaman di mobile */
        @media (max-width: 576px) {
            h3, h4 {
                font-size: 1.1rem !important;
            }
            p {
                font-size: 0.95rem !important;
                line-height: 1.5 !important;
            }
        }
    </style>
""", unsafe_allow_html= True)

# --------- EKSTRAK GAMBAR -------------- #
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_string}"

indonesia = get_base64_image("aset/indonesia.png")
fundus = get_base64_image("aset/fundus.png")


# ---------- HALAMAN BERANDA ---------- #
# ---------- SECTION: PARAGRAF PEMBUKA ---------- #
st.markdown("""<h2 style="font-family: 'Segoe UI;">Selamat Datang di Website Deteksi Katarak</h2>""", unsafe_allow_html=True)
st.markdown(
    """
        <p style='font-size: 18px; padding-bottom: 60px'>
            Deteksi katarak kini semakin mudah melalui pemanfaatan teknologi berbasis citra fundus. 
            Website ini menjadi bagian dari inovasi dalam bidang kesehatan mata untuk mendukung 
            diagnosis awal yang akurat dan terpercaya. Website ini bertujuan untuk membantu 
            diagnosis katarak melalui analisis citra fundus mata.
        </p>
    """, unsafe_allow_html=True)


# ---------- SECTION: INFORMASI EDUKATIF ---------- #
st.markdown("""
<div class="info-wrapper">
    <div class="info-text">
        <h3 style="font-family: 'Segoe UI'; margin-top:3%;">Penyebab Kebutaan Tertinggi</h3>
        <p style="font-size: 18px; font-family: 'Segoe UI';">
            Katarak adalah penyebab kebutaan nomor satu di dunia. 
            Di Indonesia, populasi usia 50 tahun keatas diketahui mengalami kebutaan mencapai 3% dan katarak menjadi penyebab 
            tertinggi kebutaan sebesar 81% berdasarkan data nasional survei kebutaan Rapid Assessment of Avoidable Blindness (RAAB) pada tahun 2018.
            Dengan deteksi dini dapat mencegah kerusakan lebih lanjut pada penglihatan. 
            Teknologi berbasis AI kini bisa membantu mengidentifikasi katarak hanya dari citra fundus.
        </p>
    </div>
    <div class="info-image">
        <img src="{0}" alt="indonesia">
    </div>
</div>
""".format(indonesia), unsafe_allow_html=True)

st.markdown("""
<div class="info-wrapper">
    <div class="info-image">
        <img src="{0}" alt="fundus">
    </div>
    <div class="info-text">
        <h3 style="font-family: 'Segoe UI'; margin-top:3%;">Mengapa Citra Fundus?</h3>
        <p style="font-size: 18px; font-family: 'Segoe UI';">
            Citra fundus bisa menjadi second option untuk mendeteksi 
            katarak karena dapat memvisualisasikan bagian belakang mata 
            yang dapat dimanfaatkan untuk mendeteksi katarak secara non-invasif 
            dan cepat. Penggunaan citra fundus dapat lebih mudah dan relatif terjangkau.  
            Didukung oleh kecerdasan buatan (AI), website klasifikasi ini dirancang untuk membantu dokter dan tenaga medis dalam menganalisis citra fundus secara lebih efisien. 
        </p>
    </div>
</div>
""".format(fundus), unsafe_allow_html=True)
    
    
# ---------- SECTION: 3 CARD ---------- #
st.markdown("### Alat Deteksi Populer")

st.markdown("""
<div class="card-wrapper">
    <div class="gradient-card hover-pop card-item">
        <h4>🎯 Model Teruji</h4>
        <p>Didukung model CNN MobileNet yang telah melalui proses pelatihan dan evaluasi mendalam.</p>
    </div>
    <div class="gradient-card2 hover-pop card-item">
        <h4>⚡ Prediksi Seketika</h4>
        <p>Model memberikan hasil klasifikasi hanya dalam beberapa detik tanpa perlu tunggu lama.</p>
    </div>
    <div class="gradient-card3 hover-pop card-item">
        <h4>🔒 Privasi Terjaga</h4>
        <p>Data aman tidak disimpan, hanya digunakan untuk proses klasifikasi sementara.</p>
    </div>
</div>
""", unsafe_allow_html=True)

_, col, _ = st.columns([1, 2, 1])
with col:
    if st.button("🔍 Coba Deteksi", key="to_deteksi", use_container_width=True):
        switch_page("2_deteksi")


# if st.button("Coba Deteksi"):
#     st.query_params["page"] = "Cek Katarak"
#     st.rerun()

# if st.button("🔍 Coba Deteksi Sekarang"):
#     st.switch_page("pages/2_deteksi.py")