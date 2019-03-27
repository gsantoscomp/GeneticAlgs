from individual import Individual


class Population(object):

    def __init__(self, quantity: int):
        self.quantity = quantity
        self.individuals = []

    # Verifica se existem indivíduos com genes idênticos
    # dentro da população e retorna uma lista com os indivíduos repetidos
    def compare_individuals(self):
        aux_list = self.individuals
        repeated_genes = []

        for i in range(7):
            for j in range(i+1, 8):
                if aux_list[i].get_genes() == self.individuals[j].get_genes():
                    repeated_genes.append(j)

        return repeated_genes

    # Gera a quantidade de indivíduos necessária determinada para a população
    def generate_individuals(self):
        for i in range(self.quantity):
            self.individuals.append(Individual())

    def get_individuals(self):
        for x in self.individuals:
            print(x.get_genes())


