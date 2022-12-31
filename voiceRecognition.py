import speech_recognition as sr
import os

r = sr.Recognizer()


def hear():
    """
    It creates a microphone instance, adjusts for ambient noise, listens for audio, and then converts
    the audio to text
    :return: The text that is being returned is the text that is being recognized by the google speech
    recognition.
    """
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("say anything : ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You Said : ", text)
            return text
        except:
            print("Didn't Recognized :(")
            return Exception('Error')


if __name__ == "__main__":
    hear()
