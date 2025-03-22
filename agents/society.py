class Society:
    def __init__(self, name, species_name, culture_level=1.0, military_power=1.0):
        self.name = name
        self.species_name = species_name
        self.culture_level = culture_level
        self.military_power = military_power
        self.relationships = {}

    def interact(self, other_society):
        if other_society.name not in self.relationships:
            self.relationships[other_society.name] = random.uniform(-1, 1)
        interaction_score = self.relationships[other_society.name]

        if interaction_score > 0:
            print(f"{self.name} maintains a positive relationship with {other_society.name}")
        else:
            print(f"{self.name} has a hostile relationship with {other_society.name}")

    def evolve(self):
        self.culture_level *= 1 + random.uniform(-0.02, 0.05)
        self.military_power *= 1 + random.uniform(-0.03, 0.04)

    def to_dict(self):
        return {
            'name': self.name,
            'species_name': self.species_name,
            'culture_level': self.culture_level,
            'military_power': self.military_power,
            'relationships': self.relationships
        }

    @classmethod
    def from_dict(cls, data):
        society = cls(data['name'], data['species_name'], data['culture_level'], data['military_power'])
        society.relationships = data['relationships']
        return society
