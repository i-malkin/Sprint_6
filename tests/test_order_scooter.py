from pages.main_page import MainPageAction
from pages.order_page import OrderScooter
from data import RegistrationData
from selenium.webdriver.common.by import By
import allure
import time

class TestOrderScooter:
    @allure.title("Тестируем заказ самоката с первым набором данных")
    @allure.description("Тест для проверки заказа самоката в определенным набором данных")
    def test_order_scooter_via_top_button(self, browser):
        main_page = MainPageAction(browser)
        main_page.go_to_site()
        main_page.click_close_cookie()
        main_page.click_order_button_top()
        order_page = OrderScooter(browser)
        order_page.preset_for_test_form(RegistrationData.FIRST_NAME_1,
                                            RegistrationData.LAST_NAME_1,
                                            RegistrationData.ADDRESS_1,
                                            RegistrationData.PHONE_1)



        order_page.click_netx_button()
        order_page.set_delivery_date(RegistrationData.DATE)
        order_page.set_rental_period()
        order_page.set_color_black()
        order_page.click_order_button()
        order_page.click_yes_button()
        text_header = order_page.get_header_order_text()
        print(f'Итак, вот что имеем: {text_header}')
        assert 'Заказ оформлен' in text_header
    @allure.title("Тестируем заказ самоката со вторым набором данных")
    @allure.description("Тест для проверки заказа самоката в определенным набором данных")
    def test_order_scooter_via_down_button(self, browser):
        main_page = MainPageAction(browser)
        main_page.go_to_site()
        main_page.click_close_cookie()
        element = browser.find_element(By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
        browser.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)
        main_page.click_order_button_down()
        order_page = OrderScooter(browser)
        order_page.preset_for_test_form(RegistrationData.FIRST_NAME_2,
                                        RegistrationData.LAST_NAME_2,
                                        RegistrationData.ADDRESS_2,
                                        RegistrationData.PHONE_2)
        order_page.click_netx_button()
        order_page.set_delivery_date(RegistrationData.DATE)
        order_page.set_rental_period()
        order_page.set_color_grey()
        order_page.click_order_button()
        order_page.click_yes_button()
        text_header = order_page.get_header_order_text()
        print(f'Итак, вот что имеем: {text_header}')
        assert 'Заказ оформлен' in text_header





        # order_page.preset_for_test_form(RegistrationData.FIRST_NAME_1,
        #                                     RegistrationData.LAST_NAME_1,
        #                                     RegistrationData.ADDRESS_1,
        #                                     RegistrationData.PHONE_1)

