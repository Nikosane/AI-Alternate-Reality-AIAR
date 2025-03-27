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

    def generate_society(self, species_name):
        name = random.choice(self.society_names)
        culture_level = round(random.uniform(1.0, 5.0), 2)
        military_power = round(random.uniform(0.5, 3.0), 2)
        return {"name": name, "species_name": species_name, "culture_level": culture_level, "military_power": military_power}


# Example usage
if __name__ == "__main__":
    randomizer = Randomizer()
    species = randomizer.generate_species()
    print("Generated Species:", species)
    society = randomizer.generate_society(species["name"])
    print("Generated Society:", society)
