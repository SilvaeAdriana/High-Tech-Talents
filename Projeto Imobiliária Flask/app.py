from flask import Flask,abort, redirect, render_template, url_for, request, flash,Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/aluguel'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Imovel(db.Model):
   __tablename__ = 'imovel'
   id = db.Column(db.Integer,autoincrement=True, primary_key = True)
   logradouro = db.Column(db.String(), nullable = False)
   cep = db.Column(db.Integer(), nullable = False)
   bairro = db.Column(db.String(), nullable = False) 
   cidade = db.Column(db.String(), nullable = False)
   proprietario_id = db.Column(db.Integer, db.ForeignKey('proprietario.id'))

   def __init__(self, logradouro, cep, bairro,cidade):
    #self.id = id
    self.logradouro = logradouro
    self.cep = cep
    self.bairro = bairro
    self.cidade = cidade
   
   def __repr__(self):
    return f'<Dados do imóvel: id {self.id}, logradouro {self.logradouro}, cep {self.cep}, bairro {self.bairro}, cidade {self.bairro}>'


class Inquilino(db.Model):
   __tablename__ = 'inquilino'
   id = db.Column(db.Integer,autoincrement=True, primary_key = True)
   nome = db.Column(db.String(), nullable = False)
   endereco = db.Column(db.String(), nullable = False)
   data_nascimento = db.Column(db.DateTime(), nullable = False)
   genero = db.Column(db.String(), nullable = False)
   documento = db.Column(db.String(), nullable = False)
   iddocumento = db.Column(db.Integer(), nullable = False)
   aluguel = db.relationship('Aluguel', back_populates='inquilino') 
  

   def __init__(self, nome, endereco, data_nascimento, genero, documento, iddocumento):
      self.nome = nome
      self.endereco = endereco
      self.data_nascimento = data_nascimento
      self.genero = genero
      self.documento = documento
      self.iddocumento = iddocumento

   def __repr__(self):  
      return f"<Dados dos Proprietário: id {self.id}, nome {self.nome}, endereço {self.endereco}, data de nascimento {self.data_nascimento}, gênero {self.genero}, documento {self.docuemnto}, id do documento {self.iddocumento}>" 


class Proprietario(db.Model):
   __tablename__ = 'proprietario'
   id = db.Column(db.Integer, autoincrement=True, primary_key = True)
   nome = db.Column(db.String(), nullable = False)
   endereco = db.Column(db.String(), nullable = False)
   data_nascimento = db.Column(db.DateTime(), nullable = False)
   genero = db.Column(db.String(), nullable = False)
   documento = db.Column(db.String(), nullable = False)
   iddocumento = db.Column(db.Integer(), nullable = False)
   imovel = db.relationship('Imovel', back_populates='proprietario')  

   def __init__(self, nome, endereco, data_nascimento, genero, documento, iddocumento):
      #self.id =id
      self.nome = nome
      self.endereco = endereco
      self.data_nascimento = data_nascimento
      self.genero = genero
      self.documento = documento
      self.iddocumento = iddocumento


   def __repr__(self):  
      return f"<Dados dos Proprietário: id {self.id}, nome {self.nome}, endereço {self.endereco}, data de nascimento {self.data_nascimento}, gênero {self.genero}, documento {self.docuemnto}, id do documento {self.iddocumento}>" 


class Aluguel(db.Model):
   __tablename__ = 'aluguel'
   id = db.Column(db.Integer,autoincrement=True, primary_key = True)
   valor = db.Column(db.Integer(), nullable = False)
   imovel_id = db.Column(db.Integer, db.ForeignKey('imovel.id'))
   inquilino_id = db.Column(db.Integer, db.ForeignKey('inquilino.id'))


   def __init__(self,valor):
      #self.id = id
      self.valor = valor

   def __repr__(self):
      return f' <Dados do aluguel: id {self.id}, valor{self.valor}, id do imóvel{self.imovel_id},id do inquilino{self.inquilino_id}>'
      
   


# APRESENTA A TELA INICIAL DA API
@app.route('/') 
@app.route('/index')
def index(): 
   return render_template('index.html')


#return 'Aqui estão nossos contatos'
@app.route('/contatos')
def contatos():
   return render_template('contatos.html')
   

# retorna o formulário de login
@app.route('/login')
def login():
   return render_template('login.html')


# exibe a mensagem de usuário logado com sucesso se preenchidos usuário e sem (ainda sem validação)
@app.route('/login', methods =['POST'])  
def opcoes():
   if request.method == 'POST':
      if request.form['username'] != '' and request.form['password'] != '':
         return redirect(url_for('sucesso'))
      else:
         # abort(401)-abort não aceita mensagem inserida pelo programador/strings
         return '<h1> Usuário não autorizado. Realize seu cadastro ou refaça seu login! </h1>'  #renderiza diretamente no browser,não retorna pag html -->página sem configurações css etc
   else:
      return redirect(url_for('index'))


@app.route('/sucesso')
def sucesso():
   return render_template('sucesso.html') # posso retornar uma msg (sem configurações,mas mais rápida) ou retornar um template/mais bonito


@app.route("/inquilino/<int:id>", methods=["DELETE"])
def deleta_inquilino(id):
   inquilino =Inquilino.query.filterBy(id=id).first()
   db.session.delete(inquilino)
   db.session.commit()
   inquilino =Inquilino.query.all()
   return render_template('lista_inquilino.html', inquilino=inquilino)





if __name__ == '__main__':
   app.run(debug = True)
   db.create_all()  