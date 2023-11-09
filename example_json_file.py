import json


# data_list = []
# Пример данных для записи в JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# # Запись данных в JSON-файл
# with open("data.json", "a", newline='') as json_file:
#     json_file.write('\n')
#     json.dump(data, json_file)



data_list = []

# Открываем файл JSON
with open("data.json", "r") as json_file:
    for line in json_file:
        # проверка наличия данных в строке перед вызовом json.loads()
        if line.strip():
            # Разбираем каждую строку как JSON-объект и добавляем его в список
            data = json.loads(line)
            data_list.append(data)

# Теперь data_list содержит список словарей
print(len(data_list))
for item in data_list:
    print(item["age"])


