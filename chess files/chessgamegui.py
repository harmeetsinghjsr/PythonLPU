import tkinter as tk

class ChessBoard:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, width=800, height=800)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        self.pieces = {}
        self.create_pieces()

    def create_pieces(self):
        for i in range(8):  # Pawns
            self.pieces[(i, 1)] = 'black_pawn'
            self.pieces[(i, 6)] = 'white_pawn'
        # Rooks
        self.pieces[(0, 0)] = 'black_rook'
        self.pieces[(7, 0)] = 'black_rook'
        self.pieces[(0, 7)] = 'white_rook'
        self.pieces[(7, 7)] = 'white_rook'
        # Knights
        self.pieces[(1, 0)] = 'black_knight'
        self.pieces[(6, 0)] = 'black_knight'
        self.pieces[(1, 7)] = 'white_knight'
        self.pieces[(6, 7)] = 'white_knight'
        # Bishops
        self.pieces[(2, 0)] = 'black_bishop'
        self.pieces[(5, 0)] = 'black_bishop'
        self.pieces[(2, 7)] = 'white_bishop'
        self.pieces[(5, 7)] = 'white_bishop'
        # Queens
        self.pieces[(3, 0)] = 'black_queen'
        self.pieces[(3, 7)] = 'white_queen'
        # Kings
        self.pieces[(4, 0)] = 'black_king'
        self.pieces[(4, 7)] = 'white_king'

        for position, piece in self.pieces.items():
            x, y = position
            self.canvas.create_image(x*100+50, y*100+50, image=self.load_piece_image(piece))

    def load_piece_image(self, piece):
        return tk.PhotoImage(file=f"{piece}.png")

    def draw_board(self):
        color = "white"
        for i in range(8):
            color = "white" if color == "black" else "black"
            for j in range(8):
                x1 = j * 100
                y1 = i * 100
                x2 = x1 + 100
                y2 = y1 + 100
                if color == "white":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                    color = "black"
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
                    color = "white"

if __name__ == "__main__":
    root = tk.Tk()
    ChessBoard(root)
    root.mainloop()