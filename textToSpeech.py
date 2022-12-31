# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os


def text_to_speech(text: str, language: str = 'en'):
    """
    It takes a string of text and a language code as input, and outputs an mp3 file of the text being
    spoken in the specified language
    
    :param text: The text that you want to convert to speech
    :type text: str
    :param language: The language in which you want to convert the text, defaults to en
    :type language: str (optional)
    """
    mytext = text
    language = language
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("output.mp3")
