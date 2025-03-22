from .base_agent import BaseAgent
import random

class Species(BaseAgent):
    def __init__(self, name, intelligence=1.0, adaptability=1.0, population=1000):
        super().__init__(name, intelligence, adaptability)
        self.population = population

    def evolve(self, environment):
        super().evolve(environment)
        # Population growth or decline based on environmental factors
        survival_rate = max(0.1, 1.0 - abs(environment['temperature'] - 300) / 1000)
        growth_factor = (self.adaptability * survival_rate * random.uniform(0.8, 1.2))
        self.population = max(10, int(self.population * growth_factor))

        print(f"{self.name} population: {self.population}")

    def to_dict(self):
        data = super().to_dict()
        data['population'] = self.population
        return data

    @classmethod
    def from_dict(cls, data):
        species = cls(data['name'], data['intelligence'], data['adaptability'], data['population'])
        species.age = data['age']
        return species
