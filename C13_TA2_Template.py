# Import "pygame", "time" and "random" modules 
import pygame
import time
import random

# Initialize "pygame"
pygame.init() 

# TA2a-Step 1: Define image loading function here. Name it as "image_load"






# TA2b-Step 1: Define a function to display text. Name it as "text_display"





# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# Create a "carx", "cary" and "bgy" variables to track car and background positions
carx = 140
cary = 450
bgy = 0
# Create a variable "threshold" and set its value to zero
threshold = 0
# Create a counter variable to keep track of gameloop iterations
counter = 0
# Choose random x and y locations for stone placement
stone_x = random.randint(100, carx+100)
stone_y = random.randint(100, cary-100)
# Create a "red_carx" set to 305, "red_cary" set to 200 to track red car position. 
red_carx = 305
red_cary = 200

# Game loop
carryOn = True
# Create first time point "t1" 
t1 = time.time()
while carryOn:
    # NOTE: The images file and .py file in which image is being used must be in same folder
    
    # TA2a-Step 2: Call the function "image_load()" 
    # 1. To display the background image, function inputs are- "road.png", 650, 600, 0, 0


    # 2. To display the yellow car image, store the fuction output in "yellow_car_scaled", 
    #    function inputs are- "yellow_car.png", 230, 140, carx, cary


    # 3. To display the stone image, store the fuction output in "stone_scaled", 
    #    function inputs are- "stone.png", 70, 60, stone_x, stone_y 


    # 4. To display the red car image, store the fuction output in "red_car_scaled", 
    #    function inputs are- "red_car.png", 80,130, red_carx, red_cary 

    
    # Check for up, down, left, right, spacebar and enter key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cary -= 10
                bgy -= 10
            if event.key == pygame.K_DOWN:
                cary += 10
                bgy += 10
            if event.key==pygame.K_RIGHT:
                if carx <= 320:
                    carx += 10
            if event.key==pygame.K_LEFT:
                if carx >= 50:                          
                    carx -= 10 
            if event.key == pygame.K_SPACE:
                if carx < 260: 
                    carx += 90
            if event.key == pygame.K_RETURN:
                if game_time >= threshold and game_time <= (threshold+10):
                    cary -= 50 
                    threshold += 10
                
    # Reset car and background positions
    if cary <= 30:
        bgy = 0
        cary = 450
        counter += 1 
        stone_x = random.randint(100, carx+100)
        stone_y = random.randint(100, cary-100)
        
    # Create rectangle for car and stone
    yellow_car_rect = yellow_car_scaled.get_rect(topleft = (carx+75,cary))
    yellow_car_rect.width = yellow_car_rect.width/3
    stone_rect = stone_scaled.get_rect(topleft = (stone_x, stone_y))
    # Draw rectangles for car and stone
    pygame.draw.rect(screen,(100,0,100),yellow_car_rect)
    pygame.draw.rect(screen,(0,0,100),stone_rect)
    # Get rectangle for red car
    red_car_rect = red_car_scaled.get_rect(topleft = (red_carx,red_cary))
    pygame.draw.rect(screen,(23,0,250),red_car_rect)
    
    # If car and stone rectangles collide, change yellow car and stone positions
    if yellow_car_rect.collidepoint(stone_rect.x,stone_rect.y):
        cary = 450
        stone_x = random.randint(100, carx+100)
        stone_y = random.randint(100, cary-100)
    
    # If the two cars collide, change car positions 
    if yellow_car_rect.collidepoint(red_car_rect.x,red_car_rect.y):
        carx = 140
        cary = 450
        red_cary = 450
        
    # Display yellow car image upon updating "carx" and "cary" variable values
    screen.blit(yellow_car_scaled,(carx, cary))
    
    # Display the stone upon updating "stone_x" and "stone_y" variable values  
    screen.blit(stone_scaled,(stone_x, stone_y))
    
    # Display red car image upon updating "red_carx" and "red_cary" variable values
    screen.blit(red_car_scaled,(red_carx, red_cary))
    
    # Create second time point "t2" 
    t2 = time.time()
    game_time = t2-t1
    game_time = round(game_time, 2)
    
    # TA2b-Step 2: Display game time elapsed
    text_display(35,"TIME ELAPSED: " + str(game_time)+ "seconds",0, 255,255,130,15)
    
    # Display finish line after 5 iterations of game loop
    # Check if "counter" is equal to 5
    if counter == 5:
        # Create and draw the finish line white-colored rectangle at (x,y)=(95, 40) with width=400 and height=30
        finish_line = pygame.Rect(95,40,400,30)
        pygame.draw.rect(screen,(255,255,255),finish_line)
        # TA2b-Step 2: Call the function "text_display()", display "----------FINISH----------" text. 

        pygame.display.flip()
        
        # End the game loop after displaying finish line
        pygame.time.wait(3000)
        screen.fill((0,100,200))        
        # TA2b-Step 2: Call the function "text_display()", display finish time in seconds 

        
        # TA2b-Step 2: Call the function "text_display()", display "Game Over, Good Luck Next Time!" text

        
        pygame.display.flip()
        pygame.time.wait(5000)
        # Break out of 'while' game loop
        break
    
    # Update the contents of the display
    pygame.display.flip()
    
# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()