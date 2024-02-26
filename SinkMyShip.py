
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

global root
root = tk.Tk()
root.title("Don't Sink the Boat - Miss 3 questions and you will SINK the boat!")
root.geometry('600x600')
root.config(background = "green")
style = Style(theme="flatly")

style.configure("TLabel", font=("Helvetica", 30))
style.configure("TButton", font=("Helvetica", 30))

question_label = ttk.Label(
    root,
    font = ("Ariel", 30),
    anchor="center",
    wraplength=500,
    padding=10
)
question_label.pack(pady=10)

choice_btns =[]
for i in range(4):
    button = ttk.Button(root, command=lambda i=i: check_answer(i))
    button.pack(pady=10)
    choice_btns.append(button)


feedback_label = ttk.Label(
    root,
    font = ("Ariel", 25),
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)


score_label=ttk.Label(
    root,
    font = ("Ariel", 25),
    text="SAFE",
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

boats = ["Space", "\+--/", "\++-/", "\+++/"]
incorrect_answers = 0

def show_question():
    question = quiz_data[current_question]
    question_label.config(text=question["question"])

    choice = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choice[i], state="normal")
    
    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    global incorrect_answers
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        feedback_label.config(text="CORRECT!", foreground="green")
        score_label.config(text="SAFE")
    else:
        incorrect_answers+=1
        feedback_label.config(text="Boat pattern: {}".format(boats[incorrect_answers]), foreground="red")
        score_label.config(text="INCORRECT")

        if incorrect_answers == len(boats)-1:
            messagebox.showinfo("Complete", "Your Sank Your Boat!")
            root.destroy()

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")


def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        show_question()
    else: 
        messagebox.showinfo("Complete", "Your Boat Survived!")
        root.destroy()


next_btn = ttk.Button(
    root,
    text= "NEXT",
    command = next_question,
    state ="disabled"
)
next_btn.pack(pady=10)

current_question = 0
#first question
show_question()

root.mainloop()
