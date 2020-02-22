from typing import List
from abc import ABC, abstractmethod

class ASTNode(ABC):
    """Abstract class for the AST nodes.

    These nodes can be terminals or functions.
    Terminals can be seen as constants, while functions combine their children
        to produce their value.
    """

    @abstractmethod
    def evaluate(self, context, *args):
        """Evaluate the value of this node."""
        pass

    @abstractmethod
    def is_leaf(self) -> bool:
        """Returns true if this node is a leaf."""
        pass

    @staticmethod
    @abstractmethod
    def get_arity() -> int:
        """Returns the arity of a function or 0 for a terminal."""
        pass

class Terminal(ASTNode):
    """Terminal abstract base class."""

    def is_leaf(self) -> bool:
        return True

    @staticmethod
    def get_arity() -> int:
        return 0

class Function(ASTNode):
    """Function abstract base class."""

    def __init__(self, children: List[ASTNode]):
        """Builds a function node from the children given."""
        self.children = children

    def is_leaf(self) -> bool:
        return False

    def evaluate_children(self, context, *args) -> None:
        """Evaluates all the children of this function."""

        self.children_values = []
        for child in self.children:
            self.children_values.append(child.evaluate(context, *args))

class UnaryFunction(Function):
    """Base class for unary functions."""

    def __init__(self, children: List[ASTNode]):
        super().__init__(self, children)

    @staticmethod
    def get_arity() -> int:
        return 1

class BinaryFunction(Function):
    """Base class for binary functions."""

    def __init__(self, children: List[ASTNode]):
        super().__init__(self, children)

    @staticmethod
    def get_arity() -> int:
        return 2