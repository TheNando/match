from piece import Piece
from board import Board
from colorama import Fore, Back, init


class Game:
    def __init__(self):
        pieces = [
            Piece('r', (Fore.WHITE, Back.RED)),
            Piece('b', (Fore.BLACK, Back.BLUE)),
            Piece('g', (Fore.BLACK, Back.GREEN)),
            Piece('m', (Fore.BLACK, Back.MAGENTA)),
            Piece('c', (Fore.BLACK, Back.CYAN)),
            Piece('w', (Fore.BLACK, Back.WHITE))
        ]
        self.board = Board(8, 8, pieces)
        self.board.fill_board()
        self.board.print()
        matches = self.board.find_matches()
        self.board.print_matches(matches)


if __name__ == '__main__':
    init()
    game = Game()
