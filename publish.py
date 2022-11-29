#!/usr/bin/env python3

# This is used to publish information on the thread 

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import random
import sys

input_file = "/dev/stdin" #Console read
#input_file = "z_in" #Input file

output_file = "/dev/stdout" #Console output
#output_file = "z_out" #output file

mqttBroker ="mqtt.eclipseprojects.io" 

thread = ""

def read():
    file = open(input_file, "r")
    record = file.read()[:-1]
    return record

client = mqtt.Client(thread) # the Topic that It is subscribed to
client.connect(mqttBroker) 

def publish_temperatures(): 
    while True:
        client.publish(thread,random.randint(0,30))
        print("Published")
        time.sleep(1)

def main():
    print("Waking up")
    thread = read()
    print(thread)
    publish_temperatures()

if __name__ == '__main__':
    main()
