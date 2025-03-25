import matplotlib.pyplot as plt
import numpy as np

class WorldMap:
    def __init__(self, size=(100, 100)):
        self.size = size
        self.terrain = np.random.choice(['Land', 'Water'], size=self.size, p=[0.4, 0.6])

    def generate_map(self):
        plt.figure(figsize=(10, 10))
        cmap = { 'Land': 'sandybrown', 'Water': 'royalblue' }
        map_data = np.vectorize(cmap.get)(self.terrain)
        plt.imshow(map_data, interpolation='nearest')
        plt.title("AIAR World Map")
        plt.axis('off')
        plt.show()

# Example usage
if __name__ == "__main__":
    world_map = WorldMap()
    world_map.generate_map()
