from tkinter import *
from tkinter.ttk import Style, Button
from PIL import Image, ImageTk
from config import Config

class TarotApp:
    def __init__(self, deck):
        self.window = Tk()
        self.window.title("Tarot Session")
        self.window.config(bg=Config.YELLOW)

        self.window.geometry("400x700")
        #self.window.resizable(False, False)

        self.deck = deck  # TarotDeck class instance
        self.card_img = None
        self.card_label = None
        self.canvas = None
        self.card_image_on_canvas = None

        self.setup_ui()

    def setup_ui(self):
        # title label
        title_label = Label(
            text=Config.WELCOME_TEXT, 
            fg=Config.RED, 
            bg=Config.YELLOW,
            font=(Config.FONT_NAME, 30),
            justify="center"
        )
        title_label.grid(row=0, column=0, sticky="NSEW", padx=20, pady=20)

        # welcome message
        self.welcome_label = Label(
            text=Config.WELCOME_MESSAGE,
            fg=Config.RED,
            bg=Config.YELLOW,
            font=(Config.FONT_NAME, 14),
            wraplength=300,
            justify="center"
        )
        self.welcome_label.grid(row=1, column=0, pady=10)

        # canvas for card image
        self.canvas = Canvas(
            width=Config.IMAGE_SIZE[0], 
            height=Config.IMAGE_SIZE[1], 
            bg=Config.YELLOW, 
            highlightthickness=0
        )
        self.canvas.grid(column=0, row=1, pady=10)
        self.card_image_on_canvas = self.canvas.create_image(90, 150, image=self.card_img)
        self.canvas.grid_remove()

        # label for card details
        self.card_label = Label(
            text="", 
            fg=Config.RED, 
            bg=Config.YELLOW, 
            font=(Config.FONT_NAME, 12), 
            wraplength=300, 
            justify="center"
        )
        self.card_label.grid(column=0, row=2, padx=10, pady=20)

        # start session button
        style = Style()  
        style.configure(
                'TButton',
                font=(Config.FONT_NAME, 20, 'bold')
                )
        start_button = Button(text=Config.BUTTON_TEXT, command=self.generate_random_card, style='TButton')
        start_button.grid(column=0, row=3, padx=20, pady=20)
        

    def generate_random_card(self):
        if self.welcome_label:
            self.welcome_label.grid_forget()
        self.canvas.grid()
        card = self.deck.draw_random_card()
        try:
            card_img_raw = Image.open(Config.IMAGE_PATH + card["image"])
            resized_img = card_img_raw.resize(Config.IMAGE_SIZE)
            self.card_img = ImageTk.PhotoImage(resized_img)
            self.canvas.itemconfig(self.card_image_on_canvas, image=self.card_img)
        except FileNotFoundError:
            self.card_label.config(text="Image not found for this card.")
            self.card_label.grid()
            return
        
        self.card_label.config(text=f"Your card is: {card['name']}\n\n{card['meaning']}")
