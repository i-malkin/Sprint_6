from pages.main_page import MainPageAction
import time
import allure

class TestLogotyps:
    @allure.title("Тестируем клик по заголовку Самокат")
    @allure.description("Тест проверки перехода на главную страницу Самоката")
    def test_click_scooter_logo(self, browser):
         main_page = MainPageAction(browser)
         main_page.go_to_site()
         main_page.click_close_cookie()
         main_page.click_order_button_top()
         main_page.click_scooter_logo()
         scooter_link = main_page.get_current_URL()
         assert scooter_link == main_page.base_url

    @allure.title("Тестируем клик по заголовку Яндекс")
    @allure.description("Тест проверки перехода на главную страницу Дзена")
    def test_click_dzen_logo(self, browser):
        main_page = MainPageAction(browser)
        main_page.go_to_site()
        main_page.click_close_cookie()
        main_page.click_dzen_logo()
        main_page.wait_url_changes()
        main_page.switch_driver()
        main_page.wait_haider_on_page()
        assert 'dzen.ru' in main_page.get_current_URL()





