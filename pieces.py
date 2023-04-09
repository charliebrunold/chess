"""
pieces.py
Classes for each piece
"""

__author__ = "Charlie Brunold"
__version__ = "2023-04-08"

class Pawn():
    def __init__(self, color, location):
        self.VALUE = 1
        self.color = color
        self.location = location
    
    def set_location(self, coordinate):
        self.location = coordinate

    def get_location(self):
        return (self.location)
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Pawn[value={self.VALUE}, color={self.color}, location={self.location}]")
    
    def __str__(self):
        return(f"{self.color.lower()[0]}P")

class King():
    def __init__(self, color, location):
        self.VALUE = -1
        self.color = color
        self.location = location
    
    def set_location(self, coordinate):
        self.location = coordinate

    def get_location(self):
        return (self.location)
    
    def move(self):
        pass

    def __repr__(self):
        return(f"King[value={self.VALUE}, color={self.color}, location={self.location}]")
    
    def __str__(self):
        return(f"{self.color.lower()[0]}K")

class Queen():
    def __init__(self, color, location):
        self.VALUE = 9
        self.color = color
        self.location = location
    
    def set_location(self, coordinate):
        self.location = coordinate

    def get_location(self):
        return (self.location)
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Queen[value={self.VALUE}, color={self.color}, location={self.location}]")
    
    def __str__(self):
        return(f"{self.color.lower()[0]}Q")

class Bishop():
    def __init__(self, color, location):
        self.VALUE = 3
        self.color = color
        self.location = location
    
    def set_location(self, coordinate):
        self.location = coordinate

    def get_location(self):
        return (self.location)
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Bishop[value={self.VALUE}, color={self.color}, location={self.location}]")
    
    def __str__(self):
        return(f"{self.color.lower()[0]}B")

class Knight():
    def __init__(self, color, location):
        self.VALUE = 3
        self.color = color
        self.location = location
    
    def set_location(self, coordinate):
        self.location = coordinate

    def get_location(self):
        return (self.location)
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Knight[value={self.VALUE}, color={self.color}, location={self.location}]")
    
    def __str__(self):
        return(f"{self.color.lower()[0]}N")

class Rook():
    def __init__(self, color, location):
        self.VALUE = 5
        self.color = color
        self.location = location
    
    def set_location(self, coordinate):
        self.location = coordinate

    def get_location(self):
        return (self.location)
    
    def move(self):
        pass

    def __repr__(self):
        return(f"Rook[value={self.VALUE}, color={self.color}, location={self.location}]")
    
    def __str__(self):
        return(f"{self.color.lower()[0]}R")