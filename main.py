import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Big Testy Game")

#------colors
WHITE = (255,255,255)

FPS= 60
#-----spaceship assets
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55,40))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (55,40))


def draw_windows():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_windows()
    
       
                
    pygame.quit()


if __name__=="__main__":
    main()