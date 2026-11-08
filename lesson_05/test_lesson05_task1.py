from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_navigation():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(15) # Ограничиваем время загрузки, чтобы не ждать по 80 секунд

    try:
        # 1. Открываем главную страницу
        base_url = "https://httpbin.qa-territory.online/"
        driver.get(base_url)

        # 2. Находим ссылку "HTML Form" по тексту и кликаем
        html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
        html_form_link.click()
        
        # Небольшая пауза, чтобы страница успела прогрузиться
        time.sleep(1) 

        # (Промежуточная проверка: убеждаемся, что URL изменился)
        url_after_click = driver.current_url
        assert url_after_click != base_url, "URL не изменился после клика по ссылке!"

        # 3. Возвращаемся назад
        driver.back()

        # Пауза, чтобы браузер успел вернуться и обновить адресную строку
        time.sleep(1)

        # 4. Проверяем URL после возврата
        returned_url = driver.current_url
        
        # Проверяем, что мы вернулись на главную страницу
        assert returned_url == base_url, f"Ожидался URL {base_url}, но получен {returned_url}"
        print(f"Успех! Мы вернулись на страницу: {returned_url}")

    finally:
        # Закрываем браузер при любом исходе
        driver.quit()