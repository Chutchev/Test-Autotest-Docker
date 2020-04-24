from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
TIMEOUT = 3


class FindText():

    def __getitem__(self, item):
        return f".//*[text()='{item}']"


xpath_dict = {
    "кнопку": {
        "Новая заявка": "//button//span[.='НОВАЯ ЗАЯВКА']",
        "Колокольчик": "//button[contains(@aria-label, 'notifications')]",
        "Мой профиль": "//button[contains(@aria-label, 'current user')]",
    },
    "ссылку": {
        "Проекты": "//a[.='Проекты']",
        "Сообщения": "//a[.='Сообщения']",
        "CI/CD": "//a[.='CI/CD']",
    },
    "текст": FindText()
}

@given('Зайти на сайт "{site}"')
def step_impl(context, site):
    context.browser.get(site)


@then('Нашли "{element}" "{value}"')
def step_impl(context, element, value):
    WebDriverWait(context.browser, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, xpath_dict[element][value]))
    )


@then('Нажали на "{element}" "{value}"')
def step_impl(context, element, value):
    element = WebDriverWait(context.browser, TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, xpath_dict[element][value]))
    )
    element.click()