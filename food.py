import pygame
import random

class Food:
    rect: pygame.Rect
    size: int # size of screen
    snake_size: int # size of the snake

    def __init__(self, size, snake_size):
        self.size = size
        self.snake_size = snake_size
        self.new_coords()

    def new_coords(self):
        x = random.randrange(0, self.size[0], self.snake_size)
        y = random.randrange(0, self.size[1], self.snake_size)
        self.rect = pygame.Rect(x, y, self.snake_size, self.snake_size)
    
    def get_rect(self) -> list:
        return self.rect