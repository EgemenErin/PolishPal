from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

#check whether if data exists
if os.path.exists("./data/words_to_learn.csv"):
    data = pd.read_csv("./data/words_to_learn.csv")
else:
    data = pd.read_csv("./data/polish_words.csv")

# load data
polish_words = data.to_dict(orient="records")
current_word = {}

def show_random_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)  # Cancel any scheduled flip
    current_word = random.choice(polish_words)
    canvas.itemconfig(card_title, text="Polish", fill="black")
    canvas.itemconfig(card_word, text=current_word["Polish"], fill="black")
    canvas.itemconfig(card_image, image=logo_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_image, image=logo_img_back)

def known_word():
    global polish_words
    polish_words.remove(current_word)
    pd.DataFrame(polish_words).to_csv("./data/words_to_learn.csv", index=False)
    show_random_word()


#initialize the main window
window = Tk()
window.title("Polish Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

#create PhotoImage objects
try:
    logo_img = PhotoImage(file="./images/card_front.png")
    logo_img_back = PhotoImage(file="./images/card_back.png")
    right_button_img = PhotoImage(file="./images/right.png")
    wrong_button_img = PhotoImage(file="./images/wrong.png")
except TclError:
    print("Error: One or more image files not found.")
    exit()

#create and configure the canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=logo_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#create and place the buttons
right_button = Button(image=right_button_img, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=show_random_word)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(3000, func=flip_card)

#start the window
show_random_word()
window.mainloop()
