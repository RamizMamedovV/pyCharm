

def main_menu():
    while True:
        print("""Меню:
         1. Создать заметку
         2. Распечатать все 
         3. Редактировать 
         4. Найти 
         5. Удалить
         6. Выход""")
        choice = input("Введите пункт меню: ")
        if choice.isdigit and 0 < int(choice) < 7:
            return int(choice)
        else:
            print("Введите ЦИФРУ от 1 до 6!")


def show_titles(data: list[dict], error_message):
    if data:
        for i, note in enumerate(data, 1):
            print(f'{i}. {note.get("title")}')


def print_all(data: list[dict], error_message):
    if data:
        for i in data:
            print(f'note_id = {i["note_id"]}')
            print(f"title: {i['title']}")
            print(f"content: {i['content']}")
            print(f"rec_time: {i['rec_time']}")


def user_edit_note(data: list[dict]) -> dict:
    temp = {}
    while True:
        choice = input("Введите ваш выбор: ")
        if choice.isdigit() and 0 < int(choice) <= len(data):
            temp['note_id'] = choice
            temp['title'] = input("Введите title: ")
            temp['content'] = input("Введите content: ")
            return temp
        else:
            print(f"Введите от 0 до {len(data)}")


def search(data: list[dict], error_message: str):
    if data:
        while True:
            choice = input("Введите искомый id: ")
            if choice.isdigit() and 0 < int(choice) <= len(data):
                for item in data:
                    if int(choice) == item['note_id']:
                        print(item['note_id'])
                        print(item['title'])
                        print(item['content'])
            else:
                print(f"Введите от 0 до {len(data)}")
    else:
        print(error_message)