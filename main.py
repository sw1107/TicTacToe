from itertools import cycle
import sys

BOARD = {}


def main():
    while input("Do you want to play a game of Tic Tac Toe? Type 'y' to play': ") == 'y':
        play_game()


def play_game():
    # game setup
    reset_board()

    is_game_over = False
    number_of_moves = 0
    player = cycle(range(2))
    current_player = next(player)

    while not is_game_over:
        print_board()

        # validate input from user
        while True:
            next_move = input(f"Player {current_player + 1} move? Type 1-9 : ")
            if next_move == "exit":
                sys.exit()
            try:
                next_move = int(next_move)
            except ValueError:
                print("Move not valid")
                pass
            if next_move in range(1, 10):
                if BOARD[next_move - 1] == " ":
                    break
                else:
                    print("Move not available")
            else:
                print("Move not valid")

        # update board with move
        if current_player == 0:
            BOARD[next_move - 1] = 'x'
        else:
            BOARD[next_move - 1] = 'o'

        # toggle to next player
        current_player = next(player)
        number_of_moves += 1

        # check for game over
        if number_of_moves >= 5:
            is_game_over = check_game_over()
        if number_of_moves == 9 and is_game_over is False:
            is_game_over = True
            print_board()
            print(f"Game over: No winner\n")
            return

    print_board()
    winner = next(player)
    print(f"Game over: Player {winner + 1} is the winner! \n")


def check_game_over():
    if ((BOARD[0] == BOARD[1] == BOARD[2] and BOARD[0] != " ") or
            (BOARD[3] == BOARD[4] == BOARD[5] and BOARD[3] != " ") or
            (BOARD[6] == BOARD[7] == BOARD[8] and BOARD[6] != " ") or
            (BOARD[0] == BOARD[3] == BOARD[6] and BOARD[0] != " ") or
            (BOARD[1] == BOARD[4] == BOARD[7] and BOARD[1] != " ") or
            (BOARD[2] == BOARD[5] == BOARD[8] and BOARD[2] != " ") or
            (BOARD[0] == BOARD[4] == BOARD[8] and BOARD[0] != " ") or
            (BOARD[2] == BOARD[4] == BOARD[6] and BOARD[2] != " ")):
        return True
    else:
        return False


def print_board():
    print(f"\n"
          f" {BOARD[0]} | {BOARD[1]} | {BOARD[2]} \n"
          f"-----------\n"
          f" {BOARD[3]} | {BOARD[4]} | {BOARD[5]} \n"
          f"-----------\n"
          f" {BOARD[6]} | {BOARD[7]} | {BOARD[8]} \n")


def reset_board():
    for i in range(9):
        BOARD[i] = " "


main()
