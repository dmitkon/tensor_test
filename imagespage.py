from basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_image_url(url: str):
    url = url.split("?")[1]
    return url[url.find("img_url=") + len("img_url="):url.find("&", url.find("img_url="))]

class ImagesPage(BasePage):
    
    def set_images_link(self):
        self.images_link = self.find_element(By.LINK_TEXT, "Картинки")
        return self.images_link != None

    def click_element(self, elem):
        elem.click()

    def get_group(self, number):
        group = self.find_element(By.XPATH, f"//div[@data-grid-name='im'][{number}]")
        group_name = group.get_attribute("data-grid-text")
        group_link = group.find_element(By.TAG_NAME, "a").get_attribute("href")

        return {"object": group, "name": group_name, "url": group_link}

    def get_serch_value(self):
        return self.find_element(By.NAME, "text").get_attribute("value")

    def get_item(self):
        image_item = self.find_element(By.CLASS_NAME, "serp-item__link")
        image_item_url = get_image_url(image_item.get_attribute("href"))
        
        return {"object": image_item, "url": image_item_url}

    def set_view(self):
        self.image_view = self.find_element(By.CLASS_NAME, "MMImage-Preview")
        return self.image_view != None

    def get_view_src(self):
        return self.image_view.get_attribute("src")

    def get_image_url(self):
        return get_image_url(self.get_url())

    def set_forward_arrow(self):
        self.forward_arrow = self.find_element(By.CSS_SELECTOR, "div.CircleButton:nth-child(4)")

    def set_prev_arrow(self):
        self.prew_arrow = self.find_element(By.CSS_SELECTOR, ".CircleButton_type_prev")
