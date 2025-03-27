import random

class Randomizer:
    def __init__(self):
        self.species_names = ["NeoSapiens", "Aetherians", "Luminites", "Terranoids"]
        self.society_names = ["Empire of Dawn", "Celestial Dominion", "Iron Pact", "Solar Federation"]

    def generate_species(self):
        name = random.choice(self.species_names)
        intelligence = round(random.uniform(0.5, 2.0), 2)
        adaptability = round(random.uniform(0.5, 2.0), 2)
        population = random.randint(1000, 50000)
        return {"name": name, "intelligence": intelligence, "adaptability": adaptability, "population": population}
