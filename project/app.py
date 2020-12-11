'''Modulo para correr el webserver con Flask'''
from flask import Flask,render_template, request
import os
from converter import converter as fhtml

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if request.files:
            #devuelve una lista de objetos con cada file subido
            files = request.files.getlist('files[]')
            for f in files:
                #guardo cada file de la lista en la carpeta uploads
                f.save(os.path.join("uploads", f.filename))

    return render_template("index.html", message="Los archivos se cargaron con exito")

@app.route('/files')
def files_view():
    fname = fhtml()
    return render_template("files.html", fname=fname)

@app.route('/files', methods=['POST','GET'])
def visualizar():
    if request.method == "POST":
        for i in fhtml():
            if i[:-5] == request.form.get('slct'):
                #Retorno el texto plano html segun la opcion seleccionada
                return fhtml()[i]


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
