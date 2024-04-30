import pygame
from pygame.sprite import Sprite
import os

assets_dir = os.path.join(os.path.dirname(__file__), 'assets/images')

class Tree(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(assets_dir, "Tree.png")), (800, 600))
        self.rect = self.image.get_rect()
        self.rect.x = 0  # Posición x del árbol
        self.rect.y = 0  # Posición y del árbol

    def get_image(self):
        return self.image

    def get_position(self):
        return self.rect.x, self.rect.y
