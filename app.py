from flask import Flask, render_template
import sys

sys.path.insert(0, '/home/itexps/SmarrtCarProject/Code/Server')

from Buzzer import *
from Led import *
from Motor import *



buzzer = Buzzer()
led = Led()
PWM = Motor()

toggleBuzzer = False
toggleLED = False
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggleBuzzer')
def toggleBuzzer():
    global toggleBuzzer
    toggleBuzzer = not toggleBuzzer
    if toggleBuzzer == True:
        buzzer.run('1')
    else:
        buzzer.run('0')


@app.route('/toggleLED')
def toggleLED():
    global toggleLED
    toggleLED = not toggleLED
    if toggleLED == True:
        led.ledIndex(0x01,255,0,0)      #Red
    else:
        led.colorWipe(led.strip, Color(0,0,0))
    print('LED', toggleLED)

# Motor
@app.route('/forward')
def forward():
    PWM.setMotorModel(1000,1000,1000,1000)  
@app.route('/backward')
def backward():
    PWM.setMotorModel(-1000,-1000,-1000,-1000) 
@app.route('/left')
def left():
    PWM.setMotorModel(-1500,-1500,2000,2000)   
@app.route('/right')
def right():
    PWM.setMotorModel(2000,2000,-1500,-1500)  
@app.route('/stopmotor')
def stopmotor():
    PWM.setMotorModel(0,0,0,0)  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')