#!usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import operations

list_of_temps = []
average_temperature = 0

def on_message(client, userdata, message):
	decoded_message = str(message.payload.decode("utf-8"))
	print("received message: " ,decoded_message)
	list_of_temps.append(decoded_message)

def print_temps():
	print(list_of_temps)

def do_operations(list_of_temps):
	output = operations.operation_average(list_of_temps)	
	return output

def serve_content():
	#print_temps()
	#print(do_operations(list_of_temps))
	content = str(list_of_temps) + ", the average is" + str(do_operations(list_of_temps))
	return content

def make_connection():

	mqttBroker ="mqtt.eclipseprojects.io"

	client = mqtt.Client("Smartphone")
	client.connect(mqttBroker) 

	client.loop_start()

	client.subscribe("JT/Temperature")
	client.on_message=on_message 

	time.sleep(3)
	client.loop_stop()


def main():
	make_connection()
	content = serve_content()
	return content

if __name__ == '__main__':
	main()