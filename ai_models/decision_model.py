import ollama

class DecisionModel:
    def __init__(self, model_name="deepseek_r1_1.5b"):
        self.model_name = model_name

    def generate_decision(self, prompt):
        try:
            response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": prompt}])
            decision = response.get('message', {}).get('content', 'No response generated')
            print(f"Decision Generated: {decision}")
            return decision
        except Exception as e:
            print(f"Error in Decision Model: {e}")
            return "Error in decision generation"

# Example usage
if __name__ == "__main__":
    model = DecisionModel()
    print(model.generate_decision("Should civilization A form an alliance with civilization B?"))
