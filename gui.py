import tkinter as tk
from tkinter import IntVar, ttk
from voiceRecognition import hear
from openAi import Travis
import threading
with open('./data/apikey.txt') as key:
    api = key.readline()
    
mybot = Travis(api)

def ask():

    try:
        my_query = hear()
        info_label["text"] = "Status: Processing..."
        try:
            mybot.hello('text-davinci-002', my_query)
        except:
            pass
        info_label["text"] = "Status: OK"
        if check.get() == 1:
            mybot.save('./records/')
    except:
        info_label["text"] = "Status: Error!"
        

def schedule_check(t):
    """
    Schedule the execution of the `check_if_done()` function after
    one second.
    """
    root.after(1000, check_if_done, t)


def check_if_done(t):
    # If the thread has finished, re-enable the button and show a message.
    if not t.is_alive():
        info_label["text"] = ""
        download_button["state"] = "normal"
    else:
        # Otherwise check again after one second.
        schedule_check(t)

# t = threading.Thread(target=ask)
# t.start()
def download_file():

    info_label["text"] = "Status: Listening..."
    # Disable the button while downloading the file.
    download_button["state"] = "disabled"
    # Start the download in a new thread.
    t = threading.Thread(target=ask)
    t.start()
    # Start checking periodically if the thread has finished.
    schedule_check(t)


root = tk.Tk()
root.title("Ask Open AI")
root.geometry("250x200")
check = IntVar()
tick = ttk.Checkbutton(text='save response', variable=check)

info_label = ttk.Label(text="Status: Idle")
info_label.pack(side="top")
tick.pack()

download_button = ttk.Button(text="Ask Me", command=download_file)
download_button.pack(pady=50)

cred = ttk.Label(text="github.com/Anas Dew")
cred.pack(anchor='s', pady=3, side="bottom")

root.mainloop()