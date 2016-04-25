class Piece:
    def __init__(self, name, color):
        self.name = name
        self.fore_color = color[0]
        self.back_color = color[1]
        self.value = '  '

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.fore_color + self.back_color + self.value
