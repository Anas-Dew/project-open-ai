import openai
from voiceRecognition import hear
from textToSpeech import text_to_speech
from playsound import playsound as play
from saveResponse import save_it


class Travis:
    def __init__(self, apiKey: str) -> None:
        openai.api_key = apiKey
        self.result = None

    def hello(self, model: str, command: str, temperature: int = 0.7):
        """
        The function takes in a model, a command, and a temperature. The model is the name of the model
        you want to use, the command is the prompt you want to give the model, and the temperature is
        the temperature you want to use. The function then uses the OpenAI API to generate a response to
        the prompt. The response is then converted to speech and played
        
        :param model: The name of the model you want to use
        :type model: str
        :param command: The prompt to be completed
        :type command: str
        :param temperature: Controls the randomness of the response. At temperature=0, the model will
        always pick the token with the highest probability. At temperature=1, the model will pick a
        token randomly from the distribution
        :type temperature: int
        :return: The result of the function is the text that is being spoken.
        """
        response = openai.Completion.create(
            model=f"{model}",
            prompt=f"{command}",
            temperature=temperature,
            # ----------------------------
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        self.result = response['choices'][0]['text']

        text_to_speech(self.result)
        print(self.result)
        play('./output.mp3')
        return self.result

    def save(self, path: str = '.', filename: str = 'Ai'):
        """
        It takes a path and a filename, and saves the result of the Ai object to a file
        
        :param path: The path to the directory where you want to save the file, defaults to .
        :type path: str (optional)
        :param filename: The name of the file you want to save, defaults to Ai
        :type filename: str (optional)
        """
        save_it(f'{path}{filename}', self.result)


if __name__ == "__main__":
    mybot = Travis('add-api-key-here-to-test')
    my_query = hear()
    myresult = mybot.hello('text-davinci-002', my_query)
    print(myresult)