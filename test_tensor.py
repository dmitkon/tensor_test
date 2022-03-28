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
        
        search = find_element_by_func(driver.find_element, By.ID, "text")
        self.assertNotEqual(search, None, "search not found")

        search.send_keys("Тензор")
        suggest = find_element_by_func(driver.find_element, By.CLASS_NAME, "mini-suggest__popup-content")
        self.assertNotEqual(suggest, None, "suggest not found")

        search.send_keys(Keys.RETURN)
        
        result = find_element_by_func(driver.find_element, By.ID, "search-result")
        self.assertNotEqual(result, None, "results search not found")
        
        links = result.find_elements(By.XPATH, "//a[@accesskey]")
        url_tensor = list(map(lambda a: a.get_attribute("href").find("tensor.ru"), links))
        self.assertTrue(sum(url_tensor[:5]) > -5, "tensor.ru not found")

    def test_yandex_image(self):
        driver = self.driver

        image_link = find_element_by_func(driver.find_element, By.LINK_TEXT, "Картинки")
        self.assertNotEqual(image_link, None, "image link not found")

        image_link.click()
        driver.get(image_link.get_attribute("href"))
        self.assertEqual(driver.current_url.split('?')[0], "https://yandex.ru/images/")

        #group = driver.find_elements(By.XPATH, "//div[@data-grid-name='im']")
        #print(list(map(lambda a: a.get_attribute("data-grid-text"), group)))
        
        group = driver.find_element(By.XPATH, "//div[@data-grid-name='im'][1]")
        group.click()
        search = driver.find_element(By.NAME, "text")
        self.assertEqual(group.get_attribute("data-grid-text"), search.get_attribute("value"))

        #image = driver.find_element(By.XPATH, "//div[@role='item'][1]")
        #image.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
