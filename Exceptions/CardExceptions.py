
class CardException(Exception):
    pass

class CardParameterException(CardException):
    # if a card has a bad argument when it is initiated
    pass

class CardFunctionParameterException(CardException):
    # if a card has a bad argument inside one of its functions
    pass
