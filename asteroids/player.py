import pygame
from shot import Shot
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), points, width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # when the player shoots, set the timer equal to player shoot cooldown
    # and then call the shoot method
    def update_shoot_timer(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        else:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            self.shoot()

    def shoot(self):
        shot_position = self.position + pygame.Vector2(0, 1).rotate(self.rotation) * self.radius
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        _shot = Shot(shot_position.x, shot_position.y, *Shot.containers, velocity=shot_velocity)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.update_shoot_timer(dt)