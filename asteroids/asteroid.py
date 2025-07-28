import pygame
import random
from constants import *
from circleshape import CircleShape

# Asteroid class inherits from CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw the asteroid as a white circle
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    # Update the asteroid's position based on its velocity
    def update(self, dt):
        self.position += self.velocity * dt

    # Split the asteroid into two smaller asteroids if it is larger than the min radius
    # Returns a list of new asteroids created from the split
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            self.kill()
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x + random_angle, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x - random_angle, self.position.y, new_radius)
            new_asteroid1.velocity = velocity1
            new_asteroid2.velocity = velocity2
            return [new_asteroid1, new_asteroid2]
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return []
