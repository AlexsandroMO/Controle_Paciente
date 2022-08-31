from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')

app.run(host='0.0.0.0', port=8080, debug=True)