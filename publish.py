#!/usr/bin/env python3

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import random

mqttBroker ="mqtt.eclipseprojects.io" 

client = mqtt.Client("JT/Temperature")
client.connect(mqttBroker) 

#start_time = time.time()
#finish_time = time.time() + 

def publish_temperatures(): 
    while True:
        client.publish("JT/Temperature",random.randint(0,30))
        print("Published")
        time.sleep(1)

def main():
    publish_temperatures()

if __name__ == '__main__':
    main()