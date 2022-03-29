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

def get_image_url(url: str):
    url = url.split("?")[1]
    return url[url.find("img_url=") + len("img_url="):url.find("&", url.find("img_url="))]

class YandexScenariosTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver_linux64/chromedriver")
        self.driver.get("http://www.yandex.ru")
        
        robot = find_element_by_func(self.driver.find_element, By.XPATH, "//input[@type='submit']")
        if robot != None:
            robot.click()
            self.driver.implicitly_wait(10)

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

        images_link = find_element_by_func(driver.find_element, By.LINK_TEXT, "Картинки")
        self.assertNotEqual(images_link, None, "image link not found")

        images_link.click()
        driver.switch_to.window(driver.window_handles[1])
        self.assertEqual(driver.current_url.split('?')[0], "https://yandex.ru/images/", "image link does not work")
        
        group = driver.find_element(By.XPATH, "//div[@data-grid-name='im'][1]")
        group_link = group.find_element(By.TAG_NAME, "a")
        #print(group_link.get_attribute("href"))
        group_name = group.get_attribute("data-grid-text")
        group_link.click()
        driver.get(group_link.get_attribute("href"))
        search = driver.find_element(By.NAME, "text")
        self.assertEqual(group_name, search.get_attribute("value"), "Group title in search not foun")
 
        image_item = driver.find_element(By.CLASS_NAME, "serp-item__link")
        image_item_url = get_image_url(image_item.get_attribute("href"))
        image_item.click()
        image_view = find_element_by_func(driver.find_element, By.CLASS_NAME, "MMImage-Preview")
        image_url = get_image_url(driver.current_url)
        self.assertNotEqual(image_view, None, "Image view not open")
        self.assertTrue(image_item_url == image_url, "Wrong image was opened")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
