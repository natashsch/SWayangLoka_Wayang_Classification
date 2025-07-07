import streamlit as st

st.set_page_config(page_title="Semar", page_icon="🧵")

st.markdown("""
<style>
    body {
        background-color: #FFFFF0;
    }
    .title-box {
        background-color: #5F6534;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    .title-box .wayang-title {
        font-size: 2em;
        font-weight: bold;
        color: #FFFFFF;
        margin-bottom: 0.4rem;
    }
    .wayang-desc {
        text-align: justify;
        margin-top: 1.5em;
        color: #262730;
        font-size: 1.05em;
        line-height: 1.6;
    }
    [data-testid="stSidebar"], header, footer {
        display: none !important;
    }
    .stButton > button {
        background-color: #5F6534 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 25px !important;
        font-size: 16px !important;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #D7A03A !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
    <div class="wayang-title">Teridentifikasi: Semar ✨</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/semar.png", width=300)

st.markdown("""
<div class="wayang-desc">
Semar adalah tokoh tertua dalam Punakawan sekaligus yang paling disegani. Ia merupakan penjelmaan dari dewa Hyang Ismaya yang diturunkan ke bumi untuk membimbing dan mendampingi para ksatria seperti Pandawa. Semar memiliki wujud yang unik, yaitu wajah tua dengan rambut seperti anak kecil, tubuh gemuk dengan payudara layaknya perempuan. Semua ini melambangkan dualitas antara tua-muda, laki-laki-perempuan, atas-bawah. Meskipun berasal dari kalangan dewa, Semar hidup sebagai rakyat biasa. Ia adalah simbol kerendahan hati, kebijaksanaan, dan kasih sayang tanpa pamrih.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Tonton lakonnya di sini!")
st.video("https://www.youtube.com/watch?v=aJaTSd91SrQ")
st.markdown(" ")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("Identifikasi Ulang"):
        st.switch_page("app.py")
    st.markdown("</div>", unsafe_allow_html=True)
