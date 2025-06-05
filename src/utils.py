icons = {
    "K": "♚",
    "k": "♔",
    #
    "Q": "♛",
    "q": "♕",
    #
    "R": "♜",
    "r": "♖",
    #
    "B": "♝",
    "b": "♗",
    #
    "N": "♞",
    "n": "♘",
    #
    "P": "♟",
    "p": "♙",
}


def draw_board(fen):
    fen = fen.split(" ")

    board = "\n+---+---+---+---+---+---+---+---+\n| "
    pos = 0
    for l in fen[0]:
        if l.isdecimal():
            for space in range(int(l)):
                board += "  | "
                pos += 1
            continue

        if l == "/":
            board += "\n+---+---+---+---+---+---+---+---+\n| "
            pos += 1

        else:
            board += f"{icons[l]} | "

    board += "\n+---+---+---+---+---+---+---+---+\n"
    print(board)


if __name__ == "__main__":
    fen = "2Qn2k1/1p6/pq2R1Bp/3p3P/5b2/P1N5/1P4P1/R6K b - - 0 31"
    draw_board(fen)
