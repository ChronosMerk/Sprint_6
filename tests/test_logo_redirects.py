import allure
from pages.logo_redirects_page import LogoRedirectsPage
from data import URL

@allure.title('Тестовые сценарии переходов между страницами')
class TestsLogoRedirects:

    @allure.title('Редирект на страницу Яндекс Дзен')
    @allure.description('переход на страницу заказать, после нажать на кнопку Яндекс')
    def test_transition_via_yandex_logo(self, firefox_driver):
        redirect_page = LogoRedirectsPage(firefox_driver)
        redirect_page.open(URL.ORDER)

        assert redirect_page.check_yandex_logo_transition()

    @allure.title('Редирект на страницу главная самокат')
    @allure.description('переход на страницу заказать, после нажать на кнопку Самокат')
    def test_transition_via_scooter_logo(self, firefox_driver):
        redirect_page = LogoRedirectsPage(firefox_driver)
        redirect_page.open(URL.ORDER)

        assert redirect_page.check_scooter_logo_transition()

