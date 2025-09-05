


# from flask import Flask, request, render_template_string
# app = Flask(__name__)

# Html = '''
# <h2> feedback form </h2>
# <form method="POST"> 
# name: <input type="text" name="name" required><br><br>
# feedback: <br>
# <textarea name="feedback" row="100" cols="40" required></textarea><br><br>

# <button type="sumbit">
# Sumbit
# </button>

# </form>

# '''

# @app.route("/feedback", methods = ["GET", "POST"])

# def feedback():
#     if request.method == "POST":
#         name = request.form.get("name")
#         feedback = request.form.get("feedback")
#         return f"Thank you {name}. We will work on : {feedback}"
#     else:
#         return render_template_string(Html)

# if __name__ == "__main__":
#     app.run(debug = True)













from flask import Flask, request, render_template_string

app = Flask(__name__)

html = '''
<h2>Log in Page</h2>
<form method="POST">
    Username: <input type="text" name="name" required><br><br>
    Password: <input type="password" name="key" required><br><br>
    <button>Log in</button>
</form>
<p>{{ message }}</p>
'''

@app.route("/login", methods=["GET", "POST"])
def loginpage():
    message = ''
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("key")
        if username and password:
            message = f"Welcome {username}"
        else:
            message = "Please enter correct username or password"
    
    # Always return the rendered template, with message
    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run(debug=True)