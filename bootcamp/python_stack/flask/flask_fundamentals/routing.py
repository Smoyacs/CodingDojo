from flask import Flask

app = Flask(__name__) # Nueva instancia

@app.route('/') # Inicio de ruta despues de localhost
def hello_world():
    return f'Hola mundo'

@app.route('/dojo')
def dojo():
    return f'Dojo!'

@app.route('/say/<name>')
def hello_person(name):
    return f'Hola {name}'

@app.route('/repeat/<num>/<word>')
def repeat_word(num,word):
    return f'{int(num)*word}'

@app.route('/user/<id>/<int:user_id>')
def show_profile_info(id,user_id):
    return f'{id*user_id}'

if __name__=="__main__":
    app.run(debug=True)