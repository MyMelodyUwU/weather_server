#!usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import operations

# These variables are global!

input_file = "z_in"

list_of_temps = []
average_temperature = 0

# -------------------------------------------------------

def do_operations(list_of_temps):
	output = operations.operation_average(list_of_temps)	
	return output

def main():
	thread = read()
	make_connection(thread)
	content = serve_content()
	return content

def make_connection(thread):

	mqttBroker ="mqtt.eclipseprojects.io"

	client = mqtt.Client("Smartphone")
	client.connect(mqttBroker) 

	client.loop_start()

	client.subscribe(thread)
	client.on_message=on_message 

	time.sleep(30)
	client.loop_stop()

def on_message(client, userdata, message):
	decoded_message = str(message.payload.decode("utf-8"))
	print("received message: " ,decoded_message)
	list_of_temps.append(decoded_message)

def print_temps():
	print(list_of_temps)

def read():
    file = open(input_file, "r")
    record = file.read()[:-1]
    return record

def serve_content():
	content = "The current collected temperatures are:" + str(list_of_temps) + ", the average is" + str(do_operations(list_of_temps))
	return content

if __name__ == '__main__':
	main()