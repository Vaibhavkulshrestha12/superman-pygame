"""
Pipe obstacle class
"""
import pygame
from src.config.settings import *

class Pipe(pygame.sprite.Sprite):
    """Pipe obstacle"""
    
    def __init__(self, pipe_image, height, x_pos, is_bottom=True):
        super().__init__()
        self.image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, height))
        self.rect = self.image.get_rect()
        
        if is_bottom:
            self.rect.topleft = (x_pos, SCREEN_HEIGHT - height)
        else:
            self.rect.topleft = (x_pos, 0)

    def update(self):
        """Move pipe to the left"""
        self.rect.x -= 5