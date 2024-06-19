import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("500x450")
        self.root.config(bg="#1E1F26")
        
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0
        
        # Title Label
        self.title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 24, "bold"), fg="#FFD700", bg="#1E1F26")
        self.title_label.pack(pady=10)
        
        # Frame for Buttons
        self.button_frame = tk.Frame(root, bg="#1E1F26")
        self.button_frame.pack(pady=20)
        
        # Player Choice Buttons
        self.rock_button = tk.Button(self.button_frame, text="Rock", font=("Helvetica", 15, "bold"), fg="#FFFFFF", bg="#FF6347", width=10, command=lambda: self.play("Rock"))
        self.rock_button.grid(row=0, column=0, padx=20, pady=20)
        
        self.paper_button = tk.Button(self.button_frame, text="Paper", font=("Helvetica", 15, "bold"), fg="#FFFFFF", bg="#4682B4", width=10, command=lambda: self.play("Paper"))
        self.paper_button.grid(row=0, column=1, padx=20, pady=20)
        
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", font=("Helvetica", 15, "bold"), fg="#FFFFFF", bg="#32CD32", width=10, command=lambda: self.play("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=20, pady=20)
        
        # Score Labels
        self.score_frame = tk.Frame(root, bg="#1E1F26")
        self.score_frame.pack(pady=10)
        
        self.user_score_label = tk.Label(self.score_frame, text="Your Score: 0", font=("Helvetica", 15, "bold"), fg="#FFD700", bg="#1E1F26")
        self.user_score_label.grid(row=0, column=0, padx=20)
        
        self.computer_score_label = tk.Label(self.score_frame, text="Computer's Score: 0", font=("Helvetica", 15, "bold"), fg="#FFD700", bg="#1E1F26")
        self.computer_score_label.grid(row=0, column=1, padx=20)
        
        # Result Label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), fg="#FFD700", bg="#1E1F26")
        self.result_label.pack(pady=20)
    
    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, computer_choice)
        
        self.result_label.config(text=f"Your Choice: {player_choice}\nComputer's Choice: {computer_choice}\nResult: {result}")
        self.update_score(result)
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a Tie!"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            return "You Win!"
        else:
            return "Computer Wins!"
    
    def update_score(self, result):
        if result == "You Win!":
            self.user_score += 1
            self.user_score_label.config(text=f"Your Score: {self.user_score}")
        elif result == "Computer Wins!":
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer's Score: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
