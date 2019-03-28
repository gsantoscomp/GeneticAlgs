from individual import Individual


class Population(object):

    # A população é criada com a quantidade de indivíduos já estabelecida
    def __init__(self, quantity: int):
        self.quantity = quantity
        self.individuals = []

    def __getitem__(self, individual):
        return self.individuals[individual]

    # Verifica se existem indivíduos com genes idênticos
    # dentro da população e retorna uma lista com os indivíduos repetidos
    def equal_individuals(self, individual: Individual):
        for x in self.individuals:
            if x.get_all_genes() == individual.get_all_genes():
                return True
        return False

    # Gera a quantidade de indivíduos necessária determinada para a população
    def generate_individuals(self):
        i = 0
        while i < self.quantity:
            actual = Individual()
            if (actual.check_viability()) and (not self.equal_individuals(actual)):
                self.individuals.append(actual)
                i += 1

    def get_individuals(self):
        for x in self.individuals:
            print(x.get_all_genes())
