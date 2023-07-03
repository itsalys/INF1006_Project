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

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)