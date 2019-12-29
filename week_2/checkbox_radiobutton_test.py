import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_id("treasure")
	x = x_element.get_attribute("valuex")#x = x_element.text
	y = calc(x)

	input = browser.find_element_by_id("answer")
	input.send_keys(y)

	checkbox = browser.find_element_by_id("robotCheckbox")
	checkbox.click()

	radio_btn = browser.find_element_by_id("robotsRule")
	radio_btn.click()

	submit_btn = browser.find_element_by_tag_name("button")
	submit_btn.click()

finally:
	time.sleep(10)
	browser.quit()