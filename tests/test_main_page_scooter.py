import pytest
import allure
from pages.main_page import MainPage
from data import URL, TextInQuestions

@allure.title('Тестовые шаг главной страницы')
class TestMainPage:
    @allure.title("Проверка вопросов и ответов")
    @allure.description("Нужно проверить что открывается соответствующий текст")
    @pytest.mark.parametrize('index', [0, 1, 2, 3, 4, 5, 6, 7])

    def test_checking_questions_and_answers(self, index, firefox_driver):
        main_page = MainPage(firefox_driver)
        main_page.open(URL.BASE)

        assert main_page.check_text_in_questions(index, TextInQuestions.TEXTS[index])
