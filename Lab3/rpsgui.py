# Simple pygame program

# Import the necessary libraries
import pygame
import os
import random
ROC = 0
PAP = 1
SCI = 2


# Initialize the pygame library
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

#loading the imahe
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

answer = str(input(("What is yours? Type r/p/s for rock paper or scissors: ")))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

running = True
message = "empty"
while running:
    # Did the user click the window close button?
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    random_number = random.randint(0, 2)

    if(random_number == 0):
        image_com = scaled_image_s
        image_ucom = scaled_image_s.get_rect(center=(300, 150))
    elif(random_number == 1):
        image_com = scaled_image_r
        image_ucom = scaled_image_r.get_rect(center=(300, 150))
    elif(random_number == 2):
        image_com = scaled_image_p
        image_ucom = scaled_image_p.get_rect(center=(300, 150))
    if(answer == 'r'):
        image_user = scaled_image_r
        image_urect = scaled_image_r.get_rect(center=(300, 450))
    elif(answer == 'p'):
        image_user = scaled_image_p
        image_urect = scaled_image_p.get_rect(center=(300, 450))
    elif(answer == 's'):
        image_user = scaled_image_s
        image_urect = scaled_image_s.get_rect(center=(300, 450))

    if(answer == 'r'):
        if(random_number == 0):
            message = "Win!"
        if(random_number == 1):
            message = "Tie!"
        if(random_number == 2):
            message = "Lose!"
    elif(answer == 'p'):
        if(random_number == 0):
            message = "Lose!"
        if(random_number == 1):
            message = "Win!"
        if(random_number == 2):
            message = "Tie!"
    elif(answer == 's'):
        if(random_number == 0):
            message = "Tie!"
        if(random_number == 1):
            message = "Lose!"
        if(random_number == 2):
            message = "Win!"

    text = font.render(message , True, BLACK)
    # Blit the text onto the screen
    text_rect = text.get_rect()
    text_rect.center = (600 // 2, 600 // 2)
    screen.blit(text, text_rect)


    # Blit the image onto the screen
    screen.blit(image_com, image_ucom)
    screen.blit(image_user, image_urect)

    # Update the display
    pygame.display.flip()
    answer = str(input(("What is yours? Type r/p/s for rock paper or scissors: ")))



# Done! Time to quit.
pygame.quit()
