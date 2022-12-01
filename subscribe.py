#!usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import operations
import sql_functions

# These variables are global!

list_of_temps = []
average_temperature = 0

# -------------------------------------------------------

def do_operations(list_of_temps):
	output = operations.operation_average(list_of_temps)	
	return output

def main(location):
	config = operations.read()
	client = operations.make_connection()
	client.connect(config["broker"]) 
	recieve_msg(client, config["topic"], location)
	content = serve_content()
	#sql_functions.save_content(list_of_temps)
	return content

def recieve_msg(client, topic, location):

	client.loop_start()

	client.subscribe(topic + "/" + location)
	client.on_message=on_message 

	time.sleep(30)
	client.loop_stop()

def on_message(client, userdata, message):
	decoded_message = str(message.payload.decode("utf-8"))
	#print("received message: " ,decoded_message)
	list_of_temps.append(decoded_message)

def serve_content():
	content = "The current collected temperatures are:" + str(list_of_temps) + ", the average is" + str(do_operations(list_of_temps))
	return content

if __name__ == '__main__':
	main()