import allure
import pytest
from pages.order_scooter_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import URL, OrderData

@allure.title('Позитивный сценарий заказа самоката')
class TestOrderScooter:
    @allure.title('Регистрация заказа самоката')
    @allure.description('Нажать кнопку «Заказать». '
                        'На странице две кнопки заказа. Заполнить форму заказа. '
                        'Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    @pytest.mark.parametrize(('order_locator', 'order_data'), [(MainPageLocators.BUTTON_ORDER_UPPER, OrderData.ORDER_1),
                                                             (MainPageLocators.BUTTON_ORDER_LOWER, OrderData.ORDER_2)])
    def test_order_a_scooter(self, firefox_driver, order_locator, order_data):
        order_page = OrderPage(firefox_driver)
        order_page.open(URL.BASE)

        order_page.create_order(order_locator, order_data)
        assert order_page.check_order_is_success()