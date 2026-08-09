from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about-me')
def about_me():
    return render_template("about-me.html")

if __name__ == "__main__":
    app.run(debug=False)