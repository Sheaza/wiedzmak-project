import const
import operator
import numpy as np
import random as rand
import pandas as pd
import matplotlib.pyplot as plt


# Calculate distance between 2 positions
def calculate_distance(start, end):
    (x1, y1) = start
    (x2, y2) = end
    distance = abs(x2 - x1) + abs(y2 - y1)

    return distance


# Spawn position for 1 monster
def generate_position(used_positions, map_x, map_y):
    spawn_x = rand.randint(1, 14) + map_x * 16
    spawn_y = rand.randint(1, 14) + map_y * 16

    while (spawn_x, spawn_y) in used_positions + const.COLLISIONS + [const.START_POS]:
        spawn_x = rand.randint(1, 14) + map_x * 16
        spawn_y = rand.randint(1, 14) + map_y * 16

    return spawn_x, spawn_y


def create_position_list(monsters_count, map_x, map_y, difficulty):
    monsters_list = []
    used_positions = []

    for i in range(monsters_count):
        monster_position = generate_position(used_positions, map_x, map_y)
        monster_type = const.MONSTER_NAMES[rand.randint(0, len(const.MONSTER_NAMES[:difficulty + 1]))]
        used_positions.append(monster_position)
        monsters_list.append([monster_position, monster_type])

    return monsters_list


def initial_population(monsters_count, population_size, map_x, map_y, difficulty):
    population = []

    for i in range(population_size):
        monsters_list = create_position_list(monsters_count, map_x, map_y, difficulty)
        population.append(monsters_list)

    return population


def fitness_function(parent, difficulty):
    distances = []

    for x in parent:
        distances_per_monster = []
        for y in parent:
            distance = calculate_distance(x[0], y[0])
            if distance != 0:
                distances_per_monster.append(distance) # distances between witcher and certain monster |  ex. [11, 23, 19, 11, 20, 19, 15, 15, 11, 13]
        distances_per_monster_avg = np.mean(distances_per_monster)
        distances.append(distances_per_monster_avg)

    distance_val = sorted(distances, reverse=True)
    distance_avg = np.mean(distance_val)
    distance_to_range = abs(15 - 5 * difficulty - distance_avg)

    if distance_to_range == 0:
        fitness = 1
    else:
        fitness = 1 / distance_to_range

    return fitness


def rank_distances(population, difficulty):
    fitness_results = {}

    for i in range(len(population)):
        fitness = fitness_function(population[i], difficulty)
        fitness_results[i] = fitness

    return sorted(fitness_results.items(), key=operator.itemgetter(1), reverse=True)


def roulette_wheel_selection(population_ranked, elite_size):
    selection = []
    df = pd.DataFrame(np.array(population_ranked), columns=["index", "fitness"])
    df['cum_sum'] = df.fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.fitness.sum()

    for i in range(elite_size):
        selection.append(population_ranked[i][0])

    for i in range(len(population_ranked) - elite_size):
        pick = 100 * rand.random()

        for i in range(len(population_ranked)):
            if pick <= df.iat[i, 3]:
                selection.append(population_ranked[i][0])
                break

    return selection


def mating_pool(population, selection):
    pool = []

    for i in range(len(selection)):
        index = selection[i]
        pool.append(population[index])

    return pool


def breed(parent1, parent2):
    child1 = []

    gene_a = int(rand.random() * len(parent1))
    gene_b = int(rand.random() * len(parent1))

    start_gene = min(gene_a, gene_b)
    end_gene = max(gene_a, gene_b)

    for i in range(start_gene, end_gene):
        child1.append(parent1[i])

    child2 = [item for item in parent2 if item not in child1]
    child = child1 + child2

    return child


def breed_population(mating, elite_size):
    children = []
    length = len(mating) - elite_size
    pool = rand.sample(mating, len(mating))

    for i in range(elite_size):
        children.append(mating[i])

    for i in range(length):
        child = breed(pool[i], pool[len(mating) - i - 1])
        children.append(child)

    return children


def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if rand.random() < mutation_rate:
            swap_with = int(rand.random() * len(individual))
            distances1 = individual[swapped]
            distances2 = individual[swap_with]
            individual[swapped] = distances2
            individual[swap_with] = distances1

    return individual


def mutate_population(population, mutation_rate):
    mutated = []

    for index in range(len(population)):
        mutated_index = mutate(population[index], mutation_rate)
        mutated.append(mutated_index)

    return mutated


def next_generation(current_generation, elite_size, mutation_rate, difficulty):
    ranked = rank_distances(current_generation, difficulty)
    selection = roulette_wheel_selection(ranked, elite_size)
    mating = mating_pool(current_generation, selection)
    children = breed_population(mating, elite_size)
    next_gen = mutate_population(children, mutation_rate)

    return next_gen


def genetic_algorithm_plot(monsters_count, population_size, elite_size, mutation_rate, generations, map_x, map_y, difficulty):
    population = initial_population(monsters_count, population_size, map_x, map_y, difficulty)
    progress = []
    progress.append(1 / rank_distances(population, difficulty)[0][1])

    for i in range(generations):
        population = next_generation(population, elite_size, mutation_rate, difficulty)
        progress.append(1 / rank_distances(population, difficulty)[0][1])

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()


def algorithm(difficulty, map_x, map_y):
    monsters_count = const.MONSTER_COUNT
    population_size = 100
    elite_size = 10
    mutation_rate = 0.01
    generations = 30
    population = initial_population(monsters_count, population_size, map_x, map_y, difficulty)

    for i in range(generations):
        population = next_generation(population, elite_size, mutation_rate, difficulty)

    best_distance_index = rank_distances(population, difficulty)[0][0]
    best_distance = population[best_distance_index]

    return best_distance[:const.MONSTER_COUNT]


if __name__ == '__main__':
    result = algorithm(0, 0, 0)
    print(result)
    #genetic_algorithm_plot(const.MONSTER_COUNT, 100, 10, 0.01, 30, 0, 0, 0)
