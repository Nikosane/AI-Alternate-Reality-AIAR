import networkx as nx
import matplotlib.pyplot as plt
import json

class SocietyGraph:
    def __init__(self, society_data_file='society_data.json'):
        self.society_data_file = society_data_file
        self.graph = nx.Graph()

    def load_society_data(self):
        try:
            with open(self.society_data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("No society data found.")
            return []

    def build_graph(self):
        societies = self.load_society_data()
        for society in societies:
            self.graph.add_node(society['name'])
            for neighbor, relation in society['relationships'].items():
                self.graph.add_edge(society['name'], neighbor, weight=relation)

    def visualize_graph(self):
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights)
        plt.title("Society Relationship Graph")
        plt.show()

# Example usage
if __name__ == "__main__":
    graph = SocietyGraph()
    graph.build_graph()
    graph.visualize_graph()
