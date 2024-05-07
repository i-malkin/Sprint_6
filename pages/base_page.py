from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class BaseData:
    URL_DZEN = "https://dzen.ru/?yredirect=true"
    TITLE = "Дзен"
    MAIN_PAGE_URL = "https://qa-scooter.praktikum-services.ru/"
    QUESTION_LIST = (By.XPATH, "//div[@class='Home_SubHeader__zwi_E' and text()='Вопросы о важном']")
    ORDER_BUTTON_DOWN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")


class BasePage:
    @allure.step("Инициализация драйвера")
    def __init__(self, driver):
        self.driver = driver


    @allure.step ("Поиск элемента, в случае успеха возвращает его")
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step("Переход на сайт")
    def go_to_site(self):
        return self.driver.get(BaseData.MAIN_PAGE_URL)

    @allure.step("Получение текущего УРЛ")
    def get_current_URL(self):
        get_url = self.driver.current_url
        return get_url

    @allure.step("Переключаем двайвер")
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидаем появление заголовка на странице")
    def wait_haider_on_page(self):
        WebDriverWait(self.driver, 10).until(EC.title_is(BaseData.TITLE))

    @allure.step("Ожидаем, пока не сменится страница")
    def wait_url_changes(self):
        WebDriverWait(self.driver, 10).until(EC.url_changes(BaseData.URL_DZEN))

    @allure.step("Прокрутка страницу к элементу Вопросы о главном")
    def scroll_to_list_questions(self, driver):
        element = self.find_element(BaseData.QUESTION_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step("Переход к кнопке заказа расположенной внизу")
    def go_to_down_order_button(self, driver):
         element = self.find_element(BaseData.ORDER_BUTTON_DOWN)
         driver.execute_script("arguments[0].scrollIntoView();", element)


