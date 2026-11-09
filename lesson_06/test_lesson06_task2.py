from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- НАСТРОЙКИ ТЕСТОВЫХ ДАННЫХ ---
# 1. Замените логины на ваши реальные логины
USER1_USERNAME = "user_test_1"  
USER2_USERNAME = "user_test_2"  

# 2. Вставьте сюда длинные строки куки, которые вы скопировали из DevTools
USER1_COOKIES = [
    {"name": "session", "value": "Nzk0OGVlMmQtZWFiYS00ODM2LTg2MjItZTlmYTk2NGYzYjc1"},
]

USER2_COOKIES = [
    {"name": "session", "value": "YzBkYzkwZTktMzA2My00NGI5LTlmZGEtMWQ1MWEwZjQwMmEy"},
]

BASE_URL = "https://gitflic.ru"


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открываем главную страницу
        driver.get(BASE_URL)

        # 2. Устанавливаем cookie пользователя 1
        for cookie in USER1_COOKIES:
            driver.add_cookie(cookie)

        # 3. Обновляем страницу
        driver.refresh()

        # 4. Переходим на страницу пользователя 1
        user1_profile_url = f"{BASE_URL}/user/{USER1_USERNAME}"
        driver.get(user1_profile_url)

        wait.until(EC.url_contains(f"/user/{USER1_USERNAME}"))
        saved_url_user1 = driver.current_url
        print(f"URL пользователя 1: {saved_url_user1}")

        # 5. Очищаем cookie
        driver.delete_all_cookies()

        # 6. Устанавливаем cookie пользователя 2
        driver.get(BASE_URL)
        for cookie in USER2_COOKIES:
            driver.add_cookie(cookie)

        # 7. Обновляем страницу
        driver.refresh()

        # 8. Переходим на страницу пользователя 2
        user2_profile_url = f"{BASE_URL}/user/{USER2_USERNAME}"
        driver.get(user2_profile_url)

        wait.until(EC.url_contains(f"/user/{USER2_USERNAME}"))
        saved_url_user2 = driver.current_url
        print(f"URL пользователя 2: {saved_url_user2}")

        # 9. Проверяем, что URL различаются
        assert saved_url_user1 != saved_url_user2, (
            f"Ошибка: URL совпадают. Пользователь 1: {saved_url_user1}, "
            f"Пользователь 2: {saved_url_user2}"
        )
        print("Тест пройден: URL различаются, подмена сессии работает корректно.")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()