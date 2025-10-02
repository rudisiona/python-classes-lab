class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if(self.tie):
            print("it's a tie")
        elif(self.winner):
            print(f"{self.winner} wins the game")
        else:
            print(f"it's {self.turn}'s turn!")    
    
    def render(self):
        self.print_board()
        self.print_message()

    def place_mark(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move not in self.board:
                print("Invalid move. Enter valid space.")
                continue
            
            if self.board[move] is not None:
                print("Space taken. Choose empty space.")
                continue
            
            self.board[move] = self.turn
            break

    def check_win(self):
        winning_combo = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1']
        ]

        for combo in winning_combo:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None:
                self.winner = self.turn
                return True

        return False

    def check_tie(self):
        board_full = all(value is not None for value in self.board.values())
        if board_full and self.winner is None:
            self.tie = True
            return True

        return False

    def switch_turn(self):
        if(self.turn == "X"):
            self.turn = "O"
        else:
            self.turn = "X"
        
    def play_game(self):
        print("let's play a game")
        while not self.winner and not self.tie:
            self.render()
            self.place_mark()
            self.check_win()
            self.check_tie()
            self.switch_turn()
        self.render()


        






game_instance = Game()
game_instance.play_game()

# game_instance.render()
# game_instance.place_mark()

