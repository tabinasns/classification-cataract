import streamlit as st

st.set_page_config(page_title="Deteksi Katarak", layout="wide")

import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image
import base64

# Load the trained model
# Ubah ini dengan H5 mu Cap! 
model_katarak = load_model('model/model_mobilenet_katarak.keras', compile=False)
model_fundus = load_model('model/model_mobilenet_fundus.keras', compile=False)

# Resize atur juga jgn lupa, samakan dengan model mu make pixel berapa!!
# Fungsi preprocessing untuk CLAHE dan konversi ke grayscale

def preprocessing(img):
    image = np.array(img.resize((180, 180)))
    image = image.astype("float32") / 255.0
    return np.expand_dims(image, axis=0)

def apply_clahe(images):
    
    # Konversi PIL ke NumPy
    image = np.array(images)
    
    # Resize ukuran sesuai input model
    image = cv2.resize(image, (180, 180))
    
    # Ambil channel hijau (jika input masih RGB)
    green = image[:, :, 1]  # Ambil channel hijau dari gambar RGB
    
    # Terapkan CLAHE ke channel hijau
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
    cla = clahe.apply(green)
    
    # Konversi gambar ke grayscale setelah CLAHE
    gray_image = cv2.merge([cla, cla, cla])  # Konversi ke format 3-channel RGB untuk kompatibilitas dengan ImageDataGenerator
    
    # Normalisasi inputan
    normalisasi = gray_image.astype('float32') / 255.0
    
    return normalisasi, gray_image

# Fungsi prediksi 
def predict_cataract(images):
    # Preprocess the image to the required input format of the model
    preprocessing, clahe_image  = apply_clahe(images)
    image = np.expand_dims(preprocessing, axis=0) # Menambahkan channel grayscale

    # Make prediction
    prediction = model_katarak.predict(image)
    return prediction, clahe_image

