# lesson_06K/test_02_calc.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Используем Google Chrome, как требуется в задании
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    wait = WebDriverWait(driver, 60)  # таймаут больше 45 секунд

    # 1. Открываем страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. Устанавливаем задержку 45 секунд
    delay_input = wait.until(
        EC.presence_of_element_located((By.ID, "delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажимаем кнопки 7, +, 8, =
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()

    # 4. Ожидаем появления результата 15 в окне (элемент с классом screen)
    # Ждём не дольше 60 секунд, проверяя текст каждые 500 мс
    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # 5. Дополнительная проверка (assert) для явной фиксации результата
    screen = driver.find_element(By.CLASS_NAME, "screen")
    assert screen.text == "15", (
        f"Ожидался результат 15, но получен: {screen.text}"
    )