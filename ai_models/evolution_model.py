import random

class EvolutionModel:
    def __init__(self):
        pass

    def simulate_genetic_evolution(self, species):
        mutation_factor = random.uniform(0.95, 1.05)
        species.intelligence *= mutation_factor
        species.adaptability *= mutation_factor
        print(f"{species.name} - Intelligence: {species.intelligence:.2f}, Adaptability: {species.adaptability:.2f}")

    def simulate_societal_evolution(self, society):
        society.culture_level *= random.uniform(0.98, 1.03)
        society.military_power *= random.uniform(0.97, 1.04)
        print(f"{society.name} - Culture: {society.culture_level:.2f}, Military Power: {society.military_power:.2f}")

# Example usage
if __name__ == "__main__":
    from agents.species import Species
    from agents.society import Society

    species = Species("NeoSapiens")
    society = Society("NeoSapiens Empire", species.name)

    model = EvolutionModel()
    model.simulate_genetic_evolution(species)
    model.simulate_societal_evolution(society)
