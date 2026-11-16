import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("YOUGILE_TOKEN")
base_url = os.getenv("YOUGILE_BASE_URL")

print("--- ПРОВЕРКА ТОКЕНА ---")
if not token:
    print("❌ ОШИБКА: Токен не найден! Проверьте файл .env")
else:
    print(f"✅ Токен найден. Начинается с: {token[:10]}...")
    print(f"✅ Длина токена: {len(token)} символов")

print("\n--- ПРОВЕРКА ЗАПРОСА ---")
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Пробуем получить список проектов (безопасный GET-запрос)
response = requests.get(f"{base_url}/projects", headers=headers)
print(f"Статус ответа: {response.status_code}")
print(f"Ответ сервера: {response.text}")