import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_audio_waveform(audio_data, fs):
    fig, ax = plt.subplots(figsize=(10, 6))
    time = np.arange(0, len(audio_data)) / fs
    ax.plot(time, audio_data, color='red')
    ax.set_title('Ses Verisi Zaman Serisi')
    ax.set_xlabel('Zaman (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True)
    st.pyplot(fig)
