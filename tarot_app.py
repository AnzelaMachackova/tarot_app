from tkinter import *
from tkinter.ttk import Style, Button
from PIL import Image, ImageTk

RED = "#1e120f"
YELLOW = "#f0e2cd"
FONT_NAME = "Times New Roman"
WELCOME_TEXT = "Welcome to your\n Tarot Session!"
WELCOME_MESSAGE = (
    "Tarot cards offer guidance and insight, helping you reflect on life’s questions.\n\n"
    "To begin, clear your mind and think about a question or area of life you want to explore.\n\n"
    "When ready, press the button to draw a random tarot card.\n\n"
    "Read the card’s meaning and sllow the card's message to resonate with you, even if it doesn't seem relevant at first. "
    "Remember, tarot is a tool for self-reflection, not prediction.\n\n Enjoy your session!"
)

IMAGE_SIZE = (180, 300)
IMAGE_PATH = "tarot_deck/"

class TarotApp:
    def __init__(self, deck):
        self.window = Tk()
        self.window.title("Tarot Session")
        self.window.config(bg=YELLOW)

        self.window.geometry("400x700")  # Width x Height
        #self.window.resizable(False, False)

        self.deck = deck  # TarotDeck class instance
        self.card_img = None
        self.card_label = None
        self.canvas = None
        self.card_image_on_canvas = None

        self.setup_ui()

    def setup_ui(self):
        # title label
        title_label = Label(text=WELCOME_TEXT, fg=RED, bg=YELLOW,font=(FONT_NAME, 30),justify="center")
        title_label.grid(row=0, column=0, sticky="NSEW", padx=20, pady=20)

        # welcome message
        self.welcome_label = Label(
            text=WELCOME_MESSAGE,
            fg=RED,
            bg=YELLOW,
            font=(FONT_NAME, 14),
            wraplength=300,
            justify="center"
        )
        self.welcome_label.grid(row=1, column=0, pady=10)

        # canvas for card image
        self.canvas = Canvas(width=IMAGE_SIZE[0], height=IMAGE_SIZE[1], bg=YELLOW, highlightthickness=0)
        self.canvas.grid(column=0, row=1, pady=10)
        self.card_image_on_canvas = self.canvas.create_image(90, 150, image=self.card_img)
        self.canvas.grid_remove()

        # label for card details
        self.card_label = Label(text="", fg=RED, bg=YELLOW, font=(FONT_NAME, 12), wraplength=300, justify="center")
        self.card_label.grid(column=0, row=2, padx=10, pady=20)

        # start session button
        style = Style()  
        style.configure(
                'TButton',
                font=(FONT_NAME, 20, 'bold')
                )
        start_button = Button(text="FIND OUT THE FUTURE", command=self.generate_random_card, style='TButton')
        start_button.grid(column=0, row=3, padx=20, pady=20)
        

    def generate_random_card(self):
        if self.welcome_label:
            self.welcome_label.grid_forget()
        self.canvas.grid()
        card = self.deck.draw_random_card()
        try:
            card_img_raw = Image.open(IMAGE_PATH + card["image"])
            resized_img = card_img_raw.resize(IMAGE_SIZE)
            self.card_img = ImageTk.PhotoImage(resized_img)
            self.canvas.itemconfig(self.card_image_on_canvas, image=self.card_img)
        except FileNotFoundError:
            self.card_label.config(text="Image not found for this card.")
            self.card_label.grid()
            return
        
        self.card_label.config(text=f"Your card is: {card['name']}\n\n{card['meaning']}")
