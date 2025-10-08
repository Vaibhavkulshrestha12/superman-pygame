import pygame
from src.config.settings import *

class Superman(pygame.sprite.Sprite):
    #superman sprite class
    
    def __init__(self, superman_image):
        super().__init__()
        self.image = superman_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.velocity = 0

    def jump(self):
        #jump code
        self.velocity = -JUMP_FORCE

    def update(self):
        #update code for supes position
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        
    def reset_position(self):
        #reset the position of supes
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.velocity = 0