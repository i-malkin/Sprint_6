from pages.main_page import MainPageAction
from pages.order_page import OrderScooter
from data import RegistrationData
import allure



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
        assert 'Заказ оформлен' in text_header
    @allure.title("Тестируем заказ самоката со вторым набором данных")
    @allure.description("Тест для проверки заказа самоката в определенным набором данных")
    def test_order_scooter_via_down_button(self, browser):
        main_page = MainPageAction(browser)
        main_page.go_to_site()
        main_page.click_close_cookie()
        main_page.go_to_down_order_button(browser)
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
        assert 'Заказ оформлен' in text_header

