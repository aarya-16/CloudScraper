from tkinter import *
from tkcalendar import Calendar
from scraping import scrape_price
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import ttk
import sqlite3


con = sqlite3.connect('iata.db')
cur = con.cursor()
cur.execute("DELETE FROM Sheet1 WHERE [City name] = 'City name'")
rows = cur.fetchall()
print(rows)


def checkkey(event,lb): 
    value = event.widget.get() 
    if value == '': 
        data = l 
    else: 
        data = [item for item in l if item is not None and value.lower() in item.lower()] 
    update(data,lb) 

def update(data,lb): 
    lb.delete(0, 'end') 
    for item in data: 
        lb.insert('end', item) 

def on_listbox_click(event,lb,e):
    selected_index = lb.curselection()
    if selected_index:
        selected_item = lb.get(selected_index)
        e.delete(0, 'end')
        e.insert(0, selected_item)

r = cur.execute('SELECT * FROM Sheet1') 
w = r.fetchall()
l = ['|'.join(str(item) for item in t if item is not None) for t in w]
con.commit()

root = Tk()
root.grid()
root.geometry('900x550')
root.resizable(width=False,height=False)


frame = Frame(root)


frame.grid(row=0, column=0)
toVar = StringVar()
fromVar = StringVar()
depVar = StringVar()
arrVar = StringVar()

fromLabel = Label(frame, text="From: ")
fromLabel.grid(row=0, column=0,pady=10) 

from_e = Entry(frame,width=50)
from_e.grid(row=0, column=1)
from_e.bind('<KeyRelease>', lambda event: checkkey(event,from_lb)) 

from_lb = Listbox(frame,width=50,height=5) 
from_lb.grid(row=1, column=1) 
update(l,from_lb)
from_lb.bind('<ButtonRelease-1>', lambda event: on_listbox_click(event,from_lb,from_e))

toLabel = Label(frame, text="To: ")
toLabel.grid(row=0, column=2,pady=10)

to_e = Entry(frame,width=50)
to_e.grid(row=0, column=3)
to_e.bind('<KeyRelease>', lambda event: checkkey(event,to_lb)) 

to_lb = Listbox(frame,width=50,height=5) 
to_lb.grid(row=1, column=3) 
update(l,to_lb)
to_lb.bind('<ButtonRelease-1>', lambda event: on_listbox_click(event,to_lb,to_e))

depLabel = Label(frame, text="Departure date: ")
depLabel.grid(row=4, column=0,pady=10)

cal1 = Calendar(frame, selectmode="day")
cal1.grid(row=4, column=1,pady=10)

arrLabel = Label(frame, text="Arrival date: ")  
arrLabel.grid(row=4, column=2)

cal2 = Calendar(frame, selectmode="day")
cal2.grid(row=4, column=3)


seat_label = Label(frame,text='Type of seat: ')
seat_label.grid(row=6,column=0,pady=10,columnspan=2)

seat_select = ttk.Combobox(frame,state="readonly",values=["Economy", "Premium Economy", "Business"])
seat_select.grid(row=6,column=2,pady=10)

passenger_label = Label(frame,text='Passenger Info')
passenger_label.grid(row=7,column=1,pady=10,padx=5,columnspan=3)

adult_label = Label(frame,text='Number of adults')
adult_label.grid(row=8,column=0,pady=10,columnspan=2)

adult_select = Spinbox(frame, from_= 1, to = 25,state='readonly')
adult_select.grid(row=8,column=2,pady=10)

final_button = Button(frame, text="Fly!!", command=lambda: scrape_price( from_e.get().split('|')[1],to_e.get().split('|')[1],cal1._sel_date,adult_select.get(),seat_select.get(),cal2._sel_date), bg='coral',height=2,width=5)
final_button.grid(row=11, column=1,pady=10,columnspan=3)

    
root.mainloop()