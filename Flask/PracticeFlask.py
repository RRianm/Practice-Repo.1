#from flask import Flask

#app = Flask(__name__)

#@app.route("/greeting1")
#def test():
   # return "Hello!"

#if __name__ == "__main__":
   # app.run(debug=True)



#______________________________________________________

from flask import Flask,jsonify

app = Flask(__name__)
def farewell():
    return "Bye!"

if __name__ == "__main__":
    app.run()