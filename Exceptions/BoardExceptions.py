

class BoardException(Exception):
    pass

class OutOfBoardException(BoardException):
    pass

class InvalidBoardException(BoardException):
    pass

class BoardCombatException(BoardException):
    pass