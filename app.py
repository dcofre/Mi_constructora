from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    empresa = {
        "nombre": "Samurai",
        "especializacion": "Construcción",
        "servicios": "Próximamente",
        "publico": "Próximamente",
        "ubicacion": "Miami",
        "valores": "Próximamente",
        "estilo": "Moderno"
    }
    return render_template("index.html", empresa=empresa)

if __name__ == '__main__':
    app.run(debug=True)