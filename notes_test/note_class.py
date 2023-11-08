from datetime import datetime as rec
"""Заметка должна
содержать идентификатор, заголовок,
тело заметки и дату/время создания или
последнего изменения заметки. """


class Note:

    def __init__(self, note_id: int, title: str,
                 content: str, rec_time: str):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.rec_time = rec_time

    def note_json_format(self):
        return {
            'note_id': {self.note_id},
            'title': {self.title},
            'content': {self.content},
            'date': {self.rec_time}
        }

    def search_format(self):
        return {
            'note_id': {self.note_id},
            'title': {self.title}
        }

    def get_note_id(self):
        return self.note_id

    def set_note_title(self, title: str):
        self.title = title

    def set_note_content(self, content: str):
        self.content = content
