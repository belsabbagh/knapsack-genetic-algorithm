# Knapsack Genetic Algorithm

This is a simple implementation of a genetic algorithm to solve the knapsack problem. The knapsack problem is a combinatorial optimization problem that is NP-hard. The problem is to find the best combination of items to put in a knapsack so that the total value of the items is maximized while the total weight is less than or equal to the capacity of the knapsack.

## Structure of the code

### class Individual

This class represents an individual in the population. It has a chromosome, which is a list of 0s and 1s. It implements basic binary crossover and mutation functions that are used by the genetic algorithm.

#### class KnapsackIndividual

This is a subclass of `Individual` used by the `KnapsackGeneticAlgorithm` class. The chromosome is a list of 0s and 1s. The length of the chromosome is the number of items in the problem. A 0 in the chromosome means that the item is not in the knapsack, and a 1 means that the item is in the knapsack. The fitness of the individual is the total value of the items in the knapsack. The KnapsackIndividual class doesn't override any methods from the Individual class.

### class GeneticAlgorithm

This is the base class for the genetic algorithm. It initializes with all the parameters of the problem, including but not limited to:

- the fitness function
- the crossover function which defaults to single-point crossover
- the mutation function which defaults to bit-flip mutation
- the selection function
- the population size
- the number of generations
- the number of elite individuals
- the number of parents to select for crossover

The `run` method runs the genetic algorithm and returns evolved individuals in the end.

#### class KnapsackGeneticAlgorithm

This is a subclass of `GeneticAlgorithm` that overrides the fitness function which returns the total value of the items in an Individual's knapsack.
