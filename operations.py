#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json
#import numpy as np

config_file = "config.json" #Config info

temp_list = []

def operation_average(values):
	for i in values:
		temp_list.append(int(i))
	return sum(temp_list) / len(temp_list)

def read():
    file = open(config_file, "r")
    config = json.loads(file.read())
    return config

def make_connection():
	client = mqtt.Client()
	return client 

# def create_smooth_RNG(seed_no):
# 	x = np.random.uniform(seed_no - 5,seed_no + 5,100)
# 	returned_array = abs(x.astype(int))
# 	average_temp = sum(returned_array) / len(returned_array)
	
# 	return int(average_temp)
