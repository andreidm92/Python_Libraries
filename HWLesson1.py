# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
import requests
import json


username = 'admi70@rambler.ru'
password = 'Rerehepf20'
repos = requests.get('https://api.github.com/user/repos', auth=(username, password))
repos.json()
for repo in repos.json():
    print(repo['html_url'])

"""2.Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."""

# Адрес api метода для запроса get
link = 'https://api.oilpriceapi.com/v1/prices/latest'
headers = {
    'Authorization': 'Token 03a07f377a781196879b3d67cab7cd3c',
    'Content-Type': 'application/json'
}
# Отправляем get request (запрос GET)
oilpr = requests.get(url = link, headers = headers)
info = oilpr.json()
price = info['data']['formatted']
print(f' Цена нефти: {price}')

