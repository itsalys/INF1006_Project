from flask import Flask, json, jsonify, Response
from flask import render_template
from flask import redirect
from flask import request
from camera import Camera
import subprocess
import queue
import paho.mqtt.client as mqtt

app = Flask(__name__)

received_messages = []

mqtt_broker = "192.168.1.2"
mqtt_username = "admin"
mqtt_pwd = "mqttbroker"
topics = [("Doorway/Delivery", 0), ("Doorway/Security", 0)]

# Callback function when a message is received from the subscribed topics
def on_message(client, userdata, msg):

    received_data = json.loads(msg.payload.decode("utf-8", "ignore"))
    # received_data = json.loads(msg.payload)
    print(f"topic: {msg.topic}")

    received_messages.append({"topic": msg.topic, "mqttdata": received_data})

def on_connect(client, userdata, flags, rc):
    print("Connection attempt returned: " + mqtt.connack_string(rc))
    print(f"Successfully connected to MQTT Broker @ {mqtt_broker}")

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_pwd) # comment out if no usr name and password set
client.connect(mqtt_broker, 1883)
client.on_connect = on_connect
client.subscribe(topics)
client.on_message = on_message
client.loop_start()


@app.route('/')
def index():
    return redirect("/index", code=302)

@app.route('/index')
def analytics():
    return render_template('index.html')

@app.route('/doorway')
def doorway():
    return render_template('doorway.html')

@app.route('/process/sub')
def get_mqtt_message():
    global received_messages
    print(received_messages)
    return jsonify(received_messages)


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