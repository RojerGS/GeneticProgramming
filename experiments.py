from interfaces import *
from terminals import *
from functions import *
from gp_components import *

terminals = [int_constant_factory(0, 10), float_constant_factory(-1, 3)]
functions = [Abs, ProtectedSqrt]

tree = random_tree_full(4, functions, terminals)

print(tree)
print(tree.evaluate())
print(tree.copy())
print(tree.copy() is tree)