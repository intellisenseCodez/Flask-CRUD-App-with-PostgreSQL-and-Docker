import uuid
from flask import make_response, jsonify, request
from src import app, db
from src.books.models import BookModel

@app.route("/")
def test():
    return "<h1>Welcome to my Flask Crud APP.</h1>"


# Display all books
@app.route("/books", methods=["GET"])
def get_all_books():
    try:
        books = BookModel.query.all()
        return make_response(jsonify([book.json() for book in books]), 200)
    except Exception as e :
        print(f"Error getting books: {e}")
        return make_response(jsonify({"message":"error getting books"}), 500)
    
    
# Create a book
@app.route("/books/create", methods=["POST"])
def create_book():
    try:
        data = request.get_json()
        title = data.get('title')
        page_count = data.get("page_count")
        author = data.get('author')
        
        if not title or not page_count or not author:
            return jsonify({"error": "All fields (title, page_count, author) are required"}), 400

        
        new_book = BookModel(title=title, page_count=page_count, author=author)
        db.session.add(new_book)
        db.session.commit()
        return make_response(new_book.json(),201)
    except Exception as e :
        print(f"Error creating book: {e}")
        return make_response(jsonify({"message":"error creating books"}), 500)
    
    
# Get specific book
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    try:
        book = BookModel.query.get(book_id)
        if book:
            return make_response(book.json(),200)
        return make_response(jsonify({"message":"book not found"}), 404)
    except Exception as e :
        print(f"Error creating book: {e}")
        return make_response(jsonify({"message":"error creating books"}), 500)
     
     
     
# update specific book
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        book = BookModel.query.get(book_id)
        print(book.json())
        if book:
            data = request.get_json()
            print(data)
            book.title = data.get("title", book.title)
            book.page_count = data.get("page_count", book.page_count)
            book.author = data.get("author", book.author)
            db.session.commit()
            return make_response(book.json(),200)
        return make_response({"message":"book not found"}), 404
    except Exception as e :
        print(f"Error creating book: {e}")
        return make_response(jsonify({"message":"error creating books"}), 500)
    
# delete specific book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        book = BookModel.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return make_response(jsonify({"message":"Book successfully deleted"}), 200)
        return make_response(jsonify({"message":"book not found"}), 404)
    except Exception as e :
        print(f"Error creating book: {e}")
        return make_response(jsonify({"message":"error creating books"}), 500)