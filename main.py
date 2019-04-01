from random import randint
from population import Population

# Criação da população
population = Population(8)

best = population[randint(0, 7)]
counter = 0
while counter < 4:
    # Guarda-se a população ordenada pela função objetiva
    sorted_population = population.get_sorted_population()

    # O primeiro valor da lista é o que tem melhor resultado
    # Neste ponto, deve-se comparar o best atual com o best geral
    best_individual = sorted_population[0]
    if best_individual.objective_function > best.objective_function:
        best = best_individual
        print(best.objective_function)
        counter = 0
    else:
        counter += 1
    # A lista é dividida entre os melhores indivíduos e piores
    population_best_half = sorted_population[:4]
    population_worst_half = sorted_population[4:]

    # Escolhe-se um pai entre os melhores indivíduos e outro entre os piores
    parent1 = population.select_parent(population_best_half)
    parent2 = population.select_parent(population_worst_half)

    population.crossover(parent1, parent2)
    population.mutation([parent1, parent2])

print(best.genes)
