import pygame

class ExperienceOrb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill((0, 255, 0)) # Green
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
