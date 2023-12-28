from tkinter import *
from tkinter import ttk

from graph import make_plot

def displayr(dict_list1,dict_list,date):
    root = Toplevel()
    root.title("Flight Information")
    root.configure(bg='white')

    frame = Frame(root)
    frame.pack(fill="both", expand=True)

    # Configure row and column weights to make the frame and table expandable
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    source = dict_list[0]["Departure time"][-3:]
    dest = dict_list[0]["Arrival time"][-3:]
    
    
    journey_label = Label(frame, text=f'{source} to {dest}', font=('Courier', 14))
    journey_label.grid(row=0, column=0, sticky=NSEW)

    column = ("Airline", "Flight Code", "Departure Time", "Arrival Time", "Duration", "Price")

    style = ttk.Style(frame) 
    style.theme_use("alt") # set theam to clam
    style.configure("Treeview", background="black", 
                    fieldbackground="black", foreground="white")
    style.configure('Treeview.Heading', background="coral",relief='flat')
    table = ttk.Treeview(frame, columns=column, show="headings", style="Treeview")


    for col in column:
        table.heading(col, text=col)

    # Adjust column widths
    table.column("Airline", width=150)
    table.column("Flight Code", width=100)
    table.column("Departure Time", width=150)
    table.column("Arrival Time", width=150)
    table.column("Duration", width=100)
    table.column("Price", width=100)

    tab = [(flight['Airline'], flight['Flight code'], flight['Departure time'], flight['Arrival time'],
            flight['Flight duration'], flight['Price']) for flight in dict_list]

    for val in tab:
        table.insert("", END, values=val, tags=('center',))

    table.grid(row=1, column=0, sticky="nsew",columnspan=2)

    g_button = Button(frame,text='SEE HOW PRICES VARY FOR THE NEXT MONTH',command=lambda: make_plot(source,dest,date))
    g_button.grid(row=2,column=0,sticky=NSEW)
    
    close_button = Button(frame,text='Close',command=lambda:[root.destroy(),display(dict_list1,date)])
    close_button.grid(row=2,column=1,sticky=NSEW)
    root.mainloop()
    
    
def display(dict_list,date):
    root = Toplevel()
    root.title("Flight Information")
    root.configure(bg='white')

    frame = Frame(root)
    frame.pack(fill="both", expand=True)

    # Configure row and column weights to make the frame and table expandable
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    source = dict_list[0]["Departure time"][-3:]
    dest = dict_list[0]["Arrival time"][-3:]
    
    
    journey_label = Label(frame, text=f'{source} to {dest}', font=('Courier', 14))
    journey_label.grid(row=0, column=0, sticky=NSEW)

    column = ("Airline", "Flight Code", "Departure Time", "Arrival Time", "Duration", "Price")

    style = ttk.Style(frame) 
    style.theme_use("alt") # set theam to clam
    style.configure("Treeview", background="black", 
                    fieldbackground="black", foreground="white")
    style.configure('Treeview.Heading', background="coral",relief='flat')
    table = ttk.Treeview(frame, columns=column, show="headings", style="Treeview")


    for col in column:
        table.heading(col, text=col)

    # Adjust column widths
    table.column("Airline", width=150)
    table.column("Flight Code", width=100)
    table.column("Departure Time", width=150)
    table.column("Arrival Time", width=150)
    table.column("Duration", width=100)
    table.column("Price", width=100)

    tab = [(flight['Airline'], flight['Flight code'], flight['Departure time'], flight['Arrival time'],
            flight['Flight duration'], flight['Price']) for flight in dict_list]

    for val in tab:
        table.insert("", END, values=val, tags=('center',))

    table.grid(row=1, column=0, sticky="nsew",columnspan=2)

    g_button = Button(frame,text='SEE HOW PRICES VARY FOR THE NEXT MONTH',command=lambda: make_plot(source,dest,date))
    g_button.grid(row=2,column=0,sticky=NSEW)
    
    close_button = Button(frame,text='Close',command=root.destroy)
    close_button.grid(row=2,column=1,sticky=NSEW)
    root.mainloop()
