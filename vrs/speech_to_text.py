import speech_recognition as sr

def recognize_speech_from_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            # Tanınan metni al
            metin = r.recognize_google(audio, language="tr")
            # Kelimeleri ayır
            kelimeler = metin.split()
            # Toplam kelime sayısını yazdır
            print("Toplam kelime sayısı:", len(kelimeler))
            print(metin)
            return metin
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None