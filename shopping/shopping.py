from selenium import webdriver
from shopping.shopping_report import ShoppingReport
from prettytable import PrettyTable

import os

class Shopping(webdriver.Chrome):
    def __init__(self, driver_path = r"C:/Users/maxszostak/Code/selenium_drivers", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Shopping, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://nike.com")

    def select_gender(self, gender='Men'):
        category_button = self.find_element_by_css_selector(
            f'a[aria-label="{gender}"]'
        )
        category_button.click()

    def select_shoes(self):
        shoes_button = self.find_element_by_css_selector(
            'a[aria-label="Shoes"]'
        )
        shoes_button.click()

    def select_size(self, size=8):
        size_button = self.find_element_by_css_selector(
            f'button[aria-label="Filter for {size}"]'
        )
        size_button.click()

    def sort_by_newest(self):
        sort_button = self.find_element_by_id("dropdown-btn")
        sort_button.click()

        newest_button = self.find_element_by_css_selector(
            'button[aria-label="Newest"]'
        )
        newest_button.click()

    def report_results(self):
        shoes_list = self.find_element_by_class_name("product-grid")
        report = ShoppingReport(shoes_list)
        table = PrettyTable(
            field_names=["Shoe Name (newest first)", "Shoe Price"]
        )
        table.add_rows(report.pull_shoes_attributes())
        print(table)



    
