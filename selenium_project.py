import datetime
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://www.worldometers.info/coronavirus/')

now = datetime.datetime.now()
date_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("----------------------------------------")
print("Data from site: https://www.worldometers.info/coronavirus/")
print("Data from time: ", date_now)
print("----------------------------------------")
print("World Coronavirus Cases:")
page_data = browser.find_elements_by_xpath("//div[@class='maincounter-number']/span[1]")
print(page_data[0].text)
print("")
print("World Coronavirus Deaths:")
print(page_data[1].text)
print("----------------------------------------")
