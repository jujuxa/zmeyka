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
gold=(255,215,0)

snake_speed = 15

snake_tex = pygame.image.load("snake_head.png")
body_tex = pygame.image.load("snake_body.png")
apple_red_tex = pygame.image.load("apple_red.png")

style_font = pygame.font.SysFont("serif", 25)
score_font = pygame.font.SysFont("cmmi10", 35)

def print_score(score):
    disp.blit(pygame.font.SysFont("cmmi10", 35).render('Ваш счёт: '+ str(score),True,gold),[50,10])

def text(message, color):
    mesg = style_font.render(message, True, color)
    disp.blit(mesg, [100, 50])

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


    apple_x = int(round(random.randrange(0, disp_width -35-35) / 10.0) * 10.0)
    apple_y = int(round(random.randrange(0, disp_height-35 - 35) / 10.0) * 10.0)


    game_over=False


    while game_over==False:
        
        disp.blit(pygame.image.load("fon.png"), ( 0,0 ) )
        
    
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
        
        
        snake_x += snake_x_t
        snake_y += snake_y_t

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake.append(snake_head)
        
        if len(snake) > snake_length:
            del snake[0]
 
 
        snake_draw(snake,snake_tex,body_tex)
        print_score(score)
        disp.blit(apple_red_tex,[apple_x,apple_y])

        if ((0<=(snake_x -apple_x)<35) or (0<=(apple_x -snake_x)<35)) and ((0<=(snake_y - apple_y)<35) or (0<=(apple_y -snake_y)<35)):
            apple_x = int(round(random.randrange(0, disp_width - 35-35) / 10.0) * 10.0)
            apple_y = int(round(random.randrange(0, disp_height - 35-35) / 10.0) * 10.0)
            snake_length+= 1
            score+= 1
        
        pygame.display.update()
        clock.tick(15)

    pygame.quit()
    quit()
gameLoop()