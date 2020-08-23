import pygame
import snake
import food

class Display:
    screen = None
    snake = None
    food = None

    def __init__(self, size, snek, fud):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.snake = snek
        self.food = fud

    def update(self):
        self.screen.fill((0, 0, 0))
        
        for block in self.snake.blocks:
            self.draw(block)
        self.draw(self.food.get_rect())

        pygame.display.update()

    # draws the rectangle given
    def draw(self, rect: pygame.Rect) -> None:
        self.screen.fill((0, 0, 0), rect=rect)
        inner_rect = pygame.Rect(0, 0, 0, 0)
        inner_rect.width = int(rect.width*0.8)
        inner_rect.height = int(rect.height*0.8)
        inner_rect.center = rect.center
        self.screen.fill((255, 255, 255), rect=inner_rect)
