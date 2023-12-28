from tkinter import *
from tkinter import font

from main import main_o
from return_main import r_main

def main():
    home = Tk()

    home.title("Welcome Page")
    home.minsize(width=1370, height=700)
    home.maxsize(width=1370, height=700)

    root = Frame(home)
    font.families()

    button = Label(root, text="Welcome to CloudScraper", width=150, height=5, relief=FLAT, font=('Cascadia Mono', 32))
    button.pack(padx=1, pady=11)

    username_frame = Frame(root)

    label = Label(username_frame, text="What kind of flight will you take today?", font=('Segoe UI', 12))
    label.pack(side=LEFT)
    username_frame.pack()

    button_frame = Frame(root)
    button2 = Button(button_frame, text="One-Way", width=30, height=1,command=main_o)
    button2.pack(padx=10, pady=20, side=LEFT)
    button2 = Button(button_frame, text="Return", width=30, height=1,command=r_main)
    button2.pack(padx=10, pady=20, side=LEFT)
    button_frame.pack()

    root.pack()  # Add this line to pack the root frame

    home.mainloop()

if __name__ == "__main__":
    main()
