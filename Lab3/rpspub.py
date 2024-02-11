import paho.mqtt.client as mqtt
import time
import pygame
import os
import random

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect_async('mqtt.eclipseprojects.io')
client.loop_start()

message = "Welcome to Rock-Paper-Scissors! Type 'r', 'p', or 's' to make a move."
client.publish("ece180d/rps", str(message), qos=1)

while True:
    time.sleep(1)  # Add a delay to avoid high CPU usage

    # Assuming the user enters their move in the console
    user_move = str(input("Type 'r', 'p', or 's': "))
    
    # Publish user's move to the topic
    client.publish("ece180d/rps", user_move, qos=1)
