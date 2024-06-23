import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
# french_words = []
# new_dict = {row.French: row.English for (index, row) in data.iterrows()}
# french_words.append(new_dict)
else:
    to_learn = data.to_dict(orient="records")


def card_flip():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"])


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=card_flip)

 
def known_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 265, text="", font=("Ariel", 60, "bold"))

cancel_image = PhotoImage(file='E:/codes/Python/projects/flash card project/images/wrong.png')
button_cancel = Button(image=cancel_image, highlightthickness=0, command=next_card)
button_cancel.grid(column=0, row=1)

right_image = PhotoImage(file='E:/codes/Python/projects/flash card project/images/right.png')
button_right = Button(image=right_image, highlightthickness=0, command=known_card)
button_right.grid(column=1, row=1)

next_card()

window.mainloop()

