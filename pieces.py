"""
pieces.py
Classes for each piece
"""

__author__ = "Charlie Brunold"
__version__ = "2023-04-08"

class Pawn():
    def __init__(self, color):
        self.VALUE = 1
        self.color = color
        self.location = None
    
    def set_location(self, coordinate):
        self.location = coordinate
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Pawn[value={self.VALUE}, color={self.color}, location={self.location}]")

class King():
    def __init__(self, color):
        self.VALUE = -1
        self.color = color
        self.location = None
    
    def set_location(self, coordinate):
        self.location = coordinate
    
    def move(self):
        pass

    def __repr__(self):
        return(f"King[value={self.VALUE}, color={self.color}, location={self.location}]")

class Queen():
    def __init__(self, color):
        self.VALUE = 9
        self.color = color
        self.location = None
    
    def set_location(self, coordinate):
        self.location = coordinate
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Queen[value={self.VALUE}, color={self.color}, location={self.location}]")

class Bishop():
    def __init__(self, color):
        self.VALUE = 3
        self.color = color
        self.location = None
    
    def set_location(self, coordinate):
        self.location = coordinate
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Bishop[value={self.VALUE}, color={self.color}, location={self.location}]")

class Knight():
    def __init__(self, color):
        self.VALUE = 3
        self.color = color
        self.location = None
    
    def set_location(self, coordinate):
        self.location = coordinate
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Knight[value={self.VALUE}, color={self.color}, location={self.location}]")

class Rook():
    def __init__(self, color):
        self.VALUE = 5
        self.color = color
        self.location = None
    
    def set_location(self, coordinate):
        self.location = coordinate
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Rook[value={self.VALUE}, color={self.color}, location={self.location}]")