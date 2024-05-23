import streamlit as st
from vrs.audio_processing import predict_from_microphone
from vrs.plot_functions import plot_audio_waveform
from vrs.speech_to_text import recognize_speech_from_microphone
import numpy as np
import time

# Session state'i başlat
if 'microphone_state' not in st.session_state:
    st.session_state['microphone_state'] = False
if 'recordings' not in st.session_state:
    st.session_state['recordings'] = []
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = 0

# Sayfa ayarlarını yapılandırma
st.set_page_config(
    page_title="Ses Tanıma",
    page_icon="🎙️"
)
st.sidebar.header("Ses Tanıma 🎙️")

# Başlık ve açıklama
st.title("Proje Detayları")
st.write("Bu sayfada proje ile ilgili detaylar yer alacak.")

# Mikrofonu Aç/Kapat butonu
if st.button("Mikrofonu Aç/Kapat"):
    st.session_state['microphone_state'] = not st.session_state['microphone_state']
    if st.session_state['microphone_state']:
        st.session_state['start_time'] = time.time()  # Başlangıç zamanını kaydet

if st.session_state['microphone_state']:
    st.write("Mikrofon açık. Ses kaydediliyor ve tahmin yapılıyor...")
    prediction, recording = predict_from_microphone()
    if prediction is not None:
        st.session_state['recordings'].append(recording)
        st.write("Tahmin edilen ses:", prediction.capitalize())
        
        recognized_text = recognize_speech_from_microphone()
        st.write("Tanınan Metin:", recognized_text)
    else:
        st.write("Tahmin yapılamadı. Model ile ilgili bir sorun olabilir.")
else:
    if st.session_state['recordings']:
        st.write("Mikrofon kapalı. Kaydedilen ses verisi gösteriliyor...")
        combined_recording = np.concatenate(st.session_state['recordings'])
        plot_audio_waveform(combined_recording, fs=44100)
        st.session_state['recordings'] = []  # Kaydedilen veriyi temizle
        st.session_state['start_time'] = 0  # Başlangıç zamanını sıfırla
    else:
        st.write("Mikrofon kapalı.")
