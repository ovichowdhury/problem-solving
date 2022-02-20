import random
import numpy as np


def init_population(population_size, genes, target_size):
    p = []
    for _ in range(population_size):
        p.append(np.random.choice(genes, size=target_size))
    return p


def calc_fitness(target, choice):
    diff = 0
    row, col = target.shape
    for i in range(row):
        for j in range(col):
            if target[i, j] != choice[i, j]:
                diff += 1
    return diff


def mutate_gene(genes):
    gene = random.choice(genes)
    return gene


def crossover(parent1, parent2, genes):
    child = np.zeros(shape=parent1.shape, dtype=np.int8)
    row, col = child.shape
    for i in range(row):
        for j in range(col):
            prob = random.random()
            if prob < 0.45:
                child[i, j] = parent1[i, j]
            elif prob < 0.9:
                child[i, j] = parent2[i, j]
            else:
                child[i, j] = mutate_gene(genes)
    return child


if __name__ == "__main__":
    POPULATION_SIZE = 50
    GENES = [0, 1]
    TARGET = np.array([
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ])
    # total population
    population = init_population(
        POPULATION_SIZE,
        GENES,
        TARGET.shape
    )
    # for tracking generation
    generation = 1
    # result found status
    found = False

    while not found:
        # sort the population in asc order
        population = sorted(population, key=lambda x: calc_fitness(TARGET, x))

        # if solution found break
        if calc_fitness(TARGET, population[0]) <= 0:
            found = True
            break

        new_generation = []

        fittest_size = int((20 * POPULATION_SIZE) / 100)

        new_generation.extend(population[:fittest_size])

        remaining_size = int((80 * POPULATION_SIZE) / 100)

        for _ in range(remaining_size):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = crossover(parent1, parent2, GENES)
            new_generation.append(child)

        population = new_generation

        print(
            f'Generation {generation} : Fitness {calc_fitness(TARGET, population[0])}')

        generation += 1

    print(
        f'Generation {generation} : Fitness {calc_fitness(TARGET, population[0])}')
    print("Result:")
    print(population[0])
