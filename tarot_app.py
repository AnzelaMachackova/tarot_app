from tkinter import *

RED = "#e7305b"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WELCOME_TEXT = "Welcome to your\n Tarot Session!"

class TarotApp:
    def __init__(self):
        self.window = Tk()
        self.card_img = None 

    def create_canvas(self):
        canvas = Canvas(width=180, height=300, bg=YELLOW, highlightthickness=0)
        canvas.grid(column=1, row=1,  pady=10)
        return canvas

    def welcome_screen(self):
        self.window.title("Tarot Session")
        self.window.config(bg=YELLOW)

        title_label = Label(text=WELCOME_TEXT, fg=RED, bg=YELLOW, font=(FONT_NAME, 30))
        title_label.grid(row=0, column=0, sticky="NW", padx=10, pady=10)
        return self.window
    
    def card_image_on_canvas(self, canvas):
        card_image_on_canvas = canvas.create_image(90, 150, image=self.card_img)
        return card_image_on_canvas
    
    def generate_button(self, text, command):
        #TODO change button design 
        button = Button(text=text, highlightthickness=0, command=command)
        button.grid(column=0, row=2, pady=10) 
