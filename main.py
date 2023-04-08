import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

key_search = input('inserisci il settore: ')

# create Firefox driver with options and set to automatically accept cookies
options = webdriver.FirefoxOptions()
options.set_preference("network.cookie.cookieBehavior", 0)
driver = webdriver.Firefox(options=options)

# navigate to website and accept cookies
driver.get("https://www.paginebianche.it")
accept_button = driver.find_element(By.XPATH, "/html/body/div[11]/div/div/div/div[2]/button[3]")
if accept_button:
    accept_button.click()

# enter search keyword and submit search
driver.find_element(By.CLASS_NAME, "hsearch__input").send_keys(key_search + Keys.ENTER)

# wait for search results to load and accept cookies if necessary
time.sleep(5)

# click on first phone number in search results
buttontel = driver.find_element(By.CSS_SELECTOR, "section.list-element:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
buttontel.click()
time.sleep(1)
buttonnumber = driver.find_element(By.CSS_SELECTOR, "section.list-element:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(2) > div:nth-child(2)")
print(buttonnumber.text)

# close the browser
driver.quit()
