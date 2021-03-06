from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/students'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class estudante(db.Model):
    __tablename__ = 'estudante'
    id = db.Column('estudante_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200)) 
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

class curso(db.Model):
    __tablename__ = 'curso'
    id = db.Column('curso_id', db.Integer, primary_key = True)
    id_aula = db.Column('aula_id', db.Integer)
    id_aluno = db.Column('aluno_id', db.Integer)
    
    def __init__(self, name):
        self.name = name
    
class aula(db.Model):
    __tablename__ = 'aula'
    id = db.Column('aula_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    
    def __init__(self, name):
        self.name = name
    



@app.route('/')
def show_all():
   return render_template('show_all.html', students = estudante.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = estudante(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)