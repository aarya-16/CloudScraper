from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import matplotlib.pyplot as plt

def make_plot(source, destination, travel_date):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(
        f"https://tickets.paytm.com/flights/flightSearch/{source}/{destination}/1/0/0/E/{travel_date}/")
    driver.implicitly_wait(10)

    nearby_dates = driver.find_elements(By.CLASS_NAME, "_1D4W7")

    dates = []
    prices = []

    for number in range(len(nearby_dates)):
        text = nearby_dates[number].text.split("\n")

        date_1 = text[0]
        date = datetime.strptime(f"{date_1}", "%b %d, %a")
        date = date.strftime("%d/\n%m")
        dates.append(date)

        value = text[1]
        value = value[1:].replace(',', '_')
        value = int(value)
        prices.append(value)

    plt.plot(dates, prices, label='Cost', marker='.', markersize=10)
    plt.title(f"{source}-{destination} flight price across dates")
    plt.xlabel("Date")
    plt.ylabel("Price(₹)")
    plt.xticks(dates[::2], fontsize=8)
    plt.legend()

    plt.show()


