import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Big Testy Game")

#------colors
WHITE = (255,255,255)

FPS= 60
SHIP_SPEED=5
#-----spaceship assets
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
#-----yellow spaceship
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90  )
#---- red spaceship
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)


def draw_windows(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

def yellow_player_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= SHIP_SPEED
    if keys_pressed[pygame.K_d]:
        yellow.x += SHIP_SPEED
    if keys_pressed[pygame.K_s]:
            yellow.y += SHIP_SPEED
    if keys_pressed[pygame.K_w]:
            yellow.y -= SHIP_SPEED
        
    
    
    pygame.display.update() 

def main():
    red= pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow= pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        yellow_player_movement(keys_pressed, yellow)

        
        draw_windows(red, yellow)
        #-----movement for yellow ship
        
       
                
    pygame.quit()


if __name__=="__main__":
    main()