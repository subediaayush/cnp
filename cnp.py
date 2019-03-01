from chess import Board
from chess import pgn as pgn_reader

from player import EnginePlayer


def handle_score(board):
    print(board.result())


def main(pgn=None):
    try:
        with open(pgn) as pgn:
            game = pgn_reader.read_game(pgn)
            board = game.board()
    except Exception:
        board = Board()

    white_player = EnginePlayer("White")
    black_player = EnginePlayer("Black")

    while True:
        print(board)

        if board.is_game_over():
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


if __name__ == '__main__':
    main()
