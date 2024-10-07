import pygame #pygame is imported into the program

pygame.init() #pygame is initialized

screen_width = 640 #width of the screen
screen_height = 360 #height of the screen

screen = pygame.display.set_mode((screen_width, screen_height)) #setting the display 
pygame.display.set_caption("Wave Hunter")

player_positionx = 320 #setting position of the player on the x and y
player_positiony = 180
player_width = 128 #dimensions of the player
player_height = 128
player_velocity = 5 #speed of the player movement

game_running = True
while game_running: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks if x button in top right is pressed
            game_running = False #redirects out of loop

    pygame.draw.rect(screen, (255, 0, 0), (player_positionx, player_positiony, player_width, player_height))
    pygame.display.update()

pygame.quit() #program closes
