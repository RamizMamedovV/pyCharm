import view
import model

"""Меню:1. Создать заметку 2. Распечатать все  3. Редактировать 
 4. Найти  5. Удалить 6. Выход"""

data = []


def start():
    while True:
        model.start()
        choice = view.show_menu()
        match choice:
            case 1:
                model.add_contact()
            case 2:
                model.print_notes()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                return