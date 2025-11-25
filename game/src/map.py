import pygame

class Map:
    """
    Represents a game map with layout, obstacles, and spawn points.

    Attributes:
        layout (str): The layout identifier or description of the map.
        obstacles (list[tuple]): A list of tuples defining obstacle rectangles (x, y, width, height).
        spawn_points (list[tuple]): A list of (x, y) coordinates for enemy spawning.
        obstacle_sprites (pygame.sprite.Group): A sprite group containing all obstacle sprites.
    """

    def __init__(self, layout, obstacles, spawn_points):
        """
        Initializes the Map with layout, obstacles, and spawn points.

        Args:
            layout (str): The layout identifier of the map.
            obstacles (list[tuple]): A list of tuples defining obstacles (x, y, width, height).
            spawn_points (list[tuple]): A list of (x, y) tuples for enemy spawn locations.
        """
        self.layout = layout
        self.obstacles = obstacles
        self.spawn_points = spawn_points
        self.obstacle_sprites = pygame.sprite.Group()
        self._create_obstacles()

    def _create_obstacles(self):
        """
        Creates sprite objects for all obstacles defined in the map.

        Populates the self.obstacle_sprites group with sprites representing
        the obstacles.
        """
        for obstacle_rect in self.obstacles:
            obstacle = pygame.sprite.Sprite()
            obstacle.rect = pygame.Rect(obstacle_rect)
            self.obstacle_sprites.add(obstacle)

    def draw(self, surface):
        """
        Draws the map background and obstacles onto the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the map on.
        """
        surface.fill((34, 139, 34))  # Forest green for now
        self.obstacle_sprites.draw(surface)
