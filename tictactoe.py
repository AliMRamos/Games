import numpy as np
import numpy.typing as npt


class TicTacToe:
    col_size: int
    row_size: int
    board: npt.NDArray
    winning_mode: str

    def __init__(self):
        self.col_size = 3
        self.row_size = 3
        self.board = np.zeros((self.row_size, self.col_size))
        self.winning_mode = ""

    def movement(self, row: int, col: int, player: int):
        self.board[row][col] = player

    def available_spot(self, row: int, col: int):
        return self.board[row][col] == 0

    def is_board_full(self):
        for row in range(self.row_size):
            for col in range(self.col_size):
                if self.board[row, col] == 0:
                    return False
        return True

    def check_winner(self, player: int):
        # vertical check
        for col in range(self.col_size):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.winning_mode = "VERTICAL"
                return True

        # horizontal check
        for row in range(self.row_size):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.winning_mode = "HORIZONTAL"
                return True

        # descending diagonal
        if np.all(self.board.diagonal() == player):
            self.winning_mode = "DESC DIAGONAL"
            return True

        # ascending diagonal
        if np.all(np.fliplr(self.board).diagonal() == player):
            self.winning_mode = "ASC DIAGONAL"
            return True

        return False

    def reset_board(self):
        self.board = np.zeros((self.row_size, self.col_size))
