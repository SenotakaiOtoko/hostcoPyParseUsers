from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.chrome.webdriver.WebDriver('chromedriver.exe')

#driver = webdriver.Firefox()
driver.get("https://portal.hostco.ru/userlist/")
assert "ХОСТ" in driver.title



elems = driver.find_elements_by_css_selector("#content > table > tbody > tr > td > p > a")
users = []
for el in elems:
	users.append(el.get_attribute("href"))

for usr in users:
	driver.get(usr)
	#avatar = driver.find_element_by_class("user-avatar-personal")
	#info = driver.find_element_by_class("user-info-personal")

	
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()

#content > table > tbody > tr:nth-child(2) > td:nth-child(2) > a