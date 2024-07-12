import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("800x800")  # Adjusted size for a smaller board
        self.root.configure(bg='#121212')  # Dark background color

        self.current_player = 'X'
        self.first_player = 'X'
        self.player_X = 'X'
        self.player_O = 'O'
        self.vs_cpu = False
        self.difficulty = 'Easy'
        self.hall_of_fame = []
        self.consecutive_wins = 0
        self.total_wins = 0
        self.player_name = ""

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_screen()

        self.welcome_label = tk.Label(self.root, text="Welcome to Rajdeep's Tic Tac Toe", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.welcome_label.pack(pady=100)

        self.press_enter_label = tk.Label(self.root, text="Press Enter to Start", font=('Helvetica', 20), fg='white', bg='#121212')
        self.press_enter_label.pack(pady=50)

        self.root.bind('<Return>', self.choose_mode_screen)

    def choose_mode_screen(self, event=None):
        self.clear_screen()

        self.choose_mode_label = tk.Label(self.root, text="Choose Game Mode", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.choose_mode_label.pack(pady=80)

        self.two_player_button = tk.Button(self.root, text="2 Player Mode", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=self.choose_player_screen)
        self.two_player_button.pack(pady=20)

        self.vs_cpu_button = tk.Button(self.root, text="VS CPU Mode", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=self.choose_player_cpu_screen)
        self.vs_cpu_button.pack(pady=20)

        self.hall_of_fame_button = tk.Button(self.root, text="Hall of Fame", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=self.display_hall_of_fame)
        self.hall_of_fame_button.pack(pady=20)

    def choose_player_screen(self):
        self.vs_cpu = False
        self.clear_screen()

        self.choose_label = tk.Label(self.root, text="Choose Your Player", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.choose_label.pack(pady=80)

        self.player_X_button = tk.Button(self.root, text="Player X", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_player('X'))
        self.player_X_button.pack(pady=20)

        self.player_O_button = tk.Button(self.root, text="Player O", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_player('O'))
        self.player_O_button.pack(pady=20)

    def choose_player_cpu_screen(self):
        self.vs_cpu = True
        self.clear_screen()

        self.choose_label = tk.Label(self.root, text="Choose Your Player", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.choose_label.pack(pady=80)

        self.player_X_button = tk.Button(self.root, text="Player X", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_player_cpu('X'))
        self.player_X_button.pack(pady=20)

        self.player_O_button = tk.Button(self.root, text="Player O", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_player_cpu('O'))
        self.player_O_button.pack(pady=20)

    def set_player(self, player):
        self.player_X = player
        self.player_O = 'O' if player == 'X' else 'X'
        self.current_player = self.player_X
        self.first_player = self.player_X
        self.choose_first_move_screen()

    def set_player_cpu(self, player):
        self.player_X = player
        self.player_O = 'O' if player == 'X' else 'X'
        self.current_player = self.player_X
        self.first_player = self.player_X
        self.choose_difficulty_screen()

    def choose_first_move_screen(self):
        self.clear_screen()

        self.choose_first_label = tk.Label(self.root, text="Who Will Make the First Move?", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.choose_first_label.pack(pady=80)

        self.first_player_button = tk.Button(self.root, text=f"Player {self.player_X}", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_first_move(self.player_X))
        self.first_player_button.pack(pady=20)

        self.second_player_button = tk.Button(self.root, text=f"Player {self.player_O}", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_first_move(self.player_O))
        self.second_player_button.pack(pady=20)

    def choose_difficulty_screen(self):
        self.clear_screen()

        self.choose_difficulty_label = tk.Label(self.root, text="Choose Difficulty Level", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.choose_difficulty_label.pack(pady=80)

        self.easy_button = tk.Button(self.root, text="Easy", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_difficulty('Easy'))
        self.easy_button.pack(pady=20)

        self.medium_button = tk.Button(self.root, text="Medium", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_difficulty('Medium'))
        self.medium_button.pack(pady=20)

        self.hard_button = tk.Button(self.root, text="Hard", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_difficulty('Hard'))
        self.hard_button.pack(pady=20)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.choose_first_move_cpu_screen()

    def choose_first_move_cpu_screen(self):
        self.clear_screen()

        self.choose_first_label = tk.Label(self.root, text="Who Will Make the First Move?", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.choose_first_label.pack(pady=80)

        self.first_player_button = tk.Button(self.root, text="Player", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_first_move_cpu(self.player_X))
        self.first_player_button.pack(pady=20)

        self.second_player_button = tk.Button(self.root, text="CPU", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=lambda: self.set_first_move_cpu(self.player_O))
        self.second_player_button.pack(pady=20)

    def set_first_move(self, player):
        self.first_player = player
        self.current_player = player
        self.start_game()

    def set_first_move_cpu(self, player):
        self.first_player = player
        self.current_player = player
        if self.difficulty == 'God':
            self.player_name = simpledialog.askstring("Player Name", "Enter your name:")
        self.start_game()

    def start_game(self):
        self.clear_screen()
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        self.create_board()
        if self.vs_cpu and self.first_player == self.player_O:
            self.root.after(500, self.cpu_move)  # Add slight delay for CPU's first move

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('Helvetica', 40), width=8, height=3,
                                   command=lambda row=row, col=col: self.on_button_click(row, col), fg='#ffffff', bg='#333333', activebackground='#555555')
                button.grid(row=row, column=col, padx=10, pady=10)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.buttons[row][col]['text'] == "" and self.check_winner() is False:
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col]['fg'] = 'blue' if self.current_player == 'X' else 'red'
            if self.check_winner():
                self.highlight_winner(self.check_winner())
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.handle_win()
            elif self.is_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.end_game_screen()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.vs_cpu and self.current_player == self.player_O:
                    self.root.after(500, self.cpu_move)  # Add slight delay for CPU's moves

    def cpu_move(self):
        if self.difficulty == 'Easy':
            self.cpu_easy_move()
        elif self.difficulty == 'Medium':
            self.cpu_medium_move()
        elif self.difficulty == 'Hard':
            self.cpu_hard_move()
        elif self.difficulty == 'God':
            self.cpu_god_move()

    def cpu_easy_move(self):
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.buttons[r][c]['text'] == ""]
        move = random.choice(available_moves)
        self.on_button_click(move[0], move[1])

    def cpu_medium_move(self):
        if not self.cpu_block_or_win('O'):
            if not self.cpu_block_or_win('X'):
                self.cpu_easy_move()

    def cpu_hard_move(self):
        if not self.cpu_block_or_win('O'):
            if not self.cpu_block_or_win('X'):
                if not self.cpu_fork_or_block_fork():
                    self.cpu_medium_move()

    def cpu_god_move(self):
        if not self.cpu_block_or_win('O'):
            if not self.cpu_block_or_win('X'):
                if not self.cpu_fork_or_block_fork():
                    self.cpu_hard_move()

    def cpu_block_or_win(self, player):
        for r in range(3):
            for c in range(3):
                if self.buttons[r][c]['text'] == "":
                    self.buttons[r][c]['text'] = player
                    if self.check_winner() == player:
                        if player != self.current_player:
                            self.buttons[r][c]['text'] = self.current_player
                        return True
                    self.buttons[r][c]['text'] = ""
        return False

    def cpu_fork_or_block_fork(self):
        for r in range(3):
            for c in range(3):
                if self.buttons[r][c]['text'] == "":
                    self.buttons[r][c]['text'] = self.current_player
                    win_count = sum([self.check_fork() == self.current_player for _ in range(2)])
                    self.buttons[r][c]['text'] = ""
                    if win_count > 1:
                        self.on_button_click(r, c)
                        return True
        return False

    def check_fork(self):
        if self.buttons[1][1]['text'] == self.current_player:
            if self.buttons[0][0]['text'] == self.buttons[2][2]['text'] == "" or self.buttons[0][2]['text'] == self.buttons[2][0]['text'] == "":
                return self.current_player
        return False

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                return self.buttons[row][0]['text']
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != "":
                return self.buttons[0][col]['text']
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return self.buttons[0][0]['text']
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return self.buttons[0][2]['text']
        return False

    def highlight_winner(self, winner):
        if winner:
            if winner == 'X':
                color = 'blue'
            else:
                color = 'red'
            for r in range(3):
                for c in range(3):
                    if self.buttons[r][c]['text'] == winner:
                        self.buttons[r][c]['fg'] = color

    def is_full(self):
        return all(self.buttons[row][col]['text'] != "" for row in range(3) for col in range(3))

    def handle_win(self):
        if self.vs_cpu and self.difficulty == 'Hard' and self.current_player == self.player_X:
            self.consecutive_wins += 1
            self.total_wins += 1
            if self.consecutive_wins == 5:
                self.difficulty = 'God'
                messagebox.showinfo("Tic Tac Toe", "God Mode Unlocked!")
        elif self.vs_cpu and self.difficulty == 'God' and self.current_player == self.player_X:
            self.total_wins += 1
            if self.total_wins == 3:
                self.hall_of_fame.append((self.player_name, self.total_wins))
        else:
            self.consecutive_wins = 0

        self.end_game_screen()

    def end_game_screen(self):
        self.clear_screen()

        self.end_game_label = tk.Label(self.root, text="Game Over", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.end_game_label.pack(pady=80)

        self.restart_button = tk.Button(self.root, text="Restart Game", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=self.start_game)
        self.restart_button.pack(pady=20)

        self.title_screen_button = tk.Button(self.root, text="Back to Title Screen", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=self.create_welcome_screen)
        self.title_screen_button.pack(pady=20)

        self.quit_button = tk.Button(self.root, text="Quit", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=self.root.quit)
        self.quit_button.pack(pady=20)

    def display_hall_of_fame(self):
        self.clear_screen()

        self.hall_of_fame_label = tk.Label(self.root, text="Hall of Fame", font=('Helvetica', 40, 'bold'), fg='white', bg='#121212')
        self.hall_of_fame_label.pack(pady=80)

        for name, wins in self.hall_of_fame:
            label = tk.Label(self.root, text=f"{name}: {wins} Wins in God Mode", font=('Helvetica', 20), fg='white', bg='#121212')
            label.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Back", font=('Helvetica', 20), fg='white', bg='#333333', activebackground='#555555', command=self.create_welcome_screen)
        self.back_button.pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
