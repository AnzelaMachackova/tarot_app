import json
import random

class TarotDeck:
    def __init__(self, file_path):
        self.cards = []
        self.load_deck(file_path)

    def load_deck(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                if "cards" not in data:
                    raise ValueError("Invalid file format: Missing 'cards' key.")
                self.cards = data["cards"]
                print(f"Successfully loaded {len(self.cards)} cards.")
        except Exception as e:
            print(f"Error: {e}")
            
    def draw_random_card(self):
        if not self.cards:
            raise ValueError("The Tarot deck is empty.")
        self.current_card = random.choice(self.cards)
        return self.current_card

    # def reset_deck(self):
    #     self.current_card = None
