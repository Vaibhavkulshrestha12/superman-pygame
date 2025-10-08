import pygame
import random
from src.config.settings import *
from src.game.superman import Superman
from src.game.pipe import Pipe

class GameState:
    #Manages the game state and logic
    
    def __init__(self, screen, images, sounds):
        self.screen = screen
        self.superman_image = images['superman']
        self.pipe_image = images['pipe']
        self.background_image = images['background']
        self.start_screen_image = images['start_screen']
        
        self.music = sounds['music']
        self.game_over_sound = sounds['game_over']
        
        self.superman = Superman(self.superman_image)
        self.pipes = pygame.sprite.Group()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.frame_counter = 0
        self.current_state = START_SCREEN
        
        # Start music
        pygame.mixer.music.play(-1)
    
    def handle_event(self, event):
        """Handle game events"""
        if event.type == pygame.KEYDOWN:
            if self.current_state == START_SCREEN and event.key == pygame.K_SPACE:
                self.current_state = PLAYING
            elif self.current_state == PLAYING and event.key == pygame.K_SPACE:
                self.superman.jump()
            elif self.current_state == GAME_OVER and event.key == pygame.K_SPACE:
                self.reset_game()
            elif event.key == pygame.K_p:
                if self.current_state == PLAYING:
                    self.current_state = PAUSED
                elif self.current_state == PAUSED:
                    self.current_state = PLAYING
    
    def update(self):
        """Update game logic"""
        if self.current_state == PLAYING:
            self.superman.update()
            self.pipes.update()
            
            # Check if Superman hits the ground
            if self.superman.rect.top > SCREEN_HEIGHT:
                self.game_over()
            
            # Check collision with pipes
            for pipe in self.pipes:
                if self.superman.rect.colliderect(pipe.rect):
                    self.game_over()
            
            # Update score when Superman passes pipes
            for pipe in self.pipes:
                if pipe.rect.right == self.superman.rect.left:
                    self.score += 5
            
            # Spawn new pipes
            self.frame_counter += 1
            if self.frame_counter % PIPE_SPAWN_INTERVAL == 0:
                self.spawn_pipes()
                self.frame_counter = 0
            
            # Remove pipes that are off screen
            for pipe in self.pipes.copy():
                if pipe.rect.right < 0:
                    self.pipes.remove(pipe)
    
    def spawn_pipes(self):
        """Spawn a new pair of pipes"""
        pipe_height = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)
        gap_size = max(50, MAX_PIPE_GAP - (self.score // 1000) * GAP_REDUCTION_RATE)
        pipe_x_pos = SCREEN_WIDTH
        
        # Bottom pipe
        self.pipes.add(Pipe(self.pipe_image, pipe_height, pipe_x_pos, is_bottom=True))
        # Top pipe
        self.pipes.add(Pipe(self.pipe_image, SCREEN_HEIGHT - pipe_height - gap_size, pipe_x_pos, is_bottom=False))
    
    def game_over(self):
        """Handle game over"""
        print("Game Over!")
        self.game_over_sound.play()
        self.current_state = GAME_OVER
    
    def reset_game(self):
        """Reset the game to start playing again"""
        self.superman.reset_position()
        self.pipes.empty()
        self.score = 0
        self.frame_counter = 0
        self.current_state = PLAYING
    
    def draw(self):
        """Draw the game"""
        # Draw background
        self.screen.blit(self.background_image, (0, 0))
        
        if self.current_state == START_SCREEN:
            self.screen.blit(self.start_screen_image, (0, 0))
        elif self.current_state == PLAYING:
            self.pipes.draw(self.screen)
            self.screen.blit(self.superman.image, self.superman.rect)
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))
        elif self.current_state == GAME_OVER:
            game_over_text = self.font.render("Game Over! Press SPACE to play again", True, (255, 255, 255))
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        elif self.current_state == PAUSED:
            paused_text = self.font.render("Paused. Press P to resume.", True, (255, 255, 255))
            self.screen.blit(paused_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))