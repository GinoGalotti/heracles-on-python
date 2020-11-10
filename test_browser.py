import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test_Browser():

    # This would be isolated on a PageObject, specifying the CSS/HTML paths to find every element
    TEXT_FORM_NAME = "text"
    URL = "http://127.0.0.1:5000/"

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test_can_load_home(self, driver):
        driver.get(self.URL)

        #Assert it loads

    def test_happy_path(self, driver):
        driver.get(self.URL)
        text = driver.find_element_by_name(self.TEXT_FORM_NAME)
        text.send_keys(111)
        text.send_keys(Keys.RETURN)
        
        body = driver.find_element_by_tag_name('pre').text

        assert '"111.00"' == body

    def test_handling_numeric_error(self, driver):
        driver.get(self.URL)
        text = driver.find_element_by_name(self.TEXT_FORM_NAME)
        text.send_keys("not a number")
        text.send_keys(Keys.RETURN)
        
        body = driver.find_element_by_tag_name('pre').text

        assert '"Sorry, I need a numerical value"' == body

    def test_js_injection(self, driver):
        driver.get(self.URL)
        text = driver.find_element_by_name(self.TEXT_FORM_NAME)
        text.send_keys("javascript:alert(‘Executed!’);")
        text.send_keys(Keys.RETURN)
        
        body = driver.find_element_by_tag_name('pre').text

        assert '"Sorry, I need a numerical value"' == body




