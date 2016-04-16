import pygame
import src.enemy

class Gameloop:
	def __init__(self, screen, done, clock, player, spawns):
		self.screen = screen
		self.done = done
		self.clock = clock
		self.player = player
		self.spawns = spawns
		self.enemies = []
		self.dt = 16
		self.counter = 0

	def handle_keypress(self, key):
		if key == pygame.K_LEFT:
			self.enemies = self.player.left(self.enemies)
		if key == pygame.K_RIGHT:
			self.enemies = self.player.right(self.enemies)
		if key == pygame.K_UP:
			self.enemies = self.player.up(self.enemies)
		if key == pygame.K_DOWN:
			self.enemies = self.player.down(self.enemies)

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True
			if event.type == pygame.KEYDOWN:
				self.handle_keypress(event.key)

	def do_updates(self):
		for enemy in self.enemies:
			enemy.update(self.dt)
		self.counter += self.dt / 1000
		for spawn in self.spawns:
			if self.counter > spawn[0]:
				self.enemies.append(spawn[1])
				self.spawns.remove(spawn)

	def draw_to_screen(self):
		self.screen.fill((255, 255, 255))
		self.player.draw(self.screen)
		for enemy in self.enemies:
			enemy.draw(self.screen)
		pygame.display.flip()

	def main_loop(self):
		while not self.done:
			self.handle_events()
			self.do_updates()
			self.draw_to_screen()
			self.dt = self.clock.tick(60)