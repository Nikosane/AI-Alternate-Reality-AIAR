import ollama

class DecisionEngine:
    def __init__(self, model_name="deepseek_r1_1.5b"):
        self.model_name = model_name

    def make_decision(self, prompt):
        try:
            response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": prompt}])
            decision = response.get('message', {}).get('content', 'No response')
            print(f"AI Decision: {decision}")
            return decision
        except Exception as e:
            print(f"Error in AI Decision Engine: {e}")
            return "Error in decision-making"

# Example usage
if __name__ == "__main__":
    engine = DecisionEngine()
    decision = engine.make_decision("How should the civilization proceed with technological advancements?")
    print(decision)
