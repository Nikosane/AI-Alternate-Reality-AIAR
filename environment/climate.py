import random

class Climate:
    def __init__(self, base_temperature=300, variability=10):
        self.base_temperature = base_temperature
        self.variability = variability

    def simulate_weather(self):
        # Simulate temperature fluctuations
        temperature = self.base_temperature + random.uniform(-self.variability, self.variability)
        weather_conditions = ["Sunny", "Rainy", "Stormy", "Snowy"]
        current_weather = random.choice(weather_conditions)

        print(f"Weather: {current_weather}, Temperature: {temperature:.2f} K")
        return {'weather': current_weather, 'temperature': temperature}

    def to_dict(self):
        return {
            'base_temperature': self.base_temperature,
            'variability': self.variability
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['base_temperature'], data['variability'])
