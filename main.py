from tkinter import simpledialog
import tkinter as tk
from PIL import Image, ImageTk
import time
from pygame import mixer

name = str(simpledialog.askstring("UserName", "Please enter your name:"))

def write_(ti, *te):
    with open(f"{ti}.log","a") as f:
        s_ti = str(ti)
        s_te = str(te)
        f.write(s_ti + s_te)
        f.close()
click = 0
window = tk.Tk()
window.overrideredirect(True)
window.iconbitmap("apple_.png")
window.geometry('97x107+30+50')
image1 = ImageTk.PhotoImage(Image.open('apple.png'))
image2 = ImageTk.PhotoImage(Image.open('apple_.png'))
def play_sound():
    mixer.init()
    mixer.music.load('sound.wav')
    mixer.music.play()
def onclick():
    global click
    global str_name
    play_sound()
    button.config(image=image2)
    window.geometry('154x149+0+0')
    window.update()
    click += 1
    print("apple was clicked {} time(s)".format(click))
    write_(name, str(click) + time.strftime("  %H:%M:%S"))
    time.sleep(0.2)
    button.config(image=image1)
    window.geometry('97x107+30+50')
    window.update()
button = tk.Button(window, image=image1, command=onclick)
button.pack()


window.mainloop()