import paho.mqtt.client as mqtt


counter = 0

# Define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("ece180d/test", qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')


# The default message callback.
# (you can create separate callbacks per subscribed topic)
def on_message(client, userdata, message):
    global counter
    print('Received message: "' + str(message.payload) + '" on topic "' +
          message.topic + '" with QoS ' + str(message.qos))
    
    counter += float(message.payload)
    print('Counter: ' + str(float(counter)))
    

# Create a client instance.
client = mqtt.Client()

# Add additional client options (security, certifications, etc.)
# Many default options should be good to start off.

# Add callbacks to the client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# Connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')
# client.connect("test.mosquitto.org", 1883, 60)
# client.connect("mqtt.eclipse.org")

# Call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# client.loop_forever()

while True:  # Perhaps add a stopping condition using some break or something.
    
    pass  # Do your non-blocked other stuff here, like receive IMU data or something.

# Use subscribe() to subscribe to a topic and receive messages.
# Use publish() to publish messages to the broker.
# Use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()
