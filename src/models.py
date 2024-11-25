from datetime import datetime
import json
from src import db


class BookModel(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    subtitle = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    published = db.Column(db.DateTime, default=datetime.now)
    publisher = db.Column(db.String(50), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    website = db.Column(db.String(50), nullable=False)
    
    
    def json(self):
        return {"id":self.id, 
                "isbn":self.isbn,
                "title":self.title,
                "subtitle":self.subtitle,
                "author":self.author,
                "published":self.published,
                "publisher":self.publisher,
                "pages":self.pages,
                "description": self.description,
                "website":self.website}
    