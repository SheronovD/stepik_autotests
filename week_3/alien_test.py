from selenium import webdriver
import pytest
import time
import math

@pytest.fixture(scope="function") #"class"...
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', 
["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_is_correct_answer(browser, link):
	browser.get(link)
	input = browser.find_element_by_tag_name("textarea")
	answer = math.log(int(time.time()))
	input.send_keys(str(answer))

	submit_btn = browser.find_element_by_tag_name("button")
	submit_btn.click()

	msg = browser.find_element_by_tag_name("pre").text
	assert msg == "Correct!" , "Incorrect answer"

