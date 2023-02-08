from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from pathlib import Path
import os


def webdriver_sample():
    projectPath = str(Path(os.getcwd()).parent.absolute())
    s = Service(projectPath +"\drivers\chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.google.com")
    driver.quit()


if __name__ == '__main__':
    webdriver_sample()