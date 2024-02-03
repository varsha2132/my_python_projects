import random
from tkinter import *
from tkinter import messagebox

class RockPaperScissorsGameGUI():
    def __init__(self, master):
        self.master = master
        self.user_choice = StringVar()
        self.user_score = 0
        self.computer_score = 0

        self.master.title('Rock, Paper, Scissors Game')
        self.master.geometry('300x200')

        self.label_instruction = Label(self.master, text="Choose rock, paper, or scissors:")
        self.label_instruction.pack()

        self.choices = ['Rock', 'Paper', 'Scissors']

        for choice in self.choices:
            button = Button(self.master, text=choice, command=lambda c=choice: self.play_round(c))
            button.pack()

        self.label_result = Label(self.master, text="")
        self.label_result.pack()

        self.label_score = Label(self.master, text="Score: User - 0, Computer - 0")
        self.label_score.pack()

        self.play_again_button = Button(self.master, text="Play Again", command=self.play_again)
        self.play_again_button.pack()

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.label_result.config(text=f"User: {user_choice}, Computer: {computer_choice}\n{result}")

        if result == "You Win!":
            self.user_score += 1
        elif result == "You Lose!":
            self.computer_score += 1

        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            return "You Win!"
        else:
            return "You Lose!"

    def update_score(self):
        self.label_score.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

    def play_again(self):
        self.label_result.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.update_score()

if __name__ == "__main__":
    root = Tk()
    app = RockPaperScissorsGameGUI(root)
    root.mainloop()
