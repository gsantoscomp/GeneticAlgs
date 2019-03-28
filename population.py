from individual import Individual


class Population(object):

    # A população é criada com a quantidade de indivíduos já estabelecida
    def __init__(self, quantity: int):
        self.quantity = quantity
        self.individuals = []

    # Verifica se existem indivíduos com genes idênticos
    # dentro da população e retorna uma lista com os indivíduos repetidos
    def equal_individuals(self, individual: Individual):
        for x in self.individuals:
            if x.get_genes() == individual.get_genes():
                return True
        return False

    def change_individuals(self, individuals: list):
        for x in individuals:
            self.individuals[x] = Individual()

    # Gera a quantidade de indivíduos necessária determinada para a população
    def generate_individuals(self):
        i = 0
        while i < self.quantity:
            actual = Individual()
            if not self.equal_individuals(actual):
                self.individuals.append(actual)
                i += 1

    def get_individuals(self):
        for x in self.individuals:
            print(x.get_genes())
