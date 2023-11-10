class Note:
    def __init__(self, identity, title, context, rec_time):
        self.identity = identity
        self.title = title
        self.context = context
        self.rec_time = rec_time

    def to_dict(self):
        return {
            'id': self.identity,
            'title': self.title,
            'content': self.context,
            'timestamp': self.rec_time
        }
