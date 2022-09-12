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
    #print(read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont])
    lista_paciente.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])
  
  return render_template('paciente.html', lista_paciente=lista_paciente)



@app.route('/edit_pac/<page_id>')
def edite_pac(page_id):

  read_db_id = CALC.read_id(page_id)
  #edit_pac/2

  read_id = []
  for read in range(0, len(read_db_id['ID'])):
    read_id = [page_id,read_db_id['NAME'].loc[read],read_db_id['AGE'].loc[read],read_db_id['GEN'].loc[read],read_db_id['CPF'].loc[read],read_db_id['P_PAC'].loc[read],read_db_id['A_PAC'].loc[read]]

  return render_template('editar.html', read_id=read_id)


@app.route('/edite_data', methods=['POST', 'GET'])
def edite_data():
  if request.method == 'POST':
    result = request.form
    id_name = result['read-id']
    print(':::::::::>>: ',id_name)
    name = result['name-paciente']
    age = result['age-paciente']
    gen = result['gen-paciente']
    cpf = result['cpf-paciente']
    p_pac = result['p-paciente']
    a_pac = result['a-paciente']

    CALC.ed_data(id_name, name,age, gen, cpf, p_pac, a_pac)

    read_db = CALC.read_all()

    lista_pacientes = []
    for cont in range(0, len(read_db['ID'])):
      lista_pacientes.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])

    return render_template('home.html', lista_pacientes=lista_pacientes)


@app.route('/del_data/<page_id>')
def del_data(page_id):

  CALC.del_data(page_id)

  read_db = CALC.read_all()

  lista_pacientes = []
  for cont in range(0, len(read_db['ID'])):
    lista_pacientes.append([read_db['ID'].loc[cont], read_db['NAME'].loc[cont], read_db['AGE'].loc[cont], read_db['GEN'].loc[cont],read_db['CPF'].loc[cont],read_db['P_PAC'].loc[cont],read_db['A_PAC'].loc[cont], read_db['DATE_LOG'].loc[cont]])

  return render_template('paciente.html', lista_pacientes=lista_pacientes)

app.run(host='0.0.0.0', port='5000', debug=True)



