import pygame
import pytest
from game.src.main import Player, Enemy
from game.src.map import Map

@pytest.fixture
def game_objects():
    pygame.init()
    player = Player()
    game_map = Map("test", [], [(0,0)])
    enemy = Enemy(player, game_map)
    return player, enemy, game_map

def test_enemy_moves_towards_player(game_objects):
    player, enemy, game_map = game_objects
    player.rect.center = (400, 300)
    enemy.rect.center = (0, 0)

    initial_dx = player.rect.x - enemy.rect.x
    initial_dy = player.rect.y - enemy.rect.y
    initial_dist = (initial_dx**2 + initial_dy**2)**0.5

    enemy.update(game_map.obstacle_sprites)

    final_dx = player.rect.x - enemy.rect.x
    final_dy = player.rect.y - enemy.rect.y
    final_dist = (final_dx**2 + final_dy**2)**0.5

    assert final_dist < initial_dist
