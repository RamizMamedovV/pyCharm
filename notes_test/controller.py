import view
import model
import text_fields as texts

# data_json_file = "note_data.json"
# main_menu = """Меню:
#          1. Создать заметку
#          2. Распечатать все
#          3. Распечатать по дате
#          4. Редактировать
#          5. Найти
#          6. Удалить
#          7. Записать в note_data.json
#          8. Найти по кусочку текста
#          9. Выход"""
# choice_text = "Введите пункт меню: "
# search_node_id = "Введите искомый note_id: "
# empty_message = "А здесь ещё пусто)))"
# error_message = "Не верный ввод!"
# well_done_message = "Сделано!"
# something_wrong_message = "Что-то пошло не так!!!"
# sub_text = "Введите искомый кусок текста: "
# same_edit_message = ("               !!!ВНИМАНИЕ!!!\n"
#                      "Если не нужно менять, просто нажмите ENTER\n"
#                      "              Но дата изменится")


def start():
    notebook = model.Notebook(texts.data_json_file)
    while True:
        choice = view.user_choice(texts.choice_text,
                                  1,
                                  9,
                                  texts.error_message,
                                  texts.main_menu)
        match choice:

            case 1:   # 1. Создать заметку
                user_input = view.create_note()
                notebook.create_note(notebook.get_note_id() + 1, *user_input)

            case 2:   # 2. Распечатать все
                view.print_list(notebook.get_notes(),
                                texts.empty_message)

            case 3:   # 3. Распечатать по дате
                view.format_date(notebook.get_notes())

            case 4:  # 4. Редактировать
                if view.print_search_format(notebook.get_notes(),
                                            texts.empty_message):
                    choice = view.user_choice(texts.search_node_id,
                                              1,
                                              notebook.get_note_id(),
                                              texts.error_message)
                    view.print_message(texts.same_edit_message)
                    user_input = view.create_note()
                    if notebook.edit_note(choice, *user_input):
                        view.print_message(texts.well_done_message)
                    else:
                        view.print_message(texts.something_wrong_message)

            case 5:  # 5. Найти
                if view.print_search_format(notebook.get_notes(),
                                            texts.empty_message):
                    choice = view.user_choice(texts.search_node_id,
                                              1,
                                              notebook.get_note_id(),
                                              texts.error_message)
                    view.print_note(notebook.get_notes(),
                                    choice,
                                    texts.error_message)

            case 6:  # 6. Удалить
                if view.print_search_format(notebook.get_notes(),
                                            texts.empty_message):
                    choice = view.user_choice(texts.search_node_id,
                                              1,
                                              notebook.get_note_id(),
                                              texts.error_message)
                    notebook.delete_note(choice)
                    view.print_message(texts.well_done_message)
                else:
                    view.print_message(texts.something_wrong_message)

            case 7:  # Записать в note_data.json
                if notebook.save_note_to_json():
                    view.print_message(texts.well_done_message)
                else:
                    view.print_message(texts.empty_message)

            case 8:  # Найти по кусочку текста
                user_choice = view.user_text_choice(texts.sub_text)
                sub_list = notebook.search_sub_note(user_choice)
                view.print_list(sub_list, texts.empty_message)

            case 9:  # Выход
                return

