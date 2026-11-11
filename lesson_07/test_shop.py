# lesson_07/test_shop.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --- Page Objects ---

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_id):
        self.wait.until(EC.element_to_be_clickable((By.ID, item_id))).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_name, last_name, zip_code):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def continue_to_overview(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    def get_total(self):
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text  # Вернет "Total: $58.29"


# --- Тест ---

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(driver):
    # 1. Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавление товаров
    main_page = MainPage(driver)
    main_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
    main_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    main_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")
    main_page.go_to_cart()

    # 3. Корзина
    cart_page = CartPage(driver)
    cart_page.checkout()

    # 4. Оформление заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Петров", "123456")
    checkout_page.continue_to_overview()

    # 5. Получение и проверка итоговой суммы
    total_text = checkout_page.get_total()
    expected_price = "$58.29"
    
    assert expected_price in total_text, (
        f"Ожидалась сумма {expected_price}, но на странице указано: {total_text}"
    )