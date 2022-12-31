import datetime


def save_it(filename: str = f'response.txt', response: str = ''):
    """
    It takes a filename and a response, and saves the response to a file with the filename and the
    current date
    
    :param filename: str = f'response.txt', defaults to f'response.txt'
    :type filename: str (optional)
    :param response: str = ''
    :type response: str
    """
    now = datetime.datetime.now()
    with open(f"{filename} {now.strftime('%d %B, %Y')}.txt", 'w') as response_file:
        response_file.write(response)


if __name__ == "__main__":
    # THIS IS A TEST
    save_it('sample', 'A car is a vehicle that typically has four wheels and is used for transportation')
