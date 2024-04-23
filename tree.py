import pygame
from pygame.sprite import Sprite

class Tree(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 255, 0))  # Color verde para el árbol
        self.rect = self.image.get_rect()
        self.rect.x = 350  # Posición x del árbol
        self.rect.y = 200  # Posición y del árbol

    def get_image(self):
        return self.image

    def get_position(self):
        return self.rect.x, self.rect.y
