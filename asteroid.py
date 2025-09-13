from circleshape import *
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        # 4) new radius
        new_r = self.radius - ASTEROID_MIN_RADIUS

        # 5-7) spawn two asteroids at current position
        a1 = Asteroid(self.position.x, self.position.y, new_r)
        a2 = Asteroid(self.position.x, self.position.y, new_r)
        a1.velocity = v1
        a2.velocity = v2