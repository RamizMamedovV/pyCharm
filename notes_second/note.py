

class Note:
    def __init__(self, note_id: int, title: str, content: int):
        self.note_id = note_id
        self.title = title
        self.content = content

    def format(self):
        return {
            'id': self.note_id,
            'title': self.title,
            'content': self.content,
            #'timestamp': self.rec_time
        }

