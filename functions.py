from typing import List
from interfaces import BinaryFunction, ASTNode

class Max(BinaryFunction):
    """Returns the maximum of its two children."""
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context, *args):
        self.evaluate_children(context, *args)
        return max(self.children_values)

class Min(BinaryFunction):
    """Returns the minimum of its two children."""
    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    def evaluate(self, context, *args):
        self.evaluate_children(context, *args)
        return min(self.children_values)