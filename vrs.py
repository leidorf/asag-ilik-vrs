import streamlit as st
import pyaudio
import numpy as np
import librosa
import tensorflow as tf 
import matplotlib.pyplot as plt

# Global değişkenler
stream_is_running = False
result_text = None
model = tf.keras.models.load_model("ses_tanima_v5.h5")

# Mikrofon özelliklerini tanımlayın
chunk = 1024  # Ses verisini bölmek için kullanılacak paket boyutu
FORMAT = pyaudio.paInt16  # Ses formatı
CHANNELS = 1  # Tek kanallı ses (mono)
RATE = 16000  # Örnekleme hızı (örneğin 16 kHz)
# Konuşma eşik değeri
SPEECH_THRESHOLD = 1000

# Ses verisinin zaman serisini gösteren fonksiyon
def plot_audio_waveform(audio_data):
    fig, ax = plt.subplots(figsize=(10, 6))
    time = np.arange(0, len(audio_data)) / RATE
    ax.plot(time, audio_data, color='blue')
    ax.set_title('Ses Verisi Zaman Serisi')
    ax.set_xlabel('Zaman (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    st.pyplot(fig)

# Ses verisini tahmin et
def predict(audio_data):
    global result_text
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
        result_text.text("Sınıflandırma sonucu: Guray")
    elif class_label == 1:
        result_text.text("Sınıflandırma sonucu: Veli")
    else:
        result_text.text("Sınıflandırma sonucu: Unknown")

def classify_audio_stream():
    global stream_is_running
    global result_text

    if not stream_is_running:
        stream_is_running = True
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=chunk)

        st.text("Mikrofon başlatıldı.")
        result_text = st.empty()  # Boş bir st.text alanı oluştur

        try:
            while stream_is_running:  # stream_is_running True olduğu sürece döngüyü çalıştır
                # Ses verisi oku
                data = stream.read(chunk)
                audio_data = np.frombuffer(data, dtype=np.int16)

                # Konuşma algılama
                if np.max(np.abs(audio_data)) > SPEECH_THRESHOLD:
                    # Eğer ses verisinde konuşma algılandıysa sınıflandırma yap
                    predict(audio_data)

                # Zaman serisi çiz
                plot_audio_waveform(audio_data)

        except KeyboardInterrupt:
            pass

        finally:
            st.text("Mikrofon kapatılıyor.")

            stream.stop_stream()
            stream.close()
            p.terminate()
            stream_is_running = False  # Mikrofon kapatıldığında bayrağı sıfırla

    else:
        st.text("Mikrofon kapatıldı.")
        stream_is_running = False  # Mikrofon zaten açık olduğunda bayrağı sıfırla
