from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self): #добавить товар в корзину
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def see_product_name(self): #посмотреть название продукта
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_STORE)
        assert product_name_in_store.text == product_name_in_basket.text, "Product name is no the same"

    def product_price_is_correct(self): #цена товара правильная
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET)
        product_prise_in_store = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_STORE)
        assert product_prise_in_store.text == product_price_in_basket.text, "Price is wrong"


