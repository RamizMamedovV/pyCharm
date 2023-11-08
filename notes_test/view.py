

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
            print(error_message)


def create_note():
    title = input('Enter title: ')
    content = input('Enter title: ')
    return [title, content]


def print_message(message: str):
    print(message)

