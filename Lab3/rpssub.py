import paho.mqtt.client as mqtt
import time
import pygame
import os
import random

ROC = 0
PAP = 1
SCI = 2
pygame.init()

screen = pygame.display.set_mode([600, 600])

#loading the image


def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("ece180d/rps", qos=1)
    

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

RED = (255, 0, 0)

# Define circle parameters
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)


def on_message(client, userdata, message):
    scissors = pygame.image.load("/Users/ianwells/180DA-WarmUp/Lab3/s.png")
    paper = pygame.image.load("/Users/ianwells/180DA-WarmUp/Lab3/p.jpg")
    rock =  pygame.image.load("/Users/ianwells/180DA-WarmUp/Lab3/r.png")

    #scaling
    scale_factor_s = 0.2
    scaled_width_s = int(scissors.get_width() * scale_factor_s)
    scaled_height_s = int(scissors.get_height() * scale_factor_s)
    scaled_image_s = pygame.transform.scale(scissors, (scaled_width_s, scaled_height_s))

    scale_factor_p = 0.1
    scaled_width_p = int(paper.get_width() * scale_factor_p)
    scaled_height_p = int(paper.get_height() * scale_factor_p)
    scaled_image_p = pygame.transform.scale(paper, (scaled_width_p, scaled_height_p))

    scale_factor_r = 0.1
    scaled_width_r = int(rock.get_width() * scale_factor_r)
    scaled_height_r = int(rock.get_height() * scale_factor_r)
    scaled_image_r = pygame.transform.scale(rock, (scaled_width_r, scaled_height_r))


    # Assuming the message is the other player's move
    opponent_move = message.payload.decode("utf-8")
    # Play the game and get the result
    user_move = str(input("Type 'r', 'p', or 's': "))

    screen.fill((255, 255, 255))

    if(opponent_move == 's'):
        image_com = scaled_image_s
        image_ucom = scaled_image_s.get_rect(center=(300, 150))
    elif(opponent_move == 'r'):
        image_com = scaled_image_r
        image_ucom = scaled_image_r.get_rect(center=(300, 150))
    elif(opponent_move == 'p'):
        image_com = scaled_image_p
        image_ucom = scaled_image_p.get_rect(center=(300, 150))
    if(user_move == 'r'):
        image_user = scaled_image_r
        image_urect = scaled_image_r.get_rect(center=(300, 450))
    elif(user_move == 'p'):
        image_user = scaled_image_p
        image_urect = scaled_image_p.get_rect(center=(300, 450))
    elif(user_move == 's'):
        image_user = scaled_image_s
        image_urect = scaled_image_s.get_rect(center=(300, 450))

    if(user_move == 'r'):
        if(opponent_move == 's'):
            message = "Win!"
        if(opponent_move == 'r'):
            message = "Tie!"
        if(opponent_move == 'p'):
            message = "Lose!"
    elif(user_move == 'p'):
        if(opponent_move == 's'):
            message = "Lose!"
        if(opponent_move == 'r'):
            message = "Win!"
        if(opponent_move == 'p'):
            message = "Tie!"
    elif(user_move == 's'):
        if(opponent_move == 's'):
            message = "Tie!"
        if(opponent_move == 'r'):
            message = "Lose!"
        if(opponent_move == 'p'):
            message = "Win!"

    
    text = font.render(message , True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (600 // 2, 600 // 2)
    screen.blit(text, text_rect)


    # Blit the image onto the screen
    screen.blit(image_com, image_ucom)
            
    
    screen.blit(image_user, image_urect)

    # Update the display
    pygame.display.flip()
    # Determine the winner
    #determine_winner(user_move, opponent_move)

def determine_winner(player_move, opponent_move):
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)

    running = True
    message = "empty"
    print(message)
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white color
        screen.fill((255, 255, 255))

        # Draw a red rectangle (x, y, width, height)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 200, 150))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    
        
        
    #     # Did the user click the window close button?
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False

    #     # Fill the background with white
    #     screen.fill((255, 255, 255))
    #     running = False
    #     pygame.display.flip()
    #     pygame.quit()

    #     if(opponent_move == 0):
    #         image_com = scaled_image_s
    #         image_ucom = scaled_image_s.get_rect(center=(300, 150))
    #     elif(opponent_move == 1):
    #         image_com = scaled_image_r
    #         image_ucom = scaled_image_r.get_rect(center=(300, 150))
    #     elif(opponent_move == 2):
    #         image_com = scaled_image_p
    #         image_ucom = scaled_image_p.get_rect(center=(300, 150))
        
    #     if(player_move == 'r'):
    #         image_user = scaled_image_r
    #         image_urect = scaled_image_r.get_rect(center=(300, 450))
    #     elif(player_move == 'p'):
    #         image_user = scaled_image_p
    #         image_urect = scaled_image_p.get_rect(center=(300, 450))
    #     elif(player_move == 's'):
    #         image_user = scaled_image_s
    #         image_urect = scaled_image_s.get_rect(center=(300, 450))

    #     if(player_move == 'r'):
    #         if(opponent_move == 0):
    #             message = "Win!"
    #         if(opponent_move == 1):
    #             message = "Tie!"
    #         if(opponent_move == 2):
    #             message = "Lose!"
    #     elif(player_move == 'p'):
    #         if(opponent_move == 0):
    #             message = "Lose!"
    #         if(opponent_move == 1):
    #             message = "Win!"
    #         if(opponent_move == 2):
    #             message = "Tie!"
    #     elif(player_move == 's'):
    #         if(opponent_move == 0):
    #             message = "Tie!"
    #         if(opponent_move == 1):
    #             message = "Lose!"
    #         if(opponent_move == 2):
    #             message = "Win!"

    #     text = font.render(message , True, BLACK)
    #     text_rect = text.get_rect()
    #     text_rect.center = (600 // 2, 600 // 2)
    #     screen.blit(text, text_rect)

    #     screen.blit(image_com, image_ucom)
    #     screen.blit(image_user, image_urect)

    #     pygame.display.flip()

    #     # Exit the loop after one iteration
    #     running = False

    # # Done! Time to quit.
    # pygame.quit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async('mqtt.eclipseprojects.io')
client.loop_start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

##############################
