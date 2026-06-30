import csv
import random
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

base_dir = Path(__file__).parent
csv_path = base_dir / "assets" / "companies.csv"
print(csv_path)

with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    companies = list(reader)

print(companies)

root = tk.Tk()
root.geometry("500x500")
root.title("Guess the Company")
label = tk.Label(root, text = "Who is this")


size = len(companies)

randomPick = random.randint(0, size - 1)
prev = randomPick

#first time set up
company = companies[randomPick]
image_name = company["logo"]
image_path = base_dir / image_name

img = Image.open(image_path)
scale = 0.03
new_width = int(img.width * scale)
new_height = int(img.height * scale)
img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(img)
image_label = tk.Label(root, image=photo)
image_label.image = photo
image_label.pack()


def show_image(path):
    img = Image.open(path)
    scale = 0.03
    new_width = int(img.width * scale)
    new_height = int(img.height * scale)
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo
    print("inside show image " + str(path))

def newPickEachTime(size, prev_pick):
    pick = random.randint(0, size - 1)
    while pick == prev_pick:
        pick = random.randint(0, size - 1)
    prev_pick = pick
    return pick

def randomRun(companies):
    size = len(companies)
    global randomPick 
    randomPick = newPickEachTime(len(companies), prev)
    print("randomRun is " + str(randomPick))

def pickRandom(companies):
    company = companies[randomPick]
    image_name = company["logo"]
    image_path = base_dir / image_name
    show_image(image_path)



countdownTimer = 10
timer_label = tk.Label(root, text="10")
timer_label.pack()
answer_label = tk.Label(root)
answer_label.pack()
label.pack()

next_button = tk.Button(root, text="Next", font=("Helvetica", 20), command=lambda: next_question())

def countdown():
    global countdownTimer
    timer_label.config(text=str(countdownTimer))
    if countdownTimer > 0:
        countdownTimer -= 1
        root.after(1000, countdown)
    else:
        company = companies[randomPick]
        answer_label.config(text=company["name"])
        next_button.pack()


def next_question():
    #grab a new random int 
    randomRun(companies)
    #get a company object from that int
    pickRandom(companies)
    answer_label.config(text="")
    next_button.pack_forget()
    global countdownTimer
    countdownTimer = 10
    countdown()


countdown()    
root.mainloop()