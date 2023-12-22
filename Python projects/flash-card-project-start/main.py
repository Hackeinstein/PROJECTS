from tkinter import *
from tkinter import messagebox
from pandas import *
import random


# dataframe and read file
try:
    df = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = read_csv("./data/french_words.csv")
except Exception as ex:
    messagebox.showinfo(title="Flash", message=ex)

df_dict = df.to_dict(orient="records")
# set globals
item=""
itm_fr = "French"
itm_en = "English Word"
BACKGROUND_COLOR = "#B1DDC6"
index=""


def flip_card():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=itm_en, fill="white")
    canvas.itemconfig(canvas_img, image=card_back)


def next_card():
    global itm_fr, itm_en, flip_timer,index,item
    window.after_cancel(flip_timer)
    try:
        index = random.randint(0, len(df_dict) - 1)
        item = df_dict[index]
        itm_fr = item["French"]
        itm_en = item["English"]
    except ValueError:
        messagebox.showinfo(title="Flash", message="You've learnt all words")

    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=itm_fr, fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, flip_card)


# wrong btn function
def wrong_select():
    next_card()


# right btn function
def right_select():
    next_card()
    try:
        df_dict.remove(item)
    except ValueError:
        messagebox.showinfo(title="Flash",message="You've learnt all words")
    finally:
        data = DataFrame(df_dict)
        data.to_csv("./data/words_to_learn.csv",index=False)




# card flipping


window = Tk()
window.title("Flashcard")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(4000,next_card)
# canvas
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 264, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
# canvas text
language_label = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word in French", font=("Ariel", 60, "bold"))

# buttons
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=wrong_select)
wrong_btn.grid(row=1, column=0)
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=right_select)
right_btn.grid(row=1, column=1)

window.mainloop()
