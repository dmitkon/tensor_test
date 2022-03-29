from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage(BasePage):

    def set_search(self):
        self.search = self.find_element(By.ID, "text")
        return self.search != None

    def suggest_is_exist(self):
        return self.find_element(By.CLASS_NAME, "mini-suggest__popup-content") != None

    def set_result(self):
        self.result = self.find_element(By.ID, "search-result")
        return self.result != None

    def get_url_links_result(self):
        links = self.result.find_elements(By.XPATH, "//a[@accesskey]")
        return list(map(lambda a: a.get_attribute("href").find("tensor.ru"), links))

    def search_input_text(self, text):
        self.search.send_keys(text)

    def click_return(self):
        self.search.send_keys(Keys.RETURN)
