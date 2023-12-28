from selenium.webdriver.common.by import By
from selenium import webdriver
from display import display
from international import scrape_price_i
import traceback 

def scrape_price(dep, arr, travel_date, adult, child, infant, seat):
    
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        

        source = dep.upper()
        destination = arr.upper()
        adult_count = adult
        child_count = child
        infant_count = infant
        seat_type = seat[0]
        travel_date = travel_date

        driver.get(
            f"https://tickets.paytm.com/flights/flightSearch/{source}/{destination}/{adult_count}/0/0/{seat_type}/{travel_date}/{travel_date}")
        driver.minimize_window()
        driver.implicitly_wait(10)


        prices = driver.find_elements(By.CLASS_NAME, "_3YkZQ")  
        carrier_name = driver.find_elements(By.CLASS_NAME, "_3Tmlu")  
        dep_time = []
        flight_duration = driver.find_elements(By.CLASS_NAME, "_12xh6")  
        arr_time = []
        time = driver.find_elements(By.CLASS_NAME, "_2JyKP") 
       

        for index in range(len(time)):
            j = index + 1
            if j % 2 == 1:
                dep_time.append(time[index].text.replace('\n', ' '))
            else:
                arr_time.append(time[index].text.replace('\n', ' '))

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
        # print(dict_list)
        display(dict_list,travel_date)
    except:
        traceback.print_exc() 
        scrape_price_i(dep, arr, travel_date, adult, child, infant, seat)