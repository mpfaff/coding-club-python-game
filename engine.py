import sys

import pygame

class World:
	def __init__(self):
		self.screen = pygame.display.set_mode((800, 600))
		self.entities = []

	def run(self):
		clock = pygame.time.Clock()
		deltaTime = 0

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				else:
					for entity in self.entities:
						entity.onEvent(event)

			for entity in self.entities:
				entity.update(deltaTime)

			self.screen.fill(0x000000)

			for entity in self.entities:
				entity.draw(self.screen)

			pygame.display.flip()

			deltaTime = clock.tick(60)
	
	def is_on_screen(self, minX, minY, maxX, maxY):
		if minX > self.screen.get_width() or maxX < 0:
			return False
		if minY > self.screen.get_height() or maxY < 0:
			return False
		return True

class Entity:
	def __init__(self, world):
		"""Initializes the entity and spawns it in the world."""
		self.world = world
		self.world.entities.append(self)
		print(f'spawned {self}')

	def update(self, deltaTime):
		pass

	def draw(self, screen):
		pass

	def onEvent(self, event):
		pass

	def remove(self):
		"""Removes the entity from the world."""
		self.world.entities.remove(self)
		print(f'removed {self}')
	
	def __str__(self):
		return f'{type(self).__name__}[id={id(self)}]'
