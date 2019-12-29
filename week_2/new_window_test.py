import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	btn = browser.find_element_by_tag_name("button")
	btn.click()

	browser.switch_to.window(browser.window_handles[1])

	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	input = browser.find_element_by_id("answer")
	input.send_keys(y)


	submit_btn = browser.find_element_by_tag_name("button")
	submit_btn.click()

finally:
	time.sleep(10)
	browser.quit()