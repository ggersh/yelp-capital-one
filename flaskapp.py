from flask import Flask, render_template, request, url_for, redirect, flash,  g, current_app
import requests
import json
from fusionAPI import query_api
from tester import findTimeTest, convertDistToMiles

# pagination extension since yelp api doesn't directly offer pagination
from flask_paginate import Pagination, get_page_args


app = Flask(__name__)
cache = {}

# @ signifies a decorator
@app.route('/')
def index():
    return render_template("main.html")

@app.route('/search', methods=['GET','POST'])
def my_form_post():
    search = False
    PER_PAGE = 10

    if request.method == 'POST':
        print('***in form***')
        term = request.form['term']
        location = request.form['location']
        price = request.form['price']
        open_now = request.form['open']
        time = request.form['time']
    	# print(term, location, price, open_now)
        result = query_api(term=term, location=location,price=price,open_now=open_now)
        run_times = findTimeTest(time = time, data = result)
        miles = convertDistToMiles(data = result)
        if not result:
    		result = []
    	# cache this result so we can paginate through it
        cache['searches'] = result
        cache['location'] = location
        cache['term'] = term
        cache['run_times'] = run_times
        cache['miles'] = miles
    if 'searches' not in cache:
    	# user reloads search page
    	return redirect(url_for('index'))
    page = request.args.get('page', type=int, default=1)
    start_index = (page-1) * PER_PAGE
    end_index = start_index + PER_PAGE
    page_data = cache['searches'][start_index:end_index]
    location = cache['location']
    term = cache['term']
    run_times = cache['run_times'][start_index:end_index]
    miles = cache['miles'][start_index:end_index]
    pagination = Pagination(css_framework='bootstrap3', page=page, per_page=PER_PAGE, total=len(cache['searches']), search=search, record_name='searches')
    return render_template('results.html', location = location, term = term, data=page_data, pagination=pagination, run_times=run_times, miles=miles)

	# print(json.dumps(searches, sort_keys = False, indent = 2))

def get_css_framework():
    return current_app.config.get('CSS_FRAMEWORK', 'bootstrap3')


if __name__ == "__main__":
    app.run(debug=True, , port=33507)
