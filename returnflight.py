from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import *
from display import displayr

def scrape_price(dep, arr, travel_date, adult, seat,ret):
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    source = dep.upper()
    destination = arr.upper()
    passenger_count = adult
    return_date = ret

    driver.get(
        f"https://tickets.paytm.com/flights/flightSearch/{source}/{destination}/{passenger_count}/0/0/{seat[0]}/{travel_date}/{return_date}")
    driver.implicitly_wait(10)

    prices = driver.find_elements(By.CLASS_NAME, "_3YkZQ")
    carrier_name = driver.find_elements(By.CLASS_NAME, "_3Tmlu")
    dep_time = []
    flight_duration = driver.find_elements(By.CLASS_NAME, "_12xh6")
    arr_time = []
    time = driver.find_elements(By.CLASS_NAME, "_2JyKP")
    

    print(len(prices), len(carrier_name), len(dep_time), len(flight_duration),
        len(arr_time))

    for index in range(len(time)):
        j = index + 1
        if j % 2 == 1:
            dep_time.append(time[index].text.replace('\n', ' '))
        else:
            arr_time.append(time[index].text.replace('\n', ' '))

    print(len(dep_time), len(arr_time))

    dict_list = []

    for flight in range(len(prices)):
        flight_info_dict = {'Airline': carrier_name[flight].text.split('\n')[0],
                            'Flight code': carrier_name[flight].text.split('\n')[1],
                            'Departure time': dep_time[flight],
                            'Arrival time': arr_time[flight],
                            'Flight duration': flight_duration[flight].text.split('\n')[0],
                            'Stops': flight_duration[flight].text.split('\n')[1],
                            'Price': prices[flight].text}
        dict_list.append(flight_info_dict)

    returning_flights = []
    for flight in dict_list:
        if flight['Arrival time'][-3:] == source:
            returning_flights.append(flight)
            dict_list.remove(flight)
    if(len(dep_time)!=0):
        displayr(returning_flights,dict_list,travel_date)
    else: 
        messagebox.showerror("error", "International return flights not implemented yet")
        
        
    