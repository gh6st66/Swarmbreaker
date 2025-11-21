import pygame
import random
from game.src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    """
    Represents a standard enemy that chases the player.

    Attributes:
        image (pygame.Surface): The visual representation of the enemy.
        rect (pygame.Rect): The bounding rectangle of the enemy.
        player (Player): The player instance this enemy targets.
        speed (int): The movement speed of the enemy.
    """

    def __init__(self, player):
        """
        Initializes the enemy.

        Spawns the enemy at a random location just outside the screen boundaries.

        Args:
            player (Player): The player instance to chase.
        """
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect()
        self.player = player

        # Spawn at a random location off-screen
        side = random.randint(1, 4)
        if side == 1: # Top
            self.rect.x = random.randint(-50, SCREEN_WIDTH + 50)
            self.rect.y = random.randint(-50, 0)
        elif side == 2: # Bottom
            self.rect.x = random.randint(-50, SCREEN_WIDTH + 50)
            self.rect.y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 50)
        elif side == 3: # Left
            self.rect.x = random.randint(-50, 0)
            self.rect.y = random.randint(-50, SCREEN_HEIGHT + 50)
        else: # Right
            self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50)
            self.rect.y = random.randint(-50, SCREEN_HEIGHT + 50)

        self.speed = 2

    def update(self):
        """
        Updates the enemy's position.

        Moves the enemy directly towards the player's current position.
        """
        # Move towards the player
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        dist = (dx**2 + dy**2)**0.5
        if dist != 0:
            self.rect.x += self.speed * dx / dist
            self.rect.y += self.speed * dy / dist
