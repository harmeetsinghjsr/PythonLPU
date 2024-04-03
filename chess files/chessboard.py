import tkinter as tk

class ChessBoard:
    def __init__(self, master):
        self.master = master
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                button = tk.Button(master, width=10, height=5)
                button.grid(row=i, column=j)
                if (i+j) % 2 == 0:
                    button.config(bg='white')
                else:
                    button.config(bg='black')
                row.append(button)
            self.board.append(row)

root = tk.Tk()
chess = ChessBoard(root)
root.mainloop()