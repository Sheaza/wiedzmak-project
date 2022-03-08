import pygame
import const  # Declaration of constants
from camera import Camera
from grid import Grid
from wiedzmak import Wiedzmak

# Initialize pygame
pygame.init()

# Initialize game clock
clock = pygame.time.Clock()

witcher = Wiedzmak()
grid = Grid()
camera = Camera()

# Set up the drawing window
window = pygame.display.set_mode(const.windows_size)
background = pygame.image.load('assets\\map1.png')

# Set up the caption and icon for window
pygame.display.set_caption('Wiedzmak')
icon = pygame.image.load('assets\\witcher.png')
pygame.display.set_icon(icon)


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
    camera_x, camera_y = camera.update_camera(pos_x, pos_y)

    ### DRAWING ####
    # Fill the background
    window.blit(background,(camera_x, camera_y))

    # Draw grid
    grid.draw_grid(window)

    # Draw character
    character = witcher.asset
    window.blit(character, (pos_x % 16 * const.SQUARE_SIZE, pos_y % 16 * const.SQUARE_SIZE))

    ### DISPLAY ###
    pygame.display.update()

pygame.quit()