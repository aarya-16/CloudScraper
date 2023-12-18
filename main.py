from tkinter import *
from tkcalendar import Calendar
from scraping import scrape_price
from selenium.webdriver.common.by import By
from selenium import webdriver


def on_date_select(cal, date_label):
    global depVar
    depVar = cal._sel_date
    selected_date = cal._sel_date
    date_label.config(text=f"Selected Date: {selected_date}")


def to_select():
    global toVar
    toVar = to_.get('1.0', 'end-1c')
    print(toVar)


def from_select():
    global fromVar
    fromVar = from_.get('1.0', 'end-1c')
    print(fromVar)


root = Tk()
root.grid()
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.geometry('675x500')
root.resizable(width=False,height=False)
frame = Frame(root)

frame.grid(row=0, column=0)
toVar = StringVar()
fromVar = StringVar()
depVar = StringVar()
arrVar = StringVar()

fromLabel = Label(frame, text="From: ")
fromLabel.grid(row=0, column=0)
from_ = Text(frame, height="1", width=50)
from_.grid(row=0, column=1)
fromButton = Button(frame, text='Select', command=from_select, bg='white')
fromButton.grid(row=0, column=2)

toLabel = Label(frame, text="To: ")
toLabel.grid(row=1, column=0)
to_ = Text(frame, height="1", width=50)
to_.grid(row=1, column=1)
toButton = Button(frame, text='Select', command=to_select, bg='white')
toButton.grid(row=1, column=2)

depLabel = Label(frame, text="Departure date: ")
depLabel.grid(row=2, column=0)
cal1 = Calendar(frame, selectmode="day")
cal1.grid(row=2, column=1)

select_button1 = Button(frame, text="Select Date", command=lambda: on_date_select(cal1, date_label), bg='white')
select_button1.grid(row=3, column=1)

date_label = Label(frame, text="Selected Date: ")
date_label.grid(row=2, column=2)

# arrLabel = Label(frame, text="Arrival date: ")  # Fix label text
# arrLabel.grid(row=4, column=0)
# cal2 = Calendar(frame, selectmode="day")
# cal2.grid(row=4, column=1)
#
# select_button2 = Button(frame, text="Select Date", command=lambda: on_date_select(cal2, date_label2), bg='white')
# select_button2.grid(row=5, column=1)
#
# date_label2 = Label(frame, text="Selected Date: ")
# date_label2.grid(row=4, column=2)
# print(toVar.get())
final_button = Button(frame, text="Fly!!", command=lambda: scrape_price(toVar, fromVar, depVar), bg='coral',height=2,width=5)
final_button.grid(row=10, column=1,pady=100)

root.mainloop()
