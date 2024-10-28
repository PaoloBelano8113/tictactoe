class TicTacToeBoard:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print(' | '.join(cell if cell != '' else '-' for cell in row))
        print("\n")

    def put_symbol(self, row, col, player):
        row = int(row)
        col = int(col)
        if self.board[row][col] == '':
            self.board[row][col] = player
            return True
        return False

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        return None
        
    def is_full(self):
        return all(cell != '' for row in self.board for cell in row)

    def clear_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def return_flat_board(self):
        flat_board = [cell for row in self.board for cell in row]
        flat_board = [1 if cell != '' else 0 for row in self.board for cell in row]
        return flat_board