from app import app, db
from app.models.usuarios import Usuario
from flask import render_template, request

@app.route('/cadastrar')
def cadastrar_usuario():
    usuario = Usuario(username='leosilva', email='leo@leo.com')
    db.session.add(usuario)
    db.session.commit()
    return 'Usuário cadastrado com sucesso!'

@app.route('/inserir', methods=['GET', 'POST'])
def inserir_novo_usuario():
    if request.method == 'POST':
        nome = request.form['username']
        email_user = request.form['email']
        senha_user = request.form['senha']

        usuario = Usuario(username=nome, email=email_user, senha=senha_user)
        db.session.add(usuario)
        db.session.commit()

    return render_template('index.html')