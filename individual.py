from random import randint


class Individual(object):

    # Genes podem ser automaticamente gerados
    # Ou podem ter seus valores definidos via parâmetro

    def __init__(self, genes: list = 0):
        if genes:
            self.genes = genes
        else:
            self.genes = [randint(0, 1) for x in range(5)]

    def get_genes(self):
        return self.genes
