from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/index", code=302)

@app.route('/index')
def analytics():
    return render_template('index.html')

@app.route('/doorway')
def doorway():
    return render_template('doorway.html')

@app.route('/livingroom')
def livingroom():
    return render_template('livingroom.html')

@app.route('/babyroom')
def babyroom():
    return render_template('babyroom.html')

@app.route('/bedroom')
def bedroom():
    return render_template('bedroom.html')

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)