import controller
main_menu = """Меню:
         1. Создать заметку
         2. Распечатать все 
         3. Редактировать 
         4. Найти 
         5. Удалить
         6. Выход"""


if __name__ == '__main__':
    controller.start(main_menu, 0, 6)
