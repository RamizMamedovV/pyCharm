import view
import model
import note

""" 1. Создать заметку 2. Распечатать все 3. Редактировать 
    4. Найти            5. Удалить        6. Выход"""


def start(message: str, choice_start: int, choice_length: int):
    model.start()
    while True:
        choice = view.user_choice(message,
                                  choice_start, choice_length)
        match choice:
            #   1. Создать заметку
            case 1:
                temp = view.create_note()
                model.add_new_node(temp)
            #   2. Распечатать все
            case 2:
                view.print_all(model.get_notes(),
                               "заметок пока нет!!")
            #   3. Редактировать
            case 3:
                view.show_titles(model.get_notes(),
                                 "заметок пока нет!!")
                temp = (view.user_edit_note(model.get_notes()))
                view.print_is_done(model.edit_note(int(temp['note_id']),
                                                   temp['title'], temp['content']))
            #   4. Найти
            case 4:
                view.show_titles(model.get_notes(), "заметок пока нет!!")
                view.search(model.get_notes(), "Пусто((:")
            #   5. Удалить
            case 5:
                view.show_titles(model.get_notes(), "заметок пока нет!!")
                choice = view.user_choice("Введите искомый id: ",
                                          1, model.get_notes_length())
                view.print_is_done(model.delete_note(choice))
            #   6. Выход
            case 6:
                return
