import pygame
pygame.init()
disp=pygame.display.set_mode((1200,900))
 
pygame.display.set_caption('Zmeyka')
 
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
x_snake = 300
y_snake = 300
 
x_snake_change = 0       
y_snake_change = 0
 
clock = pygame.time.Clock()

game_over=False

while not game_over:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_snake_change = -10
                y_snake_change = 0
            elif event.key == pygame.K_RIGHT:
                x_snake_change = 10
                y_snake_change = 0
            elif event.key == pygame.K_UP:
                y_snake_change = -10
                x_snake_change = 0
            elif event.key == pygame.K_DOWN:
                y_snake_change = 10
                x_snake_change = 0
 
    x_snake += x_snake_change
    y_snake += y_snake_change
    disp.blit(pygame.image.load("fon.png"), ( 0,0 ) )
    pygame.draw.circle(disp,green,[x_snake,y_snake],15)
    
    pygame.display.update()
pygame.quit()
quit()