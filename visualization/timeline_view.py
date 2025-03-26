import matplotlib.pyplot as plt
import json

class TimelineView:
    def __init__(self, log_file='event_log.json'):
        self.log_file = log_file

    def load_events(self):
        try:
            with open(self.log_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("No timeline data found.")
            return []

    def plot_timeline(self):
        events = self.load_events()
        years = range(1, len(events) + 1)
        descriptions = [event['description'] for event in events]

        plt.figure(figsize=(12, 6))
        plt.plot(years, [len(desc) for desc in descriptions], marker='o', linestyle='-', color='skyblue')
        plt.xlabel('Year')
        plt.ylabel('Event Complexity (Text Length)')
        plt.title('Historical Timeline Overview')
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    timeline_view = TimelineView()
    timeline_view.plot_timeline()
