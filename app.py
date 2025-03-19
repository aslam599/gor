from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Harry Potter dan Batu Bertuah", "author": "J.K. Rowling"},
    {"id": 2, "title": "Laskar Pelangi", "author": "Andrea Hirata"},
    {"id": 3, "title": "Negeri 5 Menara", "author": "Ahmad Fuadi"},
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Buku tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)