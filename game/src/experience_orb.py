import pygame

class ExperienceOrb(pygame.sprite.Sprite):
    """
    Represents an experience orb dropped by enemies.

    Attributes:
        image (pygame.Surface): The visual representation of the orb.
        rect (pygame.Rect): The bounding rectangle of the orb.
    """

    def __init__(self, x, y):
        """
        Initializes an experience orb at the specified position.

        Args:
            x (int): The x-coordinate of the orb's center.
            y (int): The y-coordinate of the orb's center.
        """
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill((0, 255, 0)) # Green
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
