import streamlit as st
from vrs.audio_processing import predict_from_microphone
from vrs.plot_functions import plot_audio_waveform
from vrs.speech_to_text import recognize_speech_from_microphone
import numpy as np
import time

# Initialize session state
def initialize_session_state():
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

# Handle microphone toggle
def toggle_microphone():
    st.session_state['microphone_state'] = not st.session_state['microphone_state']
    if st.session_state['microphone_state']:
        st.session_state['start_time'] = time.time()

# Perform speech-to-text and prediction
def process_audio():
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
        st.session_state['prediction'] = "Tahmin yapılamadı."

# Display results
def display_results():
    st.write("Tahmin edilen ses:", st.session_state['prediction'])
    st.write("Tanınan Metin:", st.session_state['recognized_text'])
    
    # Toplam kelime sayısını hesapla
    if st.session_state['recognized_text']:
        kelime_sayısı = len(st.session_state['recognized_text'].split())
        st.write("Toplam Kelime:", kelime_sayısı)
    else:
        st.write("Toplam Kelime: 0")
    
    if st.session_state['recordings']:
        combined_recording = np.concatenate(st.session_state['recordings'])
        plot_audio_waveform(combined_recording, fs=44100)


# Main function to run the Streamlit app
def main():
    initialize_session_state()

    # Configure page settings
    st.set_page_config(page_title="Ses Tanıma", page_icon="🎙")
    st.sidebar.header("Ses Tanıma 🎙")

    # Title and description
    st.title("Ses Tanıma")
    st.write("Kayıt almak için Mikrofon Aç/Kapat butonu kullanılır. 10 saniyelik tahminden sonra tahmin edilen ses, tanınan metin ve sesin histogramı çıkartılır. Tekrar kayıt almak için mikrofonun kapatılıp açılması gerekir.")

    # Toggle microphone button
    if st.button("Mikrofonu Aç/Kapat"):
        toggle_microphone()

    if st.session_state['microphone_state']:
        st.write("Mikrofon AÇIK. Ses kaydediliyor ve metin tanınıyor...")

        # Perform speech-to-text and prediction
        process_audio()

        # Display results
        display_results()
    else:
        if st.session_state['recordings']:
            st.write("Mikrofon KAPALI. Butona tıklayarak tekrar kayıt alabilirsiniz. Kaydedilen ses verisi gösteriliyor...")
            display_results()
            st.session_state['recordings'] = []  # Clear recorded data
            st.session_state['start_time'] = 0  # Reset start time

# Run the main function
if __name__ == "__main__":
    main()