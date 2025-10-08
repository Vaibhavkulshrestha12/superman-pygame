import pygame
import sys
from src.config.settings import *
from src.game.game_state import GameState

class SupermanGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Superman')
        self.clock = pygame.time.Clock()
        
        # Load assets
        self.images = self.load_images()
        self.sounds = self.load_sounds()
        
        # Initialize game state
        self.game_state = GameState(self.screen, self.images, self.sounds)
    #game images code
    def load_images(self):
       
        images = {}
        
        # Load and scale images
        images['superman'] = pygame.image.load(SUPERMAN_IMAGE)
        images['superman'] = pygame.transform.scale(images['superman'], (SUPERMAN_SIZE, SUPERMAN_SIZE))
        
        images['pipe'] = pygame.image.load(PIPE_IMAGE)
        images['pipe'] = pygame.transform.scale(images['pipe'], (PIPE_WIDTH, SCREEN_HEIGHT))
        
        images['background'] = pygame.image.load(BACKGROUND_IMAGE)
        images['background'] = pygame.transform.scale(images['background'], (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        images['start_screen'] = pygame.image.load(START_SCREEN_IMAGE)
        images['start_screen'] = pygame.transform.scale(images['start_screen'], (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        return images
    
    #game music
    def load_sounds(self):
        
        sounds = {}
        
        # Load music and sounds
        pygame.mixer.music.load(MUSIC_FILE)
        pygame.mixer.music.set_volume(0.5)
        sounds['music'] = None  # Music is handled globally
        
        sounds['game_over'] = pygame.mixer.Sound(GAME_OVER_SOUND)
        
        return sounds
    
    #game loop
    def run(self):
        
        running = True
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.game_state.handle_event(event)
            
            # Update game
            self.game_state.update()
            
            # Draw everything
            self.game_state.draw()
            
            # Update display
            pygame.display.flip()
            self.clock.tick(FPS)
        
        # Quit
        pygame.quit()
        sys.exit()

#game start loop
def main():
   
    game = SupermanGame()
    game.run()

if __name__ == "__main__":
    main()