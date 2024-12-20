import pygame
import random
pygame.init()
disp_width = 1200
disp_height = 900
disp=pygame.display.set_mode((disp_width,disp_height))

pygame.display.set_caption('Zmeyka')

clock = pygame.time.Clock()

blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)

snake_speed = 15


snake_tex = pygame.image.load("snake_head.png")
body_tex = pygame.image.load("snake_body.png")
apple_red_tex = pygame.image.load("apple_red.png")
apple_gold_tex = pygame.image.load("apple_gold.png")
apple_black_tex=pygame.image.load("apple_black.png")
apple_not_tex=pygame.image.load("apple_not.png")

style_font = pygame.font.SysFont("serif", 25)

def print_score(score):
    disp.blit(pygame.font.SysFont("cmmi10", 35).render('Ваш счёт: '+ str(score),True,black),[10,10])
def text(message, color):
    mesg = style_font.render(message, True, color)
    disp.blit(mesg, [50, 100])

def snake_draw(snake,snake_tex,body_tex):
    if len(snake)>1:
        for i in range(len(snake)):
            if i != len(snake)-1:
                disp.blit(body_tex,[snake[i][0],snake[i][1]])
               
            else:
                disp.blit(snake_tex,[snake[i][0],snake[i][1]])
    else:
        disp.blit(snake_tex,[snake[0][0],snake[0][1]])

def gameLoop():
    snake_x = 300
    snake_y = 300
 
    snake_x_t = 0       
    snake_y_t = 0
    snake_length = 1
    
    snake = []

    score= 0

    apple_choose=random.randint(1,100)

    apple_x = int(round(random.randrange(0, disp_width -70) / 10.0) * 10.0)
    apple_y = int(round(random.randrange(0, disp_height-70) / 10.0) * 10.0)


    game_over=False
    game_lose=False

    while game_over==False:
        
        disp.blit(pygame.image.load("fon.png"), ( 0,0 ) )
        
        while game_lose == True:
                disp.blit(pygame.image.load("fon_death.png"),(0,0))
                text("Ты проиграл! Ты набрал очков: "+str(score)+ ". Нажми r-чтобы попробовать снова, q-чтобы выйти:", red)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_lose = False
                        if event.key == pygame.K_r:
                            gameLoop()
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_t = -snake_speed
                    snake_y_t = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_t = snake_speed
                    snake_y_t = 0
                elif event.key == pygame.K_UP:
                    snake_y_t = -snake_speed
                    snake_x_t = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_t = snake_speed
                    snake_x_t = 0

        if snake_x > disp_width:
            snake_x = 0
        if snake_x < 0:
            snake_x = disp_width-1
        if snake_y > disp_height:
            snake_y = 0        
        if snake_y < 0:
            snake_y = disp_height-1
        
        
        if 85<apple_choose<=100:
            disp.blit(apple_gold_tex,[apple_x,apple_y])
        elif 0<apple_choose<=20:
            disp.blit(apple_not_tex,[apple_x,apple_y])
        elif 40<apple_choose<=55:
            disp.blit(apple_black_tex,[apple_x,apple_y])
        else:
            disp.blit(apple_red_tex,[apple_x,apple_y])
        
        snake_x += snake_x_t
        snake_y += snake_y_t

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake.append(snake_head)
        
        if len(snake) > snake_length:
            del snake[0]
 
        for x in snake[:-1]:
            if x == snake_head:
                game_lose = True
 
        snake_draw(snake,snake_tex,body_tex)
        print_score(score)
        

        if ((0<=(snake_x -apple_x)<35) or (0<=(apple_x -snake_x)<35)) and ((0<=(snake_y - apple_y)<35) or (0<=(apple_y -snake_y)<35)):
            if 85<apple_choose<=100:
                apple_x = int(round(random.randrange(0, disp_width - 70) / 10.0) * 10.0)
                apple_y = int(round(random.randrange(0, disp_height - 70) / 10.0) * 10.0)
                apple_choose = random.randint(1,100)
                if snake_length >1:
                    snake_length -= 1
                    del snake[0]
                score+= 5
            elif 0<apple_choose<=20:
                if snake_length>1:
                    if snake_y_t!=0:
                        if snake_y_t<0:
                            if apple_y+10*snake_speed>disp_height:
                                for i in range(10):
                                    snake.insert(0,[snake[0][0],snake[0][1]-1])
                            else:
                                for i in range(10):
                                    snake.insert(0,[snake[-1][0],snake[-1][1]+1])
                        if snake_y_t>0:
                            if apple_y-10*snake_speed<0:
                                for i in range(10):
                                    snake.insert(0,[snake[0][0],snake[0][1]+1])
                            else:
                                for i in range(10):
                                    snake.insert(0,[snake[-1][0],snake[-1][1]-1])
                    else:
                        if snake_x_t>0:
                            if apple_x+10*snake_speed>disp_width:
                                for i in range(10):
                                    snake.insert(0,[snake[0][0]-1,snake[0][1]])
                            else:
                                for i in range(10):
                                    snake.insert(0,[snake[-1][0]+1,snake[-1][1]])
                        if snake_x_t<0:
                            if apple_x-10*snake_speed<0:
                                for i in range(10):
                                    snake.insert(0,[snake[0][0]+1,snake[0][1]])
                            else:
                                for i in range(10):
                                    snake.insert(0,[snake[-1][0]-1,snake[-1][1]])
                else:
                    if snake_y_t!=0:
                        if apple_y+10*snake_speed>disp_height:
                            for i in range(10):
                               snake.insert(0,[snake[0][0],snake[0][1]-1])
                        else:
                            for i in range(10):
                               snake.insert(0,[snake[0][0],snake[0][1]+1])
                    else:
                        if apple_x+10*snake_speed>disp_width:
                            for i in range(10):
                                snake.insert(0,[snake[0][0]-1,snake[0][1]])
                        else:
                             for i in range(10):
                                 snake.insert(0,[snake[0][0]+1,snake[0][1]])
                apple_x = int(round(random.randrange(0, disp_width - 70) / 10.0) * 10.0)
                apple_y = int(round(random.randrange(0, disp_height - 70) / 10.0) * 10.0)
                apple_choose = random.randint(1,100)
                snake_length += 10
                score +=0    
            elif 40<apple_choose<=55:
                apple_x = int(round(random.randrange(0, disp_width - 70) / 10.0) * 10.0)
                apple_y = int(round(random.randrange(0, disp_height - 70) / 10.0) * 10.0)
                apple_choose = random.randint(1,100)
                if snake_length >1:
                    while(len(snake)>1):
                        del snake[0]
                    snake_length = 1
                score+= 15
            else:
                apple_x = int(round(random.randrange(0, disp_width - 70) / 10.0) * 10.0)
                apple_y = int(round(random.randrange(0, disp_height - 70) / 10.0) * 10.0)
                apple_choose = random.randint(1,100)
                snake_length+= 1
                score+= 1
        
        pygame.display.update()
        clock.tick(15)

    pygame.quit()
    quit()
gameLoop()