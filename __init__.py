from voiceRecognition import hear
from openAi import Travis

if __name__ == "__main__":
    mybot = Travis('add-api-key-here-to-test')
    
    my_query = hear()
    mybot.hello('text-davinci-002', my_query)
    mybot.save('./records/')