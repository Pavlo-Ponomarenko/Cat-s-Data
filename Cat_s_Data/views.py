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
    our_request = request.form['Input_id'].strip()
    if our_request in data:
        return render_template('index.html', title='Cat\'s Data', x=data[our_request], id_into=our_request)
    return render_template('index.html', title='Cat\'s Data', message="Данных не обнаружено")

@app.route('/data_add', methods=['POST'])
def data_adding():
    file = open('data.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    our_request = request.form['Input_id']
    if our_request != "" and not (' ' in list(our_request.strip())):
        data[our_request] = request.form["TextArea"]
        file = open('data.pkl', 'wb')
        pickle.dump(data, file)
        file.close()
        return ('', 204)
    else:
        return render_template('index.html', title='Cat\'s Data', message="Не корректное id")