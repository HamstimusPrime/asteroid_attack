# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode(size = (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # type: ignore
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    AsteroidField.containers = (updatable,) # type: ignore
    asteroid_field = AsteroidField()

    Shot.containers = (shots_group, updatable, drawable) # type: ignore
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable_object in updatable:
            updatable_object.update(dt)
        
        for asteroid_object in asteroids:
            if asteroid_object.get_collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots_group:
                if asteroid_object.get_collision(bullet):
                    bullet.kill()
                    asteroid_object.split()
                    

        screen.fill("black")
        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()
        

        dt = clock_object.tick(60) / 1000
        




if __name__ == "__main__":
    main()