from flask import Flask, render_template


#create flask instance
app = Flask(__name__)


#Create route decorator
@app.route('/')

def index():
	first_name = "Trev"

	stuff = "This is <strong>bold</strong> text"

	favourite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]

	return render_template("index.html", first_name=first_name, stuff=stuff,favourite_pizza=favourite_pizza)

#localhost:5000/user/trevor
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)

#Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500	
