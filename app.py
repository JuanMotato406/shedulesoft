from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "hello world"

if __name__ == "__main__":
	app.run(debug=True)

@app.route('/login')
def login():
        return render_template('inicio.html')

@app.route('/validarlogin', methods=['POST'])
def validarlogin():
    if request.method == "POST":
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']
        conexion = mysql.connection.cursor()
        conexion.execute("SELECT * FROM   usuarios")
        data = conexion.fetchall()

        contador = 0
        for linea in data:
                usuario = linea[3]
                password = linea[4]

                if nombre_usuario == usuario and contrasena == password:
                        contador = 1
                        break

        if contador == 1:
                print ("Login correcto")
                contador = 0
                return redirect(url_for('home'))

        else:
                print ("Usuario o Contraseña Incorrectos")
                return redirect(url_for('login'))

        conexion.close()
        return render_template('index.html')
