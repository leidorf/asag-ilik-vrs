import streamlit as st
from vrs.audio_processing import predict_from_microphone, recognize_speech_from_microphone, plot_audio_waveform

st.set_page_config(
    page_title="Ses Tanıma",
    page_icon="🎙️"
)
st.sidebar.header("Ses Tanıma 🎙️")

st.title("Proje Detayları")
st.write("Bu sayfada proje ile ilgili detaylar yer alacak.")

# "Mikrofonu Aç/Kapat" butonu
if st.button("Mikrofonu Aç/Kapat"):
    # Predict the class from microphone input
    result, recording = predict_from_microphone()
    st.write("Tahmin edilen ses:", result.capitalize())

    # Plot the audio waveform
    plot_audio_waveform(recording.flatten(), fs=44100)

    # Recognize speech from microphone
    recognized_text = recognize_speech_from_microphone()
    st.write("Tanınan Metin:", recognized_text)
