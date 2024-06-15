import time
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BasePage):
    URL = "https://rozetka.com.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def check_add_to_cart(self):
        search_keyword = "ноутбук"

        search_box = self.driver.find_element(By.NAME, "search")
        search_box.send_keys(search_keyword)
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "goods-tile"))
        )

        first_product = self.driver.find_element(By.CLASS_NAME, "goods-tile__heading")
        first_product.click()

        time.sleep(3)

        self.driver.execute_script(
            "arguments[0].click();",
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//rz-buy-button/button"))
            ),
        )

        time.sleep(3)

        cart_count = self.driver.find_element(By.XPATH, "//rz-cart-counter/div/input")

        if cart_count.get_attribute("value") == "1":
            return 1
        else:
            return 0
