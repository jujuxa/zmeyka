import pygame
pygame.init()
disp_width = 1200
disp_height = 900
disp=pygame.display.set_mode((disp_width,disp_height))

pygame.display.set_caption('Zmeyka')
 
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
snake_x = 300
snake_y = 300
 
snake_x_change = 0       
snake_y_change = 0

snake_body = 10
snake_speed = 15

clock = pygame.time.Clock()

game_over=False

while not game_over:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -10
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 10
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -10
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = 10
                snake_x_change = 0
    if snake_x >= disp_width:
        snake_x = 1
    if snake_x < 0:
        snake_x = disp_width-1
    if snake_y >= disp_height:
        snake_y = 0        
    if snake_y < 0:
        snake_y = disp_height-1

    snake_x += snake_x_change
    snake_y += snake_y_change
    disp.blit(pygame.image.load("fon.png"), ( 0,0 ) )
    pygame.draw.circle(disp,green,[snake_x,snake_y],15)
    pygame.display.update()
pygame.quit()
quit()