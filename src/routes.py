import uuid
from flask import make_response, jsonify, request
from src import app, db
from src.models import BookModel

@app.route("/", methods=["GET"])
def test():
    return """<h1> Flask Crud APP</h1>
                <p> A flask rest api implementation using Docker Container. </p>
            """


# Display all books
@app.route("/books", methods=["GET"])
def get_all_books():
    try:
        books = BookModel.query.all()
        print(books)
        return make_response(jsonify([book.json() for book in books]), 200)
    except Exception as e :
        print(f"Error getting books: {e}")
        return make_response(jsonify({"message":"error getting books"}), 500)
    
    
# Create a book
@app.route("/books/create", methods=["POST"])
def create_book():
    try:
        data = request.get_json()
        isbn = data.get('isbn')
        title = data.get('title')
        subtitle = data.get('subtitle')
        author = data.get('author')
        publisher = data.get('publisher')
        pages = data.get('pages')
        description = data.get('description')
        website = data.get('website')
        
        if not isbn or not title or not subtitle or not author or not publisher or not pages or not description or not website:
            return make_response(jsonify({"message": "All fields (title, page_count, author) are required"}), 400)

        
        new_book = BookModel(isbn=isbn,
                             title=title,
                             subtitle=subtitle,
                             author=author,
                             publisher=publisher,
                             pages=pages,
                             description=description,
                             website=website)
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
        book = BookModel.query.get({"id":book_id})
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
        book = BookModel.query.get({"id":book_id})
        if book:
            data = request.get_json()
        
            book.title = data.get("title", book.title)
            book.isbn = data.get('isbn', book.isbn)
            book.title = data.get('title', book.title)
            book.subtitle = data.get('subtitle', book.subtitle)
            book.author = data.get('author', book.author)
            book.publisher = data.get('publisher', book.publisher)
            book.pages = data.get('pages', book.pages)
            book.description = data.get('description', book.description)
            book.website = data.get('website', book.website)
            
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
        book = BookModel.query.get({"id":book_id})
        if book:
            db.session.delete(book)
            db.session.commit()
            return make_response(jsonify({"message":"Book successfully deleted"}), 200)
        return make_response(jsonify({"message":"book not found"}), 404)
    except Exception as e :
        print(f"Error creating book: {e}")
        return make_response(jsonify({"message":"error creating books"}), 500)