from flask import Flask, render_template, request
import calc as CALC

app = Flask('app')

@app.route('/')
def home():
  #CALC.read_all()
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

@app.route('/read_all')
def read_all():

  read_db = CALC.read_all()

  lista_paciente = []
  for cont in range(0, len(read_db['ID'])):
    print(read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont])
    lista_paciente.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])
  
  return render_template('paciente.html', lista_paciente=lista_paciente)


app.run(host='0.0.0.0', port='5000', debug=True)





