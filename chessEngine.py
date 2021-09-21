# This class is responsible for storing all the information about the current state of a chess game. It will also be responsible for determining the valid moves of the current state. It will also keep a move log.

class GameState():
    def __init__(self):
        # The board is an 8x8 2D list, and each element of the list has 2 characters.
        # The first character represents the color of the piece, "b" or "w"
        # The second character represents the type of piece, "K", "Q", "R", "B", "N", or "p"
        # "--" represents an empty space with no piece
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []