import pygame
import pytest
from game.src.main import Player, Enemy

@pytest.fixture
def game_objects():
    pygame.init()
    player = Player()
    enemy = Enemy(player)
    return player, enemy

def test_enemy_moves_towards_player(game_objects):
    player, enemy = game_objects
    player.rect.center = (400, 300)
    enemy.rect.center = (0, 0)

    initial_dx = player.rect.x - enemy.rect.x
    initial_dy = player.rect.y - enemy.rect.y
    initial_dist = (initial_dx**2 + initial_dy**2)**0.5

    enemy.update()

    final_dx = player.rect.x - enemy.rect.x
    final_dy = player.rect.y - enemy.rect.y
    final_dist = (final_dx**2 + final_dy**2)**0.5

    assert final_dist < initial_dist
