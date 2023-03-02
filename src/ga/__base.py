import random
from typing import Callable

from src.ga.individual import Individual


class GeneticAlgorithm(object):
    """Genetic Algorithm class."""

    _fitness: Callable[[Individual], float] = None
    _crossover: Callable[[list[Individual]], list[Individual]] = None
    _mutate: Callable[[Individual], Individual] = None
    _select: Callable[[list[Individual]], list[Individual]] = None

    def __init__(self, **kwargs):
        """Initialize the Genetic Algorithm class."""
        self._fitness = kwargs.get('fitness')
        self._crossover = kwargs.get('crossover')
        self._mutate = kwargs.get('mutate')
        self._select = kwargs.get('select')

    @classmethod
    def create(
        cls,
        validate: callable = None,
        fitness: Callable[[Individual, any], float] = None,
        crossover=None,
        mutate=None,
        select=None
    ):
        """Create a Genetic Algorithm object."""
        if not issubclass(cls, GeneticAlgorithm):
            raise TypeError(
                f"{cls} is not a subclass of GeneticAlgorithm.")
        return cls(**cls.build_attributes(
            validate, fitness, crossover, mutate, select))

    @staticmethod
    def build_attributes(
        validate: callable,
        fitness: Callable[[Individual, any], float],
        crossover,
        mutate,
        select
    ):
        """Initialize the default attributes."""
        return {
            'validate': validate if validate is not None else lambda x: True,
            'fitness': fitness if fitness is not None else lambda x, y: 0,
            'crossover': crossover if crossover is not None else lambda x, y: x,
            'mutate': mutate if mutate is not None else lambda x: x,
            'select': select if select is not None else lambda x: x[:int(len(x)*0.05)]
        }

    def get_fitness(self):
        return self._fitness

    def get_crossover(self):
        return self._crossover

    def get_mutate(self):
        return self._mutate

    def get_select(self):
        return self._select

    def _check_params(self, population, generations, zero_best, log, reverse):
        if zero_best and reverse:
            raise ValueError('Cannot set zero_best and reverse to True.')

    def run(
        self,
        population: list[Individual],
        generations,
        zero_best: bool = True,
        debug: bool = False,
        max_fitness: bool = False
    ):
        self._check_params(population, generations,
                           zero_best, debug, max_fitness)
        pool = population
        """Run the Genetic Algorithm."""
        for gen_i in range(1, generations+1):
            pool = sorted(pool, key=lambda x: self._fitness(x),
                          reverse=max_fitness)
            best_ind = pool[0]
            best_score = self._fitness(best_ind)
            if debug:
                print(self._log_msg(gen_i, best_ind, best_score, len(pool)))
            if zero_best and best_score <= 0:
                return [pool[0]]
            pool = self._new_pool(pool)
        return pool

    def _reproduce(self, parents: list[Individual]):
        """Create a new generation of individuals."""
        new_gen = []
        for _ in range(len(parents)):
            kids = self._crossover(random.choice(parents), random.choice(parents))
            new_gen.append(kids[0])
            new_gen.append(kids[1])
        return [self._mutate(ind) for ind in new_gen]

    def _log_msg(self, generation, best: Individual, fitness_score, pool_size):
        """Generate a log message."""
        return f'Gen {generation}:\tBest: {"".join([str(i) for i in best.get_chromosome()])}\tFitness: {fitness_score}\tPool: {pool_size}'

    @staticmethod
    def _get_ratio(population: list[Individual], ratio: float):
        """Return the fittest individual in the population."""
        return population[:int(len(population)*ratio)]

    def _new_pool(self, pool: list[Individual]):
        """Create a new pool of individuals."""
        return self._reproduce(self._get_ratio(pool, 0.5))
