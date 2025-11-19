UPGRADES = {
    "health": lambda p: setattr(p, 'max_health', p.max_health + 25),
    "speed": lambda p: setattr(p, 'speed', p.speed + 1),
    "firerate": lambda p: setattr(p, 'shoot_delay', max(50, p.shoot_delay - 25))
}
