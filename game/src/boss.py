import pygame
from game.src.enemy import Enemy

class Boss(Enemy):
    """
    Represents a Boss enemy, which is a stronger variant of a standard Enemy.

    Inherits from Enemy.

    Attributes:
        image (pygame.Surface): The visual representation of the boss.
        rect (pygame.Rect): The bounding rectangle of the boss.
        health (int): The health points of the boss.
        speed (int): The movement speed of the boss.
    """

    def __init__(self, player):
        """
        Initializes the Boss enemy.

        Args:
            player (Player): The player instance the boss targets.
        """
        super().__init__(player)
        self.image = pygame.Surface([100, 100])
        self.image.fill((255, 165, 0))  # Orange
        self.rect = self.image.get_rect()
        self.health = 500
        self.speed = 1
