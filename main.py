# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from shot import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS
    clock = pygame.time.Clock()
    dt = 0


    # Grupos
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
 
    #registro dos containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Jogador
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Asteróide
    asteroidfield = AsteroidField()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
         # update antes da checagem de colisão
        for obj in updatable:
            obj.update(dt)

        # colisão: apenas asteroides vs player
        for rock in asteroids:
            if rock.collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if rock.collision(bullet):
                    rock.split()
                    bullet.kill()
        
            

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
