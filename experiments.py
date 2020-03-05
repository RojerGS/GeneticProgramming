from interfaces import *
from terminals import *
from functions import *
from gp_components import *

terminals = [int_constant_factory(0, 10), float_constant_factory(-1, 3)]
functions = [Abs, ProtectedSqrt, Addition, Product]

left = random_tree_full(3, functions, terminals)
right = random_tree_full(3, functions, terminals)

print(left)
print(right)
print(tree_crossover(left, right))
print(tree_crossover(left, right))