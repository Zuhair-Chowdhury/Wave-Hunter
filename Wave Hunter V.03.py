import pygame #pygame is imported into the program

pygame.init() #pygame is initialized

clock = pygame.time.Clock()
fps = 60 #frames per second
screen_width = 1600 #width of the screen
screen_height = 800 #height of the screen

screen = pygame.display.set_mode((screen_width, screen_height)) #setting the display 
pygame.display.set_caption("Wave Hunter")

player_positionx = 320 #setting position of the player on the x and y
player_positiony = 180
player_width = 128 #dimensions of the player
player_height = 128
player_velocity = 5 #speed of the player movement
player_jump = False #is player jumping
jump_count = 10
player_dash = False
dash_count = 5
playerfacing_right = True #which direction is the player facing

game_running = True
while game_running: #game loop
    clock.tick(fps)
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #checks if x button in top right is pressed
            game_running = False #redirects out of loop
    
    keys = pygame.key.get_pressed() #detects when a key is pressed

    if keys[pygame.K_a] and player_positionx > player_velocity: #when the 'A' key is pressed and not on the edge of the screen
        player_positionx -= player_velocity #player moves left
        playerfacing_right = False
    if keys[pygame.K_d] and player_positionx < screen_width - player_width: #when 'D' key is pressed and not on the edge of the screen
        player_positionx += player_velocity #player moves right
        playerfacing_right = True
    if not(player_jump):
        if keys[pygame.K_SPACE]: #when the spacebar is pressed
            player_jump = True #player is jumping
    else:
        if jump_count >= -10:
            neg = 1 #makes jump move upwards before peak
            if jump_count < 0:
                neg = -1 #makes the jump moves downwards after its peak
            player_positiony -= (jump_count ** 2) * 0.5 *neg #player moves in a line of a quadratic
            jump_count -= 1
        else:
            player_jump = False #jump has finished and now player is no longer in jump motion
            jump_count = 10
    if not(player_dash):
        if keys[pygame.K_LSHIFT]: #when left shift is pressed
            player_dash == True
    else:
        if dash_count > 0:
            if playerfacing_right == False:
                player_positionx -=  player_velocity * 2
                dash_count -= 1
            if playerfacing_right == True:
                player_positionx += player_velocity * 2
                dash_count -= 1
        else:
            player_dash = False
            dash_count = 5
                
    screen.fill((0,0,0)) #ensures the character does not copy itself
    pygame.draw.rect(screen, (255, 0, 0), (player_positionx, player_positiony, player_width, player_height))
    pygame.display.update()

pygame.quit() #program closes
