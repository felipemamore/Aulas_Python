from flask import Flask, render_template, request, redirect
import sys
sys.path.append('/Felipe/15-01-19/AulasPython/37-Aula37')
from Controller.squad_controller import SquadController


from Model.squad import Squad

app = Flask(__name__)
squad_controller = SquadController()

nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    
    squad_controller.deletar(id)
    
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    dic = request.args.to_dict()
    #print('*\n'*10,type(dic))
    squad.criar(**dic)
    #print('**\n'*10,squad,'**\n'*10)
    
    

   
    if squad.id == '0':
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

app.run(debug=True)