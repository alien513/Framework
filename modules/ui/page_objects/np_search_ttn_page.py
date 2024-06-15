from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://novaposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def search_ttn(self, ttn):
        search_ttn_field = self.driver.find_element(By.ID, "cargo_number")
        search_ttn_field.send_keys(ttn)

        search_ttn_popup_close_btn = self.driver.find_element(By.XPATH, "//*[@id='popup_info']/div[1]/i")
        search_ttn_popup_close_btn.click()

        search_ttn_btn = self.driver.find_element(By.XPATH, "//div[@class='search_cargo_form']/form/input[2]")
        search_ttn_btn.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
