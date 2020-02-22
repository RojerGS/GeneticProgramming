from typing import List
from random import choice

from interfaces import ASTNode, Function, Terminal

def random_tree_full(
    depth: int, functions: List[Function], terminals: List[Terminal]
) -> ASTNode:
    """Creates a random tree with full depth specified by the argument.
    
    Uses the given lists of functions and terminals to build the tree.
    """

    if depth == 1:
        return choice(terminals)

    else:
        func = choice(functions)
        arity = func.get_arity()
        children = []
        for _ in range(arity):
            children.append(random_tree_full(depth - 1, functions, terminals))

        return func(children)

class Simulation(object):
    """Class to hold a whole genetic programming simulation."""

    def __init__(self, terminals, functions):
        self.terminals = terminals
        self.functions = functions

        self.max_generations = 100
        self.current_generation = 0

        self.initialize_population()

    def initialize_population(self):
        """Initialize a random population for an evolutionary run."""
        pass

    def next_generation(self):
        """Performs one generation of the evolutionary algorithm."""
        pass

    def run(self):
        """Run the whole evolutionary simulation until the final generation."""
        
        while self.current_generation < self.max_generations:
            self.next_generation()
            self.current_generation += 1