# ------------------------- STYLE CSS ---------------------------------#
st.markdown("""
            <style>
                body {
                    font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    # color: #333;
                }
                h1 {
                    color: #1a1a1a;
                    font-size: 2.5em; /* Larger title */
                }
                p.instruction {
                    font-size: 1.5em;
                    font-weight: 600;
                    # color: #555;
                }
                .subtitle {
                    font-size: 1.2rem;
                    color: #7b7b7b;
                    text-align: center;
                    font-family: 'Segoe UI';
                    margin-bottom: 2.8em;
                }
                .stExpander {
                    border-radius: 10px; /* More rounded corners */
                    background-color: #ffffff; /* White background */
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* Softer, more pronounced shadow */
                    transition: all 0.3s ease-in-out; /* Smooth transition on hover/open */
                }
                .stExpander:hover {
                    box-shadow: 0 6px 16px rgba(0,0,0,0.12); /* Slightly more shadow on hover */
                }
                .stExpander details summary {
                    font-weight: 600; /* Medium bold */
                    color: #007bff; /* Primary blue for summary */
                    font-size: 1.2em; /* Larger font for expander titles */
                    cursor: pointer;
                    display: flex; /* Use flexbox for icon alignment */
                    align-items: center; /* Center icon vertically */
                }
                .stExpander details summary:hover {
                    color: #0056b3; /* Darker blue on hover */
                }
                .stExpander details[open] summary {
                    color: #0056b3; /* Darker blue when open */
                }
                .stExpander details div {
                    color: #444; /* Slightly darker text for content */
                    font-size: 1em; /* Standard content font size */
                }
                .responsive-image img {
                    max-width: 300px; /* Lebar maksimum yang diizinkan */
                    margin-top: 15px;
                    margin-left: auto;
                    margin-right: auto;
                    height: auto; /* Mempertahankan rasio aspek */
                    display: block; /* Menghilangkan ruang ekstra di bawah gambar */
                }
                .responsive-image-container {{
                    width: 100%;
                    display: flex;
                    margin-bottom: 20px;
                    justify-content: center;
                    align-items: center;
                }}
                .responsive-image-container img {{
                    max-width: 100%;
                    height: auto;
                    display: block;
                    margin-top: 15px;
                }}
                .card {
                    background-color: #f9f9f9;
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                }
                .card:hover{
                    box-shadow: 0 6px 16px rgba(0,0,0,0.12); /* Slightly more shadow on hover */
                }
                .title {
                    font-weight: 600;
                    font-size: 16px;
                    color: #333;
                    margin-bottom: 10px;
                }
                .value {
                    background-color: #e7edff;
                    padding: 6px 12px;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: bold;
                    color: #3b6cb7;
                    display: inline-block;
                }
                .value2 {
                    background-color: #CFFFC5;
                    padding: 6px 12px;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: bold;
                    color: #33D621;
                    display: inline-block;
                }
                .info-label {
                    font-weight: 600;
                    margin-bottom: 5px;
                }
                /* CSS untuk Kolom Konten (Col2) */
                .content-column {{
                    padding: 0 15px; /* Tambahkan sedikit padding agar tidak terlalu mepet dengan tepi */
                    box-sizing: border-box; /* Pastikan padding tidak menambah lebar total */
                }}
                /* Wrapper untuk gambar dan informasi prediksi */
                .prediction-wrapper {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                    align-items: flex-start;
                }

                .image-section {
                    flex: 1 1 250px;
                    max-width: 300px;
                }

                .image-section img {
                    width: 100%;
                    border-radius: 10px;
                }

                .info-section {
                    flex: 1 1 300px;
                    display: flex;
                    flex-direction: column;
                    gap: 15px;
                }

                /* MEDIA QUERIES untuk Responsivitas */
                @media (max-width: 768px) {{
                    /* Mengatur agar kolom menumpuk di layar kecil */
                    .main-content-wrapper .st-emotion-cache-yzfmqf.e1fqkh3o5 > div {{ /* PERLU INSPEKSI ULANG CLASS INI! */
                        flex-direction: column;
                    }}

                    .main-content-wrapper .st-emotion-cache-yzfmqf.e1fqkh3o5 > div > div {{ /* PERLU INSPEKSI ULANG CLASS INI! */
                        width: 100% !important;
                        margin-bottom: 20px;
                    }}

                    .responsive-image-container img {{
                        max-width: 80%; /* Gambar ilustrasi bisa lebih kecil di layar sempit */
                    }}

                    /* Penyesuaian font untuk layar kecil */
                    h1 {{ font-size: 2em; }}
                    p.instruction {{ font-size: 1em; }}
                    .stExpander details summary {{ font-size: 1.2em; }}

                    /* Sesuaikan padding kolom konten saat menumpuk */
                    .content-column {{
                        padding: 0 10px; /* Padding lebih kecil untuk layar sempit */
                    }}
                    .image-section, .info-section {
                        max-width: 100%;
                    }
                }}
            </style>
            """, unsafe_allow_html=True)

# --------- EKSTRAK GAMBAR -------------- #
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_string}"

scan = get_base64_image("aset/scan.png")


# ------------------------- UI STREAMLIT ------------------------------ #

