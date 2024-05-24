import streamlit as st
from vrs.audio_processing import predict_from_microphone
from vrs.plot_functions import plot_audio_waveform
from vrs.speech_to_text import recognize_speech_from_microphone
import numpy as np
import time

# Initialize session state
if 'microphone_state' not in st.session_state:
    st.session_state['microphone_state'] = False
if 'recordings' not in st.session_state:
    st.session_state['recordings'] = []
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = 0
if 'recognized_text' not in st.session_state:
    st.session_state['recognized_text'] = ""
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = ""

# Configure page settings
st.set_page_config(
    page_title="Ses Tanıma",
    page_icon="🎙"
)
st.sidebar.header("Ses Tanıma 🎙")

# Title and description
st.title("Proje Detayları")
st.write("Bu sayfada proje ile ilgili detaylar yer alacak.")

# Toggle microphone button
if st.button("Mikrofonu Aç/Kapat"):
    st.session_state['microphone_state'] = not st.session_state['microphone_state']
    if st.session_state['microphone_state']:
        st.session_state['start_time'] = time.time()  # Record start time

if st.session_state['microphone_state']:
    st.write("Mikrofon açık. Ses kaydediliyor ve metin tanınıyor...")

    # Perform speech-to-text and prediction simultaneously
    recognized_text = recognize_speech_from_microphone()
    prediction, recording = predict_from_microphone()
    
    if recognized_text:
        st.session_state['recognized_text'] = recognized_text
    else:
        st.session_state['recognized_text'] = "Metin tanınamadı."
    
    if prediction is not None:
        st.session_state['recordings'].append(recording)
        st.session_state['prediction'] = prediction.capitalize()
    else:
        st.session_state['prediction'] = "Tahmin yapılamadı. Model ile ilgili bir sorun olabilir."
    
    # Show results
    st.write("Tanınan Metin:", st.session_state['recognized_text'])
    st.write("Tahmin edilen ses:", st.session_state['prediction'])

    if st.session_state['recordings']:
        combined_recording = np.concatenate(st.session_state['recordings'])
        plot_audio_waveform(combined_recording, fs=44100)
else:
    if st.session_state['recordings']:
        st.write("Mikrofon kapalı. Kaydedilen ses verisi gösteriliyor...")
        combined_recording = np.concatenate(st.session_state['recordings'])
        plot_audio_waveform(combined_recording, fs=44100)
        st.session_state['recordings'] = []  # Clear recorded data
        st.session_state['start_time'] = 0  # Reset start time

    if st.session_state['recognized_text']:
        st.write("Tanınan Metin:", st.session_state['recognized_text'])
    else:
        st.write("Mikrofon kapalı.")
