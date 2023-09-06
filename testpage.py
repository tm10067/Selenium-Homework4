import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocator:
    dictloc = {}
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        dictloc[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        dictloc[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Ввод <{word}> в элемент <{element_name}>')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Элемент <{locator}> не найден')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Ошибка обработки <{locator}>')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Ошибка кнопки')
            return False
        logging.debug(f'Кнопка <{element_name}> нажата')
        return True

    def get_text_from_element(self, locator, description=None):

        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, times=10)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Ошибка получения текста из <{element_name}>')
            return None
        logging.debug(f'Текст <{text}> найден в элементе <{element_name}>')
        text = field.text

        return text

    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_LOGIN_FIELD"], word, description="Поле логин")

    def enter_pswd(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_PASS_FIELD"], word, description="Поле пароль")

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_TITLE_FIELD"], word,
                                   description="Поле заголовок")

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_DESCRIPTION_FIELD"], word,
                                   description="Поле описание")

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_CONTENT_FIELD"], word,
                                   description="Поле содержание")

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_CONTACT_NAME_FIELD"], word,
                                   description="Поле имя")

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_CONTACT_EMAIL_FIELD"], word,
                                   description="Поле email")

    def enter_contact_content(self, word):
        self.enter_text_into_field(TestSearchLocator.dictloc["LOCATOR_CONTACT_CONTENT_FIELD"], word,
                                   description="Поле контакт")

    def click_login_button(self):
        self.click_button(TestSearchLocator.dictloc["LOCATOR_LOGIN_BTN"], description="Кнопка авторизации")

    def click_to_do_new_post(self):
        self.click_button(TestSearchLocator.dictloc["LOCATOR_NEW_POST_BTN"], description="Кнопка поста")

    def click_save_post_button(self):
        self.click_button(TestSearchLocator.dictloc["LOCATOR_SAVE_BTN"], description="Кнопка сохранить пост")

    def click_contact_button(self):
        self.click_button(TestSearchLocator.dictloc["LOCATOR_CONTACT_BTN"], description="Кнопка контакт")

    def contact_us_save_button(self):
        self.click_button(TestSearchLocator.dictloc["LOCATOR_CONTACT_SAVE_BTN"],
                          description="Кнопка сохранить контакт")

    def get_title_text(self):
        return self.get_text_from_element(TestSearchLocator.dictloc["LOCATOR_TITLE_TEXT"], description="Заголовок")

    def get_error_msg(self):
        return self.get_text_from_element(TestSearchLocator.dictloc["LOCATOR_ERROR_FIELD"], description="Ошибка")

    def get_profile_text(self):
        return self.get_text_from_element(TestSearchLocator.dictloc["LOCATOR_USER_PROFILE_NAME"],
                                          description="Имя пользователя")

    def get_alert_text(self):
        logging.info("Текст оповещения")
        text = self.alert()
        logging.info(text)
        return text
