from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

#"Base de datos"
logs = []

usuarios = {
    1: {"nombre": "Juan", "activo": True},
    2: {"nombre": "Maria", "activo": False},
}


#Validaciones
def validar_acceso(usuario_id):
    usuario = usuarios.get(usuario_id)

    if not usuario:
        return False, "inactivo"

    if not usuario["activo"]:
        return False, "inactivo"

    return True, "activo"


#Rutas para la pagina
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route('/logo.png')
def logo():
    return send_from_directory(".", "logo.png")

@app.route('/Wordmark.png')
def Wordmark():
    return send_from_directory(".", "Wordmark.png")

@app.route("/panel")
def panel():
    return send_from_directory(".", "panel.html")



#Simular acceso
@app.route("/acceso", methods=["POST"])
def acceso():
    data = request.json

    usuario_id = data.get("usuario_id")
    metodo = data.get("metodo")

    permitido, estado = validar_acceso(usuario_id)

    log = {
        "usuario_id": usuario_id,
        "metodo": metodo,
        "estado": estado
    }

    logs.append(log)

    return jsonify(log)


#funcion para los logs
@app.route("/logs", methods=["GET"])
def obtener_logs():
    return jsonify(logs)


if __name__ == "__main__":
    app.run(debug=True)