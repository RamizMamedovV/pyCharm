import view
import model

""" 1. Создать заметку 2. Распечатать все 3. Редактировать 
    4. Найти            5. Удалить        6. Выход"""


def start():
    model.start()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                pass
            case 2:
                view.print_all(model.get_notes(), "заметок пока нет!!")
            case 3:
                view.show_titles(model.get_notes(), "заметок пока нет!!")
                temp = (view.user_edit_note(model.get_notes()))
                model.edit_note(int(temp['note_id']), temp['title'], temp['content'])
            case 4:
                view.show_titles(model.get_notes(), "заметок пока нет!!")
                pass
            case 5:
                pass
            case 6:
                return
