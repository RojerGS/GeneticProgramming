from typing import List
from interfaces import BinaryFunction, ASTNode

class Max(BinaryFunction):
    """Returns the maximum of its two children."""
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context = None, *args):
        self.evaluate_children(context, *args)
        return max(self.children_values)

class Min(BinaryFunction):
    """Returns the minimum of its two children."""
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context = None, *args):
        self.evaluate_children(context, *args)
        return min(self.children_values)

class Addition(BinaryFunction):
    """Returns the sum of its two children."""
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context = None, *args):
        self.evaluate_children(context, *args)
        return self.children_values[0] + self.children_values[1]

class Subtraction(BinaryFunction):
    """Returns difference between the lift and right children."""
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context = None, *args):
        self.evaluate_children(context, *args)
        return self.children_values[0] - self.children_values[1]

class Product(BinaryFunction):
    """Returns the product of two numbers."""
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context = None, *args):
        self.evaluate_children(context, *args)
        return self.children_values[0] * self.children_values[1]

class ProtectedDivision(BinaryFunction):
    """Returns the protected division of the first children by the second.

    The protected division of `a` with `b` is `a/b` if `b != 0`, else is `0`.
    """
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context = None, *args):
        """If the right child is 0, return 0, otherwise do left/right."""
        self.evaluate_children(context, *args)
        if self.children_values[1]:
            return self.children_values[0] / self.children_values[1]
        else:
            return 0