 # this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from shot import *
from asteroid import *
from asteroidfield import *

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
        for ast in asteroids:
            for sho in shots:
                if ast.collision(sho):
                    ast.split()
                    sho.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()