import pygame

class Background:
    def __init__(self, images, window_width, window_height):
        self.layers = [
            Layer(pygame.transform.scale(pygame.image.load(images[i]), (window_width, window_height)), speed=i+1)
            for i in range(len(images))
        ]
        self.window_width = window_width
        self.window_height = window_height

    def update(self):
        for layer in self.layers:
            layer.update()

    def draw(self, window):
        for layer in self.layers:
            layer.draw(window)

class Layer:
    def __init__(self, image, speed=1):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.speed = speed * 0.5 #velocity 
        self.offset = 0

    def update(self):
        self.offset += self.speed
        if self.offset >= self.rect.width:
            self.offset = 0

    def draw(self, window):
        window.blit(self.image, (-self.offset, 0))
        window.blit(self.image, (self.rect.width - self.offset, 0))
