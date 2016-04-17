import pygame
import src.particle

class Player:
    def __init__(self, red, pimg, hit, miss, fail):
        self.rect = pygame.Rect(280, 280, 40, 40)
        self.lzone = pygame.Rect(200, 280, 40, 40)
        self.rzone = pygame.Rect(360, 280, 40, 40)
        self.tzone = pygame.Rect(280, 200, 40, 40)
        self.bzone = pygame.Rect(280, 360, 40, 40)
        self.zones = [self.lzone, self.rzone, self.tzone, self.bzone]
        self.score = 0
        self.red = red
        self.redalpha = 0
        self.pimg = pimg
        self.particles = []
        self.hitsound = hit
        self.misssound = miss
        self.failsound = fail

    def left(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.lzone):
                self.score += 40 - round(abs(200 - enemy.x))
                enemies.remove(enemy)
                for i in range(15):
                    self.particles.append(src.particle.Particle(215, 295, self.pimg))
                self.hitsound.play()
                break
        else:
            self.score -= 100
            self.redalpha = 200
            self.misssound.play()
        return enemies

    def right(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.rzone):
                self.score += 40 - round(abs(360 - enemy.x))
                enemies.remove(enemy)
                for i in range(15):
                    self.particles.append(src.particle.Particle(365, 295, self.pimg))
                self.hitsound.play()
                break
        else:
            self.score -= 100
            self.redalpha = 200
            self.misssound.play()
        return enemies

    def up(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.tzone):
                self.score += 40 - round(abs(200 - enemy.y))
                enemies.remove(enemy)
                for i in range(15):
                    self.particles.append(src.particle.Particle(295, 215, self.pimg))
                self.hitsound.play()
                break
        else:
            self.score -= 100
            self.redalpha = 200
            self.misssound.play()
        return enemies

    def down(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.bzone):
                self.score += 40 - round(abs(360 - enemy.y))
                enemies.remove(enemy)
                for i in range(15):
                    self.particles.append(src.particle.Particle(295, 365, self.pimg))
                self.hitsound.play()
                break
        else:
            self.score -= 100
            self.redalpha = 200
            self.misssound.play()
        return enemies

    def update(self, enemies, dt):
        if self.redalpha > 0:
            self.redalpha -= dt * 1.5
        if self.redalpha < 0:
            self.redalpha = 0
        self.red.set_alpha(self.redalpha)
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                self.failsound.play()
                return "game over"
                break
        else:
            return True

    def draw(self, screen, dt):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        for zone in self.zones:
            pygame.draw.rect(screen, (255, 255, 255), zone, 2)
        for particle in self.particles:
            particle.update(dt)
            particle.draw(screen)
        screen.blit(self.red, (0, 0))