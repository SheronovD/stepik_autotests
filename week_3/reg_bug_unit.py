from selenium import webdriver
import time
import unittest

def reg_test(link):
	try:
		browser = webdriver.Chrome()
		browser.get(link)

		input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
		input1.send_keys("Мой ответ")
		input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
		input2.send_keys("Мой ответ")
		input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
		input3.send_keys("Мой ответ")

		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)

		welcome_text_elt = browser.find_element_by_tag_name("h1")
		return welcome_text_elt.text
	finally:
		#time.sleep()
		browser.quit()

class TestAbs(unittest.TestCase):
	def test_reg_1(self):
		welcome_text = reg_test("http://suninjuly.github.io/registration1.html") #...1.html
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "First_registration failed")
	def test_reg_2(self):
		welcome_text = reg_test("http://suninjuly.github.io/registration2.html") #...1.html
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Second_registration failed")

if __name__ == "__main__":
	unittest.main()
