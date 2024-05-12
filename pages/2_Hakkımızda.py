import streamlit as st

st.set_page_config(
    page_title="Hakkımızda",
    page_icon="👥",
    layout="centered",
    
)
st.sidebar.header("Hakkımızda 👥")

guray_image_url = "https://avatars.githubusercontent.com/u/93585259?v=4"
guray_github_url = "https://github.com/leidorf"

veli_image_url = "https://avatars.githubusercontent.com/u/95528034?v=4"
veli_github_url = "https://github.com/VeliYarar"

st.markdown("<h1 style='text-align: center;'>Hakkımızda</h1>", unsafe_allow_html=True)

st.divider()
col1, col2 = st.columns([1, 1])
with col1, st.container():
    st.markdown(f'<a href="{guray_github_url}"><img src="{guray_image_url}" alt="Güray DAĞ GitHub" style="width:350px;"></a>', unsafe_allow_html=True) 
    st.markdown("<div style='text-align: center;'><h5>Güray DAĞ</h5>(Web Developer)</div>", unsafe_allow_html=True)
with col2, st.container():
    st.markdown(f'<a href="{veli_github_url}"><img src="{veli_image_url}" alt="Güray DAĞ GitHub" style="width:350px;"></a>', unsafe_allow_html=True) 
    st.markdown("<div style='text-align: center;'><h5>Veli YARAR</h5>(AI Developer)</div>", unsafe_allow_html=True)    
st.divider()
st.markdown("<div style='text-align: center;'>Daha fazla bilgi için <a href='https://github.com/leidorf/asag-ilik-vrs'>GitHub deposuna</a> göz atabilirsiniz.</div>", unsafe_allow_html=True)