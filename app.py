from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>BLOKE TRANZA RP</title>
        <style>
            body {
                background: #0f0f0f;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 40px;
            }
            .card {
                background: #1c1c1c;
                padding: 20px;
                margin: 20px auto;
                width: 300px;
                border-radius: 10px;
                box-shadow: 0 0 10px #00ffff;
            }
            .btn {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 20px;
                background: #00ffff;
                color: black;
                font-weight: bold;
                text-decoration: none;
                border-radius: 8px;
            }
            .btn:hover {
                background: #00cccc;
            }
        </style>
    </head>
    <body>

        <h1>🔥 BLOKE TRANZA RP 🔥</h1>
        <p>El mejor servidor Roleplay de MTA</p>

        <div class="card">
            <h2>🌐 Conéctate</h2>
            <p>IP: 45.32.172.17:7117</p>
            <a class="btn" href="#">Entrar al servidor</a>
        </div>

        <div class="card">
            <h2>💬 Comunidad</h2>
            <p>Únete a nuestro Discord</p>
            <a class="btn" href="#">Entrar al Discord</a>
        </div>

        <div class="card">
            <h2>💎 Beneficios VIP</h2>
            <p>Obtén autos exclusivos y ventajas especiales</p>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
