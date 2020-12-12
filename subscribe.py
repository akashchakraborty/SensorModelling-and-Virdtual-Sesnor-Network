import paho.mqtt.client as mqtt
import time
import matplotlib.pyplot as plt

def Subscribe_data(topic):
	data=[]

	def on_message(client, userdata, message):
	    print("received message: " ,str(message.payload.decode("utf-8")))
	    x = message.payload.decode("utf-8")
	    #print(x)
	    x = float(x)
	    data.append(x)
	    

	mqttBroker ="test.mosquitto.org"

	client = mqtt.Client("Neelakshi_7081")
	client.connect(mqttBroker) 

	client.loop_start()

	client.subscribe(topic)
	client.on_message=on_message 


	time.sleep(10)
	client.loop_stop()
	
	return data

#Subscribe_data("Capstone Data Temperature")