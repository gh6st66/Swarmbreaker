import pygame
from game.src.constants import PLAYER_SIZE, PLAYER_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from game.src.upgrades import UPGRADES
from game.src.bullet import Bullet
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
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
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.level * 100:
            xp_needed = self.level * 100
            self.experience -= xp_needed
            self.level_up()

    def level_up(self):
        self.level += 1
        upgrade = random.choice(list(UPGRADES.keys()))
        UPGRADES[upgrade](self)
        print(f"Player leveled up to level {self.level}! Upgraded {upgrade}.")
