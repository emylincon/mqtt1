import paho.mqtt.client as mqtt
import os

os.system('clear')
print('-----------------------------------')
print('Welcome to MQTT Publisher client')
print('-----------------------------------')
client = mqtt.Client()
username = input('Username of Broker: ').strip()
password = input('Password of Broker: ').strip()
broker_ip = input("Broker's IP: ").strip()
broker_port_no = int(input("Broker's Port no: ").strip())
topic = input("Topic: ").strip()
print('-----------------------------------')


client.username_pw_set(username, password)
client.connect(broker_ip, broker_port_no, 60)

while True:
    try:
        message = input('Input Message: ').strip().lower()
        client.publish(topic, message)
        print("Message Sent")
    except KeyboardInterrupt:
        print('\nProgramme Terminated')
        break
