from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException    

class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver_linux64/chromedriver")

    def find_element(self, by, value):
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            return None

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def go_to_site(self, url):
        return self.driver.get(url)

    def switch_to_window(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])

    def get_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()
