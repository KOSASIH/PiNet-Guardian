import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker_ip, broker_port):
        self.client = mqtt.Client()
        self.client.connect(broker_ip, broker_port)

    def publish_message(self, topic, message):
        self.client.publish(topic, message)

    def subscribe_topic(self, topic):
        self.client.subscribe(topic)

    def on_message(self, client, userdata, message):
        print("Received message:", message.payload)

    def start_listening(self):
        self.client.loop_start()
