from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(15)

    try:
        # 1. Открываем страницу с формой
        driver.get("https://httpbin.qa-territory.online/forms/post")

        # 2. Заполняем поле (используем By.NAME, как сказано в задании)
        name_field = driver.find_element(By.NAME, "custname")
        name_field.send_keys("Test User")

        # 3. Отправляем форму напрямую
        form = driver.find_element(By.TAG_NAME, "form")
        form.submit()

        # 4. Ждем, пока текст "Test User" появится на странице (до 15 секунд)
        # Это надежнее, чем ждать конкретный тег <pre>
        WebDriverWait(driver, 15).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Test User")
        )

        # 5. Дополнительная проверка: убеждаемся, что текст действительно есть
        page_text = driver.find_element(By.TAG_NAME, "body").text
        assert "Test User" in page_text, "Ошибка! На странице нет результата отправки формы."
        print("Успех! Форма отправлена, и результат отображен на странице.")

    finally:
        # Закрываем браузер при любом исходе
        driver.quit()