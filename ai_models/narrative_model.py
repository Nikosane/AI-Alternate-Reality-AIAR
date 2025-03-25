import ollama

class NarrativeModel:
    def __init__(self, model_name="deepseek_r1_1.5b"):
        self.model_name = model_name

    def generate_story(self, civilization_data):
        prompt = f"Create a detailed narrative for a civilization with the following characteristics: {civilization_data}" 
        try:
            response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": prompt}])
            story = response.get('message', {}).get('content', 'No story generated')
            print("Generated Story:")
            print(story)
            return story
        except Exception as e:
            print(f"Error in Narrative Generation: {e}")
            return "Error generating story"

# Example usage
if __name__ == "__main__":
    narrative_model = NarrativeModel()
    civilization_data = {
        'name': 'Eldoria',
        'culture_level': 3.5,
        'military_power': 2.0,
        'population': 150000
    }
    narrative_model.generate_story(civilization_data)
