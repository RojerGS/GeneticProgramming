from typing import List, Union
from random import choice, randint

from interfaces import ASTNode, Function, Terminal

def random_tree_full(
    depth: int, functions: List[Function], terminals: List[Terminal]
) -> ASTNode:
    """Creates a random tree with full depth specified by the argument.
    
    Uses the given lists of functions and terminals to build the tree.
    """

    if depth == 1:
        terminal = choice(terminals)
        return terminal()

    else:
        func = choice(functions)
        arity = func.get_arity()
        children = []
        for _ in range(arity):
            children.append(random_tree_full(depth - 1, functions, terminals))

        return func(children)

def tree_crossover(left: ASTNode, right: ASTNode) -> ASTNode:
    """Creates a tree by joining together two parts, one from each arg tree.

    Randomly and uniformly picks a point from the left tree and cuts the subtree
    rooted at the chosen point; call that point A.
    Randomly and uniformly picks a point from the right tree and extracts the
    subtree rooted at that point; call that tree T.
    Inserts tree T at the point A and returns a copy of that.
    """

    left = left.copy()
    right = right.copy()

    right_size = len(right)
    node_idx = randint(1, right_size)
    # Do a "depth-first search" counting the nodes as they are traversed
    # This performs a search from right to left
    stack = [right]
    count = 0
    while stack:
        subtree = stack.pop()
        count += 1
        if count == node_idx:
            # Have the `right` variable point to the subtree T
            right = subtree
            break

        if not subtree.is_leaf():
            for child in subtree.children:
                stack.append(child)
    # If the stack became empty without breaking from the while raise an error
    else:
        raise ValueError(
            "Exhausted tree when looking for the {}th node.".format(node_idx)
        )

    left_size = len(left)
    node_idx = randint(1, left_size)
    # If node_idx is 1 then we substitute the whole tree with `right`
    if node_idx == 1:
        return right

    # Do a similar "depth-first search", but now we increment the counter
    ## as soon as we touch a children, before adding it to the stack.
    # This makes it easier to replace the correct subtree with `right`.
    stack = [left]  # This stack will only contain non-leaf nodes
    count = 1
    while stack:
        subtree = stack.pop()
        for idx, child in enumerate(subtree.children):
            # This `child` is the `count`th node, is this the node we want?
            count += 1
            if count == node_idx:
                subtree.children[idx] = right
                return left

            if not child.is_leaf():
                stack.append(child)
    else:
        raise ValueError(
            "Exhausted tree when looking for the {}th node.".format(node_idx)
        )

    return left

class Simulation(object):
    """Class to hold a whole genetic programming simulation."""

    def __init__(self, functions, terminals):
        self.functions = functions
        self.terminals = terminals

        self.population_size = 100
        self.max_generations = 100
        self.current_generation = 0

        self.initialize_population()

    def initialize_population(self):
        """Initialize a random population for an evolutionary run."""
        self.population = random_tree_full(3, self.functions, self.terminals)

    def next_generation(self):
        """Performs one generation of the evolutionary algorithm."""
        pass

    def run(self):
        """Run the whole evolutionary simulation until the final generation."""
        
        while self.current_generation < self.max_generations:
            self.next_generation()
            self.current_generation += 1