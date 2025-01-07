import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        
        v1 = self.velocity.rotate(rand_angle)
        v2 = self.velocity.rotate(-rand_angle)
        
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, newRadius).velocity = 1.2 * v1
        Asteroid(self.position.x, self.position.y, newRadius).velocity = 1.2 * v2