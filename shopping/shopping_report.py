from selenium.webdriver.remote.webelement import WebElement

class ShoppingReport():
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.shoes = self.pull_shoes()

    def pull_shoes(self):
        return self.boxes_section_element.find_elements_by_class_name(
            'product-card__info'
        )

    def pull_shoes_attributes(self):
        collection = []
        for shoe in self.shoes:
            shoe_name = shoe.find_element_by_class_name(
                'product-card__title'
            ).get_attribute('innerHTML').strip()
            shoe_price = shoe.find_element_by_class_name(
                'product-price'
            ).get_attribute('innerHTML').strip()
            collection.append([shoe_name, shoe_price])
        return collection
            