import pygame 
import random
from GameZone.constants import *


class Player:
    rect: pygame.Rect

    def __init__(self, rect) -> None:
        self.rect = rect
    
    def update(self) -> None:
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 720:
            self.rect.right = 720
    
    def getRect(self) -> pygame.Rect:
        return self.rect


class Foods:
    rect: pygame.Rect
    color: tuple
    is_yummy: bool

    def __init__(self, rect, is_yummy: float) -> None:
        self.rect = rect
        if is_yummy > 0.5:
            self.color = (0, 0, 255)
            self.is_yummy = True
        else:
            self.color = (255, 0, 0)
            self.is_yummy = False

    def fall(self):
        self.rect.move_ip(0, random.random() * 5)
        if self.rect.bottom >= 600:
            self.rect.bottom = random.randint(-1000, 0)
            self.rect.x = random.randint(0, 720)
    

class Animator:
    animation_index: int
    player_rect: pygame.Rect
    index: int
    time: int = 1

    def __init__(self, rect: pygame.Rect):
        self.player_rect = rect

    # def cycleGifs(self, screen):
    #     self.time += 1
    #     if(self.time % 60 == 0):
    #         self.index += 1
    #         self.index = self.index % 5
    #     image = pygame.image.load("GameZone/Medium Fat Cat " + str(self.index) + ".png")
    #     image = pygame.transform.scale(image, (80, 80))
    #     screen.blit(image, self.player_rect)

    def cycleGifs(self, screen, index: int = 1):
        self.index = index
        image = pygame.image.load("GameZone/Medium Fat Cat " + str(self.index) + ".png")
        image = pygame.transform.scale(image, (80, 80))
        screen.blit(image, self.player_rect)


def main():
    size = width, height = 720, 600
    screen = pygame.display.set_mode(size)
    display = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    pygame.init()

    index: int = 1

    # background = pygame.image.load("GameZone/background.png")

    # pygame.mixer.music.load(BACKGROUND_MUSIC)
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(1)

    player = Player(pygame.Rect(360,500,20,20))
    playerAnimator = Animator(player.getRect())

    foods = [Foods(pygame.Rect(random.randint(0, 720), random.randint(-1000, 0), 20, 20), random.random()) for i in range(10)]

    while 1:
        display.fill((255,255,255))
        clock.tick(288)
        for i in pygame.event.get():
            player.update()
            if i.type == pygame.QUIT:
                pygame.quit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    player.rect.move_ip(-15, 0)
                if i.key == pygame.K_RIGHT:
                    player.rect.move_ip(15,0)

        for i in foods:
            i.fall()
            if i.rect.colliderect(player.rect):
                # pygame.mixer.music.load(SCORE_NOISE)
                # pygame.mixer.music.play(1)
                # pygame.mixer.music.set_volume(1)
                i.rect.top = 0
                #pygame.time.delay(500)
                if i.is_yummy:
                    index += 1
                else:
                    index -= 1
                #playerAnimator.cycleGifs(screen, index)
                if index > 5 or index < 0:
                    pygame.quit()
            pygame.draw.rect(display, i.color, i.rect)

        # screen.blit(background, (0, 0))
        playerAnimator.cycleGifs(screen, index)
        pygame.display.update()


if __name__ == "__main__":
    main()