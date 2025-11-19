import pygame
from game.src.enemy import Enemy

class Boss(Enemy):
    def __init__(self, player):
        super().__init__(player)
        self.image = pygame.Surface([100, 100])
        self.image.fill((255, 165, 0))  # Orange
        self.rect = self.image.get_rect()
        self.health = 500
        self.speed = 1
