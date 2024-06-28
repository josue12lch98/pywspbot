from flask import Flask, request, jsonify, render_template

from app import recibir_mensaje
from dbQuery import UserState


def init_app(app):
    @app.route('/')
    def index():
        # Obtener todos los registros de la base de datos
        registros = UserState.query.all()
        registros_ordenados = ordenar_por_fecha_y_hora(registros)
        return render_template('index.html', registros=registros_ordenados);

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        challenge = verificar_token(request)
        return challenge
    elif request.method == 'POST':
        response = recibir_mensaje(request)
        return response
def verificar_token(req):
    token = req.args.get('hub.verify_token')
    challenge = req.args.get('hub.challenge')
    if challenge and token == TOKEN:
        return challenge
    else:
        return jsonify({'error': 'Token Invalido'}), 401

