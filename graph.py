from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import matplotlib.pyplot as plt

driver = webdriver.Chrome()

driver.get(
    f"https://tickets.paytm.com/flights/flightSearch/BOM/DEL/1/0/0/E/2023-12-29/")
driver.minimize_window()
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
    value = value[1:]
    value = value.replace(',', '_')
    value = int(value)
    prices.append(value)


def make_plot(dates, prices):
    plt.plot(dates, prices, label='Cost', marker='.', markersize=10)
    plt.title("Mumbai-Delhi flight price across dates")
    plt.xlabel("Date")
    plt.ylabel("Price(₹)")
    plt.xticks(dates[::2], fontsize=8)
    plt.legend()

    plt.show('Graph')