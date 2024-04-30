import pygame
import sys
import os
from character import Character
from tree import Tree
from fruit import Fruit
from background import Background 
import random

# Get the path to the assets folder relative to the current file
assets_dir = os.path.join(os.path.dirname(__file__), 'assets/images')


class Game:
    def __init__(self):
        pygame.display.set_caption("Tutti-frutti")
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.character = Character()
        self.tree = Tree()
        self.all_fruits = pygame.sprite.Group()
        self.background_images = [os.path.join(assets_dir, filename) for filename in ["background1.png", "background2.png", "background3.png", "background4.png"]]
        self.background = Background(self.background_images, self.window_width, self.window_height)
        self.fruit_images_dir = "assets\without_shadow"

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.move_left()
        if keys[pygame.K_RIGHT]:
            self.character.move_right()

        if random.random() < 0.05:
            new_fruit = Fruit(self.fruit_images_dir)
            self.all_fruits.add(new_fruit)

        self.all_fruits.update()

        for fruit in self.all_fruits:
            if pygame.sprite.collide_rect(self.character, fruit):
                self.all_fruits.remove(fruit)
                self.score += fruit.get_points()

        for fruit in self.all_fruits:
            if fruit.rect.top >= self.window_height:
                self.all_fruits.remove(fruit)
                if fruit.fruit_type == "rotten":  # if Rotten fruit subtract point
                    self.score -= 1

        if self.score < 0:
            self.game_over()

        self.background.update()

    def render(self):
        self.window.fill((255, 255, 255))
        self.background.draw(self.window)
        self.window.blit(self.tree.image, (self.tree.rect.x, self.tree.rect.y))
        self.all_fruits.draw(self.window)
        self.window.blit(self.character.image, (self.character.rect.x, self.character.rect.y))
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.window.blit(score_text, (10, 10))
        pygame.display.update()

    def game_over(self):
        self.renderer.render_game_over(self.score)
        pygame.time.delay(2000)
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.character.reset_position()
        self.all_fruits.empty()

