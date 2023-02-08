from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from pathlib import Path
import os


def test_page_title():
    projectPath = str(Path(os.getcwd()).parent.absolute())
    s = Service(projectPath + "\drivers\chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("http://4.227.227.208/wp-admin")
    expected_title = "Log In ‹ User's blog — WordPress"
    original_title = driver.title
    print("El titulo original de la pagina es: "+ original_title)

    assert expected_title == original_title