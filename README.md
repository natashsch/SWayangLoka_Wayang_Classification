<div align="center">
	<h1>🧵 SWayangLoka: Eksplorasi AI untuk Mengenal Wayang Punakawan</h1>
</div>

<div align="center">
    <img src="https://img.shields.io/badge/streamlit-darkgreen?style=for-the-badge&logo=streamlit&logoColor=white">
    <img src="https://img.shields.io/badge/python-yellow.svg?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/tensorflow-red.svg?style=for-the-badge&logo=tensorflow&logoColor=white">
    <img src="https://img.shields.io/badge/keras-gray.svg?style=for-the-badge&logo=keras&logoColor=white">
</div>

<br>

**SWayangLoka** adalah aplikasi web berbasis kecerdasan buatan yang mengenali tokoh wayang **Punakawan** dari gambar yang diunggah oleh pengguna. Aplikasi ini menggabungkan teknologi klasifikasi gambar menggunakan deep learning dengan tampilan visual yang estetik untuk memperkenalkan budaya lokal secara digital dan interaktif.

---

## 🚀 Apa Itu SWayangLoka?

SWayangLoka membantu mengenal dan memahami filosofi di balik empat tokoh Punakawan: **Semar, Gareng, Petruk, dan Bagong**.

Dengan hanya mengunggah sebuah gambar:
- 🧠 **AI akan memprediksi tokoh wayang** berdasarkan model deep learning.
- 📜 **Menampilkan deskripsi dan filosofi tokoh** secara visual.
- 📺 **Menautkan ke lakon YouTube** untuk memperkaya pengalaman belajar budaya.

---

## 🌟 Fitur Utama

- ✅ **Klasifikasi gambar otomatis** menggunakan model MobileNetV2, ResNet-50, dan EfficientNetB0
- 🎨 **Tampilan bernuansa budaya** (warna `olive` dan `emas` yang elegan).
- 🔁 **Navigasi dinamis** berdasarkan hasil prediksi.
- 📚 **Konten edukatif** untuk pelestarian budaya.
- ☁️ **Model diambil otomatis dari Hugging Face Hub (`natashsch/wayang-models`)**, tanpa perlu folder `model/` lokal.

---

## 💻 Tech Stack

- **Backend & ML:** Python, TensorFlow/Keras
- **Framework Web:** Streamlit
- **UI & Styling:** HTML, CSS (custom inline), PIL

---

## 🪰 Struktur Folder

```
SWayangLoka_Wayang_Classification/
│
├── app.py                      # Halaman utama
├── utils.py                    # Fungsi bantu (preprocessing gambar)
├── requirements.txt            # Daftar dependensi
├── label_map.json              # Mapping label model ke nama tokoh
│
├── assets/                     # Gambar karakter tokoh
│   ├── semar.png
│   ├── gareng.png
│   ├── petruk.png
│   ├── bagong.png
│
├── pages/
│   ├── 1_Bagong.py
│   ├── 2_Gareng.py
│   ├── 3_Petruk.py
│   └── 4_Semar.py
```

---

## 🚀 Get Started

### ✅ Prasyarat

- Python `>=3.8`
- pip & virtualenv (jika menjalankan lokal)

---

### 🧪 Instalasi & Menjalankan Lokal

1. **Clone Repository**
   ```bash
   git clone https://github.com/natashsch/SWayangLoka_Wayang_Classification.git
   cd SWayangLoka_Wayang_Classification
   ```

2. **Buat & Aktifkan Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instal Semua Dependensi**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi**
   ```bash
   streamlit run app.py
   ```

5. **Akses di Browser**
   [http://localhost:8501](http://localhost:8501)

---

## 🌟 Mengapa SWayangLoka?

SWayangLoka adalah sarana edukasi berbasis teknologi yang:

- 📣 **Meningkatkan apresiasi budaya Indonesia**
- ⚡ **Memanfaatkan AI untuk klasifikasi real-time**
- 🎨 **Menyajikan visualisasi yang modern namun tetap kental nilai tradisi**

SWayangLoka cocok untuk pelajar, pengajar, pemerhati budaya, atau siapa pun yang ingin menjelajah kisah Punakawan dengan cara baru.

---
