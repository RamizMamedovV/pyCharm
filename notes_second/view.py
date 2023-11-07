def user_choice(message: str, choice_start: int, choice_length: int):
    while True:
        print(message)
        choice = input("Введите пункт меню: ")
        if choice.isdigit and choice_start <= int(choice) <= choice_length:
            return int(choice)
        else:
            print(f"Введите ЦИФРУ от {choice_start} "
                  f"до {choice_length} включительно!")


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
            # print(f"rec_time: {i['rec_time']}")
    else:
        print(error_message)


def user_edit_note(data: list[dict]) -> dict:
    temp = {}
    while True:
        choice = input("Введите ваш выбор: ")
        if choice.isdigit() and 1 < int(choice) <= len(data):
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
                        return
            else:
                print(f"Введите от 0 до {len(data)}")
    else:
        print(error_message)


def print_is_done(is_done: bool):
    if is_done:
        print("Done")
    else:
        print("Error")


def create_note(note_id: int) -> dict:
    return {'note_id': int(note_id),
            'title': input("Введите title: "),
            'content': input("Введите content: ")}
