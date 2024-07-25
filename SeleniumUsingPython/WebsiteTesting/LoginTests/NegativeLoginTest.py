import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


def negative_login_test():
    # Directory where chromedriver is located
    chromedriver_dir = r"C:\SeleniumDrivers"

    service = Service(os.path.join(chromedriver_dir, 'chromedriver.exe'))
    driver = webdriver.Chrome(service=service)

    try:
        #open the webshop site
        sleep(15)
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(30) #potential wait for the response

        #wpisujemy NIEPOPRAWNE username
        username = driver.find_element(By.ID, 'user-name')
        username.send_keys("standard_user22")

        #wpisujemy NIEPOPRAWNE hasło
        password = driver.find_element(By.ID, 'password')
        password.send_keys("secret_sauce22")

        #klikamy przycisk logowania
        login_form = driver.find_element(By.ID, 'login-button')
        login_form.click()

        # Check if the error message is displayed
        try:
            error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
            print("Niepoprawne hasło lub nazwa użytkownika.")
        except NoSuchElementException:
            print("Error element not found, login might have succeeded unexpectedly.")

    finally:
        sleep(10)
        driver.quit()


negative_login_test()