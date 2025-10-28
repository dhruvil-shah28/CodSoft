import tkinter as tk
import random

root=tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("440x480")
root.config(bg="#e8ebf7")

CHOICES=["Rock", "Paper", "Scissors"]
EMOJIS={"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

user_score=0
computer_score=0
tie_score=0

def determine_winner(user_choice,computer_choice):
    """Return the result text."""
    if user_choice==computer_choice:
        return "It's a tie!"
    elif (user_choice=="Rock" and computer_choice=="Scissors") or \
         (user_choice=="Paper" and computer_choice=="Rock") or \
         (user_choice=="Scissors" and computer_choice=="Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play(user_choice):
    """Triggered when user clicks a choice."""
    global user_score,computer_score, tie_score

    computer_choice=random.choice(CHOICES)
    result=determine_winner(user_choice,computer_choice)

    result_label.config(
        text=f"🧍 You: {EMOJIS[user_choice]} {user_choice}\n💻 Computer: {EMOJIS[computer_choice]} {computer_choice}\n\n➡️ {result}",fg="#333"
    )

    if result=="You win!":
        user_score += 1
    elif result=="Computer wins!":
        computer_score += 1
    else:
        tie_score += 1

    score_label.config(
        text=f"You: {user_score}  |  Computer: {computer_score}  |  Tie: {tie_score}"
    )

    toggle_choice_buttons(state="disabled")
    play_again_btn.pack(pady=15)

def reset_game():
    """Reset scores and UI."""
    global user_score, computer_score,tie_score
    user_score=0
    computer_score=0
    tie_score=0
    score_label.config(text="You: 0  |  Computer: 0  |  Tie: 0")
    result_label.config(text="Make your move!", fg="#444")
    toggle_choice_buttons(state="normal")
    play_again_btn.pack_forget()

def play_again():
    """Start a new round (does not reset scores)."""
    result_label.config(text="Make your move!",fg="#444")
    toggle_choice_buttons(state="normal")
    play_again_btn.pack_forget()

def toggle_choice_buttons(state):
    """Enable or disable all choice buttons."""
    rock_btn.config(state=state)
    paper_btn.config(state=state)
    scissors_btn.config(state=state)

title_label= tk.Label(
    root,
    text="Rock-Paper-Scissors 🎮",
    font=("Segoe UI", 20, "bold"),
    bg="#e8ebf7",
    fg="#2b2d42"
)
title_label.pack(pady=15)

result_frame=tk.Frame(root, bg="#e8ebf7")
result_frame.pack(pady=20)

result_label= tk.Label(
    result_frame,
    text="Make your move!",
    font=("Segoe UI", 14),
    bg="#e8ebf7",
    fg="#444",
    justify="center"
)
result_label.pack()

button_frame= tk.Frame(root, bg="#e8ebf7")
button_frame.pack(pady=15)

btn_style={
    "width":10,
    "font":("Segoe UI", 12, "bold"),
    "bg":"#8ecae6",
    "fg":"white",
    "activebackground":"#219ebc",
    "activeforeground":"white",
    "relief": "ridge",
    "bd":3
}

rock_btn=tk.Button(button_frame,text="🪨 Rock", command=lambda: play("Rock"),**btn_style)
paper_btn=tk.Button(button_frame,text="📄 Paper", command=lambda: play("Paper"),**btn_style)
scissors_btn=tk.Button(button_frame, text="✂️ Scissors", command=lambda: play("Scissors"), **btn_style)

rock_btn.grid(row=0,column=0,padx=10)
paper_btn.grid(row=0,column=1,padx=10)
scissors_btn.grid(row=0,column=2,padx=10)

score_label= tk.Label(
    root,
    text="You: 0  |  Computer: 0  |  Tie: 0",
    font=("Segoe UI", 13, "bold"),
    bg="#e8ebf7",
    fg="#2b2d42"
)
score_label.pack(pady=20)

play_again_btn= tk.Button(
    root,
    text="🔁 Play Again",
    command=play_again,
    bg="#90be6d",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=15,
    relief="ridge",
    bd=3
)

play_again_btn.pack_forget()

reset_btn=tk.Button(
    root,
    text="⏹ Reset Scores",
    command=reset_game,
    bg="#ef233c",
    fg="white",
    font=("Segoe UI",12,"bold"),
    width=15,
    relief="ridge",
    bd=3
)
reset_btn.pack(pady=10)
root.mainloop()
