import streamlit as st 

st.set_page_config(page_title="Informasi", layout="wide")

import base64
import pandas as pd
import plotly.graph_objects as go

#------------------------ISI TA -----------------------#
# Tambahkan CSS untuk styling
st.markdown(
    """
    <style>
        h2.big-title {
            text-align: center;
            margin-bottom: 0.2em;
            font-family: 'Segoe UI';
        }
        h2.big-title1 {
            margin-bottom: 0.2em;
            font-size:28px;
            font-family: 'Segoe UI';
        }
        .subtitle {
            font-size: 1.2rem;
            color: #7b7b7b;
            text-align: center;
            font-family: 'Segoe UI';
            margin-bottom: 5em;
        }
        .title {
            font-family: 'Segoe UI';
            font-size: 1.7rem;
            font-weight: 500;
            padding-left:30%;
            margin-right:20%;
            margin-top: 2em;
            margin-bottom: 0.3em;
            display: flex;
            align-items: center;
            gap: 0.5em;
        }
        .title2 {
            font-size: 1.7rem;
            font-weight: 500;
            padding:20px;
            margin-top: 2em;
            margin-bottom: 0.3em;
            display: flex;
            align-items: center;
            gap: 0.5em;
        }
        .subtitle3 {
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.3em;
            display: flex;
            justify-content: center;
            text-align: center;
        }
        .content-box {
            background-color: #EDE7E3;
            color: black;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: justify;
            margin-bottom: 50px;
            overflow:hidden;
        }
        .gradient-card, .gradient-card2, .gradient-card3 {
            font-family: 'Segoe UI';
            border-radius: 16px;
            padding: 1.5em 1em 1em 1em;
            color: black;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1.5em;
            box-shadow: 0 2px 12px rgba(140,140,140,0.07);
            width: 100%;
            max-width: 100%;
            box-sizing: border-box;
            overflow-x: auto;
        }
        .gradient-card {
            background: linear-gradient(250deg, #FFFFFF 0%, #E7F4FF 100%);
        }
        .gradient-card2 {
            background: linear-gradient(120deg, #FFFFFF 10%, #FFDBDF 100%);
        }
        .gradient-card3 {
            padding: 1em 1em;
            background: linear-gradient(120deg, #FFFFFF 10%, #FFE3C1 100%);
        }
        .gradient-card ul {
            padding-left: 20px;
        }
        .gradient-card li {
            margin-bottom: 8px;
        }
        .img {
            border-radius: 10px;
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }
        .hover-pop {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .hover-pop:hover {
            transform: scale(1.02);
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
        }
        .custom-selectbox label {
            font-size: 18px;
            font-weight: 600;
            color: #333;
            margin-bottom: 0.5em;
            font-family: 'Segoe UI';
        }
        .custom-selectbox .stSelectbox {
            background-color: #F5FAFF;
            padding: 8px 12px;
            border-radius: 10px;
            border: 1px solid #C3DCF3;
            font-family: 'Segoe UI';
        }
    </style>
    """,
    unsafe_allow_html=True
)

# List gambar 
image_paths = [
    "aset/normal1.jpeg", "aset/normal2.jpg", "aset/normal3.jpg", "aset/normal4.jpeg", "aset/normal5.jpg",
    "aset/ctr1.jpg", "aset/ctr2.png", "aset/ctr3.png", "aset/ctr4.jpg", "aset/ctr5.png"
]

# Fungsi untuk encode gambar ke base64 
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64_string}"

# Encode gambar 1 folder
base64_images = [get_base64_image(path) for path in image_paths]

# Judul dan konten overview
st.markdown('<h2 class="big-title">Tentang Klasifikasi Katarak</h2>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Informasi Lengkap Mengenai Pembuatan Website Klasifikasi Katarak </div>', unsafe_allow_html=True)

# Informasi gambaran umum

