from tkinter import *
from tkinter import ttk

def display(dict_list,date):
    root = Tk()
    root.title("Flight Information")
    root.configure(bg='white')

    frame = Frame(root)
    frame.pack(fill="both", expand=True)

    # Configure row and column weights to make the frame and table expandable
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    source = dict_list[0]["Departure time"][-3:]
    dest = dict_list[0]["Arrival time"][-3:]
    date = dict_list[0][""]
    
    journey_label = Label(frame, text=f'{source} to {dest}', font=('Courier', 14))
    journey_label.grid(row=0, column=0, sticky=NSEW)

    column = ("Airline", "Flight Code", "Departure Time", "Arrival Time", "Duration", "Price")

    style = ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview", font=('Segoe UI', 10), background="black", fieldbackground="black", foreground="white")

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

    tab = [(flight['Airline'], flight['Flight Code'], flight['Departure time'], flight['Arrival time'],
            flight['Flight duration'], flight['Price']) for flight in dict_list]

    for val in tab:
        table.insert("", END, values=val, tags=('center',))

    table.grid(row=1, column=0, sticky="nsew",columnspan=2)

    g_button = Button(frame,text='SEE HOW PRICES VARY FOR THE NEXT MONTH')
    g_button.grid(row=2,column=0,sticky=NSEW)
    
    close_button = Button(frame,text='Close',command=root.destroy)
    close_button.grid(row=2,column=1,sticky=NSEW)
    root.mainloop()
