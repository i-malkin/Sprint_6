from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


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


