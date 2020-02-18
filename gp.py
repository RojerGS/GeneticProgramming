class Simulation(object):
    """Class to hold a whole genetic programming simulation."""

    def __init__(self, terminals, functions):
        self.terminals = terminals
        self.functions = functions

        self.max_generations = 100
        self.current_generation = 0

        self.initialize_population()

    def initialize_population(self):
        """Initialize a random population for an evolutionary run."""
        pass

    def next_generation(self):
        """Performs one generation of the evolutionary algorithm."""
        pass

    def run(self):
        """Run the whole evolutionary simulation until the final generation."""
        
        while self.current_generation < self.max_generations:
            self.next_generation()
            self.current_generations += 1