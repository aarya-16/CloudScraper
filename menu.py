from tkinter import *
from tkinter import font
def main ():
    home = Tk()
    bg = PhotoImage(file='bg.png')
    home.title("Welcome Page")
    home.minsize(width = 1370, height = 700)
    home.maxsize(width = 1370, height = 700)
    root= Frame(home,image=bg)
    font.families()
    button = Label(root, text = "Welcome to CloudScraper", width = 150, height = 5, relief=FLAT,font=('Cascadia Mono',32))
    button.pack(padx = 1, pady = 11 )

    username_frame = Frame(root)
    
    label = Label(username_frame, text="What kind of flight will you take today?",font=('Segoe UI',12))
    label.pack(side=LEFT)
    username_frame.pack()
    button_frame = Frame(root)
    button2 = Button(button_frame, text = "One-Way", width = 30, height = 1)
    button2.pack(padx = 10, pady= 20,side=LEFT )
    button2 = Button(button_frame, text = "Return", width = 30, height = 1)
    button2.pack(padx = 10, pady= 20,side=LEFT )
    button_frame.pack()
    root.mainloop()

if __name__ == "__main__":
    main()