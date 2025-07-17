from flask import Flask, render_template 

#Criação do app flask
app = Flask(__name__)

#Rota da pagina Principal 
@app.route('/')
def home():
    return "<h1> Welcome to my API <h1>"

#Rota da pagina sobre
@app.route('/sobre')
def sobre():
    return "<h1> Created by the best, Emily <h1>"

#Rota com variaveis na URL
@app.route('/Ello/<nome>')
def yo(nome):
    return f"<h1>Ello, {nome}!</h1><br/><h2>Welcome to my page gang</h2><a href='//www.google.com'>Google</a>"


#Iniciar o servidor
if __name__ == '__main__':
    app.run(debug = True)
