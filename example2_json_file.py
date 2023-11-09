import json

data_str = '{"admin":{"name": "ramiz"}}'
# print(type(data_str))

# Преобразование ПРАВИЛЬНОЙ ('{"admin":{"name": "ramiz"}}')
# строки в json(java script ...)
data_dict = json.loads(data_str)

print(data_dict)        # {'admin': {'name': 'ramiz'}} "<class 'dict'>"
print(type(data_str))   # <class 'str'>
print(type(data_dict))  # <class 'dict'>
# print(data_dict['admin']['name'])

# with open('data.json', 'r') as f:
# # Преобразование json файла в словарь
#         data_dict = json.load(f)      # считывание файла в виде словаря

# Преобразование json "<class 'dict'> в строку "<class 'str'>"
# new_json = json.dumps(data_dict, indent=2)
# print(new_json)
# print(type(new_json))   # <class 'str'>
# new_json_str = json.dumps(data_str)
# print(new_json_str)
# print(type(new_json_str))   # <class 'str'>

