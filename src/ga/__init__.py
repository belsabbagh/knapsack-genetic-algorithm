"""
Genetic Algorithm
"""
from .__base import GeneticAlgorithm
from .individual import Individual


GeneticAlgorithm = GeneticAlgorithm


class KnapsackGeneticAlgorithm(GeneticAlgorithm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = kwargs.get('items')
        self.max_weight = kwargs.get('max_weight')
        self.guard_self()

    def fitness(self, individual):
        chromosome = individual.get_chromosome()
        total_weight = 0
        total_value = 0
        for i in range(len(chromosome)):
            if chromosome[i] == 1:
                total_weight += self.items[i][0]
                total_value += self.items[i][1]
        return total_value if total_weight <= self.max_weight else 0

    def guard_self(self):
        if self.items is None:
            raise ValueError('items must be provided')
        if self.max_weight is None:
            raise ValueError('max_weight must be provided')
        if self.max_weight <= 0:
            raise ValueError('max_weight must be non-negative')

    def run(self, population: list[Individual], generations, debug: bool = False):
        self.guard_self()
        pool = population
        """Run the Genetic Algorithm."""
        for gen_i in range(1, generations + 1):
            pool = sorted(pool, key=lambda x: self.fitness(x), reverse=True)
            best_individual = pool[0]
            if debug:
                print(self._log_msg(gen_i, best_individual, self.fitness(best_individual), len(pool)))
            pool = self._new_pool(pool)
        return sorted(pool, key=lambda x: self.fitness(x), reverse=True)
