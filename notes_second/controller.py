import view
import model

""" 1. Создать заметку 2. Распечатать все 3. Редактировать 
    4. Найти            5. Удалить        6. Выход"""


def start(message: str, choice_start: int, choice_length: int):
    model.start()
    while True:
        choice = view.user_choice(message, 0, choice_length)
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
                view.search(model.get_notes(), "Пусто((:")
            case 5:
                view.show_titles(model.get_notes(), "заметок пока нет!!")
                print(f"model.get_notes_length()= {model.get_notes_length()}")
                choice = view.user_choice("Введите искомый id: ",
                                          0, model.get_notes_length())
                print(type(choice))
                print(f"choice= {choice}")
                flag = model.delete_note(choice)
                if flag:
                    view.print_message("Done")
                else:
                    view.print_message("Error")
            case 6:
                return
