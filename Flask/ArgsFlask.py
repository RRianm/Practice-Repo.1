from flask import Flask,request


app = Flask(__name__)

@app.route("/test")

def run():
    name = request.args.get("name", "guest")
    return f"<h2> Hello {name}, Welcome to my website! </h2>"

if __name__ == "__main__":
    app.run(debug = True)