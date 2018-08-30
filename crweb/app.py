# app.py
from flask import Flask,jsonify
from web import *
app = Flask(__name__)
@app.route('/')
def index():
    Produtos = contapalavrasite('https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test,palavra','abada')
    return  jsonify(Produtos.conta_palavra())
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
