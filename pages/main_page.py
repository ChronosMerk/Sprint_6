import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Клик по вопросу')
    def click_to_question(self, index):
        element = self.find_element_with_wait(MainPageLocators.QUESTION_ELEMENT_SCROLL)
        self.scroll_to_element(element)
        self.click_element(MainPageLocators.QUESTION(index))

    @allure.step('Получение текста внутри карточки вопроса')
    def getting_text_inside_a_question_card(self, index):
        return self.get_text_from_element(MainPageLocators.TEXT_INSIDE_THE_QUESTION(index))

    @allure.step('Проверка текста в вопросах')
    def check_text_in_questions(self, index, input_text):
        self.click_to_question(index)
        result = self.getting_text_inside_a_question_card(index)
        return result == input_text
