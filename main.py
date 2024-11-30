# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from a module
# into the current file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if object.col_dect(player):
                print("Game Over!")
                return
            for bullet in shots:
                if object.col_dect(bullet):
                    object.kill()
                    bullet.kill()
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()