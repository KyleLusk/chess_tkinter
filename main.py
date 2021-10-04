from tkinter import *
from PIL import ImageTk, Image

import pieces

MainWindow = Tk()
MainWindow.title("Chess")
MainWindow.geometry("2000x1000")

text_output = StringVar()
OutputLabel = Label(MainWindow, textvariable=text_output)
OutputLabel.config(font=("Times New Roman", 14), bg="gray")

pawn_b = Image.open('images/pawn_black.png')
pawn_b = pawn_b.resize((50, 50), Image.ANTIALIAS)
pawn_black = ImageTk.PhotoImage(pawn_b)

pawn_w = Image.open('images/pawn_white.png')
pawn_w = pawn_w.resize((50, 50), Image.ANTIALIAS)
pawn_white = ImageTk.PhotoImage(pawn_w)

rook_w = Image.open('images/rook_white.png')
rook_w = rook_w.resize((50, 50), Image.ANTIALIAS)
rook_white = ImageTk.PhotoImage(rook_w)

rook_b = Image.open('images/rook_black.png')
rook_b = rook_b.resize((50, 50), Image.ANTIALIAS)
rook_black = ImageTk.PhotoImage(rook_b)

knight_b = Image.open('images/knight_black.png')
knight_b = knight_b.resize((50, 50), Image.ANTIALIAS)
knight_black = ImageTk.PhotoImage(knight_b)

knight_w = Image.open('images/knight_white.png')
knight_w = knight_w.resize((50, 50), Image.ANTIALIAS)
knight_white = ImageTk.PhotoImage(knight_w)

bishop_w = Image.open('images/bishop_white.png')
bishop_w = bishop_w.resize((50, 50), Image.ANTIALIAS)
bishop_white = ImageTk.PhotoImage(bishop_w)

bishop_b = Image.open('images/bishop_black.png')
bishop_b = bishop_b.resize((50, 50), Image.ANTIALIAS)
bishop_black = ImageTk.PhotoImage(bishop_b)

king_b = Image.open('images/king_black.png')
king_b = king_b.resize((50, 50), Image.ANTIALIAS)
king_black = ImageTk.PhotoImage(king_b)

king_w = Image.open('images/king_white.png')
king_w = king_w.resize((50, 50), Image.ANTIALIAS)
king_white = ImageTk.PhotoImage(king_w)

queen_w = Image.open('images/queen_white.png')
queen_w = queen_w.resize((50, 50), Image.ANTIALIAS)
queen_white = ImageTk.PhotoImage(queen_w)

queen_b = Image.open('images/queen_black.png')
queen_b = queen_b.resize((50, 50), Image.ANTIALIAS)
queen_black = ImageTk.PhotoImage(queen_b)


def switch_colors(color):
    if color == "white":
        return "black"
    else:
        return "white"


class Piece:
    def __init__(self, col, row, color, image):
        self.col = col
        self.row = row
        self.color = color
        self.image = image
        self.pc = Button(MainWindow, image=image, bg="tan", command=self.select)
        self.pc.grid(column=col, row=row)

    def select(self):
        global piece_selected
        global current_piece
        piece_selected = True
        current_piece = self
        print(self.col, self.row)

    def move(self, col, row):
        self.col = col
        self.row = row
        self.pc.grid(column=col, row=row)

    def attack(self, col, row):
        pass

    def check_legal_move(self):
        print("Nope!")
        return False

    def check_legal_attack(self):
        pass


class Square:
    def __init__(self, col, row, color, status):
        self.col = col
        self.row = row
        self.color = color
        self.status = status
        sq = Button(MainWindow, bg=color, command=self.select)
        sq.img = PhotoImage()
        sq.config(height=100, width=100, image=sq.img, compound=CENTER)
        sq.grid(column=col, row=row)

    occupying_piece = Piece(None, None, None, None)
    occupied = False

    def select(self):
        global grid_check
        grid_check = [self.col, self.row]
        if piece_selected and not self.occupied and current_piece.check_legal_move():
            current_piece.move(self.col, self.row)  # square isn't occupied so we're only moving
            self.occupying_piece = current_piece
            self.occupied = True
        elif piece_selected and self.occupied and current_piece.check_legal_attack():
            current_piece.attack(self.col, self.row)
            self.occupying_piece = current_piece
            self.occupied = True


def draw_squares():
    color = "white"
    for c in range(8):
        for r in range(8):
            sq = Square(r, c, color, 'empty')
            color = switch_colors(color)
        color = switch_colors(color)


def init_pieces():
    for r in range(8):
        PawnB = Pawns(r, 1, 'black', pawn_black)
        PawnW = Pawns(r, 6, 'white', pawn_white)
    RookB1 = Rooks(0, 0, 'black', rook_black)
    RookB2 = Rooks(7, 0, 'black', rook_black)
    RookW1 = Rooks(0, 7, 'white', rook_white)
    RookW2 = Rooks(7, 7, 'white', rook_white)
    KnightB1 = Knights(1, 0, 'black', knight_black)
    KnightB2 = Knights(6, 0, 'black', knight_black)
    KnightW1 = Knights(1, 7, 'white', knight_white)
    KnightW2 = Knights(6, 7, 'white', knight_white)
    BishopB1 = Bishops(2, 0, 'black', bishop_black)
    BishopB1 = Bishops(5, 0, 'black', bishop_black)
    BishopW1 = Bishops(2, 7, 'white', bishop_white)
    BishopW1 = Bishops(5, 7, 'white', bishop_white)
    QueenB = Queens(3, 0, 'black', queen_black)
    QueenW = Queens(3, 7, 'white', queen_white)
    KingB = Kings(4, 0, 'black', king_black)
    KingW = Kings(4, 7, 'white', king_white)


class Pawns(Piece):
    def __init__(self, col, row, color, image):
        super().__init__(col, row, color, image)

    on_first_move = True

    def check_legal_move(self):
        if
        elif grid_check[0] != self.col:
            return False
        else:
            self.on_first_move = False
            return True

    def check_legal_attack(self):
        pass


class Rooks(Piece):
    def __init__(self, col, row, color, image):
        super().__init__(col, row, color, image)


class Knights(Piece):
    def __init__(self, col, row, color, image):
        super().__init__(col, row, color, image)


class Bishops(Piece):
    def __init__(self, col, row, color, image):
        super().__init__(col, row, color, image)


class Kings(Piece):
    def __init__(self, col, row, color, image):
        super().__init__(col, row, color, image)


class Queens(Piece):
    def __init__(self, col, row, color, image):
        super().__init__(col, row, color, image)


piece_selected = False
current_piece = Piece(None, None, None, None)
grid_check = []

if __name__ == '__main__':
    draw_squares()
    init_pieces()
    MainWindow.mainloop()
