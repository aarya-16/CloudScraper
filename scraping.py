from selenium.webdriver.common.by import By
from selenium import webdriver
from display import display
from international import scrape_price_i


def scrape_price(dep, arr, travel_date, adult, child, infant, seat):
    # try:
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--window-size=1920,1080')
    #     chrome_options.add_argument('--headless')
    #     driver = webdriver.Chrome(options=chrome_options)
    #     # driver = webdriver.Chrome()
    #
    #     source = dep.upper()
    #     destination = arr.upper()
    #     # passenger_count = "1"
    #     adult_count = adult
    #     child_count = child
    #     infant_count = infant
    #     seat_type = seat[0]
    #     travel_date = travel_date
    #
    #     driver.get(
    #         f"https://tickets.paytm.com/flights/flightSearch/{source}/{destination}/{adult_count}/{child_count}/{infant_count}/{seat_type}/{travel_date}/")
    #     driver.minimize_window()
    #     driver.implicitly_wait(10)
    #
    #     flights_count = len(driver.find_elements(By.CLASS_NAME, "_2MkSl"))
    #     total_flights = min(25, flights_count)
    #
    #     prices = driver.find_elements(By.CLASS_NAME, "_2MkSl")[:total_flights]
    #     carrier_name = driver.find_elements(By.CLASS_NAME, "_2cP56")[:total_flights]
    #     dep_time = []
    #     flight_duration = driver.find_elements(By.CLASS_NAME, "_1J4f_")[:total_flights]
    #     arr_time = []
    #     time = driver.find_elements(By.CLASS_NAME, "_3x8TR")[:(2 * total_flights)]
    #     more_details = driver.find_elements(By.CLASS_NAME, "_3U68I")[:total_flights]
    #
    #     flight_codes = []
    #     for element in more_details:
    #         element.click()
    #         codes = driver.find_elements(By.CSS_SELECTOR, "._3tMEB span")
    #         flight_codes.append(codes[1].text)
    #
    #     print(f"Total flights found: {total_flights}")
    #
    #     for index in range(len(time)):
    #         j = index + 1
    #         if j % 2 == 1:
    #             dep_time.append(time[index].text.replace('\n', ' '))
    #         else:
    #             arr_time.append(time[index].text.replace('\n', ' '))
    #
    #     dict_list = []
    #
    #     for flight in range(len(prices)):
    #         flight_info_dict = {'Airline': carrier_name[flight].text, 'Flight Code': flight_codes[flight],
    #                             'Departure time': dep_time[flight], 'Arrival time': arr_time[flight],
    #                             'Flight duration': flight_duration[flight].text,
    #                             'Price': prices[flight].text}
    #         dict_list.append(flight_info_dict)
    #     # driver.close()
    #     display(dict_list)
    # except:
    #     scrape_price_i(source, destination, travel_date,adult_count,child_count,infant_count,seat_type)

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()

    source = dep.upper()
    destination = arr.upper()
    adult_count = adult
    child_count = child
    infant_count = infant
    seat_type = seat[0]
    travel_date = travel_date

    driver.get(
        f"https://tickets.paytm.com/flights/flightSearch/{source}/{destination}/{adult_count}/0/0/E/{travel_date}/{travel_date}")
    driver.minimize_window()
    driver.implicitly_wait(10)

    # flights_count = len(driver.find_elements(By.CLASS_NAME, "_3YkZQ"))
    # total_flights = min(25, flights_count)

    prices = driver.find_elements(By.CLASS_NAME, "_3YkZQ")  # [:total_flights]
    carrier_name = driver.find_elements(By.CLASS_NAME, "_3Tmlu")  # [:total_flights]
    dep_time = []
    flight_duration = driver.find_elements(By.CLASS_NAME, "_12xh6")  # [:total_flights]
    arr_time = []
    time = driver.find_elements(By.CLASS_NAME, "_2JyKP")  # [:(2 * total_flights)]
    # more_details = driver.find_elements(By.CLASS_NAME, "_3U68I")[:total_flights]
    # stops = driver.find_elements(By.CLASS_NAME, "_25GnP _1VjNa")[:total_flights]

    # flight_codes = driver.find_elements(By.CSS_SELECTOR, "_1VM2t span")
    # for element in more_details:
    #     element.click()
    #     codes = driver.find_elements(By.CSS_SELECTOR, "._3tMEB span")
    #     flight_codes.append(codes[1].text)
    #     close = driver.find_element(By.CLASS_NAME, "_3wyJs")
    #     close.click()

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
