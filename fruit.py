import pygame
from pygame.sprite import Sprite
import random
import os


class Fruit(Sprite):
    # Define the probabilities of generating each type of fruit
    PROB_NORMAL = 0.7
    PROB_ROTTEN = 0.2
    PROB_SPECIAL1 = 0.05  # Special fruit with value 2 (blue)
    PROB_SPECIAL2 = 0.05  # Special fruit with value 5 (pink)

    def __init__(self, fruit_images_dir):
        super().__init__()
        self.speed = 3
        self.fruit_images_dir = fruit_images_dir
        self.generate_fruit()

    def generate_fruit(self):
        # Get a list of all image filenames in the fruit images folder
        fruit_image_files = os.listdir(self.fruit_images_dir)

        # Select a random image filename from the list
        random_image_file = random.choice(fruit_image_files)

        # Load the selected image
        image_path = os.path.join(self.fruit_images_dir, random_image_file)
        self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 100))

        # Set rect based on image size
        self.rect = self.image.get_rect()

        # Set initial position (random x, top of the screen)
        self.rect.x = random.randint(0, 800)
        self.rect.y = 0

        # Determine fruit type and points based on image filename
        filename_no_extension = os.path.splitext(random_image_file)[0]
        if "rotten" in filename_no_extension:
            self.fruit_type = "rotten"
            self.points = -1
        elif "special1" in filename_no_extension:
            self.fruit_type = "special"
            self.points = 2
        elif "special2" in filename_no_extension:
            self.fruit_type = "special"
            self.points = 5
        else:
            self.fruit_type = "normal"
            self.points = 1

    def update(self):
        self.rect.y += self.speed

    def get_image(self):
        return self.image

    def get_position(self):
        return self.rect.x, self.rect.y

    def get_points(self):
        return self.points
