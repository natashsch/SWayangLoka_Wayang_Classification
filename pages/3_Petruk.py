import streamlit as st

st.set_page_config(page_title="Petruk", page_icon="🧵")

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
    <div class="wayang-title">Teridentifikasi: Petruk ✨</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("assets/petruk.png", width=300)

st.markdown("""
<div class="wayang-desc">
Petruk adalah tokoh Punakawan yang tinggi kurus dengan hidung panjang yang mencolok. Ia digambarkan sebagai sosok yang cerdas, pandai mengambil hati orang lain, dan usil. Dengan kecerdasan dan kepandaiannya, ia dapat membangun kedekatan secara psikologis dengan banyak ksatria. Ia berani menyuarakan kebenaran secara langsung, tanpa takut pada kekuasaan. Kelucuannya sering menjadi sarana menyampaikan kritik sosial, namun selalu dengan niat tulus untuk memperbaiki keadaan. Petruk adalah lambang dari rasa, logika, dan keberanian yang dibalut dengan humor.
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
    