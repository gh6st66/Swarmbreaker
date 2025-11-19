import pygame
import pytest
from game.src.main import Player

@pytest.fixture
def player():
    pygame.init()
    return Player()

def test_player_moves_left(player, mocker):
    keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False}
    mocker.patch('pygame.key.get_pressed', return_value=keys)
    initial_x = player.rect.x
    player.update(pygame.sprite.Group())
    assert player.rect.x == initial_x - player.speed

def test_player_moves_right(player, mocker):
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_UP: False, pygame.K_DOWN: False}
    mocker.patch('pygame.key.get_pressed', return_value=keys)
    initial_x = player.rect.x
    player.update(pygame.sprite.Group())
    assert player.rect.x == initial_x + player.speed

def test_player_moves_up(player, mocker):
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: True, pygame.K_DOWN: False}
    mocker.patch('pygame.key.get_pressed', return_value=keys)
    initial_y = player.rect.y
    player.update(pygame.sprite.Group())
    assert player.rect.y == initial_y - player.speed

def test_player_moves_down(player, mocker):
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: True}
    mocker.patch('pygame.key.get_pressed', return_value=keys)
    initial_y = player.rect.y
    player.update(pygame.sprite.Group())
    assert player.rect.y == initial_y + player.speed
