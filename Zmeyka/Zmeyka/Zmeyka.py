import pygame
pygame.init()
disp=pygame.display.set_mode((1200,900))
 
pygame.display.set_caption('Zmeyka')
 
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)


game_over=False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.circle(disp,green,[500,500],15)
    pygame.display.update()
pygame.quit()
quit()