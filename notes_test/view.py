

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
    content = input('Enter content: ')
    return [title, content]


def print_message(message: str):
    print('=' * len(message))
    print(message)
    print('=' * len(message))


def print_list(notebook: list[dict], error_message: str):
    if notebook:
        for note in notebook:
            print(f" note_id: {note['note_id']}\n title: {note['title']}\n"
                  f" rec_time: {note['date']}\n content: {note['content']}")
            print("-"*10)
        return True
    else:
        print_message(error_message)
        return False


def print_search_format(notebook: list[dict], error_message: str):
    if notebook:
        for note in notebook:
            print(f" note_id: {note['note_id']}: title: {note['title']}")
            print("-" * 10)
        return True
    else:
        print_message(error_message)
        return False


def print_note(notebook: list[dict], note_id, error_message: str):
    if notebook:
        for note in notebook:
            if note_id == int(note['note_id']):
                print(f" note_id: {note['note_id']} title: {note['title']}\n"
                      f" rec_time: {note['date']}\n content: {note['content']}")
                print("-" * 10)
    else:
        print_message(error_message)


def get_node_date(note):
    return note['date']


def format_date(notebook: list[dict]):
    sorted_notebook = sorted(notebook, key=get_node_date)
    print_list(sorted_notebook, "sort_error")
