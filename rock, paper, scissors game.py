import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock, Paper, Scissors Game")

        self.player_score = 0
        self.computer_score = 0

        self.choices = ["Rock", "Paper", "Scissors"]

        self.player_choice_label = tk.Label(self.root, text="Your Choice:")
        self.player_choice_label.pack()

        for choice in self.choices:
            tk.Button(self.root, text=choice, width=15, height=2, command=lambda c=choice: self.play_game(c)).pack()

        self.computer_choice_label = tk.Label(self.root, text="Computer's Choice:")
        self.computer_choice_label.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(self.root, text="Score: 0 - 0")
        self.score_label.pack()

        tk.Button(self.root, text="Reset", command=self.reset_game).pack()

    def play_game(self, player_choice):
        computer_choice = random.choice(self.choices)

        result = ""

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Paper" and computer_choice == "Rock") or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.update_labels(player_choice, computer_choice, result)
        self.update_score()

    def update_labels(self, player_choice, computer_choice, result):
        self.player_choice_label.config(text=f"Your Choice: {player_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
        self.result_label.config(text=result)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.player_score} - {self.computer_score}")

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.update_labels("", "", "")
        self.update_score()

    def run(self):
        self.root.mainloop()

# Create an instance of the game and run it
game = RockPaperScissorsGame()
game.run()
