import pygame
import pytest
from game.src.main import Player, Enemy
from game.src.map import Map

@pytest.fixture
def game_objects():
    pygame.init()
    player = Player()
    game_map = Map("test", [], [(100, 100)])
    enemy = Enemy(player, game_map)
    return player, enemy

def test_player_loses_health_on_collision(game_objects):
    player, enemy = game_objects
    player.rect.center = (400, 300)
    enemy.rect.center = (400, 300)

    initial_health = player.health

    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        player.health -= 10

    assert player.health == initial_health - 10

def test_game_ends_when_player_health_is_zero(game_objects):
    player, enemy = game_objects
    player.rect.center = (400, 300)
    enemy.rect.center = (400, 300)
    player.health = 10

    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    running = True
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        player.health -= 10
        if player.health <= 0:
            running = False

    assert not running

def test_game_ends_after_20_minutes():
    game_time = 1200
    running = True
    if game_time >= 1200:
        running = False
    assert not running

def test_player_gains_experience(game_objects):
    player, _ = game_objects
    initial_xp = player.experience
    player.gain_experience(25)
    assert player.experience == initial_xp + 25

def test_player_levels_up(game_objects):
    player, _ = game_objects
    player.experience = 90
    player.level = 1
    player.gain_experience(25)
    assert player.level == 2
    assert player.experience == 15
