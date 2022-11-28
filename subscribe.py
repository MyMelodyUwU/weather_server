#!usr/bin/env python3

print("Subscribe is up ")
import paho.mqtt.client as mqtt
import time
import sys

import operations

def on_message(client, userdata, message):
	#print(str(message.payload.decode("utf-8")))
	output = str(message.payload.decode("utf-8"))
    #print("received message: " ,str(message.payload.decode("utf-8")))
	#output = operations.operation_average(str(message.payload.decode("utf-8")))
	print(output)
	return output

def main():

	mqttBroker ="mqtt.eclipseprojects.io"

	client = mqtt.Client("Smartphone")
	client.connect(mqttBroker) 

	client.loop_start()

	client.subscribe("JT/Temperature")
	# Initally the code was like this before change
	# 
	# client.on_message= on_message	


	# Here it is after change:
	print("Test")
	msg = client.on_message=on_message
	print("Fred")
	print(msg)

	time.sleep(30)
	client.loop_stop()

if __name__ == '__main__':
	main()