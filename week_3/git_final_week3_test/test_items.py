import time
from selenium.common.exceptions import NoSuchElementException

def test_is_exist_add_to_basket_btn(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	browser.get(link)
	time.sleep(5)
	is_btn_exist = len(browser.find_elements_by_css_selector("#add_to_basket_form > button"))
	
	assert is_btn_exist == 1 , "Button doesn't exist!"
