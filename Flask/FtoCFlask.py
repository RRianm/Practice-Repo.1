"""
from flask import Flask, request
app = Flask(__name__)
@app.route('/subject')

def favsubject():
    subject = request.args.get('subject')
    if subject == None:
        return "Enter your favorite subject please!"
    else:
        return f"your favorite subject is {subject}!"
    
if __name__ == "__main__":
    app.run(debug = True)
"""

from flask import Flask, request 
app = Flask(__name__)
@app.route("/CtoF")

def celtofar():
    Celsius = request.args.get("Celsius", type = float)
    if Celsius == None:
        return "Please enter your Celsius value!"
    else : 
        fahrenheit = (Celsius * 9/5) + 32
        return f"<h1>{Celsius} degree celsius is equal to {fahrenheit} degree fahrenheit!</h1>"
    
if __name__ == "__main__":
    app.run(debug = True)
