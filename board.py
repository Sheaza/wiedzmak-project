import pygame
from random import randint

import const  # Declaration of constants
import a_star
import genetic_generation as genetic
from bandit import Bandit
from grid import Grid
from griffin import Griffin
from leshy import Leshy
from state import State
from wiedzmak import Wiedzmak
from wolf import Wolf
from button import Button
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
menu_background = pygame.image.load('assets\\main.jpg')

# Set up the caption and icon for window
pygame.display.set_caption('Wiedzmak')
icon = pygame.image.load('assets\\witcher.png')
pygame.display.set_icon(icon)

hp_full = pygame.image.load('assets\\hp_full.png')
hp_medium = pygame.image.load('assets\\hp_medium.png')
hp_low = pygame.image.load('assets\\hp_low.png')

change_witcher_direction = pygame.USEREVENT
pygame.time.set_timer(change_witcher_direction, 500)

MENU_TEXT = pygame.font.Font('assets\\font.ttf',90).render('WIEDZMAK',True,'Black')
MENU_RECT = MENU_TEXT.get_rect(center=(400,130))

EASY_BUTTON = Button(image=pygame.image.load("assets\\play.png"), pos=(400, 250), 
                    text_input="EASY", font=pygame.font.Font('assets\\font.ttf',75), base_color="#d7fcd4", hovering_color="White")
MEDIUM_BUTTON = Button(image=pygame.image.load("assets\\play_longer.png"), pos=(400, 400), 
                    text_input="MEDIUM", font=pygame.font.Font('assets\\font.ttf',75), base_color="#d7fcd4", hovering_color="White")
HARD_BUTTON = Button(image=pygame.image.load("assets\\play.png"), pos=(400, 550), 
                    text_input="HARD", font=pygame.font.Font('assets\\font.ttf',75), base_color="#d7fcd4", hovering_color="White")

game_mode = -1
running = True
while running:
    if game_mode == -1:
        window.blit(menu_background, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        window.blit(MENU_TEXT,MENU_RECT)

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.change_color(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    game_mode = 0
                elif MEDIUM_BUTTON.check_for_input(MENU_MOUSE_POS):
                    game_mode = 1
                elif HARD_BUTTON.check_for_input(MENU_MOUSE_POS):
                    game_mode = 2
                print(game_mode)
    else:
        ### CLOCK ###
        dt = clock.tick(const.framerate)

        ### MATHS ###
        pos_x, pos_y = witcher.get_witcher_position()
        map_x, map_y = pos_x // 16, pos_y // 16

            # RANDOM SPAWN
        if (map_x, map_y) not in been:
            been.append((map_x, map_y))  # list of tuples
            genetic_result = genetic.algorithm(game_mode, map_x, map_y, (pos_x, pos_y))  # list of monster positions chosen by genetic algorithm

            for monster in genetic_result:
                position = monster[0]
                type = monster[1]

                # tworzenie nowego obiektu wylosowanego potwora
                if type == 'Leshy':
                    new_monster = Leshy(position[0], position[1])
                elif type == 'Wolf':
                    new_monster = Wolf(position[0], position[1])
                elif type == 'Bandit':
                    new_monster = Bandit(position[0], position[1])
                elif type == 'Griffin':
                    new_monster = Griffin(position[0], position[1])

                # finalna tablica obiektow z potworami
                monsters.append(new_monster)
                print(monsters)
                monsters_positions = [x.get_position() for x in monsters]
                print(monsters_positions)

        if witcher.get_hp() <= 0:
            running = False
            print("You lost")

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
                else:
                    distances = []
                    for map in const.MAPS:
                        if map not in been:
                            x, y = map
                            distance = (abs(map_x - x)) + (abs(map_y - y))
                            temp = map, distance
                            distances.append(temp)

                    if distances:
                        distances.sort(key=lambda x: x[1])
                        new_map_x, new_map_y = distances[0][0]
                        new_x = randint(new_map_x * 16, new_map_x * 16 + 15)
                        new_y = randint(new_map_y * 16, new_map_y * 16 + 15)

                        while (new_x,new_y) in monsters_positions or (new_x, new_y) in const.COLLISIONS:
                            new_x = randint(new_map_x * 16, new_map_x * 16 + 15)
                            new_y = randint(new_map_y * 16, new_map_y * 16 + 15)

                        new_monster = Leshy(new_x,new_y)
                        monsters.append(new_monster)
                        monsters_positions = [x.get_position() for x in monsters]
                    else:
                        running = False
                        print("You won!")

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

        # Draw hp bar
        hp_bar_pos_x = 0
        hp_bar_pos_y = 0

        if pos_y % 16 == 0:
            hp_bar_pos_x = pos_x % 16 * const.SQUARE_SIZE
            hp_bar_pos_y = pos_y % 16 * const.SQUARE_SIZE + 50
        else:
            hp_bar_pos_x = pos_x % 16 * const.SQUARE_SIZE
            hp_bar_pos_y = pos_y % 16 * const.SQUARE_SIZE - 10

        if witcher.get_hp() == 3:
            window.blit(hp_full, (hp_bar_pos_x, hp_bar_pos_y))
        elif witcher.get_hp() == 2:
            window.blit(hp_medium, (hp_bar_pos_x, hp_bar_pos_y))
        elif witcher.get_hp() == 1:
            window.blit(hp_low, (hp_bar_pos_x, hp_bar_pos_y))

    ### DISPLAY ###
    pygame.display.update()

pygame.quit()