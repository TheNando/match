from copy import copy
from colorama import Style
import random


class Board:
    def __init__(self, rows, cols, pieces):
        self.rows = rows
        self.cols = cols
        self.pieces = pieces

        self.grid = {}

        for x in range(self.cols):
            for y in range(self.rows):
                self.grid[x, y] = None

    def fill_board(self):
        for row, col in self.grid:
            self.grid[row, col] = copy(random.choice(self.pieces))

    def swap_pieces(self, p1, p2):
        self.grid[p1], self.grid[p2] = self.grid[p2], self.grid[p1]

    def print(self):
        for y in range(self.rows):
            row_string = ''
            for x in range(self.cols):
                row_string += str(self.grid[x, y])

            print(row_string + Style.RESET_ALL)
        print()

    def print_matches(self, matches):
        match_grid = {}
        for match in matches:
            x = match[0]
            y = match[1]
            direction = match[2]
            piece = matches[match][0]
            while matches[match]:
                match_grid[x, y] = piece
                x += (direction == 'h') and 1 or 0
                y += (direction == 'v') and 1 or 0
                matches[match].pop()

        for y in range(self.rows):
            row_string = ''
            for x in range(self.cols):
                if (x, y) in match_grid:
                    row_string += str(match_grid[x, y])
                else:
                    row_string += Style.RESET_ALL + '  '

            print(row_string + Style.RESET_ALL)
        print()

    def find_matches(self):

        matches = {}
        h_matches = {}
        v_matches = {}

        for y in range(self.rows):
            for x in range(self.cols):
                xd = x + 1
                matches[x, y, 'h'] = [self.grid[x, y]]

                while (not (x, y) in h_matches and
                        xd < self.cols and
                        self.grid[x, y].name == self.grid[xd, y].name):
                    matches[x, y, 'h'].append(self.grid[xd, y])
                    h_matches[xd, y] = None
                    xd += 1

                if len(matches[x, y, 'h']) < 3:
                    matches.pop((x, y, 'h'), None)

                yd = y + 1
                matches[x, y, 'v'] = [self.grid[x, y]]

                while (not (x, y) in v_matches and
                        yd < self.rows and
                        self.grid[x, y].name == self.grid[x, yd].name):
                    matches[x, y, 'v'].append(self.grid[x, yd])
                    v_matches[x, yd] = None
                    yd += 1

                if len(matches[x, y, 'v']) < 3:
                    matches.pop((x, y, 'v'), None)

        return matches
