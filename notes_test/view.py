import note_class


def user_choice(choice_text,
                start_int: int,
                end_int: int,
                error_message: str,
                menu: str = None) -> int:
    while True:
        print(menu)
        choice = input(choice_text)
        if choice.isdigit() and start_int <= int(choice) <= end_int:
            return int(choice)
        else:
            print_message(error_message)


def create_note():
    title = input('Enter title: ')
    content = input('Enter title: ')
    return [title, content]


def print_message(message: str):
    print('=' * len(message))
    print(message)
    print('=' * len(message))


def print_list(notebook: list[dict], error_message: str):
    if notebook:
        for note in notebook:
            print(note_class.Note.note_json_format(note))
        return True
    else:
        print_message(error_message)
        return False


def print_search_format(notebook: list[dict], error_message: str):
    if notebook:
        for note in notebook:
            print(note_class.Note.search_format(note))
        return True
    else:
        print_message(error_message)
        return False


def print_note(notebook: list[dict], note_id, error_message: str):
    if notebook:
        for note in notebook:
            if note_id == note_class.Note.get_note_id(note):
                print(note_class.Note.note_json_format(note))
    else:
        print_message(error_message)


