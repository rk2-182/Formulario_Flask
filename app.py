from flask import Flask, render_template,request
import hashlib

#https://recursospython.com/guias-y-manuales/hashlib-md5-sha/


#Instancia del objeto
app = Flask(__name__)


@app.errorhandler(404)
def paga_not_found(e):
    return render_template('page_no_found.html'),404


#definir ruta
@app.route('/')
def index():
    return render_template('index.html')

"""POST consiste en datos "ocultos" (porque el cliente no los ve) enviados por un formulario cuyo método de envío es post. 
        Es adecuado para formularios. Los datos no son visibles.

1.-tener un formulario en html al cual se le indica que utilizara el metodo post.
2.-los input debe tener un nombre asignado para enviar los datos al metodo
3.-si el metodo es post este recibe los datos del formulario y se alamacenan en una variable
4.-los datos en variable ya pueden ser utilizado para distintos fines, ej.: enviarlos a una bd.

"""
@app.route('/formulario',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        #Valores obtenidos de los name de cada input
        email = request.form['email']
        contrasena = request.form['contrasena']

        cifrado = hashlib.sha256()

        cifrado.update(contrasena.encode('utf-8'))


        print("Email: {}".format(email))
        print("Contraseña: {}".format(cifrado.hexdigest()))

    return render_template('login.html')


#Correr servidor en modo depurador y seleccionar puerto 5000
app.run(debug=True,port=5000)
