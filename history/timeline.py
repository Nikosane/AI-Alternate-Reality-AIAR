import json

class EventLog:
    def __init__(self, log_file='event_log.json'):
        self.log_file = log_file
        self.events = []

    def log_event(self, description, involved_species=None, event_type="General"):
        event = {
            'description': description,
            'involved_species': involved_species or [],
            'event_type': event_type
        }
        self.events.append(event)
        self.save_log()
        print(f"Event Logged: {description}")

    def save_log(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.events, f, indent=4)

    def load_log(self):
        try:
            with open(self.log_file, 'r') as f:
                self.events = json.load(f)
        except FileNotFoundError:
            print("No previous event log found. Starting fresh.")

    def to_dict(self):
        return self.events

# Example usage
if __name__ == "__main__":
    log = EventLog()
    log.log_event("A new civilization has emerged.", ["Species_X"], "Civilization")
