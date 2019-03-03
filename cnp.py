import time

import numpy
from chess import Board, engine
from chess import pgn as pgn_reader

import engines
from player import EnginePlayer


def handle_score(board):
    print(board.result())


def is_white_win(result):
    return result is "1-0"


def is_black_win(result):
    return result is "0-1"


def is_draw(result):
    return result is "1/2-1/2"


def main(pgn=None):
    times = list()
    wins = losses = draws = 0

    for i in range(10):
        try:
            with open(pgn) as pgn:
                game = pgn_reader.read_game(pgn)
                board = game.board()
        except Exception:
            board = Board()

        white_player = EnginePlayer("White", depth=.01)
        black_player = EnginePlayer("Black", depth=.1)

        start = time.time()
        print("Starting game", i + 1)

        while True:
            # print(board)

            if board.is_game_over():
                if is_white_win(board.result()):
                    wins = wins + 1
                elif is_black_win(board.result()):
                    losses = losses + 1
                else:
                    draws = draws + 1

                handle_score(board)
                break

            white_turn = board.turn

            if white_turn:
                move = white_player.get_next_move(board)
            else:
                move = black_player.get_next_move(board)

            if move is "-":
                exit()

            board.push(move)

        white_player.clean()
        black_player.clean()

        end = time.time()

        diff = (end - start)

        print("Game lasted {:.0f} seconds\n".format(diff))
        times.append(diff)

    engines.clean_all()
    print("Average time per game", numpy.average(times))
    print("Standard deviation for all games", numpy.std(times))
    print("Total wins", wins)
    print("Total losses", losses)
    print("Total draws", draws)


if __name__ == '__main__':
    main()
