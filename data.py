from pages.main_page import QuestionsLocator
class RegistrationData:

    FIRST_NAME_1 = 'ТестовоеИмяА'
    LAST_NAME_1 = 'ТестоваяФамилияПервая'
    ADDRESS_1 = 'ТестовыйАдрес1'
    PHONE_1 = '89998887766'

    FIRST_NAME_2 = 'ТестовоеИмяБ',
    LAST_NAME_2 = 'ТестоваяФамилияВторая'
    ADDRESS_2 = 'ТестовыйАдрес2'
    PHONE_2 = '89997776655'

    DATE = '09.05.2024'

    preset_for_test_1 = [FIRST_NAME_1, LAST_NAME_1, ADDRESS_1, PHONE_1]

class AnswerOriginal:
    TEXT_1 = 'Сутки — 400 рублей'
    TEXT_2 = 'Пока что у нас так'
    TEXT_3 = 'Допустим, вы оформляете'
    TEXT_4 = 'Только начиная с завтрашнего'
    TEXT_5 = 'Пока что нет! Но если что-то срочное'
    TEXT_6 = 'Самокат приезжает к вам'
    TEXT_7 = 'Да, пока самокат не привезли'
    TEXT_8 = 'Да, обязательно. Всем'


    questions_list = [
        [QuestionsLocator.QUESTION_1, QuestionsLocator.HINT_1, TEXT_1],
        [QuestionsLocator.QUESTION_2, QuestionsLocator.HINT_2, TEXT_2],
        [QuestionsLocator.QUESTION_3, QuestionsLocator.HINT_3, TEXT_3],
        [QuestionsLocator.QUESTION_4, QuestionsLocator.HINT_4, TEXT_4],
        [QuestionsLocator.QUESTION_5, QuestionsLocator.HINT_5, TEXT_5],
        [QuestionsLocator.QUESTION_6, QuestionsLocator.HINT_6, TEXT_6],
        [QuestionsLocator.QUESTION_7, QuestionsLocator.HINT_7, TEXT_7],
        [QuestionsLocator.QUESTION_8, QuestionsLocator.HINT_8, TEXT_8],
    ]
