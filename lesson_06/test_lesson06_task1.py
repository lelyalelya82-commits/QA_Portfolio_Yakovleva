import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Открываем страницу
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Находим и нажимаем кнопку "Start"
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # 3. Явное ожидание появления текста "Hello World!"
        wait = WebDriverWait(driver, 10)
        finish_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        # 4. Сохраняем скриншот
        # abspath делает путь абсолютным, dirname берет папку с этим файлом
        base_dir = os.path.dirname(os.path.abspath(__file__))
        screenshots_dir = os.path.join(base_dir, "screenshots")
        
        # На всякий случай создаем папку, если ее вдруг нет (exist_ok=True не даст упасть, если она есть)
        os.makedirs(screenshots_dir, exist_ok=True)

        screenshot_path = os.path.join(screenshots_dir, "dynamic_loading.png")
        driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранён: {screenshot_path}")

        # 5. Проверяем текст
        actual_text = finish_element.text
        print(f"Полученный текст: {actual_text!r}")
        
        assert actual_text == "Hello World!", (
            f"Ожидался текст 'Hello World!', но получен {actual_text!r}"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()