from tkinter import *
import random
import json
from PIL import Image, ImageTk
from tarot_app import TarotApp

with open("tarot_cards.json", "r") as file:
    tarot_data = json.load(file)

cards_list = tarot_data["cards"]

RED = "#e7305b"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
IMAGE_PATH = "tarot_deck/"
IMAGE_SIZE = (180,300)
START_BUTTON_TEXT = " Start Session "

def generate_random_card():
    global card_img # replace global variables with instance attributes - self.card_img in TarotApp
    card = random.choice(cards_list)
    
    #print(card) # {'name': 'Empress', 'image': 'empress.png', 'meaning': 'Abundance, nurturing, and fertility. Represents growth, creativity, and connection to nature. A call to embrace self-care and nurture others with compassion.'}
    #card_img = PhotoImage(file=IMAGE_PATH + card["image"])  
    card_img_raw = Image.open(IMAGE_PATH + card["image"])
    card_img = card_img_raw.resize(IMAGE_SIZE)
    card_img = ImageTk.PhotoImage(card_img)
    canvas.itemconfig(card_image_on_canvas, image=card_img) 
    card_label.config(text="Your card is: " + card["name"] + "\n\n" + card["meaning"])

# OPP implementation
tarot_app = TarotApp()

window = tarot_app.welcome_screen()
canvas = tarot_app.create_canvas()

card_image_on_canvas = tarot_app.card_image_on_canvas(canvas)

card_label = Label(text="",fg=RED, bg=YELLOW, font=(FONT_NAME, 12), wraplength=400, justify="center")
card_label.grid(column=0, row=1, pady=20)

start_button = tarot_app.generate_button(START_BUTTON_TEXT, generate_random_card)

window.mainloop()
