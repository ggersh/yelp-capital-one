from flask import Flask, render_template, request, url_for, redirect, flash
import requests
from capSumm import query_api

app = Flask(__name__)

# @ signifies a decorator
@app.route('/')
def index():
    return render_template("main.html")

@app.route('/', methods=['POST'])
def my_form_post():
	print('***in form***')
	term = request.form['term']
	location = request.form['location']
	price = request.form['price']
	open_now = request.form['open']
	print(term, location, price, open_now)
	searches = query_api(term=term, location=location,price=price,open_now=open_now)
	return render_template('results.html', location = location, data=searches)


if __name__ == "__main__":
    app.run(debug=True)
