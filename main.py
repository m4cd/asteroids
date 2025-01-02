
import pygame
from constants import *
from player import*
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for u in updatable:
            u.update(dt)

        screen.fill(color=(0,0,0))
        
        for d in drawable:
            d.draw(screen)
        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()