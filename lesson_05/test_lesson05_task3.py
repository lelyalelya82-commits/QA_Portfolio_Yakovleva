from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()

    try:
        # 1. Открываем страницу
        driver.get("https://httpbin.qa-territory.online/links/10")

        # 2. Находим все ссылки на странице с помощью find_elements
        links = driver.find_elements(By.TAG_NAME, "a")

        # 3. Проверяем, что количество ссылок равно 9
        assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

        # 4. Проверяем, что все ссылки отображаются на странице
        for index, link in enumerate(links):
            assert link.is_displayed(), f"Ссылка с индексом {index} не отображается на странице"

        # 5. Проверяем, что текст первой ссылки (индекс [0]) содержит "1"
        first_link_text = links[0].text
        assert "1" in first_link_text, f"Текст первой ссылки '{first_link_text}' не содержит '1'"

        print("Успех! Все проверки для множества элементов пройдены.")

    finally:
        # Закрываем браузер при любом исходе
        driver.quit()