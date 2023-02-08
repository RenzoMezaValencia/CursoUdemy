from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from pathlib import Path
import os

def manejo_paginas():
    projectPath = str(Path(os.getcwd()).parent.absolute())
    s = Service(projectPath + "\drivers\chromedriver")
    driver = webdriver.Chrome(service=s)
    driver.get("http://4.227.227.208/wp-admin")
    driver.maximize_window()
    print("El URL actual es: " + driver.current_url)
    print("Contenido HTML de la pagina: ")
    print(driver.page_source)
    print("El titulo de la pagina es: " + driver.title)


if __name__ == '__main__':
    manejo_paginas()