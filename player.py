import chess
import chess.engine

import engines


class Player(object):
    def get_next_move(self, board):
        raise Exception("Allow player to generate and input next move")

    def clean(self):
        pass


class HumanPlayer(Player):

    def __init__(self, name="Human") -> None:
        super().__init__()
        self.name = name

    def get_next_move(self, board):
        while True:
            raw_move = input("Enter {0}'s move:".format(self.name))
            if raw_move is "-":
                return raw_move

            move = chess.Move.from_uci(raw_move)
            if move not in board.legal_moves:
                print("Illegal move", raw_move)
            else:
                return move


class EnginePlayer(Player):

    def __init__(self, name="Engine", engine_name="stockfish", depth=0.100) -> None:
        super().__init__()
        self.name = name
        self.engine = engines.engine(engine_name)
        self.limit = chess.engine.Limit(time=depth)

    def get_next_move(self, board):
        return self.engine.play(board=board, limit=self.limit).move
