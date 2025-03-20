import json
import os
from config import CONFIG
from agents.species import Species
from environment.physics import Physics
from history.timeline import Timeline


def load_universe_state():
    if os.path.exists('universe_state.json'):
        with open('universe_state.json', 'r') as f:
            return json.load(f)
    return None


def save_universe_state(state):
    with open('universe_state.json', 'w') as f:
        json.dump(state, f, indent=4)


def initialize_universe():
    print("Initializing AI - Alternate Reality (AIAR)...")
    physics = Physics(CONFIG['initial_physics'])
    species_list = [Species(f"Species_{i}") for i in range(CONFIG['num_species'])]
    timeline = Timeline()

    state = {
        'physics': physics.to_dict(),
        'species': [species.to_dict() for species in species_list],
        'timeline': timeline.to_dict()
    }
    save_universe_state(state)
    print("Universe Initialized!")


def run_simulation():
    print("Loading AIAR state...")
    state = load_universe_state()
    if state is None:
        print("No previous state found. Initializing new universe.")
        initialize_universe()
        state = load_universe_state()

    print("Starting Simulation...")
    physics = Physics.from_dict(state['physics'])
    species_list = [Species.from_dict(s) for s in state['species']]
    timeline = Timeline.from_dict(state['timeline'])

    for step in range(CONFIG['simulation_steps']):
        print(f"\n--- Simulation Step {step + 1}/{CONFIG['simulation_steps']} ---")
        physics.update()
        for species in species_list:
            species.evolve(physics)
        timeline.record_event(species_list, physics)
        state = {
            'physics': physics.to_dict(),
            'species': [species.to_dict() for species in species_list],
            'timeline': timeline.to_dict()
        }
        save_universe_state(state)

    print("Simulation Completed! State saved to universe_state.json.")


if __name__ == "__main__":
    run_simulation()
