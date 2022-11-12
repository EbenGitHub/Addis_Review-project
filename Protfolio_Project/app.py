from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Restaurant_page_test.html")

@app.route('/login')
def login():
    return redirect("/signup", code=301)

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
