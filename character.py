import pygame
from pygame.sprite import Sprite

class Character(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Color rojo para el personaje
        self.rect = self.image.get_rect()
        self.rect.centerx = 400  # Posición inicial en el centro horizontal de la ventana
        self.rect.bottom = 580   # Posición inicial en la parte inferior de la ventana
        self.speed = 5

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > 800:
            self.rect.right = 800

    def reset_position(self):
        self.rect.centerx = 400  # Restablecer la posición horizontal al centro de la ventana
        self.rect.bottom = 580   # Restablecer la posición vertical en la parte inferior de la ventana

    def get_image(self):
        return self.image

    def get_position(self):
        return self.rect.x, self.rect.y
