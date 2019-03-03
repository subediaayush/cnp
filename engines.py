import chess
from chess.engine import SimpleEngine

engines = {
    "stockfish": chess.engine.SimpleEngine.popen_uci(r"stockfish-10-mac/Mac/stockfish-10-64")
}


def engine(name):
    return engines[name]


def clean(name):
    engines[name].quit()


def clean_all():
    for engine_name in engines:
        engines[engine_name].quit()
