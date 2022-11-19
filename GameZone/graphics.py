import pygame
class Animator:
    animation_index: int
    player_rect: pygame.Rect
    index: int = 1
    time: int = 1

    def __init__(self, rect: pygame.Rect):
        self.player_rect = rect

    def cycleGifs(self, screen):
        self.time += 1
        if(self.time % 60 == 0):
            self.index += 1
            self.index = self.index % 2
        image = pygame.image.load("mediumfatcat" + str(self.index) + ".png")
        image = pygame.transform.scale(image, (40, 40))
        screen.blit(image, self.player_rect)