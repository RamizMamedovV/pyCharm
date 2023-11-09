import json
import os
from datetime import datetime
import note_class


class Model:
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
        note = note_class.Note(note_id, title, content, timestamp)
        self.notes.append(note)
        self.save_notes()
        print("Note created successfully.")

    def list_notes(self):
        for note in self.notes:
            print(f"ID: {note.identity}, Title: {note.title}, Timestamp: {note.rec_time}")
        if not self.notes:
            print("No notes found.")

    def read_note(self, note_id):
        for note in self.notes:
            if note.identity == note_id:
                print(f"Title: {note.title}\nContent: {note.context}\nTimestamp: {note.rec_time}")
                return
        print("Note not found.")

    def edit_note(self, note_id, new_title, new_content):
        for note in self.notes:
            if note.identity == note_id:
                note.title = new_title
                note.context = new_content
                note.rec_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Note edited successfully.")
                return
        print("Note not found.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.identity == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Note deleted successfully.")
                return
        print("Note not found.")