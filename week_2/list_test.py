from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(str(x))

	submit_btn = browser.find_element_by_tag_name("button")
	submit_btn.click()

finally:
	time.sleep(10)
	browser.quit()