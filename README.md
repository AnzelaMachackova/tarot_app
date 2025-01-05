# Tarot Session App

## Manual Setup
If you prefer manually setting up the environment, follow these steps:

Clone the repository: git clone `https://github.com/AnzelaMachackova/tarot_app.git`

Create a virtual environment: `python3 -m venv venv` - ?

Activate the virtual environment: `source venv/bin/activate` - ?

Install dependencies: `pip install -r requirements.txt` - ?

Run the main script: `python main.py`

### TODOs:
1) Implement OPP:
    - Move Logic into TarotApp
    - Create a TarotDeck Class

    Classes:
    - TarotApp: Handles the UI and interaction logic.
    - TarotDeck: Manages card data and random selection.
    - TarotCard: Represents a single card with its attributes (name, image path, meaning).

    Methods:
    - load_deck: Loads card data using TarotDeck.
    - update_card: Updates the UI with a selected card's details.
    - generate_random_card: Calls the TarotDeck to select a random card.

2) Button and text design should be changed.
3) Implement error handling and move dynamic variables (like colors etc.) into a separate configuration file.