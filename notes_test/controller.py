import view
import model

data_json_file = "my_data.json"
main_menu = """Меню:
         1. Создать заметку
         2. Распечатать все 
         3. Редактировать 
         4. Найти 
         5. Удалить
         6. Выход"""
choice_text = "Введите пункт меню: "
search_node_id = "Введите искомый note_id: "


def start():
    notebook = model.Notebook(data_json_file)
    while True:
        choice = view.user_choice(choice_text,
                                  1,
                                  len(main_menu),
                                  "error",
                                  main_menu)
        match choice:
            # 1. Создать заметку
            case 1:
                user_input = view.create_note()
                notebook.create_note(notebook.get_note_id()+1, *user_input)
            # 2. Распечатать все
            case 2:
                notebook.print_list()
            # 3. Редактировать
            case 3:
                notebook.print_search_format()
                choice = view.user_choice(search_node_id,
                                          1,
                                          notebook.get_note_id(),
                                          "error")
                user_input = view.create_note()
                if notebook.edit_note(choice, *user_input):
                    view.print_message("Done")
                else:
                    view.print_message("Error")

            # 4. Найти
            case 4:
                notebook.print_search_format()
                choice = view.user_choice(search_node_id,
                                          1,
                                          notebook.get_note_id(),
                                          "error")
                print(notebook.print_search_note(choice))
                print("type = ")
                print(type(notebook.print_search_note(choice)))
            # 5. Удалить
            case 5:
                pass
            case 6:
                return


