import pygame

from engine import *

pygame.init()

image = pygame.image.load("chicken.jpg")
image = pygame.transform.scale(image, (80, 80))

class Chicken(Entity):
	def __init__(self, world):
		super().__init__(world)
		self.x = 140
		self.y = 140

	def update(self, deltaTime):
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			self.x -= 0.5 * deltaTime
		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.x += 0.5 * deltaTime

	def draw(self, screen):
		screen.blit(image, (self.x, self.y))

	def onEvent(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			if event.pos[0] > self.x and event.pos[1] > self.y and event.pos[0] < self.x + image.get_width() and event.pos[1] < self.y + image.get_height():
				Egg(self.world, x = self.x + image.get_width() / 2, y = self.y + image.get_height(), vx = 0.1, vy = -0.3)

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

		if not self.world.is_on_screen(self.x - image.get_width(), self.y - image.get_height(), self.x + image.get_width(), self.y + image.get_height()):
			self.remove()

	def draw(self, screen):
		pygame.draw.circle(screen, 0x37e50e, (self.x, self.y), 20)

world = World()
chicken = Chicken(world)
world.run()

