from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.chrome.webdriver.WebDriver('chromedriver.exe')

#driver = webdriver.Firefox()
driver.get("https://portal.hostco.ru/userlist/")
assert "ХОСТ" in driver.title


elems = driver.find_elements_by_css_selector("#content > table > tbody > tr:nth-child(2) > td:nth-child(2) > p > a")
for el in elems:
	print(el.text())

	
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()

#content > table > tbody > tr:nth-child(2) > td:nth-child(2) > a