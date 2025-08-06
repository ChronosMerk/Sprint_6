import allure
from pages.base_page import BasePage
from locators.order_page_locators import FirstPageLocators, SecondPageLocators
from locators.main_page_locators import MainPageLocators

class OrderPage(BasePage):
    @allure.step('Закрытие плашки с Куки')
    def closing_cookies(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON_LOCATOR)

    @allure.step('Заполнение данных на первой странице')
    def set_fields_first_page(self, order_data):
        self.set_text_to_element(FirstPageLocators.ORDER_NAME, order_data['first_name'])
        self.set_text_to_element(FirstPageLocators.ORDER_LAST_NAME, order_data['last_name'])
        self.set_text_to_element(FirstPageLocators.ORDER_ADDRESS, order_data['address'])
        self.set_text_to_element(FirstPageLocators.ORDER_METRO, order_data['station'])
        self.find_element_with_click(FirstPageLocators.ORDER_METRO_LIST(order_data['station']))
        self.set_text_to_element(FirstPageLocators.ORDER_PHONE, order_data['phone'])
        self.click_element(FirstPageLocators.ORDER_NEXT)


    @allure.step('Заполнение данных на второй странице')
    def set_fields_second_page(self, order_data):
        self.set_text_to_element(SecondPageLocators.ORDER_DATE, order_data['date'])
        self.click_element(SecondPageLocators.ORDER_PERIOD)
        self.click_element(SecondPageLocators.ORDER_RENTAL_PERIOD)
        self.click_element(SecondPageLocators.ORDER)
        self.click_element(SecondPageLocators.ORDER_DESIGN)


    @allure.step('Создание заказа')
    def create_order(self, order_locator, order_data):
        self.closing_cookies()
        self.click_element(order_locator)
        self.set_fields_first_page(order_data)
        self.set_fields_second_page(order_data)

    @allure.step('Проверка  создания заказа')
    def check_order_is_success(self):
        label = self.get_text_from_element(SecondPageLocators.ORDER_SUCCESS)
        return 'Заказ оформлен' in label