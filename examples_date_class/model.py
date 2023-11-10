from datetime import datetime
import note_class
import json
import os

notebook = []
path_json = 'notes.json'
note_id = -1
note = None


def add_contact():
    global notebook
    global note
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_note = len(notebook) + 1
    title = input('Введите тему заметки: ')
    content = input('Введите тект заметки: ')
    note = note_class.Note(id_note, title, content, timestamp)
    notebook.append(note)
    print_notes()


def print_notes():
    global notebook
    for notes in notebook:
        print(notes)
        print(notes[id])
        #print(f"ID: {note.id}, Title: {note.title}, Timestamp: {note.timestamp}")
    if not notebook:
        print("No notes found.")

def start():
    global notebook
    global note
    global note_id
    notes = []
    if os.path.exists(path_json):
        with open(path_json, 'r', encoding='UTF-8') as file:
            notebook = json.load(file)
            # for line in file:
                # if line.strip():
            # data = json.loads(file)
            # notes.append(data)

        # for item in notebook:
        #     note = note_class.Note(item.id, item['title'],
        #                            item['content'], item['timestamp'])
        #     notebook.append(note)
    else:
        note_id = 0



start()