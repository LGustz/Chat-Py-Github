
import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "chave-local-de-desenvolvimento"
)

socketio = SocketIO(app, async_mode="threading")


@app.route("/")
def inicio():
    return render_template("index.html")


@socketio.on("mensagem")
def receber_mensagem(dados):
    if not isinstance(dados, dict):
        return

    nome = str(dados.get("nome", ""))
    texto = str(dados.get("texto", ""))

    nome = nome.strip()[:30]
    texto = texto.strip()[:500]

    if not nome or not texto:
        return

    socketio.emit("mensagem", {
        "nome": nome,
        "texto": texto
    })


@socketio.on("connect")
def conectar():
    print(f"Cliente conectado: {request.sid}")


if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
