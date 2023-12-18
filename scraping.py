from selenium.webdriver.common.by import By
from selenium import webdriver
from display import display


def scrape_price(dep, arr, travel_date):
    driver = webdriver.Chrome()

    source = dep.upper()
    destination = arr.upper()
    passenger_count = "1"
    travel_date = travel_date

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
    time = driver.find_elements(By.CLASS_NAME, "_3x8TR")[:(2 * total_flights)]
    more_details = driver.find_elements(By.CLASS_NAME, "_3U68I")[:total_flights]

    flight_codes = []
    for element in more_details:
        element.click()
        codes = driver.find_elements(By.CSS_SELECTOR, "._3tMEB span")
        flight_codes.append(codes[1].text)

    print(f"Total flights found: {total_flights}")

    for index in range(len(time)):
        j = index + 1
        if j % 2 == 1:
            dep_time.append(time[index].text.replace('\n', ' '))
        else:
            arr_time.append(time[index].text.replace('\n', ' '))

    dict_list = []

    for flight in range(len(prices)):
        flight_info_dict = {'Airline': carrier_name[flight].text, 'Flight Code': flight_codes[flight],
                            'Departure time': dep_time[flight], 'Arrival time': arr_time[flight],
                            'Flight duration': flight_duration[flight].text,
                            'Price': prices[flight].text}
        dict_list.append(flight_info_dict)
    driver.close()
    display(dict_list)
