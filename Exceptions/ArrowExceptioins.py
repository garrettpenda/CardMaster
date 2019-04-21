class ArrowException(Exception):
    pass

class ArrowParameterException(ArrowException):
    # if a card has a bad argument when it is initiated
    pass

class ArrowFunctionParameterException(ArrowException):
    # if a card has a bad argument inside one of its functions
    pass