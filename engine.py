import chess
from chess.engine import SimpleEngine


class Engine(object):

    def __init__(self) -> None:
        self.engines = {
            "stockfish": chess.engine.SimpleEngine.popen_uci(r"stockfish-10-mac/Mac/stockfish-10-64")
        }

    def engine(self, name):
        return self.engines[name]


class Stockfish(Engine):
    def engine(self, name):
        return super().engine("stockfish")
