#import

# Simple Rock, Paper, Scissors GUI using Tkinter
import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")

high_score = {"wins": 0}
player_score = {"Player": 0, "Computer": 0}

score_label = tk.Label(root, text="Player: 0  Computer: 0")
score_label.pack()

high_score_label = tk.Label(root, text="High Score (Wins): 0")
high_score_label.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

def update_scores(result):
    if result == "You win!":
        player_score["Player"] += 1
    elif result == "Computer wins!":
        player_score["Computer"] += 1
    score_label.config(text=f"Player: {player_score['Player']}  Computer: {player_score['Computer']}")

def update_high_score(result):
    if result == "You win!":
        high_score["wins"] += 1
        high_score_label.config(text=f"High Score (Wins): {high_score['wins']}")

def determine_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif (
        (player == "Rock" and computer == "Scissors") or
        (player == "Scissors" and computer == "Paper") or
        (player == "Paper" and computer == "Rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You: {player_choice}\nComputer: {computer_choice}\n{result}")
    update_scores(result)
    update_high_score(result)

tk.Label(root, text="Choose:").pack()

button_frame = tk.Frame(root)
button_frame.pack()

for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(button_frame, text=choice, width=10, command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)

root.mainloop()
