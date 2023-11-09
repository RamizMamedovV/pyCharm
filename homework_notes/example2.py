import json
import os
from datetime import datetime

class Note:
    def __init__(self, id, title, content, timestamp):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }


class NoteManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.notes = []

    def load_notes(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.notes = json.load(file)

    def save_notes(self):
        notes_as_dicts = [note.to_dict() for note in self.notes]
        with open(self.data_file, 'w') as file:
            json.dump(notes_as_dicts, file, indent=4)

    def create_note(self, title, content):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note_id = len(self.notes) + 1
        note = Note(note_id, title, content, timestamp)
        self.notes.append(note)
        self.save_notes()
        print("Note created successfully.")

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}, Title: {note.title}, Timestamp: {note.timestamp}")
        if not self.notes:
            print("No notes found.")

    def read_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                print(f"Title: {note.title}\nContent: {note.content}\nTimestamp: {note.timestamp}")
                return
        print("Note not found.")

    def edit_note(self, note_id, new_title, new_content):
        for note in self.notes:
            if note.id == note_id:
                note.title = new_title
                note.content = new_content
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Note edited successfully.")
                return
        print("Note not found.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Note deleted successfully.")
                return
        print("Note not found.")

def main():
    data_file = "notes.json"
    note_manager = NoteManager(data_file)
    # note_manager.load_notes()

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
        elif choice == "2":
            note_manager.list_notes()
        elif choice == "3":
            note_id = int(input("Enter the ID of the note you want to read: "))
            note_manager.read_note(note_id)
        elif choice == "4":
            note_id = int(input("Enter the ID of the note you want to edit: "))
            new_title = input("Enter the new title: ")
            new_content = input("Enter the new content: ")
            note_manager.edit_note(note_id, new_title, new_content)
        elif choice == "5":
            note_id = int(input("Enter the ID of the note you want to delete: "))
            note_manager.delete_note(note_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
