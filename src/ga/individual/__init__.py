"""
This module contains the Individual class.
"""


import random


class Individual(object):
    """Individual class."""

    def __init__(self, chromosome: list = None):
        if chromosome is None:
            chromosome = []
        self._chromosome = chromosome
        """Initialize the Individual class."""

    def get_chromosome(self):
        """Return the chromosome of the individual."""
        return self._chromosome

    @classmethod
    def random_population(cls, size: int, target_size, genes):
        """Create a random population of individuals."""
        return [cls([random.choice(genes) for _ in range(target_size)]) for _ in range(size)]

    @staticmethod
    def _create_child_chromosome(c1, c2):
        child1, child2 = [], []
        for gp1, gp2 in zip(c1, c2):
            prob = random.random()
            if prob < 0.5:
                child1.append(gp1)
                child2.append(gp2)
            else:
                child1.append(gp2)
                child2.append(gp1)
        return child1, child2

    @classmethod
    def mate(cls, par1, par2):
        '''
        Perform mating and produce new offspring
        '''
        c1, c2 = cls._create_child_chromosome(
            par1.get_chromosome(), par2.get_chromosome())
        return cls(c1), cls(c2)

    def __add__(self, other):
        return self.__class__.mate(self, other)
    
    @classmethod
    def mutate(cls, x):
        index = random.randint(0, len(x.get_chromosome()) - 1)
        x.get_chromosome()[index] = 1 - x.get_chromosome()[index]
        return x


class KnapsackIndividual(Individual):
    def __init__(self, chromosome: list = None):
        super().__init__(chromosome)

    @classmethod
    def random_population(cls, size: int, genes):
        """Create a random population of individuals."""
        return [cls([random.choice([0, 1]) for _ in range(len(genes))]) for _ in range(size)]

    def __add__(self, other):
        return self.__class__.mate(self, other)

    def render_items(self, items):
        return [items[i] for i, x in enumerate(self.get_chromosome()) if x == 1]

    def fitness(self, items):
        return sum([x[1] for x in self.render_items(items)])

    def weight(self, items):
        return sum([x[0] for x in self.render_items(items)])

    def render(self, items) -> str:
        d = {'Weight': self.weight(items), 'Value': self.fitness(items)}
        return f"{d}"
