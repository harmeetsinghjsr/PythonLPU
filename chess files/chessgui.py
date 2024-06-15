from PIL import Image, ImageTk

# Load the chess piece images
piece_files = {
    "wP": "w_pawn.png",
    "wR": "w_rook.png",
    "wN": "w_knight.png",
    "wB": "w_bishop.png",
    "wQ": "w_queen.png",
    "wK": "w_king.png",
    "bP": "b_pawn.png",
    "bR": "b_rook.png",
    "bN": "b_knight.png",
    "bB": "b_bishop.png",
    "bQ": "b_queen.png",
    "bK": "b_king.png"
}

for piece, file in piece_files.items():
    img = Image.open(file)
    piece_images[piece] = ImageTk.PhotoImage(img)

# ...

# Draw the chess pieces
for row in range(BOARD_SIZE):
    for col in range(BOARD_SIZE):
        if board[row][col] != "  ":
            x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            y = row * SQUARE_SIZE + SQUARE_SIZE // 2
            # Store a reference to the PhotoImage object
            piece_image = piece_images[board[row][col]]
            canvas.create_image(x, y, image=piece_image)
