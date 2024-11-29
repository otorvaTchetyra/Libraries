import requests

# Отправляем GET-запрос на API и выводим данные
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()  # Получаем данные в формате JSON
print(data[:5])  # Выводим 5 записей
