# This is a sample Python script.
import time
from Generic.generic import SeleniumUtils

generic = SeleniumUtils()
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generic.open_url('https://web.whatsapp.com/')
    time.sleep(10)
    try:

        # Find the span element that contains the number 2 and has a text value greater than 0
        span_with_2 = generic.find_element_by_xpath('//div[@class="_8nE1Y"]//span[number() >= 1]')
        # Verify that the span element exists
        assert span_with_2 is not None

        # Find the span element that contains the text "get inventory tauheed"
        span_with_text = generic.find_element_by_xpath('''//span[contains(text(),'get inventory
tauheed')]''')
        # Verify that the span element exists
        assert span_with_text is not None

        # Find the parent div element and click on it
        parent_div = generic.find_element_by_xpath('div[@class="_8nE1Y"]')
        parent_div.click()

    except parent_div as e:
        print(f"Element not found: {e}")
