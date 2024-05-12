import streamlit as st
from vrs import classify_audio_stream

st.set_page_config(
    page_title="Ses Tanıma",
    page_icon="🎙️"
)
st.sidebar.header("Ses Tanıma 🎙️")

st.title("Proje Detayları")
st.write("Bu sayfada proje ile ilgili detaylar yer alacak.")

# "Mikrofonu Aç/Kapat" butonu
if st.button("Mikrofonu Aç/Kapat"):
    classify_audio_stream()
