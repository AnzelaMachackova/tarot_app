from tkinter import *
import random
import json
from PIL import Image, ImageTk

with open("tarot_cards.json", "r") as file:
    tarot_data = json.load(file)

cards_list = tarot_data["cards"]

RED = "#e7305b"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WELCOME_TEXT = "Welcome to your\n Tarot Session!"
IMAGE_PATH = "tarot_deck/"
IMAGE_SIZE = (180,300)

def generate_random_card():
    global card_img
    card = random.choice(cards_list)
    #print(card) # {'name': 'Empress', 'image': 'empress.png', 'meaning': 'Abundance, nurturing, and fertility. Represents growth, creativity, and connection to nature. A call to embrace self-care and nurture others with compassion.'}
    #card_img = PhotoImage(file=IMAGE_PATH + card["image"])  
    card_img_raw = Image.open(IMAGE_PATH + card["image"])
    card_img = card_img_raw.resize(IMAGE_SIZE)
    card_img = ImageTk.PhotoImage(card_img)
    canvas.itemconfig(card_image_on_canvas, image=card_img) 
    card_label.config(text="Your card is: " + card["name"] + "\n\n" + card["meaning"])

def start_session():
    pass

window = Tk()
window.title("Tarot Session")
window.config(bg=YELLOW)

title_label = Label(text=WELCOME_TEXT, fg=RED, bg=YELLOW, font=(FONT_NAME, 30))
title_label.grid(row=0, column=0, sticky="NW", padx=10, pady=10)

# canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
# canvas.grid(column=0, row=1)  

canvas = Canvas(width=180, height=300, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1,  pady=10)

card_img = None  
card_image_on_canvas = canvas.create_image(90, 150, image=card_img)


card_label = Label(text="",fg=RED, bg=YELLOW, font=(FONT_NAME, 12), wraplength=400, justify="center")
card_label.grid(column=0, row=1, pady=20)

#TODO change button design 
start_button = Button(text=" Start Session ", highlightthickness=0, command=generate_random_card)
start_button.grid(column=0, row=2, pady=10) 


window.mainloop()
