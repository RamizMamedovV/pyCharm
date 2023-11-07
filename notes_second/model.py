import os
import json
import note

my_path = 'my_notes.json'
my_notes = []


def start():
    global my_notes
    if os.path.exists(my_path):
        with open(my_path, 'r', encoding='UTF-8') as file:
            my_notes = json.load(file)


def get_notes():
    return my_notes


def get_notes_length():
    return len(my_notes)


def edit_note(note_id: int, title: str, content: str):
    global my_notes
    for notes in my_notes:
        if note_id == notes['note_id']:
            notes['title'] = title
            notes['content'] = content


def delete_note(note_id: int) -> bool:
    global my_notes
    my_notes.remove(my_notes[note_id - 1])
    return True


def add_new_node(temp: dict):
    global my_notes
    my_notes.append(temp)
