import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SUPERMAN_SIZE = 50
PIPE_WIDTH = 30
GRAVITY = 1
JUMP_FORCE = 15
MAX_PIPE_GAP = 350
GAP_REDUCTION_RATE = 50
PIPE_SPAWN_INTERVAL = 120
MIN_PIPE_HEIGHT = 50
MAX_PIPE_HEIGHT = 200

superman_image = pygame.image.load("C:\\Users\\vaibhav kulshrestha\\Desktop\\Pygame Projects\\superman\\superman.png")
superman_image = pygame.transform.scale(superman_image, (SUPERMAN_SIZE, SUPERMAN_SIZE))

pipe_image = pygame.image.load("C:\\Users\\vaibhav kulshrestha\\Desktop\\Pygame Projects\\superman\\pipe.png")
pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, SCREEN_HEIGHT))

background_image = pygame.image.load("C:\\Users\\vaibhav kulshrestha\\Desktop\\Pygame Projects\\superman\\background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.music.load("C:\\Users\\vaibhav kulshrestha\\Desktop\\Pygame Projects\\superman\\music.mp3")
pygame.mixer.music.set_volume(0.5)

game_over_sound = pygame.mixer.Sound("C:\\Users\\vaibhav kulshrestha\\Desktop\\Pygame Projects\\superman\\game_over.wav")

start_screen_image = pygame.image.load("C:\\Users\\vaibhav kulshrestha\\Desktop\\Pygame Projects\\superman\\start_screen.png")
start_screen_image = pygame.transform.scale(start_screen_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

class Superman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = superman_image
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.velocity = 0

    def jump(self):
        self.velocity = -JUMP_FORCE

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

class Pipe(pygame.sprite.Sprite):
    def __init__(self, height, x_pos, is_bottom=True):
        super().__init__()
        self.image = pipe_image
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, height))
        self.rect = self.image.get_rect()
        if is_bottom:
            self.rect.topleft = (x_pos, SCREEN_HEIGHT - height)
        else:
            self.rect.topleft = (x_pos, 0)

    def update(self):
        self.rect.x -= 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Superman')

superman = Superman()
pipes = pygame.sprite.Group()

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

frame_counter = 0

START_SCREEN = 0
PLAYING = 1
GAME_OVER = 2
current_state = START_SCREEN

pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if current_state == START_SCREEN and event.key == pygame.K_SPACE:
                current_state = PLAYING
            elif current_state == PLAYING and event.key == pygame.K_SPACE:
                superman.jump()
            elif current_state == GAME_OVER and event.key == pygame.K_SPACE:
                superman.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
                superman.velocity = 0
                pipes.empty()
                score = 0
                current_state = PLAYING

    if current_state == PLAYING:
        superman.update()
        pipes.update()

        if superman.rect.top > SCREEN_HEIGHT:
            print("Game Over!")
            game_over_sound.play()
            current_state = GAME_OVER

        for pipe in pipes:
            if superman.rect.colliderect(pipe.rect):
                print("Game Over!")
                game_over_sound.play()
                current_state = GAME_OVER

        for pipe in pipes:
            if pipe.rect.right == superman.rect.left:
                score += 5

        if score >= 1000:
            max_gap = MAX_PIPE_GAP - (score // 1000) * GAP_REDUCTION_RATE
        else:
            max_gap = MAX_PIPE_GAP

        frame_counter += 1
        if frame_counter % PIPE_SPAWN_INTERVAL == 0:
            frame_counter = 0
            pipe_height = random.randint(MIN_PIPE_HEIGHT, MAX_PIPE_HEIGHT)
            gap_size = max(50, MAX_PIPE_GAP - (score // 1000) * GAP_REDUCTION_RATE)
            pipe_x_pos = SCREEN_WIDTH
            pipes.add(Pipe(pipe_height, pipe_x_pos, is_bottom=True))
            pipes.add(Pipe(SCREEN_HEIGHT - pipe_height - gap_size, pipe_x_pos, is_bottom=False))

        for pipe in pipes.copy():
            if pipe.rect.right < 0:
                pipes.remove(pipe)

    screen.blit(background_image, (0, 0))

    if current_state == START_SCREEN:
        screen.blit(start_screen_image, (0, 0))
    elif current_state == PLAYING:
        pipes.draw(screen)
        screen.blit(superman.image, superman.rect)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
    elif current_state == GAME_OVER:
        game_over_text = font.render("Game Over! Press SPACE to play again", True, (255, 255, 255))
        screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(FPS)

