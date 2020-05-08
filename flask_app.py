from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
@app.route('/')
def inicio():
    return  render_template('inicio.html')


@app.route("/login")
@app.route('/')
def login():
    return  render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
