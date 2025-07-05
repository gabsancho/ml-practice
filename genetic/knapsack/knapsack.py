class Knapsack():
    """ Defines an instance of a binary Knapsack problem """
    def __init__(self, capacity, weights, values):
        self.capacity = capacity
        self.weights = weights
        self.values = values

        if not self.is_valid():
            raise RuntimeError('Problem setup is not valid.')
    
    def is_valid(self):
        return ((self.capacity is not None)
                and isinstance(self.capacity, int)
                and (self.capacity > 0)
                and isinstance(self.weights, (list))
                and isinstance(self.values, (list))
                and len(self.weights) == len(self.values))
    
    def test_solution(self, solution):
        if len(solution) != len(self.weights):
            raise RuntimeError(f'Given solution does not match dimensionality, {len(self.weights)} != {len(solution)}.')
        
        v = w = 0.0
        for i in range(len(solution)):
            if solution[i] == 1:
                v += self.values[i]
                w += self.weights[i]

        return w <= self.capacity, v, w
    
    def __str__(self):
        return f"""Knapsack with capacity = {self.capacity} and {len(self.weights)} possible items"""
