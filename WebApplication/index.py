from flask import Flask, json, jsonify, Response
from flask import render_template
from flask import redirect
from flask import request
from camera import Camera
import subprocess
import queue


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

@app.route("/doorway/retrieve")
def retrieve_data():
    return


@app.route('/livingroom')
def livingroom():
    return render_template('livingroom.html')

@app.route('/process_LRLight_Toggle', methods=['POST'])
def process_light():
    print('Process triggered')
    status = request.form.get('status')
    print('Status: ', status)
    if status == 'true':
        print('Status is true.')
        subprocess.Popen(['python', 'Living Room/LivingRoom_Light_On.py'])
        return jsonify({'msg': 'The living room light is turned On'})
    elif status == 'false':
        print('Status is false.')
        subprocess.Popen(['python', 'Living Room/LivingRoom_Light_Off.py'])
        return jsonify({'msg': 'The living room light is turned Off'})
    else:
        print('Status is error.')
        return jsonify({'msg': 'There is an error with the Living Room light toggle.'})
    
@app.route('/process_LRFan_Toggle', methods=['POST'])
def process_fan():
    print('Process triggered')
    status = request.form.get('status')
    print('Status: ', status)
    if status == 'true':
        print('Status is true.')
        subprocess.Popen(['python', 'Living Room/LivingRoom_Fan_On.py'])
        return jsonify({'msg': 'The living sroom fan is turned On'})
    elif status == 'false':
        print('Status is false.')
        subprocess.Popen(['python', 'Living Room/LivingRoom_Fan_Off.py'])
        return jsonify({'msg': 'The living room fan is turned Off'})
    else:
        print('Status is error.')
        return jsonify({'msg': 'There is an error with the Living Room fan toggle.'})

@app.route('/babyroom')
def babyroom():
    return render_template('babyroom.html')

@app.route('/bedroom')
def bedroom():
    return render_template('bedroom.html')

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)