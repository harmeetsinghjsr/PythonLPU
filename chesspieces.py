from chesspieces import King, Queen, Bishop, Knight, Rook, Pawn

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        # Place pieces on the board
        for i in range(8):
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')

        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(8):
            board[0][i] = pieces[i]('black')
            board[7][i] = pieces[i]('white')

        return board
