from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

source = input("Enter departure airport: ").upper()
destination = input("Enter arrival airport: ").upper()
passenger_count = input("Enter number of passengers: ")
travel_date = input("Enter travel date in yyyy-mm-dd form:  ")
return_date = input("Enter return date in yyyy-mm-dd form: ")

driver.get(
    f"https://tickets.paytm.com/flights/flightSearch/{source}/{destination}/{passenger_count}/0/0/E/{travel_date}/{return_date}")
driver.minimize_window()
driver.implicitly_wait(10)

# flights_count = len(driver.find_elements(By.CLASS_NAME, "_3YkZQ"))
# total_flights = min(25, flights_count)

prices = driver.find_elements(By.CLASS_NAME, "_3YkZQ")#[:total_flights]
carrier_name = driver.find_elements(By.CLASS_NAME, "_3Tmlu")#[:total_flights]
dep_time = []
flight_duration = driver.find_elements(By.CLASS_NAME, "_12xh6")#[:total_flights]
arr_time = []
time = driver.find_elements(By.CLASS_NAME, "_2JyKP")#[:(2 * total_flights)]
# more_details = driver.find_elements(By.CLASS_NAME, "_3U68I")[:total_flights]
# stops = driver.find_elements(By.CLASS_NAME, "_25GnP _1VjNa")[:total_flights]

# flight_codes = driver.find_elements(By.CSS_SELECTOR, "_1VM2t span")
# for element in more_details:
#     element.click()
#     codes = driver.find_elements(By.CSS_SELECTOR, "._3tMEB span")
#     flight_codes.append(codes[1].text)
#     close = driver.find_element(By.CLASS_NAME, "_3wyJs")
#     close.click()

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

for flight in dict_list:
    print(flight)
