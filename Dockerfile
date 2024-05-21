# Base image olarak resmi Python imajını kullan
FROM python:3.11-slim

# Gerekli paketleri yükle
RUN apt-get update && apt-get install -y \
    gcc \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılıkları yüklemek için requirements.txt dosyasını kopyala
COPY requirements.txt /app/

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . /app/

# Streamlit'i 8501 portundan çalıştır
EXPOSE 8501

# Streamlit komutunu çalıştır
CMD ["streamlit", "run", "Ana Sayfa.py"]
