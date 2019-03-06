import paho.mqtt.client as mqtt
import os

os.system('clear')
print('-----------------------------------')
print('Welcome to MQTT Subscriber client')
print('-----------------------------------')

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
    print(str(msg.payload, 'utf-8'))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("admin", "password")
client.connect("192.168.40.222", 1883, 60)

client.loop_forever()