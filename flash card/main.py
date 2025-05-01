import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
words={}



try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    words=original_data.to_dict(orient='records')

else:
    words=data.to_dict(orient='records')


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(words)
    c.itemconfig(card_title,text="French",fill="black")
    c.itemconfig(card_word,text=current_card["French"],fill="black")
    c.itemconfig(card_background, image=card_image_french)
    flip_timer=window.after(3000,func=flip_card)



def flip_card():
    c.itemconfig(card_title,text="English",fill="white")
    c.itemconfig(card_word,text=current_card["English"],fill="white")
    c.itemconfig(card_background,image=card_image_english)

def is_known():
    words.remove(current_card)
    data=pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()









window=Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

flip_timer=window.after(3000,func=flip_card)

card_image_french=PhotoImage(file="./images/card_front.png")
card_image_english=PhotoImage(file="images/card_back.png")
c=Canvas(height=526,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
card_background=c.create_image(400,263,image=card_image_french)
card_title=c.create_text(400,150,text="",font=("Ariel",40,"italic") )
card_word=c.create_text(400,263,text="",font=("Ariel",60,"bold") )
c.grid(row=0,column=0,columnspan=2)

wrong_image=PhotoImage(file="./images/wrong.png")
wrong_btn=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_btn.grid(row=1,column=0)

right_image=PhotoImage(file="./images/right.png")
right_btn=Button(image=right_image,highlightthickness=0,command=is_known)
right_btn.grid(row=1,column=1)


next_card()













window.mainloop()