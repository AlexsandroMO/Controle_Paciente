from flask import Flask, render_template, request
import calc as CALC

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/add_')
def add_():
  return render_template('cadastrar.html')

@app.route('/add_create', methods=['POST', 'GET'])
def add_create():
  if request.method == 'POST':
    result = request.form
    name = result['name-paciente']
    age = result['age-paciente']
    gen = result['gen-paciente']
    cpf = result['cpf-paciente']
    p_pac = result['p-paciente']
    a_pac = result['a-paciente']

    CALC.create_data(name,age, gen, cpf, p_pac, a_pac)
    msg = 'Registrado!'
  
  return render_template('home.html', msg=msg)



#app.run(host='0.0.0.0', port=8080, debug=True)
app.run(host='0.0.0.0', port='5000', debug=True)





'''@app.route('/banco')
def banco():
  CALC.create_db()
  msg = 'Banco Criado!'
  return render_template('home.html', msg=msg)

CRUD

'''

