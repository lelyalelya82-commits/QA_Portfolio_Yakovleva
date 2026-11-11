# lesson_07/test_calculator.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay_value):
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def click_button(self, button_text):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
        )
        button.click()

    def get_result(self):
        # Ждем появления результата "15" в окне
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # 1. Создаем объект страницы
    calculator_page = CalculatorPage(driver)
    
    # 2. Выполняем действия (только через методы страницы)
    calculator_page.open()
    calculator_page.set_delay(45)
    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")
    
    # 3. Получаем результат и проверяем
    result = calculator_page.get_result()
    assert result == "15", f"Ожидался результат 15, но получен {result}"
    