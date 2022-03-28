import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException    

def find_element_by_func(func, by, value):
    try:
        return func(by, value)
    except NoSuchElementException:
        return None

class YandexScenariosTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver_linux64/chromedriver")
        self.driver.get("http://www.yandex.ru")

    def test_yandex_search(self):
        driver = self.driver
        
        # Поиск
        elem = find_element_by_func(driver.find_element, By.ID, "text")
        self.assertNotEqual(elem, None, "search not found")

        elem.send_keys("Тензор")
        #elem1 = driver.find_element(By.ID, "suggest-list-12ciq544100c")

        elem.send_keys(Keys.RETURN)
        
        # Результаты поиска
        elem = find_element_by_func(driver.find_element, By.ID, "search-result")
        self.assertNotEqual(elem, None, "results search not found")
        
        links = elem.find_elements(By.XPATH, "//a[@accesskey]")
        url_tensor = list(map(lambda a: a.get_attribute("href").find("tensor.ru"), links))
        self.assertTrue(sum(url_tensor[:5]) > -5, "tensor.ru not found")

    #def test_yandex_image(self):
        #pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
