from pages.main_page import MainPageAction
import time


class TestLogotyps:
    def test_click_scooter_logo(self, browser):
         main_page = MainPageAction(browser)
         main_page.go_to_site()
         main_page.click_close_cookie()
         main_page.click_order_button_top()
         main_page.click_scooter_logo()
         scooter_link = main_page.get_current_URL()
         assert scooter_link == main_page.base_url
         print(f'Нужная ссылка: {scooter_link}')

    def test_click_dzen_logo(self, browser):
        main_page = MainPageAction(browser)
        main_page.go_to_site()
        main_page.click_close_cookie()
        main_page.click_dzen_logo()
        all_handles = browser.window_handles
        if len(all_handles) == 1:
            print('Новая вкладка не открыта!')
        else:
            print('Новая вкладка открыта')
        browser.switch_to.window(all_handles[-1])
        time.sleep(6)
        get_URL = browser.current_url
        if get_URL == "https://dzen.ru/?yredirect=true":
            print("Новый сайт открыт корректно!")
        else:
            print("Не тот новый сайт открыт!")


