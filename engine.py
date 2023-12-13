import sys

import pygame

pygame.init()

class World:
	def __init__(self, width: int, height: int):
		self.screen = pygame.display.set_mode((width, height))
		self.entities: list[Entity] = []

	def run(self):
		"""
		Runs the game loop. This function never returns, unless an exception is raised.

		During any operation where the world's entities are iterated over, added entities *may* be
		processed during the iteration and removed entities *may* cause other entities to be
		skipped during the iteration.

		The game loop runs at 60 FPS. Every frame proceeds as follows:
		- pygame is polled for events. Any event received is broadcast to every entity in the world.
		- `Entity.update` is called for each entity in the world.
		- The screen is cleared with black
		- `Entity.draw` is called for each entity in the world.
		- The screen is flipped, making the current frame visible
		- The clock is ticked, synchronizing the game loop to 60 FPS.
		"""

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
	def __init__(self, world: World):
		"""
		Initializes the entity and spawns it in the world.
		"""
		self.world = world
		self.world.entities.append(self)
		print(f'spawned {self}')

	def update(self, deltaTime: float):
		"""
		Called on every frame to update the entity's state and process its interactions with the world.
		"""
		pass

	def draw(self, screen: pygame.Surface):
		"""
		Called on every frame to draw the entity to the screen.
		"""
		pass

	def onEvent(self, event):
		"""
		Called for every event emitted by pygame. Things like keyboard input, mouse buttons, etc.
		"""
		pass

	def remove(self):
		"""
		Removes the entity from the world.
		"""
		self.world.entities.remove(self)
		print(f'removed {self}')
	
	def __str__(self):
		return f'{type(self).__name__}[id={id(self)}]'
