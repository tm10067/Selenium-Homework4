from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import yaml

with open("./testdata.yaml") as f:
    data = yaml.safe_load(f)
    url = data["url"]

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, times=10):
        try:
            element = WebDriverWait(self.driver, times).until(EC.presence_of_element_located(locator),
                                                              message=f'Элемент {locator} не найден')
        except:
            logging.exception("Ошибка поиска элемента")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.exception(f'Свойство {property} элемента {locator} не найдено')
            return None

    def go_to_site(self):
        try:
            site = self.driver.get(self.base_url)
        except:
            logging.exception("Ошибка открытия сайта")
            site = None
        return site

    def alert(self):
        try:
            alert_obj = self.driver.switch_to.alert
            return alert_obj.text
        except:
            logging.exception("Ошибка оповещения")
            return None
