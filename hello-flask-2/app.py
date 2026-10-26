from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/hello")
def api_hello():
    return jsonify({"mensagem": "Olá Flask2! Recebi a requisição"})


if __name__ == "__main__":
    app.run(debug=True)