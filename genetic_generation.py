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
    chosen_monsters = difficulty
    chosen_monsters += 2

    for monster_name in const.MONSTER_NAMES[:chosen_monsters]:
        type_count[monster_name] = 0  # {'Leshy': 0, 'Wolf': 0, 'Bandit': 0, 'Griffin': 0}

    for x in parent:
        type_count[x[1]] += 1  # monster occurencies | ex. {'Leshy': 0, 'Wolf': 5, 'Bandit': 4, 'Griffin': 1}
        distances.append(calculate_distance(witcher_pos, x[0]))  # distances between witcher and certain monster |  ex. [11, 23, 19, 11, 20, 19, 15, 15, 11, 13]
        #print(f'dist {x[0]} & {witcher_pos} -> {distances[-1]}')

    chosen_monsters -= 1
    type_count_val = sorted(list(type_count.values()), reverse=True)  # sorted number of monster occurencies  | ex. [5, 4, 1, 0]
    type_count_avg = mean(type_count_val[:chosen_monsters])  # average of <difficulty+1> highest occurencies | ex. 5.0 for difficulty=0 ( average of highest 0+1=1 values -> avg( [5] ) )
    # print(type_count)
    # print(type_count_val)
    # print(type_count_avg)
    # print(distances)
    #distance_avg = mean(distances)
    #value = 100*round((distance_avg+(15+(20*difficulty)))-(abs(distance_avg-(15+(20*difficulty)))),2)
    value = 0
    for i in distances:
        if i < (5 + (2-difficulty)*5):
            value += 0#i/(10 + difficulty*10)
        elif i > (10 + (2-difficulty)*5):
            value += 0
        elif i in range((5 + (2-difficulty)*5),(11 + (2-difficulty)*5)):
            value += 1
    
    #fitness += type_count_avg  # TODO make sth related to certain distance from witcher's current position
    #fitness += 1/(1+(abs(mean(distances)-(8 + difficulty*5))))
    print(f'{fitness} = {distances} x {difficulty} x {witcher_pos}')
    dif = 2-difficulty
    value = 0
    for i in distances:
        if i < (5 + (2-difficulty)*5):
            value += 0#i/(10 + difficulty*10)
        elif i > (10 + (2-difficulty)*5):
            value += 0
        elif i in range((5 + (2-difficulty)*5),(11 + (2-difficulty)*5)):
            value += 1
    fitness += value
    fitness += 5/(1 + abs(type_count_avg-(7+(2-difficulty)*5)))

    return fitness


def crossbreed(spawnlist1, spawnlist2, map_x, map_y, difficulty, witcher_pos):
    used_positions1 = []
    used_positions2 = []
    for i in range(len(spawnlist1)):
        used_positions1.append(spawnlist1[i][0])
        used_positions2.append(spawnlist2[i][0])
    print(f'przed crossem')
    print(f'list1: {spawnlist1}\nlist2: {spawnlist2}\nused_positions1: {used_positions1}\nused_positions2: {used_positions2}')

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
    

    fx1 = fitness_function(spawnlist1,difficulty,witcher_pos)
    fx2 = fitness_function(spawnlist2,difficulty,witcher_pos)
    x1 = [spawnlist1,fx1,'m']
    x2 = [spawnlist2,fx2,'m']

    print(f'po crossie')
    print(f'x1[0] --> {x1[0]}')
    print(f'x2[0] --> {x2[0]}')
    print(f'x1[1] --> {x1[1]}')
    print(f'x2[1] --> {x2[1]}')
    
    return x1,x2  # return mixed pair


def algorithm(difficulty, map_x, map_y, witcher_pos):
    universe = []
    population = 100
    to_breed = 10
    mutations = 10

    for parent_id in range(population):
        parent = generate_parent(map_x, map_y, difficulty)
        fitness = fitness_function(parent, difficulty, witcher_pos)
        universe.append([parent, fitness, 'n'])
        # print(universe[-1])

    universe = sorted(universe, key=lambda x: x[1], reverse=True)  # list of possible sets sorted by fitness value
    print('BEGIN :\nUni first after 1st sort',universe[0])
    print('BEGIN :\nUni last after 1st sort',universe[-1])
    for iter in range(mutations):
        print(f'--- iter {iter+1} ---')
        breed = universe[:to_breed]
        for pairs in range(int(len(breed) / 2)):
            # print(f'{2*pairs}:\n{breed[2*pairs]}')
            # print(f'{2*pairs+1}:\n{breed[2*pairs+1]}\n')
            # print('----------------')
            b1 = breed[2 * pairs][0]
            b2 = breed[2 * pairs + 1][0]
            breed[2 * pairs], breed[2 * pairs + 1] = crossbreed(b1, b2, map_x, map_y, difficulty, witcher_pos)  # mix 2 parents
            
            x1 = breed[2 * pairs]
            x2 = breed[2 * pairs + 1]
            print(f'Qx1[0]({x1[2]}) --> {x1[0]}')
            print(f'Qx2[0]({x2[2]}) --> {x2[0]}')
            print(f'Qx1[1]({x1[2]}) --> {x1[1]}')
            print(f'Qx2[1]({x2[2]}) --> {x2[1]}')

            # print('----------------')
            # print(f'{2*pairs}:\n{breed[2*pairs]}')
            # print(f'{2*pairs+1}:\n{breed[2*pairs+1]}\n')
        universe = universe[:(-1)*to_breed]
        universe += breed  # replaced the worst elements by new ones
        for xdd in universe:
            xdd[1] = fitness_function(xdd[0],difficulty,witcher_pos)
        print('Uni first b4 sort',universe[-1])
        print('Uni last b4 sort',universe[-2])
        universe = sorted(universe, key=lambda x: x[1], reverse=True)  # sort list of possible sets by fitness value

        #print('Uni last after sort',universe[-1])
        #print('Uni first b4 sort',universe[0])
    print('Uni first after sort\n',universe[0])
    print('Uni last after sort\n',universe[-1])
    return universe[0][0]  # OUTPUT : list( list( tuple( ), Str() ), ..., list( tuple( ), Str() )) | list( list( pozycja, nazwa_potwora ), ....... , list( pozycja, nazwa_potwora ) )


# result = algorithm(0, 0, 0, const.START_POS) algorithm(difficulty, map_x, map_y) | LAUNCH EXAMPLE
# print(result)
# print(result[0][0])
# print(result[1][0])
