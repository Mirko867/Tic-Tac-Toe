from tkinter import *
import ttkbootstrap as ttk
import numpy as np

size_of_board = 300
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 20
symbol_X_color = '#EE4035'
symbol_O_color = '#0492CF'


class Tic_Tac_Toe():

    def __init__(self):
        self.window = ttk.Window(themename="superhero")
        self.window.title("Tic Tac Toe")
        self.window.configure(height=800 , width=800)
        self.window.bind('<Button-1>' , self.click)

        self.canvas = Canvas()
        self.canvas.config(height=300 , width=300 , bg="white")
        self.canvas.grid(column=0 , row=1 , padx=(30 , 0), pady=(0,20))  # Added padx to create left margin

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

        self.label_status = ttk.Label(self.window , text="Tic Tac Toe" , justify="left" , bootstyle="success" ,
                                      font=("garamond" , 20 , "bold") , borderwidth=10)
        self.label_status.grid(columnspan=3 , row=0)

        self.label_frame = ttk.LabelFrame(height=300 , width=300 , bootstyle="success")
        self.label_frame.grid(column=1 , row=1 , padx=100)

        self.label_status_content = ttk.Label(self.label_frame , text="==============" , justify="left" ,
                                              bootstyle="success" , font=("garamond" , 10 , "bold") , borderwidth=10)
        self.label_status_content.grid(columnspan=3 , row=0 , )

        self.label_score = ttk.Label(self.label_frame , text="Score" , justify="left" , bootstyle="success" ,
                                     font=("garamond" , 10 , "bold") , borderwidth=10)
        self.label_score.grid(column=0 , row=1)

        self.label_Player1 = ttk.Label(self.label_frame , text="Player X" , justify="left" , bootstyle="success" ,
                                       font=("garamond" , 10 , "bold") , borderwidth=10)
        self.label_Player1.grid(column=0 , row=2)

        self.label_score_player1 = ttk.Label(self.label_frame , text=f"{self.X_score}" , justify="left" ,
                                             bootstyle="success" ,
                                             font=("garamond" , 10 , "bold") , borderwidth=10)
        self.label_score_player1.grid(column=1 , row=2)

        self.label_player2 = ttk.Label(self.label_frame , text="Player O" , justify="left" , bootstyle="success" ,
                                       font=("garamond" , 10 , "bold") , borderwidth=10)
        self.label_player2.grid(column=0 , row=3)

        self.label_score_player2 = ttk.Label(self.label_frame , text=f"{self.O_score}" , justify="left" ,
                                             bootstyle="success" ,
                                             font=("garamond" , 10 , "bold") , borderwidth=10)
        self.label_score_player2.grid(column=1 , row=3)
        self.button_restart = ttk.Button(self.window , text="Restart" , bootstyle="success")
        self.button_restart.grid(column=0 , row=2 , padx=5 , pady=10 , )

        self.button_tbd = ttk.Button(self.window , text="Reset" , bootstyle="success")
        self.button_tbd.grid(column=1 , row=2 , padx=5 , pady=10 , )

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3 , 3))

    def mainloop(self):
        self.window.mainloop()

    # Creating the board
    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * 300 / 3 , 0 , (i + 1) * 300 / 3 , 300)
        for i in range(2):
            self.canvas.create_line(0 , (i + 1) * 300 / 3 , 300 , (i + 1) * 300 / 3)
        self.canvas.grid(column=0 , row=1)

    # Function to reset the board, deleting all the scores
    def reset(self):
        self.X_score = 0
        self.O_score = 0
        self.label_status_content.config(text='==============')
        self.label_score_player1.config(text=f"{self.X_score}")
        self.label_score_player2.config(text=f"{self.O_score}")
        self.canvas.delete("all")
        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3 , 3))
        self.reset_board = False
        self.gameover = False

    # Function to restart the game keeping the score
    def restart(self):
        self.label_status_content.config(text='==============')
        self.canvas.delete("all")
        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3 , 3))
        self.reset_board = False
        self.gameover = False

    # Function needed to reassign the button once the class is created
    def configure_reset_button(self):
        self.button_tbd.config(command=self.reset)

    def configure_restart_button(self):
        self.button_restart.config(command=self.restart)

    # Function that, after having identified the coordinate of the event register,get the pixel at the center of the identofied area
    def draw_O(self , logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[ 0 ] - symbol_size , grid_position[ 1 ] - symbol_size ,
                                grid_position[ 0 ] + symbol_size , grid_position[ 1 ] + symbol_size ,
                                width=symbol_thickness ,
                                outline=symbol_O_color)

    def draw_X(self , logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[ 0 ] - symbol_size , grid_position[ 1 ] - symbol_size ,
                                grid_position[ 0 ] + symbol_size , grid_position[ 1 ] + symbol_size ,
                                width=symbol_thickness ,
                                fill=symbol_X_color)
        self.canvas.create_line(grid_position[ 0 ] - symbol_size , grid_position[ 1 ] + symbol_size ,
                                grid_position[ 0 ] + symbol_size , grid_position[ 1 ] - symbol_size ,
                                width=symbol_thickness ,
                                fill=symbol_X_color)

    # Function for the management of the game outcome on within the created labels
    def display_gameover(self):
        if self.X_wins:
            self.X_score += 1
            self.label_status_content.config(text='Winner: Player 1 (X)')
            print(f"Winner: Player 1. Score{self.X_score}")
        elif self.O_wins:
            self.O_score += 1
            self.label_status_content.config(text='Winner: Player 2 (O)')
            print(f"Winner: Player 2. Score{self.O_score}")
        else:
            self.tie_score += 1
            self.label_status_content.config(text='It is a tie')
        self.label_score_player1.config(text=f"{self.X_score}")
        self.label_score_player2.config(text=f"{self.O_score}")

    # Game logic
    def convert_logical_to_grid_position(self , logical_position):
        logical_position = np.array(logical_position , dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self , grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3) , dtype=int)

    def is_grid_occupied(self , logical_position):
        if self.board_status[ logical_position[ 0 ] ][ logical_position[ 1 ] ] == 0:
            return False
        else:
            return True

    def is_winner(self , player):
        player = -1 if player == 'X' else 1
        # Three in a row
        for i in range(3):
            if self.board_status[ i ][ 0 ] == self.board_status[ i ][ 1 ] == self.board_status[ i ][ 2 ] == player:
                return True
            if self.board_status[ 0 ][ i ] == self.board_status[ 1 ][ i ] == self.board_status[ 2 ][ i ] == player:
                return True
        # Diagonals
        if self.board_status[ 0 ][ 0 ] == self.board_status[ 1 ][ 1 ] == self.board_status[ 2 ][ 2 ] == player:
            return True
        if self.board_status[ 0 ][ 2 ] == self.board_status[ 1 ][ 1 ] == self.board_status[ 2 ][ 0 ] == player:
            return True

        return False

    def is_tie(self):
        r , c = np.where(self.board_status == 0)
        tie = False
        if len(r) == 0:
            tie = True
        return tie

    def is_gameover(self):
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()
        gameover = self.X_wins or self.O_wins or self.tie
        return gameover

    def click(self , event):
        grid_position = [ event.x , event.y ]
        logical_position = self.convert_grid_to_logical_position(grid_position)
        if self.is_gameover():
            self.restart()
            return
        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[ logical_position[0]][ logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1] ] = 1
                    self.player_X_turns = not self.player_X_turns

            # Check if game is concluded
            if self.is_gameover():
                self.display_gameover()
                print('Done')


game_instance = Tic_Tac_Toe()
game_instance.configure_reset_button()
game_instance.configure_restart_button()
game_instance.mainloop()
