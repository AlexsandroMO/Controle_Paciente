from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/add_create')
def add_create():
  return render_template('cadastrar.html')

#app.run(host='0.0.0.0', port=8080, debug=True)
app.run(host='0.0.0.0', port='5000', debug=True)