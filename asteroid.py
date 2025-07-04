from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
        def __init__(self, x, y, radius, velocity=pygame.Vector2(0, 0)):
                super().__init__(x, y, radius)
                self.velocity = velocity


        def draw(self, screen):
                pygame.draw.circle(screen, "white", (self.position.x , self.position.y), self.radius, 2)

        def update(self, dt):
                self.position += (self.velocity * dt)

        def split(self):
                self.kill()
                if self.radius <= ASTEROID_MIN_RADIUS:
                        return
                random_angle = random.uniform(20, 50)
                velocity1 = (self.velocity.rotate(random_angle)) * 1.2
                velocity2 = (self.velocity.rotate(-random_angle)) * 1.2
                new_radius = self.radius - ASTEROID_MIN_RADIUS
                Asteroid(self.position.x, self.position.y, new_radius, velocity1)
                Asteroid(self.position.x, self.position.y, new_radius, velocity2)
