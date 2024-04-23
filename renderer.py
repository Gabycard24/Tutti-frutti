import pygame
import sys

class Renderer:
    def __init__(self, window_width, window_height):
        pygame.display.set_caption("Fruit Catcher")
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()

    def render_element(self, image, position):
        self.window.blit(image, position)

    def render_score(self, score):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        self.window.blit(score_text, (10, 10))

    def render_game_over(self):
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(self.window_width // 2, self.window_height // 2))
        self.window.blit(game_over_text, text_rect)
        pygame.display.update()

    def clear_screen(self):
        self.window.fill((255, 255, 255))

    def update_display(self):
        pygame.display.update()

    def get_window_width(self):
        return self.window_width

    def get_window_height(self):
        return self.window_height

    def get_clock(self):
        return self.clock
