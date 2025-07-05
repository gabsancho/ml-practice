from genetic_algorithm import GeneticAlgorithm
from knapsack import Knapsack
from math import floor, pow
from random import random, getrandbits

values = [
  360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
  78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
  87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
  312
]

weights = [
  7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
   42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
   3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
]

"""
Ideas:
 - change crossover method
 - test different fitness functions
 - add population history tracking for debug
 - evaluate population similarities to prevent early convergence
 - visualization
 - change the way new population is generated, making sure each pair
    also generates a new pair of individuals, then they are removed from the
    'parent pool'
"""

if __name__ == '__main__':
    knapsack = Knapsack(850, weights, values)
    def fit(g: list[int]) -> float:
        ok, value, weight = knapsack.test_solution(g)
        return value if ok else pow(2, knapsack.capacity - weight)
    
    def build_solution() -> list[int]:
        return [getrandbits(1) for _ in range(len(knapsack.weights))]
    
    def mutate(g: list[int])-> list[int]:
        """ Flips a single value in the genome. """
        g[floor(random() * len(g))] ^= 1
        return g
    
    def middle_point_crossover(p1: list[int], p2: list[int]) -> list[int]:
        assert len(p1) == len(p2)
        mid = len(p1) >> 1
        return p1[:mid] + p2[mid:]


    runner = GeneticAlgorithm(
        fit,
        build_solution,
        mutate,
        middle_point_crossover,
        300,
        generations=1000,
        mutation_rate=0.09,
        debug=True
    )
    g, f = runner.run()
    assert knapsack.test_solution(g)[0] == True
    # current best solution:
    #   [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
    # with value = 7534.0
    print(g, f)
