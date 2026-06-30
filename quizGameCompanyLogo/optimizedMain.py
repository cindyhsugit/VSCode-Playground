import csv
import random
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "assets" / "companies.csv"
SCALE = 0.03
TIME_LIMIT = 10

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    companies = list(csv.DictReader(f))

root = tk.Tk()
root.title("Guess the Company")
root.geometry("500x500")

title_label = tk.Label(root, text="Who is this")
title_label.pack()

image_label = tk.Label(root)
image_label.pack()

timer_label = tk.Label(root, text=str(TIME_LIMIT))
timer_label.pack()

answer_label = tk.Label(root)
answer_label.pack()

next_button = tk.Button(root, text="Next")
next_button.pack_forget()

current_pick = None
countdown_timer = TIME_LIMIT

def show_image(path):
    img = Image.open(path)
    new_size = (int(img.width * SCALE), int(img.height * SCALE))
    photo = ImageTk.PhotoImage(img.resize(new_size, Image.Resampling.LANCZOS))
    image_label.config(image=photo)
    image_label.image = photo

def pick_new_company():
    global current_pick
    choices = list(range(len(companies)))
    if current_pick is not None and len(choices) > 1:
        choices.remove(current_pick)
    current_pick = random.choice(choices)
    company = companies[current_pick]
    show_image(BASE_DIR / company["logo"])
    answer_label.config(text="")
    next_button.pack_forget()
    return company

def countdown():
    global countdown_timer
    timer_label.config(text=str(countdown_timer))
    if countdown_timer > 0:
        countdown_timer -= 1
        root.after(1000, countdown)
    else:
        answer_label.config(text=companies[current_pick]["name"])
        next_button.pack()

def next_question():
    global countdown_timer
    countdown_timer = TIME_LIMIT
    pick_new_company()
    countdown()

next_button.config(command=next_question)

pick_new_company()
countdown()
root.mainloop()