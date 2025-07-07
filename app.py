import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import json
from utils import display_and_prepare_image
from huggingface_hub import hf_hub_download
import os

st.set_page_config(layout="centered", page_title="WayangLoka", page_icon="🧵", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    body {
        background-color: #FFFFF0;
    }

    .main {
        background-color: #FFFFF0;
    }

    .title {
        font-size: 3em;
        font-weight: bold;
        color: #5F6534;
        margin-bottom: 0.2em;
        text-align: center;
    }

    .subtitle {
        color: #D7A03A;
        font-size: 1.1em;
        margin-bottom: 2em;
        text-align: center;
    }

    .title-box {
        background-color: #5F6534;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }

    .title-box .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 0.4rem;
    }

    .title-box .subtitle {
        color: #FFD95A;
        font-size: 1.1em;
        margin: 0;
    }

    .character-name {
        text-align: center;
        font-size: 1.3em;
        font-weight: 600;
        color: #5F6534;
        margin-bottom: 10px;
    }

    hr {
        border: none;
        border-top: 1px solid #D7A03A;
        margin: 40px 0;
    }

    hr.custom-divider {
        border: none;
        border-top: 5px solid #5F6534;
        margin: auto;
    }

    button, .stButton > button {
        background-color: #5F6534 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 25px !important;
        font-size: 16px !important;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }

    button:hover, .stButton > button:hover {
        background-color: #D7A03A !important;
    }

    .stSelectbox label {
        color: #5F6534 !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        margin-bottom: 0.3rem;
    }

    .stFileUploader > div div:last-child button {
        background-color: #5F6534 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        transition: background-color 0.3s ease;
    }

    .stFileUploader > div div:last-child button:hover {
        background-color: #D7A03A !important;
        cursor: pointer !important;
    }

    .stFileUploader > label:first-child {
        color: #5F6534 !important;
        background: none !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        cursor: default !important;
        padding: 0 !important;
        border: none !important;
    }

    [data-testid="stSidebar"], header, footer {
        display: none !important;
    }

    @media (prefers-color-scheme: dark) {
        body, .main, .stApp {
            background-color: #FFFFF0 !important;
            color: #262730 !important;
        }

        .title-box {
            background-color: #5F6534 !important;
            color: #FFFFFF !important;
        }

        .character-name, .subtitle, .title {
            color: #5F6534 !important;
        }

        .wayang-desc {
            color: #262730 !important;
        }

        .stFileUploader > label:first-child,
        .stSelectbox label {
            color: #5F6534 !important;
        }

        .stMarkdown {
            color: #262730 !important;
        }
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
    <div class="title">SWayangLoka</div>
    <div class="subtitle">Eksplorasi budaya dalam genggaman digital • Mengenal wayang berdasarkan citra • Menjelajah cerita dengan cinta</div>
</div>
""", unsafe_allow_html=True)

# Separator
st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)
st.markdown(" ")

# --- Model Selector ---
model_option = st.selectbox(
    "Pilih model klasifikasi yang ingin digunakan:",
    ("MobileNetV2", "ResNet50", "EfficientNetB0")
)

model_files = {
    "MobileNetV2": "mobilenetv2_wayang_best.h5",
    "ResNet50": "resnet50_wayang_best.h5",
    "EfficientNetB0": "efficientnetb0_wayang_best.h5"
}

@st.cache_resource
def load_model_from_hf(repo_id, filename):
    local_path = hf_hub_download(repo_id=repo_id, filename=filename)
    return tf.keras.models.load_model(local_path)

@st.cache_data
def load_label_map():
    with open("label_map.json", "r") as f:
        return json.load(f)

uploaded_file = st.file_uploader("Unggah gambar wayangmu (Maksimal 200 mb)", type=["png", "jpg", "jpeg"])

model = load_model_from_hf("natashsch/wayang-models", model_files[model_option])
label_map = load_label_map()

if uploaded_file:
    img_batch = display_and_prepare_image(uploaded_file)
    pred = model.predict(img_batch)
    class_name = label_map[str(np.argmax(pred))]
    st.success(f"Wayang teridentifikasi: {class_name}")
    st.switch_page(f"pages/{list(label_map.values()).index(class_name)+1}_{class_name}.py")

st.markdown("""
<div style='background-color:#FFF8DC; border-left: 5px solid #D7A03A; padding: 1rem 1.5rem; margin-top:1rem; border-radius:8px'>
    <strong>Tips:</strong> Untuk hasil prediksi maksimal, gunakan foto Wayang Punakawan dari <em>Museum Wayang Jakarta</em>.
</div>
""", unsafe_allow_html=True)
st.markdown(" ")

st.markdown("---")
st.markdown("## Wayang Punakawan", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: justify'>
Punakawan adalah tokoh khas dalam dunia wayang Indonesia yang tidak ditemukan dalam kisah pewayangan asli India. Mereka pertama kali muncul dalam karya sastra Gatotkacasraya yang ditulis oleh Empu Panuluh. Di berbagai daerah di Pulau Jawa, tokoh Punakawan memiliki variasi, namun versi paling dikenal berasal dari tradisi Yogyakarta dan Surakarta, yaitu Semar, Gareng, Petruk, dan Bagong. Keempatnya tidak hanya berperan sebagai abdi para ksatria, tetapi juga menjadi penghibur, penyampai kritik sosial, penjaga nilai moral, serta penuntun jalan cerita dengan cara yang jenaka dan penuh makna.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

cols = st.columns(4)
names = ["Semar", "Gareng", "Petruk", "Bagong"]
images = ["semar.png", "gareng.png", "petruk.png", "bagong.png"]
for i, col in enumerate(cols):
    with col:
        st.markdown(f'<div class="character-name">{names[i]}</div>', unsafe_allow_html=True)
        st.image(f"assets/{images[i]}", use_container_width=True)
