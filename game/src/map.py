import pygame

class Map:
    def __init__(self, layout, obstacles, spawn_points):
        self.layout = layout
        self.obstacles = obstacles
        self.spawn_points = spawn_points
        self.obstacle_sprites = pygame.sprite.Group()
        self._create_obstacles()

    def _create_obstacles(self):
        for obstacle_rect in self.obstacles:
            obstacle = pygame.sprite.Sprite()
            obstacle.rect = pygame.Rect(obstacle_rect)
            self.obstacle_sprites.add(obstacle)

    def draw(self, surface):
        surface.fill((34, 139, 34))  # Forest green for now
        self.obstacle_sprites.draw(surface)
