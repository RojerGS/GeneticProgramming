from interfaces import *
from terminals import *
from functions import *
from gp_components import *

terminals = [int_constant_factory(0, 10), Zero]
functions = [Addition, Subtraction]

tree = random_tree_full(3, functions, terminals)

print(tree)
print(tree.evaluate())