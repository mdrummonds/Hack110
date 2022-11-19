import pygame 
import random

class Foods:
    rect: pygame.Rect
    color: tuple
    is_yummy: bool

    def __init__(self, rect, is_yummy: float) -> None:
        self.rect = rect
        if is_yummy > 0.5:
            self.color = (0, 0, 255)
        else:
            self.color = (255, 0, 0)

    def fall(self):
        self.rect.move_ip(0, 1)
        if self.rect.bottom >= 600:
            self.rect.bottom = random.randint(-1000, 0)
            self.rect.x = random.randint(0, 720)


class Player:
    rect: pygame.Rect
    color: tuple

    def __init__(self, rect) -> None:
        self.rect = rect
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def update(self) -> None:
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 720:
            self.rect.right = 720


def main():
    screen = width, height = 720, 600
    display = pygame.display.set_mode(screen)

    clock = pygame.time.Clock()
    pygame.init()

    player = Player(pygame.Rect(360,550,20,20))

    foods = [Foods(pygame.Rect(random.randint(0, 720), random.randint(-1000, 0), 20, 20), random.random()) for i in range(100)]

    while 1:
        display.fill((255,255,255))
        clock.tick(88)
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
                pygame.quit()
            pygame.draw.rect(display, i.color, i.rect)

        pygame.draw.rect(display, player.color, player.rect)
        pygame.display.update()


if __name__ == "__main__":
    main()