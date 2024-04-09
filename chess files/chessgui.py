import tkinter as tk
from PIL import Image, ImageTk

# Define the board size and square size
BOARD_SIZE = 8
SQUARE_SIZE = 80

# Define the chess piece images
piece_images = {
    "wP": ImageTk.PhotoImage(Image.open("white_pawn.png")),
    "wR": ImageTk.PhotoImage(Image.open("white_rook.png")),
    "wN": ImageTk.PhotoImage(Image.open("white_knight.png")),
    "wB": ImageTk.PhotoImage(Image.open("white_bishop.png")),
    "wQ": ImageTk.PhotoImage(Image.open("white_queen.png")),
    "wK": ImageTk.PhotoImage(Image.open("white_king.png")),
    "bP": ImageTk.PhotoImage(Image.open("black_pawn.png")),
    "bR": ImageTk.PhotoImage(Image.open("black_rook.png")),
    "bN": ImageTk.PhotoImage(Image.open("black_knight.png")),
    "bB": ImageTk.PhotoImage(Image.open("black_bishop.png")),
    "bQ": ImageTk.PhotoImage(Image.open("black_queen.png")),
    "bK": ImageTk.PhotoImage(Image.open("black_king.png"))
}

# Define the initial board state
board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
]

# Create the main window
root = tk.Tk()
root.title("Chess")

# Create the canvas to draw the chess board and pieces
canvas = tk.Canvas(root, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE)
canvas.pack()

# Draw the chess board
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        x1 = col * SQUARE_SIZE
        y1 = row * SQUARE_SIZE
        x2 = x1 + SQUARE_SIZE
        y2 = y1 + SQUARE_SIZE
        if (row + col) % 2 == 0:
            color = "beige"
        else:
            color = "brown"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

# Draw the chess pieces
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        if board[row][col] != "  ":
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2
            canvas.create_image(x, y, image=piece_images[board[row][col]])

# Start the main event loop
root.mainloop()