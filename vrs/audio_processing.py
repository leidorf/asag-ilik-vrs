import numpy as np
import sounddevice as sd
import librosa
from joblib import load

# Model ve scaler'ı yükle
knn_loaded = load("./models/knn_model21.joblib")
scaler_loaded = load("./models/scaler21.joblib")

# Feature extraction fonksiyonu
def extract_features_live(signal, sr, num_mfcc=13, n_fft=2048, hop_length=512):
    mfcc_features = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
    mfcc_features = np.mean(mfcc_features.T, axis=0)
    return mfcc_features

# Mikrofondan tahmin yapma
def predict_from_microphone(duration=0.1, fs=44100, num_mfcc=13, n_fft=2048, hop_length=512):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    features = extract_features_live(recording.flatten(), sr=fs, num_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
    features_scaled = scaler_loaded.transform([features])
    prediction = knn_loaded.predict(features_scaled)
    return prediction[0], recording
