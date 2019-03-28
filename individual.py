from random import randint


class Individual(object):

    # Genes podem ser automaticamente gerados
    # Ou podem ter seus valores definidos via parâmetro

    def __init__(self, genes: list = 0):
        if genes:
            self.genes = genes
        else:
            self.genes = [randint(0, 1) for x in range(5)]

        self.objective_function = 0
        values = [20, 15, 60, 35, 10]

        for i in range(5):
            self.objective_function += self.genes[i] * values[i]

    def __getitem__(self, gene):
        return self.genes[gene]

    # Verifica se a restrição é obedecida
    # A soma dos pesos das sacolas não deve ultrapassar 90kg
    def check_viability(self):
        weights = [30, 20, 50, 35, 15]
        result = 0

        for i in range(5):
            result += weights[i] * self[i]

        if result > 90:
            return False
        return True
