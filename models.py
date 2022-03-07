from app import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published

    def __repr__(self):
        return f'<id {self.id}>'

    def serialize(self):            # this method will be used to get back response in json format
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'published': self.published
        }
