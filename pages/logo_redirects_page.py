import allure
from pages.base_page import BasePage
from locators.logo_page_locators import LogoPageLocators

class LogoRedirectsPage(BasePage):
    @allure.step('Переход на другую страницу')
    def go_to_another_page(self, locator):
        self.click_element(locator)
        return self.get_current_url()

    @allure.step('Проверка на корректность перехода')
    def check_transition_success(self,locator, received_url):
        self.wait_for_url(received_url)
        element = self.find_element_with_wait(locator)
        return element.is_displayed()

    @allure.step('Переход по логотипу Яндекс')
    def check_yandex_logo_transition(self):
        received_url = self.go_to_another_page(LogoPageLocators.YANDEX_LOGO)
        return self.check_transition_success(LogoPageLocators.BUTTON_DZEN_SEARCH, received_url)

    @allure.step('Переход по логотипу Самокат')
    def check_scooter_logo_transition(self):
        received_url = self.go_to_another_page(LogoPageLocators.SCOOTER_LOGO)
        return self.check_transition_success(LogoPageLocators.SCOOTER_HOME_HEADER, received_url)