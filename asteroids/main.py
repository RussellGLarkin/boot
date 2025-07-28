import pygame
import sys
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    # Initialize pygame and create the main window
    pygame.init()

    # Create sprite groups for different types of game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up the containers for the sprite classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()

    # Create the main screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set the clock for controlling the frame rate
    clock = pygame.time.Clock()
    dt = 0

    # Create the player object at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over!")
                sys.exit(0)
        for shot in shots:
            for asteroid in asteroids:
                if shot.collisions(asteroid):
                    shot.kill()
                    new_asteroids = asteroid.split()
                    for new_asteroid in new_asteroids:
                        asteroids.add(new_asteroid)
                    break
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
