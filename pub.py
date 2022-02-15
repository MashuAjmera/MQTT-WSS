import random  
import time
from paho.mqtt import client as mqtt_client

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def publish(client,topic):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        
if __name__ == '__main__':
    broker = 'localhost'
    port = 9001
    topic = "python/wss" 
    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    # username = 'emqx'
    # password = 'public'
    client = mqtt_client.Client(client_id,transport='websockets')
    # client.username_pw_set(username, password)
    client.tls_set('ca.crt',tls_version=2)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()
    publish(client,topic)
