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

@app.route('/data_f', methods=['GET'])
def data_getting():
    file = open('data.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    our_request = request.args['Input_id'].strip()
    if our_request in data:
        return render_template('index.html', title='Cat\'s Data',
                               id_into=our_request,
                               name=data[our_request][0],
                               gender=data[our_request][1],
                               age=data[our_request][2],
                               breed=data[our_request][3],
                               color=data[our_request][4],
                               toy=data[our_request][5])
    return render_template('index.html', title='Cat\'s Data', message="Данных не обнаружено", id_into=our_request)

@app.route('/data', methods=['POST'])
def data_adding():
    file = open('data.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    our_request = request.form['Input_id']
    if our_request != "" and not (' ' in list(our_request.strip())):
        req_list = [request.form["Name"],
                    request.form["Gender"],
                    request.form["Age"],
                    request.form["Breed"],
                    request.form["Color"],
                    request.form["Toy"]]
        data[our_request] = req_list
        file = open('data.pkl', 'wb')
        pickle.dump(data, file)
        file.close()
        return ('', 204)
    else:
        return render_template('index.html', title='Cat\'s Data', message="Не корректное id")

@app.route('/data_d', methods=['GET'])
def data_del():
    file = open('data.pkl', 'rb')
    data = pickle.load(file)
    file.close()
    our_request = request.args['Input_id'].strip()
    if our_request in data:
        del data[our_request]
        file = open('data.pkl', 'wb')
        pickle.dump(data, file)
        file.close()
        return render_template('index.html', title='Cat\'s Data', message="Запись удалена")
    else:
        return render_template('index.html', title='Cat\'s Data', message="Не корректное id")
