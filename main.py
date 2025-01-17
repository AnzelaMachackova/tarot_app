from tarot_app import TarotApp
from tarot_deck import TarotDeck

# initialize the Tarot Deck and Tarot App
deck = TarotDeck("tarot_cards.json")
app = TarotApp(deck)

app.window.mainloop()
