import pygame

class Player:
    speed: int = 4
    direction: list[int] = [0,0]
    rect: pygame.Rect

    def __init__(self, num: int, rect: pygame.Rect):
        self.num = num
        self.rect = rect
        self.dir_moving = {"up": False, "down": False, "left": False, "right": False}

    def move(self) -> None:
        dir = self.direction
        if((self.dir_moving["up"] or self.dir_moving["down"]) and (self.dir_moving["left"] or self.dir_moving["right"])):
            dir = [dir[0] / 2, dir[1] / 2]
        
        self.rect.y += dir[0]
        self.rect.x += dir[1]

    def getKey(self, key: pygame.event.Event, pressed: bool) -> None:
        move: int = self.speed
        if not pressed:
            move = -1 * move
        if key.key == pygame.K_w:
            self.direction[0] -= move
        if key.key == pygame.K_s:
            self.direction[0] += move
        if key.key == pygame.K_a:
            self.direction[1] -= move
        if key.key == pygame.K_d:
            self.direction[1] += move

    def getRect(self) -> pygame.Rect:
        return self.rect