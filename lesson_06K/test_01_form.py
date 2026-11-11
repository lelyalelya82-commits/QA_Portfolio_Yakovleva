import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color

@pytest.fixture
def driver():
    driver = webdriver.Edge()  
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(driver):
    wait = WebDriverWait(driver, 10)

     # 1. Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # 2. Заполняем форму значениями
    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",  # Оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for name, value in data.items():
        # Ждём, пока поле появится, и заполняем его
        field = wait.until(
            EC.presence_of_element_located((By.NAME, name))
        )
        field.clear()
        if value:  # Если значение не пустое, вводим текст
            field.send_keys(value)

    # 3. Нажимаем кнопку Submit
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    # 4. Проверяем, что поле Zip code подсвечено красным
    # Ждём появления элемента с классом alert-danger (красный фон)
    zip_alert = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger"))
    )
    bg_color_zip = zip_alert.value_of_css_property("background-color")
    hex_color_zip = Color.from_string(bg_color_zip).hex.lower()
    expected_red = "#f8d7da"  # Стандартный оттенок красного в Bootstrap
    assert hex_color_zip == expected_red, (
        f"Поле Zip code не подсвечено красным: {hex_color_zip}, ожидалось {expected_red}"
    )

        # 5. Проверяем, что остальные поля подсвечены зелёным
    # Ищем любые элементы с классом alert-success (без привязки к тегу input)
    other_fields = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".alert-success"))
    )

    # Убедимся, что среди них нет поля zip-code
    for field in other_fields:
        assert field.get_attribute("id") != "zip-code", (
            "Поле Zip code не должно быть зелёным"
        )

    # Дополнительно проверяем, что количество зелёных полей равно 9
    assert len(other_fields) == 9, (
        f"Ожидалось 9 зелёных полей, найдено {len(other_fields)}"
    )

   