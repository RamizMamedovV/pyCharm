"""
from typing import List
from create_contact import contact_tuple

from phonebook_user import print_menu as user_print
"""
menu = """
1. Открыть файл телефонной книги
2. Сохранить файл телефонной книги
3. Показать все контакты
4. Найти контакт
5. Добавить контакт
6. Изменить контакт
7. Удалить контакт
8. Выход
"""

start_menu = """
not available-----------------------
1. Открыть файл телефонной книги    |
2. Сохранить файл телефонной книги  |
3. Показать все контакты            |
4. Найти контакт                    |
6. Изменить контакт                 |
7. Удалить контакт                  |
------------------------------------
5. Добавить контакт
8. Выход
"""
file_name = None
data = {}
count = 0

while True:

    print(menu)
    user_choice = int(input("enter your choice: "))
    if user_choice == 1:
        file_name = input("enter name of file to create notebook: ")
    elif user_choice == 2:
        with open(file_name, 'a', encoding='UTF-8') as file:
            for k, v in data.values():
                file.write(v)
        print("done")
    if user_choice == 3:
        for item, value in data.items():
            print(item, value)
    elif user_choice == 4:
        for item, value in data.items():
            print(item, value)
        user_choice = int(input("enter id: "))
        print(data[user_choice])
    elif user_choice == 5:
        contact_id = len(data)
        contacts = [input("name: "), input("phone: ")]
        data[contact_id] = contacts
    elif user_choice == 6:
        for item, value in data.items():
            print(item, value)
        contact_id = int(input("enter id for change: "))
        contact_to_del = [data.pop(contact_id)]
        contacts = [input("name: "), input("phone: ")]
        data[contact_id] = contacts
        print(f"{contact_to_del} changed on {contacts}")
    elif user_choice == 7:
        for item, value in data.items():
            print(item, value)
        user_choice = int(input("enter your choice for delete: "))
        if 0 <= user_choice <= len(data):
            print(f" deleted{data.pop(user_choice)}")
        else:
            print("wrong id")
    elif user_choice == 8:
        break







# text_del = """
# def is_start(name):
#     try:
#         with open(name, 'r', encoding='UTF-8') as file:
#             contacts = file.read()
#             if len(contacts) == 0:
#                 return False
#     except FileNotFoundError:
#         print("File Not Found Error. Please try again!")
#         return False
#     return True
#
#
# #
# # def print_contacts():
# #     global data
# #     with open(file_name, 'r', encoding='UTF-8') as file:
# #          list_of_contacts = "file"
# #     if len(list_of_contacts) > 0:
# #         data[list_of_contacts[0]] = {'name': list_of_contacts[0][1],
# #                                      'phone': list_of_contacts[0][2]}
# #     print(data)
# #
# #
# # def read_file(file_name_to_read) -> list[str]:
# #     print(file_name_to_read)
# #     with open(file_name_to_read, 'r', encoding='UTF-8') as file:
# #         contacts = "file"
# #     print(contacts)
# #     return contacts
#
#
# def add_contact_to_dict(name):
#     dict_contacts = {}
#     list_contacts = contact_tuple()
#     id_contact, name, phone = list_contacts
#     dict_contacts[id_contact] = {'name': name, 'phone': phone}
#     return dict_contacts
#
#
# def add_contact_to_file(name):
#     global data
#     with open(file_name, 'a', encoding='UTF-8') as file:
#         for item in data:
#             file.write(f"{int(item[0][0])};")
#             file.write(f"{item[0][1]};")
#             file.write(f"{item[0][2]}\n")
#
#
# def start(name):
#     global count
#     if is_start(name):
#         while True:
#             user_enter = int(user_print(menu))
#             if user_enter == 5:
#                 count += 1
#                 data[count] = add_contact_to_dict(name)
#             if user_enter == 2:
#                 add_contact_to_file(name)
#                 print("added")
#             else:
#                 return
#     else:
#         user_enter = int(user_print(start_menu))
#         if user_enter == 5:
#             add_contact_to_dict(name)
#         elif user_enter == 8:
#             return
#         else:
#             print("Not correct")
#
#
# start(file_name)"""

