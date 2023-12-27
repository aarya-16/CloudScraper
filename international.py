from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

source = input("Enter departure airport: ").upper()
destination = input("Enter arrival airport: ").upper()
passenger_count = input("Enter number of passengers: ")
travel_date = input("Enter travel date in yyyy-mm-dd form:  ")

driver.get(
    f"https://tickets.paytm.com/flights/flightSearch/{source}/{destination}/{passenger_count}/0/0/E/{travel_date}/")
driver.minimize_window()
driver.implicitly_wait(10)

flights_count = len(driver.find_elements(By.CLASS_NAME, "_2MkSl"))
total_flights = min(25, flights_count)

prices = driver.find_elements(By.CLASS_NAME, "_2MkSl")[:total_flights]
carrier_name = driver.find_elements(By.CLASS_NAME, "_2cP56")[:total_flights]
dep_time = []
flight_duration = driver.find_elements(By.CLASS_NAME, "_1J4f_")[:total_flights]
arr_time = []
time = driver.find_elements(By.CLASS_NAME, "_29g4q")[:(2*total_flights)]
more_details = driver.find_elements(By.CLASS_NAME, "_3U68I")[:total_flights]
stops = driver.find_elements(By.CLASS_NAME, "_1FfRE")[:total_flights]

# prices.extend(driver.find_elements(By.CLASS_NAME, "_2RNuC"))
# carrier_name.extend(driver.find_elements(By.CLASS_NAME, "cBm7W"))
# flight_duration.extend(driver.find_elements(By.CLASS_NAME, "QPbNf"))
# time.extend(driver.find_elements(By.CLASS_NAME, "_4Q7O5"))
# more_details.extend(driver.find_elements(By.CLASS_NAME, "_3WBGO"))
# stops.extend(driver.find_elements(By.CLASS_NAME, "_2_3yg"))

flight_codes = []
for element in more_details:
    element.click()
    codes = driver.find_elements(By.CSS_SELECTOR, "._3tMEB span")
    flight_codes.append(codes[1].text)
    close = driver.find_element(By.CLASS_NAME, "_3wyJs")
    close.click()

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
    flight_info_dict = {'Airline': carrier_name[flight].text, 'Flight code': flight_codes[flight],
                        'Departure time': dep_time[flight],
                        'Arrival time': arr_time[flight], 'Flight duration': flight_duration[flight].text,
                        'Stops': stops[flight].text, 'Price': prices[flight].text}
    dict_list.append(flight_info_dict)

for flight in dict_list:
    # if flight['Stops'] == 'Non-Stop' and flight['Arrival time'][-3:] == destination:
    print(flight)

