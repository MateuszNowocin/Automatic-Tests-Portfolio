import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def website_testing_script():
    os.environ['PATH'] += r"C:\SeleniumDrivers"
    driver = webdriver.Chrome()

    #otwieramy stronę sklepu
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(30) #potencjalne czekanie na odpowiedź,
                               #dotyczy WSZYSTKICH czynności w skrypcie

    #wpisujemy NIEPOPRAWNE username
    username = driver.find_element(By.ID, 'user-name')
    username.send_keys("standard_user22")

    #wpisujemy NIEPOPRAWNE hasło
    password = driver.find_element(By.ID, 'password')
    password.send_keys("secret_sauce22")

    #klikamy przycisk logowania
    login_form = driver.find_element(By.ID, 'login-button')
    login_form.click()

    #sprawdzamy, czy wyświetlił się błąd
    try:
        exception = driver.find_element(By.XPATH, "//button[@class='error-button']")
    except:
        print("Niepoprawne hasło lub nazwa użytkownika.")

    #wpisujemy username
    username = driver.find_element(By.ID, 'user-name')
    username.send_keys(Keys.LEFT_CONTROL, "A", Keys.DELETE)
    username.send_keys("standard_user")

    #wpisujemy hasło
    password = driver.find_element(By.ID, 'password')
    password.send_keys(Keys.LEFT_CONTROL, "A", Keys.DELETE)
    password.send_keys("secret_sauce")

    #klikamy przycisk logowania
    login_form = driver.find_element(By.ID, 'login-button')
    login_form.click()

    #sortujemy artykuły od najtańszych do najdroższych
    dropdown = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
    dd = Select(dropdown) #sprawdzamy, czy wybrany element to menu typu dropdown
    dd.select_by_visible_text("Price (high to low)")

    #dodajemy item to koszyka
    add_item = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_item.click()

    #wchodzimy w podstronę innego itemu
    item_link = driver.find_element(By.ID, 'item_1_title_link')
    item_link.click()

    #dodajemy powyższy item do koszyka
    add_to_cart = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bolt-t-shirt')
    add_to_cart.click()

    #wchodzimy w koszyk
    move_to_cart = driver.find_element(By.ID, 'shopping_cart_container')
    move_to_cart.click()

    #usuwamy item z koszyka
    remove_from_cart = driver.find_element(By.ID, 'remove-sauce-labs-bolt-t-shirt')
    remove_from_cart.click()

    #przechodzimy do checkoutu
    checkout = driver.find_element(By.NAME, 'checkout')
    checkout.click()

    #wpisujemy imie
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys("Jan")

    #wpisujemy nazwisko
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys("Kowalski")

    #wpisujemy kod pocztowy
    postal_code = driver.find_element(By.ID, 'postal-code')
    postal_code.send_keys("02-222")

    #klikamy przycisk kontynuuj
    checkout_continue = driver.find_element(By.ID, 'continue')
    checkout_continue.click()

    #klikamy przycisk zakończ
    finish_button = driver.find_element(By.ID, 'finish')
    finish_button.click()

    #czekamy aż wyświetli się komunikat o zakonczeniu zakupu. Jeśli tak - test zakończony pomyślnie
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'complete-header'), #znajdujemy element po klasie
            'Thank you for your order!' #oczekiwany tekst
        )
    )

    sleep(5)

    #zamykamy przeglądarkę
    driver.quit()

def main():
    website_testing_script()

if __name__ == '__main__':
    main()