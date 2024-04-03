import chess

def print_board(board):
    print(board)

def get_move():
    move = input("Enter your move: ")
    return move

def main():ṇ
    board = chess.Board()

    while not board.is_checkmate():
        print_board(board)
        move = get_move()
        if chess.Move.from_uci(move) in board.legal_moves:
            board.push(chess.Move.from_uci(move))
        else:
            print("Illegal move. Try again.")

    print("Game over. The winner is ", board.result())

if __name__ == "__main__":
    main()