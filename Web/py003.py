from flask import Flask, render_template, request, redirect
from alunos import Alunos

pagina_nome='Lista Alunos'
aluno1 = Alunos('Cristiane', 'Ortiz', 47999480775)
aluno2 = Alunos('Junior', 'Sousa', 47966884475)
# aluno3 = Alunos('Luis', 'Eduardo', 47996131242)
# aluno4 = Alunos('Maria', 'Silva', 47996565588)
# aluno5 = Alunos('João', 'Silva', 47993554477)
lista_alunos = [aluno1, aluno2]
# aluno3, aluno4, aluno5]
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome=pagina_nome, lista=lista_alunos)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/salvar', methods=['POST']) 
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    novo_aluno = Alunos(nome, sobrenome, telefone)
    lista_alunos.append(novo_aluno)
    return redirect('/')

app.run()