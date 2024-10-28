import json
import ast
from tictactoe import TicTacToe
from board import TicTacToeBoard
from player import Player

with open('tictactoe/tictactoe_data.json', 'r') as f:
    data = json.load(f)  

game_dict_list = []
original_result = []
for game_str in data:
    game_data = ast.literal_eval(game_str)
    if isinstance(game_data, list):
        game_dict_list.extend(game_data) 
    else:
        game_dict_list.append(game_data)  

# replay games
# for result in game_dict_list:
#     original_result.append(result)

# all_games_data = []
# for game in game_dict_list:
#     moves = game["moves"]

#     p1_moves = []
#     p2_moves = []

#     for index, move in enumerate(moves):
#         player, symbol, position = move
#         if index % 2 == 0:  
#             p1_moves.append(position)
#         else:  
#             p2_moves.append(position)

    
#     player1 = Player(moves[0][0], moves[0][1]) 
#     player2 = Player(moves[1][0], moves[1][1])  

#     player1.set_moves(p1_moves)
#     player2.set_moves(p2_moves)
  
#     board = TicTacToeBoard()
#     tictactoe = TicTacToe(board, player1, player2)
#     tictactoe.start_game()
#     all_games_data.append(str(tictactoe.games_data))

# with open('tictactoe_rebuild_data.json', 'w') as f:
#     json.dump(all_games_data, f,indent=4)
