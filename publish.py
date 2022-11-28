#!/usr/bin/env python3

# This is used to publish information on the thread 

import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import random

mqttBroker ="mqtt.eclipseprojects.io" 

client = mqtt.Client("JT/Temperature") # the Topic that It is subscribed to
client.connect(mqttBroker) 

def publish_temperatures(): 
    while True:
        client.publish("JT/Temperature",random.randint(0,30))
        print("Published")
        time.sleep(1)

def main():
    publish_temperatures()

if __name__ == '__main__':
    main()
