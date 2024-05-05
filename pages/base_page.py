from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BaseData:
    URL_DZEN = "https://dzen.ru/?yredirect=true"
    TITLE = "Дзен"


class BasePage:
    @allure.step("Инициализация драйвера")
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step ("Поиск элемента, в случае успеха возвращает его")
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step("Переход на сайт")
    def go_to_site(self):
        return self.driver.get(self.base_url)

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

