from flask import Flask, request, jsonify

app = Flask(__name__)

Books = [
    {"id":1, "name": "Book1", "author":"me" },
    {"id":2, "name": "Book2", "author":"ALSOme" },
    {"id":3, "name": "Book3", "author":"Someone" }
]
@app.route("/books", methods = ["GET"])
def getbooks():
    return jsonify(Books)

# @app.route("/books", methods = ["POST"])
# def postbooks():
#     newbook = {"id":len(Books)+1, "name": request.get_json["name"], "author": request.get_json["author"]}
#     Books.append(newbook)
#     return jsonify(newbook)
@app.route("/books", methods=['POST'])
def create_book():
    new_book={"id": len(Books)+1, "name":request.json['name'], "author":request.json['author']}
    Books.append(new_book)
    return Books

@app.route("/books/<int:Books_id>", methods = ["PUT"])
def editbooks(Books_id):
    for id in Books:
        if id["id"] == Books_id:
            id["name"] = request.json["name"]
            id["author"] = request.json["author"]
            return Books
    return {"Error" : "Book not found"  }
    
@app.route("/books/<int:Books_id>", methods = ["DELETE"])
def removebooks(Books_id):
    for search in Books:
         if search['id']==Books_id:
            Books.remove(search) 
            return {"data":"Deleted successsfully"}
    return {"Error: book not found"}




if __name__ == "__main__":
    app.run(debug=True)




# from flask import Flask, jsonify, request

# app=Flask(__name__)

# books=[
#     {"id":1, "title":"Book 1", "author":"Author 1"},
#     {"id":2, "title":"Book 2", "author":"Author 2"},
#     {"id":3, "title":"Book 3", "author":"Author 3"}
# ]

# #CRUD - READ (GET)

# @app.route('/books', methods=['GET'])
# def get_books():
#     return books

# # CREATE (POST)
# @app.route('/books', methods=['POST'])
# def create_book():
#     new_book={"id": len(books)+1, "title":request.json['title'], "author":request.json['author']}
#     books.append(new_book)
#     return books

# # UPDATE (PUT)
# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     for id in books:
#         if id['id']== book_id:
#             id['title']=request.json['title']
#             id['author']=request.json['author']
#             return id
#     return {'error': "BOOk not found"}

# #DELETE (DELETE)
# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     for search in books:
#         if search['id']==book_id:
#             books.remove(search)
#             return {"data":"Deleted successsfully"}
#     return {"error": "Book Not Found"}



# if __name__ == '__main__':
#     app.run(debug=True)


