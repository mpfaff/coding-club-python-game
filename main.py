from math import sqrt, atan

import pygame

from engine import *

world = World(1600, 1200)

chicken_image = pygame.image.load("chicken.png").convert_alpha()
chicken_image = pygame.transform.smoothscale(chicken_image, (120, 120))

egg_image = pygame.image.load("egg.png").convert_alpha()
egg_image = pygame.transform.smoothscale(egg_image, (40, 40))

class Chicken(Entity):
	def __init__(self, world):
		super().__init__(world)
		self.x = 140
		self.y = 140
		self.shooting = False

	def update(self, deltaTime):
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			self.x -= 0.5 * deltaTime
		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.x += 0.5 * deltaTime

	def draw(self, screen):
		screen.blit(chicken_image, (self.x, self.y))

	def onEvent(self, event):
		if self.shooting:
			if event.type == pygame.MOUSEBUTTONUP:
				self.shooting = False
				pos1 = event.pos
				pos2 = self.pos2
				self.pos2 = None
				vec = (pos2[0] - pos1[0], pos2[1] - pos1[1])
				velocity = (vec[0] * 0.01, vec[1] * 0.01)
				Egg(self.world, x = self.x + chicken_image.get_width() / 2, y = self.y + chicken_image.get_height() / 2, vx = velocity[0], vy = velocity[1])
		else:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.pos[0] > self.x and event.pos[1] > self.y and event.pos[0] < self.x + chicken_image.get_width() and event.pos[1] < self.y + chicken_image.get_height():
					self.shooting = True
					self.pos2 = event.pos

class Egg(Entity):
	def __init__(self, world, x, y, vx, vy):
		super().__init__(world)
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def update(self, deltaTime):
		self.x += self.vx * deltaTime
		self.y += self.vy * deltaTime
		self.vy += 0.05

		if self.__is_off_screen_forever():
			self.remove()

	def draw(self, screen):
		screen.blit(egg_image, (self.x, self.y))

	def __is_off_screen_forever(self):
		minX = self.x
		minY = self.y
		maxX = self.x + egg_image.get_width()
		maxY = self.y + egg_image.get_height()
		if minX > self.world.screen.get_width() or maxX < 0:
			return True
		# maxY < 0 is left out because gravity will bring it back down
		if minY > self.world.screen.get_height():
			return True
		return False

chicken = Chicken(world)
world.run()

