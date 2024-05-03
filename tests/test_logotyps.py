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
        all_handles = browser.window_handles
        browser.switch_to.window(all_handles[-1])
        time.sleep(6)
        get_URL = browser.current_url
        assert get_URL == "https://dzen.ru/?yredirect=true"



