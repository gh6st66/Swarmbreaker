import pygame
import random
from game.src.maps.cursed_grove import CursedGroveMap

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
PLAYER_COLOR = (0, 128, 255)  # Blue

# --- Upgrade Definitions ---
UPGRADES = {
    "health": lambda p: setattr(p, 'max_health', p.max_health + 25),
    "speed": lambda p: setattr(p, 'speed', p.speed + 1),
    "firerate": lambda p: setattr(p, 'shoot_delay', max(50, p.shoot_delay - 25))
}

# --- Player Class ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
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

    def update(self, obstacles):
        original_pos = self.rect.copy()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Check for collisions with obstacles
        if pygame.sprite.spritecollide(self, obstacles, False):
            self.rect = original_pos

        self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

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

# --- Bullet Class ---
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 0)) # Yellow
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self, *args, **kwargs):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# --- ExperienceOrb Class ---
class ExperienceOrb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill((0, 255, 0)) # Green
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, *args, **kwargs):
        pass

# --- Enemy Class ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, game_map):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect()
        self.player = player
        self.game_map = game_map

        # Spawn at a random spawn point from the map
        self.rect.center = random.choice(self.game_map.spawn_points)

        self.speed = 2

    def update(self, obstacles):
        original_pos = self.rect.copy()

        # Move towards the player
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        dist = (dx**2 + dy**2)**0.5
        if dist != 0:
            self.rect.x += self.speed * dx / dist
            self.rect.y += self.speed * dy / dist

        if pygame.sprite.spritecollide(self, obstacles, False):
            self.rect = original_pos

# --- Game Setup ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multiplayer Survivor Game")
all_sprites = pygame.sprite.Group()
game_map = CursedGroveMap()

player = Player()
all_sprites.add(player)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
experience_orbs = pygame.sprite.Group()
clock = pygame.time.Clock()
game_time = 0
# Arena
ARENA_DAMAGE = 5
arena_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

WAVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(WAVE_EVENT, 5000) # 5 seconds
wave_number = 1
# --- Game Loop ---
def main():
    global wave_number, game_time, arena_rect
    running = True
    last_time = pygame.time.get_ticks()
    while running:
        now = pygame.time.get_ticks()
        dt = (now - last_time) / 1000.0
        last_time = now
        game_time += dt
        if game_time >= 1200: # 20 minutes
            running = False
        # Arena Shrinking
        shrink_factor = 1.0 - (game_time / 1200.0)
        arena_width = SCREEN_WIDTH * shrink_factor
        arena_height = SCREEN_HEIGHT * shrink_factor
        arena_rect.width = max(50, arena_width)
        arena_rect.height = max(50, arena_height)
        arena_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == WAVE_EVENT:
                for _ in range(wave_number * 2): # Increase enemies each wave
                    enemy = Enemy(player, game_map)
                    all_sprites.add(enemy)
                    enemies.add(enemy)
                wave_number += 1

        # --- Update ---
        all_sprites.update()
        # --- Collision Detection ---
        # Arena Damage
        if not arena_rect.contains(player.rect):
            player.health -= ARENA_DAMAGE * dt
            if player.health <= 0:
                running = False
        # Player <> Enemies
        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            player.health -= 10
            print(f"Player health: {player.health}")
            if player.health <= 0:
                running = False

        # Bullets <> Enemies
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            orb = ExperienceOrb(hit.rect.centerx, hit.rect.centery)
            all_sprites.add(orb)
            experience_orbs.add(orb)

        # Player <> Experience Orbs
        hits = pygame.sprite.spritecollide(player, experience_orbs, True)
        for hit in hits:
            player.gain_experience(25)

        # --- Draw ---
        screen.fill((0, 0, 0))  # Black background
        pygame.draw.rect(screen, (100, 100, 100), arena_rect, 2) # Draw arena border
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