st.markdown('<h2 class="big-title1">Gambaran Umum </h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="gradient-card hover-pop">
        <p>
            Deteksi katarak menggunakan model MobileNet merupakan hasil dari penelitian  
            yang bertujuan untuk mengklasifikasikan citra fundus mata. 
            Model MobileNet dipilih setelah dilakukan perbandingan dengan model VGG16.
            Untuk meningkatkan kualitas citra, dataset diproses menggunakan teknik 
            CLAHE (Contrast Limited Adaptive Histogram Equalization). 
            Penerapan model klasifikasi ini dirancang untuk membantu dokter dalam  
            menganalisis citra fundus mata katarak secara lebih cepat dan akurat.
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

# informari dataset
st.markdown("""<h2 class="big-title1"> Informasi Dataset</h2>""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="gradient-card2 hover-pop">
        <p>
            Klasifikasi katarak pada penelitian ini menggunakan data citra fundus. 
            Citra fundus merupakan gambar yang diambil dari bagian belakang mata atau fundus mata. 
            Terdapat dua jenis citra fundus yang digunakan yaitu normal dan katarak. 
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
normal_images = ""
for img in base64_images[:4]:
    normal_images += f'<img src="{img}" width="100" height="100" style="object-fit:cover; margin-right:10px; border-radius:8px;"/>'

with col1:
    st.markdown("""<div class="subtitle3 "><b>Citra Fundus Mata Normal<b></div>""", unsafe_allow_html=True)
    st.markdown(
            """
            <div class="gradient-card3 hover-pop" style="text-align: center">
                <div>""" + normal_images + """</div>
            </div>
            """, unsafe_allow_html=True
        )
    
katarak_images = ""
for img in base64_images[6:]:
        katarak_images += f'<img src="{img}" width="100" height="100" style="object-fit:cover; margin-right:10px; border-radius:8px;"/>'

with col2:
    st.markdown("""<div class="subtitle3"><b>Citra Fundus Mata Katarak<b></div>""", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="gradient-card3 hover-pop" style="text-align: center">
        <div>""" + katarak_images + """</div>
        </div>
        """, unsafe_allow_html=True
    )

# Pembuatan model
st.markdown("""<h2 class="big-title1"> Pembuatan Model</h2>""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="gradient-card hover-pop">
        <p>
            Pada pembuatan model, penelitian ini menggunakan model VGG16 dan model MobileNet. Karena fokus penelitian ini membandingkan performa kedua model tersebut, 
            maka dilakukan beberapa percobaan untuk melihat performa yang dihasilkan kedua model tersebut. Percobaan yang dilakukan pada kedua model tersebut antara lain:
            <ul>
                <li>Percobaan Data Seimbang</li>
                <li>Percobaan Tanpa Teknik CLAHE</li>
                <li>Percobaan Menggabungkan Kedua Model (ensemble)</li>
            </ul>
        </p>
        <p> 
            Dari percobaan tersebut didapatkan 9 model dengan kondisi yang berbeda-beda. 
        </P>
    </div>
    """, 
    unsafe_allow_html=True
) 

# Evaluasi model
st.markdown("""<h2 class="big-title1"> Evaluasi Model</h2>""", unsafe_allow_html=True)  
st.markdown(
    """
    <div class="gradient-card2 hover-pop">
        <p>
            Dari seluruh hasil evaluasi, menunjukkan bahwa baik model VGG16 maupun model MobileNet mampu mengklasifikasikan citra fundus dengan akurasi yang tinggi. 
            Namun, model MobileNet menunjukkan keunggulan yang lebih konsisten di berbagai percobaan. 
            Pada hasil percobaan, model MobileNet secara umum memiliki nilai akurasi yang lebih tinggi dan nilai loss yang lebih rendah dibandingkan model VGG16. 
            Distribusi data yang seimbang terbukti lebih berpengaruh terhadap performa model dibandingkan jumlah total data. 
            Selain itu, penerapan teknik CLAHE memberikan peningkatan akurasi, terutama pada model VGG16. 
            Pendekatan ensemble menunjukkan hasil yang identik dengan model MobileNet, mengindikasikan bahwa performa model MobileNet sudah sangat optimal 
            bahkan sebelum digabungkan. Dari segi efisiensi waktu, model MobileNet juga memiliki durasi pelatihan yang jauh lebih singkat dibandingkan model VGG16.         
        </p>
        <p>
            Berdasarkan keseluruhan evaluasi, <b>Model MobileNet</b> dengan data seimbang dan teknik CLAHE 
            digunakan pada website ini sebagai model teroptimal untuk klasifikasi citra fundus mata katarak, 
            karena memiliki kombinasi performa, stabilitas, dan efisiensi yang paling optimal.
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Memanggil file csv
excel_file_path = "log/model.xlsx"

# Mapping antara nama dropdown dengan sheet Excel
model_mapping = {
    "Model VGG16 Data Keseluruhan CLAHE": "vgg 2112 clahe",
    "Model MobileNet Data Keseluruhan CLAHE": "mobilenet 2112 clahe",
    "Model VGG16 Data Seimbang CLAHE": "vgg 1000 clahe",
    "Model MobileNet Data Seimbang CLAHE": "mobilenet 1000 clahe",
    "Model VGG16 Data Keseluruhan Tanpa CLAHE": "vgg 2112 non clahe",
    "Model MobileNet Data Keseluruhan Tanpa CLAHE": "mobilenet 2112 non clahe",
    "Model VGG16 Data Seimbang Tanpa CLAHE": "vgg 1000 non clahe",
    "Model MobileNet Data Seimbang Tanpa CLAHE": "mobilenet 1000 non clahe",
    "Model Gabungan (Ensemble)": "ensemble",
}

# Judul
st.markdown("""<h2 class="big-title1"> Grafik Akurasi dan Loss Pelatihan Tiap Model</h2>""", unsafe_allow_html=True)

# Dropdown untuk memilih model
with st.container():
    st.markdown("<div class='custom-selectbox'>", unsafe_allow_html=True)
    selected_model_name = st.selectbox("", list(model_mapping.keys()))
    st.markdown("</div>", unsafe_allow_html=True)
    
# selected_model_name = st.selectbox("Pilih Model", list(model_mapping.keys()))

# Dapatkan nama sheet dari mapping
selected_sheet = model_mapping[selected_model_name]
    
try:
    df = pd.read_excel(excel_file_path, sheet_name=selected_sheet)

    col1, col2 = st.columns(2)

    
    # Tampilkan grafik pelatihan
    with col1:
        
        df_clean = df[['accuracy', 'val_accuracy', 'loss', 'val_loss']].dropna()
        
        fig = go.Figure()
    
        fig.add_trace(go.Scatter(y=df["accuracy"], name="accuracy", line=dict(color='blue')))
        fig.add_trace(go.Scatter(y=df["val_accuracy"], name="val_accuracy", line=dict(color='orange')))
        
        fig.update_layout(
            title=dict(text="Grafik Akurasi", font=dict(size=18, family='Segoe UI')),            
            xaxis_title="Epoch",
            yaxis_title="Accuracy",
            yaxis=dict(range=[0.8, 1.0]),  # ⬅️ Custom axis limit
            template="plotly_white"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(y=df["loss"], name="loss", line=dict(color='blue')))
        fig1.add_trace(go.Scatter(y=df["val_loss"], name="val_loss", line=dict(color='orange')))
        fig1.update_layout(
            title=dict(text="Grafik Loss", font=dict(size=18, family='Segoe UI')),
            xaxis_title="Epoch",
            yaxis_title="Loss",
            # yaxis=dict(range=[0.8, 1.0]),  # ⬅️ Custom axis limit
            template="plotly_white"
        )
        st.plotly_chart(fig1, use_container_width=True)
        
    # Classification report    
    if "label" in df.columns:
        # Isi NaN dengan string kosong agar tidak error di tampilan
        df.fillna('', inplace=True)

        # Pastikan index label diset (opsional)
        df.index = df['label'].tolist()

        # Drop kolom label dari isi tabel, karena sudah dipakai jadi index
        df_report = df[["presisi", "recall", "f1-score", "support"]]
        
        # Buat Plotly Table
        fig = go.Figure(data=[go.Table(
            columnwidth=[60, 50, 50, 50, 50],  # Ukuran relatif tiap kolom
            header=dict(
                values=["<b>Label</b>"] + [f"<b>{col.title()}</b>" for col in df_report.columns],
                fill_color="#FAE7C0",  # header warna kuning soft
                font=dict(color='black', size=18, family='Segoe UI'),
                align='center'
            ),
            cells=dict(
                values=[df.index.tolist()] + [df_report[col].tolist() for col in df_report.columns],
                fill_color='white',
                align='center',
                font=dict(color='black',size=16, family='Segoe UI'),
                height=28
            )
        )])

        fig.update_layout(
            title=dict(text="Classification Report", font=dict(size=18, family='Segoe UI')),
            width=1000,
            margin=dict(l=0, r=0, t=50, b=50),
            height=300,
        )

        # Tampilkan di Streamlit
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Gagal membaca sheet: {e}")
