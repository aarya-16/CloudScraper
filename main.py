from tkinter import *
from tkcalendar import Calendar
from scraping import scrape_price
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import ttk

# def on_date_select(cal, date_label):
#     global depVar
#     depVar = cal._sel_date
#     selected_date = cal._sel_date
#     date_label.config(text=f"Selected Date: {selected_date}")


# def to_select():
#     global toVar
#     toVar = to_.get('1.0', 'end-1c')
#     print(toVar)


# def from_select():
#     global fromVar
#     fromVar = from_.get('1.0', 'end-1c')
#     print(fromVar)

###########################################################################################################################################################
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
# root = Tk() 

# e = Entry(root) 
# e.pack() 
# e.bind('<KeyRelease>', checkkey) 

# lb = Listbox(root) 
# lb.pack() 
# update(l)

# # Bind the listbox click event to the on_listbox_click function
# lb.bind('<ButtonRelease-1>', on_listbox_click)

# root.mainloop()

###########################################################################################################################################################


# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)
# root.grid_rowconfigure(3, weight=1)
# root.grid_rowconfigure(4, weight=1)
# root.grid_rowconfigure(5, weight=1)
# root.grid_columnconfigure(3, weight=1)
# root.grid_columnconfigure(4, weight=1)
# root.grid_columnconfigure(5, weight=1)
root = Tk()
root.grid()
root.geometry('525x800')
root.resizable(width=False,height=False)
frame = Frame(root)

# e = Entry(root) 
# e.pack() 
# e.bind('<KeyRelease>', checkkey) 

# lb = Listbox(root) 
# lb.pack() 
# update(l)

# # Bind the listbox click event to the on_listbox_click function
# lb.bind('<ButtonRelease-1>', on_listbox_click)



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
# from_ = Text(frame, height="1", width=50)
# from_.grid(row=0, column=1,pady=10)
# fromButton = Button(frame, text='Select', command=from_select, bg='white')
# fromButton.grid(row=0, column=2,pady=10)

toLabel = Label(frame, text="To: ")
toLabel.grid(row=2, column=0,pady=10)
to_e = Entry(frame,width=50)
to_e.grid(row=2, column=1)
to_e.bind('<KeyRelease>', lambda event: checkkey(event,to_lb)) 
to_lb = Listbox(frame,width=50,height=5) 
to_lb.grid(row=3, column=1) 
update(l,to_lb)
to_lb.bind('<ButtonRelease-1>', lambda event: on_listbox_click(event,to_lb,to_e))
# to_ = Text(frame, height="1", width=50)
# to_.grid(row=1, column=1,pady=10)
# toButton = Button(frame, text='Select', command=to_select, bg='white')
# toButton.grid(row=1, column=2,pady=10)

depLabel = Label(frame, text="Departure date: ")
depLabel.grid(row=4, column=0,pady=10)
cal1 = Calendar(frame, selectmode="day")
cal1.grid(row=4, column=1,pady=10)

# select_button1 = Button(frame, text="Select Date", command=lambda: on_date_select(cal1, date_label), bg='white')
# select_button1.grid(row=3, column=1,pady=10)

# date_label = Label(frame, text="Selected Date: ")
# date_label.grid(row=2, column=2,pady=10)

seat_label = Label(frame,text='Type of seat: ')
seat_label.grid(row=5,column=0,pady=10)

seat_select = ttk.Combobox(frame,state="readonly",values=["Economy", "Premium Economy", "Business"])
seat_select.grid(row=5,column=1,pady=10)

passenger_label = Label(frame,text='Passenger Info')
passenger_label.grid(row=6,column=1,pady=10,padx=50)

adult_label = Label(frame,text='Number of adults')
adult_label.grid(row=7,column=0,pady=10)

adult_select = Spinbox(frame, from_= 1, to = 25,state='readonly')
adult_select.grid(row=7,column=1,pady=10)

child_label = Label(frame,text='Number of children')
child_label.grid(row=8,column=0,pady=10)

child_select = Spinbox(frame, from_= 0, to = 25,state='readonly')
child_select.grid(row=8,column=1,pady=10)


infant_label = Label(frame,text='Number of infants')
infant_label.grid(row=9,column=0,pady=10)

infant_select = Spinbox(frame, from_= 0, to = 25,state='readonly')
infant_select.grid(row=9,column=1,pady=10)
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

final_button = Button(frame, text="Fly!!", command=lambda: scrape_price( from_e.get().split('|')[1],to_e.get().split('|')[1],cal1._sel_date,adult_select.get(),child_select.get(),infant_select.get(),seat_select.get()), bg='coral',height=2,width=5)
final_button.grid(row=10, column=1,pady=10)

    
root.mainloop()
