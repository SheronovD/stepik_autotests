import math
from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/cats.html"
	browser = webdriver.Chrome()
	browser.get(link)

	browser.implicitly_wait(5)  # неявное ожидание, будет использоваться при поиске каждого элемента
	browser.find_element_by_id("button")


finally:
	time.sleep(1)
	browser.quit()