import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("ece180d/rps", qos=1)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, message):

    # Assuming the message is the other player's move
    opponent_move = str(message.payload.decode("utf-8"))

    # Play the game and get the result
    user_move = str(input("Type 'rock', 'paper', or 'scissors': "))
    
    # Determine the winner
    winner = determine_winner(user_move, opponent_move)
    print("Result:", winner)

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async('mqtt.eclipseprojects.io')
client.loop_start()

def determine_winner(player_move, opponent_move):
    # Implement your logic to determine the winner
    # Example logic: rock beats scissors, scissors beats paper, paper beats rock

    if player_move == opponent_move:
        return "It's a tie!"
    elif (player_move == 'rock' and opponent_move == 'scissors') or \
         (player_move == 'scissors' and opponent_move == 'paper') or \
         (player_move == 'paper' and opponent_move == 'rock'):
        return "You win!"
    else:
        return "You lose!"

while True:
    pass  # Add any other non-blocking operations if needed
