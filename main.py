import random
import json
from tictactoe import TicTacToe
from board import TicTacToeBoard
from player import Player

players = ['human','random','minimax','alpha','toetactic']

def simulate_games(num_games):
    all_games_data = []
    board_states = []
    for _ in range(num_games):
        board = TicTacToeBoard()
        p1 = Player(players[random.randrange(0,1)],'x')
        p2 = Player(players[random.randrange(4,5)],'o')       
        tictactoe = TicTacToe(board,p1,p2)
        tictactoe.start_game()
        all_games_data.append(str(tictactoe.games_data))
        #board_states.append(str(tictactoe.board_states))
        #print(tictactoe.games_data)

    with open('tictactoe/tictactoe_data.json', 'w') as f:
        json.dump(all_games_data, f, indent=4)

    # with open('tictactoe/tictactoe_board_states.json', 'w') as f:
    #     json.dump(board_states, f, indent=4)

simulate_games(1)
