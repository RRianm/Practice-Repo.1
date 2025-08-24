from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {"id": 1, "name": "Rian", "page_nr": 516},
    {"id": 2, "name": "Mansi", "page_nr": 301}
]
@app.route('/books', methods = ["GET"])

def sendbooks():
    return jsonify(books)

@app.route('/books', methods = ["POST"])  

def addbook():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book),201




if __name__ == '__main__':
    app.run()
