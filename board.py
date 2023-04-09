"""
board.py
Board class
"""

__author__ = "Charlie Brunold"
__version__ = "2023-04-08"

class Board():
    def __init__(self, view="white"):
        if view.lower() == "black":
            coordinates = self.sort_coordinates(view)
        else:
            coordinates = self.sort_coordinates("white")
        piece_locations = ["x" for _ in range(64)]
        self.board = {coordinates:piece_locations for coordinates, piece_locations in zip(coordinates, piece_locations)}
         
    def display_coordinates(self):
        i = 0
        for space in self.board:
            print(f"{space}".center(2), end=' ')
            i += 1
            if i == 8:
                print("")
                i = 0
    
    def display_gamestate(self):
        i = 0
        for piece in self.board.values():
            print(f"{piece}".center(2), end=' ')
            i += 1
            if i == 8:
                print("")
                i = 0
    
    def sort_coordinates(self, view):
        coordinates = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
        if view.lower() == "black":
            better_coords = sorted(coordinates, key= lambda sub : sub[0], reverse=True)
            better_coords = sorted(better_coords, key= lambda sub : sub[1])
        else:
            better_coords = sorted(coordinates, key= lambda sub : sub[1], reverse=True)
        return(better_coords)
                           
    def __repr__(self):
        return (f"Board[board={self.board}]")