from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text

    def get_basket_total(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text

    def should_be_correct_product_name_in_message(self):
        product_name = self.get_product_name()
        message_name = self.get_success_message_name()
        assert product_name == message_name, (
            f"Название товара не совпадает.\n"
            f"На странице: '{product_name}'\n"
            f"В сообщении: '{message_name}'"
        )

    def should_be_correct_basket_total(self):
        price = self.get_product_price()
        basket_total = self.get_basket_total()
        assert price == basket_total, (
            f"Цена не совпадает.\n"
            f"Цена товара: '{price}'\n"
            f"Итого в корзине: '{basket_total}'"
        )