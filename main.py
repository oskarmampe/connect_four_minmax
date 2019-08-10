from connect_four import *

def random_eval(board):
  return random.randint(-100, 100)

def my_evaluate_board(board):
  if has_won(board, "X"):
    return float("Inf")
  elif has_won(board, "O"):
    return -float("Inf")
  else:
    x_two_streak = 0
    o_two_streak = 0

    for x in range(len(board) - 1):
      for y in range(len(board[0])):
        if board[x][y] == "X" and board[x + 1][y] == "X":
          x_two_streak += 1
        elif board[x][y] == "O" and board[x + 1][y] == "O":
          o_two_streak += 1
    return x_two_streak - o_two_streak


def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      #The "X" player finds their best move.
      result = minimax(my_board, True, 4, -float("Inf"), float("Inf"), my_evaluate_board)
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #The "O" player finds their best move
        result = minimax(my_board, False, 1, -float("Inf"), float("Inf"), codecademy_evaluate_board)
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

two_ai_game()
'''my_board = make_board()
select_space(my_board, 5, "X")
select_space(my_board, 4, "O")
select_space(my_board, 2, "X")
select_space(my_board, 3, "O")
select_space(my_board, 3, "X")
select_space(my_board, 1, "O")
select_space(my_board, 4, "X")
select_space(my_board, 2, "O")
select_space(my_board, 6, "X")

print_board(my_board)

print(my_evaluate_board(my_board))'''
