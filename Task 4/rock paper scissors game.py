import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("430x700")
        self.root.configure(bg="#0D1B2A")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

        self.player_name = ""

        # SCORE VARIABLES
        self.wins = 0
        self.losses = 0
        self.draws = 0

        self.build_name_screen()

    # -------------------------------
    def build_name_screen(self):
        self.clear_window()

        title = tk.Label(self.root, text="Rock Paper Scissors",
                         font=("Poppins", 26, "bold"), fg="white", bg="#0D1B2A")
        title.pack(pady=40)

        card = tk.Frame(self.root, bg="#1B263B")
        card.pack(pady=20, ipadx=25, ipady=25)

        lbl = tk.Label(card, text="Enter Your Name",
                       font=("Poppins", 18), bg="#1B263B", fg="#E0E1DD")
        lbl.pack(pady=10)

        self.name_entry = tk.Entry(card, font=("Poppins", 18),
                                   bg="#E0E1DD", fg="#0D1B2A",
                                   relief="flat", width=18)
        self.name_entry.pack(pady=10)

        start_btn = tk.Button(card, text="Start Game", font=("Poppins", 16, "bold"),
                              bg="#415A77", fg="white",
                              activebackground="#778DA9", width=14,
                              relief="flat", command=self.start_game)
        start_btn.pack(pady=15)

    # -------------------------------
    def start_game(self):
        name = self.name_entry.get().strip()
        if name == "":
            name = "Player"
        self.player_name = name
        self.build_game_screen()

    # -------------------------------
    def build_game_screen(self):
        self.clear_window()

        title = tk.Label(self.root, text=f"{self.player_name} vs Computer",
                         font=("Poppins", 22, "bold"), bg="#0D1B2A", fg="#E0E1DD")
        title.pack(pady=25)

        # Result
        self.result_label = tk.Label(self.root, text="", font=("Poppins", 26, "bold"),
                                     bg="#0D1B2A", fg="white")
        self.result_label.pack(pady=10)

        # Player Labels
        self.player_label = tk.Label(self.root, text="You:",
                                     font=("Poppins", 18), bg="#0D1B2A", fg="#E0E1DD")
        self.player_label.pack(pady=5)

        self.computer_label = tk.Label(self.root, text="Computer:",
                                       font=("Poppins", 18), bg="#0D1B2A", fg="#E0E1DD")
        self.computer_label.pack(pady=5)

        # Buttons Container
        btn_card = tk.Frame(self.root, bg="#1B263B")
        btn_card.pack(pady=40, ipadx=10, ipady=10)

        def make_btn(symbol, text, choice, col):
            btn = tk.Button(btn_card, text=symbol, font=("Poppins", 45),
                            bg="#415A77", fg="white", width=3, relief="flat",
                            activebackground="#778DA9",
                            command=lambda: self.play(choice))
            btn.grid(row=0, column=col, padx=20, pady=5)

            label = tk.Label(btn_card, text=text, font=("Poppins", 16, "bold"),
                             bg="#1B263B", fg="#E0E1DD")
            label.grid(row=1, column=col, padx=20, pady=5)

        make_btn("🪨", "Rock", "Rock", 0)
        make_btn("📄", "Paper", "Paper", 1)
        make_btn("✂️", "Scissors", "Scissors", 2)

        # SCOREBOARD FRAME
        score_frame = tk.Frame(self.root, bg="#1B263B")
        score_frame.pack(pady=20, ipadx=10, ipady=10)

        self.win_label = tk.Label(score_frame, text="Wins: 0",
                                  font=("Poppins", 16, "bold"), bg="#1B263B", fg="#2A9D8F")
        self.win_label.grid(row=0, column=0, padx=15, pady=5)

        self.loss_label = tk.Label(score_frame, text="Losses: 0",
                                   font=("Poppins", 16, "bold"), bg="#1B263B", fg="#E63946")
        self.loss_label.grid(row=0, column=1, padx=15, pady=5)

        self.draw_label = tk.Label(score_frame, text="Draws: 0",
                                   font=("Poppins", 16, "bold"), bg="#1B263B", fg="#F4A261")
        self.draw_label.grid(row=0, column=2, padx=15, pady=5)

        # RESET BUTTON
        reset_btn = tk.Button(self.root, text="Reset Score", font=("Poppins", 15, "bold"),
                              bg="#E63946", fg="white",
                              activebackground="#9A031E", relief="flat",
                              width=14, command=self.reset_score)
        reset_btn.pack(pady=10)

    # -------------------------------
    def play(self, player_choice):
        computer_choice = random.choice(self.choices)

        self.player_label.config(text=f"You: {self.emojis[player_choice]}  ({player_choice})")
        self.computer_label.config(text=f"Computer: {self.emojis[computer_choice]}  ({computer_choice})")

        if player_choice == computer_choice:
            result = "It's a Draw!"
            color = "#F4A261"
            self.draws += 1
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            color = "#2A9D8F"
            self.wins += 1
        else:
            result = "You Lose!"
            color = "#E63946"
            self.losses += 1

        # Update UI
        self.result_label.config(text=result, fg=color)
        self.update_scoreboard()

    # -------------------------------
    def update_scoreboard(self):
        self.win_label.config(text=f"Wins: {self.wins}")
        self.loss_label.config(text=f"Losses: {self.losses}")
        self.draw_label.config(text=f"Draws: {self.draws}")

    # -------------------------------
    def reset_score(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.update_scoreboard()
        self.result_label.config(text="Score Reset!", fg="white")

    # -------------------------------
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


root = tk.Tk()
game = RPSGame(root)
root.mainloop()
