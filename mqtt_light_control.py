# Developed by Emeka
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12      #GPIO 18

os.system('clear')
print('---------------------------------------------------')
print('Welcome to MQTT subscriber client for light Control')
print('---------------------------------------------------')

username = input('Username of Broker: ').strip()
password = input('Password of Broker: ').strip()
broker_ip = input("Broker's IP: ").strip()
broker_port_no = int(input("Broker's Port no: ").strip())
topic = input("Topic: ").strip()


# Callback Function on Connection with MQTT Server
def on_connect(connect_client, userdata, flags, rc):
    print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(topic)


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    # print the message received from the subscribed topic
    message = str(msg.payload, 'utf-8')
    print(message)
    if message.strip() == 'lights on':
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, GPIO.HIGH)
        print('switched on')
        time.sleep(2)
    elif message.strip() == 'lights off':
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, GPIO.LOW)
        print('switched off')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(broker_ip, broker_port_no, 60)

client.loop_forever()
