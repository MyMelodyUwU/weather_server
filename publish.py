#!/usr/bin/env python3

# This is used to publish information on the topic 

import paho.mqtt.client as mqtt 
import random
import time
import operations
import numpy as np

# These are the global variables ->

client = mqtt.Client() 

# These functions are in alphabetical order! It shows the order the computer

def main():
    print("Waking up")
    config = operations.read()
    topic = config["topic"]
    #location = config["location"]
    client.connect(config["broker"]) 
    publish_temperatures(topic, config)

def publish_temperatures(topic, config): 
    while True:
        count = -1
        max_count = 4
        for i in config["location"]:
            count += 1
            set_location = config["location"][count]
            if(count == max_count) :
                count = 0
            #seed_no = random.randint(0, 30) 
            #temperature = operations.create_smooth_RNG(seed_no)
            temperature = random.randint(0, 30) 
            client.publish(topic + "/" + set_location, temperature)
            print(f"Published: {temperature} C in {set_location}")
            time.sleep(1)

if __name__ == "__main__":
    main()
