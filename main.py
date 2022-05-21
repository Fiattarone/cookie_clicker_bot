import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(executable_path="C:/Development/chromedriver.exe"))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# item_list = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
# item_ids = [item.get_attribute("id") for item in item_list]
#
upgrade_list = ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment',
                'buyAlchemy lab', 'buyPortal', 'buyTime machine']

one_second = time.time() + 1
five_seconds = time.time() + 5
five_minutes = time.time() + 60*5


def refresh_store(driver_handle):
    return driver_handle.find_elements(by=By.CSS_SELECTOR, value='#store b')


def refresh_cookie(driver_handle):
    return driver_handle.find_element(by=By.ID, value='cookie')


def get_cookie_quantity(driver_handle):
    return driver_handle.find_element(by=By.ID, value='money')


def get_prices(store_handle):
    return [int(product.text.split(" - ")[1].strip().replace(",", ""))
            for product in store_handle if product.text != ""]


store = refresh_store(driver_handle=driver)

# print(costs)

while not time.time() > five_minutes:
    cookie = refresh_cookie(driver_handle=driver)
    cookie.click()
    # get current cookie count
    cookies = int(get_cookie_quantity(driver_handle=driver).text)
    # get item prices
    if time.time() > one_second:
        store = refresh_store(driver_handle=driver)
        prices = get_prices(store_handle=store)
        one_second = time.time() + 1
        # buy stuff
        for i in range(len(prices)):
            # print(type(cookies))
            if cookies >= prices[i]:
                driver.find_element(by=By.ID, value=upgrade_list[i]).click()
                break
print(driver.find_element(by=By.ID, value="cps").text)
