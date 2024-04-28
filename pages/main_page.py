from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH,"//button[@class='Button_Button__ra12g' and text()='Заказать']") #верхняя кнопка заказа
    ORDER_BUTTON_DOWN = (By.XPATH,"//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") #нижнаа кнопка заказа
    COOKIE_BUTTON = (By.CLASS_NAME, "App_CookieButton__3cvqF")
class QuestionsLocator:
    QUESTION_1 = (By.ID, 'accordion__heading-0')
    QUESTION_2 = (By.ID, 'accordion__heading-1')
    QUESTION_3 = (By.ID, 'accordion__heading-2')
    QUESTION_4 = (By.ID, 'accordion__heading-3')
    QUESTION_5 = (By.ID, 'accordion__heading-4')
    QUESTION_6 = (By.ID, 'accordion__heading-5')
    QUESTION_7 = (By.ID, 'accordion__heading-6')
    QUESTION_8 = (By.ID, 'accordion__heading-7')
    HINT_1 = (By.ID, 'accordion__panel-0')
    HINT_2 = (By.ID, 'accordion__panel-1')
    HINT_3 = (By.ID, 'accordion__panel-2')
    HINT_4 = (By.ID, 'accordion__panel-3')
    HINT_5 = (By.ID, 'accordion__panel-4')
    HINT_6 = (By.ID, 'accordion__panel-5')
    HINT_7 = (By.ID, 'accordion__panel-6')
    HINT_8 = (By.ID, 'accordion__panel-7')


class LogotypsLocators:
    SCOOTER_LOGO = (By.XPATH,"//a[@class='Header_LogoScooter__3lsAR']")
    DZEN_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    DZEN_LOGO_ORIGIN = (By.XPATH, "//a[@desktop-base-header__logoLink-aE']")


class MainPageAction(BasePage):

    def click_close_cookie(self):
        return self.find_element(MainPageLocators.COOKIE_BUTTON).click()

    def click_order_button_top(self):
        return self.find_element(MainPageLocators.ORDER_BUTTON_TOP, time=4).click()

    def click_order_button_down(self):
        return self.find_element(MainPageLocators.ORDER_BUTTON_DOWN, time=4).click()

    def click_scooter_logo(self):
        logo_1 = self.find_element(LogotypsLocators.SCOOTER_LOGO)
        logo_1.click()

    def click_dzen_logo(self):
        logo_2 = self.find_element(LogotypsLocators.DZEN_LOGO)
        logo_2.click()

    def go_to_questions_list(self, browser):
        self.go_to_site()
        self.click_close_cookie()
        element = browser.find_element(By.XPATH, "//div[@class='Home_SubHeader__zwi_E' and text()='Вопросы о важном']")
        browser.execute_script("arguments[0].scrollIntoView();", element)

    def click_drop_down_list(self, question):
        click_list = self.find_element(question)
        click_list.click()

    def get_text_from_drop_down_list(self, hint):
        questions_text = self.find_element(hint).text
        return questions_text











