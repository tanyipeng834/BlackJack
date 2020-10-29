""" This is a BlackJack Game that competes with the dealer with the aim
    to have a higher card value than the dealer but not exceeding 21.
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
        # Start the game by building and shuffling the deck
        self.build_deck().shuffle()

    @property
    def cards(self):
        return self.__cards

    def build_deck(self):
        """Build a deck of 48 cards with values from 0 to 11
           and suits from suits_available
        """
        for suits in Card.suits_available:
            for i in range(1, 12):
                self.cards.append(Card(suits, i))
        return self

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


class Player:
    """ A class that is used to describe a player in this blackjack game

        . . .

        Attributes
        _ _ _ _ _
        name:str
            name of player
        is_dealer:bool
            check if player is dealer
        hand:list
            hand of cureent player

        Methods
        _ _ _ _
        draw_card(self)
            Player draws card from the top of deck
        show_hand(self, is_dealer=False)
            Players and dealers show hand
    """
    def __init__(self, name, is_dealer=False):
        self.__name = name
        self.__is_dealer = is_dealer
        self.__hand = []

    @property
    def name(self):
        return self.__name

    @property
    def hand(self):
        return self.__hand

    @property
    def is_dealer(self):
        return self.__is_dealer

    def draw_card(self):
        """Draws the top card from deck
        """
        self.hand.append(deck.draw_top_card())
        return self

    def show_hand(self, reveal_card=False):
        """ Show hand of player every turn, while dealer shows all cards
            except last card unless it is time to reveal cards
        """
        if not self.is_dealer:
            # Print entire hand of player
            for card in self.hand:
                print(str(card))
        else:
            # Print entire hand of dealer except last card
            for i in range(0, len(self.hand)-1):
                print(str(self.hand[i]))
            if reveal_card:
                # Print last card when it is time to reveal cards
                print(str(self.hand[-1]))
            else:
                # Keep last card hidden
                print("X")

    def check_value(self):
        """ Check total value of cards in current hand
        """
        value = 0
        for card in self.hand:
            value += card.value
        return value

    def turn_choice(self):
        """Player hace 2 options To draw card or to stand
        """
        option = int(input("Press 1 to Stand or 2 to Draw Card\n"))
        if option == 1:
            return option
        else:
            # player draw card and shows the card
            self.draw_card().show_hand()
            return option


class Game:
    """ A class that is used to describe a BlackJack Game

        ...

        Attributes
        _ _ _ _ _ _
        deck:Deck object
            A deck of cards that has been created
        dealer:Player object
            A player that has been created to play against the player
        player:Player obkect
            A player that will win the dealer if he or
            she has a higher value than the dealer but below the value of 21.

        Methods
        _ _ _ _
        start_game(self)
            Player and dealer start the game based on turns and compete
            who has the higher value but it must remain below 21 to remain
            victorious.
    """
    INSTRUCTIONS = """  | Welcome to our version of the Blackjack Game |

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

    def __init__(self, deck, dealer, player):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.turn = 1
        self.start_game()

    def start_game(self):
        """Game of BlackJack starts and player will have an option to
           stand or draw card to beat the dealer
        """
        print(Game.INSTRUCTIONS)
        self.player.draw_card().draw_card()
        self.dealer.draw_card().draw_card()
        while True:
            print(f"========== Turn #{self.turn} ==========")
            print("The Dealer's Hand is")
            dealer.show_hand()
            print("Your Hand is")
            player.show_hand()
            if player.check_value() == 21:
                print("You Have Won The Game")
                break
            elif player.check_value() > 21:
                print("Your hand has exceeded 21 , You have lost the game")
                break
            else:
                option = self.player.turn_choice()
                if option == 1:
                    print("The dealer's Card Was")
                    self.dealer.show_hand(reveal_card=True)
                    if self.player.check_value() > self.dealer.check_value():
                        print("You have Won the Game")
                        break
                    elif self.player.check_value() < self.dealer.check_value():
                        print("You have Lost The Game")
                        break
                    else:
                        print("Tie")
                        break
                else:
                    self.turn += 1

# Create a deck of cards
deck = Deck()
# Create a player called John
player = Player("John")
# Create a dealer called Tom
dealer = Player("Tom", is_dealer=True)
# Create and Start a Game
game = Game(deck, dealer, player)
