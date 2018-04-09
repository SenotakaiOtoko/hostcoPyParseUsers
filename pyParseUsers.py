from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from http.server import HTTPServer, BaseHTTPRequestHandler

class user:
	def __init__(self, avatar, name, info):
		self.avatar = avatar
		self.info = info
		self.name = name
	avatar = ""
	info = ""
	name = ""

class HttpProcessor(BaseHTTPRequestHandler):
	table = ""
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.wfile.write(table.encode("utf-8"))
	
driver = webdriver.chrome.webdriver.WebDriver('chromedriver.exe')

print("Feature added!")

#driver = webdriver.Firefox()
driver.get("https://portal.hostco.ru/userlist/")
assert "ХОСТ" in driver.title

elems = driver.find_elements_by_css_selector("#content > table > tbody > tr > td > p > a")
user_links = []
for el in elems:
	user_links.append(el.get_attribute("href"))

user_list = []

for lnk in user_links:
	driver.get(lnk)
	avatar = driver.find_element_by_css_selector(".user-avatar-personal img")
	info = driver.find_element_by_class_name("user-info-personal")
	name = driver.find_element_by_class_name("page-title")
	user_list.append(user(avatar.get_attribute("src"), name, info.text))

	
print("Oh, no! Somebody is committed here! AWFUL!")

table = "<table><tboby>"
for usr in user_list:
	table += "<tr><td><img src=\"" + usr.avatar + "\"><\td>"
	table += "<td>" + usr.name + "</td>"
	table += "<td>" + usr.info + "</td></tr>"
table += "</tbody></table>"

f = open("./file.html",'w')
f.write(table)

driver.close()
print("Well done!")
#serv = HTTPServer(("localhost",80),HttpProcessor.init(table))
#serv.serve_forever()


	
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source

#content > table > tbody > tr:nth-child(2) > td:nth-child(2) > a