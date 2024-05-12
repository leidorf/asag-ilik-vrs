import streamlit as st

st.set_page_config(
    page_title="Ana Sayfa",
    page_icon="🏠"
)
st.sidebar.header("Ana Sayfa 🏠")
st.markdown("<h1 style='text-align: center;'>🎙️</br>ASAG-ILIK VRS</h1>", unsafe_allow_html=True)
    
st.divider()

st.write("Bu proje, ses verilerini işleyerek konuşmacıyı tanımlama ve konuşmanın duygusunu tahmin etme üzerine odaklanmaktadır. Projenin temel amacı, ses tanımlama ve duygu tahmini alanlarında makine öğrenimi yöntemlerini kullanarak kullanıcı dostu bir uygulama geliştirmektir.")
