from interfaces import *
from terminals import *
from functions import *
from gp_components import *

terminals = [int_constant_factory(0, 10), float_constant_factory(-1, 3)]
functions = [Addition, Subtraction, Product, ProtectedDivision]

tree = random_tree_full(2, functions, terminals)

print(tree)
print(tree.evaluate())