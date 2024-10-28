from board import TicTacToeBoard

class TicTacToe:
    def __init__(self, _board, _player1, _player2):
        self.board = _board
        self.player1 = _player1
        self.player2 = _player2
        self.winner = None
        self.games_data = [] 
        self.board_states = []

    def start_game(self):
        game_moves = []
        counter1, counter2 = 0,0
        turn = 0
        while self.board.check_winner() is None and not self.board.is_full():
            self.board.display_board()
            current_player = self.player1 if turn == 0 else self.player2
            if turn == 0: 
                row, col = self.make_move(current_player, counter1)
                counter1 += 1 
            else:  
                row, col = self.make_move(current_player, counter2)
                counter2 += 1  
            game_moves.append((current_player.player,current_player.symbol,(row, col))) 
            
            #append board states
            self.board_states.append(self.board.return_flat_board())

            winner = self.board.check_winner()
            if winner is not None:
                self.winner = winner
                #self.board.display_board()
                self.games_data.append({
                    'moves': game_moves,
                    'result': current_player.player
                })
                print(f"{self.winner} wins!")
                break 
            turn = 1 - turn
        else:
            #self.board.display_board()
            self.games_data.append({
                    'moves': game_moves,
                    'result': None
                })
            print("Draw!")
        
    def make_move(self, player, counter):
        while True:
            row, col = player.move_player(self.board,counter)
            if row is not None and col is not None:
                valid_move = self.board.put_symbol(row, col, player.symbol)
                if valid_move:
                    return row,col
                else: 
                    print("Space already occupied.")
        
    def get_winner(self):
        return self.winner

