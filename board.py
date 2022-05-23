import pygame
from random import randint
import const  # Declaration of constants
import a_star
from bandit import Bandit
from grid import Grid
from griffin import Griffin
from leshy import Leshy
from state import State
from wiedzmak import Wiedzmak
from wolf import Wolf
import time

# Initialize pygame
pygame.init()

# Initialize game clock
clock = pygame.time.Clock()

# Initialize game classes
witcher = Wiedzmak()
grid = Grid()
monsters = []
monsters_position = []
been = []
path = []

# Set up the drawing window
window = pygame.display.set_mode(const.windows_size)
background = pygame.image.load('assets\\mapa.png')

# Set up the caption and icon for window
pygame.display.set_caption('Wiedzmak')
icon = pygame.image.load('assets\\witcher.png')
pygame.display.set_icon(icon)

change_witcher_direction = pygame.USEREVENT
pygame.time.set_timer(change_witcher_direction, 500)

running = True
while running:

    ### CLOCK ###
    dt = clock.tick(const.framerate)

    ### MATHS ###
    pos_x, pos_y = witcher.get_witcher_position()
    map_x, map_y = pos_x//16, pos_y//16

    # RANDOM SPAWN
    if (map_x, map_y) not in been:
        been.append((map_x, map_y)) # list of tuples
        
        for x in range(const.MONSTER_COUNT): # spawn certain number of monsters
            # 1 to 14 are values which exclude borders of a map
            spawn_x = randint(1, 14) + map_x * 16
            spawn_y = randint(1, 14) + map_y * 16
            monster_type = randint(0, len(const.MONSTER_NAMES)-1)

            # pomocnicza lista pozycji potworow i deklaracja zmiennej przetrzymujacej obiekt
            monsters_positions = [x.get_position() for x in monsters]

            while (spawn_x, spawn_y) in const.COLLISIONS or (spawn_x, spawn_y) in monsters_positions or (spawn_x, spawn_y) == (witcher.get_witcher_position()):
                spawn_x = randint(1, 14) + map_x * 16
                spawn_y = randint(1, 14) + map_y * 16

            # tworzenie nowego obiektu wylosowanego potwora
            if const.MONSTER_NAMES[monster_type] == 'Leshy':
                new_monster = Leshy(spawn_x, spawn_y)
            elif const.MONSTER_NAMES[monster_type] == 'Wolf':
                new_monster = Wolf(spawn_x, spawn_y)
            elif const.MONSTER_NAMES[monster_type] == 'Bandit':
                new_monster = Bandit(spawn_x, spawn_y)
            elif const.MONSTER_NAMES[monster_type] == 'Griffin':
                new_monster = Griffin(spawn_x, spawn_y)

            # finalna tablica obiektow z potworami
            monsters.append(new_monster)
            print(monsters)
            monsters_positions = [x.get_position() for x in monsters]
            print(monsters_positions)

    ### EVENTS ###
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # handling button "X"
            running = False
        if event.type == pygame.KEYDOWN:    # moving character
            curr_position = witcher.get_witcher_position()
            if event.key == pygame.K_LEFT:
                witcher.move('LEFT', monsters, monsters_positions) 
            if event.key == pygame.K_RIGHT:
                witcher.move('RIGHT', monsters, monsters_positions)
            if event.key == pygame.K_UP:
                witcher.move('UP', monsters, monsters_positions)
            if event.key == pygame.K_DOWN:
                witcher.move('DOWN', monsters, monsters_positions)
                
        if event.type == change_witcher_direction:
            if monsters_positions:
                if len(path) == 0:
                    nearest_monster = a_star.nearest_monster_pos(witcher.get_witcher_position(), monsters_positions)
                    path = a_star.a_star_search(State(witcher.get_witcher_position(), witcher.get_witcher_orientation()), nearest_monster)

                witcher.move(path.pop(0), monsters, monsters_positions)


    ### DRAWING ####
    # Fill the background
    window.blit(background, (map_x * -800, map_y * -800))

    # Draw grid
    grid.draw_grid(window)

    # Draw character
    character = witcher.asset
    window.blit(character, (pos_x % 16 * const.SQUARE_SIZE, pos_y % 16 * const.SQUARE_SIZE))

    # draw monsters which positions are in range of current map
    for monster in monsters:
        in_x_range = map_x * 16 <= monster.pos_x < 16 + map_x * 16
        in_y_range = map_y * 16 <= monster.pos_y < 16 + map_y * 16

        if in_x_range and in_y_range:
            monster_image = monster.asset
            window.blit(monster_image, (monster.pos_x % 16 * const.SQUARE_SIZE, monster.pos_y % 16 * const.SQUARE_SIZE))

    ### DISPLAY ###
    pygame.display.update()

pygame.quit()