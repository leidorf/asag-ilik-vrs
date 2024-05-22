import sounddevice as sd
import numpy as np
import librosa
from joblib import load
import speech_recognition as sr
import matplotlib.pyplot as plt
import streamlit as st

# Load the KNN model and scaler
knn_loaded = load("./models/knn_model21.joblib")
scaler_loaded = load("./models/scaler21.joblib")

# Feature extraction function
def extract_features_live(signal, sr, num_mfcc=13, n_fft=2048, hop_length=512):
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
    mfcc_features = np.mean(mfcc_features.T, axis=0)
    return mfcc_features

# Live audio prediction function
def predict_from_microphone(duration=10, fs=44100, num_mfcc=13, n_fft=2048, hop_length=512):
    print("Mikrofon dinleniyor...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    print("Kayıt tamamlandı.")
    features = extract_features_live(recording.flatten(), sr=fs, num_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
    features_scaled = scaler_loaded.transform([features])
    prediction = knn_loaded.predict(features_scaled)
    return prediction[0], recording

# Recognize speech from microphone
def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Lütfen konuşun...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("Anlaşılan Metin:", text)
        return text
    except sr.UnknownValueError:
        print("Anlaşılamayan ses.")
        return ""
    except sr.RequestError as e:
        print("Ses tanıma servisine erişilemiyor; {0}".format(e))
        return ""

# Plot audio waveform function
def plot_audio_waveform(signal, fs):
    plt.figure(figsize=(10, 4))
    plt.plot(np.linspace(0, len(signal) / fs, num=len(signal)), signal)
    plt.title('Audio Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    st.pyplot(plt)
