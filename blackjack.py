"""  | Welcome to our version of the Blackjack Game |

=================================================================================

The goal is to get as close to 21 as possible, without going over 21.

Each card has a value and a suit. The values are added for the final result.



The game starts by dealing two cards to the player (you) and to the dealer.

You are playing against the dealer. On each turn, you must choose if you

would like to take another card or stand to stop the game and see if you won.



The game ends if the total value of the player's hand goes over 21,

and if the total value of the hand is below 21, the game continues

until the player chooses to stand.



When the game ends or when the player chooses to stand,

the total value of each hand is calculated.

The value that is closest to 21 without going over it wins the game.

If the total value is over 21, the player or dealer

automatically lose the game.

=================================================================================
"""


import random


class Card:
    """ A class that is used to represent a card that is used in BlackJack

        . . .

    Attributes
    _ _ _ _ _
    suit:string
        The suit of a BlackJack card
    value:int
        Value of card from Ace to a Picture card that
        is represented from 0 to 11

    Methods
    _ _ _ _
    __str__(self)
        A string representaion of a card.
    """
    suits_available = ["Spade", "Heart", "Club", "Diamond"]

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    @property
    def suit(self):
        """ A method to get current card suit
        """
        return self.__suit

    @suit.setter
    def suit(self, suit):
        # Check if suit is a suit available
        if suit not in Card.suits_available:
            raise Exception("Card Suit Not Available")
        else:
            self.__suit = suit

    @property
    def value(self):
        """A method to get current card value
        """
        return self.__value

    @value.setter
    def value(self, value):
        # Check if suit is a suitable value
        if not 11 > value > 1:
            raise Exception("Value Not Available")
        else:
            self.__value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


card = Card("Spade", 11)
print(str(card))

