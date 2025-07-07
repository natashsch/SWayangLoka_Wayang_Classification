from PIL import Image, ImageOps
import numpy as np
import streamlit as st

def display_and_prepare_image(uploaded_file):
    # Buka dan auto-perbaiki orientasi berdasarkan EXIF
    image = Image.open(uploaded_file).convert("RGB")
    image = ImageOps.exif_transpose(image)

    # Tampilkan gambar dengan ukuran sedang dan terpusat
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(image, caption="Gambar yang diunggah", width=400)

    # Resize gambar untuk prediksi model
    img_resized = image.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)
    return img_batch
