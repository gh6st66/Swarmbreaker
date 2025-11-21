from game.src.map import Map

class CursedGroveMap(Map):
    """
    A specific map implementation representing the 'Cursed Grove'.

    Inherits from the base Map class and defines a specific layout of obstacles
    and spawn points.
    """

    def __init__(self):
        """
        Initializes the Cursed Grove map with predefined obstacles and spawn points.
        """
        layout = "maze"  # As described in the user's vision
        obstacles = [
            (100, 100, 50, 200),  # x, y, width, height
            (300, 200, 50, 200),
            (500, 100, 50, 200),
            (700, 200, 50, 200),
        ]
        spawn_points = [
            (50, 50),
            (750, 50),
            (50, 550),
            (750, 550),
        ]
        super().__init__(layout, obstacles, spawn_points)

    def draw(self, surface):
        """
        Draws the Cursed Grove map background and obstacles.

        Args:
            surface (pygame.Surface): The surface to draw the map on.
        """
        surface.fill((1, 50, 32))  # Dark green for the Cursed Grove
        # In the future, we can draw more detailed visuals here
        self.obstacle_sprites.draw(surface)
