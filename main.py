"""Main module for the genetic algorithm project."""

from src.ga import KnapsackGeneticAlgorithm
from src.ga.individual import KnapsackIndividual

if __name__ == '__main__':
    ga = KnapsackGeneticAlgorithm(
        items=[
            [1, 2],
            [2, 4],
            [3, 4],
            [4, 5],
            [5, 7],
            [6, 9]
        ],
        max_weight=10,
        crossover=lambda x, y: x + y,
        mutate=lambda x: KnapsackIndividual.mutate(x),
        select=lambda x: x[:int(len(x)*0.05)]
    )
    population = KnapsackIndividual.random_population(20, ga.items)
    res = ga.run(population, 200, debug=True)
    print(f"Answer: {res[0].render(ga.items)}")
