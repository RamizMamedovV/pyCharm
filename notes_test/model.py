import json
import os
import pytz
import note_class
from datetime import datetime as date


class Notebook:

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.notebook = []
        self.open()
        # if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
        #     try:
        #         with open(self.data_file, 'r', encoding='UTF-8') as file:
        #             self.notebook = json.load(file)
        #     except json.decoder.JSONDecodeError as e:
        #         print(f"Error decoding JSON in {self.data_file}: {e}")

    def open(self):
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            try:
                with open(self.data_file, 'r', encoding='UTF-8') as file:
                    self.notebook = json.load(file)
            except json.decoder.JSONDecodeError as e:
                print(f"Error decoding JSON in {self.data_file}: {e}")

    def get_notes(self):
        return self.notebook

    def create_note(self, note_id: int,
                    title: str,
                    content: str) -> bool:
        new_note = note_class.Note(note_id,
                                   title,
                                   content,
                                   date.now().strftime("%d.%m.%y %H:%M:%S"))
        self.notebook.append(new_note.note_json_format())
        return True

    def get_note_id(self):
        return len(self.notebook)

    def edit_note(self, note_id: int,
                  title: str,
                  content: str) -> bool:
        for note in self.notebook:
            if note_id == int(note['note_id']):
                note['title'] = title if title != '' else note['title']
                note['content'] = content if content != '' else note['content']
                note['date'] = date.now().strftime("%d.%m.%y %H:%M:%S")
                return True
        return False

    def delete_note(self, note_id: int) -> bool:
        for note in self.notebook:
            if note_id == int(note['note_id']):
                del self.notebook[note_id-1]
                self.format_notes()
                return True
        return False

    def format_notes(self):
        i = 0
        for note in self.notebook:
            i += 1
            note['note_id'] = i

    def save_note_to_json(self):
        with open(self.data_file, 'w', encoding='UTF-8') as file:
            json.dump(self.notebook, file, indent=3)

    def search_sub_note(self, sub_str: str) -> list:
        notes = []
        for note in self.notebook:
            for fields in note.values():
                if sub_str.lower() in str(fields).lower():
                    notes.append(note)
        return notes
