import time
from selenium.common.exceptions import NoSuchElementException

def test_is_exist_add_to_basket_btn(browser):
	try:
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		browser.get(link)
		time.sleep(5)
		browser.find_element_by_css_selector("#add_to_basket_form > button")

	except NoSuchElementException:
		assert False , "Button doesn't exist!"
