from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        position = self.position
        radius = self.radius
        velocity = self.velocity

        if radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20,50)
            v1 = velocity.rotate(angle)
            v2 = velocity.rotate(-angle)
            new_radius = radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(position.x, position.y, new_radius)
            asteroid1.velocity = v1
            asteroid2 = Asteroid(position.x, position.y, new_radius)
            asteroid2.velocity = v2
        self.kill()
