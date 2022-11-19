import sys, pygame
from player import Player
from graphics import Animator

pygame.init()

size = width, height = 640, 480

background = pygame.image.load("GameZone/Medium Fat Cat 0.png")

screen = pygame.display.set_mode(size)
player = Player(1, pygame.Rect(50, 50, 40 ,40))
clock = pygame.time.Clock()
playerAnimator = Animator(player.getRect())

while 1:
    # Sets frame rate
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            player.getKey(event, True)
        if event.type == pygame.KEYUP:
            player.getKey(event, False)

    player.move()

    screen.blit(background, (0, 0))
    playerAnimator.cycleGifs(screen)
   
    pygame.display.flip()
