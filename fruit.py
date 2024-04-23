import pygame
from pygame.sprite import Sprite
import random

class Fruit(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))  # Color aleatorio para la fruta
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)  # Posición x inicial aleatoria
        self.rect.y = 0  # Posición y inicial en la parte superior de la ventana
        self.speed = 3

    def update(self):
        self.rect.y += self.speed

    def get_image(self):
        return self.image

    def get_position(self):
        return self.rect.x, self.rect.y
