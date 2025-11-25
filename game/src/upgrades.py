"""
Upgrade definitions for the player.

This module contains the available upgrades that can be applied to the player
upon leveling up.
"""

UPGRADES = {
    "health": lambda p: setattr(p, 'max_health', p.max_health + 25),
    "speed": lambda p: setattr(p, 'speed', p.speed + 1),
    "firerate": lambda p: setattr(p, 'shoot_delay', max(50, p.shoot_delay - 25))
}
"""
dict[str, callable]: A dictionary mapping upgrade names to lambda functions.

Each key is a string representing the upgrade name (e.g., 'health', 'speed').
Each value is a callable that takes a Player instance as an argument and modifies
its attributes directly.

Args:
    p (Player): The player instance to apply the upgrade to.
"""
