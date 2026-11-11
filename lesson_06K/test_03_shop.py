# lesson_06K/test_03_shop.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Используем Firefox, как указано в задании
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_total(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуемся как standard_user
    # Обратите внимание: на этом сайте для standard_user пароль всегда "secret_sauce"
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавляем товары в корзину
    # Ждем загрузки каталога и кликаем по кнопкам "Add to cart"
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
    ).click()
    
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))
    ).click()

    # 4. Переходим в корзину
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    # 5. Нажимаем Checkout
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # 6. Заполняем форму своими данными
    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")
    
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    # 7. Нажимаем кнопку Continue
    wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    ).click()

    # 8. Читаем со страницы итоговую стоимость (Total)
    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text  # Текст будет вида "Total: $58.29"

    # 9. Закрываем браузер (это делает фикстура driver в конце теста через driver.quit())

    # 10. Проверяем (assert), что итоговая сумма равна $58.29
    # Так как в тексте есть слово "Total:", мы извлекаем только цену или проверяем вхождение
    expected_total = "$58.29"
    
    assert expected_total in total_text, (
        f"Ожидалась итоговая сумма {expected_total}, но получено: {total_text}"
    )