from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from Generic.intials import driver
from selenium.webdriver.common.by import By



class SeleniumUtils:

    def __init__(self):
        self.driver = driver.get_chrome_driver(self)
        self.wait_timeout = 10

    def open_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(f"Error: {str(e)}")

    def find_element_by_id(self, id):
        try:
            element = self.driver.find_element_by_id(id)
            return element
        except NoSuchElementException:
            print(f"Error: Element with ID '{id}' not found.")

    def find_element_by_name(self, name):
        try:
            element = self.driver.find_element_by_name(name)
            return element
        except NoSuchElementException:
            print(f"Error: Element with name '{name}' not found.")

    def find_element_by_xpath(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            return element
        except NoSuchElementException:
            print(f"Error: Element with XPath '{xpath}' not found.")

    def find_element_by_css_selector(self, css_selector):
        try:
            element = self.driver.find_element_by_css_selector(css_selector)
            return element
        except NoSuchElementException:
            print(f"Error: Element with CSS selector '{css_selector}' not found.")

    def find_element_by_class_name(self, class_name):
        try:
            element = self.driver.find_element_by_class_name(class_name)
            return element
        except NoSuchElementException:
            print(f"Error: Element with class name '{class_name}' not found.")

    def find_element_by_tag_name(self, tag_name):
        try:
            element = self.driver.find_element_by_tag_name(tag_name)
            return element
        except NoSuchElementException:
            print(f"Error: Element with tag name '{tag_name}' not found.")

    def send_keys(self, element, keys):
        try:
            element.send_keys(keys)
        except Exception as e:
            print(f"Error: {str(e)}")

    def click(self, element):
        try:
            element.click()
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_element_text(self, element):
        try:
            return element.text
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_element_attribute(self, element, attribute):
        try:
            return element.get_attribute(attribute)
        except Exception as e:
            print(f"Error: {str(e)}")

    def wait_for_element(self, element_locator, timeout=None):
        if not timeout:
            timeout = self.wait_timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element_locator))
            return element
        except TimeoutException:
            print(f"Error: Element with locator '{element_locator}' not found within {timeout} seconds.")

    def switch_to_frame(self, frame):
        try:
            self.driver.switch_to.frame(frame)
        except Exception as e:
            print(f"Error: {str(e)}")

    def switch_to_window(self, window_handle):
        try:
            self.driver.switch_to.window(window_handle)
        except Exception as e:
            print(f"Error: {str(e)}")