with st.container():
    st.markdown("""<h2 style="font-family: 'Segoe UI'; text-align: center; margin-bottom: 0.5em">Deteksi Katarak Menggunakan Model CNN</h2>""", unsafe_allow_html=True)
    st.markdown("""<div class="subtitle">Unggah gambar citra fundus mata, biarkan model CNN menganalisis, dan dapatkan deteksi katarak yang efisien.</div>""", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([1, 1.4])
    with col1:
        st.markdown(f"""<div class="responsive-image-container"><img src={scan} style="width:85%"></div>""", unsafe_allow_html=True)
        st.markdown("""""",unsafe_allow_html=True)
    
    st.markdown("<div class='content-column'>", unsafe_allow_html=True)   
    
    with col2:
        st.markdown("<p class='instruction'>Cara Mengetahui Katarak atau Tidak</p>", unsafe_allow_html=True)
        
        # Upload Gambar Anda Expander
        st.markdown("<div class='upload-expander'>", unsafe_allow_html=True)
        with st.expander("📤 Unggah Gambar Citra Fundus Mata"):
            st.write("Pilih dan unggah citra fundus yang akan dianalisis. Pastikan gambar jelas dan tidak buram untuk hasil deteksi terbaik.")
        
        # Analisis Gambar Expander
        st.markdown("<div class='analyze-expander'>", unsafe_allow_html=True)
        with st.expander("🔎 Analisis Deteksi Katarak"):
            st.write("Model akan menganalisis citra fundus untuk mendeteksi tanda-tanda katarak. Proses ini cepat dan akurat.")
        
        # Dapatkan Hasil yang Detail Expander
        st.markdown("<div class='results-expander'>", unsafe_allow_html=True)
        with st.expander("📄 Dapatkan Hasil yang Detail"):
            st.write("Dapatkan hasil analisis terperinci yang mengklasifikasikan apakah citra fundus terindikasi katarak atau tidak, beserta nilai keyakinan untuk akurasi.")

# Upload the image
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file).convert('RGB')
    
    # Make prediction fundus or no
    image_input = preprocessing(image)
    fundus_predict = model_fundus.predict(image_input)
    
    if fundus_predict[0][0] >= 0.5:
        prediction, clahe_image = predict_cataract(image)
                
        # INI JUGA PERHATIKAN KATARAK OR NOT NYA, klo kebalik kebalik coba tanda '>' di otak atik
        # Assuming the output is a single probability for the positive class
        if prediction[0][0] >= 0.5:
            predicted_class = 'Terindikasi Katarak'
            confidence = prediction[0][0]
        else:
            predicted_class = 'Tidak Terindikasi Katarak'
            confidence = 1 - prediction[0][0]
        
        # Ubah ke persen dan bulatkan 2 angka di belakang koma
        confidence_percent = round(confidence * 100, 2)
    
        # ==== container ui ====
        with st.container(border=True):   
            st.markdown("""<p style="margin:10px; padding-bottom:15px" class='instruction'>Hasil Prediksi</p>""", unsafe_allow_html=True)
            
            fundus_np = np.array(image)
            _, fundus_encoded = cv2.imencode(".png", cv2.cvtColor(fundus_np, cv2.COLOR_RGB2BGR))
            fundus_b64 = base64.b64encode(fundus_encoded).decode()

            _, clahe_encoded = cv2.imencode(".png", clahe_image)
            clahe_b64 = base64.b64encode(clahe_encoded).decode()

            st.markdown(f"""
            <div class="prediction-wrapper">
                <div class="image-section">
                    <img src="data:image/png;base64,{fundus_b64}" alt="Fundus">
                    <p style="text-align:center; color: gray;">Gambar Fundus</p>
                </div>
                <div class="image-section">
                    <img src="data:image/png;base64,{clahe_b64}" alt="CLAHE">
                    <p style="text-align:center; color: gray;">Hasil CLAHE</p>
                </div>
                <div class="info-section">
                    <div class="card">
                        <div class="title">Detected Condition</div>
                        <div style="display:flex; justify-content:space-between; padding-bottom: 10px">
                            <div>Prediksi : </div>
                            <div class="value">{predicted_class}</div>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <div>Tingkat Kepercayaan :</div>
                            <div class="value2">{confidence_percent}%</div>
                        </div>
                    </div>
                    <div class="card">
                        <div>
                            <p><b>Keterangan :</b></p>
                            <p>Berdasarkan hasil analisis model, gambar fundus yang diunggah termasuk dalam <b>{predicted_class}</b> dengan tingkat keyakinan <b>{confidence_percent}</b>.</p>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Gambar tidak dikenali sebagai citra fundus.")
