import random
from paho.mqtt import client as mqtt_client

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

if __name__ == '__main__':
    broker = 'localhost'
    port = 9001
    topic = "python/wss"
    client_id = f'python-mqtt-{random.randint(0, 100)}'
    # username = 'emqx'
    # password = 'public'
    client = mqtt_client.Client(client_id,transport='websockets')
    # client.username_pw_set(username, password)
    client.tls_set('ca.crt',tls_version=2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.subscribe(topic)
    client.loop_forever()
