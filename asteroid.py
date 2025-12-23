
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
	def __init__(self,x, y, radius):
		super().__init__(x, y, radius)
		
		
	def draw(self, screen):
		pygame.draw.circle(surface=screen, color="white",center=self.position, radius= self.radius, width= LINE_WIDTH)
	
	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			random_angle = random.uniform(20,50)
			v1 =self.velocity.rotate(random_angle)
			v2 =self.velocity.rotate(-random_angle)
			self.new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid = Asteroid(self.position.x, self.position.y, self.new_radius)
			asteroid2 = Asteroid(self.position.x, self.position.y, self.new_radius)
			asteroid.velocity = v1 * 1.2
			asteroid2.velocity = v2 * 1.2