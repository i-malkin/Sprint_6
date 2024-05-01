from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

class OrderPageLocators:
    F_NAME = (By.CSS_SELECTOR, "[placeholder='* Имя']")
    L_NAME = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")
    ADDRESS = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")
    METRO_ST_OPEN = (By.CSS_SELECTOR, "[placeholder = '* Станция метро']")
    METRO_ST_CHOICE = (By.CSS_SELECTOR, "div.Order_Text__2broi")
    PHONE = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    DELIVERY_DATE = (By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']")               # когда привезти самокат
    RENTAL_PERIOD =  (By.CSS_SELECTOR, '.Dropdown-placeholder')                                 # срок аренды
    NUMBER_OF_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")       # количество дней
    CHEK_BOX_COLOR_BLACK = (By.ID, "black")
    CHEK_BOX_COLOR_GRAY = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    YES_BUTTON = (By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    HEADER_ORDER = (By.XPATH,"//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']") # текст заголовка




class OrderScooter(BasePage):
    @allure.step("Ввод имени")
    def input_first_name(self, name):
        name_input = self.find_element(OrderPageLocators.F_NAME)
        name_input.click()
        name_input.send_keys(name)
    @allure.step("Ввод фамилии")
    def input_last_name(self, last_name):
        last_name_input = self.find_element(OrderPageLocators.L_NAME)
        last_name_input.click()
        last_name_input.send_keys(last_name)
    @allure.step("Ввод адреса")
    def input_address(self, address):
        address_input = self.find_element(OrderPageLocators.ADDRESS)
        address_input.click()
        address_input.send_keys(address)
    @allure.step("Ввод телефона")
    def input_phone(self, phone):
        phone_input = self.find_element(OrderPageLocators.PHONE)
        phone_input.click()
        phone_input.send_keys(phone)
    @allure.step("Выбрать станцию метро")
    def set_metro_stantion(self):
        metro_station_open = self.find_element(OrderPageLocators.METRO_ST_OPEN)
        metro_station_open.click()
        choise_station = self.find_element(OrderPageLocators.METRO_ST_CHOICE)
        choise_station.click()

    @allure.step("Клик по кнопке Далее")
    def click_netx_button(self):
        next_button = self.find_element(OrderPageLocators.NEXT_BUTTON)
        next_button.click()

    @allure.step("Выбрать дату доставки")
    def set_delivery_date(self, set_date):
        date = self.find_element(OrderPageLocators.DELIVERY_DATE)
        date.click()
        date.send_keys(set_date)
        date.send_keys(Keys.ENTER)
    @allure.step("Выбрать срок аренды")
    def set_rental_period(self):
        period_open = self.find_element(OrderPageLocators.RENTAL_PERIOD)
        period_open.click()
        choise_period = self.find_element(OrderPageLocators.NUMBER_OF_DAY)
        choise_period.click()
    @allure.step("Выбрать цвет самоката Черный")
    def set_color_black(self):
        color_bl = self.find_element(OrderPageLocators.CHEK_BOX_COLOR_BLACK)
        color_bl.click()
    @allure.step("Выбрать цвет самоката Серый")
    def set_color_grey(self):
        color_gr = self.find_element(OrderPageLocators.CHEK_BOX_COLOR_GRAY)
        color_gr.click()
    @allure.step("Клик по кнопке заказать")
    def click_order_button(self):
        order_button = self.find_element(OrderPageLocators.ORDER_BUTTON)
        order_button.click()
    @allure.step("Клик по кнопке Да")
    def click_yes_button(self):
        yes_button = self.find_element(OrderPageLocators.YES_BUTTON)
        yes_button.click()
    @allure.step("Получить текст с информацией о заказе")
    def get_header_order_text(self):
        header_order = self.find_element(OrderPageLocators.HEADER_ORDER).text
        return header_order

    @allure.step("Набор действий для заполнения формы заказа")
    def preset_for_test_form(self, name, last_name, address, phone):
        self.input_first_name(name)
        self.input_last_name(last_name)
        self.input_address(address)
        self.set_metro_stantion()
        self.input_phone(phone)





