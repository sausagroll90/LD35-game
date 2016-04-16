import pygame
import src.enemy
import random

class Gameloop:
	def __init__(self, screen, done, clock, player, spawnslist, font):
		self.screen = screen
		self.done = done
		self.clock = clock
		self.player = player
		self.spawnslist = spawnslist
		self.spawns = spawnslist[0]
		self.enemies = []
		self.dt = 16
		self.overalltime = 0
		self.counter = 0
		self.statestack = []
		self.font = font

	def game_over_state(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = True
		if pygame.key.get_pressed()[pygame.K_SPACE]:
			self.statestack = []
			self.overalltime = 0
			self.counter = 0
			self.overalltime = 0
			self.enemies = []
			self.spawns = []
			for spawn in self.spawnslist[0]:
				self.spawns.append(spawn)
		text = self.font.render("Your score:   Press space to restart", False, (255, 255, 255))
		self.screen.fill((0, 0, 0))
		self.screen.blit(text, (100, 290))
		pygame.display.flip()

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
			enemy.update(self.dt, self.overalltime)
		self.counter += self.dt / 1000
		self.overalltime += self.dt / 1000
		for spawn in self.spawns:
			if self.counter > spawn[0]:
				self.enemies.append(src.enemy.Enemy(spawn[1]))
				self.spawns.remove(spawn)
		if self.player.update(self.enemies) == "game over":
			self.enemies = []
			self.statestack.append(self.game_over_state)
		if len(self.spawns) == 0:
			self.counter = 0
			random.seed()
			select = random.randint(0, 2)
			for i in self.spawnslist[select]:
				self.spawns.append(i)

	def draw_to_screen(self):
		self.screen.fill((0, 0, 0))
		self.player.draw(self.screen)
		for enemy in self.enemies:
			enemy.draw(self.screen)
		pygame.display.flip()

	def main_state(self):
		self.handle_events()
		self.do_updates()
		self.draw_to_screen()
		self.dt = self.clock.tick(60)

	def run_current_state(self):
		while not self.done:
			print(len(self.enemies))
			if len(self.statestack) == 0:
				self.statestack.append(self.main_state)
			self.statestack[-1]()