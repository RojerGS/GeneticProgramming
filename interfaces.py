from typing import List
from abc import ABC, abstractmethod

class ASTNode(ABC):
    """Abstract class for the AST nodes.

    These nodes can be terminals or functions.
    Terminals can be seen as constants, while functions combine their children
        to produce their value.
    """

    def __init__(self, *args):
        self.children = []

    @abstractmethod
    def evaluate(self, context = None, *args):
        """Evaluate the value of this node."""
        pass

    @abstractmethod
    def is_leaf(self) -> bool:
        """Returns true if this node is a leaf."""
        pass

    @abstractmethod
    def copy(self) -> "ASTNode":
        """Return a copy of this tree"""
        pass

    @staticmethod
    @abstractmethod
    def get_arity() -> int:
        """Returns the arity of a function or 0 for a terminal."""
        pass

    def __str__(self) -> str:
        """Returns the string representation of the ASTNode."""

        name = self.__class__.__name__
        if self.is_leaf():
            return name
        else:
            children = [str(child) for child in self.children]
            return "{}[{}]".format(name, " ".join(children))

class Terminal(ASTNode):
    """Terminal abstract base class."""

    def __init__(self):
        super().__init__()
        self.value = None

    def evaluate(self, context = None, *args):
        """For terminal nodes, evaluating defaults to returning the value."""
        return self.value

    def is_leaf(self) -> bool:
        return True

    def copy(self) -> "Terminal":
        cls = type(self)
        obj = cls()
        obj.value = self.value
        return obj

    @staticmethod
    def get_arity() -> int:
        return 0

    def __str__(self) -> str:
        """String representation of the terminal."""
        name = self.__class__.__name__
        return "{}({})".format(name, self.value)

class IntTerminal(Terminal):
    """Terminal parent class that evaluates to int."""

    def __init__(self):
        super().__init__()

    def evaluate(self, context = None, *args) -> int:
        """Return the integer self value."""
        return self.value

class FloatTerminal(Terminal):
    """Terminal parent class that evaluates to float."""

    def __init__(self):
        super().__init__()

    def evaluate(self, context = None, *args) -> float:
        """Return the float self value."""
        return self.value

class Function(ASTNode):
    """Function abstract base class."""

    def __init__(self, children: List[ASTNode]):
        """Builds a function node from the children given."""
        super().__init__(children)

        self.children = children

    def is_leaf(self) -> bool:
        return False

    def copy(self) -> "Function":
        """Create a deep copy of this Function ASTNode."""
        children_copies = [child.copy() for child in self.children]
        cls = type(self)
        obj = cls(children_copies)
        return obj

    def evaluate_children(self, context = None, *args) -> None:
        """Evaluates all the children of this function."""

        self.children_values = []
        for child in self.children:
            self.children_values.append(child.evaluate(context, *args))

class UnaryFunction(Function):
    """Base class for unary functions."""

    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    @staticmethod
    def get_arity() -> int:
        return 1

class BinaryFunction(Function):
    """Base class for binary functions."""

    def __init__(self, children: List[ASTNode]):
        super().__init__(children)

    @staticmethod
    def get_arity() -> int:
        return 2