import random
from individual import Individual


class Population(object):

    # A população é criada com a quantidade de indivíduos já estabelecida
    # Verifica-se também as restrições de cada indivíduo e se existem indivíduos repetidos
    def __init__(self, quantity: int):
        self.individuals = []
        i = 0
        while i < quantity:
            actual = Individual()
            if (actual.check_viability()) and (not self.equal_individuals(actual)):
                self.individuals.append(actual)
                i += 1

    def __getitem__(self, individual):
        return self.individuals[individual]

    # Verifica se existem indivíduos com genes idênticos
    # dentro da população e retorna uma lista com os indivíduos repetidos
    def equal_individuals(self, individual: Individual):
        for x in self.individuals:
            if x.genes == individual.genes:
                return True
        return False

    # Retorna uma lista com os objetos Individuals ordenados pelo valor da função objetiva
    def get_sorted_population(self):
        sorted_population = []
        index_sorted_individual = []
        index_value_dict = {}
        counter = 0

        # Associa o id do indivíduo ao valor da sua função objetiva dentro
        # dentro do dicionário "index_value_dict"
        for individual in self.individuals:
            index_value_dict[counter] = individual.objective_function
            counter += 1

        # Ordena o dicionário a partir do valor da função objetiva
        sorted_list = sorted(index_value_dict.items(),
                             key=lambda value: value[1],
                             reverse=True)

        # Guarda os ids dos indivíduos ordenados
        for individual in sorted_list:
            index_sorted_individual.append(individual[0])

        # Cria uma nova lista com os indíviduos ordenados
        for index in index_sorted_individual:
            sorted_population.append(self.individuals[index])

        return sorted_population

    def select_parent(self, selected_individuals):
        values_list = [value.objective_function for value in selected_individuals]
        total = sum(values_list)
        accumulated_percentages = []

        percentage = 0
        for value in values_list:
            percentage += (value/total)*100
            accumulated_percentages.append(percentage)

        chosen = 0
        random_number = random.uniform(0, 100)
        for chance in accumulated_percentages:
            if random_number > chance:
                chosen += 1

        return selected_individuals[chosen]

    def crossover(self, parent1: Individual, parent2:Individual):
        gene_parent1 = random.randint(0, 4)
        gene_parent2= random.randint(0, 4)

        print(gene_parent1, gene_parent2)

    def get_individuals(self):
        for individual in self.individuals:
            print(individual.genes)
