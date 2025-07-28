import pygame
from constants import *
from circleshape import CircleShape

class Shot (CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, *groups, radius=SHOT_RADIUS, velocity=pygame.Vector2(0, 1).rotate(0) * PLAYER_SHOOT_SPEED):
        pygame.sprite.Sprite.__init__(self, *groups)
        CircleShape.__init__(self, x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        self.position += self.velocity * dt