import pygame
from game.src.constants import PLAYER_SIZE, PLAYER_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from game.src.upgrades import UPGRADES
from game.src.bullet import Bullet
import random

class Player(pygame.sprite.Sprite):
    """
    Represents the player character in the game.

    Handles movement, shooting, leveling up, and health management.

    Attributes:
        image (pygame.Surface): The visual representation of the player.
        rect (pygame.Rect): The bounding rectangle of the player.
        speed (int): The movement speed of the player.
        max_health (int): The maximum health of the player.
        health (float): The current health of the player.
        shoot_delay (int): The time in milliseconds between shots.
        experience (int): The current accumulated experience points.
        level (int): The current player level.
        last_shot (int): The timestamp of the last shot fired.
        all_sprites (pygame.sprite.Group): Reference to the group containing all sprites.
        bullets (pygame.sprite.Group): Reference to the group containing bullet sprites.
    """

    def __init__(self, all_sprites, bullets):
        """
        Initializes the player.

        Args:
            all_sprites (pygame.sprite.Group): The group to add created bullets to.
            bullets (pygame.sprite.Group): The specific group for bullets.
        """
        super().__init__()
        self.image = pygame.Surface([PLAYER_SIZE, PLAYER_SIZE])
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Base Stats
        self.speed = 5
        self.max_health = 100
        self.health = self.max_health
        self.shoot_delay = 250

        # Leveling
        self.experience = 0
        self.level = 1

        self.last_shot = pygame.time.get_ticks()

        self.all_sprites = all_sprites
        self.bullets = bullets

    def update(self):
        """
        Updates the player's state.

        Handles keyboard input for movement and calls the shoot method.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.shoot()

    def shoot(self):
        """
        Fires a bullet if the cooldown has passed.

        Creates a new Bullet instance and adds it to the sprite groups.
        """
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)

    def gain_experience(self, amount):
        """
        Adds experience points to the player.

        Checks if the player has enough experience to level up.

        Args:
            amount (int): The amount of experience to add.
        """
        self.experience += amount
        while self.experience >= self.level * 100:
            xp_needed = self.level * 100
            self.experience -= xp_needed
            self.level_up()

    def level_up(self):
        """
        Levels up the player and applies a random upgrade.

        Increments the level and selects a random upgrade from the UPGRADES list.
        """
        self.level += 1
        upgrade = random.choice(list(UPGRADES.keys()))
        UPGRADES[upgrade](self)
        print(f"Player leveled up to level {self.level}! Upgraded {upgrade}.")
