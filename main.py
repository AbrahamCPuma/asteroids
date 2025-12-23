from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import sys

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Shot.containers = (shots,updatable,drawable)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	player = Player(x, y)
	asteroidfield = AsteroidField()


	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		delta_time = clock.tick(60)
		dt = delta_time / 1000

		screen.fill("black")
		updatable.update(dt)
		
		
		for asteroid in asteroids:
			for shot in shots:
				collided = shot.collides_with(asteroid)
				if collided:
					log_event("asteroid_shot")
					asteroid.split()
					shot.kill()
			collided = player.collides_with(asteroid)
			if collided:
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		for drawing in drawable:
			drawing.draw(screen)
		pygame.display.flip()
		
		


if __name__ == "__main__":
    main()
