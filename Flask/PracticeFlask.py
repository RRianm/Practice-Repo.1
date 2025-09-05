#from flask import Flask

#app = Flask(__name__)

#@app.route("/greeting1")
#def test():
   # return "Hello!"

#if __name__ == "__main__":
   # app.run(debug=True)



#_____________________________________________________
from flask import Flask
app = Flask(__name__)
@app.route("/yes")
def imuststop():
    return "sweden will beat slovakia 3-1 or will draw 2-2 but not lose"


if __name__ == "__main__":
    app.run()

