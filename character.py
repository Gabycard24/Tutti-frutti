import pygame
from pygame.sprite import Sprite
import os

assets_dir = os.path.join(os.path.dirname(__file__), 'assets/images')

class Character(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(assets_dir, "character.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400  # Initial Hor position
        self.rect.bottom = 600   # Initial Ver position
        self.speed = 10

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > 800:
            self.rect.right = 800

    def reset_position(self):
        self.rect.centerx = 400  # Reset horizontal position to be in the middle of the window 
        self.rect.bottom = 580   # Reset Vertical position to be in the middle of the window

    def get_image(self):
        return self.image

    def get_position(self):
        return self.rect.x, self.rect.y
