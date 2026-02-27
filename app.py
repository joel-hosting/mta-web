from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>MTA Server</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
            }
            h1 {
                margin-top: 40px;
                font-size: 50px;
                color: #00ffff;
                text-shadow: 0 0 15px #00ffff;
            }
            .card {
                background: #111;
                width: 350px;
                margin: 30px auto;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 0 20px #00ffff;
            }
            .btn {
                display: inline-block;
                margin-top: 15px;
                padding: 12px 25px;
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
            <a class="btn" href="mtasa://45.32.172.17:7117">Entrar al servidor</a>
        </div>

        <div class="card">
            <h2>💬 Comunidad</h2>
            <p>Únete a nuestro Discord</p>
            <a class="btn" href="#">Entrar al Discord</a>
        </div>

        <div class="card">
            <h2>💎 Beneficios VIP</h2>
            <p>Obtén autos exclusivos, dinero y ventajas únicas.</p>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
