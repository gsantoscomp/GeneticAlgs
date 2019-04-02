from random import randint
from population import Population

# Criação da população
print("Início da população:")
population = Population(8)
print([values.genes for values in population])

best = population[randint(0, 7)]
print("Cromossomo sorteado: ", best.genes, '\n')

counter = 0
while counter < 4:
    # Guarda-se a população ordenada pela função objetiva
    sorted_population = population.get_sorted_population()

    # O primeiro valor da lista é o que tem melhor resultado
    # Neste ponto, deve-se comparar o best atual com o best geral
    best_individual = sorted_population[0]
    print("Melhor cromossomo na população:", best_individual.genes, "FO =", best_individual.objective_function)
    if best_individual.objective_function > best.objective_function:
        best = best_individual
        print("O melhor cromossomo dessa população é maior que o cromossomo geral:", best.objective_function, '\n')
        counter = 0
    else:
        print("O melhor cromossomo dessa população não é maior que o cromossomo geral:", best.objective_function, '\n')
        counter += 1
    # A lista é dividida entre os melhores indivíduos e piores
    population_best_half = sorted_population[:4]
    print("Melhor metade da população:", [value.genes for value in population_best_half])
    print("Porcentagens acumuladas, para o sorteio do pai na melhor metade:")
    parent1 = population.select_parent(population_best_half)
    print("Pai escolhido na melhor metade:", parent1.genes, '\n')

    population_worst_half = sorted_population[4:]
    print("Pior metade da população:", [value.genes for value in population_worst_half])
    print("Porcentagens acumuladas, para o sorteio do pai na pior metade:")
    parent2 = population.select_parent(population_worst_half)
    print("Pai escolhido na pior metade:", parent2.genes, '\n')

    population.crossover(parent1, parent2)
    population.mutation([parent1, parent2])

print("Melhor cromossomo escolhido:", best.genes, "FO:", best.objective_function)
