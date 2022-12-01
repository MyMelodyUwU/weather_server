#!/usr/bin/env python3

# This is used to publish information on the topic 

import paho.mqtt.client as mqtt 
import random
import time
import operations

# These are the global variables ->

client = mqtt.Client() 

# These functions are in alphabetical order! It shows the order the computer

def main():
    print("Waking up")
    config = operations.read()
    topic = config["topic"]
    location = config["location"]
    client.connect(config["broker"]) 
    publish_temperatures(topic, location)

def publish_temperatures(topic, location): 
    while True:
        temperature = random.randint(0, 30)
        client.publish(topic + "/" + location, temperature)
        print(f"Published: {temperature} C")
        time.sleep(1)

if __name__ == "__main__":
    main()
