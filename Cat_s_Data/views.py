"""
Routes and views for the flask application.
"""
import pickle
from flask import render_template, request
from Cat_s_Data import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Cat\'s Data')

@app.route('/data_rec', methods=['POST'])
def data_getting():
    file = open('data.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    our_request = request.form['Input_id']
    if our_request in data:
        return render_template('index.html', title='Cat\'s Data', x=data[our_request])
    return render_template('index.html', title='Cat\'s Data', message="Данных не обнаружено")
    