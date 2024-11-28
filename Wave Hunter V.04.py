import pygame #pygame is imported into the program

pygame.init() #pygame is initialized

clock = pygame.time.Clock()
fps = 60 #frames per second
screen_width = 1920 #width of the screen
screen_height = 1080 #height of the screen

screen = pygame.display.set_mode((screen_width, screen_height)) #setting the display 
pygame.display.set_caption("Wave Hunter")

RunRight = [pygame.image.load('Player Animations/RRA0.png'), pygame.image.load('Player Animations/RRA1.png'), pygame.image.load('Player Animations/RRA2.png'), pygame.image.load('Player Animations/RRA3.png'), pygame.image.load('Player Animations/RRA4.png'), pygame.image.load('Player Animations/RRA5.png'), pygame.image.load('Player Animations/RRA6.png'), pygame.image.load('Player Animations/RRA7.png')]
RunLeft = [pygame.image.load('Player Animations/LRA0.png'), pygame.image.load('Player Animations/LRA1.png'), pygame.image.load('Player Animations/LRA2.png'), pygame.image.load('Player Animations/LRA3.png'), pygame.image.load('Player Animations/LRA4.png'), pygame.image.load('Player Animations/LRA5.png'), pygame.image.load('Player Animations/LRA6.png'), pygame.image.load('Player Animations/LRA7.png')]
IdleRight = [pygame.image.load('Player Animations/RIA0.png'), pygame.image.load('Player Animations/RIA1.png'), pygame.image.load('Player Animations/RIA2.png'), pygame.image.load('Player Animations/RIA3.png'), pygame.image.load('Player Animations/RIA4.png'), pygame.image.load('Player Animations/RIA5.png'), pygame.image.load('Player Animations/RIA6.png'), pygame.image.load('Player Animations/RIA7.png'), pygame.image.load('Player Animations/RIA8.png'), pygame.image.load('Player Animations/RIA9.png'), pygame.image.load('Player Animations/RIA10.png'), pygame.image.load('Player Animations/RIA11.png'), pygame.image.load('Player Animations/RIA12.png'), pygame.image.load('Player Animations/RIA13.png'), pygame.image.load('Player Animations/RIA14.png'), pygame.image.load('Player Animations/RIA15.png'), pygame.image.load('Player Animations/RIA16.png'), pygame.image.load('Player Animations/RIA17.png'), pygame.image.load('Player Animations/RIA18.png'), pygame.image.load('Player Animations/RIA19.png')]
IdleLeft = [pygame.image.load('Player Animations/LIA0.png'), pygame.image.load('Player Animations/LIA1.png'), pygame.image.load('Player Animations/LIA2.png'), pygame.image.load('Player Animations/LIA3.png'), pygame.image.load('Player Animations/LIA4.png'), pygame.image.load('Player Animations/LIA5.png'), pygame.image.load('Player Animations/LIA6.png'), pygame.image.load('Player Animations/LIA7.png'), pygame.image.load('Player Animations/LIA8.png'), pygame.image.load('Player Animations/LIA9.png'), pygame.image.load('Player Animations/LIA10.png'), pygame.image.load('Player Animations/LIA11.png'), pygame.image.load('Player Animations/LIA12.png'), pygame.image.load('Player Animations/LIA13.png'), pygame.image.load('Player Animations/LIA14.png'), pygame.image.load('Player Animations/LIA15.png'), pygame.image.load('Player Animations/LIA16.png'), pygame.image.load('Player Animations/LIA17.png'), pygame.image.load('Player Animations/LIA18.png'), pygame.image.load('Player Animations/LIA19.png')]
JumpRight = [pygame.image.load('Player Animations/RJA0.png'), pygame.image.load('Player Animations/RJA1.png'), pygame.image.load('Player Animations/RJA2.png'), pygame.image.load('Player Animations/RJA3.png'), pygame.image.load('Player Animations/RJA4.png'), pygame.image.load('Player Animations/RJA5.png'), pygame.image.load('Player Animations/RJA6.png'), pygame.image.load('Player Animations/RJA7.png'), pygame.image.load('Player Animations/RJA8.png')]
JumpLeft = [pygame.image.load('Player Animations/LJA0.png'), pygame.image.load('Player Animations/LJA1.png'), pygame.image.load('Player Animations/LJA2.png'), pygame.image.load('Player Animations/LJA3.png'), pygame.image.load('Player Animations/LJA4.png'), pygame.image.load('Player Animations/LJA5.png'), pygame.image.load('Player Animations/LJA6.png'), pygame.image.load('Player Animations/LJA7.png'), pygame.image.load('Player Animations/LJA8.png')]
DashRight = [pygame.image.load('Player Animations/RDA0.png'), pygame.image.load('Player Animations/RDA1.png'), pygame.image.load('Player Animations/RDA2.png'), pygame.image.load('Player Animations/RDA3.png'), pygame.image.load('Player Animations/RDA4.png'), pygame.image.load('Player Animations/RDA5.png'), pygame.image.load('Player Animations/RDA6.png'), pygame.image.load('Player Animations/RDA7.png'), pygame.image.load('Player Animations/RDA8.png')]
DashLeft = [pygame.image.load('Player Animations/LDA0.png'), pygame.image.load('Player Animations/LDA1.png'), pygame.image.load('Player Animations/LDA2.png'), pygame.image.load('Player Animations/LDA3.png'), pygame.image.load('Player Animations/LDA4.png'), pygame.image.load('Player Animations/LDA5.png'), pygame.image.load('Player Animations/LDA6.png'), pygame.image.load('Player Animations/LDA7.png'), pygame.image.load('Player Animations/LDA8.png')]

