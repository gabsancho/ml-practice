import random
from typing import Callable, List, Tuple, Any

class GeneticAlgorithm:
    """ Genetic algorithm definition """
    def __init__(
        self,
        fitness_fn: Callable[[Any], float],
        create_genome_fn: Callable[[], Any],
        mutate_fn: Callable[[Any], Any],
        crossover_fn: Callable[[Any, Any], Any],
        population_size: int = 100,
        elite_size: int = 1,
        mutation_rate: float = 0.01,
        generations: int = 100,
        debug: bool = False
    ):
        self.fitness_fn = fitness_fn
        self.create_genome_fn = create_genome_fn
        self.mutate_fn = mutate_fn
        self.crossover_fn = crossover_fn
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.debug = debug
    
    def _select_parents(self, population: List[Any], weights: List[float]) -> Tuple[Any, Any]:
        parents = random.choices(population, weights=weights, k=2)
        return parents[0], parents[1]

    def run(self) -> Tuple[Any, float]:
        population = [self.create_genome_fn() for _ in range(self.population_size)]

        for generation in range(self.generations):
            fitness_scores = [self.fitness_fn(genome) for genome in population]

            sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
            elite = [genome for genome, _ in sorted_population[:self.elite_size]]

            total_fitness = sum(fitness_scores)
            if total_fitness == 0:
                weights = [1] * self.population_size  # prevent divide-by-zero
            else:
                weights = [f / total_fitness for f in fitness_scores]

            new_population = elite.copy()
            while len(new_population) < self.population_size:
                parent1, parent2 = self._select_parents(population, weights)
                child = self.crossover_fn(parent1, parent2)
                if random.random() < self.mutation_rate:
                    child = self.mutate_fn(child)
                new_population.append(child)

            population = new_population

            if self.debug:
                best_fitness = sorted_population[0][1]
                print(f"Generation {generation}: Best fitness = {best_fitness}")

        best_genome, best_fitness = sorted_population[0]
        return best_genome, best_fitness
