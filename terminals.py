from random import random, randint
from interfaces import Terminal

class Zero(Terminal):
    """The 0 constant terminal."""
    def __init__(self):
        pass

    def evaluate(self, *args) -> int:
        return 0

class One(Terminal):
    """The 1 constant terminal."""
    def __init__(self):
        pass

    def evaluate(self, *args) -> int:
        return 1

class IntConstant(Terminal):
    """A latent constant integer.
    
    When initialized, this terminal assumes a fixed value chosen
        randomly from the range given.
    """
    def __init__(self, min: int = 0, max: int = 1):
        self.value = randint(min, max)

    def evaluate(self, *args) -> int:
        return self.value

class FloatConstant(Terminal):
    """A latent constant float.

    When initialized, this terminal assumes a fixed value chosen
        randomly from the range given.
    """
    def __init__(self, min: float = 0, max: float = 1):
        self.value = random()*(max - min) + min

    def evaluate(self, *args) -> float:
        return self.value