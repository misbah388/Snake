#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random
import os
pygame.mixer.init()

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

screen_width=900
screen_hight=600

#Creating window
gamewindow=pygame.display.set_mode((900,600))
# background image
bgimg = pygame.image.load('bimage.webp')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_hight)).convert_alpha()
bcimg = pygame.image.load('bgimage.jpg')
bcimg = pygame.transform.scale(bcimg, (screen_width, screen_hight)).convert_alpha()
img = pygame.image.load('image.jpg')
img = pygame.transform.scale(img, (screen_width, screen_hight)).convert_alpha()


#creat title
pygame.display.set_caption("Snake With Harry") 
pygame.display.update()

# set Timing
clock=pygame.time.Clock()
font=pygame.font.SysFont(None, 45) #set test font


def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])
    
def plot_snake(gamewindow,color,snake_list,snake_size):
    #print(snake_list)
    for x, y in snake_list:
            pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
            
            
def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill((240,220,240))
        gamewindow.blit(bcimg, (0,0))
        text_screen("Welcom to Snakes",black,260,250)
        text_screen("Press Space Bar to Play",black,235,300)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.load('back.mp3')
                        pygame.mixer.music.play()
                        gameloop()
        
                    
        pygame.display.update()

        clock.tick(30)

                    

    #crating a game loop
def gameloop():
    
    #Game specific varibal
    exit_game= False
    game_over = False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    snake_list=[]
    snake_len=1
    # check if highscore file exists
    if(not os.path.exists("highscore,txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    
    with open("highscore.txt","r") as f:
        highscore=f.read()
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_hight/2)
    score=0
    init_velocity = 5

    snake_size=15
    fps=30
# Game loop
    while not exit_game: #Set Game Over
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))

            gamewindow.fill((250,240,3))
            gamewindow.blit(img, (0,0))
            text_screen("Game Over! Please Enter To Continue",red,160,250)
            
            # page quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                  # Game Restart  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                       
                        welcome()

        else:
        
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    exit_game=True
                    
             # Set moving Keyes
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0
                            
                    if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0
                    if event.key == pygame.K_UP:
                            velocity_y = - init_velocity
                            velocity_x = 0
                    if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0
                    if event.key == pygame.K_q:
                            score +=5
                            
            snake_x += velocity_x
            snake_y += velocity_y 
            # Set Snake Food
            if abs(snake_x - food_x)<6and abs(snake_y - food_y)<6:
                #pygame.mixer.music.load('food.mp3')
                #pygame.mixer.music.play()
                score += 10
                food_x = random.randint(20,screen_width)
                food_y = random.randint(20,screen_hight)
                snake_len += 5
                if score>int(highscore):
                    highscore=score


            gamewindow.fill((0,255,0))
            gamewindow.blit(bgimg, (0,0))
            # How to show score in screen
            text_screen("score: " + str(score)+ "  highscore: "+ str(highscore), black,5,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            #pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_len:
                del snake_list[0]
               # game over 
            if head in snake_list[:-1]:
                game_over= True
                pygame.mixer.music.load('gameover.mpeg')
                pygame.mixer.music.play()
                
                # set snake in screen
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_hight:
                    game_over = True
                    pygame.mixer.music.load('gameover.mpeg')
                    pygame.mixer.music.play()
            
            plot_snake(gamewindow,black,snake_list,snake_size)


        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    quit()
welcome()


# In[ ]:






# In[ ]:






# In[ ]:





# In[ ]:




