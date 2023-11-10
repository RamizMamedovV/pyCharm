import json
import os

import pytz

import note_class
from datetime import datetime as date


class Notebook:

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.notebook = []
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            try:
                with open(self.data_file, 'r', encoding='utf-8') as file:
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
        self.notebook.append(new_note)
        return True

    def get_note_id(self):
        return len(self.notebook)

    def edit_note(self, note_id: int,
                  title: str,
                  content: str) -> bool:
        for note in self.notebook:
            if note_id == note_class.Note.get_note_id(note):
                note_class.Note.set_note_title(note, title)
                note_class.Note.set_note_content(note, content)
                note_class.Note.set_note_date(note, date.now().strftime("%d.%m.%y %H:%M:%S"))
                return True
        return False

    def delete_note(self, note_id: int) -> bool:
        for note in self.notebook:
            if note_id == note_class.Note.get_note_id(note):
                del self.notebook[note_id - 1]
                self.format_notes()
                return True
        return False

    def format_notes(self):
        i = 0
        for note in self.notebook:
            i += 1
            note_class.Note.set_note_id(note, i)

    def save_note_to_json(self):
        dict_to = [note_class.Note.note_json_format(note) for note in self.notebook]
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(dict_to, file, indent=3)

