import pygame
import const  # Declaration of constants
from wiedzmak import Wiedzmak

# Initialize pygame
pygame.init()

# Initialize game clock
clock = pygame.time.Clock()

witcher = Wiedzmak()

# Set up the drawing window
window = pygame.display.set_mode(const.windows_size)
background = pygame.image.load('assets\\map1.png')

# Set up the caption and icon for window
pygame.display.set_caption('Wiedzmak')
icon = pygame.image.load('assets\\witcher.png')
pygame.display.set_icon(icon)


def update_camera(pos_x, pos_y):
    if pos_x < 16:
        camera_x = 0
    elif 16 <= pos_x < 32:
        camera_x = -800
    elif pos_x >= 32:
        camera_x = -1600

    # Moving camera on y axis
    if pos_y < 16:
        camera_y = 0
    elif 16 <= pos_y < 32:
        camera_y = -800
    elif pos_y >= 32:
        camera_y = -1600

    return camera_x, camera_y


def draw_grid():
    for i in range(int(const.rows)):
        pygame.draw.line(window, const.LINES, (0, i * const.GAP), (const.windows_size[0], i * const.GAP))
        for j in range(int(const.columns)):
            pygame.draw.line(window, const.LINES, (j * const.GAP, 0), (j * const.GAP, const.windows_size[1]))


running = True
while running:

    ### CLOCK ###
    dt = clock.tick(const.framerate)

    ### EVENTS ###
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # handling button "X"
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: witcher.move('LEFT')
            if event.key == pygame.K_RIGHT: witcher.move('RIGHT')
            if event.key == pygame.K_UP: witcher.move('UP')
            if event.key == pygame.K_DOWN: witcher.move('DOWN')

    ### MATHS ###
    pos_x, pos_y = witcher.get_witcher_position()
    camera_x, camera_y = update_camera(pos_x, pos_y)

    ### DRAWING ####
    # Fill the background
    window.blit(background,(camera_x, camera_y))

    # Draw grid
    draw_grid()

    # Draw character
    character = witcher.asset
    window.blit(character, (pos_x % 16 * const.SQUARE_SIZE, pos_y % 16 * const.SQUARE_SIZE))

    ### DISPLAY ###
    pygame.display.update()

pygame.quit()