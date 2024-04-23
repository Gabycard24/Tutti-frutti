import pygame
import sys
from renderer import Renderer
from character import Character
from tree import Tree
from fruit import Fruit

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fruit Catcher")
        self.window_width = 800
        self.window_height = 600
        self.renderer = Renderer(self.window_width, self.window_height)
        self.clock = self.renderer.get_clock()
        self.score = 0
        self.character = Character()
        self.tree = Tree()
        self.all_fruits = pygame.sprite.Group()

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

        if pygame.time.get_ticks() % 60 == 0:
            new_fruit = Fruit()
            self.all_fruits.add(new_fruit)

        self.all_fruits.update()

        for fruit in self.all_fruits:
            if pygame.sprite.collide_rect(self.character, fruit):
                self.all_fruits.remove(fruit)
                self.score += 1

        for fruit in self.all_fruits:
            if fruit.rect.top >= self.window_height:
                self.all_fruits.remove(fruit)
                self.score -= 1

        if self.score < 0:
            self.game_over()

    def render(self):
        self.renderer.clear_screen()

        # Renderizar el árbol
        tree_image = self.tree.get_image()
        tree_position = self.tree.get_position()
        self.renderer.render_element(tree_image, tree_position)

        # Renderizar todas las frutas
        for fruit in self.all_fruits:
            fruit_image = fruit.get_image()
            fruit_position = fruit.get_position()
            self.renderer.render_element(fruit_image, fruit_position)

        # Renderizar el personaje
        character_image = self.character.get_image()
        character_position = self.character.get_position()
        self.renderer.render_element(character_image, character_position)

        # Renderizar el puntaje
        self.renderer.render_score(self.score)

        self.renderer.update_display()

    def game_over(self):
        self.renderer.render_game_over()
        pygame.time.delay(2000)
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.character.reset_position()
        self.all_fruits.empty()

