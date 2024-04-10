from random import randint
scores = {"computer": 0, "player": 0}


class Board:
    def __init__(self, size, num_ships, name, board_type):
    self.size = size
    self.board = [["." for _ in range(size)] for _ in range(size)]