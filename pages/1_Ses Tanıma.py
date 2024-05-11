import streamlit as st
import pyaudio
import numpy as np
import librosa
import tensorflow as tf 

# Mikrofon özelliklerini tanımlayın
chunk = 1024  # Ses verisini bölmek için kullanılacak paket boyutu
FORMAT = pyaudio.paInt16  # Ses formatı
CHANNELS = 1  # Tek kanallı ses (mono)
RATE = 16000  # Örnekleme hızı (örneğin 16 kHz)
# Konuşma eşik değeri
SPEECH_THRESHOLD = 1000

# Model yükleme
#model = tf.keras.models.load_model("your_model.h5")  # Load your TensorFlow model

# Ses verisini tahmin et
def predict(audio_data):
    # Ses verisini önişleme
    audio_data = audio_data.astype(np.float32) / 32767.0  # Normalize et
    audio_data, _ = librosa.effects.trim(audio_data, top_db=20)  # Gürültüyü kırp (20 dB üzeri sessizlikler kesilir)
    
    # Örnekleme hızını modele uyacak şekilde değiştir (RATE -> modelin beklentisi olan örnekleme hızı)
    audio_data = librosa.resample(audio_data, orig_sr=RATE, target_sr=model.input_shape[1])

    # Model için özellik vektörü oluştur
    features = librosa.feature.mfcc(y=audio_data, sr=model.input_shape[1], n_mfcc=40)
    features = features.reshape(1, -1)  # Modelin beklentilerine uyacak şekilde yeniden boyutlandır

    # Sınıflandırma yap
    prediction = model.predict(features)
    class_label = np.argmax(prediction)

    if class_label == 0:
        return "guray"
    elif class_label == 1:
        return "veli"
    else:
        return "Unknown"

# Ses yakalama ve sınıflandırma
def classify_audio_stream():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=chunk)

    st.text("Mikrofon başlatıldı...")

    try:
        while True:
            # Ses verisi oku
            data = stream.read(chunk)
            audio_data = np.frombuffer(data, dtype=np.int16)

            # Konuşma algılama
            if np.max(np.abs(audio_data)) > SPEECH_THRESHOLD:
                # Eğer ses verisinde konuşma algılandıysa sınıflandırma yap
                result = predict(audio_data)
                st.text("Sınıflandırma sonucu: " + result)

    except KeyboardInterrupt:
        pass

    st.text("Mikrofon kapatılıyor...")

    stream.stop_stream()
    stream.close()
    p.terminate()

st.set_page_config(
    page_title="Ses Tanıma",
    page_icon="🎙️"
)
st.sidebar.header("Ses Tanıma 🎙️")


st.title("Proje Detayları")
st.write("Bu sayfada proje ile ilgili detaylar yer alacak.")
# "Mikrofonu Aç" butonu
if st.button("Mikrofonu Aç"):
    classify_audio_stream()
