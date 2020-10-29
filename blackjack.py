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


class Deck:
    """ A class that is used to represent 52 cards in a deck
        of poker cards

        . . .

        Attributes
        _ _ _ _ _
        cards: list
            Cards that are in the current deck created

        Methods
        _ _ _ _
        build_deck(self)
            Build a deck of cards with value ranging from
            0 to 11 and available suits
    """
    def __init__(self):
        self.__cards = []
        self.build_deck()

    @property
    def cards(self):
        return self.__cards

    def build_deck(self):
        for suits in Card.suits_available:
            for i in range(0, 12):
                self.cards.append(Card(suits, i))

    def shuffle(self):
        """Implement a shuffling alogithm on the cards
        """
        for i in range((len(self.cards)-1), 0, -1):
            rand = random.randint(0, i)
            # swap current cards with random cards
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[rand]

    def draw_top_card(self):
        """Player draws top card
        """
        return self.cards.pop()


deck = Deck()
