from selenium import webdriver
import os
import logging
import datetime
import shutil


logging.basicConfig(filename='logs.log', level=logging.DEBUG)


def before_all(context):
    try:
        shutil.rmtree(os.path.abspath("./Screenshots"))
    except FileNotFoundError as e:
        os.mkdir(os.path.abspath("./Screenshots"))
        logging.info("Папка со скриншотами уже создана")
    context.browser = webdriver.Chrome(os.path.abspath('chromedriver.exe'))
    context.browser.maximize_window()


def after_scenario(context, scenario):
    if str(scenario.status) == 'Status.failed':
        make_screen(context, f"{scenario.name}")


def after_step(context, step):
    if str(step.status) == 'Status.failed':
        make_screen(context, step.name)
    logging.info(step.name)
    logging.debug("Отладочное сообщение")


def make_screen(context, screen_name):
    short_name = screen_name[:7]
    now = datetime.datetime.now().strftime("%d-%m-%Y %H'%M''%S")
    context.browser.get_screenshot_as_file(os.path.abspath(f"./Screenshots/{short_name}_{now}.png"))


