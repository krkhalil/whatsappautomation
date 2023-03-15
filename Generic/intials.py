from selenium import webdriver
class driver:
    def get_chrome_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")  # maximize the browser window
            driver = webdriver.Chrome(options=options)
            return driver
        except Exception as e:
            print(f"Error: {str(e)}")
