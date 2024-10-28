import random
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('D:/Portfolio/tictactoe/toetactic_alpha.h5')


class Player:
    def __init__(self, _player, _symbol):
        self.player = _player
        self.symbol = _symbol.lower()
        self.moves = []

    def move_player(self, board,counter):
        if self.moves != []:
            return self.moves[counter]
        elif self.player.lower() == 'human':
            row, col = self.human_player()
            return row, col
        elif self.player.lower() == 'random':
            return self.random_AI_player(board)
        elif self.player.lower() == 'minimax':
            return self.minimax_AI_player(board, True)
        elif self.player.lower() == 'alpha':
            return self.minimax_alpha_beta_AI(board, True, float('-inf'), float('inf'))
        elif self.player.lower() == "toetactic":
            return self.toetactic(board)
        
    def set_moves(self,moves):
        self.moves = moves

    def human_player(self):
        while True: 
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): ")) 
                if 0 <= row <= 2 and 0 <= col <= 2:
                    return row, col
                else:
                    print("Invalid move. Please enter values between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter integers only.")

    def random_AI_player(self, board_obj):
        available_moves = [(row, col) for row in range(3) for col in range(3) if board_obj.board[row][col] == '']
        
        if available_moves:
            return random.choice(available_moves)
        return None, None

    def minimax_AI_player(self, board_obj, is_maximizing_player, depth=0):
        ai_symbol = self.symbol
        enemy_symbol = 'o' if ai_symbol == 'x' else 'x'

        winner = board_obj.check_winner()
        if winner == ai_symbol:
            return None, 10 - depth
        elif winner == enemy_symbol:
            return None, depth - 10  
        elif board_obj.is_full():
            return None, 0  

        if is_maximizing_player:
            best_score = float('-inf')
            best_move = None
            for row in range(3):
                for col in range(3):
                    if board_obj.board[row][col] == '': 
                        board_obj.board[row][col] = ai_symbol
                        _, score = self.minimax_AI_player(board_obj, False, depth + 1) 
                        board_obj.board[row][col] = ''
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)

            if depth == 0:
                return best_move
            return None, best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board_obj.board[row][col] == '': 
                        board_obj.board[row][col] = enemy_symbol
                        _, score = self.minimax_AI_player(board_obj, True, depth + 1) 
                        board_obj.board[row][col] = ''
                        if score < best_score:
                            best_score = score

            return None, best_score
        
    def minimax_alpha_beta_AI(self, board_obj, is_maximizing, alpha, beta, depth=0):
        ai_symbol = self.symbol
        enemy_symbol = 'o' if ai_symbol == 'x' else 'x'
        winner = board_obj.check_winner()
        
        if winner == ai_symbol:
            return None, 10 - depth
        elif winner == enemy_symbol:
            return None, depth - 10
        elif board_obj.is_full():
            return None, 0

        if is_maximizing:
            max_eval = float('-inf')
            best_move = None  
            for row in range(3):
                for col in range(3):
                    if board_obj.board[row][col] == '':
                        board_obj.board[row][col] = ai_symbol
                        _, eval = self.minimax_alpha_beta_AI(board_obj, False, alpha, beta, depth + 1)
                        board_obj.board[row][col] = ''
                        if eval > max_eval:
                            max_eval = eval
                            best_move = (row, col)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            if depth == 0: 
                return best_move
            return None, max_eval
        else:
            min_eval = float('inf')
            for row in range(3):
                for col in range(3):
                    if board_obj.board[row][col] == '':
                        board_obj.board[row][col] = enemy_symbol
                        _, eval = self.minimax_alpha_beta_AI(board_obj, True, alpha, beta, depth + 1)
                        board_obj.board[row][col] = ''
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return None, min_eval
    
    def toetactic(self,board_obj):
        board = [[0 if cell == '' else 1 if cell == self.symbol else 2 for cell in row] for row in board_obj.board]
        input_data = self.toetactic_input(board)
        predictions = model.predict(input_data)
        next_move = np.argmax(predictions)
        return self.toetactic_output(next_move)

    def toetactic_input(self,board):
        return np.array(board).flatten().reshape(1,9)
    
    def toetactic_output(self,predictions):
        output = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        return output[predictions]