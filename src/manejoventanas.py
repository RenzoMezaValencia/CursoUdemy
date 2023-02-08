import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from pathlib import Path
import os


def manejoventanas():
    projectPath = str(Path(os.getcwd()).parent.absolute())
    s = Service(projectPath +"\drivers\chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.get("https://www.cnn.com")
    driver.back()
    original_window =driver.current_window_handle
    driver.switch_to.new_window('tab')
    driver.get("http://www.rpp.pe")

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            driver.close()

    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    manejoventanas()