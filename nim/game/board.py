import random

# TODO: Define the Board class here

class Board:
    """The game board. Displays the board and updates itself after every move.
    
    Stereotype: 
        Information Holder

    Attributes:
        _piles (list): List of piles containing different numbers of stones.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """    
        self._piles = []
        self.__prepare()

    def __prepare(self):
        """Sets random values to the number of piles and stones.
        
        Args:
            self (Board): An instance of Board.
        """
        num_piles = range(random.randint(2, 5))
        for n in num_piles:
            self._piles.append(random.randint(1, 9))

    def apply(self, move):
        """Updates the number of stones on a player-selected pile.
        
        Args:
            self (Board): An instance of Board.
            move (Move): An instance of Move.
        """
        pile = self._piles[move.get_pile()]
        self._piles[move.get_pile()] = pile - move.get_stones()

    def is_empty(self):
        """Checks if the board is empty.
        
        Args:
            self (Board): An instance of Board.
        """
        empty_board = [0] * len(self._piles)
        return empty_board == self._piles

    def to_string(self):
        """Converts the board representation to a string to be displayed on the screen.
        
        Args:
            self (Board): An instance of Board.
        """
        board_string = '\n--------------------'
        for x in self._piles:
            stones = ''
            if x > 0:
                stones = x * ' O'
            index = self._piles.index(x)
            board_string += '\n' + str(index) + ':' + stones
        board_string += '\n--------------------'
        return board_string
