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

# Write code below 💖
'''
repeat = 1

while repeat != 0:
    print("===================\nRock Paper Scissors\n===================\n")

    user_input = input("Pick (r)ock, (p)aper, or (s)cissors: ").lower()
    if user_input == 'r': player = 1
    elif user_input == 'p': player = 2
    elif user_input == 's': player = 3
    else:
        print("Invalid input, please enter r, p, or s.")
        continue

    computer = random.randint(1,3)  

    if player == 1 and computer == 2:
        print("You chose: ✊\nCPU chose: ✋\nThe CPU won!")
    elif player == 2 and computer == 1:
        print("You chose: ✋\nCPU chose: ✊\nThe player won!")
    elif player == 3 and computer == 2:
        print("You chose: ✌️\nCPU chose: ✋\nThe player won!")
    elif player == 2 and computer == 3:
        print("You chose: ✋\nCPU chose: ✌️\nThe CPU won!")
    elif player == 1 and computer == 3:
        print("You chose: ✊\nCPU chose: ✌️\nThe player won!")
    elif player == 3 and computer == 1:
        print("You chose: ✌️\nCPU chose: ✊\nThe CPU won!")
    else:
        print("Same choice, draw")


    # Allow user to enter 'r', 'p', or 's' as input
    # Map input to corresponding number for game logic
    # (1 = Rock, 2 = Paper, 3 = Scissors)

    # To implement this, replace the player input section above with:
    # user_input = input("Pick (r)ock, (p)aper, or (s)cissors: ").lower()
    # if user_input == 'r': player = 1
    # elif user_input == 'p': player = 2
    # elif user_input == 's': player = 3
    # else: handle invalid input

    # Example implementation:
    # (Place this code above the game logic where player is set)

    # --- Begin replacement code ---
    # print("1) ✊\n2) ✋\n3) ✌️")
    # user_input = input("Pick (r)ock, (p)aper, or (s)cissors: ").lower()
    # if user_input == 'r':
    #     player = 1
    # elif user_input == 'p':
    #     player = 2
    # elif user_input == 's':
    #     player = 3
    # else:
    #     print("Invalid input, please enter r, p, or s.")
    #     continue
    # --- End replacement code ---

'''

