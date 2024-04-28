from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    def input_first_name(self, name):
        name_input = self.find_element(OrderPageLocators.F_NAME)
        name_input.click()
        name_input.send_keys(name)

    def input_last_name(self, last_name):
        last_name_input = self.find_element(OrderPageLocators.L_NAME)
        last_name_input.click()
        last_name_input.send_keys(last_name)

    def input_address(self, address):
        address_input = self.find_element(OrderPageLocators.ADDRESS)
        address_input.click()
        address_input.send_keys(address)

    def input_phone(self, phone):
        phone_input = self.find_element(OrderPageLocators.PHONE)
        phone_input.click()
        phone_input.send_keys(phone)

    def set_metro_stantion(self):
        metro_station_open = self.find_element(OrderPageLocators.METRO_ST_OPEN)
        metro_station_open.click()
        choise_station = self.find_element(OrderPageLocators.METRO_ST_CHOICE)
        choise_station.click()


    def click_netx_button(self):
        next_button = self.find_element(OrderPageLocators.NEXT_BUTTON)
        next_button.click()


    def set_delivery_date(self, set_date):
        date = self.find_element(OrderPageLocators.DELIVERY_DATE)
        date.click()
        date.send_keys(set_date)
        date.send_keys(Keys.ENTER)
    def set_rental_period(self):
        period_open = self.find_element(OrderPageLocators.RENTAL_PERIOD)
        period_open.click()
        choise_period = self.find_element(OrderPageLocators.NUMBER_OF_DAY)
        choise_period.click()

    def set_color_black(self):
        color_bl = self.find_element(OrderPageLocators.CHEK_BOX_COLOR_BLACK)
        color_bl.click()

    def set_color_grey(self):
        color_gr = self.find_element(OrderPageLocators.CHEK_BOX_COLOR_GRAY)
        color_gr.click()

    def click_order_button(self):
        order_button = self.find_element(OrderPageLocators.ORDER_BUTTON)
        order_button.click()

    def click_yes_button(self):
        yes_button = self.find_element(OrderPageLocators.YES_BUTTON)
        yes_button.click()

    def get_header_order_text(self):
        header_order = self.find_element(OrderPageLocators.HEADER_ORDER).text
        return header_order

    # набор для первого теста
    def preset_for_test_form(self, name, last_name, address, phone):
        self.input_first_name(name)
        self.input_last_name(last_name)
        self.input_address(address)
        self.set_metro_stantion()
        self.input_phone(phone)





