# Slinik Szachowy (klasa przechowująca aktualny stan gry, ocenia nielegalne ruchy, przechowując logi ruchów na plansy)

class Gamestate():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK" ,"bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp" ,"bp", "bp", "bp"],
            ["--", "--", "--", "--", "--" ,"--", "--", "--"],
            ["--", "--", "--", "--", "--" ,"--", "--", "--"],
            ["--", "--", "--", "--", "--" ,"--", "--", "--"],
            ["--", "--", "--", "--", "--" ,"--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp" ,"wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK" ,"wB", "wN", "wR"],
        ]