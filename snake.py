import pygame

class Snake:

    direction = 'U' # U, D, L, R, for up, down, left right
    blocks = []
    move_space = 40
    size = 0

    # initializer
    def __init__(self, size, snake_s) -> None:
        self.direction = 'U'
        self.size = size
        self.move_space = snake_s
        self.blocks.append(
            pygame.Rect(0, size[1]-self.move_space, self.move_space, self.move_space))

    # updates where snake is
    def move(self) -> None:
        # iterates thorugh non-front blocks
        for i in range(len(self.blocks) - 1, 0, -1):
            self.blocks[i].x = self.blocks[i-1].x
            self.blocks[i].y = self.blocks[i-1].y
        # moves front block
        if self.direction == 'U':
            self.blocks[0].y -= self.move_space
        elif self.direction == 'D':
            self.blocks[0].y += self.move_space
        elif self.direction == 'L':
            self.blocks[0].x -= self.move_space
        elif self.direction == 'R':
            self.blocks[0].x += self.move_space

    # adds block at the end of snake
    def add_block(self) -> None:
        x = self.blocks[-1].x
        y = self.blocks[-1].y
        new_block = \
            pygame.Rect(x, y, self.move_space, self.move_space)
        self.blocks.append(new_block)
    
    # Returns true if hits itself
    def self_hit(self) -> bool:
        front = self.blocks[0]
        for i in range(len(self.blocks) -1, 0, -1):
            if front.colliderect(self.blocks[i]):
                return True
        return False

    # Returns true if it is in contact with food
    def collides_with(self, rect) -> bool:
        for block in self.blocks:
            if block.colliderect(rect):
                return True
                
        return False

    # setter for direction
    def set_direction(self, direc) -> None:
        self.direction = direc

    # returns if out of bounds
    def is_outside(self) -> bool:
        x, y = self.blocks[0].x, self.blocks[0].y
        return x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]

    def get_length(self) -> int:
        return len(self.blocks)