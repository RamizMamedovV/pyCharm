class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def list_notes(self):
        for index, note in enumerate(self.notes, start=1):
            print(f"Note {index}:\n{note}\n")

    def read_note(self, index):
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            print(f"Note {index}:\n{note}\n")
        else:
            print("Note not found.")

    def edit_note(self, index, title, content):
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            note.title = title
            note.content = content
            print("Note edited successfully.")
        else:
            print("Note not found.")

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            print("Note deleted successfully.")
        else:
            print("Note not found.")

def main():
    note_manager = NoteManager()

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
            note_manager.create_note(title, content)
            print("Note created successfully.")
        elif choice == "2":
            note_manager.list_notes()
        elif choice == "3":
            index = int(input("Enter the index of the note you want to read: "))
            note_manager.read_note(index)
        elif choice == "4":
            index = int(input("Enter the index of the note you want to edit: "))
            title = input("Enter the new title: ")
            content = input("Enter the new content: ")
            note_manager.edit_note(index, title, content)
        elif choice == "5":
            index = int(input("Enter the index of the note you want to delete: "))
            note_manager.delete_note(index)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
