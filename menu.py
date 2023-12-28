from tkinter import *
from main import main_o
from return_main import r_main

def main():
    home = Tk()

    home.title("Welcome Page")
    home.geometry('1070x450')
    home.configure(bg='SkyBlue')
    root = Frame(home,bg='SkyBlue')

    button = Label(root, text="Welcome to CloudScraper", width=150, height=5, relief=FLAT, font=('Cascadia Mono', 32),bg='SkyBlue')
    button.pack(padx=1, pady=11)

    frame1 = Frame(root,bg='SkyBlue')

    label = Label(frame1, text="What kind of flight will you take today?", font=('Segoe UI', 12),bg='SkyBlue')
    label.pack(side=LEFT)
    frame1.pack()

    frame2 = Frame(root,bg='SkyBlue')
    button2 = Button(frame2, text="One-Way", width=30, height=1,command=main_o,bg='White')
    button2.pack(padx=10, pady=20, side=LEFT)
    
    button2 = Button(frame2, text="Return", width=30, height=1,command=r_main,bg='White')
    button2.pack(padx=10, pady=20, side=LEFT)
    frame2.pack()

    root.pack()  

    home.mainloop()

if __name__ == "__main__":
    main()
