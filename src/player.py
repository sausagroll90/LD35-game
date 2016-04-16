import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(280, 280, 40, 40)
        self.lzone = pygame.Rect(200, 280, 40, 40)
        self.rzone = pygame.Rect(360, 280, 40, 40)
        self.tzone = pygame.Rect(280, 200, 40, 40)
        self.bzone = pygame.Rect(280, 360, 40, 40)
        self.zones = [self.lzone, self.rzone, self.tzone, self.bzone]
        self.score = 0

    def left(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.lzone):
                self.score += 40 - round(abs(200 - enemy.x))
                enemies.remove(enemy)
                break
        else:
            self.score -= 100
        return enemies

    def right(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.rzone):
                self.score += 40 - round(abs(360 - enemy.x))
                enemies.remove(enemy)
                break
        else:
            self.score -= 100
        return enemies

    def up(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.tzone):
                self.score += 40 - round(abs(200 - enemy.y))
                enemies.remove(enemy)
                break
        else:
            self.score -= 100
        return enemies

    def down(self, enemies):
        for enemy in enemies:
            if enemy.rect.colliderect(self.bzone):
                self.score += 40 - round(abs(360 - enemy.y))
                enemies.remove(enemy)
                break
        else:
            self.score -= 100
        return enemies

    def update(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                return "game over"
                break
        else:
            return True

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        for zone in self.zones:
            pygame.draw.rect(screen, (255, 255, 255), zone, 2)