d = [{'Airline': 'SpiceJet', 'Flight Code': 'SG-8702', 'Departure time': '09:40 AM BOM', 'Arrival time': '11:40 AM DEL', 'Flight duration': '2h', 'Stops': 'Non Stop', 'Price': '₹4,519'}, {'Airline': 'SpiceJet', 'Flight Code': 'SG-8152', 'Departure time': '07:20 AM BOM', 'Arrival time': '09:30 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹4,519'}, {'Airline': 'SpiceJet', 'Flight Code': 'SG-8112', 'Departure time': '01:50 AM BOM', 'Arrival time': '04:00 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹4,519'}, {'Airline': 'Akasa Air', 'Flight Code': 'QP-1120', 'Departure time': '06:50 PM BOM', 'Arrival time': '08:55 PM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹4,752'}, {'Airline': 'Akasa Air', 'Flight Code': 'QP-1410', 'Departure time': '07:50 AM BOM', 'Arrival time': '10:10 AM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹4,752'}, {'Airline': 'Akasa Air', 'Flight Code': 'QP-1127', 'Departure time': '01:05 PM BOM', 'Arrival time': '03:15 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹4,901'}, {'Airline': 'Vistara', 'Flight Code': 'UK-960', 'Departure time': '11:55 AM BOM', 'Arrival time': '01:55 PM DEL', 'Flight duration': '2h', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-954', 'Departure time': '05:50 AM BOM', 'Arrival time': '07:55 AM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-986', 'Departure time': '10:50 PM BOM', 'Arrival time': '01:00 AM (+1d) DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-928', 'Departure time': '06:30 AM BOM', 'Arrival time': '08:40 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-930', 'Departure time': '07:30 AM BOM', 'Arrival time': '09:40 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-994', 'Departure time': '10:25 AM BOM', 'Arrival time': '12:40 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-950', 'Departure time': '09:55 PM BOM', 'Arrival time': '12:10 AM (+1d) DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-944', 'Departure time': '02:40 PM BOM', 'Arrival time': '04:55 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Vistara', 'Flight Code': 'UK-952', 'Departure time': '12:35 PM BOM', 'Arrival time': '02:55 PM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹4,916'}, {'Airline': 'Air India', 'Flight Code': 'AI-816', 'Departure time': '09:00 PM BOM', 'Arrival time': '11:10 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-888', 'Departure time': '07:00 PM BOM', 'Arrival time': '09:15 PM DEL', 
'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-809', 'Departure time': '10:00 AM BOM', 
'Arrival time': '12:15 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-864', 'Departure time': '07:00 AM BOM', 'Arrival time': '09:15 AM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-855', 'Departure time': '11:40 AM BOM', 'Arrival time': '01:55 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-677', 'Departure time': '01:00 PM BOM', 'Arrival time': '03:15 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-806', 'Departure time': '08:00 AM BOM', 'Arrival time': '10:20 AM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-687', 'Departure time': '04:00 PM BOM', 'Arrival time': '06:20 PM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-866', 'Departure time': '09:00 AM BOM', 'Arrival time': '11:20 AM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India', 'Flight Code': 'AI-859', 'Departure time': '01:30 AM BOM', 'Arrival time': '04:00 AM DEL', 'Flight duration': '2h 30m', 'Stops': 'Non Stop', 'Price': '₹4,943'}, {'Airline': 'Air India Express', 'Flight Code': 'I5-338', 'Departure time': '06:25 PM BOM', 'Arrival time': '11:55 PM DEL', 'Flight duration': '5h 30m', 'Stops': '1 Stop (GOI)', 'Price': '₹5,195'}, {'Airline': 'Air India Express', 'Flight Code': 'I5-338', 'Departure time': '06:25 PM BOM', 
'Arrival time': '02:50 AM (+1d) DEL', 'Flight duration': '8h 25m', 'Stops': '1 Stop (GOI)', 'Price': '₹5,195'}, {'Airline': 'Air India Express', 'Flight Code': 'I5-762', 'Departure time': '12:10 PM BOM', 'Arrival time': '11:55 PM DEL', 'Flight duration': '11h 45m', 'Stops': '1 Stop (GOI)', 'Price': '₹5,195'}, {'Airline': 'Air India Express', 'Flight Code': 'I5-762', 'Departure time': '12:10 PM BOM', 'Arrival time': '02:50 AM (+1d) DEL', 'Flight duration': '14h 40m', 'Stops': '1 Stop (GOI)', 'Price': '₹5,195'}, {'Airline': 'Air India Express', 'Flight Code': 'IX-2773', 'Departure time': '11:25 PM BOM', 'Arrival time': '03:35 AM (+1d) DEL', 'Flight duration': '4h 10m', 'Stops': '1 Stop (LKO)', 'Price': '₹5,320'}, {'Airline': 'IndiGo', 'Flight Code': '6E-762', 'Departure time': '06:05 AM BOM', 'Arrival time': '08:05 AM DEL', 'Flight duration': '2h', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-301', 'Departure time': '07:00 AM BOM', 'Arrival time': '09:05 AM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-2224', 'Departure time': '11:15 PM BOM', 'Arrival time': '01:20 AM (+1d) DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-6045', 'Departure time': '02:30 AM BOM', 'Arrival time': '04:35 AM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-6082', 'Departure time': '06:00 PM BOM', 'Arrival time': '08:10 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-615', 'Departure time': '01:15 PM BOM', 'Arrival time': '03:25 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-882', 'Departure time': '05:00 PM BOM', 'Arrival time': '07:10 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-993', 'Departure time': '02:15 PM BOM', 'Arrival time': '04:25 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-333', 'Departure time': '07:45 AM BOM', 'Arrival time': '09:55 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-656', 'Departure time': '05:00 AM BOM', 'Arrival time': '07:10 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,321'}, {'Airline': 'IndiGo', 'Flight Code': '6E-2775', 'Departure time': '01:20 AM BOM', 'Arrival time': '03:20 AM DEL', 'Flight duration': '2h', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-355', 'Departure time': '08:30 AM BOM', 'Arrival time': '10:35 AM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-2326', 'Departure time': '03:30 PM BOM', 'Arrival time': '05:35 PM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-102', 'Departure time': '09:15 PM BOM', 'Arrival time': '11:20 PM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-6049', 'Departure time': '08:15 PM BOM', 'Arrival time': '10:25 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-2139', 'Departure time': '09:30 AM BOM', 'Arrival time': '11:40 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-651', 'Departure time': '10:15 PM BOM', 'Arrival time': '12:25 AM (+1d) DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-6028', 'Departure time': '12:15 PM BOM', 'Arrival time': '02:25 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,323'}, {'Airline': 'IndiGo', 'Flight Code': '6E-6613', 'Departure time': '07:15 PM BOM', 'Arrival time': '09:30 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹5,373'}, {'Airline': 'IndiGo', 'Flight Code': '6E-6821', 'Departure time': '11:00 AM BOM', 'Arrival time': '01:10 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,428'}, {'Airline': 'IndiGo', 'Flight Code': '6E-534', 'Departure time': '04:35 AM BOM', 'Arrival time': '08:25 AM DEL', 'Flight duration': '3h 50m', 'Stops': '1 Stop (AMD)', 'Price': '₹5,750'}, {'Airline': 'IndiGo', 'Flight Code': '6E-269', 'Departure time': '05:25 AM BOM', 'Arrival time': '09:35 AM DEL', 'Flight duration': '4h 10m', 'Stops': '1 Stop (BDQ)', 'Price': '₹5,750'}, {'Airline': 'IndiGo', 'Flight Code': '6E-5201', 'Departure time': '03:15 PM BOM', 'Arrival time': '08:10 PM DEL', 'Flight duration': '4h 55m', 'Stops': '1 Stop (AMD)', 'Price': '₹5,750'}, {'Airline': 'IndiGo', 'Flight Code': '6E-2347', 'Departure time': '08:15 AM BOM', 'Arrival time': '01:40 PM DEL', 'Flight duration': '5h 25m', 'Stops': '1 Stop (AMD)', 'Price': '₹5,750'}, {'Airline': 'IndiGo', 'Flight Code': '6E-5052', 'Departure time': '05:05 AM BOM', 'Arrival time': '10:45 AM DEL', 'Flight duration': '5h 40m', 'Stops': '1 Stop (JAI)', 'Price': '₹5,750'}, {'Airline': 'Air India', 'Flight Code': 'AI-637', 'Departure time': '06:35 PM BOM', 'Arrival time': '11:45 PM DEL', 'Flight duration': '5h 10m', 'Stops': '1 Stop (AMD)', 'Price': '₹5,793'}, {'Airline': 'Air India', 'Flight Code': 'AI-637', 'Departure time': '06:35 PM BOM', 'Arrival time': '03:05 PM (+1d) DEL', 'Flight duration': '20h 30m', 'Stops': '1 Stop (AMD)', 'Price': '₹5,793'}, {'Airline': 'IndiGo', 'Flight Code': '6E-5038', 'Departure time': '06:20 AM BOM', 'Arrival time': '11:15 AM DEL', 'Flight duration': '4h 55m', 'Stops': '1 Stop (UDR)', 'Price': '₹5,855'}, {'Airline': 'Air India', 'Flight Code': 'AI-816', 'Departure time': '09:00 PM BOM', 'Arrival time': '11:10 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-888', 'Departure time': '07:00 PM BOM', 'Arrival time': '09:15 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 
'AI-864', 'Departure time': '07:00 AM BOM', 'Arrival time': '09:15 AM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-809', 'Departure time': '10:00 AM BOM', 'Arrival time': '12:15 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-855', 'Departure time': '11:40 AM BOM', 'Arrival time': '01:55 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-677', 'Departure time': '01:00 PM BOM', 'Arrival time': '03:15 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-866', 'Departure time': '09:00 AM BOM', 'Arrival time': '11:20 AM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-806', 'Departure time': '08:00 AM BOM', 'Arrival time': '10:20 AM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-687', 'Departure time': '04:00 PM BOM', 'Arrival time': '06:20 PM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'Air India', 'Flight Code': 'AI-859', 'Departure time': '01:30 AM BOM', 'Arrival time': '04:00 AM DEL', 'Flight duration': '2h 30m', 'Stops': 'Non Stop', 'Price': '₹5,888'}, {'Airline': 'IndiGo', 'Flight Code': '6E-2442', 'Departure time': '11:20 AM BOM', 'Arrival time': '03:45 PM DEL', 'Flight duration': '4h 25m', 'Stops': '1 Stop (LKO)', 'Price': '₹5,907'}, {'Airline': 'IndiGo', 'Flight Code': '6E-953', 'Departure time': '03:20 PM BOM', 'Arrival time': '08:30 PM DEL', 'Flight duration': '5h 10m', 'Stops': '1 Stop (DED)', 'Price': '₹5,907'}, {'Airline': 'Air India Express', 'Flight Code': 'IX-2773', 'Departure time': '11:25 PM BOM', 'Arrival time': '10:00 AM (+1d) DEL', 'Flight duration': '10h 35m', 'Stops': '1 Stop (LKO)', 'Price': '₹5,970'}, {'Airline': 'IndiGo', 'Flight Code': '6E-5326', 'Departure time': '07:00 PM BOM', 'Arrival time': '12:05 AM (+1d) DEL', 'Flight duration': '5h 5m', 'Stops': '1 Stop (HYD)', 'Price': '₹6,012'}, {'Airline': 'IndiGo', 'Flight Code': '6E-564', 'Departure time': '04:45 AM BOM', 'Arrival time': '10:10 AM DEL', 'Flight duration': '5h 25m', 'Stops': '1 Stop (HYD)', 'Price': '₹6,012'}, {'Airline': 'IndiGo', 'Flight Code': '6E-5318', 'Departure time': '10:15 AM BOM', 'Arrival time': '03:45 PM DEL', 'Flight duration': '5h 30m', 'Stops': '1 Stop (HYD)', 'Price': '₹6,012'}, {'Airline': 'IndiGo', 'Flight Code': '6E-5228', 'Departure time': '05:05 PM BOM', 'Arrival time': '10:40 PM DEL', 'Flight duration': '5h 35m', 'Stops': '1 Stop (HYD)', 'Price': '₹6,012'}, {'Airline': 'Air India', 'Flight Code': 'AI-617', 'Departure time': '11:00 AM BOM', 'Arrival time': '04:25 PM DEL', 'Flight duration': '5h 25m', 'Stops': '1 Stop (HYD)', 'Price': '₹6,276'}, {'Airline': 'Air India', 'Flight Code': 'AI-637', 'Departure time': '06:35 PM BOM', 'Arrival time': '11:45 PM DEL', 'Flight duration': '5h 10m', 'Stops': '1 Stop (AMD)', 'Price': '₹6,318'}, {'Airline': 'Air India', 'Flight Code': 'AI-637', 'Departure time': '06:35 PM BOM', 'Arrival time': '03:05 PM (+1d) DEL', 'Flight duration': '20h 30m', 'Stops': '1 Stop (AMD)', 'Price': '₹6,318'}, {'Airline': 'Air India', 'Flight Code': 'AI-637', 'Departure time': '06:35 PM BOM', 'Arrival time': '08:30 PM (+1d) DEL', 'Flight duration': '25h 55m', 'Stops': '1 Stop (AMD)', 'Price': '₹6,339'}, {'Airline': 'Air India Express', 'Flight Code': 'I5-334', 'Departure time': '10:10 PM BOM', 'Arrival time': '07:30 AM (+1d) DEL', 'Flight duration': '9h 20m', 'Stops': '1 Stop (JAI)', 'Price': '₹6,382'}, {'Airline': 'Vistara', 'Flight Code': 'UK-960', 'Departure time': '11:55 AM BOM', 'Arrival time': '01:55 PM DEL', 'Flight duration': '2h', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-954', 'Departure time': '05:50 AM BOM', 'Arrival time': '07:55 AM DEL', 'Flight duration': '2h 5m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-928', 'Departure time': '06:30 AM BOM', 'Arrival time': '08:40 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-986', 'Departure time': '10:50 PM BOM', 'Arrival time': '01:00 AM (+1d) DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-930', 'Departure time': '07:30 AM BOM', 'Arrival time': '09:40 AM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-944', 'Departure time': '02:40 PM BOM', 'Arrival time': '04:55 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-950', 'Departure time': '09:55 PM BOM', 'Arrival time': '12:10 AM (+1d) DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-994', 'Departure time': '10:25 AM BOM', 'Arrival time': '12:40 PM DEL', 'Flight duration': '2h 15m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Vistara', 'Flight Code': 'UK-952', 'Departure time': '12:35 PM BOM', 'Arrival time': '02:55 PM DEL', 'Flight duration': '2h 20m', 'Stops': 'Non Stop', 'Price': '₹6,455'}, {'Airline': 'Air India', 'Flight Code': 'AI-637', 'Departure time': '06:35 PM BOM', 'Arrival time': '08:30 PM (+1d) DEL', 'Flight duration': '25h 55m', 'Stops': '1 Stop (AMD)', 'Price': '₹6,864'}, {'Airline': 'Air India', 'Flight Code': 'AI-816', 'Departure time': '09:00 PM BOM', 'Arrival time': '11:10 PM DEL', 'Flight duration': '2h 10m', 'Stops': 'Non Stop', 'Price': '₹6,938'}]

display(d)