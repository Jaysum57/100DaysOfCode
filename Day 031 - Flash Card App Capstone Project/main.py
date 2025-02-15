from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"

random_word = {}

try: # reading words to learn csv
    french_words_df = pd.read_csv("./data/words_to_learn.csv")
    
except (FileNotFoundError, pd.errors.EmptyDataError): # No words to learn csv or empty words to learn csv
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = french_words_df.to_dict(orient="records")


# -------------------- Button Press --------------------
def next_card():
    global random_word

    try:
        random_word = rand.choice(to_learn)
    except IndexError:
        canvas.itemconfig(title_card, text="")
        canvas.itemconfig(word_card, text="")
        messagebox.showinfo(title="No more words to learn", message="There are no more words to learn! :)")
    else:
        print(random_word)
        window.after(3000, func=flip_card)
        canvas.itemconfig(face_card, image=card_front_img)
        canvas.itemconfig(title_card, text="French", fill="black")
        canvas.itemconfig(word_card, text=random_word["French"], fill="black")
    
# -------------------- Flip Card --------------------

def flip_card():
    canvas.itemconfig(face_card, image=card_back_img)
    canvas.itemconfig(title_card, text="English", fill="white")
    canvas.itemconfig(word_card, text=random_word["English"],fill="white")

# -------------------- Known Card --------------------

def is_known():
    try:
        to_learn.remove(random_word)
    except ValueError:
        pass
    else:
        to_learn_df = pd.DataFrame(to_learn)
        to_learn_df.to_csv('./data/words_to_learn.csv', index=False)
        next_card()

# -------------------- UI --------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

# Canvas Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")

face_card = canvas.create_image(400, 263, image=card_front_img)

title_card = canvas.create_text(400,150, text="French", font=("Arial", 40, "italic"))
word_card = canvas.create_text(400,263, text="trouve", font=("Arial", 60, "bold"))

canvas.grid(column=0,row=0,columnspan=2)


# Buttons
right_button_img = PhotoImage(file="./images/right.png")
wrong_button_img = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right_button_img, highlightthickness=0, bd=0, command=is_known)
right_button.grid(column=1,row=1)

wrong_button = Button(image=wrong_button_img, highlightthickness=0, bd=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()


