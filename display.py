from tkinter import *
from tkinter import ttk

def display(dict_list):
    root = Tk()
    root.geometry('1200x600')  # Increase the dimensions of the root window
    root.title("Flight Information")  # Set a title for the window
    root.configure(bg='white')  # Set root window background to white

    def update_table(frame4, dict_list):
        column = ("Airline", "Flight Code", "Departure Time", "Arrival Time", "Duration", "Price")

        # Remove existing widgets in frame4
        for widget in frame4.winfo_children():
            widget.destroy()

        style = ttk.Style()
        style.configure("Treeview", font=('Segoe UI', 18),)  # Set font for the table

        table = ttk.Treeview(frame4, columns=column, show="headings", style="Treeview")

        table.heading("Airline", text="Airline")
        table.heading("Flight Code", text="Flight Code")
        table.heading("Departure Time", text="Departure Time")
        table.heading("Arrival Time", text="Arrival Time")
        table.heading("Duration", text="Duration")
        table.heading("Price", text="Price")

        # Adjust column widths
        table.column("Airline", width=150)
        table.column("Flight Code", width=100)
        table.column("Departure Time", width=150)
        table.column("Arrival Time", width=150)
        table.column("Duration", width=100)
        table.column("Price", width=100)

        tab = []
        for flight in dict_list:
            tab.append((flight['Airline'], flight['Flight Code'], flight['Departure time'], flight['Arrival time'],
                        flight['Flight duration'], flight['Price']))

        for val in tab:
            table.insert("", END, values=val,tags=('center',))
                    
        table.grid(row=0, column=0, sticky="nsew")

    frame = Frame(root, bg='white')
    frame.pack(fill="both", expand=True)

    # Configure row and column weights to make the frame and table expandable
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    update_table(frame, dict_list)

    root.mainloop()


