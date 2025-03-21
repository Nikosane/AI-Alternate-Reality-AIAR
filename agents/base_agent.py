import random

class BaseAgent:
    def __init__(self, name, intelligence=1.0, adaptability=1.0):
        self.name = name
        self.intelligence = intelligence
        self.adaptability = adaptability
        self.age = 0

    def evolve(self, environment):
        self.age += 1
        self.intelligence *= (1 + random.uniform(-0.05, 0.1))
        self.adaptability *= (1 + random.uniform(-0.05, 0.1))
        print(f"{self.name} evolved - Intelligence: {self.intelligence:.2f}, Adaptability: {self.adaptability:.2f}")

    def to_dict(self):
        return {
            'name': self.name,
            'intelligence': self.intelligence,
            'adaptability': self.adaptability,
            'age': self.age
        }

    @classmethod
    def from_dict(cls, data):
        agent = cls(data['name'], data['intelligence'], data['adaptability'])
        agent.age = data['age']
        return agent
