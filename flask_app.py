from flask import Flask, request, make_response, abort, jsonify
import json


app = Flask(__name__)


books = [
    {
        "id": 1,
        "title": "Flask Web Development",
        "description": "Development Web application with python",
        "author": "Miguel Grinberg",
    },
    {
        "id": 2,
        "title": "Starting out with python",
        "description": "Programming principles on python",
        "author": "Tony Gaddis",
    },
]


@app.route("/")
def index():
    return "Testing Flask"


# getting data- to get all books
@app.route("/bookapi/books")
def get_books():
    return jsonify({"Books": books})


# getting books by id
@app.route("/bookapi/books/<book_id>")
def get_by_id():
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({"books": books[0]})


# working with errors:
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "not found"}), 404)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({"error": "Bad request"}), 400)


if __name__ == "__main__":
    app.run(debug=True)
