from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Ваш код здесь
    
    # 1. Открываем сайт (используем URL из вашего прошлого скриншота)
    expected_url = "https://httpbin.qa-territory.online/"
    driver.get(expected_url)

    # 2. Получаем текущий URL
    current_url = driver.current_url

    # 3. Проверяем, что URL совпадает
    assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"
    print(f"Успех! Тест пройден. Текущий URL: {current_url}")

    driver.quit()