import pygame

class Bullet(pygame.sprite.Sprite):
    """
    Represents a projectile fired by the player.

    Attributes:
        image (pygame.Surface): The visual representation of the bullet.
        rect (pygame.Rect): The bounding rectangle of the bullet.
        speed (int): The speed at which the bullet moves vertically.
    """

    def __init__(self, x, y):
        """
        Initializes a bullet at the specified position.

        Args:
            x (int): The x-coordinate of the bullet's center.
            y (int): The y-coordinate of the bullet's center.
        """
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 0)) # Yellow
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        """
        Updates the bullet's position.

        Moves the bullet upwards by its speed. If the bullet moves off-screen,
        it is removed from all sprite groups.
        """
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
