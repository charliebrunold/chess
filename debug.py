"""
debug.py
Jolly testing space
"""

__author__ = "Charlie Brunold"
__version__ = "2023-04-08"

from board import *
from pieces import *

def main():
    test_board = Board("white")
    test_board.display_coordinates()
    test_board.display_gamestate()
    test_board.initialize_game()
    print()
    test_board.display_gamestate()


if __name__ == "__main__":
    main()