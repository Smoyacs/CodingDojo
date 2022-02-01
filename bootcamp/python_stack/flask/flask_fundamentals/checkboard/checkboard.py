from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkboard_default():
    return render_template("index.html",filas=8,columnas=8)

@app.route('/<int:rows>/<int:col>')
def checkboard(rows,col):
    print(rows,col)
    return render_template("index.html",filas=rows,columnas=col)
    
if __name__=="__main__":
    app.run(debug=True)
