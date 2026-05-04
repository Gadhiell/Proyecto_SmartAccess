from flask import Blueprint, request, jsonify
from services.auth_service import validar_acceso
from data.memory_db import usuarios, logs

api = Blueprint("api", __name__)


@api.route("/acceso", methods=["POST"])
def acceso():
    data = request.json

    usuario_id = data.get("usuario_id")
    metodo = data.get("metodo")

    permitido, estado = validar_acceso(usuario_id, usuarios)

    log = {
        "usuario_id": usuario_id,
        "metodo": metodo,
        "estado": estado
    }

    logs.append(log)

    return jsonify(log)


@api.route("/logs", methods=["GET"])
def obtener_logs():
    return jsonify(logs)