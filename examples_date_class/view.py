

def show_menu() -> int:
    while True:
        print("""Меню:
         1. Создать заметку
         2. Распечатать все 
         3. Редактировать 
         4. Найти 
         5. Удалить
         6. Выход""")
        choice = input("Выберите из меню: ")
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)
        else:
            print("Введите ЧИСЛО от 1 до 6!")