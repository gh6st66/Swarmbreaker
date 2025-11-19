import pytest
from game.src.main import Player, UPGRADES

@pytest.fixture
def player():
    return Player()

def test_health_upgrade(player):
    initial_max_health = player.max_health
    UPGRADES["health"](player)
    assert player.max_health == initial_max_health + 25

def test_speed_upgrade(player):
    initial_speed = player.speed
    UPGRADES["speed"](player)
    assert player.speed == initial_speed + 1

def test_firerate_upgrade(player):
    initial_firerate = player.shoot_delay
    UPGRADES["firerate"](player)
    assert player.shoot_delay == initial_firerate - 25
