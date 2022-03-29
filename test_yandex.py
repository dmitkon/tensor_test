import unittest
from imagespage import ImagesPage
from searchpage import SearchPage

class YandexScenariosTest(unittest.TestCase):

    def test_yandex_search(self):
        search = SearchPage()
        search.go_to_site("http://www.yandex.ru")
        
        self.assertTrue(search.set_search(), "search not found")

        search.search_input_text("Тензор")
        self.assertTrue(search.suggest_is_exist(), "suggest not found")

        search.click_return()
        
        self.assertTrue(search.set_result(), "results search not found")
        self.assertTrue(sum(search.get_url_links_result()[:5]) > -5, "tensor.ru not found")

        search.quit()

    def test_yandex_images(self):
        images = ImagesPage()
        images.go_to_site("http://www.yandex.ru")

        self.assertTrue(images.set_images_link(), "image link not found")
        images.click_element(images.images_link)
        images.switch_to_window(1)

        self.assertEqual(images.get_url().split('?')[0], "https://yandex.ru/images/", "image link does not work")

        group = images.get_group(1)
        images.click_element(group.get('object'))
        images.go_to_site(group.get('url'))
        self.assertEqual(group.get('name'), images.get_serch_value(), "Group title in search not found")

        item = images.get_item()
        images.click_element(item.get('object'))
        self.assertNotEqual(images.set_view(), "Image view not open")
        self.assertTrue(item.get('url') == images.get_image_url(), "Wrong image was opened")

        image_src = images.get_view_src()
        images.set_forward_arrow()
        images.click_element(images.forward_arrow)
        next_image_src = images.get_view_src()
        self.assertNotEqual(image_src, next_image_src, "the following image did not open")

        images.set_prev_arrow()
        images.click_element(images.prew_arrow)
        prev_image_src = images.get_view_src()
        self.assertEqual(prev_image_src, image_src, "the previous image did not open")

        images.quit()

if __name__ == "__main__":
    unittest.main()