player_positionx = 320 #setting position of the player on the x and y
player_positiony = 180
player_width = 384 #dimensions of the player
player_height = 384
player_velocity = 10 #speed of the player movement
player_jump = False #is player jumping
jump_count = 10
player_dash = False
dash_count = 5
playerfacing_right = False #which direction is the player facing
playerfacing_left = False
playerrunning_right = False
playerrunning_left = False
playerjumping_right = False
playerjumping_left = False
playerdashing_right = False
playerdashing_left = False
walkframe_count = 0
dash_cooldown = 0

def draw_window():
    global walkframe_count
    screen.fill((0, 0, 0))  # Clear the screen

    # Frame duration (fine-tuned for faster feel)
    frame_duration = 2  # Speed up animation while staying close to 1-second cycle

    if walkframe_count >= len(RunRight) * frame_duration:
        walkframe_count = 0  # Reset after cycling through all frames

    # Running Right
    if playerrunning_right:
        frame_index = walkframe_count // frame_duration
        screen.blit(RunRight[frame_index], (player_positionx, player_positiony))
        walkframe_count += 1

    # Running Left
    elif playerrunning_left:
        frame_index = walkframe_count // frame_duration
        screen.blit(RunLeft[frame_index], (player_positionx, player_positiony))
        walkframe_count += 1

    # Reset animation if not moving
    else:
        walkframe_count = 0

    pygame.display.update()


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
        playerrunning_left = True
        playerrunning_right = False
    elif keys[pygame.K_d] and player_positionx < screen_width - player_width: #when 'D' key is pressed and not on the edge of the screen
        player_positionx += player_velocity #player moves right
        playerrunning_right = True
        playerrunning_left = False
    else:
        playerrunning_left = False
        playerrunning_right = False
    if not(player_jump):
        if keys[pygame.K_SPACE]: #when the spacebar is pressed
            player_jump = True #player is jumping
            if playerfacing_right == True:
                playerjumping_right = True
                playerjumping_left = False
            if playerfacing_left == True:
                playerjumping_left = True
                playerjumping_right = False
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
            playerjumping_right = False
            playerjumping_left = False
    if not(player_dash):
        dash_cooldown -= 1 #player cooldown decrements by 1 if the the player is not dashing
        if dash_cooldown < 0:
            dash_cooldown = 0 #makes sure the variable does not go below 0
        if keys[pygame.K_LSHIFT] and dash_cooldown == 0 and player_positionx > player_velocity and player_positionx < screen_width - player_width: #when left shift is pressed
            player_dash = True #player dash is set to true and now goes to the else statement
    else:
        if dash_count > 0: 
            if playerfacing_left == True and player_positionx > player_velocity: #checks which way the player is facing and if the player might dash off the screen
                player_positionx -=  player_velocity * 2 #player moves by velocity * 2 5 times
                dash_count -= 1
                playerdashing_left = True
                playerdashing_right = False
                if player_positionx == player_velocity or player_positionx < player_velocity: #cancels the dash if they are dashing into the boundary
                    player_dash = False #all variables are reset
                    dash_count = 5
                    dash_cooldown = 15
                    playerdashing_right = False
                    playerdashing_left = False
            if playerfacing_right == True and player_positionx < screen_width - player_width:
                playerdashing_right = True
                playerdashing_left = False
                player_positionx += player_velocity * 2
                dash_count -= 1
                if player_positionx == screen_width - player_width or player_positionx > screen_width - player_width:
                    player_dash = False #all variables are reset
                    dash_count = 5
                    dash_cooldown = 15
                    playerdashing_right = False
                    playerdashing_left = False
        else: #dash has ended
            player_dash = False #all variables are reset
            dash_count = 5
            dash_cooldown = 15
            playerdashing_right = False
            playerdashing_left = False

    draw_window()

pygame.quit() #program closes
