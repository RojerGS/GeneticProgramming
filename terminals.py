from random import random, randint
from interfaces import Terminal

class Zero(IntTerminal):
    """The 0 constant terminal."""
    def __init__(self):
        super().__init__()
        self.value = 0

class One(IntTerminal):
    """The 1 constant terminal."""
    def __init__(self):
        super().__init__()
        self.value = 1

class IntConstant(IntTerminal):
    """A latent constant integer.
    
    When initialized, this terminal assumes a fixed value chosen
        randomly from the range given.
    """
    def __init__(self, min: int = 0, max: int = 1):
        self.value = randint(min, max)

def int_constant_factory(min: int = 0, max: int = 1) -> IntConstant:
    """Creates an IntConstant class with the specified range."""
        
    return lambda: IntConstant(min, max)

class FloatConstant(FloatTerminal):
    """A latent constant float.

    When initialized, this terminal assumes a fixed value chosen
        randomly from the range given.
    """
    def __init__(self, min: float = 0, max: float = 1):
        self.value = random()*(max - min) + min

    def evaluate(self, *args) -> float:
        return self.value