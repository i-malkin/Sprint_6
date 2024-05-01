from pages.main_page import MainPageAction
from data import AnswerOriginal
import pytest
import time
import allure


class TestQuestionsText:
    @allure.title("Тестируем выпадающий список")
    @allure.description("Тест для проверки выпадающего списка, текст соответствует при раскрытии")
    @pytest.mark.parametrize("questions, hint, text", AnswerOriginal.questions_list)
    def test_questions_drop_down_list(self, browser, questions, hint, text):
        main_page = MainPageAction(browser)
        main_page.go_to_questions_list(browser)
        time.sleep(1)
        main_page.click_drop_down_list(questions)
        answer = main_page.get_text_from_drop_down_list(hint)
        print(answer)
        assert text in answer


