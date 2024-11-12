import json
from src import db


class BookModel(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    page_count = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(150), nullable=False)
    
    def json(self):
        return {"id":self.id, 
                "title":self.title,
                "page_count":self.page_count,
                "author": self.author}
    