import json
import os
import note_class
from datetime import datetime as date


class Notebook:

    def __init__(self, data_file: str):
        self.data_file = data_file
        self.notebook = []
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as file:
                self.notebook = json.load(file)

    def print_list(self):
        for note in self.notebook:
            print(note_class.Note.note_json_format(note))

    def print_search_note(self, note_id: int):
        for note in self.notebook:
            if note_id == note_class.Note.get_note_id(note):
                return note_class.Note.note_json_format(note)

    def print_search_format(self):
        for note in self.notebook:
            print(note_class.Note.search_format(note))

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
                return True
            else:
                return False
