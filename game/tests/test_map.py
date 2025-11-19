import pytest
import pygame
from game.src.map import Map
from game.src.main import Player

@pytest.fixture
def game_map():
    obstacles = [(100, 100, 50, 200)]
    spawn_points = [(50, 50)]
    return Map("test", obstacles, spawn_points)

@pytest.fixture
def player():
    return Player()

def test_map_creation(game_map):
    assert len(game_map.obstacle_sprites) == 1

def test_player_collision(game_map, player):
    player.rect.topleft = (100, 100)
    assert pygame.sprite.spritecollideany(player, game_map.obstacle_sprites)

def test_player_no_collision(game_map, player):
    player.rect.topleft = (0, 0)
    assert not pygame.sprite.spritecollideany(player, game_map.obstacle_sprites)
