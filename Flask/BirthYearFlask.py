from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
@app.route('/year')

def findyear():
    
    birthyear = request.args.get('year',type = int)
    if birthyear == None:
        return "please enter your birth year."
    else:
        currentyear = datetime.now().year
        age = currentyear - birthyear
        return f"You are currently {age} years old"
    
if __name__ == "__main__":
    app.run(debug = True)
    

