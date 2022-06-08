from audioop import avg
import const
from random import randint
from numpy import mean


# Calculate distance between 2 positions
def calculate_distance(start, end):
    (x1, y1) = start
    (x2, y2) = end
    distance = abs(x2 - x1) + abs(y2 - y1)

    return distance


# Spawn position for 1 monster
def generate_position(used_positions, map_x, map_y):
    spawn_x = randint(1, 14) + map_x * 16
    spawn_y = randint(1, 14) + map_y * 16

    while (spawn_x, spawn_y) in used_positions + const.COLLISIONS + [const.START_POS]:
        spawn_x = randint(1, 14) + map_x * 16
        spawn_y = randint(1, 14) + map_y * 16

    return spawn_x, spawn_y


# Generate monsters spawn list
def generate_parent(map_x, map_y, difficulty):
    used_positions = []
    parent = []

    for x in range(const.MONSTER_COUNT):
        monster_position = generate_position(used_positions, map_x, map_y)
        monster_type = const.MONSTER_NAMES[randint(0, len(const.MONSTER_NAMES[:difficulty + 1]))]
        used_positions.append(monster_position)
        parent += [[monster_position, monster_type]]

    # print(used_positions,parent)
    return parent


# Fitness function
def fitness_function(parent, difficulty, witcher_pos):
    type_count = {}
    distances = []
    fitness = 0

    for monster_name in const.MONSTER_NAMES[:difficulty + 2]:
        type_count[monster_name] = 0  # {'Leshy': 0, 'Wolf': 0, 'Bandit': 0, 'Griffin': 0}

    for x in parent:
        type_count[x[1]] += 1  # monster occurencies | ex. {'Leshy': 0, 'Wolf': 5, 'Bandit': 4, 'Griffin': 1}
        distances.append(calculate_distance(witcher_pos, x[0]))  # distances between witcher and certain monster |  ex. [11, 23, 19, 11, 20, 19, 15, 15, 11, 13]

    type_count_val = sorted(list(type_count.values()), reverse=True)  # sorted number of monster occurencies  | ex. [5, 4, 1, 0]
    type_count_avg = mean(type_count_val[:difficulty + 1])  # average of <difficulty+1> highest occurencies | ex. 5.0 for difficulty=0 ( average of highest 0+1=1 values -> avg( [5] ) )
    # print(type_count)
    # print(type_count_val)
    # print(type_count_avg)
    # print(distances)
    fitness = type_count_avg  # TODO make sth related to certain distance from witcher's current position
    return fitness


def crossbreed(spawnlist1, spawnlist2, map_x, map_y, difficulty, witcher_pos):
    used_positions1 = []
    used_positions2 = []
    for i in range(len(spawnlist1)):
        used_positions1.append(spawnlist1[i][0])
        used_positions2.append(spawnlist2[i][0])
    # print(f'list1: {spawnlist1}\nlist2: {spawnlist2}\nused_positions1: {used_positions1}\nused_positions2: {used_positions2}')

    crosspoint = randint(1, len(spawnlist1) - 1)

    spawnlist1[:crosspoint], spawnlist2[:crosspoint] = spawnlist2[:crosspoint], spawnlist1[:crosspoint]
    used_positions1[:crosspoint], used_positions2[:crosspoint] = used_positions2[:crosspoint], used_positions1[:crosspoint]

    for iter in range(len(spawnlist1) + 1, 0, -1):  # get rid of redundant elements
        while used_positions1[i] in used_positions1[:i]:
            new_pos = generate_position(used_positions1, map_x, map_y)
            spawnlist1[i][0] = new_pos
            used_positions1[i] = new_pos

    to_modify = randint(1, len(spawnlist1) - 1)  # modify random element in list 1
    rerolled_pos = generate_position(used_positions1, map_x, map_y)
    rerolled_monster = const.MONSTER_NAMES[randint(0, len(const.MONSTER_NAMES[:difficulty + 1]))]
    spawnlist1[to_modify] = [rerolled_pos, rerolled_monster]
    used_positions1[to_modify] = rerolled_pos

    to_modify = randint(1, len(spawnlist2) - 1)  # modify random element in list 2
    rerolled_pos = generate_position(used_positions2, map_x, map_y)
    rerolled_monster = const.MONSTER_NAMES[randint(0, len(const.MONSTER_NAMES[:difficulty + 1]))]
    spawnlist2[to_modify] = [rerolled_pos, rerolled_monster]
    used_positions2[to_modify] = rerolled_pos

    # print(f'list1: {spawnlist1}\nlist2: {spawnlist2}\nused_positions1: {used_positions1}\nused_positions2: {used_positions2}')

    return [spawnlist1, fitness_function(spawnlist1, difficulty, witcher_pos)], [spawnlist2, fitness_function(spawnlist2, difficulty, witcher_pos)]  # return mixed pair


def algorithm(difficulty, map_x, map_y, witcher_pos):
    universe = []
    population = 100
    to_breed = 10
    mutations = 10

    for parent_id in range(population):
        parent = generate_parent(map_x, map_y, difficulty)
        fitness = fitness_function(parent, difficulty, witcher_pos)
        universe.append([parent, fitness])
        # print(universe[-1])

    universe = sorted(universe, key=lambda x: x[1], reverse=True)  # list of possible sets sorted by fitness value
    for iter in range(mutations):
        breed = universe[:to_breed]
        for pairs in range(int(len(breed) / 2)):
            # print(f'{2*pairs}:\n{breed[2*pairs]}')
            # print(f'{2*pairs+1}:\n{breed[2*pairs+1]}\n')
            # print('----------------')
            breed[2 * pairs], breed[2 * pairs + 1] = crossbreed(breed[2 * pairs][0], breed[2 * pairs + 1][0], map_x, map_y, difficulty, witcher_pos)  # mix 2 parents
            # print('----------------')
            # print(f'{2*pairs}:\n{breed[2*pairs]}')
            # print(f'{2*pairs+1}:\n{breed[2*pairs+1]}\n')
        universe[-1 * to_breed:] = breed  # replaced the worst elements by new ones
        # print(universe[-1])
        universe = sorted(universe, key=lambda x: x[1], reverse=True)  # sort list of possible sets by fitness value

        # print(universe[-1])
        # print(universe[0])
    return universe[0][0]  # OUTPUT : list( list( tuple( ), Str() ), ..., list( tuple( ), Str() )) | list( list( pozycja, nazwa_potwora ), ....... , list( pozycja, nazwa_potwora ) )


# result = algorithm(0, 0, 0, const.START_POS) algorithm(difficulty, map_x, map_y) | LAUNCH EXAMPLE
# print(result)
# print(result[0][0])
# print(result[1][0])
