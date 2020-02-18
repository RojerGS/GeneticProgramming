from abc import ABC, abstractmethod

class Terminal(ABC):
    """Terminal abstract base class."""

    @abstractmethod
    def evaluate(self, context):
        pass

class Function(ABC):
    """Function abstract base class."""

    def __init__(self, arity):
        self.arity = arity

    @abstractmethod
    def evaluate(self, context, *args):
        pass

class ASTNode(object):
    """Abstract Syntax Tree class to represent the programs.

    A node can have an arbitrary number of children, including 0.
    """

    def __init__(self, children = None):
        self.children = children

    def is_leaf(self):
        """Boolean method returning True if this node is a leaf."""
        return len(self.children) == 0