from flask import Flask, render_template  # Importar Flask para que permita crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente

def hello_world():
    return 'Hello World!'  # Retorna la cadena 'Hello World!' como respuesta


@app.route('/list')
def render_lists():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("list.html", random_numbers = [3,1,5], students = student_info)


if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depurac