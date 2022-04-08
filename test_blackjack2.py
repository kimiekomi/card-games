#! /usr/bin/env python3

from blackjack2 import *
from cards import *

Burn_Card = Ace_of_Hearts

dealer_gets_blackjack = [Burn_Card, Ten_of_Spades, Ten_of_Diamonds, Five_of_Spades, Ace_of_Clubs]
player_gets_blackjack = [Burn_Card, Ten_of_Spades, Ten_of_Diamonds, Ace_of_Spades, Five_of_Clubs]
player_dealer_gets_blackjack = [Burn_Card, Ten_of_Spades, Ten_of_Diamonds, Ace_of_Spades, Ace_of_Clubs]
dealer_shows_ace = [(), Ten_of_Spades, Ten_of_Diamonds, Five_of_Spades, Ace_of_Clubs, Five_of_Hearts]

player_gets_21 = [(), Ten_of_Spades, Ten_of_Diamonds, Five_of_Spades, Ten_of_Clubs, Six_of_Hearts]
player_gets_pair = [(), Five_of_Clubs, Ten_of_Diamonds, Five_of_Spades, Ten_of_Clubs, Six_of_Hearts]

Tests = [
    ("player gets a pair", player_gets_pair),
    ("player hits to 21", player_gets_21),

    ("dealer blackjack", dealer_gets_blackjack),
    ("player blackjack", player_gets_blackjack),
    ("dealer shows an ace", dealer_shows_ace)
]


if __name__ == "__main__":

    for test in Tests:
        print (f"test: {test[0]}\n")
        play(test[1].copy())
        print ("\n")

        while True:
            repeat = input ("repeat test? " ).lower()

            if repeat != "y": break

            play_hand(test[1].copy())

            print ()
