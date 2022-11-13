from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/restaurants')
def restaurants():
    return render_template("Restaurant_page_test.html")

@app.route('/login')
def login():
    return redirect("/signup", code=301)

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/foods')
def foods():
    return render_template("Food_Page_test.html")

@app.route('/reviews')
def reviews():
    return render_template("review.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
