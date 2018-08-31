
from flask import Flask,jsonify,request,render_template
from web import *
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

'''class Formulario(FlaskForm):
    url= StringField("URL",validators=[DataRequired()])
    palavra=StringField("Palavra",validators=[DataRequired()])
    submit = SubmitField('Sign In')'''
#Classe para o formulario de URL
app = Flask(__name__)
@app.route('/')
def index():
    conta = contapalavrasite(['https://pt.wikipedia.org/wiki/Ci%C3%AAncia_da_computa%C3%A7%C3%A3o'],'computador')
    return jsonify(Palavra=conta.conta_palavra())




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
