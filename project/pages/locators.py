from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    # Сообщение об успехе: "Coders at Work has been added to your basket."
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")

    # Сообщение о стоимости корзины: "Your basket total is now £19.99"
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")