import model


def main():
    data_file = "notes.json"
    models = model.Model(data_file)
    # models.load_notes()

    while True:
        print("\nOptions:")
        print("1. Create a new note")
        print("2. List all notes")
        print("3. Read a note")
        print("4. Edit a note")
        print("5. Delete a note")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the note: ")
            content = input("Enter the content of the note: ")
            models.create_note(title, content)
        elif choice == "2":
            models.list_notes()
        elif choice == "3":
            note_id = int(input("Enter the ID of the note you want to read: "))
            models.read_note(note_id)
        elif choice == "4":
            note_id = int(input("Enter the ID of the note you want to edit: "))
            new_title = input("Enter the new title: ")
            new_content = input("Enter the new content: ")
            models.edit_note(note_id, new_title, new_content)
        elif choice == "5":
            note_id = int(input("Enter the ID of the note you want to delete: "))
            models.delete_note(note_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
