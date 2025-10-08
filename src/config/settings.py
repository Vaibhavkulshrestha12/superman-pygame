"""
Game configuration settings
"""
import os

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Game object sizes
SUPERMAN_SIZE = 50
PIPE_WIDTH = 30

# Physics settings
GRAVITY = 1
JUMP_FORCE = 15

# Pipe settings
MAX_PIPE_GAP = 350
GAP_REDUCTION_RATE = 50
PIPE_SPAWN_INTERVAL = 120
MIN_PIPE_HEIGHT = 50
MAX_PIPE_HEIGHT = 200

# Game states
START_SCREEN = 0
PLAYING = 1
GAME_OVER = 2
PAUSED = 3

# Asset paths
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
SOUNDS_DIR = os.path.join(ASSETS_DIR, 'sounds')

# Specific asset files
SUPERMAN_IMAGE = os.path.join(IMAGES_DIR, 'superman.png')
PIPE_IMAGE = os.path.join(IMAGES_DIR, 'pipe.png')
BACKGROUND_IMAGE = os.path.join(IMAGES_DIR, 'background.png')
START_SCREEN_IMAGE = os.path.join(IMAGES_DIR, 'start_screen.png')
MUSIC_FILE = os.path.join(SOUNDS_DIR, 'music.mp3')
GAME_OVER_SOUND = os.path.join(SOUNDS_DIR, 'game_over.wav')